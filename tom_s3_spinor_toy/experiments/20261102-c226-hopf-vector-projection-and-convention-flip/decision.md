# C226 Decision -- Doublet times adjoint, projection to the vector, SO(3), normalisation, and the active/passive convention

**Date:** 2026-11-02

## Result

Exact sympy plus numeric checks, 30 checks. (1) For F = xi xi^dagger and V^i = (1/2) tr(F sigma^i) = (1/2) xi^dagger sigma^i xi: F = (1/2)|xi|^2 I + V^i sigma^i exactly, and sum_i V^i V^i = |xi|^4/4 as a polynomial identity. (2) V(g xi) = R(g) V(xi) with R_ij = (1/2) tr(sigma_j g^dagger sigma_i g): R R^T = I and det R = +1 exactly at five rational SU(2) elements (symbolic xi) and numerically for 2000 random elements (max |R R^T - I| < 1e-15); every unit xi is g(xi)(1,0) with g(xi) = [[xi^1, -conj xi^2],[xi^2, conj xi^1]] and V(xi) = R(g(xi)) (0, 0, 1/2) (500 random points, deviation 1e-16); V is invariant under xi -> e^{i phi} xi, |V| = |xi|^2/2. (3) The doublet psi = lambda xi with lambda^2 = sqrt(3/pi) on |xi| = 1 gives V = sqrt(3/(4 pi)) n, the sphere-normalised vector harmonics of C220; psi changes under the phase, so it is a section, not a function on S^2. (4) The active reading xi -> g xi and the reading f(g^-1 xi) give generators that differ by an overall sign: the D_3 weights on (xi^1, xi^2) change from (-1/2, +1/2) to (+1/2, -1/2) and at the same time [D_a, D_b] = +i eps D_c becomes -i eps D_c; with the first convention (D_1 + i D_2) psi = (-lambda xi^2, 0), (D_1 - i D_2) psi = (0, -lambda xi^1), with the second the signs are opposite. The weight +1/2 on the first component together with the standard algebra belongs to conj(xi).

## Scripts and outputs (re-run in this folder)

| script | output | outcome |
|---|---|---|
| `hopf_vector_map_stages_check.py` | `run_output_hopf_vector_map_stages_check.txt` | 30 PASS, 0 FAIL |

## Conventions

Two conventions compared side by side: A = U(g) f = f(g^-1 xi) (as in C225); B = xi -> g xi acting on the components.

## What this does NOT imply

- which convention is physical, or which the correspondent intends: the sign flip is a mathematical fact about the two readings
- that psi = lambda xi is a field on S^2: it is a section of the Hopf bundle
- that the weight assignment of C225 is wrong: it is the consistent choice with [D_a, D_b] = +i eps D_c

## Caveat

The numeric parts (S2c, S2d, S3b) are random-sample checks, not proofs; the sample sizes are given in the statement. The normalisation check S4c is arithmetic, not an independent test.

## Notes

Result rows R10, R11 and R12 of the private correspondence layer; computed on 2026-11-02 after the correspondent's message of that date. Status vocabulary follows the ledger; no result here is externally reviewed.

Correction (2026-11-04), see C229: the reading 'xi -> g xi' used above as the 'active' one is the substitution f(g xi), which is an ANTI-representation ([D_a, D_b] = -i eps D_c, D_B = -D_A componentwise); it is not an 'active' reading in a physical sense. The correspondent's formulation (components transform as the defining representation, no inverse) corresponds to reading C, f(g^T xi) (representation, weights (+1/2,-1/2), [D_a, D_b] = +i eps D_c), or, read literally, to f(g xi) (reading B). The mathematics of C226 is unchanged; only this label and the sentence 'the weight +1/2 on the first component together with the standard algebra belongs to conj(xi)' need the C229 reading C as a qualification: reading C gives (+1/2,-1/2) on (xi^1,xi^2) with the standard algebra.
