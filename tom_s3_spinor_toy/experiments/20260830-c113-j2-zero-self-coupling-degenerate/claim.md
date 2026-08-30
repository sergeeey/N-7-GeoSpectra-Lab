# C113 claim -- can j2=0 (trivial/singlet auxiliary) break the C112
target_level=2 confound? Algebraic argument first, then confirmed
numerically.

## L0 gate (EstimandOps)

**Question type:** Descriptive.

## Background

C112's own artifact review (skeptic, context-blind) found that
`target_level=2` is reached by exactly one cell in the tested `(j1,j2)`
grid -- the already-known C108 anchor -- so "`j1=j2` does not reproduce
the anomaly" could not be disentangled from "`target_level=2`
specifically is the trigger." The decision.md's own "what survives"
section named `j2=0` (a trivial/singlet auxiliary representation) as the
one way to reach `target_level=2` with `j1 != j2` -- but flagged it as
"itself a degenerate self-coupling case ... not a like-for-like control,"
not attempted in C112 due to time/scope pressure. User asked to attempt
it directly this round.

## Entity / falsifiable predicate / measurable outcome (Zero-Signal Gate)

- **Entity:** the `j2=0` construction: `j_target = j1+0 = j1`, so
  `target_level = 2*j1 = k_source` -- source and target level COINCIDE,
  meaning `D1 = D2 = dbar_full(k_source)` (the same certified operator on
  both diagonal blocks). The single `(a,b)=(0,0)` component gives
  `CG(j1,m,0,0,j1,m) = 1` for every `m` (coupling to a singlet is the
  identity map) -- so the off-diagonal block is exactly `t*I` (scaled
  identity), not a genuine mixing operator.
- **Falsifiable predicate:** does this `[[D, t*I],[t*I, D]]` construction
  ever have `max|Im|>0`, for any tested `k_source` or coupling `t`?
- **Measurable outcome:** `max|Im(eig([[D,tI],[tI,D]]))|` via
  `np.linalg.eigvals`.

## Algebraic argument, stated BEFORE computing (this is the actual
content of this round -- the computation is a confirmation, not a
discovery)

For ANY square matrix `D` (Hermitian or not) and ANY scalar `t`, the
block matrix `[[D, tI],[tI, D]]` is similar, via the fixed change of
basis `u=x+y, v=x-y` (independent of `D`), to the block-diagonal matrix
`diag(D+tI, D-tI)`. This is pure linear algebra -- it does not use any
property of `D` beyond being square of the right size, and holds for
every `k_source` and every `t` simultaneously, not case-by-case.

**Consequence:** since every `dbar_full(k)` in this project has an
EXACTLY real spectrum (Meier's own certified construction, re-confirmed
this round to be exactly `0.0`, not merely small, for k=1,2,3 -- see
Results), `D+tI` and `D-tI` both have exactly real spectra for any real
`t` (shifting a real number by a real number stays real). **The
`j2=0` construction is therefore ALGEBRAICALLY INCAPABLE of ever
breaking reality, for any `k_source`, at any coupling strength -- not a
close call, not level-dependent, a general fact about this specific
block shape.**

## Predictions (stated before the script runs, though the algebra above
already fixes the answer -- P1 is a confirmation, not a genuine test of
an uncertain outcome, stated honestly)

| # | Prediction |
|---|---|
| P0 | Each individual `dbar_full(k)` (k=1,2,3) has EXACTLY real spectrum (`max\|Im\|=0.0`, not just below a numerical threshold) -- re-confirms the base certified fact this whole construction rests on. |
| P1 | The `j2=0` self-coupled `[[D,tI],[tI,D]]` construction has `max\|Im\|=0.0` (or machine epsilon) for k=1,2,3 at `t=1` -- confirms the algebraic argument, not an open empirical question. |
| P2 | The computed spectrum matches `eig(D+tI) UNION eig(D-tI)` exactly (sorted comparison) -- directly verifies the similarity-transform argument, not just its real/complex conclusion. |

## What this genuinely establishes

If P0-P2 hold: **`j2=0` cannot be used to break the C112 confound, for a
provable structural reason, not merely "we tried it and it didn't work."**
This closes off that specific route rigorously -- the `target_level=2`
vs `j1=j2` confound remains genuinely unbroken by any construction in
the "positive-spin-or-singlet auxiliary, stretched-top-state" family
this project has built. A genuine disambiguation would need either a
non-stretched-top `j_target` convention (abandoning adjacency-adjacent
conventions entirely -- a much bigger design change) or accepting the
confound as a structural feature of this construction family that cannot
be cheaply resolved.

## What this cannot show

- Does not test whether a DIFFERENT `j_target` convention (not
  `j1+j2`, e.g. taking a non-stretched CG channel) could reach
  `target_level=2` non-degenerately with `j1 != j2` -- a materially
  bigger design change, not attempted here.
- Does not change `N_gen=3`'s CONDITIONAL status; this lineage stays
  entirely internal to S3 (see `OPEN_BLOCKERS.md` OB11's correction box).
- Does not solicit Tom Lawrence's Part 5.

## kill_criterion

If P0 or P1 fails to be EXACTLY zero (not just below `1e-9`), the
algebraic argument above has an error -- stop, do not trust the general
claim, investigate the specific matrix that broke it. If P2 fails
(spectrum doesn't match the `D+-t` prediction), the block-similarity
argument itself needs re-derivation, not just this instance.
