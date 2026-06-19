# S6-HARM-G3 — Decision

**Date:** 2026-06-15
**Verdict:** PROMOTE
**Status:** PASS_S6_SEPARATION_CONFIRMED

## Evidence
- T1: Δ(cosβ₃) = L₃(cosβ₃)/(cos²β₁cos²β₂) — nested form verified [VERIFIED-sympy]
- T1b: Δ(sin²β₁) = L₁(sin²β₁) — β₁-only function [VERIFIED-sympy]
- T1c: Δ(sin²β₂) = L₂(sin²β₂)/cos²β₁ — β₂-only function [VERIFIED-sympy]
- T2: L₃(1)=0, L₃(cosβ₃)=−2cosβ₃, L₃(P₂)=−6P₂ — Legendre eigenvalues [VERIFIED-sympy]
- T3: Δ(A₁A₂) = A₂L₁A₁ + A₁L₂A₂/cos²β₁ — exact separation, no cross terms [VERIFIED-sympy]
- T3b: Δ(A₁A₃) — exact separation [VERIFIED-sympy]
- T3c: Δ(A₁A₂A₃) — three-way exact separation [VERIFIED-sympy]
- T4: Full nesting: Δ(sin²β₁·sinβ₂·cosβ₃) matches ODE decomposition [VERIFIED-sympy]
- T5: L₁(sin²β₁)=14cos²β₁−10, L₁(1)=0, L₁(sin²)+L₁(cos²)=0 [VERIFIED-sympy]
- 13/13 pytest tests PASS [VERIFIED-pytest 2026-06-15, 5s]
- Full suite: 477 passed, 2 skipped [VERIFIED-pytest 2026-06-15]

## Key result: Scalar Laplacian on S⁶ factorizes exactly

### Operator structure
```
Δ_S⁶ = L₁ + (1/cos²β₁)[L₂ + (1/cos²β₂)L₃]

L₃ = (1/sinβ₃)∂_{β₃}(sinβ₃ ∂_{β₃}) − m₃²/sin²β₃    [S² Laplacian!]
L₂ = (1/(sinβ₂cos²β₂))∂_{β₂}(sinβ₂cos²β₂ ∂_{β₂}) − m₂²/sin²β₂
L₁ = (1/(sinβ₁cos⁴β₁))∂_{β₁}(sinβ₁cos⁴β₁ ∂_{β₁}) − m₁²/sin²β₁
```

### Three nested ODEs (for Δf = −λf)
```
ODE₃: L₃A₃ + l₃(l₃+1) A₃ = 0          → Legendre P_{l₃}^{m₃}(cosβ₃)
ODE₂: L₂A₂ + [l₂ − l₃(l₃+1)/cos²β₂] A₂ = 0    → Jacobi-type on [0,π/2]
ODE₁: L₁A₁ + [λ − l₂/cos²β₁] A₁ = 0           → Jacobi-type on [0,π/2]
```

### Connection to G2
The 1/cos²β_k "centrifugal" terms in ODE₂ and ODE₁ are the G2 cotβ_k frame artifacts
appearing in their natural role: they are NOT physical singularities, they are
the eigenvalue contributions from the nested inner spheres.

### Tom Lawrence analog

| S³ (Tom) | S⁶ (G3) |
|---|---|
| One radial ODE in α (Jacobi/Gegenbauer) | Three nested ODEs (ODE₃→ODE₂→ODE₁) |
| Solutions: Jacobi polynomials | Inner: Legendre P_l(cosβ₃); Outer: Jacobi-type |
| cot(2α) from G2 enters as centrifugal term | cotβ_k enter as l₃(l₃+1)/cos²β₂, l₂/cos²β₁ |

## What this does NOT mean
- SCALAR Laplacian only — Dirac operator on S⁶ requires spinor connection (Γ^a e_a^μ ∇_μ)
- Does NOT solve Dirac (different operator, different eigenvalues)
- Does NOT fix λ or select compactification
- Integer quantum numbers l₃, l₂ take all non-negative values; no physical selection

## Next gates
- G4: Spinor Dirac operator on S⁶ — how do γ-matrices modify the separated ODEs?
  (spinor connection terms will couple the chiral components, analog of Tom rows 16-19)
