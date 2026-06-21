# G54-C Decision

**Verdict:** C1-C3 PASS · C4 OPEN  
**Date:** 2026-06-21  
**Tests:** 1739 total (21 new for G54-C)  
**Commit:** pending

---

## Results

### C1 PASS — B₁₀_S6 is genuinely non-zero

B₁₀ ≈ −0.0033 from small-τ fit over [0.005, 0.080].
Stability check: 6-param gives −0.0033, 7-param gives −0.0029, residual method −0.0033.
|B₁₀/B₈| ≈ 0.43 — a non-perturbative contribution.

The 6-param fit uses basis {τ^{-3}, τ^{-2}, τ^{-1}, τ^0, τ^1, τ^2}.
Residuals < 1e-4 relative at all fitting points.
B₀ = 2/15 = 0.13333... (exact analytic value) recovered to 5 significant figures.

### C2 PASS — G54-B B4 was INCOMPLETE

G54-B B4 relied on 5-param fit giving B₈_eff ≈ −0.0108 (overcorrected).
True B₈ ≈ −0.0076 (6-param) with separate B₁₀ ≈ −0.0033.

The two terms have DIFFERENT ρ-dependences:
  A₂_S3 × B₈ × ρ₃/ρ₆² = A₂_S3 × B₈ × C = CONST along constraint
  A₀_S3 × B₁₀ × ρ₃³/ρ₆⁴ = A₀_S3 × B₁₀ × C³ × ρ₆² = grows as ρ₆²

When lumped into one effective B₈_eff, the ρ₆² growth appears as a constant
(because B₈_eff itself doesn't depend on ρ₆). The 5-param formula was internally
consistent but described the effective coefficient, not the SW coefficient.

### C3 PASS — Pole cancellation at ρ₆* ≈ 1.09

The two competing terms cancel exactly at:
  ρ₆*² = −(A₂_S3 × B₈) / (A₀_S3 × B₁₀ × C²)

With A₂_S3 = −√π/4, A₀_S3 = √π/2, B₈ ≈ −0.0076, B₁₀ ≈ −0.0033, C = 0.986:
  ρ₆*² ≈ (√π/4 × 0.0076) / (√π/2 × 0.0033 × 0.972) ≈ 1.19
  ρ₆* ≈ 1.09

Numerical verification: c_{1/2}(ρ₆*) < 0.002 × c_{1/2}(0.1).
Sign flip confirmed: c_{1/2} > 0 for ρ₆ < ρ₆*, < 0 for ρ₆ > ρ₆*.

### C4 OPEN — ζ_FP(−1/2) needs Hadamard subtraction

The full Laurent expansion of ζ(s) near s = −1/2:
  ζ(s) = c_{1/2}/[Γ(−1/2)(s+1/2)] + ζ_FP + O(s+1/2)

At ρ₆ = ρ₆*, the pole VANISHES (c_{1/2} = 0), so ζ(s) is regular at s = −1/2.
Does ζ_FP itself also vanish at ρ₆*? This requires Hadamard subtraction of ALL
singular SW cross-terms (powers t^{−9/2}, ..., t^{−1/2}) and numerical integration
of the regular remainder.

This is G54-D.

---

## Impact on Pearl Registry

The G54-A+B pearl "double scale-invariance" needs partial revision:

| Component | Status |
|-----------|--------|
| V_flux (G54-A) = g₂²/g₃² | CONFIRMED — still CONSTANT on constraint |
| c_{1/2} = CONST (G54-B B4) | REVISED — NOT constant, varies as const + slope×ρ₆² |

Revised pearl: "V_flux is constant on SM constraint (G54-A), but c_{1/2} is NOT —
it has a zero at ρ₆* ≈ 1.09 where the Casimir UV pole cancels."

---

## Next steps

**G54-D: Hadamard finite part ζ_FP(−1/2)**
- Subtract all singular SW cross-terms from K(t)
- Compute Mellin integral of regular remainder numerically
- Check if ζ_FP(ρ₆) has a minimum, and whether the minimum is at ρ₆*

**G54-E: Physical interpretation of ρ₆***
- What sets the units (normalization) in which ρ₆* ≈ 1.09?
- Is ρ₆* related to any physical scale (Planck, SUSY breaking, flux quantization)?

---

## Kill analysis (if applicable)

No branch killed. G54-B B4 was INCOMPLETE not WRONG — it computed a different
(effective) quantity. G54-C corrects the formula by separating the two cross-terms.

The Poisson theorem (A₄=0 for S³) is UNAFFECTED — it controls S³ coefficients only.
The B₁₀ term is a property of S⁶ SW expansion, independent of the Poisson theorem.

---

## Pearl Gate

New pearl from C3:
- Observation: c_{1/2}(ρ₆) changes sign at ρ₆* — a zero of the Casimir UV divergence
- Falsifiable prediction: At ρ₆*, ζ(s) is regular at s = −1/2, so the Casimir
  energy is UV finite (no counterterm needed). Check numerically.
- Trigger condition: Compute ζ_FP(ρ₆*) — if it's also finite and unique, this fixes ρ₆.
- Next check: G54-D, 2026-06-21
