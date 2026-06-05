# Gate 4B v0.1.24 Comparison — v0.1.21 vs v0.1.24

**Date:** [FILL AFTER ANALYSIS]  
**Status:** DRAFT TEMPLATE  
**Operator version:** S³ Dirac corrected (commit `093573b`)  
**Metric version:** `v0.1.24_true_ipr_corrected_s3_dirac`

---

## 1. Executive Summary

**Verdict:** [SIGNAL_PRESERVED | SIGNAL_WEAKENED | SIGNAL_DISAPPEARED | TECHNICALLY_INCONCLUSIVE]

**One-sentence summary:** [FILL]

**Key findings:**
- [FILL: aggregate contrast change]
- [FILL: FSS trend change]
- [FILL: family-specific changes]

---

## 2. Completion Status

### v0.1.21 (frozen, operator bug)
- **Total cases:** 216
- **Completed:** [CHECK]
- **Failed:** [CHECK]
- **Operator:** S³ Dirac WITHOUT k=0 negative branch (BUG)

### v0.1.24 (corrected rerun)
- **Total cases:** 216
- **Completed:** [FILL from batches count]
- **Failed:** [FILL]
- **Operator:** S³ Dirac WITH k=0 negative branch (commit `093573b`)

**Coverage comparison:**
| Dimension | v0.1.21 | v0.1.24 | Match? |
|-----------|---------|---------|--------|
| Families | [FILL] | [FILL] | [✅/❌] |
| N sizes | [FILL] | [FILL] | [✅/❌] |
| j_max values | [FILL] | [FILL] | [✅/❌] |
| Seeds | [FILL] | [FILL] | [✅/❌] |

---

## 3. Aggregate IPR Contrast (W=20 vs W=0)

**Definition:** Mean IPR at W=20 divided by mean IPR at W=0, averaged across all cases.

| Version | W=0 mean IPR | W=20 mean IPR | Contrast | Δ from v0.1.21 |
|---------|--------------|---------------|----------|----------------|
| v0.1.21 | [FILL] | [FILL] | [FILL]× | baseline |
| v0.1.24 | [FILL] | [FILL] | [FILL]× | [FILL]% |

**Threshold for PRESERVED verdict:** Contrast ≥ 2.0× AND Δ from v0.1.21 < 20%

**Assessment:** [FILL: PASS/FAIL with reasoning]

---

## 4. Finite-Size Scaling (FSS) Trend

**Definition:** IPR vs s1_size (N=16 → 128) slope, separately for W=0 and W=20.

### W=0 (clean, no disorder)
| N | v0.1.21 IPR | v0.1.24 IPR | Δ |
|---|-------------|-------------|---|
| 16 | [FILL] | [FILL] | [FILL]% |
| 32 | [FILL] | [FILL] | [FILL]% |
| 64 | [FILL] | [FILL] | [FILL]% |
| 128 | [FILL] | [FILL] | [FILL]% |

**Trend:** [FILL: increasing/stable/decreasing in both versions?]

### W=20 (strong disorder)
| N | v0.1.21 IPR | v0.1.24 IPR | Δ |
|---|-------------|-------------|---|
| 16 | [FILL] | [FILL] | [FILL]% |
| 32 | [FILL] | [FILL] | [FILL]% |
| 64 | [FILL] | [FILL] | [FILL]% |
| 128 | [FILL] | [FILL] | [FILL]% |

**Trend:** [FILL: increasing/stable/decreasing in both versions?]

**FSS verdict:** [FILL: trends consistent/diverged]

---

## 5. Family-Specific Contrasts

| Family | v0.1.21 contrast | v0.1.24 contrast | Δ | Status |
|--------|-----------------|-----------------|---|--------|
| `spectral_circle` | [FILL]× | [FILL]× | [FILL]% | [✅/⚠️/❌] |
| `ring` | [FILL]× | [FILL]× | [FILL]% | [✅/⚠️/❌] |
| `wilson_ring` | [FILL]× | [FILL]× | [FILL]% | [✅/⚠️/❌] |

**Assessment:** [FILL: all families preserved/some weakened/all disappeared]

---

## 6. r-statistic Changes

**Definition:** Adjacent gap ratio (Poisson ≈ 0.39, GOE ≈ 0.53, localized ≈ 1.0).

| Version | W=0 r-stat | W=20 r-stat | Separation |
|---------|------------|-------------|------------|
| v0.1.21 | [FILL] | [FILL] | [FILL] |
| v0.1.24 | [FILL] | [FILL] | [FILL] |

