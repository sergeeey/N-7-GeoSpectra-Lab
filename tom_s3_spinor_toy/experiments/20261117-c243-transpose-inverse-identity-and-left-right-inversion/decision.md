# C243 Decision -- The transposed SU(2) matrix is the inverse element conjugated by sigma2; inversion on S^3 reverses orientation and swaps left and right

**Date:** 2026-11-17

## Result

Exact sympy plus numeric checks, 13 checks. For u in SU(2) written u = [[a, -conj b], [b, conj a]] (a, b, conj a, conj b independent symbols; then a conj a + b conj b = 1): u^T = sigma2 u^{-1} sigma2 and u^T e1 = i sigma2 u^{-1} e2, so the doublet built from the first row of u equals the inverse element acting on the other basis vector, up to a fixed unitary and a phase; numerically on 500 random elements, worst residual 6e-16. In quaternion coordinates inversion is (x0, x) -> (x0, -x), determinant -1 on R^4 (it reverses the orientation of S^3), and (h g k)^{-1} = k^{-1} g^{-1} h^{-1} (it turns left translation by h into right translation by h^{-1}). Negative controls: for ONE pair of doublets of C242 an SU(2) element mapping xi_+ to xi_- exists (transitivity), but the linear map V_+ -> V_- fixed by three independent points is diag(-1,1,1) with determinant -1, so no FIXED SU(2) element realises it at all points; and xi' = sigma_3 conj(xi) of C242 holds for n3 = 0 only (median residual 0.56 for generic n3).

## Status of each part

| part | status |
|---|---|
| u^T = sigma2 u^{-1} sigma2 and u^T e1 = i sigma2 u^{-1} e2 for SU(2) | EXACT |
| the transposed-entry doublet is the inverse element acting on the other basis vector | EXACT (a restatement of the identity) |
| inversion on S^3 reverses orientation | standard fact, checked in quaternion coordinates |
| inversion turns left translation into right translation | EXACT |
| link to the choice of the spin SU(2) | HYPOTHESIS |
| link to the earlier contragredient-representation issue | UNVERIFIED |

## Addendum 2026-11-17: reading C of C229

Reading C, (U_C(g) f)(xi) = f(g^T xi), is reading A, (U_A(g) f)(xi) = f(g^{-1} xi), in the fixed variables sigma2 xi: U_C(g) = S U_A(g) S, (Sf)(xi) = f(sigma2 xi). Follows from g^T = sigma2 g^{-1} sigma2 (E2). Numeric: 300 random SU(2) elements, random quadratic f, worst residual 1.1e-14; both readings satisfy U(gh) = U(g)U(h) in 300 of 300 (reverse order in 0 of 300), so reading C is an ordinary representation. The generator comparison (R3) is a weak check (same arithmetic path on both sides, residual exactly 0). Status: exact identity plus numeric support. Not established: which SU(2) is the spin, R05, R12. Consequence: reading C adds no representation beyond reading A in rotated variables. A symbolic run with a generic function was started and stopped unfinished.

## Scripts and outputs

| script | output | outcome |
|---|---|---|
| `transpose_inverse_identity_check.py` | `run_output_transpose_inverse_identity_check.txt` | 13 PASS, 0 FAIL |
| `reading_C_vs_A_numeric_check.py` | `run_output_reading_C_vs_A_numeric_check.txt` | 3 PASS, 0 FAIL |

## Conventions

Standard Pauli matrices; u = [[a, -conj b], [b, conj a]]; e1 = (1, 0)^T, e2 = (0, 1)^T; left translation L_h g = h g, right translation R_k g = g k.

## What this does NOT imply

- that the sign question of C242 is a question of left versus right SU(2), or which SU(2) is the spin: a HYPOTHESIS, needing the correspondent's explicit definitions
- anything about the earlier contragredient-representation issue (UNVERIFIED)
- that SU(2) cannot map one doublet to another: for one pair it can; only a FIXED element realising the reflection at all points is excluded
- that inversion on S^3 is the same map as the reflection of the 2-sphere in C242

## Caveat

Same-model-family review only; the S^3 orientation and left/right facts are standard, not newly derived; no independent human review. The reading-C cross-check (addendum) is numeric plus the exact identity.

## Notes

Result row R19 of the private correspondence layer; computed 2026-11-17 after an external note was compared with C242. An earlier wording in the working discussion, that no SU(2) element can map one doublet to the other, was wrong and is corrected here by negative control N1.

Ledger: C243_TRANSPOSE_OF_SU2_ELEMENT_IS_SIGMA2_INVERSE_SIGMA2_INVERSION_REVERSES_S3_ORIENTATION_AND_SWAPS_LEFT_RIGHT_LINK_TO_SPIN_CHOICE_IS_HYPOTHESIS
