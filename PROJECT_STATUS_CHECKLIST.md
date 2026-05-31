# GeoSpectra Project Status — Complete Checklist

**Date:** 2026-05-31 14:40 UTC  
**Current state:** Gate 4B v0.1.24 rerun IN PROGRESS на Hetzner CX52

---

## 🚀 СЕЙЧАС ВЫПОЛНЯЕТСЯ

### ✅ Gate 4B v0.1.24 Full Rerun (216 cases)
- **Status:** 🟢 RUNNING (batch 1/9, case 19/24 в процессе)
- **Server:** Hetzner CX52 (46.224.28.128), 32 GB RAM, 16 vCPU
- **Started:** 2026-05-31 14:28 UTC
- **Expected finish:** 2026-05-31 16:06 UTC (~1.5 hours remaining)
- **Progress:** ~8% завершено (18 из 216 cases)
- **Tmux session:** `rerun` (активна)
- **Log:** `~/geospectra/reports/RUNS/gate4_fss_v0.1.24_run.log`
- **Monitoring:** `ssh root@46.224.28.128 'tail -f ~/geospectra/reports/RUNS/gate4_fss_v0.1.24_run.log'`

**Action:** Ждать завершения (~1.5 часа), затем скачать результаты

---

## ✅ ЗАВЕРШЕНО (сегодня 2026-05-31)

1. ✅ **Hetzner CX52 server provisioned**
   - IP: 46.224.28.128
   - Specs: 32 GB RAM, 16 vCPU, 640 GB SSD
   - OS: Ubuntu 24.04 LTS
   - Swap: 32 GB created

2. ✅ **Dependencies installed**
   - Python 3.12, numpy 2.4.6, scipy 1.17.1
   - pytest, structlog, scikit-learn, matplotlib

3. ✅ **Code deployed**
   - Repo cloned from GitHub
   - Branch: `main` (commit `4b77684`)
   - S³ Dirac operator corrected (commit `093573b`)

4. ✅ **S³ Dirac tests passed**
   - `pytest tests/cc_toy_lab/spectral/test_dirac_s3_branches.py` → 6/6 PASSED
   - Negative k=0 branch verified
   - Hermiticity verified

5. ✅ **Smoke test PASSED**
   - Case: N=128 j_max=3 seed=123 (heaviest)
   - Time: 120.8 seconds
   - Peak RSS: <2 GB (из 32 GB available)
   - IPR mean: 0.0078, r-stat: 1.0
   - Result: ✅ NO OOM, metrics valid

6. ✅ **BLAS config verified**
   - `OPENBLAS_NUM_THREADS=8`
   - `OMP_NUM_THREADS=8`
   - CPU utilization: 16 cores active

7. ✅ **Full rerun launched**
   - Command: `python3 scripts/run_gate4_batched.py --run-all ...`
   - Output: `reports/RUNS/gate4_fss_v0.1.24/`
   - Protocol: v0.1.24 (corrected S³ Dirac)

---

## ⏳ ОСТАЛОСЬ СДЕЛАТЬ (после rerun)

### 1. Скачать результаты с сервера
**Priority:** 🔴 HIGH (после завершения rerun)

```bash
# Option A: rsync (если работает локально)
rsync -avz --progress root@46.224.28.128:~/geospectra/reports/RUNS/gate4_fss_v0.1.24/ \
  "E:/Проверка Гипотез/работаю над проверкой гипотез/N-7-GeoSpectra-Lab/reports/RUNS/gate4_fss_v0.1.24/"

# Option B: tar + scp
ssh root@46.224.28.128 'cd ~/geospectra && tar -czf results.tar.gz reports/RUNS/gate4_fss_v0.1.24'
scp root@46.224.28.128:~/geospectra/results.tar.gz .
tar -xzf results.tar.gz
```

**Verify:** 9 batches × 24 cases = 216 cases completed
```bash
find reports/RUNS/gate4_fss_v0.1.24/batches/ -name "results.json" | wc -l
# Должно быть 9
```

---

### 2. Создать comparison report v0.1.21 vs v0.1.24
**Priority:** 🔴 HIGH (scientific verdict)

**File:** `reports/GATE_4B_v0.1.24_COMPARISON_v0.1.21_vs_v0.1.24.md`

**Required analysis:**
- Completed cases (per family, per N, per j_max)
- Failure count and failure modes
- `true_ipr_mean` per cell (v0.1.21 vs v0.1.24)
- `r_stat` per cell
- Family contrasts (spectral_circle vs ring vs wilson_ring)
- Aggregate contrast (W=20 vs W=0)
- Finite-size trend (s1_size=16 → 128)

**Verdict options:**
1. ✅ **Signal preserved** — aggregate contrast and FSS trend consistent with v0.1.21
2. ⚠️ **Signal weakened** — contrast reduced but still ≥2.0×
3. ❌ **Signal disappeared** — contrast below threshold or FSS collapse
4. ⏸️ **Rerun failed** — insufficient cases for verdict

**Action:** Write comparison script or manual analysis

---

### 3. Update project documentation
**Priority:** 🟡 MEDIUM

**Files to update:**
- [ ] `PRE_RERUN_CHECKLIST.md` → mark preconditions 1-9 status after rerun
- [ ] `docs/OUTCOMES.md` → update Gate 4B outcome card (commit if ready)
- [ ] `reports/MEMORY_SAFE_RERUN_PLAN_v0.1.24.md` → mark as EXECUTED
- [ ] `.claude/memory/geospectra-status-*.md` → create new memory with v0.1.24 verdict

---

### 4. Commit results to git
**Priority:** 🟡 MEDIUM (after comparison report)

