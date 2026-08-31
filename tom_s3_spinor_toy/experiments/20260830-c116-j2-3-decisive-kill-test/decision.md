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

(`j2=1`, `j2=3/2` re-extracted from `../20260830-c114-.../results_c114.json`,
filtered to `type=='remove_one'` only -- C114's own `subsets` list also
contains `single_alone`/`structured_intermediate` entries, which the
original pearl's 5/9 and 4/16 numbers evidently already excluded
correctly, confirmed by the count matching `n^2` exactly. `j2=2` from
`results_c115.json`'s `remove_one_detail` (`breaks` field). `j2=3` from
this round's own `all_remove_one_detail` (`actual_breaks` field).)

**Answer to the pearl's own question ("threshold or smooth decay?"):
the FRACTION is monotonically decreasing** across all 4 points --
0.556 -> 0.250 -> 0.240 -> 0.000, with a near-plateau between `j2=3/2`
and `j2=2` (0.250 vs 0.240) rather than a jump. This does NOT contradict
this file's own "narrow window" language above -- that language was
about a different quantity (how well the asymmetric RULE's predictions
match outcomes: 100% at `j2 in {3/2,2}`, worse elsewhere), not the raw
magnitude of the real fraction. Both are true at once: the rule
describes the mechanism cleanly only in the plateau region, while the
raw fraction of real cases simply decays throughout, with no rise
anywhere in the tested range.

**What this does NOT settle:** the raw REAL COUNT itself (5, 4, 6, 0)
is not monotonic in `j2` -- it dips at `j2=3/2` before ticking back up
at `j2=2`, then collapsing at `j2=3`. And the 4 tested cells skip
`j2=5/2` (`n=6`) entirely, so whether the fraction's descent from 0.24
to 0.00 is gradual through that gap or a cliff exactly at the
`j2=2 -> j2=3` step cannot be read off the existing data -- the
apparent "smoothness" of the fraction trend is partly an artifact of
only 4 unevenly-spaced sample points. Per this file's own Cheapest
Differentiating Test note above, this gap is NOT being closed with a
new brute-force `j2=5/2` round absent a specific reason to test it --
recorded here as a named, honest limit on the trend claim, not
pursued further this session.
- Re-verification method: direct `python -c` read of each round's own
  `results_*.json`, cross-checked against `n^2` dimension formula as an
  internal consistency check (all 4 counts matched exactly). No new
  matrices computed, no test suite re-run needed (read-only analysis
  of already-committed, already-tested JSON artifacts).
