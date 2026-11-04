# C229 Decision -- Three readings of the SU(2) action, asserted

**Date:** 2026-11-03

## Result

Exact sympy, 29 asserted checks and 5 self-controls, exit 0 (`run_output_conventions_asserted_check.txt`). Derived from the definitions with exact g_a(t) = cos(t/2) + i sin(t/2) sigma_a:

- A: f(g^-1 xi): representation, [D_a, D_b] = +i eps D_c, D3 weights (-1/2, +1/2) on (xi^1, xi^2), [D3, D+] = +D+, D+ xi = (-xi^2, 0).
- B: f(g xi): anti-representation, D_B = -D_A componentwise, [D_a, D_b] = -i eps D_c, weights (+1/2, -1/2), [D3, D+] = -D+ (D1 + i D2 lowers).
- C: f(g^T xi): representation, [D_a, D_b] = +i eps D_c, weights (+1/2, -1/2), D+^C = -D-^A. So "weights flipped" does not imply "commutator flipped".
- Casimir 3/4 on xi in all three: nothing physical separates them.
- V(g xi) = R(g) V(xi) with R_ij = (1/2) tr(sigma_j g^+ sigma_i g) for generic g (a, b, conj a, conj b independent), R R^T = (|a|^2+|b|^2)^2 I, det R = (|a|^2+|b|^2)^3, every entry of R real as a polynomial.
- Integral over S^2 of (lambda^2 V_i)^2 = 1 for lambda^2 = sqrt(3/pi), computed.

## What this does NOT imply

- which reading is the correspondent's; that needs his text
- that anything in C225/C226 was wrong: their mathematics is confirmed, only the testing of convention B was print-only

## Caveat

The C row `D+ xi` for reading C is derived, not predicted. Reality and orthogonality of R hold for symbolic g; the S^2 integral is symbolic. Same-model-family review only.

## Notes

Not recorded in CLAIM_LEDGER.yaml (not authorised).

Ledger: C229_THREE_READINGS_OF_SU2_ACTION_A_AND_C_ARE_REPRESENTATIONS_B_IS_ANTIREPRESENTATION_WEIGHTS_AND_ALGEBRA_SIGN_ASSERTED
Follow-ups: none
