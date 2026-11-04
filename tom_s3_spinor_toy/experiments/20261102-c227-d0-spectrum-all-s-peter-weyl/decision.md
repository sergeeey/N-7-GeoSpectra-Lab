# C227 Decision -- Spectrum of D0 on C^2-valued functions on S^3: all s by Peter-Weyl, checked to s = 3

**Date:** 2026-11-02

## Result

D0 = -i sum_a sigma_a X_a^R on L^2(S^3, C^2), with C = -1 (T_a = -i sigma_a), has eigenvalue -2s with multiplicity (2s+1)(2s+2) and eigenvalue 2s+2 with multiplicity (2s+1)(2s), for s = 0, 1/2, 1, 3/2, ... . Evidence: (a) a derivation by hand from Peter-Weyl (L^2(S^3) = sum V_s x V_s; D0 = -4 S.K; total spin s+1/2 gives -2s, total spin s-1/2 gives 2s+2), not checked by a tool; (b) the full spectrum of D0 on the 60-dimensional space of degree <= 3 polynomials modulo |x|^2 - 1 matches the formula, as do all 9 weight sectors, with [D0, J_3] = 0 (floating-point eigenvalues, exact matrix entries); (c) an independent numeric check by a fresh-context subagent, different SU(2) parametrisation, harmonic homogeneous polynomials of degree 0 to 6 (s up to 3), every degree matches with invariance residual at most 8e-14; (d) D0 - 3/2 reproduces the degeneracy (n+1)(n+2) of each of the eigenvalues +-(n+3/2) of Camporesi-Higuchi gr-qc/9505009 eq. (3.58), checked against the PDF text by the same subagent.

## Scripts and outputs (re-run in this folder)

| script | output | outcome |
|---|---|---|
| `weight_sectors_d0_check.py` | `run_output_weight_sectors_d0_check.txt` | numeric output (no PASS/FAIL lines); read the listed values |
| `independent_subagent_check_all_s_to_3.py` | `run_output_independent_subagent_check_all_s_to_3.txt` | numeric output (no PASS/FAIL lines); read the listed values |

## Conventions

X_a^R quaternion right-multiplication fields; T_a = -i sigma_a (C = -1); J_a = X_a + T_a.

## What this does NOT imply

- that D0 - 3/2 is the geometric Dirac operator in the left-invariant frame: only equality of spectra is established
- the all-s statement beyond s = 3 by any tool: it rests on the hand derivation
- anything with the normalisation C = -1/2: every eigenvalue changes

## Caveat

The file name of the first script says deg2 but it uses N = 3, and its eigenvalues are floating point although the matrix entries are exact. The independent check is a fresh-context review by the same model family, not a human or a different-model review. It extends C180 (k <= 3) to s <= 3 numerically.

## Notes

Result row R13 of the private correspondence layer; independent review verdict CONFIRMED-REAL (fresh-context subagent, same model family). Status vocabulary follows the ledger; no result here is externally reviewed.
