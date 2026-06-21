# H1 Claim — Geometric λ-law for Product Spheres

**Date:** 2026-06-21
**Question type:** Predictive
**Ladder tier:** Standard

## Claim

For a product geometry Sᵃ×Sᵇ, the non-perturbative exponent in the KKLT-like
stabilization potential is fixed by the dimensional ratio:

    λ = dim(Sᵃ) / dim(Sᵃ×Sᵇ) = a / (a + b)

**Falsifiable prediction:** with λ=a/(a+b) and A_np from the Minkowski condition
(G60 pearl), the NP potential V_total = (V_FLUX − A_np·exp(−λ/ρ²))/(K_VOL·ρ¹²)
has a minimum at ρ_min > ρ* with V_min < 0 for ALL (a,b) in the family.

**Specific test cases:**
| (a,b) | Manifold | λ = a/(a+b) |
|-------|---------|------------|
| (1,8) | S¹×S⁸  | 1/9 ≈ 0.111 |
| (2,7) | S²×S⁷  | 2/9 ≈ 0.222 |
| (3,6) | S³×S⁶  | 3/9 = 1/3   ← G62 anchor |
| (4,5) | S⁴×S⁵  | 4/9 ≈ 0.444 |
| (5,4) | S⁵×S⁴  | 5/9 ≈ 0.556 |

## What this does NOT mean

1. Does NOT prove these other manifolds are physical compactifications
2. Does NOT re-derive V_FLUX or ρ* for each (a,b) — those are fixed from S³×S⁶
3. Does NOT constrain which (a,b) gives the correct SM physics

## Controls

**Positive control:** (3,6) → λ=1/3, must reproduce G62 result ρ_min=1.1791
**Negative control:** λ=0 → A_np=V_FLUX, numerator→(V_FLUX−V_FLUX)=0 → runaway (no minimum)

## Kill conditions

- REJECT if minimum disappears for any (a,b)
- REJECT if (3,6) anchor doesn't reproduce ρ_min=1.1791 ± 0.001
- WEAK if ρ_min is not monotone in λ (pattern unclear)
- PROMOTE if all 5 cases have minimum AND ρ_min/ρ* > 1 AND m_mod/m_KK < 10%
