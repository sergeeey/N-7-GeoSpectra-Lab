# Memory-Safe Rerun Plan — Gate 4B v0.1.24

## 1. Purpose

Prepare a safe rerun strategy for corrected Gate 4B v0.1.24 after the OOM failure on the 15 GB server documented in `reports/INCIDENT_GATE4B_v0.1.24_OOM_2026-05-25.md`.

This document is a **design only**. It does not authorize any rerun, code change, commit, or push. It captures the prerequisites that must be in place before any v0.1.24 rerun is attempted, and the decision rules that govern interpretation after the rerun completes.

## 2. Current Blocker

- OOM occurred on N=128, j_max=3 dense eigendecomposition (May 25 11:45:21, anon-rss ~10.5 GiB on 15 GiB host with no swap)
- no per-case checkpointing — 21 in-memory successful cases were lost when the kernel killed the process
- no scientific verdict (this was an infrastructure failure, not a physics result)
- rerun must not restart unchanged on the same host with the same runner

## 3. Required Preconditions Before Any Full Rerun

All nine items must be in place. Order of items is implementation order:

1. **Per-case checkpointing implemented and tested** — runner writes a per-case artifact immediately after each `eigh` completes; verified locally on a small case grid.
2. **Heavy smoke case protocol defined** — N=128, j_max=3 isolated smoke documented with success/failure criteria and acceptance threshold for peak RSS.
3. **64–128 GB RAM machine available** — provisioned, accessible via ssh, free of memory-heavy cohabitating services for the duration of the run.
4. **BLAS thread limits configured** — `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS`, `NUMEXPR_NUM_THREADS` set to a documented value matching the machine; verified via `OPENBLAS_NUM_THREADS=$OPENBLAS_NUM_THREADS` echo in the tmux session.
5. **Output namespace verified** — `--output-base reports/RUNS/gate4_fss_v0.1.24`, `--protocol-version v0.1.24`, `--ipr-metric-version v0.1.24_true_ipr_corrected_s3_dirac`; guards in commit `4b77684` confirmed by dry-run.
6. **Old v0.1.21 outputs protected** — `reports/RUNS/gate4_fss_v0.1.21/` exists on the target machine (or on a read-only mirror) for any comparison work; runner must refuse to write into the v0.1.21 namespace.
7. **Resume behavior tested** — runner skips already completed per-case artifacts on `--resume`; verified by killing the smoke case mid-run and observing correct restart.
8. **Rerun command documented** — exact final command line frozen in this document and in the pre-rerun memory note, including all flags, env vars, and tmux session name.
9. **Backup/export procedure documented** — how to pull per-case artifacts from the rerun host to local before/during/after the run; includes git push behavior for partial result indexes if any are committed.

## 4. Recommended Compute

**Preferred:**

- 128 GB RAM
- 16–32 CPU cores
- NVMe disk
- clean machine, no unrelated memory-heavy services (no co-tenant uvicorn, no co-tenant Next.js build, no co-tenant TimescaleDB)

**Acceptable minimum:**

- 64 GB RAM
- 16 CPU cores
- heavy smoke case required before full rerun (no exceptions)

**GPU:**

- not required for the current `scipy.linalg.eigh` path
- GPU acceleration (CuPy) is a separate future validation track and is not the immediate solution to this OOM
- introducing GPU now would change the numerical pipeline mid-rerun and is forbidden

## 5. Environment Settings

Proposed environment for the rerun tmux session:

```bash
export OMP_NUM_THREADS=4
export OPENBLAS_NUM_THREADS=4
export MKL_NUM_THREADS=4
export NUMEXPR_NUM_THREADS=4
```

Rationale: on a 16-core target machine, 2–4 BLAS threads per process keep per-thread workspaces bounded while still using all cores when multiple processes run in parallel. If running a single sequential process (one case at a time), 4 threads is a safe default; if running multiple cases in parallel, drop to 1–2 threads per case to avoid thread-workspace multiplication.

Final thread count must be re-measured during the heavy smoke case (Section 7) and the documented number must be the one used in the full rerun. No silent thread-count changes after smoke pass.

