# Pre-Rerun Checklist — Gate 4B v0.1.24 Corrected Rerun

**Date:** 2026-05-31  
**Source:** `reports/MEMORY_SAFE_RERUN_PLAN_v0.1.24.md` Section 3 (9 required preconditions)  
**Status:** ❌ NOT READY — 5/9 BLOCKING issues

---

## ✅ READY (4/9)

### ✅ 1. S³ Dirac operator corrected and tested
- **Status:** PASS
- **Evidence:**
  - Commit `093573b`: `fix(operator): restore S3 Dirac negative k0 branch`
  - Targeted tests: `pytest tests/cc_toy_lab/spectral/test_dirac_s3_branches.py -v` → 6/6 PASSED
  - Negative k=0 branch (λ=-3/2) present and verified
  - Hermiticity: PASS
  - Spectrum structure: PASS

### ✅ 2. Output namespace isolation guards in place
- **Status:** PASS
- **Evidence:**
  - Commit `4b77684`: `fix(gate-4b): parameterize batched rerun output namespace`
  - v0.1.21 outputs protected at `reports/RUNS/gate4_fss_v0.1.21/`
  - v0.1.24 namespace: `reports/RUNS/gate4_fss_v0.1.24` (separate directory)
  - CLI args: `--output-base`, `--protocol-version`, `--ipr-metric-version` implemented
  - Guard: runner refuses to write if `--output-base` already contains batches without `--force` or `--resume`

### ✅ 3. Pre-registered protocol locked
- **Status:** PASS
- **Evidence:**
  - Protocol commit: `1f4173c` (original v0.1.20 grid)
  - Protocol document: `reports/GATE_4B_RERUN_PROTOCOL_v0.1.24.md` (dated 2026-05-25)
  - Grid UNCHANGED: 216 cases (3 families × 3 W × 4 sizes × 2 j_max × 3 seeds)
  - ONLY metric corrected (eigvalsh → eigh), grid/thresholds unchanged

### ✅ 4. Git clean (modulo dev artifacts)
- **Status:** ACCEPTABLE
- **Evidence:**
  - Modified: `.claude/settings.local.json` (local config, not committed)
  - Untracked: `docs/OUTCOMES.md`, `hardware_requirements_calculation.md`, `PRE_RERUN_CHECKLIST.md` (new docs)
  - No uncommitted changes to operator code, runner, or tests
