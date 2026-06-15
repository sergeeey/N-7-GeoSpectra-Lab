# S6-HARM-G2 — Decision

**Date:** 2026-06-15
**Verdict:** PROMOTE
**Status:** PASS_S6_ROOT_GENERATORS_COTBETA_CONFIRMED

## Evidence
- T1: L₁₂ = ∂_{φ₁} (Cartan = pure azimuthal, c_{φ₁}=1, all others 0) [VERIFIED-sympy]
- T2: L₃₄ = ∂_{φ₂} [VERIFIED-sympy]
- T3: L₅₆ = ∂_{φ₃} [VERIFIED-sympy]
- T4: L₁₃ φ₁-coeff = cotβ₁ sinβ₂ cosφ₂ sinφ₁ — full 6-component structure verified [VERIFIED-sympy]
- T4b: L₁₃ has no β₃, φ₃ components (no long-range coupling) [VERIFIED-sympy]
- T5: L₃₅ φ₂-coeff = cotβ₂ sinβ₃ cosφ₃ sinφ₂ [VERIFIED-sympy]
- T5b: L₃₅ no β₁, φ₁ coupling [VERIFIED-sympy]
- T6: L₁₅ φ₁-coeff = cotβ₁ cosβ₂ sinβ₃ cosφ₃ sinφ₁ [VERIFIED-sympy]
- T7: L₂₃ φ₁-coeff = −cotβ₁ sinβ₂ cosφ₂ cosφ₁ (hierarchy confirmed) [VERIFIED-sympy]
- 11/11 pytest tests PASS [VERIFIED-pytest 2026-06-15, 1.24s]
- Full suite: 464 passed, 2 skipped [VERIFIED-pytest 2026-06-15, 21s]

## Key result: cotβ_k hierarchy on S⁶

In nested sphere coordinates, the Killing vectors L_{ij} decompose as:

**Cartan generators** (SO(6) Cartan subalgebra):
```
L₁₂ = ∂_{φ₁}    (H₁)
L₃₄ = ∂_{φ₂}    (H₂)
L₅₆ = ∂_{φ₃}    (H₃)
```
Pure azimuthal — no cotangent terms.

**Root generators** (ladder operators):
```
L₁₃: c_{φ₁} = cotβ₁ · sinβ₂ cosφ₂ sinφ₁
L₁₅: c_{φ₁} = cotβ₁ · cosβ₂ sinβ₃ cosφ₃ sinφ₁
L₂₃: c_{φ₁} = −cotβ₁ · sinβ₂ cosφ₂ cosφ₁
L₃₅: c_{φ₂} = cotβ₂ · sinβ₃ cosφ₃ sinφ₂
...
```

**Hierarchy rule:**
- L_{1j}, L_{2j} for j≥3 → cotβ₁ appears in ∂_{φ₁} coefficient
- L_{3j}, L_{4j} for j≥5 → cotβ₂ appears in ∂_{φ₂} coefficient
- No cross-level coupling: L₁₃ has zero β₃, φ₃ components

**Crucially:** the cotβ_k factors arise only because the coordinates are adapted
to SO(6) Cartan planes (nested sphere), not because of any physical singularity.

## Tom Lawrence analog (confirmed)

| S³ (Tom row) | S⁶ (G2 result) |
|---|---|
| Row 13: ∂_θ + ∂_θ̃ = Î_{3L} (Cartan = pure azimuthal) | L₁₂ = ∂_{φ₁}, L₃₄ = ∂_{φ₂}, L₅₆ = ∂_{φ₃} |
| Row 15: cot(2α) = Hopf-frame artifact ("Sounds right") | cotβ_k = nested-sphere-frame artifact |

The cotβ_k structure is the S⁶ analog of Tom's cot(2α): a coordinate artifact
of choosing Cartan-adapted frames, not a physical singularity.

## What this does NOT mean
- cotβ_k does NOT signal a physical singularity at β_k = 0 or π/2
- Does NOT determine how spinor harmonics depend on β_k (that is G3+)
- Does NOT fix λ or select a physical compactification
- Does NOT establish that the Dirac operator on S⁶ is solvable

## Next gates
- G3: Spinor harmonics — how does Aⱼ(β₁,β₂,β₃) factorize given the cotβ_k structure?
  (analog: what equation does the "radial" part satisfy on S³?)
- G4: Spectrum — eigenvalues of the Dirac/Laplace operator on S⁶ in these coordinates
