---
experiment_id: 20260625-e-coker
date: 2026-06-25
tier: Full-Ladder
status: in_progress
---

# claim.md — E-COKER: dim coker(D^+_{S⁻}) = 0

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — adjoint argument via representation theory

## Falsifiable Claim

**C1:** dim coker(D^+_{S⁻}) = 0 on G₂/SU(3) = S⁶.

**C2 (adjoint):** D^- = (D^+)†: Γ(S⁻⊗S⁻) → Γ(S⁺⊗S⁻), so ker(D^-) = coker(D^+).

**C3 (non-trivial G₂-reps):** Same KP gap argument as E-KP1: for all non-trivial ρ in S⁻⊗S⁻, λ²(ρ) ≥ 4 - 10/3 = 2/3 > 0 → no zero modes.

**C4 (trivial G₂-rep):**
- S⁻⊗S⁻|_{SU(3)} has 1 trivial (0,0) copy [domain of D^-]
- S⁺⊗S⁻|_{SU(3)} has 2 trivial (0,0) copies [codomain of D^-]
- D^-|_{trivial}: ℂ¹ → ℂ²; rank(D^-) = rank(D^+) = 1 [from E-KP1]
- dim ker(D^-|_{trivial}) = 1 - 1 = 0

**Corollary:** dim coker(D^+_{S⁻}) = dim ker(D^-_{S⁻}) = 0.

Combined with E-KP1 (dim ker = 1): ind(D^+_{S⁻}) = 1 - 0 = 1 ✓ (consistent with Atiyah-Singer).

## Kill Condition

C1 is FALSIFIED if:
- dim ker(D^-|_{trivial}) ≠ 0 (i.e., rank(D^+|_{trivial}) < 1 despite ind=1 > 0)
- OR the adjoint relation D^- = (D^+)† fails to hold

Both impossible: rank=1 follows from ind=1 and dim domain=2 > dim target=1.
