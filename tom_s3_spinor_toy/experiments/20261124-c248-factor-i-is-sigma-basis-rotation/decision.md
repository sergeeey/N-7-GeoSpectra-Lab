# Decision C248

**Verdict:** PROMOTE as a recorded convention (truth_status PROVED by exact arithmetic; finding_status QUALIFIED: convention, not result).

Ledger: C248_FACTOR_I_IN_SECOND_COMPONENT_IS_PAULI_BASIS_ROTATION_U_DIAG_1_I

## Evidence

- `scripts/verify_factor_i_basis_rotation.py`, run 2026-11-24 with `python -I`: exit 0, "22 exact SymPy checks passed" (`logs/run_verify_factor_i.txt`).
- Positive controls: the unphased Pauli identity for a = 1, 2, 3; Lie brackets [D_a, D_b] = i eps D_c; radius invariance.
- Negative controls: for the phased doublet the original identity fails for D_1 and D_2 and the original ladder fails for D+ and D- (four assertions that must be False, and are).
- Residuals printed: ladder residuals [0, -xi2 + i xi2, xi1 - i xi1, 0]; transformed sigma as in claim.md.

## Provenance and independence

The script was written outside this repository (external analysis, 2026-11-24, sha256 of the original 15a01cd15d98169c...), copied with ruff fixes, a new docstring, and one change of mechanism: check() exits non-zero instead of using assert (which python -O would strip). It was re-run here; it was not rewritten independently. Same model family on both sides, no human review. The identity is elementary (conjugation by a diagonal unitary), so the risk is low.

## Use

Prepares the reading of any answer to the open question about the factor i: if the correspondent writes (xi1, i xi2), it is the same doublet in a rotated Pauli basis. Not for sending (project rule 10).
