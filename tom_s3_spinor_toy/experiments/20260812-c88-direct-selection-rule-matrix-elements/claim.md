# C88 -- direct selection-rule matrix elements; corrects C86/C87's methodology and finds a genuine S3-side coupling channel

**Experiment id:** `20260812-c88-direct-selection-rule-matrix-elements`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C86, C87 (joint-level eps-sweep coupling tests).
Directed by an integrity check performed while scoping the round after
C87: `d_joint_base`'s Hermiticity residual was `0.0` at k=1 (C86, valid)
but `2.0` at k=2 (C87, INVALID -- `eigvalsh` silently assumes Hermitian
input).

---

## Why this round exists

`np.linalg.eigvalsh`, used throughout C81-C87's own eps-sweep
methodology, silently reads only the Hermitian part of its input matrix
and does not error on non-Hermitian input. C87's own `d_joint_base` at
k=2 was found to be genuinely non-Hermitian (residual `2.0`, not a
numerical-precision-level artifact). This is a real methodological gap
in the eps-sweep approach once `D_S3` itself stops being Hermitian
(true for k>=2, per C85's own certification work -- Meier's `|p>` basis
is not orthonormal, and the certified `l_{e3}` generator is genuinely
not anti-Hermitian beyond k=1).

Rather than patch the eps-sweep and hope, this round asks the DIRECT
question the external reviewer's own C84B framing originally posed:
compute the actual matrix elements `<n',m'|T|n,m>` connecting adjacent
Peter-Weyl eigenspaces. This needs no Hermiticity assumption, no S6
factor, and no eps-sweep -- `D-bar` is guaranteed DIAGONALIZABLE (not
merely real-eigenvalued) by its own minimal polynomial
`(D-bar+k)(D-bar-(k+2))=0` (distinct roots), certified in C85, so a
general (non-Hermitian) eigendecomposition gives a valid, complete
eigenbasis regardless of whether it is orthonormal, and transforming any
operator into that eigenbasis via similarity (`S^-1 X S`) correctly
reads off inter-eigenspace matrix elements.

## The claim under test

> **C88.** `Z_i` (round67's level-independent Clifford generator, the
> S3-side factor of C79-C83's own coupling operator T), embedded in
> `D-bar`'s own `(p,r)` basis, is tested for nonzero matrix elements
> connecting the "-k" eigenspace (physical n=k, sigma=-1) to the "+k+2"
> eigenspace (physical n=k-1, sigma=+1), for k=1,2,3,4. This is
> genuinely undetermined in advance -- a nonzero result would mean a
> real S3-side coupling channel exists between adjacent Peter-Weyl
> levels (independent of whether it produces an actual eigenvalue
> crossing in any specific joint operator with S6); a zero result would
> mean C86/C87's own "clean NULL" findings reflect the absence of any
> coupling channel at all, not merely the absence of a crossing in the
> specific tested operator.

## Predictions, recorded before running the permanent script

| # | Prediction | Outcome |
|---|---|---|
| **P1 (diagonalizability)** | D-bar's eigenvalues have zero imaginary part (general eig), and the eigenvector reconstruction is exact to machine precision | pending |
| **P2 (eigenspace dimensions)** | match round67's own target ((k+2) and k per copy) for k=1..4 | pending |
| **P3 (matrix elements)** | genuinely undetermined -- either all-zero (confirming C86/C87's "no coupling" reading) or nonzero (requiring the precise reading: "coupling exists, doesn't produce a crossing in the specific tested operator") | pending |

## kill_criterion

P1/P2 failing means the construction itself has a bug (reusing C85's
already-certified substrate incorrectly) -- stop and fix before trusting
anything downstream (the script does not proceed past this without these
checks). P3 is the actual, genuinely open question this round answers.

## What this cannot show

- Does **not** determine whether the JOINT (S3xS6) operator's spectrum
  ever crosses zero due to this coupling channel -- that requires the
  eps-sweep machinery (C86/C87), now corrected for Hermiticity.
- Does **not** test k>=5.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