```bash
git add reports/RUNS/gate4_fss_v0.1.24/
git add reports/GATE_4B_v0.1.24_COMPARISON_v0.1.21_vs_v0.1.24.md
git commit -m "feat(gate-4b): complete v0.1.24 corrected rerun (216 cases)

- S³ Dirac operator corrected (commit 093573b)
- IPR metric v0.1.24_true_ipr_corrected_s3_dirac
- Full grid: 216 cases (9 batches × 24 cases)
- Server: Hetzner CX52 (32 GB RAM, 16 vCPU)
- Runtime: ~2 hours
- Verdict: [SIGNAL_PRESERVED | SIGNAL_WEAKENED | SIGNAL_DISAPPEARED]

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

git push
```

---

### 5. Negative Controls batches 3-6 (v0.1.22)
**Priority:** 🟢 LOW (blocked until v0.1.24 verdict)

**Current status:**
- Batches 1-2 completed (18/54 cases, 2026-05-22)
- Batches 3-6 paused (36 cases remaining)
- Location: `reports/RUNS/negative_controls_v0.1.22/`

**Action required:**
- **IF v0.1.24 signal PRESERVED** → resume batches 3-6
- **IF v0.1.24 signal WEAKENED/DISAPPEARED** → pause indefinitely, focus on diagnosis

**Estimate:** ~6 hours compute (если запускать на том же сервере)

---

### 6. Delete Hetzner server (cost cleanup)
**Priority:** 🟡 MEDIUM (после скачивания results)

**Steps:**
1. Verify results downloaded and extracted locally
2. Verify 216 cases present: `ls reports/RUNS/gate4_fss_v0.1.24/batches/`
3. Hetzner Console → `Default` project → server `geospectra-run` → **Delete**

**Cost:** €29.95/месяц (minimum billing 1 month даже если удалишь через день)

---

### 7. Per-case checkpointing implementation (future improvement)
**Priority:** 🟢 LOW (nice-to-have для следующих rerun)

**Current:** Batch-level persistence (24 cases → 1 results.json)  
**Needed:** Case-level persistence (1 case → 1 case_<id>.json)

**Blocker from Memory-Safe Rerun Plan:**
- Modify `scripts/run_gate4_batched.py` → write after each `run_single_case()`
- Add resume logic (skip existing `case_*.json`)
- Atomic write (`*.tmp` → rename)

**Estimate:** 2-3 hours implementation + testing

**Benefit:** Next OOM loses ≤1 case instead of 21

---

## 📊 OVERALL PROJECT STATUS

### Gate Progress

| Gate | Status | Last run | Verdict | Notes |
|------|--------|----------|---------|-------|
| Gate 1 | ✅ PASS | v0.1.19 | Radion stabilized | Completed 2026-05 |
| Gate 2 | ⏳ PARTIAL | v0.1.19 | Positive controls pass | Some TODO remain |
| Gate 3 | ✅ PASS | v0.1.20 | Full diagnostic complete | S³×S¹ controls validated |
| **Gate 4A** | ✅ PASS | v0.1.20 | FSS grid complete | 216 cases, IPR metric (old) |
| **Gate 4B** | 🟡 **v0.1.21 FROZEN** | v0.1.21 | Operator bug found | v0.1.24 rerun IN PROGRESS |
| Gate 5 | ❌ NOT STARTED | — | — | Blocked on Gate 4B |

### Critical Path

```
Gate 4B v0.1.24 rerun (IN PROGRESS, ~1.5h remaining)
  ↓
Download results + comparison report (~1-2 hours)
  ↓
Verdict: PRESERVED / WEAKENED / DISAPPEARED
  ↓
  IF PRESERVED:
    → Negative Controls batches 3-6 (~6h compute)
    → Gate 5 planning
  IF WEAKENED/DISAPPEARED:
    → Diagnosis + methodology paper update
    → Pivot to negative-result write-up
```

---

## 🔴 BLOCKING ISSUES (none currently)

**All blockers resolved:**
- ✅ Hardware: CX52 provisioned
- ✅ Operator bug: Fixed in `093573b`
- ✅ Smoke test: PASSED
- ✅ Full rerun: IN PROGRESS

---

## 📝 UNCOMMITTED LOCAL CHANGES

```
M  .claude/settings.local.json
?? PRE_RERUN_CHECKLIST.md
?? SERVER_INFO.md
?? docs/OUTCOMES.md
?? hardware_requirements_calculation.md
?? PROJECT_STATUS_CHECKLIST.md (this file)
```

**Action:** Commit documentation after v0.1.24 verdict

---

## 🎯 NEXT 3 ACTIONS (in order)

1. **Wait for rerun to finish** (~1.5 hours, автоматически)
2. **Download results** (rsync или tar+scp, ~5 минут)
3. **Write comparison report** (v0.1.21 vs v0.1.24 analysis, ~1-2 hours)

---

## ⏰ ESTIMATED TIMELINE

| Milestone | ETA | Confidence |
|-----------|-----|------------|
| Gate 4B v0.1.24 rerun completes | 2026-05-31 16:06 UTC | 95% |
| Results downloaded locally | 2026-05-31 16:30 UTC | 90% |
| Comparison report written | 2026-05-31 18:00 UTC | 70% |
| Scientific verdict | 2026-05-31 18:30 UTC | 60% |
| Negative Controls resume (if signal preserved) | 2026-06-01 00:00 UTC | 40% |

---

## 💰 COSTS

| Item | Amount | Notes |
|------|--------|-------|
| Hetzner CX52 | €29.95/мес | Minimum billing 1 month |
| **Total** | **€29.95** | ~$32 USD |

**Actual usage:** ~2 hours  
**Effective rate:** €14.98/hour для этого rerun

---

**Last updated:** 2026-05-31 14:40 UTC  
**Next update:** После завершения rerun (expected 16:06 UTC)
