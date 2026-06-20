# G53 Claim — Casimir Vacuum Energy on S³×S⁶

**Date:** 2026-06-20  
**Ladder tier:** FL Standard  
**Question type:** Descriptive (structural) + Predictive (open)

## Claim

The spectral zeta function ζ_{D²}(s; ρ₃, ρ₆) = Σ_{j,k} mult(j,k) [(j+1)²/ρ₃² + (k+3)²/ρ₆²]^{-s}
is a well-defined analytic function for s > 9/2, with:

**C1 (structural):** ζ(s; ρ₃, ρ₆) satisfies the exact scaling law ζ(s; λρ₃, λρ₆) = λ^{2s} ζ(s; ρ₃, ρ₆).

**C2 (structural):** ζ(s; ρ₃, ρ₆) does NOT factorize as ζ_{S³}(s) × ζ_{S⁶}(s), because
eigenvalues ADD (product spectrum), not multiply.

**C3 (structural):** The Seeley-DeWitt expansion K_{S³}(τ) ~ A₀/τ^{3/2} + A₂/τ^{1/2} + ...
has A₀ > 0 and A₂ < 0 (negative curvature correction).

**C4 (predictive — OPEN):** The analytic continuation ζ(s=-1/2; ρ₃, ρ₆) — the regularized
Casimir energy — has a local minimum at finite (ρ₃*, ρ₆*) along the SM coupling constraint
ρ₃ = 0.986 ρ₆².

## Background

G51 NULL proved: S_spec(ρ₃, ρ₆) = K_{S³}(1/ρ₃²) × K_{S⁶}(1/ρ₆²) is monotone along
the SM coupling constraint → spectral action alone cannot stabilize radii.

G53 asks: does the FULL vacuum energy (integrated over all time scales, not just t=1)
provide a genuinely different potential landscape? Concretely, does E_Casimir ∝ ζ(-1/2)
have a different functional form than S_spec?

C1-C3 are immediately verifiable. C4 requires the analytic continuation of the double
Epstein-type zeta function to s = -1/2, which needs Seeley-DeWitt subtraction of 4 terms
(9/2 + 1/2 = 5 subtractions; dim = 9 → 4 SW terms needed before the integral converges).

## Known

Birmingham-Kantowski-Milton (1988): E_Casimir(S⁶) for the 6-sphere alone.
This single-factor result is INSUFFICIENT — the two-radius cross-terms couple ρ₃ and ρ₆.

## Falsification

C1 is falsified if ζ(s; λρ₃, λρ₆) / λ^{2s} ≠ ζ(s; ρ₃, ρ₆) to better than 1%.
C2 is falsified if ζ_product = ζ_{S³} × ζ_{S⁶} to better than 5%.
C3 is falsified if A₀ < 0 or A₂ > 0.
C4 remains OPEN pending the full computation.

## MCID

C1-C3: exact algebraic identities (any violation > 1% = falsified).
C4: open — minimum must be at ρ₃* > 0, ρ₆* > 0 on the constraint curve.