## 6. Per-Case Checkpointing Requirement

Current batch-level persistence lost 21 successful cases. New rule:

> one case completed → immediately write JSON/NPZ result → fsync/flush → mark complete

Required behavior:

- **Skip already completed cases on resume.** Runner reads the case artifact index on startup and skips any case whose artifact passes integrity check.
- **Never overwrite a valid case unless `--force`.** Default is to refuse overwriting; explicit override required for re-computation.
- **Write temp file then atomic rename.** Pattern: write to `case_<idx>.json.tmp`, fsync, rename to `case_<idx>.json`. This prevents half-written artifacts on kill.
- **Include reproducibility envelope in every case artifact:**
  - git commit hash
  - operator parameters (N, j_max, family, W, alpha, seed, q)
  - timestamp (UTC start, UTC end)
  - runtime (wall and CPU)
  - metrics (true IPR, r-stat, peak RSS sample if available)
  - python/scipy/numpy versions
- **Record failure as an explicit failed-case artifact.** If a case raises or is killed before write, the next runner invocation must be able to detect "missing case" vs "failed case" — failure artifact is `case_<idx>.failed.json` with reason, exit code, and last known state.

Implementation work for these behaviors is a separate task; it is NOT part of this plan. This plan only fixes the requirements.

## 7. Heavy Smoke Test

The first action on the new machine, after preconditions 1–9, is a single heavy smoke case run in isolation.

**Smoke case parameters:**

- N = 128
- j_max = 3
- seed = 123
- family = `spectral_circle` (first family encountered in batch 1; same family/parameters as the failed heavy case)
- corrected S³ Dirac operator (commit `093573b`)
- IPR metric v0.1.24 (`v0.1.24_true_ipr_corrected_s3_dirac`)
- output to a separate smoke namespace, e.g. `reports/RUNS/gate4_smoke_v0.1.24/`

**Smoke success criteria** (all must hold):

- process completes (no SIGKILL, no Python exception)
- result file written and atomically renamed to final name
- peak resident memory acceptable (documented threshold ≤ 50% of machine RAM, e.g. ≤ 32 GiB on a 64 GiB machine, ≤ 64 GiB on a 128 GiB machine)
- metrics present in the artifact (true IPR, r-stat both populated and within sanity bounds)
- no OOM events in `dmesg -T` during or after run
- no corruption indicators (file passes integrity check; ASCII-readable JSON parts parse)
- runtime recorded (and reasonable: minutes, not days)

**If smoke fails:**

- do not full rerun
- choose larger RAM or solver strategy (Option C or D from incident report Section 8)
- do not modify operator, metric, or grid to make smoke pass

**If smoke passes:**

- proceed to Section 8 (full rerun strategy) only after explicit user authorization
- do not auto-chain smoke → full rerun

## 8. Full Rerun Strategy

After smoke passes and user authorizes:

- run batch-by-batch or case-by-case (case-level preferred given per-case checkpointing)
- checkpoint after every case (Section 6 contract)
- monitor memory (background process logging `/proc/self/status` or `psutil` peak RSS to a heartbeat file every 60 s)
- keep tmux session (no `nohup` alone — tmux survives disconnect AND allows interactive attach for inspection)
- periodic backup (rsync per-case artifacts to a second location every N hours; backup runs from a separate ssh session, not from inside the tmux)
- do not run unrelated services if possible (no nginx/uvicorn/etc on the same host for the rerun window; if cohabitation is unavoidable, document peak RSS budget per service before start)

**Rerun command (proposed final form, to be frozen after smoke passes):**

```bash
python scripts/run_gate4_batched.py \
  --run-all \
  --output-base reports/RUNS/gate4_fss_v0.1.24 \
  --protocol-version v0.1.24 \
  --ipr-metric-version v0.1.24_true_ipr_corrected_s3_dirac \
  --resume \
  2>&1 | tee -a reports/RUNS/gate4_fss_v0.1.24_run.log
```

(Exact flag set depends on what `--resume` and per-case checkpointing are named after implementation. This is a placeholder shape, not an authorization to run.)

