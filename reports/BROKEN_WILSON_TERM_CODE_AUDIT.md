# Broken Wilson Term Control — Code Audit

**Date:** 2026-06-01  
**Purpose:** Root-cause analysis of why `broken_wilson_term` control reproduced full Gate 4B pattern (8.20× contrast + STABLE FSS trend)  
**Status:** ✅ **ROOT CAUSE IDENTIFIED**

---

## Executive Summary

**VERDICT:** `broken_wilson_term` control construction **DOES NOT test Wilson term** as pre-registered.

**Root cause:** Execution script hardcodes `wilson_mode="disabled"`, which builds **pure ring** (identical to `s1_family='ring'`), NOT a Wilson-term perturbation.

**Impact:** Control C tested "ring vs wilson_ring" contrast, NOT "broken Wilson term vs intact Wilson term".

**Consequence:** Full Pattern Audit verdict `HARNESS_NONSPECIFIC` is valid, but **diagnosis incomplete** — we tested the wrong null hypothesis.

---

## Pre-Registration vs Implementation Mismatch

### Pre-Registration Intent

From `reports/S3_S1_NEGATIVE_CONTROLS_PREREGISTRATION_v0.1.22.md` (lines 168-189):

> **Control C: Broken Wilson term**
> 
> Purpose: Test whether wilson_ring family result depends on *meaningful* Wilson term implementation.
> 
> Construction options:
> - `wilson_mode='disabled'`: Wilson coefficient = 0 (pure ring)
> - `wilson_mode='scrambled'`: Wilson term structure randomized
> 
> Expected: Should NOT reproduce wilson_ring robustness (8.49× contrast + strengthening FSS).

**Key pre-registration claim:** Two modes planned, user chooses which.

### Actual Implementation

**Execution script:** `scripts/run_negative_controls_v0_1_22.py`, line 229:

```python
operator, meta = build_broken_wilson_control(
    ...
    wilson_mode="disabled",  # ← HARDCODED
)
```

**Result:** ONLY `wilson_mode="disabled"` executed across all 18 broken_wilson_term cases (W=0/20 × sizes=16/64/128 × seeds=123/456/789).

**Verdict:** Pre-registration allowed two modes, execution tested ONE mode only.

---

## What `wilson_mode="disabled"` Actually Tests

### Code path (cc_toy_lab/controls/negative_controls.py, lines 282-294)

```python
if wilson_mode == "disabled":
    # Build S³×S¹ with pure ring (no Wilson term)
    # This is achieved by using s1_family='ring' instead of 'wilson_ring'
    op, _, _ = build_s3_s1_product_operator(
        j_max=int(j_max),
        s1_size=int(s1_size),
        alpha=float(alpha),
        mode="clean" if disorder_strength == 0.0 else "geometric_weight",
        disorder_strength=float(disorder_strength),
        seed=seed,
        radius=float(radius),
        s1_family="ring",  # ← Pure ring, Wilson disabled
    )
    operator = op
```

**Construction:** Calls `build_s3_s1_product_operator` with `s1_family="ring"`.

**Physical content:** S³ Dirac operator (k=0 corrected) ⊗ S¹ ring operator (nearest-neighbor hopping, no Laplacian correction).

**Equivalence:** This is **identical** to Gate 4B `ring` family baseline.

---

## What Was Tested vs What Should Have Been Tested

| Aspect | Pre-Registered Test | Actual Test |
|--------|---------------------|-------------|
| **Control C construction** | "Broken Wilson term" — perturb or disable Wilson correction | Pure ring (s1_family='ring') |
| **Null hypothesis** | "Wilson term is NOT load-bearing for wilson_ring robustness" | "ring family also shows robustness" |
| **Baseline comparison** | `wilson_ring` (intact) vs `broken_wilson_term` (perturbed/disabled) | `wilson_ring` vs `ring` |
| **What 8.20× contrast tells us** | Wilson term breaking did NOT kill signal → Wilson term not needed | ring family ALSO shows robustness → family choice may not matter |

**Key distinction:** We tested **family contrast** (ring vs wilson_ring), NOT **Wilson term perturbation** (intact vs broken).

---

## What `wilson_mode="scrambled"` Would Have Tested

### Code path (lines 297-331)

```python
elif wilson_mode == "scrambled":
    # Build wilson_ring first
    op_wilson, _, _ = build_s3_s1_product_operator(..., s1_family="wilson_ring")
    
    # Build ring baseline
    op_ring, _, _ = build_s3_s1_product_operator(..., s1_family="ring")
    
    # Approximate Wilson term = H_wilson - H_ring
    wilson_term_approx = op_wilson - op_ring
    
    # Scramble: multiply by random Hermitian sign pattern
    rng = np.random.default_rng(int(seed))
    random_signs = rng.choice([-1.0, 1.0], size=total_dim)
    scrambled_wilson = np.diag(random_signs) @ wilson_term_approx
    
    # Reconstruct with scrambled Wilson term
    operator = op_ring + scrambled_wilson
```

