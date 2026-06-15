# S6-HARM-G4 — Decision

**Date:** 2026-06-15
**Verdict:** PROMOTE
**Status:** PASS_S6_DIRAC_SPECTRUM_CONFIRMED

## Evidence

- T1: Γ^{φ₁}_{φ₁β₁} = cot(β₁) (ρ-independent) [VERIFIED-sympy]
- T1: Γ^{β₁}_{φ₁φ₁} = −sin(β₁)cos(β₁)          [VERIFIED-sympy]
- T2: R^{φ₁}_{β₁φ₁β₁} = 1 (mixed Riemann, from G1 metric) [VERIFIED-sympy]
- T3: K(β₁,φ₁) = 1/ρ² (unit sectional curvature — S⁶ is round sphere) [VERIFIED-sympy]
- T4: R = 30/ρ² = n(n-1)/ρ², n=6                [VERIFIED-sympy]
- T5: Lichnerowicz bound R/4 = 15/(2ρ²); |λ₀|²=9/ρ² > 15/(2ρ²), excess=3/(2ρ²) [VERIFIED-sympy]
- T6: Killing spinor count = 2^3 = 8 = G0 weight vector count (±½,±½,±½) [VERIFIED-sympy]
- T7: Spectrum ±(l+3)/ρ: l=0→±3/ρ, l=1→±4/ρ, l=2→±5/ρ [VERIFIED-sympy]
- T8: Minimum eigenvalue ratio |λ₀(S⁶)|/|λ₀(S³)| = 2 = n(S⁶)/n(S³) [VERIFIED-sympy]
- 16/16 pytest tests PASS [VERIFIED-pytest 2026-06-15, 0.47s]
- Full suite: 493 passed, 2 skipped [VERIFIED-pytest 2026-06-15]

## Key results

### Dirac spectrum structure on S⁶

```
K(β₁,φ₁)         = 1/ρ²         [sectional curvature, ρ-independent mixed Riemann]
R = n(n-1)/ρ²    = 30/ρ²        [scalar curvature, from K=const, n=6]
Lichnerowicz:     D̸² ≥ R/4 = 15/(2ρ²)

Spectrum: λ_l = ±(l + n/2)/ρ = ±(l+3)/ρ,  l = 0, 1, 2, ...
  l=0: ±3/ρ   ← Killing spinors (8 states)
  l=1: ±4/ρ
  l=2: ±5/ρ
```

### Killing spinors ↔ G0 weight vectors

| G0 weight (w₁,w₂,w₃) | Killing spinor | SO(6) rep |
|---|---|---|
| (+½,+½,+½) | ψ₁ | spinor 4 |
| (+½,+½,−½) | ψ₂ | spinor 4 |
| (+½,−½,+½) | ψ₃ | spinor 4 |
| (+½,−½,−½) | ψ₄ | spinor 4 |
| (−½,+½,+½) | ψ₅ | anti-spinor 4̄ |
| (−½,+½,−½) | ψ₆ | anti-spinor 4̄ |
| (−½,−½,+½) | ψ₇ | anti-spinor 4̄ |
| (−½,−½,−½) | ψ₈ | anti-spinor 4̄ |

→ The 8 lowest Dirac eigenstates on S⁶ ARE the G0 spinor weight states.

### Tom Lawrence analog table

| Quantity | S³ (Tom) | S⁶ (G4) |
|---|---|---|
| Dimension n | 3 | 6 |
| Scalar curvature | R=6/ρ² | R=30/ρ² |
| Lichnerowicz bound | R/4=3/(2ρ²) | R/4=15/(2ρ²) |
| Minimum eigenvalue | ±3/(2ρ) | ±3/ρ |
| Killing spinors | 2^{3/2}? → 4 (Majorana) | 2³=8 (Dirac) |
| Spectrum | ±(l+3/2)/ρ | ±(l+3)/ρ |
| l=0 eigenvalue | ±3/(2ρ) | ±3/ρ |
| Ratio min eigenvalues | — | S⁶/S³ = 2 = n(S⁶)/n(S³) |

### Geometric chain G0→G1→G2→G3→G4

```
G0: Clifford algebra Γ₁..Γ₆, {Γ_a,Γ_b}=2δ_{ab}, 8 spinor weights (±½,±½,±½)
    ↓
G1: Nested sphere metric g_{kk} diagonal (β₁,φ₁,β₂,φ₂,β₃,φ₃)
    ↓
G2: Root generators L_{ij}: φ_k-component has cot(β_k) frame artifact
    ↓
G3: Δ_S⁶ = L₁ + L₂/cos²β₁ + L₃/(cos²β₁cos²β₂); three nested ODEs
    ↓
G4: G1 metric → K=1/ρ² → R=30/ρ² → Dirac spectrum ±(l+3)/ρ
    Killing spinors (l=0) = G0 weight vectors ← GEOMETRIC CLOSURE
```

## What this does NOT mean

- Does NOT compute spinor connection ω_{μab} explicitly (complex 6D computation)
- Does NOT show that spinor harmonics on S⁶ satisfy the G3 nested ODE structure
  (spinor parallel transport mixes chiral components; ODEs for spinors differ from scalar)
- Does NOT fix λ or any compactification parameter
- The S³ "Killing spinors = 4" entry in the table is indicative (exact count depends
  on the spin structure; S³ is spin with count=4 for Majorana spinors)
- Does NOT apply to warped S⁶ products or the full KK compactification
- The ratio "2 = n(S⁶)/n(S³)" is a numerical coincidence at the level of minimum
  eigenvalues; it does NOT imply a simple dimensional-ratio rule for higher l

## Next gates
- G5: Explicit spinor connection on S⁶ in nested-sphere frame
  (spin connection terms that modify G3 ODEs for spinors)
- Or: close S6-HARM branch and prepare Tom correspondence update
  (G4 establishes the geometric foundation; spinor harmonics = separate topic)
