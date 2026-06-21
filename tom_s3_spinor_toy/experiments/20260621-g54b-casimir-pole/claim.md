# G54-B Claim — Spectral Zeta at s=−1/2: Pole Structure

**Date:** 2026-06-21  
**Type:** Descriptive  
**Ladder:** Standard

## Estimand

**Population:** The Dirac-squared spectral zeta ζ(s; ρ₃, ρ₆) on S³×S⁶ with the
product metric (round S³ of radius ρ₃, round S⁶ of radius ρ₆).

**Endpoint:** Behaviour of ζ(s) near s = −1/2, specifically whether s = −1/2
is a regular point (finite value) or a pole (divergence requiring renormalization).

**MCID:** A non-zero t^{1/2} coefficient in K(t; ρ₃, ρ₆) at any (ρ₃, ρ₆)
is sufficient to establish a pole.

## Claims

**B1 (Homogeneity):**  
ζ(-1/2; λρ₃, λρ₆) = λ^{-1} ζ(-1/2; ρ₃, ρ₆).  
Along SM constraint: ζ(-1/2; Cρ₆², ρ₆) = ρ₆^{-1} × ζ(-1/2; Cρ₆, 1).

**B2 (Pole existence):**  
K(t; ρ₃, ρ₆) = K_{S³}(t/ρ₃²) × K_{S⁶}(t/ρ₆²) has a non-zero t^{1/2} coefficient
c_{1/2}(ρ₃, ρ₆) as t→0+. Therefore ζ(s; ρ₃, ρ₆) has a simple pole at s = −1/2
with residue c_{1/2} / Γ(−1/2) = −c_{1/2} / (2√π).

**B3 (Residue formula — exact, from Poisson summation):**  
K_{S³}(τ) has EXACTLY TWO polynomial SW terms: A₀ τ^{-3/2} + A₂ τ^{-1/2}.  
Higher coefficients A₄, A₆, ... are ZERO (theorem: bilateral theta function cancellation).  
Therefore the only t^{1/2} cross-term is:
  c_{1/2}(ρ₃, ρ₆) = A_{-1/2}^{(3)} × B₈^{(6)} × ρ₃/ρ₆²
where B₈ is the τ^1 SW coefficient of K_{S⁶} (non-zero, numerically extracted).

**B4 (SM constraint — NEW result: SCALE INVARIANT):**  
Along ρ₃ = C ρ₆²: c_{1/2} = A_{-1/2}^{(3)} × B₈^{(6)} × C = CONSTANT.  
The Casimir pole residue is scale-invariant along the SM coupling constraint,
identically to V_flux (G54-A). Both are fixed ratios × C (= ρ₃/ρ₆²).

**B5 (OPEN):**  
Physical Casimir energy = Hadamard finite part of ζ at s=−1/2. Requires computing
the full Laurent expansion ζ(s) = Res/(s+1/2) + ζ_FP + O(s+1/2). The minimum
of ζ_FP(ρ₃, ρ₆) (if any) is the question for G54-C.

## What This Does NOT Mean

1. Does NOT determine whether the renormalized Casimir energy has a minimum.
2. Does NOT show the UV divergence is unrenormalizable (it is renormalizable).
3. Does NOT apply at ρ₃=ρ₆=0 (no geometry).