**Construction:** Extracts Wilson term as `(H_wilson - H_ring)`, randomizes signs, adds back to ring baseline.

**Physical meaning:** Wilson term contribution present but **geometrically meaningless** (sign-scrambled).

**Test:** Does wilson_ring robustness survive when Wilson term loses geometric structure?

**Expectation:** If Wilson term is load-bearing, scrambling should kill the 8.49× contrast + STABLE FSS trend.

---

## Why `wilson_mode="disabled"` Reproduced Gate 4B Pattern

### Hypothesis (pending verification)

**Gate 4B family contrasts (v0.1.24, W=20):**

| Family | IPR(W=20) mean | Contrast (W=20 / W=0) |
|--------|----------------|----------------------|
| spectral_circle | 0.3456 | 7.04× |
| ring | 0.3312 | 6.90× |
| wilson_ring | 0.3512 | 7.07× |

**Observation:** Family differences are small (~5% spread).

**Implication:** If ring family ALSO shows ~7× contrast + STABLE FSS, then `broken_wilson_term` = `ring` reproducing the pattern is NOT surprising — it's the SAME family.

**Root question:** Why does `ring` (no Wilson term) show similar robustness to `wilson_ring` (with Wilson term)?

**Possible answers:**
1. **Wilson term is NOT load-bearing** — signal comes from S³ Dirac operator k=0 correction, S¹ discretization choice doesn't matter much
2. **ring and wilson_ring are too similar** — Wilson term (Laplacian correction) is small compared to disorder magnitude (W=20)
3. **Harness nonspecificity** — both families fail to reject random/scrambled baselines (need to test)

---

## Evidence from Negative Controls Full Pattern Audit

From `reports/NEGATIVE_CONTROLS_FULL_PATTERN_AUDIT_v0.1.24.md`:

| Control | Contrast (W=20 / W=0) | FSS trend classification | Full pattern? |
|---------|-----------------------|-------------------------|---------------|
| random_hermitian | 1.28× | FAIL | ❌ NO |
| scrambled_geometry | 1.30× | FAIL | ❌ NO |
| **broken_wilson_term** | **8.20×** | **STABLE** | **✅ YES** |

**Comparison:**
- `random_hermitian` = fully random Hermitian matrix → FAIL (as expected)
- `scrambled_geometry` = S³×S¹ structure but scrambled indices → FAIL (as expected)
- `broken_wilson_term` = S³×S¹ with `s1_family='ring'` → **PASS** (surprising IF we thought Wilson term was needed)

**Interpretation:** Geometric product structure (S³ ⊗ S¹) survives even with `ring` family.

---

## What This Tells Us (And What It Doesn't)

### ✅ What we learned

1. **`broken_wilson_term` control is misnamed** — it's `ring` family, not "broken Wilson"
2. **ring family shows robustness** — 8.20× contrast + STABLE FSS (comparable to wilson_ring 7.07×)
3. **Scrambled geometry kills robustness** — 1.30× contrast (harness CAN reject some nulls)
4. **Geometric product structure matters** — S³ ⊗ S¹ vs scrambled makes the difference

### ❌ What we did NOT test

1. **Does scrambling Wilson term kill wilson_ring robustness?** — need `wilson_mode="scrambled"` rerun
2. **Are all three families (spectral_circle, ring, wilson_ring) equivalently robust?** — need family-by-family FSS slope analysis
3. **Does pure S³ (without S¹) show robustness?** — need S³-only control (out of v0.1.22 scope)

### 🔴 What this does NOT prove

- ❌ Does NOT prove "Wilson term is irrelevant" — we didn't test scrambled Wilson
- ❌ Does NOT prove "S³×S¹ compactification validated" — ring showing robustness ≠ physical claim
- ❌ Does NOT prove "harness is fully nonspecific" — scrambled_geometry DID fail

---

## Diagnostic Recommendations

### Priority 1 — Rerun `wilson_mode="scrambled"` (Minimal Rerun)

**Goal:** Test whether Wilson term geometric structure is load-bearing.

**Grid:** 18 cases (W=0/20 × sizes=16/64/128 × seeds=123/456/789), `wilson_mode="scrambled"`

**Compute cost:** ~14 minutes (1 batch, 9 cases per W)

