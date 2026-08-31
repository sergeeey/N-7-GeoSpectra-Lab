# C117 claim -- j2=5/2, the missing data point between j2=2 and j2=3

## Question type (EstimandOps L0)
**Descriptive.** This is a direct computation of a spectral property
(does removing one component of an already-built coupling operator
leave the combined spectrum exactly real?) at a specific parameter
value. No causal or predictive claim is being made.

## Background

C116's own FL Step 8a skeptic pass (2026-08-31, on the C116 addendum)
found that the "fraction of real removals" trend across the 4 already-
computed matched-diagonal cells (j2=1, 3/2, 2, 3) does NOT discriminate
between "the reality-preserving window closes gradually" and "it closes
as a cliff" -- monotonicity is compatible with both. The skeptic named
the specific gap: j2=5/2 (n=2*j2+1=6) is the only untested cell between
j2=2 (n=5, window still clean, asymmetric rule fits 25/25) and j2=3
(n=7, window fully collapsed, asymmetric rule's "stays real" side is
0/10). j2=5/2 is also structurally distinct from j2=3 in one respect
worth flagging: both are... no, j2=5/2 is the SECOND half-integer cell
tested (after j2=3/2), not a third integer cell -- it has no b=0
component (per C115's own decision.md), same structural family as
j2=3/2, not j2=3.

The user explicitly asked to resolve this open question this round.

## Falsifiable claim

At the matched-diagonal cell j1=j2=5/2 (k_source=5, target_level=10,
n=6, 36 remove-one tests), the asymmetric rule ("removal stays real iff
|a|=j2 AND |b|<j2") predicts exactly 8 of the 36 remove-one tests stay
real (the `|a|=5/2` sector, `2n=12` components, of which the rule
permits reality for `b` in `{-3/2,-1/2,1/2,3/2}`, i.e. 2*4=8; predicted
`|b|=5/2` corner cases, 4 of them, break like every other tested corner
case in this series).

## Three pre-registered readings, before running

| Reading | Sector-real count (of 8 rule-predicted) | Interpretation |
|---|---|---|
| **RULE_HOLDS** | 8/8 (or close, e.g. >=6) [CORRECTED post-hoc, FL Step 8a skeptic pass on the result: this table entry contradicted the kill criterion immediately below, which is all-or-nothing. The table's "or close" was written without accounting for the exact a<->-a, b<->-b symmetry this construction has throughout the whole series -- that symmetry partitions the 8 predicted-real cases into exactly 2 orbits of size 4 each, so the ONLY attainable counts are {0,4,8}, not any integer 0-8. "close, e.g. >=6" was not a reachable outcome at all. The kill criterion (all-or-nothing) is the one actually applied below; this row is left uncorrected in its original wording as the historical record, not silently rewritten.] | Window extends cleanly through j2=5/2; collapse is a genuine cliff specific to the j2=2->j2=3 step (n=5->n=7), i.e. the LAST tested step, not a gradual erosion |
| **PARTIAL** | strictly between 0 and 8 (e.g. 1-7) | Genuine gradual transition -- the rule degrades smoothly, not abruptly |
| **FULL_COLLAPSE** | 0/8 (matches j2=3's own 0/10 pattern) | The window closes one step earlier than it appeared to -- already gone by n=6, and j2=2 (n=5) is the LAST cell where it holds, meaning C116's apparent "cliff at n=7" was actually a cliff at n=6 that C116 could not see because n=6 was untested |

**Kill criterion for RULE_HOLDS:** any single one of the 8 rule-predicted
"stays real" cases actually breaking (max|Im| > 1e-9, matching this
project's own established threshold throughout C108-C116) falsifies
RULE_HOLDS outright -- the same all-or-nothing standard C116 itself
applied to its own decisive test.

**Kill criterion for FULL_COLLAPSE:** any single one of the 8 staying
real falsifies FULL_COLLAPSE.

## Why this statistic actually discriminates (responding directly to
the skeptic's own core finding on the addendum)

Unlike "the fraction is monotonically decreasing" (compatible with
every possible shape of decay, including a cliff), the sector-real
COUNT at j2=5/2 is read directly against the three readings above and
can only match ONE of them (assuming a clean outcome; a genuinely mixed
result, e.g. 3/8 or 5/8, still directly falsifies both RULE_HOLDS and
FULL_COLLAPSE and confirms PARTIAL without ambiguity). This is the
fix the skeptic's response-matrix entry required before this session
would trust a "resolved" verdict on this specific question.

## What this does NOT show

- Does not by itself explain WHY any of the three outcomes holds --
  mechanism remains a separate, harder question even after this cell
  is characterized.
- Does not test j2=4 or any cell beyond this specific gap.
- Does not change N_gen=3's CONDITIONAL status; stays entirely internal
  to S3, touches neither S6 nor triality.
- Does not solicit Tom Lawrence's Part 5.

## Verification plan

- Reuse C114's `run_cell` unmodified via direct import (same method as
  C115, C116 -- already validated 3x).
- `ruff check` clean.
- Full pytest suite before commit.
- FL Step 8a skeptic pass on the result (context-blind), given this
  question was specifically escalated after the addendum's skeptic
  pass found a real gap -- the same discipline should close it.
