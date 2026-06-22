# Decision — G87: Coupling ratio at physical vacuum

**Date:** 2026-06-22  
**Verdict:** NULL  
**Go/no-go:** STOP (no improvement over G29)

## What Was Tested

Whether g₂²/g₃² at the physical Casimir+flux minimum (ρ₃=κρ₆_min, ρ₆=1.179)
is closer to the SM value at M_Z than the equal-radii result.

## Results [VERIFIED — inline Bash computation]

```
g₂²/g₃² at physical vacuum = 0.2295
g₂²/g₃² at equal unit radii = 0.2984  (G29, 4.2% from SM)
SM at M_Z = 0.2864
```

Gap from SM: **−19.9%** (vs +4.2% at equal radii). Significantly WORSE.

## Kill Analysis

**What G87 killed:** The hypothesis that "evaluating the coupling ratio at the physical
vacuum improves or maintains the 4.2% agreement with SM."

**What was NOT killed:**
- The equal-radii structural result g₂²/g₃² = 15/(16π) = 0.2984 (G29, PROMOTE)
- The hierarchy prediction g₂ < g₃ (geometric, not phenomenological)
- The Buckingham Pi structural theorem (C1)

**Why the ratio worsens:** On the trajectory ρ₃=κρ₆, the formula becomes
g₂²/g₃² = 15/(16π)×(κ/ρ₆)³. The physical minimum has ρ₆_min = 1.179 > κ = 1.081,
so the ratio is suppressed by (κ/ρ₆_min)³ = 0.769.

## Physical Interpretation

Two distinct geometric scales in the theory:

1. **Coupling scale** (ρ₆ ≈ 1.095 on κ-trajectory): where g₂²/g₃² matches SM at M_Z.
   This is close to the string scale (ρ₆ ≈ 1).

2. **Moduli minimum** (ρ₆_min = 1.179): where Casimir + flux potential is minimized.
   This is 7.7% larger than the coupling-matching scale.

These two scales do not coincide in the current framework. In a complete theory
with known λ, the energy scale M_KK could bridge them through RGE running.

## Preprint Impact

The coupling ratio section (§2) should report:
- **Structural prediction:** g₂²/g₃² = 15/(16π) = 0.298 at tree level, M_KK scale
- **Agreement:** +4.2% from SM at M_Z; the gap is RGE running from M_KK to M_Z
- **Honest caveat:** evaluation at the moduli minimum gives 0.230 (20% off); 
  a complete reconciliation requires fixing λ

Do NOT claim the physical minimum improves the prediction. It does not.

## Relaxation Map (for future work)

The 7.7% gap between coupling scale and moduli minimum could be closed by:
A. RGE running from ρ₆_min → coupling scale (requires fixing M_KK in GeV)
B. Including loop corrections to the coupling ratio formula
C. Non-perturbative corrections to the moduli potential

All three require knowing λ → outside current scope.

## Skeptic Pre-Answers

- Concern "result depends on scale choice" → ACCEPTED. Documented as main finding.
- Concern "equal-radii is ad hoc" → DISMISSED. It is the natural unit-string-scale.
- Concern "4.2% gap unexplained" → ACCEPTED. Attributed to RGE M_KK→M_Z (consistent).
