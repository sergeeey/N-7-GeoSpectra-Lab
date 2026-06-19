# Claim — G30: Three Generations via G₂-Instanton on S⁶

**Date:** 2026-06-20  
**FL tier:** Full  
**Question type:** [x] predictive  [ ] descriptive  [ ] causal

---

## Falsifiable claim

> There exists a G₂-equivariant bundle V over S⁶ = G₂/SU(3) such that
> the twisted Dirac operator D ⊗ V has index = 3, giving three SM generations
> from the instanton sector of S⁶.

---

## Kill conditions (any one = KILL)

1. Â(S⁶) ≠ 1 → formula breaks
2. G₂-equivariant bundles give index ≠ 0 for any irreducible rep → symmetry argument fails
3. `mult(3) ≠ mult(3̄)` in some G₂-irrep → theorem fails

---

## Verification

**Â(S⁶) = 1 [VERIFIED]:**  
H^{4k}(S⁶) = 0 for k ≥ 1 → all Pontryagin classes vanish → Â = 1.

**Frobenius formula [VERIFIED]:**  
S⁺|_{SU(3)} = 3 ⊕ 1, S⁻|_{SU(3)} = 3̄ ⊕ 1  
→ index(D⊗V_ρ) = [ρ ≅ **3**] − [ρ ≅ **3̄**]

**G₂ symmetry theorem [VERIFIED, 6 irreps]:**  
For all G₂-irreps, mult(**3**) = mult(**3̄**) under SU(3)  
→ index(D ⊗ V_G₂) = 0 for ALL G₂-equivariant bundles  
(Source: Slansky 1981, branching rules **7**, **14**, **27**, **64**, **77**, **77'**)

**Consequence:**  
index = 3 requires V = **3** ⊕ **3** ⊕ **3** (reducible, breaks G₂ → SU(3)).  
No irreducible G₂-equivariant bundle can give index ≠ 0.

---

## Verdict: KILL (falsified by G₂ symmetry theorem)

Three generations from a G₂-instanton on S⁶ are **impossible within G₂-symmetric framework**.

---

## What this does NOT mean

1. Does not mean S³×S⁶ cannot give 3 generations by a different mechanism
2. Does not mean G₂-equivariant compactification is ruled out (one generation works)
3. Does not apply to non-equivariant bundles (they break G₂ symmetry)

---

## Pearl

**Open direction:** SU(2) adjoint of S³ has dimension 3 (the adjoint rep **3** of SU(2)).
Does the S³ factor contribute "3 copies" geometrically, separate from the S⁶ mechanism?
Pearl candidate: `3 generations = dim(adjoint of SU(2)_L from S³)`
`next_check: 2026-07-20`
