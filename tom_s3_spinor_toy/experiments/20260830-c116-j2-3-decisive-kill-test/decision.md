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
