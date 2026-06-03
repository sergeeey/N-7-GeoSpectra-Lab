# EstimandOps Canvas — v0.1.22 Negative Controls
# FL Full-Ladder Step -1

**Date:** 2026-06-03
**Version:** v0.1.22
**Precondition:** Gate 4B v0.1.21 GATE4B_FSS_PASS_WITH_CAVEATS (commit f7eff32)
**Input:** SKEPTIC_AUDIT_GATE4B_v0.1.22.md (context-asymmetric review, 2026-06-03)
**Question type (L0):** [x] Descriptive  [ ] Predictive  [ ] Causal

---

## L0: Question Classification

**Question type: DESCRIPTIVE**

We ask: "Can the harness reject controls that should NOT reproduce the Gate 4B
localization-like signal?" This is a discrimination test on the harness, not a
causal claim about S³×S¹ geometry.

Additionally, from the skeptic audit: "Is spectral_circle a structural artifact
or a valid weaker-localization discretization?"

No causal DAG required. No identifiability check required.

**Hard rule applied:** Results will not be interpreted causally. No inference about
WHY spectral_circle behaves differently is permitted from this estimand alone.

---

## L1: Estimand Attributes

### Primary Estimand (Harness Discrimination)

**1. Population**
Finite-lattice S³×S¹ product operator families on same grid as Gate 4B:
- Sizes: s1_size ∈ {16, 32, 64, 128} (N = 112 → 896 for j_max=3)
- j_max = 3 (primary), j_max = 2 (secondary)
- 3 seeds: 123, 456, 789
- Families: ring, wilson_ring (spectral_circle as secondary target — see estimand B)

Negative control operators (intervention group):
- Control A: random_hermitian — random Hermitian matrix, same N, no S³×S¹ structure
- Control B: scrambled_geometry — S³×S¹ operator with row/column permutation
  (destroys geometric coupling, preserves matrix dimension and sparsity)
- Control C: broken_wilson — wilson_ring with coupling constants randomized
  (destroys Wilson coefficient structure, preserves diagonal disorder)

**2. Intervention**
Anderson diagonal disorder W=20 applied identically to Gate 4B protocol:
- U(r) ∈ [-W, W] uniform random, same seeding as Gate 4B
- Metric correction v0.1.21: eigenvector-based true IPR = mean(Σ|ψᵢ|⁴), bottom 10%

**3. Comparator**
Gate 4B baseline values for ring and wilson_ring (from verified artifacts):
- ring IPR(W=20) plateau: ≈0.32–0.34 (flat across s1_size=16→128)
- wilson_ring IPR(W=20) plateau: ≈0.24–0.27 (flat across s1_size=16→128)
- Aggregate contrast: 7.15× (pre-registered Gate 4B result)
- Family consistency: 3/3 PASS (pre-registered Gate 4B result)

**4. Endpoint**
Primary: true_IPR(W=20) by s1_size — the numerator of the contrast formula
Secondary: true_IPR contrast ratio (W=20 vs W=0)
Tertiary: r-statistic per family (NOT aggregate — per FT-1 finding)

**5. Summary Measures**
A. IPR(W=20) trend across s1_size:
   - PLATEAU (flat or increasing): consistent with localization
   - DECREASING: inconsistent with localization (structural or delocalization)

B. IPR contrast ratio:
   - ≥2.0×: pre-registered PASS threshold
   - ≥7.15×: Gate 4B reference level (full reproduction)

C. Per-family r-statistic (NOT aggregate, to avoid spectral_circle contamination):
   - Report per family separately

**6. MCID (Minimum Clinically Important Difference)**
A negative control result is a FALSE POSITIVE if ALL of:
- IPR(W=20) plateau observed (flat across 3+ sizes)
- AND IPR contrast ≥7.15× (full Gate 4B level)
- AND per-family r-stat shows shift toward Poisson ≥ 0.10 (from a non-degenerate baseline)

A negative control result is a CORRECT REJECTION if ANY of:
- IPR(W=20) decreases with N at rate approaching 1/N
- OR IPR contrast < 2.0× (below pre-registered threshold)
- OR IPR(W=20) < 0.10 at all sizes (too weak for localization claim)

**Threshold for negative control campaign PASS:**
≥2/3 controls correctly rejected by ALL of: contrast and FSS criteria.

**Threshold for negative control campaign FAIL (falsifies Gate 4B specificity):**
ANY control achieves ring/wilson_ring-like IPR plateau at W=20 across ≥3 sizes.

---

### Secondary Estimand (spectral_circle diagnostic)

**From skeptic audit FT-2:** spectral_circle shows IPR(W=20) decreasing from
0.175 → 0.070 as s1_size grows 16→128. This is inconsistent with the localization
plateau observed in ring and wilson_ring.

**Population:** spectral_circle family only, same s1_size grid

