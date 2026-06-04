# FSS Slope Reanalysis — v0.1.24

**Date:** 2026-06-01  
**Purpose:** Quantify finite-size scaling (FSS) slopes for Gate 4B families vs Negative Controls  
**Status:** ✅ **ANALYSIS COMPLETE**

---

## Executive Summary

**Key finding:** `broken_wilson_term` FSS slope **MATCHES** `ring` and `wilson_ring` families (all STABLE ~0.01-0.03), but **DIFFERS** from `spectral_circle` (WEAKENING -0.49).

**Verdict:** FSS slope analysis **confirms** `broken_wilson_term` = `ring` family equivalence.

**Implication:** Cannot distinguish `broken_wilson_term` from `ring`/`wilson_ring` by FSS slope alone → supports Code Audit finding that control C tested family contrast, NOT Wilson term perturbation.

---

## Method

**Fit model:** `log(IPR) = a + b * log(N)`

Where:
- `IPR` = `true_ipr_mean` (aggregate IPR across all eigenstates)
- `N` = `s1_size` (system size: 16, 32, 64, 128)
- `b` = FSS slope (scaling exponent)

**Classification:**
- `b > 0.05`: STRENGTHENING (IPR increases with size)
- `-0.05 ≤ b ≤ 0.05`: STABLE (IPR size-independent)
- `b < -0.05`: WEAKENING (IPR decreases with size)

**Data:**
- Gate 4B v0.1.24: 216 cases (3 families × 2 W × 4 sizes × 3 j_max × 3 seeds)
- Negative Controls v0.1.22: 54 cases (3 controls × 2 W × 3 sizes × 1 j_max × 3 seeds)

---

## Results — Gate 4B Families (W=20)

| Family | Slope | R² | p-value | Classification | Interpretation |
|--------|-------|-----|---------|----------------|----------------|
| **spectral_circle** | -0.4933 ± 0.0534 | 0.9771 | 0.0115 | WEAKENING | IPR decreases as N increases (localization strengthens) |
| **ring** | 0.0106 ± 0.0280 | 0.0667 | 0.7418 | **STABLE** | IPR approximately size-independent |
| **wilson_ring** | 0.0263 ± 0.0355 | 0.2152 | 0.5362 | **STABLE** | IPR approximately size-independent |

**Observation:** `ring` and `wilson_ring` families show **identical** FSS behavior (STABLE slopes ~0.01-0.03), while `spectral_circle` shows **distinct** WEAKENING trend.

---

## Results — Negative Controls (W=20)

| Control | Slope | R² | p-value | Classification | Interpretation |
|---------|-------|-----|---------|----------------|----------------|
| **broken_wilson_term** | 0.0164 ± 0.0205 | 0.3896 | 0.5709 | **STABLE** | IPR approximately size-independent (matches `ring`) |
| **random_hermitian** | -1.1361 ± 0.0235 | 0.9996 | 0.0131 | WEAKENING | Strong 1/N scaling (expected for random matrix) |
| **scrambled_geometry** | -0.8964 ± 0.1696 | 0.9655 | 0.1190 | WEAKENING | Strong localization increase with size |

**Observation:** `broken_wilson_term` slope 0.0164 matches `ring` 0.0106 and `wilson_ring` 0.0263 within error bars.

---

## Comparison: Gate 4B vs broken_wilson_term

### FSS Slope Match

```
broken_wilson_term:  0.0164 ± 0.0205  (STABLE)
ring:                0.0106 ± 0.0280  (STABLE)
wilson_ring:         0.0263 ± 0.0355  (STABLE)
spectral_circle:    -0.4933 ± 0.0534  (WEAKENING)
```

**Δ(slope) between broken_wilson_term and ring:** 0.0058 (within combined error 0.034)

**Conclusion:** `broken_wilson_term` and `ring` are **statistically indistinguishable** by FSS slope.

### Why random_hermitian and scrambled_geometry FAIL

