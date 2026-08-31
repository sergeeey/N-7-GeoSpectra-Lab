# C118 claim -- eigenvalue-density alternative to the "asymmetric rule"

## Question type (EstimandOps L0)
**Descriptive.** Direct computation and comparison of two numeric
quantities (minimum eigenvalue gap; a perturbation-norm proxy) across
5 already-characterized cells. No causal or predictive claim.

## Background

C117's own FL Step 8a skeptic pass named an untested, cheaper
alternative to the "asymmetric rule" pattern tested since C114: rather
than a representation-theoretic mechanism, the observed pattern
(narrow reality-preservation at j2 in {3/2,2}, collapse elsewhere)
could be a spectral-density artifact -- total operator dimension grows
with j2 (68/130/212/314/436 across the 5 tested cells [CORRECTED
2026-08-31, FL Step 8a skeptic pass: original list wrongly gave
242/338 for j2=5/2,3 -- those are D2's own sub-block dimensions, not
the D_PW totals; totals confirmed against C118's own printed output]), a denser
spectrum makes a fixed-scale perturbation (removing one component)
more likely to collide two real eigenvalues into a complex-conjugate
pair, with no group-theoretic rule required at all.

User explicitly asked to run this check.

## Falsifiable claim

At each of the 5 already-tested matched-diagonal cells (j2 = 1, 3/2,
2, 5/2, 3), compute:
- `min_gap`: the minimum pairwise distance between eigenvalues of the
  FULL-SUM `D_PW` (all components included; already confirmed real at
  every cell, P0 in C114-C117).
- `component_norm`: the Frobenius norm of a single (a,b) component
  (already confirmed identical within each cell -- P1 in C114-C117),
  used as a rough perturbation-scale proxy (not a rigorous operator-norm
  perturbation bound -- an honest limitation, stated up front, not
  discovered after the fact).

**Pre-registered prediction under the density hypothesis:** the ratio
`min_gap / component_norm` should be LARGER at the two cells where
single-component removal preserves reality (j2=3/2, j2=2) than at the
three where it does not (j2=1, j2=5/2, j2=3) -- crudely, "removal only
breaks reality when the perturbation scale is comparable to or larger
than the smallest gap it could close."

**Kill criterion:** if `min_gap / component_norm` does NOT separate
the two groups {3/2, 2} vs {1, 5/2, 3} in the predicted direction (i.e.
if the ratio is smaller, not larger, at 3/2 and 2 than at 1, 5/2, 3;
or if there is no clean separation at all, e.g. j2=1's ratio sits
between the other two groups rather than clearly outside them), the
density hypothesis is NOT supported by this crude proxy -- it may
still be true under a more rigorous operator-norm treatment, but this
cheap check would not have found it.

## Explicit, named limitation (stated BEFORE running, not after)

This is a CRUDE proxy, not rigorous degenerate-perturbation-theory. A
real treatment would need the operator 2-norm of the specific
`(a,b)`-component being removed (which can differ from the Frobenius
norm, though P1 showed Frobenius norms are identical within a cell --
operator norms were never checked and could differ) and would need to
identify WHICH pair of eigenvalues actually collides for each removal,
not just the global minimum gap. This check is a first-pass filter:
if it does NOT show the predicted separation, that is meaningful
evidence against the simplest version of the density hypothesis; if it
DOES show separation, that is suggestive but not proof, and the
rigorous version remains a separate, larger undertaking not attempted
here.

## What this does NOT show

- Does not by itself prove or disprove the density hypothesis --
  a crude proxy, explicitly scoped above.
- Does not explain the specific asymmetric-rule pattern (which
  components break vs. stay real within a cell) even if density
  explains the overall collapse trend.
- Does not change N_gen=3's CONDITIONAL status; stays entirely
  internal to S3, touches neither S6 nor triality.
- Does not solicit Tom Lawrence's Part 5.

## Verification plan

- Reuse C114's module-level building blocks (`build_M_ab_general`,
  `magnetic_labels`, `magnetic_range`) via direct import -- does NOT
  reuse `run_cell` itself (which does not expose eigenvalues or full
  D_PW, only `max|Im|` per subset); duplicates `dbar_full`'s few lines
  since it is a closure inside `run_cell`, not module-level.
- `ruff check` clean.
- Full pytest suite before commit.
- FL Step 8a skeptic pass on the result, same discipline as C115-C117.

## SUBSTRATE FAILURE (v1, 2026-08-31) -- test could not honestly
discriminate anything; per this project's own FL Substrate Gate, this
is NOT recorded as evidence against the density hypothesis

`c118_eigengap_check.py`'s first version measured the GLOBAL minimum
gap across the ENTIRE eigenvalue spectrum of each cell's full-sum
`D_PW`. Result: `min_gap = 0.0` EXACTLY at all 5 cells -- not "small",
literally zero. Diagnosed before drawing any conclusion: `D1`/`D2` are
each built as `kron(I_{dim_q}, dbar)` (`dbar_full`'s own construction,
identical across C114-C117), which creates `dim_q`-fold EXACT
degeneracy by construction, independent of any physics -- confirmed
directly (level=2: `dbar` spectrum `[-2,-2,-2,-2,4,4]` -> `D1` spectrum
12x/6x degenerate after the kron). This structural degeneracy
dominates any global-minimum-gap statistic and has nothing to do with
the specific eigenvalue pair that actually collides when one component
is removed. **The v1 script was deleted before committing** (per this
project's own Substrate Gate hard rule: a broken test is never left
standing as if it were a negative result) -- not preserved as
`c118_eigengap_check.py` history, since it produced zero informative
output at any stage, unlike C114's own honestly-abandoned diagnostic
attempt (which is preserved as a named, in-code comment).

## v2 REDESIGN (2026-08-31, same day, user explicitly requested the
proper version) -- LOCAL collision gap, not global spectrum minimum

