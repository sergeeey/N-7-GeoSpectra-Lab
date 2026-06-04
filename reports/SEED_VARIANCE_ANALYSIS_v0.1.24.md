# Seed Variance Analysis — v0.1.24

**Date:** 2026-06-01  
**Purpose:** Check if contrasts are stable across seeds or driven by outliers  
**Status:** ✅ **ANALYSIS COMPLETE**

---

## Executive Summary

**Key finding:** `broken_wilson_term` seed variance (CV 73.1%) **matches** Gate 4B families (`ring` 74.5%, `wilson_ring` 80.6%).

**Verdict:** 8.20× contrast is **NOT driven by outlier seeds** — variance is comparable to intact geometry.

**Implication:** `broken_wilson_term` robustness is **reproducible** across different random disorder realizations, not a statistical fluke.

---

## Method

**Contrast computation:** For each (family/control, size, seed):
```
contrast = IPR(W=20) / IPR(W=0)
```

**Variance metric:** Coefficient of Variation (CV) = (std / mean) × 100%

**Interpretation:**
- Low CV (<20%): Contrast stable across seeds (low noise)
- Medium CV (20-50%): Moderate seed-to-seed variation
- High CV (>50%): Large variation (size-dependent effects dominate)

**Data:**
- Gate 4B: 216 cases → 12 contrasts per family (4 sizes × 3 seeds)
- Negative Controls: 54 cases → 9 contrasts per control (3 sizes × 3 seeds)

---

## Results — Gate 4B Families

### Ring Family

| Size | Mean Contrast | Std Dev | CV (%) | n seeds |
|------|---------------|---------|--------|---------|
| 16   | 4.05×         | 1.22    | 30.1   | 3       |
| 32   | 7.36×         | 1.48    | 20.2   | 3       |
| 64   | 14.25×        | 1.32    | 9.3    | 3       |
| 128  | 29.46×        | 0.74    | 2.5    | 3       |
| **AGGREGATE** | **13.78×** | **10.26** | **74.5** | **12** |

**Observation:** CV **decreases** with system size (30.1% → 2.5%), indicating size-dependent effects.

### Spectral Circle Family

| Size | Mean Contrast | Std Dev | CV (%) | n seeds |
|------|---------------|---------|--------|---------|
| 16   | 3.01×         | 0.86    | 28.5   | 3       |
| 32   | 4.71×         | 0.79    | 16.7   | 3       |
| 64   | 5.57×         | 1.13    | 20.3   | 3       |
| 128  | 8.88×         | 1.89    | 21.3   | 3       |
| **AGGREGATE** | **5.54×** | **2.47** | **44.6** | **12** |

**Observation:** CV relatively **stable** across sizes (16.7-28.5%), lower aggregate variance than ring/wilson_ring.

### Wilson Ring Family

| Size | Mean Contrast | Std Dev | CV (%) | n seeds |
|------|---------------|---------|--------|---------|
| 16   | 3.83×         | 0.43    | 11.3   | 3       |
| 32   | 7.58×         | 1.00    | 13.2   | 3       |
| 64   | 15.10×        | 0.32    | 2.1    | 3       |
| 128  | 34.07×        | 1.78    | 5.2    | 3       |
| **AGGREGATE** | **15.15×** | **12.21** | **80.6** | **12** |

**Observation:** CV **decreases** with size (11.3% → 5.2%), similar to ring family.

---

## Results — Negative Controls

### broken_wilson_term Control

| Size | Mean Contrast | Std Dev | CV (%) | n seeds |
|------|---------------|---------|--------|---------|
| 16   | 3.75×         | 1.13    | 30.1   | 3       |
| 64   | 14.25×        | 1.32    | 9.3    | 3       |
| 128  | 30.99×        | 0.78    | 2.5    | 3       |
| **AGGREGATE** | **16.33×** | **11.94** | **73.1** | **9** |

**Observation:** CV pattern **identical** to ring family (30.1% → 2.5% across sizes).

⚠️ **Note:** Size 32 missing from Negative Controls grid (pre-registration choice).

### random_hermitian Control

| Size | Mean Contrast | Std Dev | CV (%) | n seeds |
|------|---------------|---------|--------|---------|
| 16   | 1.38×         | 0.00    | 0.2    | 3       |
| 64   | 1.10×         | 0.00    | 0.2    | 3       |
| 128  | 1.05×         | 0.00    | 0.1    | 3       |
| **AGGREGATE** | **1.18×** | **0.15** | **13.0** | **9** |

**Observation:** Extremely **low variance** (CV <1% per size), indicating disorder-insensitive system.

### scrambled_geometry Control

| Size | Mean Contrast | Std Dev | CV (%) | n seeds |
|------|---------------|---------|--------|---------|
| 16   | 3.40×         | 0.48    | 14.2   | 3       |
| 64   | 8.75×         | 1.84    | 21.1   | 3       |
| 128  | 21.76×        | 4.80    | 22.1   | 3       |
| **AGGREGATE** | **11.30×** | **8.57** | **75.9** | **9** |

**Observation:** CV relatively **stable** across sizes (14-22%), high aggregate variance (75.9%).

---

## Comparison Summary

| Group | Aggregate Mean | Aggregate Std | Aggregate CV (%) | n |
|-------|---------------|---------------|-----------------|---|
| **ring** | 13.78× | 10.26 | **74.5** | 12 |
| **spectral_circle** | 5.54× | 2.47 | **44.6** | 12 |
| **wilson_ring** | 15.15× | 12.21 | **80.6** | 12 |
| **broken_wilson_term** | 16.33× | 11.94 | **73.1** | 9 |
| **random_hermitian** | 1.18× | 0.15 | **13.0** | 9 |
| **scrambled_geometry** | 11.30× | 8.57 | **75.9** | 9 |

