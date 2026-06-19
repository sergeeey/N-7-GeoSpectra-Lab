# Null Result G31 — S³ adjoint bundle cannot give 3 SM generations

**Date:** 2026-06-20  
**Verdict:** REJECT

---

## Claim that failed

D ⊗ V_{adj=1} on S³ has 3 zero modes → 3 SM generations from the S³ factor.

## Why it failed

**Lichnerowicz barrier:**
- S³ scalar curvature R = 6/ρ₃², so R/4 = 3/(2ρ₃²)
- For V_{adj} (j=1): Lichnerowicz coupling F = -1/ρ₃² in J+=3/2 sector
- D² ≥ 3/2 - 1 = 1/2 (in units 1/ρ₃²) → strictly positive → no zero modes

**Parity obstruction (stronger, covers ALL SU(2) bundles):**
- Zero-mode count = dim(J+ = j+1/2) = 2j+2
- dim = 3 requires j = 1/2
- j = 1/2 bundle: D² = 1/ρ₃² > 0 → no zero modes
- Contradiction: dim=3 and zero modes cannot coexist for any V_j on S³

## New result from G31 (pearl)

Critical spin j_critical = 3/2 (Rarita-Schwinger):
- At j=3/2: D² = 0 in J=2 sector (boundary Killing spinors)
- 5-dimensional zero-mode sector (not 3)
- For j > 3/2: zero modes exist with count 2j+2 (never = 3 for integer j)

## Conditions for retry

Would need:
- Non-spherical compact space where Lichnerowicz allows j=1/2 zero modes (negative curvature)
- Or a different mechanism entirely (not Dirac zero modes)

## Combined null result log

| G27 | Z₃ orbifold on S⁶ | Smith theory kill |
| G30 | G₂-instanton on S⁶ | Symmetry kill |
| G31 | S³ adjoint bundle | Lichnerowicz + parity kill |

All Dirac routes to 3 generations on S³×S⁶ are closed.
