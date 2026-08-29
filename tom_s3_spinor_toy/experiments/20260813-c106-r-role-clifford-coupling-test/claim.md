# C106 claim -- does the r-index actually need to be touched by the
# off-diagonal multiplication coupling, or is "r-untouched" a harmless
# simplification?

## L0 gate (EstimandOps)

**Question type:** Descriptive (does a specific alternative algebraic
construction have property X: exactly real spectrum?). Not causal, not
predictive -- no population, no intervention/comparator in the clinical
sense. A single well-defined mathematical object either has a real
spectrum or it doesn't.

## Background -- why "r's role" was still open

Every D_PW construction so far (C101, C102, C103, C105) used the
off-diagonal coupling block `B_k := M_k (x) I_r` -- i.e. the CG-based
multiplication operator `M_k` (built on the joint (q,p) index, C99/C100)
tensored TRIVIALLY with the identity on the 2-dim spinor/Clifford index
`r`. Every claim.md touching this construction (C101 onward) explicitly
flagged "r-untouched" as a POSTULATED ansatz, never derived -- see each
round's own Counterfactual Frame. C105's own Relaxation Map named this
explicitly as an unpursued relaxation: *"Revisit whether S needs a
nontrivial r-component after all -- ties back to the still-open 'r's
role' question from C99-C104."*

## Counterfactual Frame (exploratory round -- disclosed up front)

This round did NOT follow strict blind-prediction-before-data. Cheap
interactive scratch exploration (sympy/numpy, no files written) was run
FIRST to figure out whether "r's role" was even a well-posed, tractable
question, before committing to a formal claim. This exploration found:

1. **An exact algebraic identity**: `L_i(1) = -rmult_i` for i=1,2,3,
   entrywise, with the IDENTITY similarity transform (no basis change
   needed at all) -- i.e. the r-space Clifford generators used inside
   `build_dbar` are literally the negative of the q-space L-generators
   at level k=1 (the certified L/R convention from C91-C98/C99).
2. Using this, a well-defined, certified-machinery-only construction of
   a "Clifford-type" (r-coupled) alternative to the r-untouched coupling
   was built and tested on C101's own minimal 2-level (k=1,2) D_PW.
3. That alternative ALSO gives an exactly real coupled spectrum.
4. A properly validated negative-control suite (see decision.md) showed
   this is NOT a trivial/vacuous test artifact -- the eigensolver
   reliably detects complex eigenvalues for genuinely asymmetric random
   couplings, and even "real, transpose-mirrored" random couplings are
   only SOMETIMES real (not universally), given D1/D2's degenerate
   spectra. So both the r-untouched AND r-coupled results are genuine,
   non-generic findings, not artifacts of the degenerate D1/D2 spectra.

The formal script below independently RE-DERIVES all of the above from
scratch (not by re-running/importing the scratch session), matching the
project's own established discipline (C105's own note: "this round's
formal script independently re-derives the preliminary scratch numbers
... confirms the scratch work was not itself in error").

## Entity / falsifiable predicate / measurable outcome (Zero-Signal Gate)

- **Entity**: the off-diagonal coupling block of C101's minimal 2-level
  (k=1,2) D_PW construction.
- **Falsifiable predicate**: replacing the r-untouched coupling
  `B_1 = M_1 (x) I_r` with a Clifford-type r-coupled alternative
  `B_1^Gamma := sum_i M_1^{(i)} (x) rmult_i` (built from an exact, closed-
  form Cartesian decomposition of C104's own 4 (a,b) CG components, no
  new free parameters) changes whether the coupled spectrum is exactly
  real.
- **Measurable outcome**: `max|Im(eig(D_PW))| < 1e-6` (same invariant
  gate convention as C101/C102/C103), computed via `np.linalg.eigvals`
  (general, non-Hermitian-assuming solver -- same certified convention).

## Predictions (stated before the formal script runs, though after the
disclosed scratch exploration above)

| # | Prediction |
|---|---|
| P0 | `L_i(1) = -rmult_i` exactly, for i=1,2,3, identity transform (reuse-sanity, re-derives scratch finding formally). |
| P1 | `B_1^Gamma` has the same shape as `B_1 = M_1 (x) I_r` (18x8) -- a valid drop-in replacement. |
| P2 | `B_1^Gamma` genuinely differs from `B_1` (not a trivial re-expression of the same object). |
| P3 | The 2-level D_PW built with `B_1^Gamma` has an exactly real spectrum (`max|Im| < 1e-6`). |
| P4 (negative control) | A FULLY asymmetric random real coupling (no B/B.H mirroring at all) gives a clearly non-real spectrum -- confirms the eigensolver is not vacuously always-real. |
| P5 (negative control) | Random real couplings placed with the SAME B/B.H-mirrored symmetric structure as B_1/B_1^Gamma are only SOMETIMES real (not 100%) across several trials -- confirms D1/D2's own eigenvalue degeneracy does not by itself force reality for an arbitrary mirrored coupling, so P3 (if it holds) is a genuine, non-generic structural fact about the CG-derived family specifically. |

## What this cannot show

- Does not identify a unique "correct" physical form of the r-coupling
  (Clifford-type is ONE natural candidate motivated by D-bar's own
  structure, not a derivation from a first-principles physical
  Lagrangian).
- Does not resolve the general real-spectrum mechanism question left
  open by C101-C105 (this is a relaxation test, not a proof).
- Does not test k=2,3 levels or the 3-level block-tridiagonal case
  (C103) with the r-coupled alternative -- scoped to the same minimal
  2-level test as C101 for direct comparability (Cheapest Differentiating
  Test Protocol).
- Does not change N_gen=3's CONDITIONAL status.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## kill_criterion

If P3 is FALSE (Clifford-coupled B_1^Gamma gives a clearly non-real
spectrum, max|Im| not small), this establishes that "r-untouched" WAS
load-bearing for the real-spectrum property specifically -- a genuinely
informative negative result, sharpening (not just leaving open) the "r's
role" question. If P0 or P1 fails, this specific construction is
ill-defined and the round reports a construction-error null result
instead of a physics finding.
