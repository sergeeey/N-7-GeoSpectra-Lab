# C222 Decision -- Invariant subspaces on S^2: scalars under dragging, and the spin-1/2 doublet under the total action

**Date:** 2026-11-02

## Result

Exact sympy plus numeric checks, 39 checks in four scripts. (1) Scalar functions on S^2 under the dragging action (pullback by rotations) decompose into integer spins only, so no spin-1/2 invariant subspace exists among scalars. (2) Under the total action (rotation of the argument together with rotation of the two-component spin index) the pair Psi = (-(1-cos theta)/2, e^{i phi} sin theta / 2), Phi = J_- Psi spans a j = 1/2 doublet whose components lie in span{1, x, y, z}. (3) That doublet is not unique: for every [a:b] in CP^1 the subspace {Psi_v} is invariant under the total action, so the spin-1/2 invariant subspaces form a one-parameter family; the inner product within one subspace is 4 pi (|a|^2+|b|^2) <v,w> and across two subspaces 4 pi (conj(a) a' + conj(b) b') <v,w>. (4) A function in L^2 is an L^2 sum of harmonics, so a statement that a half-integer field 'cannot be a linear sum of harmonics' can only refer to scalar coefficients on the scalar space.

## Scripts and outputs (re-run in this folder)

| script | output | outcome |
|---|---|---|
| `q3_invariant_subspace.py` | `run_output_q3_invariant_subspace.txt` | 9 PASS, 0 FAIL |
| `q3b_spin_half_isotypic.py` | `run_output_q3b_spin_half_isotypic.txt` | 11 PASS, 0 FAIL |
| `q3c_uniqueness.py` | `run_output_q3c_uniqueness.txt` | 12 PASS, 0 FAIL |
| `q3d_corrections.py` | `run_output_q3d_corrections.txt` | 7 PASS, 0 FAIL |

## Conventions

J = L + S with L = -i x cross grad and S the spin matrices, as in the script docstrings; Psi, Phi as in the statement (the eta frame of C184).

## What this does NOT imply

- which of the CP^1 family, if any, the correspondent means, or whether he means the dragging action alone or the total action
- that the total action is physically the correct action for his model
- that the doublet is selected by any field equation: only invariance under rotations is tested

## Caveat

Some checks are definitional or duplicate each other (q3 K4d duplicates K4b; the scalar-trivial control in q3b is +1 by construction); the evidence is the exact representation-theory checks, not the count.

## Notes

Result row R04 of the private correspondence layer. Status vocabulary follows the ledger; no result here is externally reviewed.
