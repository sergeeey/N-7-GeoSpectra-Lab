# C116 claim -- the decisive j2=3 test named by C115's own FL Step 8a
skeptic review: does the asymmetric rule's own prediction for a=0
removals hold at an integer j2 where |b|<j2 has real resolution
(unlike j2=1, where |b|<j2 only ever means b=0)?

## L0 gate (EstimandOps)

**Question type:** Descriptive.

## Background

C115's decision.md left one question explicitly open, per its own FL
Step 8a skeptic review: does the asymmetric rule ("(a,b)-removal stays
real iff `|a|=j2` AND `|b|<j2`") hold universally with a `j2=1`
exception (3 cases, all `a=0`), or does `j2=1` follow a genuinely
DIFFERENT symmetric rule ("stays real iff `a=0` OR `b=0`", which fits
`j2=1` perfectly, 9/9, better than the asymmetric rule's 6/9 there)?
The skeptic named the decisive test: `j2=3` re-tests `a=0` removals
WITH `|b|<j2` resolution (`|b| in {0,1,2}`, unlike `j2=1`'s `|b| in
{0}` only) -- something no prior cell could test, since `j2=1/2` and
`j2=3/2` have no `a=0` at all, and `j2=1`'s own `a=0` case only ever
pairs with `b in {-1,0,1}`, none of which distinguish "b extreme" from
"b non-extreme except zero" the way `j2=3`'s richer `b` range does.

## Pre-registered prediction (stated exactly as C115's own pearl-registry
entry named it, BEFORE running anything -- this is the actual point of
this round, not restated after seeing data)

**The asymmetric rule predicts:** ALL 7 removals of the form `(0,b)`
(`b` in `{-3,-2,-1,0,1,2,3}`) at `j2=3` should BREAK reality (since
`a=0 != j2=3`, the rule's "stays real" condition `|a|=j2` is never met
for these).

**The two-regime reading predicts:** if `j2=1`'s symmetric rule
("`a=0` OR `b=0`") reflects something genuinely tied to `a` or `b`
being EXACTLY ZERO (not just "small"), then specifically `(0,0)` at
`j2=3` might behave differently from the other 6 `(0,b)` cases (`b!=0`)
-- a prediction the asymmetric-rule-only framing does not make, stated
here explicitly so a `(0,0)`-specific deviation (if found) is read as
supporting evidence for a zero-specific effect, not noise.

## Entity / falsifiable predicate / measurable outcome

- **Entity:** cell `(j1=3,j2=3)`, `k_source=6`, `target_level=12`, 49
  components (`a,b` each ranging over `{-3,-2,-1,0,1,2,3}`).
- **Falsifiable predicate:** do all 7 `(0,b)` removals break reality
  (asymmetric-rule / "j2=1 is a low-spin regime" reading), or does at
  least one stay real (regime-shift / "a=0 has its own structure"
  reading needs rebuilding)?
- **Measurable outcome:** `max|Im(eig(D_PW))|` per removal, same
  `1e-9` threshold as every prior round in this series.

## Scope (large-cell tier, matching C114's own `(3/2,3/2)` and C115's
`(2,2)` precedent)

Remove-one (49 tests) and single-alone (49 tests) only -- no structured-
intermediate sampling at this size, per the established Cheapest
Differentiating Test scoping. The single-alone tests are included for
completeness (matching every prior cell) even though they are not the
decisive test themselves.

**Also addresses the skeptic's other named gap:** report `max|Im|`
MAGNITUDES for every removal, not just the binary breaks/does-not-break
classification (C115's decision.md explicitly flagged this omission).

## What this cannot show

- Does not test `j2>3` or non-matched (`j1!=j2`) cells.
- Does not derive a group-theoretic mechanism even if the asymmetric
  rule's prediction holds cleanly -- confirms/refutes the pattern, not
  its cause.
- Does not change `N_gen=3`'s CONDITIONAL status; this lineage stays
  entirely internal to S3, touches neither S6 nor triality.
- Does not solicit Tom Lawrence's Part 5.

## kill_criterion

If ALL 7 `(0,b)` removals break reality: the asymmetric rule's own
prediction is confirmed at a THIRD integer spin with real `|b|<j2`
resolution -- strong support for "j2=1 is a low-spin regime," report
as such, do not overclaim full universality (still only 4 cells tested
total, `j2=1,3/2,2,3`). If ANY `(0,b)` stays real: report exactly which
one(s) -- if specifically `(0,0)`, this directly supports the
"zero-specific structure" reading pre-registered above; if some other
`(0,b!=0)` stays real, neither pre-registered reading anticipated that,
report it as a genuinely new, unexplained data point.
