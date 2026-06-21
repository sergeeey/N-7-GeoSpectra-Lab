# G60 claim — Geometric derivation of A_np and λ

**Date:** 2026-06-21
**Question type:** Descriptive
**Status:** TESTED → NULL

## Falsifiable claim

> Imposing Minkowski vacuum V_total(ρ₆*)=0 and dV/dρ₆|_{ρ₆*}=0 at the UV-selected
> radius ρ₆*=1.090 algebraically fixes the KKLT-like NP parameters (A_np, λ).
> Promote criterion: |λ_geom − 0.30|/0.30 < 10%.
> Null criterion: λ_geom < 0 or |λ_geom − 0.30|/0.30 > 100%.

## Derivation (analytic)

V_total = (V_flux + ζ_FP − A_np·exp(−λ/ρ₆²)) / V_int

Minkowski at ρ₆*:  V_flux + ζ_FP(ρ₆*) = A_np·exp(−λ/ρ₆*²) := P*
Minimum at ρ₆*:    ζ_FP'(ρ₆*) + (2λ/ρ₆*³)·P* = 0

→  λ_geom = −ρ₆*³/2 · ζ_FP'(ρ₆*) / P*
→  A_geom = P* · exp(+λ_geom/ρ₆*²)

## Gates

- **A1:** V_flux ∈ (0.1, 1.0) — order unity
- **A2:** |ζ_FP(ρ₆*)| << 0.01 × V_flux — Casimir negligible at UV point
- **A3:** ζ_FP'(ρ₆*) ≠ 0 — nonzero slope needed for derivation
- **B1 NULL:** λ_geom < 0 (structural: ζ_FP monotone increasing in window)
- **B2 PASS:** A_geom ≈ V_FLUX_CONST (with λ≈0, A_np cancels flux)
- **B3 PASS:** ζ_FP'(ρ₆*) > 0 (confirmed monotone increase)
- **C1 NULL:** |λ_geom − 0.30|/0.30 ≈ 101% >> 10%
- **C2 SKIP:** A_np promote criterion (skipped: λ already null)

## Key numerical results

| Quantity | Value |
|----------|-------|
| ζ_FP(ρ₆*=1.090) | small negative (~−10⁻⁴) |
| ζ_FP'(ρ₆*=1.090) | > 0 (rising toward zero at ρ₆**=1.447) |
| λ_geom | −0.0022 (NEGATIVE — unphysical) |
| A_geom | 0.2847 ≈ V_FLUX_CONST = 0.2861 |
| λ_fitted (G56) | 0.30 |
| A_np_fitted (G56) | 0.38 |

## What this does NOT mean

1. Does NOT mean A_np and λ are unconstrained — only that THIS derivation path fails
2. Does NOT rule out Thread 2 (gaugino condensation) or Thread 3 (resurgence) as sources of λ
3. Does NOT change G56 result: KKLT stabilization at ρ₆*≈1.09 still valid with fitted params
4. Does NOT imply A_geom = V_FLUX_CONST exactly — only in the λ→0 limit of this derivation
