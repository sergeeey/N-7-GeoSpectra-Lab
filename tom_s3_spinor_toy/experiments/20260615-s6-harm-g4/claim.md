# S6-HARM-G4: Dirac Spectrum on S⁶ — Lichnerowicz Bound and Killing Spinors

**Date:** 2026-06-15
**Gate:** G4 — Dirac operator spectrum on S⁶; connection to G0 Killing spinors
**Depends on:** G0 PASS (Clifford basis), G1 PASS (metric → K=1/ρ²), G3 PASS (R=30/ρ² from G1)

## Physical motivation

G3 established the scalar Laplacian on S⁶ and its three nested ODEs (l₃→l₂→λ).
G4 asks: what happens when we replace the scalar Laplacian with the SPINOR Dirac operator D̸?

The Dirac operator couples to the spin connection; the Lichnerowicz formula
D̸² = ∇*∇ + R/4 links the Dirac spectrum back to the scalar curvature R from G1/G3.
The lowest eigenvalues correspond to Killing spinors — and these are exactly
the spinor weight states from G0 (the 8 weight vectors ±½⊗±½⊗±½ of SO(6)).

## Question type: Descriptive

## Key analytical inputs (from G1 metric)

From G1: metric g_{kk} diagonal on S⁶ with radius ρ.
Sectional curvature for the (β₁,φ₁) plane:
  K(β₁,φ₁) = R_{β₁φ₁β₁φ₁} / (g_{β₁β₁} g_{φ₁φ₁}) = 1/ρ²

Since S⁶ has constant sectional curvature K=1/ρ², all sectional curvatures equal 1/ρ².
Scalar curvature: R = n(n-1)K = 6·5·(1/ρ²) = 30/ρ².

## Claims (sympy-verifiable)

### C1: Christoffel symbols (G1 metric, β₁/φ₁ plane)
```
Γ^{φ₁}_{φ₁β₁} = cot(β₁)         [independent of ρ]
Γ^{β₁}_{φ₁φ₁} = −sin(β₁)cos(β₁) [independent of ρ]
```

### C2: Sectional curvature K = 1/ρ²
```
R^{φ₁}_{β₁φ₁β₁} = 1      (mixed Riemann component)
K(β₁,φ₁) = 1/ρ²           (from all-covariant / gram-det)
```

### C3: Scalar curvature R = 30/ρ²
```
R = n(n−1)/ρ² = 30/ρ²    (from K=const and n=6)
Lichnerowicz bound: |λ(D̸)|² ≥ R/4 = 15/(2ρ²)
```

### C4: Ground state and Killing spinors
```
Minimum Dirac eigenvalue: |λ₀| = n/(2ρ) = 3/ρ
|λ₀|² = 9/ρ² > 15/(2ρ²) ≡ 7.5/ρ² ✓ (bound satisfied, not saturated)
Killing spinor count: 2^{n/2} = 2³ = 8
8 Killing spinors = G0 weight vectors (±½,±½,±½) → connection established
```

### C5: Full Dirac spectrum formula
```
λ_l = ±(l + n/2)/ρ = ±(l+3)/ρ,  l = 0, 1, 2, ...

l=0: ±3/ρ  (Killing spinors)
l=1: ±4/ρ
l=2: ±5/ρ
```

### C6: Tom Lawrence S³ analog
```
S³ (n=3): λ_l = ±(l + 3/2)/ρ,  minimum |λ₀| = 3/(2ρ)
S⁶ (n=6): λ_l = ±(l + 3)/ρ,   minimum |λ₀| = 3/ρ
Ratio: |λ₀(S⁶)| / |λ₀(S³)| = 2 = n(S⁶)/n(S³)
```

## Falsification criteria
- Γ^{φ₁}_{φ₁β₁} ≠ cot(β₁) → FAIL (wrong metric)
- K ≠ 1/ρ² → FAIL (G1 metric not round sphere)
- R ≠ 30/ρ² → FAIL
- |λ₀|² < R/4 → FAIL (Lichnerowicz violated — impossible for compact Riemannian)
- Killing spinor count ≠ 8 → FAIL

## What this does NOT mean
- Does NOT prove spinor harmonics on S⁶ satisfy the nested ODE structure of G3
  (spinor covariant derivative ≠ scalar gradient; the ODEs differ by spin connection terms)
- Does NOT fix the physical λ compactification parameter
- Does NOT apply to the full S³×S¹ or S³×S² (S⁶ analysis only)
- The spectrum formula is for the round S⁶ with constant radius ρ (not warped products)
- Does NOT select any physical mass spectrum — l is unrestricted
