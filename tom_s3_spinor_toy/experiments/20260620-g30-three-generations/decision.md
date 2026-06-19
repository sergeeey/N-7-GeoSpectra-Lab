# Decision — G30: Three Generations via G₂-Instanton on S⁶

**Date:** 2026-06-20  
**Verdict:** REJECT → null_results  
**Go/no-go:** NO-GO

---

## What Was Tested

Claim: G₂-equivariant bundle V over S⁶ = G₂/SU(3) with index(D⊗V) = 3.

## Why It Failed

**Kill condition 3 is satisfied (G₂ symmetry theorem):**

For ALL G₂-irreducible representations, when restricted to SU(3):
```
mult(3) = mult(3̄)  always
```
Therefore: index(D ⊗ V_G₂) = 0 for every G₂-equivariant bundle.

The maximum index achievable from a G₂-equivariant bundle is |index| ≤ 1  
(requiring a SU(3)-only, non-G₂-equivariant bundle).

## Positive Results (that still stand)

1. **Â(S⁶) = 1 [VERIFIED]** — clean formula for twisted index
2. **One generation from canonical bundle** [VERIFIED]:  
   index(D ⊗ T^{1,0}S⁶) = 1  (non-equivariant, SU(3)-only)
3. **Index formula** [VERIFIED]:  
   index(D⊗V) = ∫c₃(V)/2  for SU(3) bundle with c₁=c₂=0

## What's Ruled Out (complete picture)

Two roads to 3 generations on S⁶, both blocked:

| Route | Obstacle | Gate |
|-------|----------|------|
| ℤ₃ orbifold S⁶/ℤ₃ | χ(S⁶)=2, not divisible by 3 (Smith theory) | G27 |
| G₂-instanton bundle | G₂ symmetry forces index=0 for all equivariant bundles | G30 |

## Why This is Valuable

Negative results sharpen the question. We now know:
- 3 generations from S⁶ alone require breaking G₂ symmetry  
- The breaking must be explicit: V = **3** ⊕ **3** ⊕ **3** (reducible bundle)  
- This does NOT arise from a single G₂-representation

## Open Directions

**Option C (unpursued):** SU(2) adjoint representation on S³ has dimension 3.  
Does S³ provide "3 copies" of the S⁶-generation geometrically?  
Mechanism: D_{S³×S⁶} ⊗ (V_{S³,adj} ⊠ V_{S⁶,fund}) — need full product operator analysis.

This would be a new gate G31, separate from G30.

## Tests [VERIFIED]

34/34 tests pass: `tests/test_g30_three_generations.py`
