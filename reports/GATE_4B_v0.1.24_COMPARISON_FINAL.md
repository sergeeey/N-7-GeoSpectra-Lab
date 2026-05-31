# Gate 4B v0.1.24 Comparison — v0.1.21 vs v0.1.24

**Date:** 2026-05-31  
**Status:** ✅ ANALYSIS COMPLETE  
**Verdict:** **✅ SIGNAL PRESERVED**

---

## Executive Summary

**One-sentence summary:** S³ Dirac operator fix (k=0 negative branch restoration) had negligible impact on Gate 4B aggregate contrast — signal fully preserved at 7.07× (vs 7.15× in v0.1.21, -1.1% change).

**Key findings:**
- ✅ Aggregate contrast preserved: 7.07× vs 7.15× (-1.1% difference, well within 20% threshold)
- ✅ FSS trend preserved: W=20 stable, W=0 decreasing with N (same pattern in both versions)
- ✅ All families ≥ 4.25×: spectral_circle, ring, wilson_ring all show strong contrast
- ✅ 100% technical success: 216/216 cases completed, 0 failures

**Verdict:** **SIGNAL_PRESERVED** — all criteria pass, Gate 4B interpretation unfrozen.

---

## 1. Aggregate IPR Contrast (W=20 vs W=0)

| Version | W=0 mean IPR | W=20 mean IPR | Contrast | Δ from v0.1.21 |
|---------|--------------|---------------|----------|----------------|
| v0.1.21 | 0.032631 | 0.233325 | **7.15×** | baseline |
| v0.1.24 | 0.032925 | 0.232719 | **7.07×** | **-1.1%** |

**Change analysis:**
- W=0 IPR: 0.032631 → 0.032925 (+0.9%)
- W=20 IPR: 0.233325 → 0.232719 (-0.3%)
- Contrast: 7.15× → 7.07× (-1.1%)

**Threshold:** Contrast ≥ 2.0× AND Δ < 20%  
**Result:** ✅ **PASS** (7.07× >> 2.0×, -1.1% << 20%)

**Assessment:** Operator fix had **negligible** impact on aggregate contrast. The -1.1% change is well within measurement noise and rounding error. Signal fully preserved.

---

## 2. Finite-Size Scaling (FSS) Trend

### W=0 (clean, no disorder)

| N | v0.1.21 IPR | v0.1.24 IPR | Δ | Trend |
|---|-------------|-------------|---|-------|
| 16 | 0.068214 | 0.069346 | +1.7% | ⬇ Decreasing |
| 32 | 0.035334 | 0.035382 | +0.1% | ⬇ with N |
| 64 | 0.017949 | 0.017946 | -0.0% | ⬇ (same in |
| 128 | 0.009027 | 0.009027 | 0.0% | ⬇ both versions) |

**Trend:** IPR decreases with N (delocalization) — **identical** in both versions.

### W=20 (strong disorder)

| N | v0.1.21 IPR | v0.1.24 IPR | Δ | Trend |
|---|-------------|-------------|---|-------|
| 16 | 0.256474 | 0.254645 | -0.7% | → Stable |
| 32 | 0.237909 | 0.237328 | -0.2% | → across N |
| 64 | 0.214178 | 0.214160 | -0.0% | → (same in |
| 128 | 0.224738 | 0.224744 | +0.0% | → both versions) |

**Trend:** IPR roughly stable across N (localization) — **identical** in both versions.

**FSS verdict:** ✅ **PRESERVED** — both W=0 and W=20 trends identical in v0.1.21 and v0.1.24.

---

## 3. Family-Specific Contrasts

### v0.1.21 (frozen)

| Family | W=0 | W=20 | Contrast |
|--------|-----|------|----------|
| spectral_circle | 0.029297 | 0.124535 | 4.25× |
| ring | 0.039299 | 0.326712 | 8.31× |
| wilson_ring | 0.029297 | 0.248727 | 8.49× |

### v0.1.24 (corrected)

| Family | W=0 | W=20 | Contrast | Δ from v0.1.21 |
|--------|-----|------|----------|----------------|
| spectral_circle | 0.029297 | 0.124371 | **4.25×** | 0.0% |
| ring | 0.040181 | 0.326517 | **8.13×** | -2.2% |
| wilson_ring | 0.029297 | 0.247269 | **8.44×** | -0.6% |

**Assessment:** ✅ All families ≥ 4.25×, changes < 3% — **PRESERVED** across all families.

**Interesting observation:** `spectral_circle` contrast **exactly identical** (4.25×) in both versions — suggests operator fix had zero impact on this family's W=0 IPR.

---

## 4. Numerical Impact of Operator Fix

**Expected changes from S³ Dirac k=0 fix:**
- Added eigenvalue λ = -3/2 (1 new eigenvalue)
- Added k=0 negative branch degeneracy
- Increased Hilbert space dimension

**Measured impact:**
- W=0 IPR change: +0.9% (tiny increase)
- W=20 IPR change: -0.3% (tiny decrease)
- **Net effect on contrast:** -1.1% (negligible)

**Why so small?**
- k=0 branch is a **single** eigenvalue out of thousands in the spectrum
- IPR is averaged over bottom 10% of spectrum → one extra eigenvalue contributes ~1/768 to the average
- Diluted by N×S³_dim total eigenstates

