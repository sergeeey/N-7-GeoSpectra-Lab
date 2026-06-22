# G87 — Coupling ratio g₂²/g₃² at the physical vacuum

**Date:** 2026-06-22  
**Question type:** Predictive  
**Falsifiable predicate:** g₂²/g₃² evaluated at ρ₃=κρ₆_min is closer to SM value than equal-radii result  
**Measurable outcome:** numeric ratio, compare to 0.2984 (equal radii) and 0.2864 (SM at M_Z)

## Estimand

- **Population:** S³×S⁶ spectral action at the Casimir+flux minimum
- **Intervention:** evaluate g₂²/g₃² = 15ρ₃³/(16πρ₆⁶) at (ρ₃, ρ₆) = (κρ₆_min, ρ₆_min)
- **Comparator:** G29 result at equal unit radii (ρ₃=ρ₆=1)
- **Endpoint:** numeric gap from SM value 0.2864 at M_Z (PDG 2022)
- **MCID:** gap must decrease from 4.2% to be a positive result

## Parameters (from prior gates)

- κ = √(7/6) ≈ 1.0801 (analytic, G66)
- ρ₆_min ≈ 1.179 (zero-fit minimum, G62-G65)
- ρ₃_min = κ × ρ₆_min ≈ 1.2735

## Computation

From G29 formula: g₂²/g₃² = 15ρ₃³/(16πρ₆⁶)

On the trajectory ρ₃=κρ₆ this simplifies to:
```
g₂²/g₃² = 15κ³/(16πρ₆³) = 15/(16π) × (κ/ρ₆)³
```

At ρ₆ = ρ₆_min = 1.179:
- κ/ρ₆_min = 1.0801/1.179 = 0.9161
- (κ/ρ₆_min)³ = 0.7689
- g₂²/g₃² = 0.2984 × 0.7689 = **0.2295**

## Results

| Point | ρ₃ | ρ₆ | g₂²/g₃² | Gap from SM |
|-------|----|----|---------|------------|
| SM at M_Z | — | — | 0.2864 | 0% |
| Equal unit radii (G29) | 1.000 | 1.000 | 0.2984 | +4.2% |
| Physical vacuum (G87) | 1.2735 | 1.179 | **0.2295** | **−19.9%** |
| SM-matching on κ-trajectory | 1.183 | 1.095 | 0.2864 | 0% |

## Structural insight

On the trajectory ρ₃=κρ₆:
- g₂²/g₃² = 15/(16π) at ρ₆ = κ = 1.0801 (one specific point)
- g₂²/g₃² decreases as ρ₆ grows beyond κ
- Physical minimum ρ₆_min = 1.179 > κ = 1.081 → ratio is 20% below equal-radii

The gap between the coupling-matching scale (ρ₆ ≈ 1.095 for SM matching) and the
moduli minimum (ρ₆ = 1.179) is **+7.7%** — they do not coincide.

## "What this does NOT mean"

1. Does NOT mean the equal-radii prediction (0.2984) is wrong — it is valid at M_KK
2. Does NOT mean the physical vacuum is disfavored — it answers a different question
3. Does NOT prove λ is fixed (λ = FREE_COUPLING_PARAMETER maintained)
4. Does NOT establish the coupling ratio at any physical energy scale (requires knowing M_KK in GeV)