**Assessment:** [FILL: r-stat supports/contradicts IPR findings]

---

## 7. Numerical Differences Introduced by Operator Fix

**Expected changes from S³ Dirac fix:**
- Added k=0 negative branch: λ = -3/2 eigenvalue
- Increased Hilbert space dimension by degeneracy of k=0
- Changed low-energy eigenvalue count

**Measured impact on IPR:**
- [FILL: quantify how much IPR changed due to operator fix alone]
- [FILL: is this consistent with adding one eigenvalue + degeneracy?]

**Control check:**
- N=16 j_max=2 (smallest case): v0.1.21 vs v0.1.24 difference = [FILL]%
- Expected from dimension change: [FILL]%

---

## 8. Decision Matrix

| Criterion | Threshold | v0.1.24 Result | Pass? |
|-----------|-----------|----------------|-------|
| Aggregate contrast | ≥ 2.0× | [FILL]× | [✅/❌] |
| Contrast change from v0.1.21 | < 20% | [FILL]% | [✅/❌] |
| FSS trend preserved | W=20 increases, W=0 stable | [FILL] | [✅/❌] |
| All families ≥ 1.5× | Yes | [FILL] | [✅/❌] |
| No technical failures | < 5% failed cases | [FILL]% failed | [✅/❌] |

**Overall verdict:**
- [✅] **SIGNAL_PRESERVED** — all criteria pass
- [⚠️] **SIGNAL_WEAKENED** — contrast reduced but still ≥ 2.0×
- [❌] **SIGNAL_DISAPPEARED** — contrast < 2.0× or FSS collapse
- [⏸️] **TECHNICALLY_INCONCLUSIVE** — ≥ 5% cases failed

---

## 9. Implications

### If SIGNAL_PRESERVED
- ✅ Gate 4B interpretation unfrozen
- ✅ v0.1.21 outputs superseded by v0.1.24
- ✅ Resume Negative Controls batches 3-6
- ✅ Proceed to Gate 5 / W-sweep per roadmap
- ✅ Update methodology paper with corrected operator

### If SIGNAL_WEAKENED
- ⚠️ Update claims: "signal present but weaker than v0.1.21"
- ⚠️ Additional diagnostics required (more seeds? larger sizes?)
- ⚠️ Negative Controls still valuable but lower priority
- ⚠️ External communication requires explicit caveat

### If SIGNAL_DISAPPEARED
- ❌ v0.1.21 marked as implementation artifact
- ❌ Pivot to methodology paper (negative result)
- ❌ Zenodo DOI updated with retraction note for v0.1.21
- ❌ Negative Controls cancelled
- ❌ Gate 5 / W-sweep postponed indefinitely

---

## 10. Next Actions

**Based on verdict [FILL AFTER ANALYSIS]:**

**Immediate:**
- [ ] Commit v0.1.24 results to git
- [ ] Update `docs/CLAIMS_AND_CAVEATS.md` with verdict
- [ ] Update Zenodo DOI description
- [ ] Notify Tom Lawrence (CAMP) with verdict

**Soon:**
- [ ] [IF PRESERVED] Resume Negative Controls batches 3-6
- [ ] [IF PRESERVED] Plan Gate 5
- [ ] [IF WEAKENED] Diagnostic investigation plan
- [ ] [IF DISAPPEARED] Methodology paper pivot

**Later:**
- [ ] Delete Hetzner server (cost cleanup)
- [ ] Archive incident reports
- [ ] Extract lessons learned

---

## 11. Data Provenance

**v0.1.21 data:**
- Location: `reports/RUNS/gate4_fss_v0.1.21/`
- Date: 2026-05-22
- Commit: `4b77684` (runner), operator at `093573b` minus k=0 fix
- Status: FROZEN (do not use externally)

**v0.1.24 data:**
- Location: `reports/RUNS/gate4_fss_v0.1.24/`
- Date: 2026-05-31
- Commit: `4b77684` (runner), operator at `093573b` (corrected)
- Server: Hetzner CX52 (<hetzner-server-ip>), 32 GB RAM, 16 vCPU
- Runtime: [FILL] hours
- Status: [FILL after verification]

---

**Document status:** TEMPLATE — fill after v0.1.24 rerun completes  
**Author:** Sergey Boyko + Claude Sonnet 4.5  
**Last updated:** 2026-05-31  
**Next review:** After v0.1.24 download and analysis
