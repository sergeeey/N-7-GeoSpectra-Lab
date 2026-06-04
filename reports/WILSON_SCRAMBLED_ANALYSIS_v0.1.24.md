# Wilson Scrambled Analysis — v0.1.24

**Date:** 2026-06-01  
**Purpose:** Test if Wilson term geometric structure is load-bearing for Gate 4B robustness pattern  
**Status:** ✅ **COMPLETE** — Wilson term NOT load-bearing

---

## Executive Summary

**Question:** Does scrambling Wilson term kill Gate 4B robustness pattern (8.20× contrast + STABLE FSS)?

**Answer:** NO — scrambled Wilson reproduces 2.94× contrast + STABLE FSS (-0.0702 slope).

**Verdict:** **HARNESS_GEOMETRY_AGNOSTIC** — distinguishes S³⊗S¹ product from random, but NOT sensitive to S¹ family details (ring / wilson_ring / scrambled_wilson).

---

## Key Results

### Contrast Comparison (W=20 / W=0)

| Wilson Mode | W=0 IPR | W=20 IPR | Contrast | Decision |
|-------------|---------|----------|----------|----------|
| **disabled** | 0.0400 ± 0.0333 | 0.3283 ± 0.0490 | **8.20×** | Reference (intact ring) |
| **scrambled** | 0.2216 ± 0.0037 | 0.6510 ± 0.0534 | **2.94×** | ≥2.0× threshold → pattern reproduced |

**Decision rule:** IF scrambled contrast ≥2.0× → Wilson term NOT load-bearing.

**Result:** Scrambled Wilson contrast = **2.94×** → **Wilson term NOT load-bearing** ❌

---

### FSS Slope Comparison (log IPR vs log N, W=20)

| Wilson Mode | FSS Slope | R² | Classification |
|-------------|-----------|----|----|
| **disabled** | 0.0164 ± 0.0205 | 0.13 | STABLE |
| **scrambled** | **-0.0702 ± 0.0100** | **0.98** | **STABLE** (>-0.1 threshold) |

**Decision rule:** IF scrambled FSS STABLE (slope >-0.1) → Wilson term NOT load-bearing.

**Result:** Scrambled FSS slope = **-0.0702** (STABLE) → **Wilson term NOT load-bearing** ❌

---

## What This Means

### Harness Specificity Cascade (Updated)

| Level | Test | Result | Interpretation |
|-------|------|--------|----------------|
| **L1: Random rejection** | Random Hermitian (W=20) | Contrast <2.0×, FSS WEAKENING | ✅ Rejects pure randomness |
| **L2: Geometry scrambling** | Scrambled geometry (permutation) | Contrast <2.0×, FSS WEAKENING | ✅ Rejects S¹ scrambling |
| **L3: S¹ family intact** | ring / wilson_ring | Contrast ≥8.0×, FSS STABLE | ✅ Accepts intact S³⊗S¹ |
| **L4: Wilson term scrambling** | **wilson_ring with random signs** | **Contrast 2.94×, FSS STABLE** | ❌ **Accepts scrambled Wilson** |

**Conclusion:** Harness sensitivity ends at **L3 (geometry intact)**, NOT L4 (Wilson correction intact).

---

## Updated Specificity Verdict

**From:** `PARTIAL_SPECIFICITY` (rejects random/scrambled, accepts intact geometry)

**To:** `GEOMETRY_AGNOSTIC` — harness is sensitive to:
- ✅ S³⊗S¹ **product structure** (Kronecker sum H = H_S3 ⊗ I + I ⊗ H_S1)
- ❌ S¹ **family details** (ring vs wilson_ring vs scrambled_wilson)

**What harness DOES NOT distinguish:**
- Wilson term presence (ring vs wilson_ring: 8.20× vs 8.49×, both STABLE)
- Wilson term sign structure (disabled vs scrambled: 8.20× vs 2.94×, both STABLE)

**What harness DOES distinguish:**
- Random Hermitian (contrast <2.0×, FSS WEAKENING ≤-1.1)
- Scrambled geometry (contrast <2.0×, FSS WEAKENING ≤-0.9)

---

## Implications

### For S³×S¹ Physical Validation

