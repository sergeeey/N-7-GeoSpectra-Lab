# C108 claim -- does D_PW built from C104's summed multiplication operator
M_k^sum (genuine 4-fold mixing, not C100-C103/C105/C106's single-component
embedding) still have an exactly real spectrum?

## L0 gate (EstimandOps)

**Question type:** Descriptive (does a specific alternative construction
have property X: exactly real spectrum?). Not causal, not predictive.

## Background -- why this round exists

This returns to the pure C90-C106 numerical-exploration track (per user
request, after the OB1-bridge detour C107 and a documentation-only check
both concluded). C104's own decision.md explicitly named this test as a
natural follow-up, never attempted: does D_PW built from `M_k^sum`
(summed over all 4 `(a,b)` CG components, C104's own "genuine mixing"
construction -- exactly `4*dim_k^2` nonzero entries at every k, vs.
C100-C103/C105's single-component `M_k` with exactly `dim_k^2` nonzero
entries) still give an exactly real coupled spectrum?

## Counterfactual Frame (exploratory round -- disclosed up front)

Cheap interactive scratch exploration (sympy/numpy) was run FIRST,
matching this project's own established discipline. It found:

1. `M_1^sum` is entrywise real (as expected, same as every other
   CG-derived operator tested so far in this series).
2. At k=1->2: the coupled D_PW spectrum is **NOT** exactly real --
   `max|Im(eig)| = 0.106`, clearly nonzero, not floating-point noise.
   This is the FIRST candidate coupling in the entire C101-C106 series
   to break the real-spectrum property.
3. At k=2->3, k=3->4, k=4->5: the coupled spectrum **IS** exactly real
   (`max|Im| < 1e-14`, machine epsilon) -- the property holds at every
   higher level tested.

The formal script below independently re-derives all of the above from
scratch, matching this project's own disclosed-scratch-then-formalize
discipline.

## Entity / falsifiable predicate / measurable outcome (Zero-Signal Gate)

- **Entity:** the 2-level D_PW construction (C101's own minimal setup,
  extended to k,k+1 for k=1,2,3,4), with the off-diagonal coupling
  block set to `B_k^sum := M_k^sum (x) I_r` (C104's summed-component
  operator, r-untouched as in C101-C103/C105 for direct comparability).
- **Falsifiable predicate:** whether `max|Im(eig(D_PW))|` is below the
  established `1e-6` threshold (exactly real) or clearly above it, at
  each of k=1,2,3,4.
- **Measurable outcome:** `np.linalg.eigvals` (certified convention),
  compared against the same `1e-6` threshold used throughout C101-C106.

## Predictions (stated before the formal script runs, though after the
disclosed scratch exploration above)

| # | Prediction |
|---|---|
| P0 | `M_1^sum` is entrywise real (reuse-sanity). |
| P1 | `M_1^sum` genuinely differs from the single-component `M_1` used in C100-C103/C105/C106. |
| P2 | k=1->2: `max\|Im\| > 1e-3` (clearly, unambiguously non-real). |
| P3 | k=2->3: `max\|Im\| < 1e-6` (exactly real). |
| P4 | k=3->4: `max\|Im\| < 1e-6` (exactly real, replication at a second higher level). |
| P5 | k=4->5: `max\|Im\| < 1e-6` (exactly real, replication at a third higher level). |

## What this cannot show

- Does not explain WHY k=1 specifically is anomalous (an open question,
  flagged as a pearl, not resolved this round).
- Does not test the r-coupled (Clifford-type) variant of `M_k^sum`
  combined with mixing -- only the r-untouched version, for direct
  comparability with C101-C103/C105.
- Does not test the 3-level block-tridiagonal construction (C103) with
  `M_k^sum`.
- Does not change N_gen=3's CONDITIONAL status.
- Does not touch OB1 or the C107 bridge-attempt line at all -- this is a
  return to the pure mathematical exploration track.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## kill_criterion

If P2 and P3-P5 both hold as predicted (break at k=1, hold at k>=2),
this establishes the FIRST known coupling in this series with a genuine,
level-dependent real-spectrum failure -- a real, informative, non-generic
finding (not a uniform "mixing breaks reality" claim, which P3-P5 would
directly falsify if reality held everywhere, nor a uniform "reality is
completely robust" claim, which P2 already falsifies at k=1). If instead
reality holds uniformly at all k, or breaks uniformly at all k, this
round reports that instead, which would also be a real finding just a
different, simpler one than what scratch exploration suggested.
