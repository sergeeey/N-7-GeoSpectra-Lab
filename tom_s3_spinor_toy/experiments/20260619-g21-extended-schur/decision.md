# Decision — G21-EXTENDED-SCHUR

**Date:** 2026-06-19  
**Verdict:** PROMOTE  
**Go/no-go:** GO

## Result
PASS_G21_EXTENDED_SCHUR — dim=12 without B-L, dim=8 with B-L; S⁶ necessary for full distinguishability.  
Schur's lemma analysis: without B-L charge, D_F intertwiner space has dim=12 (under-constrained). Adding B-L (K₃ from S⁶) reduces to dim=8; further CPT gives 4. S⁶ is REQUIRED to distinguish all 8 fermion types.

## Scientific significance
S⁶ is not just sufficient but NECESSARY for the full fermion content. Without S⁶ (and its K₃ generator providing B-L), the fermion types are degenerate and cannot be fully distinguished by the intertwiner.

## Caveats
- Analysis uses Schur's lemma for the commutant; physical zero-mode analysis is separate
- Closes "Угол 2 — Extended Schur" of the CSDR 5-angle plan
