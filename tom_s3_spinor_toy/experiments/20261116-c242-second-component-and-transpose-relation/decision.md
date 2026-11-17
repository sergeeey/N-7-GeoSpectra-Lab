# C242 Decision -- Second component of the doublet representative derived two ways, and the relation between two sign versions

**Date:** 2026-11-16

## Result

Exact sympy plus numeric checks, 23 checks (22 exact, 1 numeric with 500 random points, worst residual 4.0e-15). For V^i = (1/2) xi^dagger sigma^i xi: V^1 + i V^2 = conj(xi^1) xi^2 and V^3 = (1/2)(|xi^1|^2 - |xi^2|^2). With V = (r^2/2)(sin th cos ph, sin th sin ph, cos th), |xi| = r and xi^1 = r cos(th/2) real and positive, the unique solution is xi^2 = r e^{i ph} sin(th/2); the relative phase is fixed, only the common phase is free. For u = cos(th/2) I + i sin(th/2) n.sigma and xi = u (r,0)^T: xi^2 = r u_21 = i r sin(th/2)(n_1 + i n_2); for any unit n = (n_1, n_2, 0), V = (r^2/2)(-n_2 sin th, n_1 sin th, cos th). Under the INPUT assumptions (N) th n = (t1, t2, 0) and (R) sin ph = t1/th, cos ph = -t2/th: (t1 + i t2)/th = -i e^{i ph}, so the u-route gives the same xi^2 as the sphere route. The version with (t1 - i t2)/th = i e^{-i ph} has xi'^2 = -r e^{-i ph} sin(th/2); it equals u^T (r,0)^T (the other entry of u) for n = (t1,t2,0)/th, equals u (r,0)^T for n = (t1,-t2,0)/th, equals sigma_3 conj(xi), and gives V' = (-V^1, V^2, V^3), a map with determinant -1 (conjugation: V^2 -> -V^2; i sigma_3 lies in SU(2) and acts as a rotation by pi). Also xi' = conj(u^{-1}) (r,0)^T with conj(u) = (u^{-1})^T. At phi = 0, u is the real matrix [[c,-s],[s,c]] and xi = r (c, s) while xi' = r (c, -s); at phi = pi/2 the two versions coincide.

## Scripts and outputs

| script | output | outcome |
|---|---|---|
| `second_component_and_transpose_check.py` | `run_output_second_component_and_transpose_check.txt` | 23 PASS, 0 FAIL |

## Conventions

Standard Pauli matrices; V^i = (1/2) xi^dagger sigma^i xi; xi = u (r,0)^T; theta is both the norm of (t1, t2) and the polar angle (an input identification, not derived here); u_21 is the entry in row 2, column 1.

## What this does NOT imply

- that (N) or (R) hold for the correspondent's explicit u or coordinates: both are inputs
- which of the two sign versions the correspondent intends
- that the orientation reversal has a physical meaning, or that it is the same issue as the anti-representation / transposed readings of C229: only an algebraic relation (the second version is built from u^T) is shown; the link to reading C of C229 is a hypothesis

## Caveat

Same-model-family review only; the numeric part is a random-sample check; no independent human review. Hand re-derivation by the project owner has not been done at the time of writing (a worksheet exists in the private correspondence folder).

## Notes

Result row R18 of the private correspondence layer; computed 2026-11-16 after the correspondent's message of that date. The closing question of the letter that uses these results asks which n the correspondent uses, because that decides which entry of u the printed combination is.

Ledger: C242_SECOND_COMPONENT_E_I_PHI_SIN_HALF_THETA_FIXED_BY_V_AND_BY_U_UNDER_STATED_INPUTS_OTHER_SIGN_VERSION_IS_THE_U_TRANSPOSE_ENTRY_DETERMINANT_MINUS_ONE
