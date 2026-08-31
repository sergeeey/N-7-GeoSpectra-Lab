# C115 decision -- third data point confirms an asymmetric rule fits
j2=3/2 and j2=2 exactly, but a competing symmetric rule fits j2=1
equally well -- two admissible readings, not one rule with exceptions.
Decisive next test identified, not yet run (see C116).

**Verdict:** `ASYMMETRIC_RULE_CONFIRMED_AT_J2_GEQ_3HALVES__TWO_REGIME_READING_ADMISSIBLE__J2_3_KILL_TEST_NAMED`
**Status:** RESOLVED as a confirmed, precisely-characterized (and
independently re-verified) pattern; WEAKENED on the single-rule framing
per FL Step 8a skeptic review; decisive follow-up named, not attempted
this round

---

## Summary

Builds a third matched-diagonal cell, `(j1=2,j2=2)`, reusing C114's own
`run_cell` unmodified. P0 (full sum real) and P1 (component norms
identical) both confirmed. P2 (asymmetric rule test) found a striking
result: the rule **"removal stays real iff `|a|=j2` AND `|b|<j2`"**
(first noticed while re-checking C114's own pearl-registry entry against
this round's raw data, not planned in claim.md in this exact form) fits
`(2,2)` PERFECTLY (25/25) and, on re-verification, fits `(3/2,3/2)`
PERFECTLY too (16/16) -- the SAME rule that C114's own decision.md
described as "fails on (1,1)'s own (0,1) case" (true, 6/9 there).

## FL Step 8a skeptic review (context-blind) -- verified the arithmetic,
found a genuine competing explanation

Given this result revises C114's own "mechanism remains genuinely open"
framing substantially, ran a context-blind artifact review before
finalizing.

**Arithmetic independently re-verified, confirmed exact:** 6/9 (j2=1),
16/16 (j2=3/2), 25/25 (j2=2) -- skeptic did the j2=2 count by hand,
matches.

**Confirmed load-bearing:** the `|b|<j2` clause is not redundant --
`|a|=j2` ALONE (dropping the `|b|<j2` condition) mispredicts the 4
"double-corner" cases at both j2=3/2 and j2=2 (e.g. `(2,2)`, `(2,-2)`,
`(-2,2)`, `(-2,-2)` all break, but "`|a|=j2` alone" would predict they
stay real). The `a` vs `b` asymmetry is also real, not a framing
artifact -- directly checked `(2,1)` vs `(1,2)` etc., genuinely
different outcomes.

**Confound checked and ruled out:** is the j2=1 "exception" actually an
`a=0`-specific anomaly (untestable at half-integer `j2`, where `a=0`
never occurs) rather than a genuine j2=1 regime effect? NO -- at j2=2,
`a=0` IS tested (5 entries) and ALL 5 break reality, matching the
asymmetric rule's own prediction there. `a=0` does not universally
preserve reality; it only does so at j2=1 specifically.

**Genuine competing explanation found, not previously considered:** at
j2=1 ALONE, a DIFFERENT, SYMMETRIC rule -- **"stays real iff `a=0` OR
`b=0`"** -- fits PERFECTLY, 9/9 (better than the asymmetric rule's 6/9
there). This rule fails at j2=3/2 (predicts all-break, since no zero
magnetic value exists at half-integer spin, but 4 entries stay real)
and at j2=2 (predicts `(2,1)` breaks; it does not). **This means the
data admits TWO readings, not one:** (a) one asymmetric rule governs
everywhere, with j2=1 as a 3-case exception; or (b) j2=1 is governed by
a genuinely DIFFERENT (symmetric) rule, and the asymmetric rule only
applies to `j2>=3/2` -- a regime shift, not an exception count. This
round's own data cannot distinguish these two readings.

**Diagnostic-power gap identified:** the "16/16 + 25/25" framing
overstates independent confirmation -- at j2=3/2, only 4 of the 16
entries (the double-corner cases) are actually diagnostic for the
`|b|<j2` clause specifically (the other 12 are `|a|<j2` cases the
simpler symmetric-vs-asymmetric distinction doesn't even test); the
asymmetric rule's load-bearing evidence is dominated by the single j2=2
cell.

## What this genuinely establishes

1. **The asymmetric rule is real, not a coincidence** -- confirmed
   independently by the skeptic's own hand-count, and the `|b|<j2`
   clause is demonstrably load-bearing (not reducible to `|a|=j2` alone)
   at both j2=3/2 and j2=2.
2. **The j2=1 "exception" is genuinely j2-specific** (not an
   untestable-elsewhere `a=0` artifact) -- but whether it reflects a
   true regime shift (a different rule for the smallest tested spin) or
   a boundary exception to one universal rule is NOT resolved by the
   three cells tested so far.
3. **A decisive next test is named, not run:** `j2=3` (`k_source=6`,
   `target_level=12`, 49 components) re-tests `a=0` with `|b|<j2`
   resolution (`|b| in {0,1,2}`, unlike j2=1's `|b| in {0}` only) --
   directly separating the two readings. If all `(0,*)` removals at
   j2=3 break reality (matching the asymmetric rule), the "j2=1 is a
   low-spin regime" reading strengthens. If any `(0,*)` at j2=3 stays
   real, the claim needs rebuilding around `a=0` structure specifically,
   not around `|a|=j2`.

## Kill Analysis

**Not killed:** C114's own full-sum results at `(1,1)` and `(3/2,3/2)`
-- reused unmodified.

**Killed:** the earlier (C114 pearl-registry) framing that BOTH tested
candidate rules were simply "refuted" -- the asymmetric rule is, on
this round's fuller re-check, NOT refuted; it is confirmed at 2 of 3
cells and precisely characterized at the third. The pearl-registry
entry undersold this rule by testing it only against `(1,1)` before
this round supplied the `(3/2,3/2)`/`(2,2)` re-confirmation.

**What survives as the live open question:** one-rule-with-an-exception
vs. two-regime reading -- named, not resolved, `j2=3` identified as the
decisive test.

## What this cannot show

- Does not resolve the one-rule-vs-two-regime ambiguity -- explicitly
  requires the named `j2=3` test, not attempted in this round (see
  `experiments/20260830-c116-*` if built as a follow-up).
- Does not report `max|Im|` MAGNITUDES as a structured finding beyond
  the binary breaks/does-not-break classification, even though the
  underlying data contains them -- flagged by the skeptic as a real,
  not attempted, gap.
- Does not change `N_gen=3`'s CONDITIONAL status; this lineage stays
  entirely internal to S3, touches neither S6 nor triality.
- Does not solicit Tom Lawrence's Part 5.

## Verification

- `ruff check experiments/20260830-c115-third-cell-2-2-mechanism-test/`
  -- clean.
- FL Step 8a skeptic pass: arithmetic independently re-verified by hand
  for the full j2=2 cell (25/25) -- matches. Found the genuine
  alternative-rule reading; this decision.md incorporates it rather
  than presenting the single-rule framing as settled.
- Reused C114's own `run_cell`, `build_M_ab_general`, `magnetic_labels`,
  `certified_L_R` unmodified via direct import (not copy-pasted).