- **Action:** None required (dev artifacts don't affect rerun)

---

## ❌ BLOCKING (5/9)

### ❌ 1. Per-case checkpointing NOT implemented
- **Status:** FAIL — this is the #1 blocker
- **Current behavior:** Runner writes results ONLY at batch completion (24 cases / batch)
  - File: `scripts/run_gate4_batched.py` line 331: `json.dump(results, f)`
  - Write location: `batch_dir / "results.json"` (all 24 cases in one file)
  - OOM at case 22/24 → lost 21 in-memory cases
- **Required behavior:**
  - One case completed → immediately write `case_<id>.json` → fsync → mark complete
  - `--resume` skips already-completed cases (not just batches)
  - Atomic write: `case_<id>.json.tmp` → rename to `case_<id>.json`
  - Reproducibility envelope in EVERY case artifact (git commit, timestamp, runtime, metrics, versions)
- **Implementation required:**
  - Modify `run_batch()` to write per-case artifacts after each `run_single_case()` return
  - Add case-level resume logic (read existing `case_*.json` files, skip those cases)
  - Add failure artifact: `case_<id>.failed.json` for killed/errored cases
- **Estimate:** 2-3 hours implementation + testing

### ❌ 2. Heavy smoke case protocol NOT defined
- **Status:** FAIL
- **Smoke case spec:**
  - N=128, j_max=3, seed=123, family=`spectral_circle` (same params as OOM case)
  - Output to separate namespace: `reports/RUNS/gate4_smoke_v0.1.24/`
  - Success criteria (ALL must hold):
    - Process completes (no SIGKILL, no exception)
    - Result file written and atomically renamed
    - Peak RSS ≤ 50% of machine RAM (e.g., ≤32 GiB on 64 GiB machine)
    - Metrics populated (true IPR, r-stat both present and sane)
    - No OOM in `dmesg -T`
    - Runtime reasonable (minutes, not days)
- **Required:** Document in `reports/SMOKE_TEST_PROTOCOL_v0.1.24.md`
- **Estimate:** 30 min to write protocol doc

### ❌ 3. 64–128 GB RAM machine NOT provisioned
- **Status:** FAIL — no hardware available
- **Current state:**
  - Hetzner CPX42 (15 GiB RAM) — server OFFLINE (ssh timeout 2026-05-31)
  - No AX42/AX52 ordered
  - No local build ready
- **Required:**
  - Option A: Hetzner AX42 (64 GiB RAM, €47.50/мес) — order now, ready in 24-48h
  - Option B: Local build (64 GiB DDR4 + Ryzen 5700X, ~$490) — order parts, build in 1-2 weeks
  - Must be clean (no memory-heavy cohabitating services)
- **Blocker:** Cannot smoke test or rerun without hardware
- **User decision required:** Which option? (See `hardware_requirements_calculation.md`)

### ❌ 4. BLAS thread limits NOT configured
- **Status:** FAIL — no documented config
- **Required:**
  ```bash
  export OMP_NUM_THREADS=4
  export OPENBLAS_NUM_THREADS=4
  export MKL_NUM_THREADS=4
  export NUMEXPR_NUM_THREADS=4
  ```
- **Rationale:** On 16-core machine, 4 BLAS threads/process bounds per-thread workspace
- **Must verify:** Echo these vars in tmux session before rerun
- **Final value:** Re-measure during smoke test, freeze that value for full rerun
- **Estimate:** 10 min to add to protocol doc

### ❌ 5. Resume behavior NOT tested
- **Status:** FAIL — runner has `--resume` for batches, but NOT for per-case
- **Current `--resume`:** Skips completed batches (line 425-435 in runner)
- **Required `--resume`:** Skips completed CASES within a batch
- **Test required:**
  - Run smoke case
  - Kill mid-run (e.g., SIGTERM after 50% progress)
  - Restart with `--resume`
  - Verify: skipped completed cases, resumed from incomplete
- **Blocker:** Cannot test until per-case checkpointing implemented (blocking issue #1)
- **Estimate:** 30 min testing after checkpointing implemented

---

## 🟡 READY BUT NEEDS VERIFICATION (0/9)

(None — all preconditions are either READY or BLOCKING)

---

## 📋 Summary by Category

| Category | Status | Count |
|---|---|---|
| ✅ READY | operator, output guards, protocol, git | 4/9 |
| ❌ BLOCKING | checkpointing, smoke protocol, hardware, BLAS config, resume test | 5/9 |
| 🟡 NEEDS VERIFICATION | — | 0/9 |

---

## 🚨 Critical Path to Unblock

**Minimum viable sequence to make rerun possible:**

1. **Hardware decision** (user) — AX42 rental vs local build? → Blocks everything
2. **Per-case checkpointing implementation** (2-3 hours) → Blocks smoke test + resume test
3. **Smoke protocol doc** (30 min) → Blocks smoke test
4. **BLAS config doc** (10 min) → Blocks smoke test
5. **Resume behavior test** (30 min after #2) → Blocks full rerun authorization

**Total estimated time:** 3.5-4.5 hours AFTER hardware decision

**Wall time to first smoke test:**
- If AX42 ordered today: 24-48h provisioning + 3.5h implementation = **2-3 days**
- If local build: 1-2 weeks parts delivery + assembly + 3.5h implementation = **2-3 weeks**

---

## 🎯 Next Actions

### Immediate (user decision required)
1. **Choose hardware option:**
   - [ ] Hetzner AX42 (64 GiB, €47.50/мес, ready 24-48h) — for quick rerun
   - [ ] Local build (64 GiB DDR4 + Ryzen, ~$490, ready 1-2 weeks) — for long-term

### After hardware decision (implementation tasks)
2. **Implement per-case checkpointing** in `scripts/run_gate4_batched.py`:
   - [ ] Write `case_<id>.json` after each `run_single_case()` return
   - [ ] Add case-level resume logic (skip existing `case_*.json` files)
   - [ ] Atomic write pattern (`*.tmp` → rename)
   - [ ] Add failure artifacts (`case_*.failed.json`)
   - [ ] Test locally on small grid (N=16, 2-3 cases)

3. **Write smoke test protocol** (`reports/SMOKE_TEST_PROTOCOL_v0.1.24.md`):
   - [ ] Smoke case params (N=128 j_max=3 seed=123 spectral_circle)
   - [ ] Success criteria (6 items from checklist above)
   - [ ] Failure response (do not full rerun, escalate to larger RAM or solver change)

4. **Document BLAS config**:
   - [ ] Add env vars section to smoke protocol
   - [ ] Add verification step (echo $OPENBLAS_NUM_THREADS in tmux)

5. **Test resume behavior**:
   - [ ] Run smoke case
   - [ ] Kill mid-run
   - [ ] Restart with `--resume`
   - [ ] Verify skip + resume works

6. **Final authorization** (user):
   - [ ] Smoke test PASSES all 6 criteria
   - [ ] Freeze rerun command (exact CLI with all flags)
   - [ ] Explicit "go" from user before full rerun

---

## 🔴 Forbidden Until All 9 Preconditions Met

- ❌ No full rerun (216 cases)
- ❌ No Negative Controls batches 3-6
- ❌ No scientific verdict on v0.1.24
- ❌ No external communication about Gate 4B outcome

---

## 📞 Server Status (Hetzner CPX42 ape-2026)

**Last check:** 2026-05-31  
**Result:** ❌ OFFLINE (ssh connection timeout)  
**Action required:**
- Check Hetzner console — server may be suspended, rebooted, or IP changed
- If server deleted — data loss risk (v0.1.24 partial run logs may be gone)
- If server reachable — check tmux session state, git repo integrity

**Command to re-check:**
```bash
ssh -o ConnectTimeout=10 root@46.224.28.128 "tmux ls; ps aux | grep python; df -h; free -h"
```

---

**Verdict:** ❌ **NOT READY FOR RERUN**

**Blocking count:** 5/9 preconditions not met  
**Estimated time to ready:** 2-3 days (AX42) or 2-3 weeks (local build) + 3.5h implementation  
**User decision blocking:** Hardware choice (AX42 vs local)

---

**Recorded:** 2026-05-31  
**Pre-requisite documents:**
- `reports/MEMORY_SAFE_RERUN_PLAN_v0.1.24.md`
- `reports/INCIDENT_GATE4B_v0.1.24_OOM_2026-05-25.md`
- `hardware_requirements_calculation.md`
