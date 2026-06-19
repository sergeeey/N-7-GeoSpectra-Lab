# Claim — G28: Spectral Action on S³×S⁶ with Inner Fluctuations

**Date:** 2026-06-20  
**Question type:** Predictive  
**FL tier:** Standard

## Falsifiable Claim

The spectral action Tr f(D²/Λ²) on S³×S⁶, with S³ and S⁶ spin connections treated as inner fluctuations (Tom's Section 7 identification), produces gauge kinetic terms for SU(2)_L and SU(3)_c. The inverse couplings are:

```
1/g_SU2² ∝ f₀ × N_{s6} × Vol(S⁶) / 12   [controlled by S⁶ volume!]
1/g_SU3² ∝ f₀ × N_{s3} × Vol(S³) / 12   [controlled by S³ volume!]
```

Coupling ratio:  
```
g₂²/g₃² = 15ρ₃³/(16π ρ₆⁶)
```

Unification condition g₂=g₃:  
```
ρ₃³ = (16π/15) ρ₆⁶   ↔   ρ₃/ρ₆² = (16π/15)^{1/3} ≈ 1.88
```

## Evidence

- a₀, a₂, a₄ for Dirac on S³ and S⁶ computed symbolically (g28_scout.py)
- Inner fluctuation Δa₄ computed from Vassilevich 2003 eq (4.5) (g28_inner_fluctuation.py)
- Gauge kinetic terms derived with correct sign (negative Euclidean = physical)
- Ratio g₂²/g₃² symbolic formula verified by SymPy

## Kill Condition

FAIL if:
- Inner fluctuation produces gauge kinetic term with wrong sign
- Ratio g₂²/g₃² diverges or is imaginary
- At equal unit radii, ratio is 0 or ∞ (would indicate structural error)

## What This Does NOT Mean

- Does NOT predict exact SM gauge couplings (ρ₃, ρ₆ are free; normalization conventions TBD)
- Does NOT claim derivation in 4D (this is internal space; full 4D requires M⁴ × S³ × S⁶)
- Does NOT prove unification at any specific energy scale
- Does NOT follow from SM coupling running; the formula is a toy model statement

## Key Non-Obvious Result

**Cross-spectator effect:** The SU(2)_L gauge coupling is controlled by Vol(S⁶), and the SU(3)_c coupling by Vol(S³). NOT the other way around.
- SU(2) fluctuation lives on S³ → S⁶ spinors are spectators → S⁶ volume enters
- SU(3) fluctuation lives on S⁶ → S³ spinors are spectators → S³ volume enters
- Consequence: g₂ < g₃ naturally when Vol(S⁶) > Vol(S³) (i.e., when ρ₆ > ρ₃^{1/2})

## References

- Vassilevich 2003 (hep-th/0306138): heat kernel coefficients for inner fluctuations
- Tom Lawrence, PMs paper Section 7: spin connection = gauge field identification
- Connes-Chamseddine 1997: spectral action principle
