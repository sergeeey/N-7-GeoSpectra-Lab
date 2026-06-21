# G59 claim — FR charge-scaling audit

**Date:** 2026-06-21
**Question type:** Descriptive
**Status:** TESTED → NULL

## Falsifiable claim

> The EH-frame minimum found in G58 at ρ₆≈0.337 can be shifted to the SM window
> [0.953, 1.447] by increasing V_FLUX_CONST. Kill criterion: required ratio
> f₀_SM / f₀_current > 100.

## Key formulas

String-frame potential on SM constraint (ρ₃ = C·ρ₆², C=0.986):
```
V_str(ρ₆) = -K_VOL·(6r6⁸/C² + 30r6¹⁰)  +  V_FLUX_CONST
∂V_str/∂ρ₆ = -K_VOL·(48r6⁷/C² + 300r6⁹)  < 0  always
```
⟹ no FR minimum in string frame (Dine-Seiberg in string frame confirmed).

Required f₀ to shift EH minimum to ρ₆=1:
```
f₀_SM = K_VOL · (24/C² + 60) / 12  ≈  4412
```
Current f₀ = V_FLUX_CONST ≈ 0.2861 (q₃q₆=1, G55).
Ratio = 4412 / 0.2861 ≈ **15,400**.

## Gates

- **A1:** ∂V_str/∂ρ₆ < 0 at 6 test points in [0.2, 2.0]
- **A2:** factored form -K_VOL·r6⁷·(48/C² + 300r6²) matches direct, inner factor always > 0
- **B1:** f₀_SM ∈ (4000, 5000); find_r6_min_eh(f₀_SM) = 1.00 ± 0.05
- **B2:** ratio > KILL_RATIO=100 (actual: ~15,000)
- **C1:** V_EH(ρ₆=1, f₀_SM) < 0 (still AdS ~-29); shallower than G58 (~-520)
- **D1:** ρ₆_min ∝ f₀^α, α ∈ [1/10, 1/8]; ×1024 in f₀ → ×2.2 in ρ₆_min
- **NULL:** ratio > 10,000; Casimir irrelevant at any charge scale

## What this does NOT mean

1. Does NOT mean the EH minimum at ρ₆≈0.337 (G58) is unphysical — it IS the genuine FR vacuum for q₃q₆=1
2. Does NOT constrain ρ₆ independently of the flux charge normalization
3. Does NOT rule out non-perturbative stabilization at SM scale (that is G56)
