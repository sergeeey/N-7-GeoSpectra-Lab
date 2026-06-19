# Claim — G31: Three Generations via Adjoint Bundle on S³

**Date:** 2026-06-20  
**FL tier:** Full  
**Question type:** [x] predictive  [ ] descriptive  [ ] causal

---

## Falsifiable claim

> The twisted Dirac operator D ⊗ V_{adj} on S³ (where V_{adj} = SU(2) adjoint, dim=3)
> has 3 zero modes, providing a geometric explanation for 3 SM generations from the S³ factor.

---

## Kill conditions (any one = KILL)

1. Lichnerowicz: D²_{adj} ≥ ε > 0 → no zero modes
2. Even when zero modes exist (j > 3/2): count ≠ 3 for any SU(2) bundle
3. j=1/2 is only bundle with potential dim=3, but D² = 1/ρ₃² > 0 → blocked

---

## Verification

**Lichnerowicz bound for V_{adj} (j=1) on S³ [VERIFIED]:**
```
D²(J+=3/2 sector) = R/4 + F = 3/2 - 1 = 1/2 ρ₃² > 0
D²(J-=1/2 sector) = R/4 + F = 3/2 + 2 = 7/2 ρ₃² > 0
min D² = 1/2 ρ₃² > 0  →  ker D = ∅
```

**Critical spin j_critical = 3/2 [VERIFIED]:**
```
D² = 0 ↔ R/4 = j_bundle ↔ j_bundle = 3/2
```
At j=3/2 (Rarita-Schwinger): 5-dimensional zero-mode sector (J=2), not 3.

**Dimension → zero-mode count formula [VERIFIED]:**
```
Zero-mode count = dim(J+ = j+1/2 rep) = 2j+2 for integer j
                = 2j+2 for half-integer j (e.g. j=1/2 → count=3)
```

**Parity obstruction [VERIFIED]:**
- For dim(J+) = 3: requires j_bundle = 1/2
- But j=1/2 → D² = 1/ρ₃² > 0 → no zero modes
- Contradiction. dim=3 and zero modes cannot coexist.

---

## Verdict: KILL

Three generations from D ⊗ V_{adj} on S³ are **impossible**.  
Stronger: No SU(2) bundle V_j on S³ simultaneously gives zero modes AND dim=3.

---

## What this does NOT mean

1. Does not mean S³×S⁶ cannot explain 3 generations by non-Dirac mechanism
2. Does not apply to non-spherical geometries (tori, Calabi-Yau)
3. The j=3/2 boundary case (Rarita-Schwinger, 5 modes) may be physically interesting

---

## Universal null result (G27 + G30 + G31)

| Gate | Mechanism blocked | Reason |
|------|-------------------|--------|
| G27 | ℤ₃ orbifold on S⁶ | Smith theory: χ(S⁶)=2 not divisible by 3 |
| G30 | G₂-instanton on S⁶ | G₂ symmetry: index=0 always |
| G31 | SU(2) adjoint on S³ | Lichnerowicz + parity obstruction |

**Conclusion:** All Dirac-based routes to 3 generations on S³×S⁶ are formally closed.
3 generations require physics beyond the sphere geometry (NCG finite triple, fluxes, etc.)
