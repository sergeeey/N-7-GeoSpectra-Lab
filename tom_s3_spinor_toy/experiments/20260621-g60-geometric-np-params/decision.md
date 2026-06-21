# G60 decision — NULL (structural)

**Date:** 2026-06-21
**Verdict:** NULL
**Tests:** 11/11 pass, 2 skip (promote criteria — λ not derived)

## Result summary

| Gate | Result | Key value |
|------|--------|-----------|
| A1 | PASS | V_flux = 0.286 ∈ (0.1, 1.0) |
| A2 | PASS | |ζ_FP(ρ₆*)| << 0.01 × V_flux |
| A3 | PASS | ζ_FP'(ρ₆*) > 0 (nonzero) |
| **B1** | **NULL** | **λ_geom = −0.0022 < 0** |
| B2 | PASS | A_geom = 0.2847 ≈ V_FLUX_CONST |
| B3 | PASS | ζ_FP'(ρ₆*) > 0 confirmed (root cause) |
| C1 | NULL (100.7% error) | λ_fitted = 0.30, λ_geom ≈ 0 |
| C2 | SKIP | (cascaded from C1 null) |

## What was falsified

"Minkowski + minimum conditions on V_total with V_np = −A·exp(−λ/ρ₆²) algebraically
derive positive λ ≈ 0.30 from the spectral/Casimir geometry of S³×S⁶."

**Falsified:** λ_geom = −0.0022 < 0. Root cause is structural, not numerical.

## Kill Analysis

**Killed:** This specific derivation path (Minkowski + minimum → solve for λ from ζ_FP').

**NOT killed:**
- G56 KKLT stabilization at ρ₆*≈1.09 (fitted λ=0.30, A_np=0.38 still valid)
- Thread 2 route: gaugino condensation from S⁶ isometry gauge group (different λ derivation)
- Thread 3 route: resurgence of ζ_FP Borel series (different mechanism)
- The fact that A_geom ≈ V_FLUX_CONST in the λ→0 limit (structural insight, see Pearl below)

## Root cause: structural monotonicity

ζ_FP(ρ₆) is monotonically increasing in [ρ₆_min=0.953, ρ₆**=1.447]:
- ρ₆_min=0.953: ζ_FP minimum (most negative)
- ρ₆*=1.090: ζ_FP rising, not extremum (UV-selection is c_{1/2}=0, NOT ζ_FP extremum)
- ρ₆**=1.447: ζ_FP = 0 (zero crossing)

Therefore: ζ_FP'(ρ₆*) > 0 always → λ_geom = −r6*³/2 · ζ_FP'/(V+ζ) < 0 always.

**No choice of ρ₆* in [0.953, 1.447] can give positive λ_geom from this formula.**

## Relaxation Map (surviving assumptions)

| Assumption killed | Surviving options |
|-------------------|------------------|
| V_np = −A·exp(−λ/r6²) | Try full SUGRA F-term (1/T³ prefactor + cross terms) |
| Minkowski uplift from NP alone | Anti-brane uplift (V_uplift separate from V_np) |
| λ from Casimir slope | λ from instanton action on S³ (Chern-Simons, Thread 1) |
| A_np from Minkowski | A_np ≈ V_FLUX_CONST (hint: NP amplitude ~ flux level) |

## Pearl Gate

**Pearl registered:** A_geom → V_FLUX_CONST in λ→0 limit.

The Minkowski condition (without minimum) gives:
  A_np · exp(−λ/ρ₆*²) ≈ V_FLUX_CONST = 15C³/(16π)

So: A_np ≈ V_FLUX_CONST · exp(+λ/ρ₆*²)

For λ=0.30, ρ₆*=1.090: A_np ≈ 0.2861 × exp(0.252) ≈ 0.363 (fitted: 0.38, 4.7% error).

**Pearl:** The Minkowski condition ALONE (not minimum) constrains A_np given λ — and this
works to within ~5% with the fitted λ=0.30. λ is the truly free parameter.

→ Registry entry: "A_np is determined by Minkowski condition given λ: A_np ≈ V_FLUX·exp(λ/ρ₆*²)"
→ Next check: can λ=3/10 be derived from Thread 2 (gaugino condensation on S⁶)?
