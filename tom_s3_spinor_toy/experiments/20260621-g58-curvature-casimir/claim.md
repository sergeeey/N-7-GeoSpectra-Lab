# G58 claim — Curvature in 4D EH frame

**Date:** 2026-06-21
**Question type:** Descriptive / Predictive
**Status:** TESTED → NULL

## Falsifiable claim

> G54-F's v_eh_total omitted V_curv^EH. Including it creates an interior minimum
> of V_curv^EH + V_flux^EH + V_Cas^EH at ρ₆_min_curv ≈ 0.337, but this minimum
> lies far outside the SM-relevant region [0.953, 1.447].

## Formula

On SM constraint ρ₃ = C ρ₆² (C = 0.986):

```
V_curv^EH(ρ₆) = V_class_string / V_int
             = [-(R_S3 + R_S6) × V_int] / V_int
             = -(6/(C²ρ₆⁴) + 30/ρ₆²)
```

## Hierarchy at ρ₆ = 1

| Term          | Value         | Ratio to V_curv |
|---------------|---------------|-----------------|
| V_curv^EH     | −36.17        | 1×              |
| V_flux^EH     | +4.6×10⁻⁴    | 7.9×10⁴ smaller |
| V_Cas^EH      | −1.6×10⁻⁶    | 2.3×10⁷ smaller |

## Gates

- **C1:** V_curv^EH < 0, ρ₆-dependent, monotone on [0.5, 2.0]
- **C2:** |V_curv^EH(1)| / V_flux^EH(1) > 10⁴
- **C3:** d/dρ₆(V_curv + V_flux) changes sign on (0.25, 0.50) → minimum exists
- **C4:** ρ₆_min_curv < 0.50 << RHO6_MIN_CAS = 0.953
- **C5:** |V_Cas^EH| / |V_curv^EH| < 10⁻⁴ at SM-scale radii
- **C6:** minimum value << −100 (deep AdS, not SM-scale)

## What this does NOT mean

1. Does NOT mean V_curv stabilizes the compactification at SM scale
2. Does NOT solve the moduli stabilization problem (minimum at wrong scale)
3. Does NOT invalidate G54-F (G54-F studied V_flux+V_Cas only, a separate sector)
4. Does NOT account for Freund-Rubin on-shell cancellation between R_int and flux