Both show strong WEAKENING slopes (-1.14 and -0.90), indicating **different physics**:
- Random Hermitian: 1/N scaling from delocalization in large matrices
- Scrambled geometry: Increased localization with size (opposite of robustness)

---

## Interpretation

### What FSS Slope Tells Us

**FSS slope classification = Finite-size scaling trend:**
- **STABLE (b ≈ 0):** IPR independent of system size → localization length ≫ system size (extended states or weak localization)
- **WEAKENING (b < 0):** IPR decreases with size → localization strengthens (Anderson localization regime)
- **STRENGTHENING (b > 0):** IPR increases with size → delocalization with size (rare, seen in some critical points)

### Gate 4B Family Differences

**spectral_circle (WEAKENING):**
- Slope -0.49: IPR ∝ N^(-0.49) ≈ 1/√N
- Physics: Localization strengthens with size (closer to Anderson localization)

**ring + wilson_ring (STABLE):**
- Slope ~0.01-0.03: IPR approximately constant across N=16 to N=128
- Physics: Localization length >> system size, or marginal delocalization

**Implication:** Family choice DOES matter for FSS behavior, but `ring` and `wilson_ring` cluster together.

### Why broken_wilson_term Matches ring

**Code Audit confirmed:** `wilson_mode="disabled"` constructs `s1_family='ring'`.

**FSS slope confirms:** `broken_wilson_term` scaling identical to `ring` within statistical error.

**Conclusion:** `broken_wilson_term` control IS `ring` family, not a perturbation of `wilson_ring`.

---

## Decision Tree: Can FSS Slope Distinguish Controls?

| Question | Answer |
|----------|--------|
| Can FSS slope distinguish `random_hermitian` from Gate 4B? | ✅ YES — random shows strong WEAKENING (-1.14), Gate shows STABLE/weak WEAKENING |
| Can FSS slope distinguish `scrambled_geometry` from Gate 4B? | ✅ YES — scrambled shows strong WEAKENING (-0.90), Gate shows STABLE/weak WEAKENING |
| Can FSS slope distinguish `broken_wilson_term` from `ring` family? | ❌ NO — slopes identical within error (0.0164 vs 0.0106) |
| Can FSS slope distinguish `ring` from `wilson_ring`? | ❌ NO — both STABLE with similar slopes (0.0106 vs 0.0263) |

**Verdict:** FSS slope is **sensitive** to geometric scrambling and random baselines, but **insensitive** to `ring` vs `wilson_ring` family choice.

---

## Implications for Harness Specificity

### Positive Evidence (Harness CAN Reject)

- ✅ `random_hermitian` slope -1.14 ≠ Gate 4B → harness rejects fully random
- ✅ `scrambled_geometry` slope -0.90 ≠ Gate 4B → harness rejects scrambled indices

### Negative Evidence (Harness CANNOT Distinguish)

- ❌ `broken_wilson_term` slope 0.0164 ≈ `ring` 0.0106 → harness cannot distinguish
- ❌ `ring` slope 0.0106 ≈ `wilson_ring` 0.0263 → Wilson term not load-bearing for FSS trend

### Updated Specificity Verdict

**From Negative Controls Full Pattern Audit:**
- `broken_wilson_term` reproduced full pattern (8.20× contrast + STABLE FSS)

**From FSS Slope Reanalysis (this report):**
- `broken_wilson_term` STABLE slope matches `ring` and `wilson_ring` families

**Conclusion:** Harness shows **partial specificity** — rejects random/scrambled baselines, but accepts `ring` family which is geometrically intact S³×S¹ product.

**What this does NOT prove:**
- ❌ Does NOT prove "Wilson term irrelevant" — `wilson_mode="scrambled"` still untested
- ❌ Does NOT prove "all families equivalent" — `spectral_circle` shows distinct WEAKENING
- ❌ Does NOT prove "harness fully nonspecific" — geometric scrambling DOES fail

---

## W=0 Baseline (Clean Limit)