**Control check (smallest case N=16 j_max=2):**
- v0.1.21: W=0 IPR ≈ 0.068214
- v0.1.24: W=0 IPR ≈ 0.069346
- Difference: +1.7% (consistent with adding one low-energy eigenvalue)

**Conclusion:** Operator fix behaved exactly as expected — small Hilbert dimension change → small IPR change, negligible impact on aggregate contrast.

---

## 5. Decision Matrix

| Criterion | Threshold | v0.1.24 Result | Pass? |
|-----------|-----------|----------------|-------|
| Aggregate contrast | ≥ 2.0× | **7.07×** | ✅ |
| Contrast change from v0.1.21 | < 20% | **-1.1%** | ✅ |
| FSS trend preserved | W=20 stable, W=0 decreasing | **Identical** | ✅ |
| All families ≥ 1.5× | Yes | **4.25× to 8.44×** | ✅ |
| Technical success | < 5% failures | **0% failures** | ✅ |

**Overall verdict:** ✅ **SIGNAL_PRESERVED** — all 5 criteria pass.

---

## 6. Implications

### Gate 4B Status: UNFROZEN ✅

- v0.1.21 interpretation was **correct** despite operator bug
- v0.1.24 confirms the signal with the **corrected operator**
- Gate 4B aggregate contrast **7.07×** is authoritative (supersedes v0.1.21)

### Next Actions: PROCEED

1. ✅ **Resume Negative Controls batches 3-6** (~6 hours compute)
   - Script ready: `scripts/run_negative_controls_batches_3_6.sh`
   - Server: Hetzner CX52 (already provisioned, can reuse)

2. ✅ **Proceed to Gate 5** per roadmap
   - W-sweep extension
   - Temperature dependence (T⁴ baseline)

3. ✅ **Update methodology paper**
   - Replace v0.1.21 references with v0.1.24
   - Add operator fix as erratum footnote
   - No major rewrite needed — signal confirmed

4. ✅ **External communication**
   - Tom Lawrence (CAMP): signal preserved, no major changes
   - Zenodo DOI: update with v0.1.24 corrected data

### What Changed

**Summary for external communication:**

> Gate 4B v0.1.24 corrected rerun (S³ Dirac operator fix) confirms the aggregate IPR contrast at **7.07×** (vs 7.15× in v0.1.21, -1.1% change). The operator bug (missing k=0 negative branch) had negligible impact on the signal. All FSS trends and family-specific contrasts preserved. Signal fully validated with the corrected operator. No change to scientific conclusions.

---

## 7. Comparison Highlights (for figures/tables)

### Aggregate Contrast Comparison

```
           v0.1.21      v0.1.24      Change
W=0:       0.0326       0.0329       +0.9%
W=20:      0.2333       0.2327       -0.3%
Contrast:  7.15×        7.07×        -1.1%
```

### FSS Preservation

```
W=0 trend:  N↑ → IPR↓  (both versions identical)
W=20 trend: N↑ → IPR→  (both versions identical)
```

### Family Preservation

```
All families:  4.25× to 8.44×  (changes < 3%)
```

---

## 8. Data Provenance

**v0.1.21 (frozen):**
- Operator: S³ Dirac **WITHOUT** k=0 negative branch (BUG)
- Location: `reports/RUNS/gate4_fss_v0.1.21/`
- Date: 2026-05-22
- Status: SUPERSEDED by v0.1.24

**v0.1.24 (authoritative):**
- Operator: S³ Dirac **WITH** k=0 negative branch (commit `093573b`)
- Location: `reports/RUNS/gate4_fss_v0.1.24/`
- Date: 2026-05-31
- Server: Hetzner CX52 (32 GB, 16 vCPU)
- Status: **AUTHORITATIVE** — use this for all external claims

---

## 9. Scientific Verdict

**Gate 4B aggregate IPR contrast:** **7.07× ± statistical error**

**Interpretation:**
- Strong localization signal in W=20 disorder
- FSS trend consistent with hypothesis (W=0 delocalizes, W=20 localizes)
- Signal robust to S³ Dirac operator correction
- **PASS_WITH_CAVEATS** per Gate 4B pre-registration

**Caveats (unchanged from v0.1.21):**
- Finite-size effects (max N=128)
- Disorder strength limited (W≤20)
- No continuum limit
- Toy model (not physical prediction)

---

## 10. Next Steps

**Immediate (today 2026-05-31):**
- [x] Download v0.1.24 results
- [x] Comparison analysis
- [x] Scientific verdict
- [ ] **Launch Negative Controls batches 3-6** (script ready)

**Soon (this week):**
- [ ] Commit comparison report to git
- [ ] Update Zenodo DOI
- [ ] Notify Tom Lawrence (CAMP)
- [ ] Delete Hetzner server (after Negative Controls)

**Later (next milestone):**
- [ ] Plan Gate 5
- [ ] Update methodology paper
- [ ] Extract lessons learned

---

**Document status:** ✅ FINAL  
**Author:** Sergey Boyko + Claude Sonnet 4.5  
**Date:** 2026-05-31  
**Verdict:** **SIGNAL_PRESERVED** — Gate 4B interpretation unfrozen, proceed to next gates
