# S6-HARM-G3: Separation of Variables — Three Nested ODEs

**Date:** 2026-06-15
**Gate:** G3 — scalar Laplacian on S⁶ separates; L₃ = S² Laplacian exactly
**Depends on:** G1 PASS (metric), G2 PASS (cotβ_k structure)

## Physical motivation
Tom Lawrence S³: after factoring out Cartan phases, the "radial" part satisfies
a Jacobi-type ODE in α. The cotβ_k terms from G2 (the coordinate artifacts)
feed directly into these ODEs as "centrifugal" potential terms.

For S⁶ with 3 Cartan directions, there are 3 nested ODEs.

## Question type: Descriptive

## Claim

### Scalar Laplace-Beltrami operator on S⁶ (ρ=1)

From G1 metric (diagonal), the LB operator is:

Δ = L₁ + (1/cos²β₁)[L₂ + (1/cos²β₂)L₃]

where the sub-operators are (all acting at m_k=0 for the β-only part):

```
L₃ = (1/sinβ₃) d/dβ₃(sinβ₃ d/dβ₃) − m₃²/sin²β₃     [S² Laplacian in β₃,φ₃]
L₂ = (1/(sinβ₂cos²β₂)) d/dβ₂(sinβ₂cos²β₂ d/dβ₂) − m₂²/sin²β₂
L₁ = (1/(sinβ₁cos⁴β₁)) d/dβ₁(sinβ₁cos⁴β₁ d/dβ₁) − m₁²/sin²β₁
```

### Separation of variables

For f = A₁(β₁) A₂(β₂) A₃(β₃) × e^{i(m₁φ₁+m₂φ₂+m₃φ₃)}, the eigenvalue
equation Δf = −λf decomposes EXACTLY into three nested ODEs:

```
ODE₃:  L₃A₃ + l₃(l₃+1) A₃ = 0                            (S²: Legendre solutions)
ODE₂:  L₂A₂ + [l₂ − l₃(l₃+1)/cos²β₂] A₂ = 0            (Jacobi-type on [0,π/2])
ODE₁:  L₁A₁ + [λ  − l₂/cos²β₁] A₁ = 0                   (Jacobi-type on [0,π/2])
```

**Nested eigenvalue structure:** l₃ → l₂ → λ (each feeds into the next ODE as
a centrifugal-like term 1/cos²β_k — these are the cotβ_k artifacts from G2).

### Key sub-claims (sympy-verifiable)
1. Δ has the nested form (no cross β₁β₂, β₁β₃, β₂β₃ terms) — diagonal metric
2. L₃ eigenvalues: L₃Pₗ(cosβ₃) = −l(l+1)Pₗ(cosβ₃) for l=0,1,2 [VERIFIED-sympy]
3. L₂ structural formula matches explicit Δ computation
4. Separation exact: Δ(A₁A₂A₃) = A₂A₃L₁A₁ + A₁A₃L₂A₂/cos²β₁ + A₁A₂L₃A₃/(cos²β₁cos²β₂)

## What this does NOT mean
- Does NOT apply to spinors (scalar analysis only; spinor Dirac involves γ-matrices)
- Does NOT fix the integer quantum numbers (l₂, l₃ take all non-negative integer values)
- Does NOT determine the spectrum of the Dirac operator (different from scalar Laplacian)
- Does NOT fix λ or any compactification parameter

## Falsification
- Any cross term ∂_{β₁}∂_{β₂} ≠ 0 in Δ → FAIL
- L₃(cosβ₃) ≠ −2cosβ₃ → FAIL
- Separation not exact → FAIL
