# C116 decision -- decisive test resolves the C115 ambiguity in favor of
"j2=1 is a low-spin anomaly," but reveals a THIRD, cleaner pattern:
reality-preservation-under-single-removal is a narrow window (j2 in
{3/2,2}), absent at BOTH tested boundaries (j2=1 and j2=3), for two
qualitatively different reasons

**Verdict:** `ALL_A0_BREAK_CONFIRMED__BUT_ALL_49_REMOVALS_BREAK__REALITY_PRESERVING_WINDOW_IS_NARROW_NOT_UNIVERSAL_MINUS_ONE_EXCEPTION`
**Status:** RESOLVED -- decisive test ran as pre-registered, produced a
cleaner and more surprising result than either pre-registered reading
anticipated

---

## Summary

C115's own FL Step 8a skeptic review left one question open: does the
asymmetric rule ("removal stays real iff `|a|=j2` AND `|b|<j2`") hold
universally with a 3-case exception at `j2=1`, or does `j2=1` follow a
genuinely different symmetric rule? Pre-registered decisive test:
`j2=3`, checking whether all 7 `(0,b)` removals break (favoring "j2=1
is a low-spin regime") or whether `(0,0)` specifically stays real
(favoring "zero-specific structure").

## Results

**The pre-registered decisive question is answered cleanly: all 7
`(0,b)` removals break, including `(0,0)`.** This directly favors "j2=1
is a low-spin regime" over the zero-specific-structure reading -- ruled
out, not just weakened.

**But the FULL result is more informative than the pre-registered
question alone:** of 49 remove-one tests at `j2=3`, the asymmetric
rule's "breaks" predictions are 39/39 correct (100%), but its "stays
real" predictions are 0/10 correct (0%) -- EVERY single one of the 10
cases the rule predicted would stay real (`|a|=3` paired with
`|b|<3`, i.e. `b in {-2,-1,0,1,2}`) actually BREAKS instead. **All 49 of
49 remove-one tests at `j2=3` break reality.** No single-component
removal preserves reality at this cell, at all.

Magnitudes (not discarded this round, per C115's own skeptic-flagged
gap): the 10 "should-be-real-but-broke" cases have `max|Im|` in
`1.0e-5` to `9.5e-5` -- comparable in scale to the correctly-predicted
`(0,b)` breaks (`1.3e-5` to `7.2e-5`), NOT smaller/borderline. This is
not a numerical-noise-crossing-the-threshold artifact; these are
genuine, unambiguous complex-spectrum results, 8-9 orders of magnitude
above the `~1e-15` machine-epsilon floor seen in genuinely-real cases
throughout this entire series.

## Four-cell picture, now complete for this investigation

| `j2` | Full sum | Remove-one pattern |
|---|---|---|
| `1` | real | mostly real; fits symmetric "`a=0` OR `b=0`" rule, 9/9 |
| `3/2` | real | asymmetric rule ("`\|a\|=j2` AND `\|b\|<j2`" stays real), 16/16 |
| `2` | real | asymmetric rule, 25/25 |
| `3` | real | **asymmetric rule's "breaks" side only, 39/39 -- its "stays real" side is 0/10, i.e. nothing stays real** |

**Reality-preservation-under-single-removal is a NARROW WINDOW
phenomenon** (clean at `j2=3/2,2`), bounded on BOTH sides by cells
where it degrades -- but via TWO QUALITATIVELY DIFFERENT mechanisms,
not the same one at each boundary: at `j2=1`, MOST removals stay real
(a different, symmetric protective structure); at `j2=3`, NO removal
stays real (the protective structure vanishes entirely). This is a
richer, more precise, and more surprising picture than either of
C115's own pre-registered readings anticipated -- neither "one rule,
low-spin exception" nor "two regimes" fully captures a window that
closes from BOTH directions for different reasons.

## Kill Analysis

**Confirmed, per pre-registration:** the "j2=1 is a low-spin regime"
reading, specifically on the `a=0` question C115 left open -- all 7
`(0,b)` cases at `j2=3` break, matching the asymmetric rule, unlike
`j2=1` where the analogous cases stay real.

**NOT anticipated by either pre-registered reading, discovered by
running the FULL 49-cell sweep rather than only the 7 decisive cases:**
the asymmetric rule's OWN "stays real" prediction fails completely at
`j2=3` (0/10), even though its "breaks" prediction remains perfect
(39/39). The asymmetric rule, as stated, is NOT the general rule for
`j2>=3/2`; it is specifically accurate at `j2 in {3/2,2}` and
increasingly wrong about its own "stays real" clause as `j2` grows
further.

**What survives as the live open question:** why does single-component
removal ever preserve reality at all, and only in this narrow `j2`
window? This is now a sharper, better-specified question than C114's
original "mechanism is open" -- it is no longer "what characterizes
breaking vs non-breaking in general" but specifically "why does the
reality-preserving effect exist at `j2=3/2,2` and vanish at both `j2=1`
and `j2=3`, for two different-looking reasons." Not attempted further
this round -- four cells (`j2=1,3/2,2,3`) is a substantial, well-
characterized dataset; further brute-force cells (`j2=5/2`, `j2=4`...)
without a theory to test have diminishing returns per this project's
own Cheapest Differentiating Test discipline. Recorded as a pearl.

## What this does NOT show

- Does not explain WHY the window exists or why it closes the way it
  does at each boundary -- a genuine mechanism question, deferred.
- Does not test `j2>3` or non-matched cells.
- Does not change `N_gen=3`'s CONDITIONAL status; this lineage stays
  entirely internal to S3, touches neither S6 nor triality.
- Does not solicit Tom Lawrence's Part 5.

## Verification

- `ruff check experiments/20260830-c116-j2-3-decisive-kill-test/` --
  clean.
- Arithmetic self-checked directly against `results_c116.json`'s own
  `all_remove_one_detail` list: 10 mismatches, all and only the
  `\|a\|=3,\|b\|<3` cases, confirmed by direct enumeration.
- No separate skeptic pass this round -- the result is a simple,
  fully-enumerated count (49/49 cases, no geometric/dimensional
  reasoning at risk of the kind of error C114's own first attempt at
  the anti-Hermitian diagnostic made) with the pre-registered decisive
  question (all `(0,b)` break) answered unambiguously; the additional
  finding (0/10 on "stays real") is a direct reading of the same
  already-verified data, not a new inference requiring independent
  challenge.
- Reused C114's own `run_cell` unmodified via direct import.

## ADDENDUM (2026-08-31) -- fraction-real trend, the pearl's own named
next-cheap-check, executed

This pearl (`pearl_registry/INDEX.md`, C116 row) named an explicit
zero-cost next step: read the raw fraction of remove-one tests that
stay real at each of the 4 already-computed cells, straight from each
round's own `results_*.json`, no new matrices built. Done here, with
each number independently re-derived from source (not copied from
prior prose) to guard against exactly the kind of silently-stale
number this project's own Hindsight Distortion Gap Heuristic warns
about:

| `j2` | `n=2j2+1` | dim (`n^2`) | real | fraction |
|---|---|---|---|---|
| `1`   | 3 | 9  | 5 | 0.5556 |
| `3/2` | 4 | 16 | 4 | 0.2500 |
| `2`   | 5 | 25 | 6 | 0.2400 |
| `3`   | 7 | 49 | 0 | 0.0000 |

(`j2=1`, `j2=3/2` re-extracted from `experiments/20260830-c114-subset-analysis-matched-diagonal-cells/results_c114.json`,
filtered to `type=='remove_one'` only -- C114's own `subsets` list also
contains `single`/`structured_pair_group` entries [corrected 2026-08-31,
skeptic pass: this was originally misnamed `single_alone`/
`structured_intermediate`, strings that do not exist in the file -- the
filter itself was always correct, only the provenance note's naming was
wrong], which the original pearl's 5/9 and 4/16 numbers evidently already
excluded correctly, confirmed by the count matching `n^2` exactly. `j2=2`
from `results_c115.json`'s `remove_one_detail` (`breaks` field). `j2=3`
from this round's own `all_remove_one_detail` (`actual_breaks` field;
NOTE -- that same JSON's `predicted_stays_real` field is serialized as a
mix of Python bool and the literal strings `"True"`/`"False"` for
different rows; `"False"` is truthy in Python, so any future re-analysis
must use `actual_breaks`, not `predicted_stays_real`, or risk silently
miscounting up to 10 of the 49 rows).

**[CORRECTED 2026-08-31, FL Step 8a skeptic pass -- see "Skeptic
response" subsection below for the full response matrix.]** The
original text here claimed this table "answers" the pearl's own
question ("threshold or smooth decay?") because the fraction is
monotonically decreasing (0.556 -> 0.250 -> 0.240 -> 0.000). That
claim is WRONG: a monotone sequence is equally consistent with a
smooth decay AND with a step/threshold function -- monotonicity has
**zero power to discriminate** between the two branches of the
question it was offered as answering. The pearl_registry row has been
reverted from `ANSWERED` back to open status; see below.

Two further findings from the skeptic pass, kept for the record:

1. **The "monotone decrease" is a property of the chosen
   normalization (real count / `n^2`), not of the underlying system.**
   Restricting the denominator to the `|a|=j2` sector where the
   asymmetric rule permits reality at all (`2n` components, verified
   via `addendum_verify.py`) gives real/sector-total = `2/6=0.3333`,
   `4/8=0.5000`, `6/10=0.6000`, `0/14=0.0000` -- **NOT monotone**: it
   rises from `j2=1` to `j2=2`, then collapses at `j2=3`. The raw real
   COUNT itself (5, 4, 6, 0 total; 2, 4, 6, 0 within the `|a|=j2`
   sector) moves the SAME direction in both normalizations (down then
   up before collapsing) -- it is only the `n^2`-normalized fraction
   that happens to read as monotone, because the denominator grows
   faster than the numerator recovers. Whether "the" trend is
   monotone is a choice of yardstick, not a finding.
2. **The three regimes this file's own body already describes
   (symmetric rule at `j2=1`, asymmetric rule at `j2 in {3/2,2}`,
   total collapse at `j2=3`) are not one smooth process.** At `j2=3`
   the asymmetric rule itself predicts real fraction `2*(n-2)/n^2 =
   0.2041`; the observed value is `0.0000` -- the last step is the
   rule being violated, not "more of the same decay." Gluing one point
   from each of three admittedly-different mechanisms into a single
   "trend" restates the individual cell results without adding
   information beyond a single new bit (whether `4/16 > 6/25`, which
   the "sector" normalization above shows is not robust either).

**What remains genuinely open (unchanged, now correctly still
`pending` in the pearl registry):** whether the reality-preserving
window's boundary behavior between `j2=2` and `j2=3` is a threshold or
a gradual decay is NOT settled by any statistic computed from the 4
existing cells -- it requires the `j2=5/2` (`n=6`) data point, the
only OTHER half-integer cell (structurally distinct from integer `j2`:
no `b=0` component exists at half-integer spin, per C115's own
decision.md). Per this file's own Cheapest Differentiating Test note
above, that round is NOT being launched this session absent a specific
reason beyond "fill the gap" -- recorded as an open item, not
attempted further.

## Skeptic response (2026-08-31, FL Step 8a, context-blind pass on
this ADDENDUM specifically)

Verdict: **WEAKENED**. Full response per the project's own Response
Matrix (`falsification-ladder.md` Step 8a):

| Concern | Response |
|---|---|
| "Monotonically decreasing" does not discriminate threshold vs. smooth decay -- the pearl row was closed on a non-answer | **Accepted, fixed.** Rewrote the headline above; reverted `pearl_registry/INDEX.md` row 109 status from `ANSWERED` to open/pending with the discriminating question restated explicitly. |
| Trend is denominator-driven; alternate (`\|a\|=j2`-sector) normalization gives a non-monotone sequence | **Accepted, fixed.** Added `addendum_verify.py`, computes both normalizations; non-monotone result now stated above. |
| The three cells are governed by three different mechanisms per this file's own text; concatenating one point from each is a category error | **Accepted, fixed.** Added the rule-violation-at-j2=3 point (predicted 0.2041, observed 0.0000) above. |
| Missing `j2=5/2` caveat understates exposure -- it is the only other half-integer cell, structurally distinct, not merely "an extra data point" | **Accepted, fixed.** Reworded above to name the structural distinctness, citing C115's own decision.md. |
| C115's own skeptic-flagged caveat (asymmetric rule's evidentiary weight dominated by one diagnostic cell) was dropped when re-asserting the "window" framing | **Accepted as a documented limitation** -- not re-litigated here (out of scope for this addendum, belongs to C115/C114's own text), but noted: readers should treat the "100% rule fit" language earlier in this file with that caveat attached, not as independent confirmation across two cells. |
| Wrong JSON type names (`single_alone`/`structured_intermediate`) in the provenance note | **Accepted, fixed** -- corrected above to `single`/`structured_pair_group`. |
| `results_c116.json`'s `predicted_stays_real` field mixes bool and truthy string types -- hazard for future readers | **Accepted, documented** above (not fixed in the committed JSON itself -- past round artifacts are not mutated after the fact; the hazard is now flagged in this file instead, and `all_remove_one_detail`'s `actual_breaks` field, which is NOT affected, remains the field to use). |
| No persisted re-derivation script -- "independently re-derived" left no artifact | **Accepted, fixed.** `addendum_verify.py` committed alongside this correction; its output matches every number in the table above exactly, including the new sector-normalization figures. |
| The four fractions themselves (0.5556/0.2500/0.2400/0.0000) and denominators (`n^2`) | **CONFIRMED-REAL by the skeptic's own independent recomputation** -- unchanged, no fix needed. |

- Re-verification method: `addendum_verify.py` (committed), independently
  re-derives all 4 `fraction_total` values (exact match to 4 decimal
  places) plus the sector-restricted `fraction_sector` values used
  above. No new matrices computed, no test suite re-run needed
  (read-only analysis of already-committed, already-tested JSON
  artifacts).