**Corrected falsifiable claim:** for a FIXED, cell-independent
component choice -- the corner `(j2,j2)`, confirmed to break reality
at every one of the 5 tested cells (C114: `(1,1)`; C115/C116/C117: the
asymmetric rule's own "breaks" prediction for `|b|=j2` is confirmed
100% correct at every cell for this component) -- sweep a continuous
removal fraction `s in [0,1]`: `D_PW(s) = D_PW_full - s * Delta_H`,
where `Delta_H` is the Hermitian block perturbation corresponding to
removing an `s`-fraction of the corner component. At `s=0`,
`D_PW(0)=D_PW_full` is confirmed real (P0, all 5 cells). At `s=1`, the
corner component is known to break reality (confirmed above). Locate
`s*` -- the critical fraction where `max|Im|` first exceeds the
project's own `1e-9` threshold along this sweep.

**Pre-registered prediction under the density hypothesis:** `s*`
should trend DOWNWARD as cell dimension grows (68 -> 130 -> 212 -> 314
-> 436 across `j2 = 1, 3/2, 2, 5/2, 3`) -- i.e. a smaller fraction of
the SAME relative perturbation is needed to trigger collision in a
larger, denser system. This tests the density hypothesis in the exact
scope this claim.md already limited it to: explaining the OVERALL
COLLAPSE TREND (why removal eventually always breaks reality as cells
grow), NOT the within-cell question of which specific components break
vs. stay real at a GIVEN cell size (explicitly out of scope, stated
above before v1 was even run).

**Kill criterion:** if `s*` does NOT trend downward monotonically (or
close to it -- one reversal tolerated given only 5 data points) with
cell dimension, the density hypothesis is not supported by this local,
corrected test either.

**Honest scope, stated before running:** this still does not test
WITHIN-cell variation (why some components at j2=3/2,2 stay real while
the corner never does) -- a genuinely different, harder question,
deferred exactly as before.
