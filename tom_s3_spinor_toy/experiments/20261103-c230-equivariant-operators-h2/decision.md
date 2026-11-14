# C230 Decision -- H2 and equivariant first-order operators

**Date:** 2026-11-03

## Result

Exact sympy, 19 asserted checks, exit 0 (`run_output_equivariant_operators_h2.txt`).

- The four operators 1, sigma.L, Gamma, Gamma sigma.L commute with J (generic F), and a control (L_z alone) does not.
- On the j = 1/2 multiplicity space with basis chi (l = 0) and Gamma chi (l = 1): O = [[a, c-2d],[c, a-2b]]; the four operators span all 2x2 matrices (rank 4), so the family is complete on that block.
- Psi = -chi/2 + Gamma chi/2, Gamma Psi = -Psi. General identity: O Psi = (a - b - c + d) Psi + ((b + d)/2) A Psi, with A Psi in ker(Gamma - 1) pointwise and nonzero.
- Therefore H2 is invariant under O exactly when b + d = 0; then O Psi = (a - c - 2b) Psi and O Phi = (a - c - 2b) Phi.
- D0-type A has (a,b,c,d) = (2,2,0,0), b + d = 2: not preserved (agrees with C228).
- Example that preserves H2: O* = (1 - Gamma) sigma.L (eigenvalue -2 on H2); equivalently A' = A - 2 Gamma sigma.L = 2(1 + (1 - Gamma) sigma.L).
- A constant matrix M cannot repair A: the exact sample-point system for (A + M) H2 in H2 is inconsistent. For O* the same solver returns exactly M = lambda * 1, so the solver can say yes.

So the C228 exclusion is robust against added constant matrix terms but NOT against added point-dependent terms: a Gamma-dependent first-order term (b + d = 0) preserves H2.

## What this does NOT imply

- that O* is physical; it is a first-order equivariant operator that kills the cross-term between the Gamma = +1 and Gamma = -1 sub-bundles
- that the correspondent's field equation is in this family

## Caveat

The family is complete on the j = 1/2 multiplicity block (rank 4), not proved complete among all equivariant first-order operators on all j. The constant-M result rests on a six-point exact sample system plus its control, not on a symbolic identity.

Ledger: C230_H2_PRESERVED_BY_EQUIVARIANT_FIRST_ORDER_OPERATOR_IFF_B_PLUS_D_ZERO_CONSTANT_MATRIX_CANNOT_REPAIR_D0
Follow-ups: none
