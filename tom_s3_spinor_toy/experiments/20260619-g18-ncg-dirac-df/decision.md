# Decision — G18-NCG-DIRAC-DF

**Date:** 2026-06-19  
**Verdict:** PROMOTE  
**Go/no-go:** GO

## Result
PASS_G18_NCG_SPECTRAL_TRIPLE — KO-dimension 6 spectral triple (γ_F, J_F, D_F) constructed; 4 free Yukawa parameters confirmed.  
J_F²=+1, {J_F,γ_F}=0, [D_F,J_F]=0 — standard KO-dim 6 relations. [SIGN
CORRECTED 2026-08-10, C36: this line originally said `J_F²=−1`, contradicting
this experiment's OWN code, which asserts `J_F**2 == sp.eye(32)` (g18_ncg.py:156)
and whose docstring line 17 states `J_F² = I`. `J_F` is 16 real transpositions,
so the antilinear square equals the linear one. The −1 propagated to 10 other
documents including preprint.tex before being caught.] H_F = 32-dim SM NCG Hilbert space verified.

## Scientific significance
Establishes that S³×S⁶ admits the NCG spectral triple structure required by Connes-Chamseddine-Marcolli. The KO-dimension 6 is not postulated but follows from the anticommutation relations of the geometric operators.

## Caveats
- 4 free Yukawa parameters remain free (derived as a COUNT in G25, not fixed values)
- Spectral action Tr f(D/Λ²) not computed here
