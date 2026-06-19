# S6-HARM-G5: Decision

**Date:** 2026-06-15
**Verdict:** PROMOTE
**Evidence:** 17/17 sympy checks + 14/14 pytest + 507 total PASS

## Result summary

Cartan structure equations verified for all three (β_k,φ_k) pairs on S⁶.

Universal coordinate spin connection law confirmed:
```
ω^{φ_k}_{β_k, φ_k}(coord) = cosβ_k    for k = 1, 2, 3
```

Frame forms (dividing by h_{φ_k}):
| k | h_{φ_k} | ω^{φ_k}_{β_k}(coord) | ω^{φ_k}_{β_k}(frame) |
|---|---------|----------------------|----------------------|
| 1 | ρ sinβ₁ | cosβ₁ | cotβ₁/ρ |
| 2 | ρ cosβ₁ sinβ₂ | cosβ₂ | cotβ₂/(ρ cosβ₁) |
| 3 | ρ cosβ₁ cosβ₂ sinβ₃ | cosβ₃ | cotβ₃/(ρ cosβ₁ cosβ₂) |

## cotβ_k universality chain — S6-HARM closure

| Gate | cotβ_k appears as | Role |
|------|-------------------|------|
| G2 | Root generator L_{1j}: φ_k-component = cotβ_k × (factor) | Frame artifact in SO(6) harmonics |
| G3 | Scalar ODE centrifugal term: l_k(l_k+1)/cos²β_k | Drives eigenvalue nesting |
| G4 | Lichnerowicz ±(l+3)/ρ shift; 3 = n/2 = #(β_k,φ_k) pairs | Dirac ground state |
| G5 | ω^{φ_k}_{β_k}(coord) = cosβ_k → frame cotβ_k/ρ | Spin connection source |

The same cotβ_k coefficient appears at every level: algebra (G2), analysis (G3), spectral theory (G4),
and Riemannian geometry (G5). This is a structural feature of the Hopf-type nested coordinate system,
not specific to any one computation.

## What this does NOT mean

- Does NOT complete the Killing spinor check (∇_μψ = ±(1/2ρ)Γ_μψ requires off-diagonal ω)
- Does NOT compute the off-diagonal spin connection components
  ω^{β_k}_{β_{k'}} (tanβ_k cross-terms) or ω^{φ_k}_{β_{k'}} (cross-nesting)
- Does NOT show that spinor harmonics satisfy the same ODE structure as G3 scalar harmonics
- Does NOT fix λ or select any compactification
- Does NOT connect this to Tom Lawrence S³ (different dimension, different Killing count)

## Next steps (open, not committed)

- Close S6-HARM branch (G0→G5 complete) and summarize for Tom update
- Tom Lawrence correspondence: await reply on rows 17+19 before S³ structure changes
- ACH matrix: G4/G5 close λ-identifiability evidence chain