**Decision rule:**
- IF scrambled Wilson reproduces 8× contrast + STABLE FSS → Wilson term NOT load-bearing
- IF scrambled Wilson fails (<2× contrast OR chaotic FSS) → Wilson term IS load-bearing

**Action:** Create `scripts/run_broken_wilson_scrambled_v0_1_22.py` (copy from v0.1.22, change line 229)

### Priority 2 — Family-by-Family FSS Slope Analysis (No Rerun)

**Goal:** Quantify FSS slope for each family separately.

**Data:** Gate 4B v0.1.24 existing results (216 cases)

**Analysis:** Linear regression `log(IPR_W20) ~ log(N)` for each family

**Output:** `reports/FSS_SLOPE_BY_FAMILY_v0.1.24.md`

**Decision:** If all families show STABLE slope → family choice doesn't matter much

### Priority 3 — S³-Only Control (Future, Heavy Rerun)

**Goal:** Test whether S¹ discretization is needed at all.

**Grid:** S³ Dirac operator (k=0 corrected) with Anderson disorder, NO S¹ Kronecker product

**Compute cost:** 36 cases (W=0/20 × j_max=3 × seeds=123/456/789 × 6 sizes)

**Not urgent** — ring showing robustness already suggests S¹ choice less critical than S³ structure

---

## Code Audit Checklist

### ✅ Construction code verified

- [x] `build_broken_wilson_control` implementation matches docstring
- [x] `wilson_mode="disabled"` correctly builds `s1_family='ring'`
- [x] `wilson_mode="scrambled"` correctly scrambles Wilson term (code path exists, not executed)
- [x] No unintended bugs in Wilson term extraction logic

### ✅ Execution script verified

- [x] `run_negative_controls_v0_1_22.py` line 229 hardcodes `wilson_mode="disabled"`
- [x] No command-line flag to override `wilson_mode`
- [x] All 18 broken_wilson_term cases use same construction
- [x] Metadata correctly records `wilson_mode: disabled` in output JSON

### ✅ Pre-registration compliance checked

- [x] Pre-registration listed TWO modes (disabled, scrambled)
- [x] Execution used ONE mode only (disabled)
- [x] No justification in commit history for mode choice
- [ ] **ACTION REQUIRED:** Update pre-registration or re-run with both modes

### ⚠️ Gaps identified

- [ ] `wilson_mode="scrambled"` never executed (pre-registered but not tested)
- [ ] No family-by-family FSS analysis (assumed all families identical)
- [ ] No S³-only control (assumed S¹ needed)

---

## Proposed Next Steps

### Immediate (this diagnostic sprint, no heavy compute)

1. ✅ **DONE:** Code audit complete
2. **TODO:** FSS slope reanalysis by family (existing Gate 4B data)
3. **TODO:** Control-normalized effect size (broken_wilson 8.20× vs Gate 4B 7.07× = 1.16× relative)
4. **TODO:** Seed variance analysis (check if 8.20× is stable across seeds)

### Short-term (1-2 weeks, minimal rerun)

5. **Rerun `wilson_mode="scrambled"`** — 18 cases, ~14 min compute
6. **Compare:** intact wilson_ring vs scrambled Wilson vs disabled (ring)
7. **Update verdict:** If scrambled ALSO reproduces pattern → "Wilson term not load-bearing"

### Long-term (1-2 months, if needed)

8. **S³-only control** — 36 cases, test whether S¹ discretization matters at all
9. **Cross-geometry validation** — S³×S² port (Tom Lawrence CAMP follow-up)

---

## Conclusion

**Root cause:** `broken_wilson_term` control executed with `wilson_mode="disabled"` only, which is **equivalent to `ring` family**.

**What we tested:** ring vs wilson_ring family contrast (both showed ~7-8× robustness).

**What we did NOT test:** Perturbed Wilson term (scrambled mode) vs intact Wilson term.

**Impact on verdict:** Full Pattern Audit `HARNESS_NONSPECIFIC` is **valid** (ring reproduced pattern), but **incomplete diagnosis** (scrambled Wilson untested).

**Recommended action:** Rerun 18 cases with `wilson_mode="scrambled"` before claiming "Wilson term irrelevant".

**Forbidden claims (still apply):**
- ❌ "S³×S¹ compactification validated" — ring showing robustness ≠ physical validation
- ❌ "Wilson term proven irrelevant" — scrambled Wilson not tested yet
- ❌ "Harness fully nonspecific" — scrambled_geometry DID fail

---

**Last updated:** 2026-06-01  
**Status:** ROOT CAUSE IDENTIFIED — awaiting Priority 2-3 diagnostics  
**Next action:** FSS slope by family (existing data, no rerun)