| Group | Slope (W=0) | Classification | Interpretation |
|-------|-------------|----------------|----------------|
| **spectral_circle** | -1.0000 ± 0.0000 | WEAKENING | Perfect 1/N scaling (analytically exact for clean spectral) |
| **ring** | -0.9524 ± 0.0082 | WEAKENING | Near-1/N scaling (close to clean limit) |
| **wilson_ring** | -1.0000 ± 0.0000 | WEAKENING | Perfect 1/N scaling |
| **broken_wilson_term** | -0.9921 ± 0.0182 | WEAKENING | Near-1/N scaling (matches ring) |
| **random_hermitian** | -1.0008 ± 0.0006 | WEAKENING | Perfect 1/N (random matrix theory) |
| **scrambled_geometry** | -1.7572 ± 0.0129 | WEAKENING | Stronger than 1/N (highly localized) |

**Observation:** At W=0, ALL groups show WEAKENING slopes (system size increases → IPR decreases), but with different exponents.

**Key difference:** Disorder (W=20) changes `ring`/`wilson_ring` slopes from -0.95 → +0.01 (WEAKENING → STABLE), while `spectral_circle` stays WEAKENING (-1.00 → -0.49).

---

## Recommendations

### Priority 1 — Rerun `wilson_mode="scrambled"` (Pending)

**Goal:** Test whether scrambling Wilson term breaks FSS STABLE trend.

**Hypothesis:** If Wilson term is load-bearing, scrambled Wilson should show WEAKENING slope (not STABLE).

**Decision rule:**
- IF scrambled Wilson slope STABLE (~0.01-0.03) → Wilson term NOT load-bearing
- IF scrambled Wilson slope WEAKENING (< -0.1) → Wilson term IS load-bearing

### Priority 2 — Contrast-Normalized Effect Size (Next)

**Goal:** Quantify `broken_wilson_term` 8.20× relative to Gate 4B baseline 7.07×.

**Metric:** Relative contrast = 8.20 / 7.07 = 1.16× (16% stronger than Gate 4B)

**Question:** Is 16% difference within seed variance?

### Priority 3 — Seed Variance Analysis (Next)

**Goal:** Check if 8.20× contrast is stable across seeds or driven by outliers.

**Method:** Compute per-seed contrasts, check variance.

---

## Raw Data

**Saved:** `reports/fss_slope_data_v0.1.24.json`

**Contents:**
- Gate 4B slopes by family + disorder
- Negative Controls slopes by control + disorder
- Fit parameters (slope, intercept, R², p-value, std_err)
- Classification (STABLE / WEAKENING / STRENGTHENING)

---

## Conclusion

**FSS slope reanalysis confirms:**
1. ✅ `broken_wilson_term` = `ring` family (slopes identical within error)
2. ✅ `ring` ≈ `wilson_ring` for FSS behavior (both STABLE at W=20)
3. ✅ `spectral_circle` distinct (WEAKENING at W=20)
4. ✅ `random_hermitian` and `scrambled_geometry` strongly WEAKENING (harness CAN reject)

**Updated diagnostic:**
- `broken_wilson_term` reproduced pattern because it IS `ring` family
- `ring` and `wilson_ring` show similar robustness (Wilson term not critical for FSS)
- Harness shows **partial specificity** (rejects random/scrambled, accepts intact geometry)

**Next steps:**
1. Rerun `wilson_mode="scrambled"` (18 cases, ~14 min)
2. Seed variance analysis (check if 8.20× stable)
3. Control-normalized effect size (quantify 16% difference)

---

**Last updated:** 2026-06-01  
**Status:** ✅ COMPLETE  
**Next action:** Seed variance analysis (deliverable 2/7)

╔═ ⚡ УРОК ══════════════════════════════════════════════════════════════════╗
  Scipy stats.linregress возвращает (slope, intercept, r_value, p_value, std_err) — r_value это Pearson correlation, НЕ R². Для коэффициента детерминации нужно r_value**2. Частая ошибка — использовать r_value напрямую как "качество фита".
╚═══════════════════════════════════════════════════════════════════════════╝
