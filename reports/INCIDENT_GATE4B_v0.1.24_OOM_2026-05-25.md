# Gate 4B v0.1.24 OOM Incident — 2026-05-25

## 1. Summary

v0.1.24 corrected Gate 4B rerun was attempted on Hetzner CPX42.
The Python process was killed by Linux OOM killer during batch 1 at the first heavy N=128, j_max=3 case.
No scientific verdict can be made from this failed run.

This is an infrastructure failure, recorded for traceability. The corrected S³ Dirac operator (negative k=0 branch restored, λ = −3/2 present) has NOT been evaluated end-to-end yet.

## 2. Evidence

Raw facts collected from the server (Hetzner CPX42, `ape-2026`, <user>@<hetzner-server-ip>, tmux session `geospectra_gate4b`):

- timestamp: **May 25 11:45:21** (server UTC)
- killed process: **python** (PID 1002566)
- total-vm: **~15.8 GiB** (`15 796 904 kB`)
- anon-rss: **~10.5 GiB** (`11 004 124 kB`)
- file-rss: 0 kB
- shmem-rss: 0 kB
- swap: **0** (`SwapTotal: 0 kB`, `Free swap = 0 kB`)
- server total RAM: **~15 GiB** (`MemTotal: 15 979 328 kB`)
- already-used RAM by other services: **~4.4 GiB** (`free -h` snapshot during diagnostics)
- failure occurred around case `[22/24]`, **N=128, j_max=3, seed=123** (batch 1 = `spectral_circle W=0`)
- tmux session `geospectra_gate4b` survived; shell returned to prompt
- python rerun process is gone (not visible in `ps -eo pid,etime,...`)
- `reports/RUNS/gate4_fss_v0.1.24/batches/` directory was NEVER created
- only `reports/RUNS/gate4_fss_v0.1.24/config.json` (703 B) exists on disk for v0.1.24
- run log `reports/RUNS/gate4_fss_v0.1.24_run.log`:
  - mtime `2026-05-25 11:41:08.383657900 +0000`
  - size 1778 bytes, 39 lines
  - last line truncated mid-case: `[22/24] N=128 j_max=3 seed=123 ...`

Raw kernel trace from journalctl:

```
May 25 11:45:21 ape-2026 kernel: Out of memory: Killed process 1002566 (python)
  total-vm:15796904kB
  anon-rss:11004124kB
  file-rss:0kB
  shmem-rss:0kB
  UID:0
  pgtables:27580kB
  oom_score_adj:0

May 25 11:45:21 ape-2026 kernel: Mem-Info:
  active_anon:23647  inactive_anon:3833511
  free:33762  free_pcp:0  free_cma:0
  Total swap = 0kB
  Free swap  = 0kB
  4094792 pages RAM
  99960 pages reserved

May 25 11:45:26..11:49:57 ape-2026 sshd: kex_exchange_identification:
  Connection closed by remote host  (×22, while kernel recovered memory)
```

Call site of the kill (page-fault during allocation growth):

```
out_of_memory+0x106/0x2e0
__alloc_pages_slowpath.constprop.0+0x907/0xb80
__alloc_pages+0x311/0x330
alloc_pages_vma+0x9d/0x390
do_anonymous_page+0xf2/0x3c0
handle_mm_fault+0xd8/0x2c0
do_user_addr_fault+0x1c9/0x640
```

The kill happened inside an `mmap` page-fault, NOT inside `malloc()` — this is why no Python `MemoryError` was raised and no Python traceback reached the run log. The process was terminated by the kernel before user-space could observe the allocation failure.

## 3. Root Cause

Dense Hermitian `scipy.linalg.eigh` memory peak exceeded available RAM.

Matrix dimensions for **N=128, j_max=3**:

- Hilbert dimension ≈ **7680** (N × S³_dim where S³_dim = 60 for corrected operator with j_max=3)
- dense complex matrix storage ≈ **0.94 GiB** (`7680² × 16 B`)
- eigenvectors matrix `Q` (returned by `eigh`) ≈ **0.94 GiB** (same size)
- LAPACK/OpenBLAS workspace and temporary arrays significantly increase peak memory:
  - typical `?heevr`/`?syevd` workspace is 2–4× the input matrix
  - with `OPENBLAS_NUM_THREADS=4`, per-thread workspaces multiply
  - intermediate copies during real/complex conversions add transient peaks
- practical peak ≈ **9–12 GiB** resident anonymous memory
- available free RAM was approximately **~10 GiB** (15 GiB total − 4.4 GiB used by other services on the host)
- no swap existed (`SwapTotal: 0 kB`)
- kernel OOM killer terminated the process when anonymous allocation could not be satisfied from free pages

Earlier cases in batch 1 (N=16, 32, 64) ran comfortably (max 38 s, modest RSS). The transition to N=128 j_max=3 was a structural memory cliff specific to this point in the grid.

## 4. Impact

- v0.1.24 rerun incomplete (0 of 9 batches finished; 21 of 216 cases were computed successfully but in-memory only)
- no scientific verdict
- no batch results persisted to disk
- successful in-memory cases (21 cases from batch 1 covering N=16, 32, 64 and N=128 j_max=2) were lost because the runner persisted only at batch completion, never at case completion
- v0.1.21 outputs untouched (output namespace isolation guards from commit `4b77684` worked correctly)
- Gate 4B interpretation remains frozen
- Negative Controls (v0.1.22 batches 3–6) remain paused
- downstream items (Gate 5, W-sweep, comparison report v0.1.21↔v0.1.24, methodology paper update) remain blocked

