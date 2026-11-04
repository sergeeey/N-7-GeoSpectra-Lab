# C228 Decision -- The j = 1/2 doublet H2 on S^2 is not invariant under D0

**Date:** 2026-11-02

## Result

With A = D0 - I, Gamma = sigma.n, Psi = (-(1-cos theta)/2, e^{i phi} sin theta/2), Phi = J_- Psi and H2 = span{Psi, Phi}: (1) numerically (sympy and float), Gamma Psi = -Psi and Gamma Phi = -Phi, J_- commutes with Gamma on a generic field, {A, Gamma} = 0, and the relative residual of A Psi on span{Psi, Phi} is 1.000 with coefficients 0; ||A Psi||/||Psi|| = 2, A^2 = 4 on the block, P2 A P2 = 0 to 1e-16. (2) An independent test by a fresh-context subagent on S^3: lifting Psi and Phi by T with pi(g) = g sigma_3 g^dagger and applying D0 directly gives projection coefficients [1, 0] and [0, 1] onto H2, ||D0 F||^2 / ||F||^2 = 5 and ||residual||^2 / ||F||^2 = 4, so the part of D0 Psi outside H2 has norm 2 ||Psi||; controls: D0 of a constant spinor is 0 and D0 T(const) = 3 T(const). Hence D0 H2 is not contained in H2.

## Scripts and outputs (re-run in this folder)

| script | output | outcome |
|---|---|---|
| `h2_noninvariance_gamma.py` | `run_output_h2_noninvariance_gamma.txt` | numeric output (no PASS/FAIL lines); read the listed values |
| `h2_j12_block.py` | `run_output_h2_j12_block.txt` | numeric output (no PASS/FAIL lines); read the listed values |
| `independent_subagent_check_s3_lift.py` | `run_output_independent_subagent_check_s3_lift.txt` | numeric output (no PASS/FAIL lines); read the listed values |

## Conventions

L = -i x cross grad (the step [J_-, Gamma] = 0 fails for L = +i x cross grad, probed by the subagent); lift T uses pi(g) = g sigma_3 g^dagger; side (left or right) convention of the correspondent not decided.

## What this does NOT imply

- that no other doublet is D0-invariant: any nonzero subspace of ker(Gamma + 1) fails to be invariant in the same way, so the statement is weak
- which side convention (left or right) the correspondent uses: left open
- the analytic argument (Gamma-anticommutation, injectivity of A): it is in a private working draft and is not part of the tracked evidence

## Caveat

Numerical evidence plus a fresh-context independent test; the analytic proof is not tracked. The independent check is by the same model family. Motivating hypothesis (H2 is invariant under D0, i.e. a selection by D0) fails, hence test_outcome FAIL with a supported negative finding.

## Notes

Result row R14 of the private correspondence layer; independent review verdict CONFIRMED-REAL (fresh-context subagent, same model family). Status vocabulary follows the ledger; no result here is externally reviewed.