## 9. Result Comparison Plan

After the full rerun completes (all 216 cases or documented failure pattern), produce `reports/GATE_4B_v0.1.24_COMPARISON_v0.1.21_vs_v0.1.24.md` with:

- completed cases (per family, per N, per j_max)
- failure count and failure modes
- `true_ipr_mean` per cell
- `r_stat` per cell
- family contrasts (spectral_circle vs ring vs wilson_ring)
- aggregate contrast (W=20 vs W=0)
- finite-size trend (s1_size=16 → 128)
- whether the signal is preserved, weakened, disappeared, or technically inconclusive

**Allowed outcomes:**

1. Signal preserved (aggregate contrast and FSS trend consistent with v0.1.21 within documented tolerance)
2. Signal weakened but present (contrast reduced but still ≥2.0× with FSS not collapsing)
3. Signal disappeared (contrast below threshold or FSS collapse)
4. Rerun failed technically (insufficient cases for verdict; redo memory plan)

No scientific claim before full completed analysis. No partial-grid verdict. No "preliminary positive" wording.

## 10. Decision Rules After Rerun

**If signal preserved:**

- update Gate 4B status from "interpretation frozen" to "v0.1.24 confirmed"
- consider resuming Negative Controls (v0.1.22 batches 3–6)
- consider scheduling Gate 5 / W-sweep / T⁴ baseline per `docs/ROADMAP.md`

**If signal weakened:**

- caveat claims: explicitly note reduction; update `docs/CLAIMS_AND_CAVEATS.md`
- decide whether additional diagnostics are needed (more seeds, larger sizes, family-specific follow-up)
- do NOT communicate weakened result externally before independent re-audit

**If signal disappeared:**

- mark v0.1.21 as implementation-artifact candidate
- pivot to methodology / negative-result write-up
- update DOI / Zenodo with explicit retraction note for v0.1.21 interpretation
- preserve all original v0.1.21 outputs and all v0.1.24 outputs side by side

**If technical failure (rerun could not complete):**

- no scientific verdict
- revise infrastructure (Section 4) and rerun this plan
- do NOT downgrade to partial-grid verdict, even if "most cases" succeeded

## 11. Forbidden Actions

- no full rerun before per-case checkpointing is implemented and smoke-tested
- no Negative Controls before corrected Gate 4B decision is finalized
- no W-sweep before Gate 4B v0.1.24 verdict
- no Gate 5 before Gate 4B v0.1.24 verdict
- no external claim (paper, grant, social media, CAMP communication) about v0.1.24 outcome before comparison report Section 9 is written
- no Tom / CAMP validation wording — Tom's CAMP framing remains "we are waiting on corrected rerun"
- no operator code change (`cc_toy_lab/spectral/dirac_s3.py` stays at commit `093573b`)
- no IPR metric change
- no pre-registered grid change (commit `1f4173c` locked)
- no silent thread-count change after smoke passes
- no auto-chain smoke → full rerun without explicit user authorization

## 12. Final Recommendation

```
MEMORY_SAFE_RERUN_REQUIRED_BEFORE_SCIENTIFIC_VERDICT
```

Sequence to follow when user is ready to resume:

1. Provision 64–128 GB machine (Option C from incident report)
2. Implement per-case checkpointing (separate task, separate doc)
3. Run heavy smoke (Section 7) with explicit measurement of peak RSS and runtime
4. If smoke passes: freeze rerun command (Section 8) and request authorization
5. Full rerun with resume-on-restart and heartbeat monitoring
6. Comparison report (Section 9)
7. Decision per rules (Section 10)
8. Only after that — decide on Negative Controls / downstream items

---

**Recorded:** 2026-05-27.
**Status:** design only, no execution authorized.
**Pre-requisite document:** `reports/INCIDENT_GATE4B_v0.1.24_OOM_2026-05-25.md`.
**Pre-registered protocol locked at:** commit `1f4173c`.
**Operator pinned at:** commit `093573b`.
**Runner pinned at:** commit `4b77684`.
