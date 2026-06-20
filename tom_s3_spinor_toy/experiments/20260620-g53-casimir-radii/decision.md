# G53 Decision — Casimir Vacuum Energy on S³×S⁶

**Date:** 2026-06-20  
**Verdict:** OPEN (C1-C3 PASS; C4 not falsified but not confirmed)

## Results

### C1 (scaling law) — PASS [VERIFIED]
ζ(s; λρ₃, λρ₆) = λ^{2s} × ζ(s; ρ₃, ρ₆) to 0.5% for λ=1.5, 2.0 at s=5,6,7.
Non-uniform scaling (ρ₃ only) breaks the law, confirming both radii must scale together.

### C2 (non-factorizability) — PASS [VERIFIED]
ζ_product ≠ ζ_{S³} × ζ_{S⁶}: relative difference >10% at (ρ₃=ρ₆=1, s=5).
Root cause: product spectrum has λ²_{j,k} = λ²_j + λ²_k (ADD, not multiply).
This cross-coupling term makes the two-radius Casimir computation non-trivial —
it is NOT the product of two single-sphere results.

### C3 (Seeley-DeWitt) — PASS [VERIFIED]
K_{S³}(τ) ~ A₀/τ^{3/2} + A₂/τ^{1/2} + ...
- A₀ = 0.886 (converges to √π/2 ≈ 0.8862 from τ=0.01 to τ=0.002) ✓
- A₂ = −0.4431 (= −√π/4 exactly, curvature correction, NEGATIVE) ✓
- B₀(S⁶) = 0.131 (positive) ✓

A₂ < 0 is the standard curvature correction for S³ with positive scalar curvature.
This term will appear in the Seeley-DeWitt subtraction when computing ζ(-1/2).

### C4 (minimum along SM constraint) — OPEN [HYPOTHESIS]
Approximate Casimir (discrete Riemann sum over t ∈ {0.5, 1, 2, 5, 10}) along constraint
ρ₃ = 0.986 ρ₆²:

| ρ₆ | ρ₃ | Casimir_approx | S_spec | Cas/Sspec |
|-----|------|----------------|--------|-----------|
| 0.80 | 0.631 | 9.95×10⁻³ | 1.77×10⁻⁷ | 56,200 |
| 1.00 | 0.987 | 1.07 | 8.26×10⁻⁴ | 1,295 |
| 1.30 | 1.667 | 65.7 | 0.288 | 228 |
| 1.70 | 2.851 | 2,586 | 22.2 | 117 |
| 2.00 | 3.946 | 21,233 | 222 | 95.6 |
| 2.50 | 6.166 | 353,725 | 4,335 | 81.6 |

**Key finding:** The approximate Casimir is MONOTONE INCREASING along the constraint,
same qualitative behavior as S_spec (G51 NULL). No interior minimum detected.

**Key structural finding:** Casimir/Sspec ratio varies from 56,200 to 81.6 across the range
— confirming these are genuinely different functionals (C2 extension). The Casimir grows
SLOWER than S_spec at large radii, but both are monotone.

**Why OPEN, not NULL:** The approximate Casimir is NOT the true Casimir energy. The true
E_Casimir = ζ_{D²}(s=-1/2; ρ₃, ρ₆) requires analytic continuation from s > 9/2 to s = -1/2,
with 5 Seeley-DeWitt subtractions. The approximate Riemann sum is dominated by the LARGE-t
behavior (BKM regime) which IS monotone, but the continued ζ(-1/2) could differ.

## What This Does NOT Mean

1. Does NOT mean the Casimir cannot stabilize radii — the full ζ(-1/2) was not computed.
2. Does NOT mean the SM coupling constraint excludes stabilization — the correct classical
   potential from dimensional reduction may have opposite sign to S_spec.
3. Does NOT establish the physical compactification scale.
4. Does NOT imply that flux-assisted stabilization (Freund-Rubin type) also fails.

## Kill Analysis (for the "approximate Casimir has a minimum" hypothesis)

**What is killed:** The claim that a simple t-slice Riemann sum of K(t; ρ₃, ρ₆) t^{-3/2}
has a minimum along ρ₃=0.986ρ₆².

**What is NOT killed:**
- The exact ζ(-1/2) via Chowla-Selberg or Mellin-Barnes regularization
- Coleman-Weinberg potential from gauge fluctuations on S³×S⁶
- Flux quantization (q units of G-flux on S⁶) → V_flux ~ q²/ρ₆⁸ (decreasing at large ρ₆)
- Combinations: V_eff = V_class + V_flux + V_Casimir

## What Remains Open (G54 candidates)

| Mechanism | What to compute | Estimate |
|-----------|-----------------|---------|
| ζ(-1/2) via Chowla-Selberg | Double sum evaluation at s=-1/2 | 2-3 days |
| CW gauge correction | 1-loop Coleman-Weinberg on S³×S⁶ gauge sector | 1 week |
| Freund-Rubin flux | Fix q units of H₃-flux; minimize V(ρ₃, ρ₆, q) | 2-3 days |

The CHEAPEST next test: Freund-Rubin type potential
V_eff(ρ₃, ρ₆) = V_class(ρ₃, ρ₆) + V_flux(ρ₃, ρ₆, q)
where V_flux ~ q²/ρ₆⁸ provides the decreasing term that competes with S_spec growth.

## Verdict

OPEN. C1-C3 confirmed by 19/19 tests. C4 is an open numerical computation.
The approximate Casimir extends G51 NULL (monotone), but the full ζ(-1/2) continuation
is the definitive test. Radii stabilization remains open pending G54.
