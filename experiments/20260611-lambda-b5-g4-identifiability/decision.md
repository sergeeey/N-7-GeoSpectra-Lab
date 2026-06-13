# Decision — LAMBDA-B5-G4

**Date:** 2026-06-11  
**Verdict:** PROMOTE  
**Go/no-go:** GO

## Result
PASS_LAMBDA_NON_IDENTIFIABLE_WITHOUT_V — 8/8 checks (T2 assert added 2026-06-13)

- rank(J_phys) = 2, rank(J_full) = 3
- lambda non-identifiable from {Dirac spectrum, KK shift} alone
- lambda identifiable IFF V-operator observable is promoted

## Cross-model review (2026-06-12)
Codex FIX FIRST 7/10: negative half CONFIRMED ROBUST, positive half conditioned on kappa-independence.
See cross_model_review.md.

## ACH impact
- Case 3 H1 KILLED (lambda non-identifiable from S3)
- Case 3 H3 VERIFIED_FORMAL_THEOREM (lambda free until external constraint)
- ACH Case 3: FORK (spin structure pending Tom Q1)

## Security constraints (carry forward)
lambda = FREE_COUPLING_PARAMETER — do NOT claim fixed value
safe_for_runtime = False