**Intervention A:** W=20 Anderson disorder on spectral_circle on S³×S¹ (already computed, Gate 4B)

**Intervention B:** W=20 Anderson disorder on spectral_circle on scrambled_geometry
(same matrix dimension, geometric coupling destroyed by permutation)

**Comparator:** spectral_circle Gate 4B values: IPR(W=20) = 0.175 → 0.070

**Endpoint:** IPR(W=20) by s1_size for scrambled spectral_circle

**Summary measure:** Does scrambled spectral_circle show same or different IPR(W=20) trend?

**Decision rule:**
- SAME trend (decreasing IPR on scrambled as on S³×S¹) → `[STRUCTURAL ARTIFACT]`:
  spectral_circle result is driven by matrix structure, not geometry.
  Gate 4B "3/3 PASS" should be re-stated as "2/3 PASS (ring + wilson_ring),
  spectral_circle indeterminate."
- DIFFERENT trend (scrambled shows higher IPR or plateau) → `[GEOMETRIC SIGNAL]`:
  spectral_circle does respond to geometry, localization is just weaker.
  Gate 4B "3/3 PASS" remains valid with weaker-localization qualifier.

---

## ICE Strategy

**Post-baseline events that change endpoint interpretation:**

| ICE | Strategy | Reason |
|-----|----------|--------|
| Numerical failure (NaN, convergence error) | composite — count as non-localized | Failure = not robust |
| Matrix rank deficiency (control A degenerate) | while-active — truncate at ICE | Different estimand if matrix singular |
| spectral_circle r_stat = 1.000 at W=0 | hypothetical — exclude r-stat from primary analysis for spectral_circle | Degenerate baseline renders r-shift uninterpretable |

---

## Natural Language Statement

*(Written BEFORE seeing any v0.1.22 batch results)*

> "We estimate the true_IPR(W=20) plateau behavior (flat vs decreasing with N)
> for three negative control operators (random_hermitian, scrambled_geometry,
> broken_wilson) and for spectral_circle on scrambled geometry, comparing each
> to the Gate 4B reference values for ring and wilson_ring (IPR plateau ≈0.32
> and ≈0.25 respectively), using the same Anderson W=20 disorder and true
> eigenvector-based IPR metric as Gate 4B v0.1.21."

---

## What This Result Does NOT Mean

1. **Does NOT prove S³×S¹ is the unique geometry capable of Anderson localization.**
   Other geometries were not tested. Negative controls failing ≠ S³×S¹ uniqueness.

2. **Does NOT validate the claim "localization proven."**
   IPR plateau is consistent with localization but does not prove exponential
   eigenfunction decay (the mathematical criterion for localization).

3. **Does NOT change Gate 4B verdict retroactively.**
   Whether spectral_circle is an artifact or not, Gate 4B pre-registered thresholds
   are immutable. Only CLAIMS_ALLOWED_AND_FORBIDDEN may be updated with qualifier.

4. **Does NOT prove that if controls reject, the signal is physical.**
   Finite-lattice ≠ continuum. No physical compactification claim is permitted.

5. **Does NOT apply to W≠20 disorder.**
   All results conditional on W=20. No generalization to other disorder strengths.

---

## Sensitivity Analysis Plan

**≥2 required (Full-Ladder):**

1. **Alternative control definition:** Repeat Control B (scrambled_geometry) with
   column-only permutation vs. full row+column permutation. If results differ,
   permutation depth affects conclusion — flag as `[SCRAMBLING-SENSITIVE]`.

2. **j_max sensitivity:** Compare results at j_max=2 vs j_max=3 for each control.
   If conclusion reverses between j_max values — `[JMAX-SENSITIVE]`.

---

## Estimator

**Estimand type:** Descriptive (comparison of IPR trajectories)
**Estimator:** Direct mean ± std of true_IPR(W=20) per (control, s1_size, j_max)
**No statistical test required:** Decision is based on qualitative trajectory
(plateau vs. decay) and quantitative threshold (≥2.0× or ≥7.15× contrast).
**No p-value, no MLE, no regression:** Pattern comparison only.

---

## Artifacts Required Before Batch Launch

Per FL Full-Ladder, the following must exist BEFORE running batches:
- [x] This estimand file (`ESTIMAND_v0.1.22.md`)
- [x] Pre-registration (`S3_S1_NEGATIVE_CONTROLS_PREREGISTRATION_v0.1.22.md`)
- [x] Skeptic audit (`SKEPTIC_AUDIT_GATE4B_v0.1.22.md`)
- [ ] Claim file (`CLAIM_v0.1.22.md`) — to be written next
- [ ] Batch protocol specifying exact operator implementations

---

**Status:** FINAL — pre-run, written before batch execution
**FL step:** -1 (EstimandOps) COMPLETE
**Next step:** FL step 0 — write CLAIM_v0.1.22.md
**Date:** 2026-06-03