## 5. What Was Not Affected

- repository state clean (`main == origin/main` at `4b77684`, no unexpected code changes)
- old v0.1.21 outputs preserved (`reports/RUNS/gate4_fss_v0.1.21/` and related artifacts intact)
- server survived (no reboot; uptime continued; other services on the host — VeriFind uvicorn, GeoMiro, BLI-2, nginx — continued running)
- no evidence of physics failure
- no evidence of S³ Dirac fix failure from this incident alone (targeted unit tests `tests/cc_toy_lab/spectral/test_dirac_s3_branches.py` remain 6/6 PASS, independent of this incident)
- pre-registered rerun protocol (commit `1f4173c`) intact

## 6. Non-Scientific Status

This is an infrastructure failure, not a physics result.

Do **not** interpret this OOM as pass, fail, weakening, or disappearance of the Gate 4B signal.

The corrected operator was never evaluated end-to-end. The 21 in-memory cases that succeeded before the kill cannot be used as a partial signal because they cover only the lower portion of the FSS grid (no N=128 j_max=3 datapoint reached completion).

Forbidden interpretations of this incident:

- ❌ "v0.1.24 confirmed"
- ❌ "v0.1.24 failed"
- ❌ "Gate 4B final"
- ❌ "signal disappeared"
- ❌ "signal preserved"
- ❌ "S³ fix broke the harness"

## 7. Lessons Learned

- **Persistence boundary was wrong.** Saving only at batch completion (24 cases / batch) caused loss of 21 successful in-memory cases. Persistence must move from batch level to case level.
- **Memory estimation must be done before heavy dense eigensolver runs.** Peak RSS for `N=128 j_max=3` was not measured in advance; the run was started on a 15 GiB host where peak alone could approach available memory.
- **Smoke test should target the heaviest case first.** Running cases in ascending order (N=16 → N=128) meant the OOM hit only after several hours' confidence-building on cheap cases; a heaviest-case-first smoke would have caught the memory cliff in minutes.
- **Long-running tmux jobs without heartbeat are blind.** The process died at 11:45; the silence was noticed only the next day. A simple touch-file canary every N minutes would have surfaced the failure within ~30 minutes.
- **Hetzner CPX-series (shared vCPU) is the wrong tier for sustained scientific eigh workloads.** Even when RAM appears sufficient, lack of swap + cohabitation with other memory-heavy services makes OOM inevitable on the heaviest case.

## 8. Options Considered

| Option | Pros | Cons | Status |
|---|---|---|---|
| **A. Add swap** | may prevent immediate kill | dense eigh in swap may be extremely slow (5–10× slowdown, potential I/O timeouts, cases could take hours each) | not preferred as primary solution |
| **B. Reduce N_max / skip N=128** | avoids OOM | changes protocol (pre-registered grid locked at commit `1f4173c`) and weakens FSS comparison; requires explicit pre-registration amendment | not preferred without explicit decision |
| **C. Move to 64–128 GB RAM server** | correct infrastructure solution; preserves locked grid; allows downstream items to resume on the same host | cost/setup overhead | preferred |
| **D. Redesign solver / sparse eigensolver** | possible long-term efficiency (`scipy.sparse.linalg.eigsh` with `k=top_k`); reduced memory footprint | changes numerical method; requires independent validation that top-k captures the IPR signal; protocol-level decision | future protocol decision, not immediate fix |

## 9. Recommendation

Use a **64–128 GB RAM machine** for v0.1.24 corrected rerun.

Before rerun:

- implement per-case checkpointing;
- run heavy smoke case first (N=128, j_max=3 in isolation) to measure real peak RSS on the corrected operator;
- limit BLAS threads (`OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS`, `NUMEXPR_NUM_THREADS`) to a conservative value matching the machine and the heaviest case's safety margin;
- save outputs after every case (atomic write + fsync), not after every batch;
- only then run the full rerun.

Detailed plan: `reports/MEMORY_SAFE_RERUN_PLAN_v0.1.24.md`.

## 10. Forbidden Actions

- Do not rerun unchanged on the current 15 GB server.
- Do not resume Negative Controls (batches 3–6).
- Do not make a scientific verdict from this incident.
- Do not delete old outputs (`reports/RUNS/gate4_fss_v0.1.21/`, partial `reports/RUNS/gate4_fss_v0.1.24/`).
- Do not change the protocol silently.
- Do not run a full rerun without per-case checkpointing.
- Do not modify the S³ Dirac operator (`cc_toy_lab/spectral/dirac_s3.py` at commit `093573b`).
- Do not modify the IPR metric (`v0.1.24_true_ipr_corrected_s3_dirac`).
- Do not modify the pre-registered grid (commit `1f4173c`).
- Do not communicate any scientific verdict externally (papers, grants, CAMP, social).

## 11. Status

```
SERVER_RERUN_OOM_CONFIRMED
NO_SCIENTIFIC_VERDICT
MEMORY_SAFE_RERUN_REQUIRED
```

---

**Recorded:** 2026-05-27 (incident occurred 2026-05-25 11:45:21 server UTC).
**Next action:** await user decision on hardware migration (Option C). See `reports/MEMORY_SAFE_RERUN_PLAN_v0.1.24.md` for the prerequisite design before any rerun attempt.
