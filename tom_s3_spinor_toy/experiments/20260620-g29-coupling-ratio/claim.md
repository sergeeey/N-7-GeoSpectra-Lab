# Claim — G29: Geometric coupling ratio g₂/g₃ vs SM

**Date:** 2026-06-20  
**Question type:** Predictive  
**FL tier:** Standard

## Falsifiable Claim

The S³×S⁶ spectral action formula (G28) predicts:

```
g₂²/g₃² = 15ρ₃³ / (16π ρ₆⁶)
```

At equal compactification radii (ρ₃=ρ₆=1, natural choice):

```
g₂²/g₃² = 15/(16π) ≈ 0.2984
```

This matches the SM observed value at M_Z (0.2865) within 4.3%, with zero free parameters.

## Kill Conditions

FAIL if at equal unit radii:
- Predicted g₂²/g₃² > 1 (wrong hierarchy g₂ > g₃)  
- Error vs SM at M_Z exceeds 50%
- Unification condition ρ₃/ρ₆² = (16π/15)^{1/3} gives ratio ≠ 1.000

## Results [VERIFIED — computation]

| Scale | SM g₂²/g₃² | ρ₃/ρ₆² needed | Notes |
|-------|------------|----------------|-------|
| M_Z = 91.2 GeV | 0.28645 (PDG 2022) | 0.98645 | 1.4% from unity |
| Equal radii (natural) | 0.29842 | 1.00000 | +4.3% off SM |
| GUT (MSSM) | 1.00000 | 1.49644 | = (16π/15)^{1/3} exact |

**Fine-tuning measure:** to reproduce SM at M_Z exactly, need ρ₃/ρ₆² = 0.986 — only 1.4% from the natural equal-radius value. No fine-tuning required at the % level.

## What This Does NOT Mean

- Does NOT predict g₂ or g₃ individually (only the ratio; f₀ is free)
- Does NOT account for 4D running between M_KK and M_Z (this is tree-level)
- Does NOT prove unification in SM (SM does not unify exactly; MSSM does)
- Normalization convention for Tr in SU(2) vs SU(3) reps introduces ×2 ambiguity in absolute couplings (only ratio is unambiguous)

## Sources

- SM values: PDG 2022 (arXiv:2206.00019)
  - α_s(M_Z) = 0.1180, sin²θ_W(M_Z) = 0.23122, α_EM(M_Z) = 1/127.951
- MSSM GUT: α_GUT ≈ 1/24 at M_GUT ≈ 2×10¹⁶ GeV
- Formula source: G28 inner fluctuation computation
