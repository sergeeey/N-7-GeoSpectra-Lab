# G61 decision — WEAK PROMOTE (two candidates, not conclusive)

**Date:** 2026-06-21
**Verdict:** WEAK PROMOTE — two geometric candidates identified, neither conclusive

## Key finding

λ_Minkowski-exact = ρ₆*² · ln(A_np/V_FLUX) = 1.090² × ln(0.38/0.2861) = **0.3374**

This is the λ that makes (A_np=0.38, Minkowski condition) consistent.
Note: G56 used λ_fitted=0.30 (for minimum position, NOT Minkowski consistency).

## Two candidates

| Candidate | Value | Δλ/λ_exact | A_np_pred | ΔA_np/0.38 |
|-----------|-------|------------|-----------|------------|
| **λ=1/3 (dimensional)** | 0.3333 | **1.2%** | 0.3787 | 0.3% |
| **λ=π/9 (E7 gaugino)** | 0.3491 | **3.5%** | 0.3838 | 1.0% |
| λ=3/10 (G56 fitted) | 0.3000 | 11.1% | 0.3682 | 3.2% |

### Candidate A: λ = 1/3 = dim(S³)/dim(S³×S⁶)

Physical interpretation: The instanton action of a brane wrapping the S³ 3-cycle
within the 9-dimensional internal manifold S³×S⁶ gives an action proportional to
the fraction of internal dimensions covered: S_inst ∝ 3/9 = 1/3.

Status: WEAK. Dimensional argument is suggestive but not derived from first principles.
λ = 1/3 is within **1.2%** of the Minkowski-exact value (0.3333 vs 0.3374).

### Candidate B: λ = π/9 = 2π/h^∨(E7)

Physical interpretation: Gaugino condensation in an E7 hidden sector (E7 ⊂ E8 in
E8×E8 heterotic string) gives V_np = A·exp(−2π τ/18). With τ = 1/ρ₆²:
λ = 2π/18 = π/9 ≈ 0.3491.

Status: WEAK. E7 ⊂ E8 is natural in heterotic string theory. But S³×S⁶ is not
obviously embedded in E8×E8 heterotic without additional structure.
λ_E7 is within **3.5%** of the Minkowski-exact value and gives A_np within **1.0%**.

## Kill Analysis

**NOT killed:**
- G56 KKLT stabilization (λ=0.30 fitted)
- The G60 Pearl: A_np ≈ V_FLUX·exp(λ/ρ₆*²)
- Both dimensional and E7 candidates (neither falsified)

**Key insight:** The G56 fitted λ=0.30 is inconsistent with the Minkowski condition
for A_np=0.38. The Minkowski-consistent λ is 0.337, not 0.30. One of three things:
1. A_np_fitted is slightly off from its Minkowski-consistent value
2. G56 minimum and Minkowski are independent (AdS minimum, then uplift)
3. The true physical λ is 1/3 or π/9, not 0.30

## Pearl Gate

**Pearl registered:** λ_Minkowski-exact = 0.337 ≈ 1/3 = dim(S³)/dim(S³×S⁶)

The factor 1/3 has a clean geometric interpretation: the NP exponent measures
what fraction of the internal space is wrapped by the instanton.

→ Registry entry: "λ ≈ 1/3 is within 1.2% of Minkowski-exact. Dimensional origin:
dim(wrapped cycle)/dim(internal manifold) = dim(S³)/dim(S³×S⁶) = 3/9 = 1/3."

## Next gates

1. **G62** (Variant 2): Accept λ≈1/3 as best estimate, A_np from Minkowski pearl.
   Compute observables: moduli mass m²(ρ₆*), KK scale m_KK = 1/ρ₆*.
2. **Alternative**: Embed S³×S⁶ in E8×E8 heterotic string explicitly,
   show E7 condensate gives the right τ = 1/ρ₆² identification.