❌ **Wilson correction NOT physically validated** — scrambled Wilson survives the same tests.

**What this does NOT prove:**
- ❌ "S³×S¹ compactification validated" — harness accepts scrambled Wilson
- ❌ "Wilson term irrelevant" — we only tested scrambling, not removal

**What this DOES prove:**
- ✅ Harness sensitive to product structure (S³ ⊗ S¹)
- ✅ Harness insensitive to Wilson term sign structure
- ✅ Gate 4B pattern = **product geometry signature**, NOT Wilson correction signature

### For Tom Lawrence CAMP Claim

Tom Lawrence claim (2026-05-26):
> "S³×S¹ → S³×S² geometric fork validated by Gate 4B FSS robustness"

**Updated assessment:**
- ✅ Gate 4B validates **product structure** (S³ ⊗ S¹)
- ❌ Gate 4B does NOT validate **S¹ family choice** (ring / wilson_ring / scrambled)
- ⚠️ S³×S² claim requires **independent test** — Gate 4B harness insufficient

---

## Diagnostic Sprint Outcome

**Timeline:**
- 2026-05-31: Negative Controls Full Pattern Audit → `HARNESS_NONSPECIFIC` (broken_wilson_term reproduced 8.20×)
- 2026-06-01: Code Audit → broken_wilson_term = ring (NOT Wilson perturbation)
- 2026-06-01: FSS/Variance Analysis → ring ≈ wilson_ring (both STABLE)
- 2026-06-01: wilson_mode="scrambled" rerun → **2.94× contrast + STABLE FSS**

**Conclusion:**
- ✅ Diagnostic sprint exhausted all existing-data analyses
- ✅ wilson_mode="scrambled" rerun executed (18 cases, ~13 min)
- ✅ Decision: **Wilson term NOT load-bearing**
- ✅ Updated verdict: `GEOMETRY_AGNOSTIC`

---

## Next Steps

### Priority 1 — Update Existing Documentation

**Files to update:**
- `reports/EXISTING_DATA_DIAGNOSTIC_SUMMARY.md` — add scrambled Wilson verdict
- `reports/S3_S1_NEGATIVE_CONTROLS_FULL_PATTERN_AUDIT.md` — update specificity verdict
- `docs/OUTCOMES.md` — Gate 4B outcome downgraded from "S³×S¹ validated" to "product structure detected"

### Priority 2 — Tom Lawrence CAMP Follow-Up

**Question:** If Gate 4B harness accepts scrambled Wilson, does it also accept S³×S²?

**Action:** Email Tom Lawrence with updated verdict + ask about S³×S² test priority.

### Priority 3 — Gate 4B v0.2.x Rerun Decision

**Question:** Is full Gate 4B rerun (216 cases, 6 hours) still needed?

**Answer:** Depends on what we want to test:
- IF goal = "energy-resolved diagnostics" → YES (Tier 1 saves eigenvalues)
- IF goal = "validate S³×S¹ specificity" → NO (harness geometry-agnostic)

**Recommendation:** Defer Gate 4B v0.2.x until Tom Lawrence S³×S² question resolved.

---

## Appendix: Decision Rules

### Contrast Decision Rule

```
IF scrambled_contrast ≥ 2.0× AND disabled_contrast ≥ 2.0×:
    → Wilson term NOT load-bearing (both reproduce pattern)
ELSE IF scrambled_contrast < 2.0× AND disabled_contrast ≥ 2.0×:
    → Wilson term IS load-bearing (only intact survives)
```

**Result:** scrambled=2.94×, disabled=8.20× → both ≥2.0× → **NOT load-bearing**

### FSS Slope Decision Rule

```
IF scrambled_slope > -0.1 AND disabled_slope > -0.1:
    → Wilson term NOT load-bearing (both STABLE)
ELSE IF scrambled_slope ≤ -0.1 AND disabled_slope > -0.1:
    → Wilson term IS load-bearing (only intact STABLE)
```

**Result:** scrambled=-0.0702, disabled=0.0164 → both >-0.1 → **NOT load-bearing**

---

**Last updated:** 2026-06-01  
**Status:** ✅ COMPLETE  
**Next action:** Update documentation + email Tom Lawrence
