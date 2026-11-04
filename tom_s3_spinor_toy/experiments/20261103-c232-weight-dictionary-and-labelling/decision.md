# C232 Decision -- Weight dictionary and labelling

**Date:** 2026-11-03

## Result

Exact sympy, all asserted checks passed and all self-controls caught, exit 0 (`run_output_weight_dictionary_and_labelling.txt`).

- (J3L, J3R) on (g00, g01, g10, g11) = ((-1/2,+1/2), (-1/2,-1/2), (+1/2,+1/2), (+1/2,-1/2)); this reproduces the TOM-CERT-01 table independently.
- On every g_ab, 2*J3R equals the Hopf charge Q (xi-type +1, conj(xi)-type -1). So J3R on the right index is (1/2) diag(1,-1): the same diagonal as Gamma_2(T_12) = (1/2) diag(1,-1) in his equation (77), provided his index is b. This is a candidate dictionary entry: his "spin-weight-type condition" is the Hopf charge divided by 2.
- Relabelling a doublet by the swap sigma_x keeps [T_a,T_b] = i eps T_c, maps T_3 -> -T_3, T_2 -> -T_2, T_1 -> T_1, and keeps the Casimir 3/4. Hence "the first component has the negative eigenvalue" holds for (xi^1, xi^2) and for eta = (conj xi^2, -conj xi^1), and is reversed for (conj xi^1, conj xi^2) or for the swapped labelling: it is a labelling convention.

## What this does NOT imply

- that his claim "this is the wrong way round" is a mistake of his or ours: it is about labelling, which only he can fix
- that his index in (77) is the right index of g_ab

## Caveat

The identification with (77) rests on the diagonal alone; the text of (77) was not re-read here.

Ledger: C232_J3R_ON_RIGHT_INDEX_IS_HALF_HOPF_CHARGE_AND_WEIGHT_ORDER_IS_A_LABELLING_CONVENTION
Follow-ups: none
