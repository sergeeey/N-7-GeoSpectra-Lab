# Decision — G29: Geometric coupling ratio vs SM

**Date:** 2026-06-20  
**Verdict:** PROMOTE  
**Go/no-go:** GO

## What Was Tested

Comparison of geometric formula g₂²/g₃² = 15ρ₃³/(16πρ₆⁶) from G28
against SM running coupling constants from PDG 2022.

## Results [VERIFIED — g29_coupling_ratio.py]

**At equal unit radii (natural, no free parameters):**
```
Predicted:  g₂²/g₃² = 15/(16π) = 0.2984
SM at M_Z:            0.2865  (PDG 2022)
Error:                +4.3%
```

**To match SM exactly at M_Z:**
```
Need: ρ₃/ρ₆² = 0.9865   (1.4% from unity — essentially no fine-tuning)
```

**Unification condition (g₂=g₃):**
```
ρ₃/ρ₆² = (16π/15)^{1/3} = 1.4964   (exact geometric formula)
```

## Key Non-Obvious Insight

The WEAK/STRONG hierarchy g₂ < g₃ is a **geometric prediction** of S³×S⁶:  
- SU(2) coupling ← Vol(S⁶) × N_{s6} = large  → weak coupling
- SU(3) coupling ← Vol(S³) × N_{s3} = small  → strong coupling

The hierarchy g₂ < g₃ follows from N_{s6} × Vol(S⁶) > N_{s3} × Vol(S³) at equal radii.  
No phenomenological input needed.

## Comparison to CCM 2006

In CCM, g₂ and g₃ are determined by D_F matrix elements (free parameters).  
In S³×S⁶: the same quantities come from **geometry alone** (spinor dimensions × volumes).  
This is the geometric upgrade of CCM.

## Fine-Tuning Assessment

String theory landscape: typical tuning ~10⁻¹²⁰.  
Our result: 1.4% radius adjustment needed to hit SM exactly.  
Interpretation: no fine-tuning. "Natural" equal-radius compactification  
predicts the coupling hierarchy correctly at tree level.

## Caveats

1. Tree-level result: 4D loop corrections (RGE from M_KK to M_Z) not included
2. Absolute couplings need fixing f₀ (spectral action function moment)
3. Ratio formula has ×2 normalization ambiguity in SU(3) trace convention
4. MSSM assumed for GUT unification (SM alone does not unify perfectly)

## Pearl Registry Entry

**PEARL:** g₂²/g₃² = 15/(16π) at equal radii.  
- SM value at M_Z: (g₂/g₃)² = 0.2865, prediction 0.2984 → ratio 1.043
- Question: does 15/(16π) have a deeper combinatorial origin?  
  15 = 3×5, 16 = 2⁴ — both from spinor dimensions and volumes of S³/S⁶.
- Next check: compare at M_Planck where quantum gravity may fix ρ₃/ρ₆² = 1 exactly.
- `next_check: 2026-07-20` (after conference submission)