**Gate 4B mean CV:** 66.6% (average of three families)

**broken_wilson_term CV:** 73.1%

**Δ(CV):** +6.5% (within 10% tolerance)

---

## Interpretation

### Why High Aggregate CV (70-80%)?

**Root cause:** Size-dependent contrasts dominate variance.

**Example (ring family):**
- N=16: 4.05×
- N=128: 29.46×

Range = 7.3× between smallest and largest size → aggregate std = 10.26 → high CV.

**Key insight:** High aggregate CV is **NOT** from seed noise, but from **size scaling** (contrast increases ~7× from N=16 to N=128).

### Within-Size CV (Low)

**Per-size CV for broken_wilson_term:**
- N=16: 30.1%
- N=64: 9.3%
- N=128: 2.5%

**Interpretation:** Seed-to-seed variation **decreases** with system size (larger systems more reproducible).

### Comparison: broken_wilson_term vs ring

| Metric | broken_wilson_term | ring | Match? |
|--------|-------------------|------|--------|
| Aggregate CV | 73.1% | 74.5% | ✅ YES (within 2%) |
| N=16 CV | 30.1% | 30.1% | ✅ **EXACT MATCH** |
| N=64 CV | 9.3% | 9.3% | ✅ **EXACT MATCH** |
| N=128 CV | 2.5% | 2.5% | ✅ **EXACT MATCH** |

**Verdict:** `broken_wilson_term` and `ring` family have **identical** seed variance profiles.

**Explanation:** Code Audit confirmed `broken_wilson_term` uses `s1_family='ring'` → same construction → same variance.

---

## Decision Tree

### Q1: Is 8.20× contrast driven by outlier seeds?

**Answer:** ❌ NO

**Evidence:** CV 73.1% comparable to Gate 4B families (66.6% mean), indicating normal seed variance.

### Q2: Does broken_wilson_term show higher seed noise than Gate 4B?

**Answer:** ❌ NO

**Evidence:** CV 73.1% vs 74.5% (ring) and 80.6% (wilson_ring) — broken_wilson_term is **middle of the range**.

### Q3: Is broken_wilson_term more stable than scrambled_geometry?

**Answer:** ≈ COMPARABLE

**Evidence:** CV 73.1% vs 75.9% — both show similar aggregate variance.

### Q4: Why does random_hermitian have such low CV (13.0%)?

**Answer:** Disorder-insensitive regime

**Evidence:** Contrasts ~1.05-1.38× (near-unity) with minimal spread → Anderson disorder at W=20 has weak effect on random Hermitian baselines.

---

## Recommendations

### Finding 1 — Seed Variance is NOT a Discriminator

**Conclusion:** Cannot distinguish `broken_wilson_term` from `ring`/`wilson_ring` by seed variance alone.

**Implication:** All three show high aggregate CV (~73-81%) due to size-dependent contrast scaling, NOT seed noise.

### Finding 2 — Per-Size Variance Decreases with N

**Trend:** CV drops from ~30% (N=16) to ~2-5% (N=128) for ring/wilson_ring/broken_wilson_term.

**Physical interpretation:** Larger systems → more eigenstates → ensemble averaging reduces seed-to-seed fluctuations.

### Finding 3 — Scrambled Geometry Shows Unexpected High Variance

**Observation:** scrambled_geometry CV 75.9% comparable to intact geometry.

**Question:** Why does scrambling NOT reduce variance?

**Hypothesis:** Scrambled indices may introduce size-dependent randomness that maintains high CV.

**Action:** Deeper investigation of scrambled_geometry construction (out of scope for this sprint).

---

## Limitations

### Aggregate CV Misleading

**Issue:** Aggregate CV (73.1%) dominated by size-range spread (4× to 30×), not seed noise.

**Better metric:** Within-size CV (2.5-30.1%) directly measures seed reproducibility.

**Recommendation:** Report both aggregate CV (for completeness) and per-size CV (for interpretation).

### Missing Size N=32 in Negative Controls

**Impact:** broken_wilson_term has 9 data points vs Gate 4B 12 → slightly less statistical power.

**Mitigation:** Per-size CV comparisons use matching sizes (16, 64, 128) → fair comparison.

### Only 3 Seeds Per (Size, W) Cell

**Limitation:** n=3 seeds → CV estimates have high uncertainty (need ≥5 seeds for robust CV).

**Impact:** Small differences in CV (<10%) may be noise, not signal.

**Conclusion:** Focus on **large differences** (e.g., random_hermitian 13% vs broken_wilson_term 73% = 5.6× ratio).

---

## Conclusion

**Seed variance analysis confirms:**
1. ✅ `broken_wilson_term` CV 73.1% matches `ring` 74.5% (within 2%)
2. ✅ Per-size CV pattern **identical** for broken_wilson_term and ring (30% → 2.5%)
3. ✅ 8.20× contrast is **NOT** driven by outlier seeds (reproducible across seeds)
4. ✅ High aggregate CV (70-80%) is due to **size scaling**, NOT seed noise

**Updated diagnostic:**
- `broken_wilson_term` variance indistinguishable from `ring` family
- Seed-to-seed reproducibility **normal** for this harness
- Cannot use seed variance to distinguish control from intact geometry

**Next steps:**
1. Control-normalized effect size (quantify 16.33× vs 7.07× difference)
2. r_stat analysis (level spacing statistics by control)
3. Rerun preparation checklist (what to save for per-state diagnostics)

---

**Last updated:** 2026-06-01  
**Status:** ✅ COMPLETE  
**Next action:** Control-normalized effect size (deliverable 4/7)
