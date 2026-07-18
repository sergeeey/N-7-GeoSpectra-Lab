# Round100 (E1) — Decision

**Date:** 2026-07-17
**Verdict:** `CONSISTENT__NO_CONTRADICTION__ONE_SHARPENED_SUMMARY_SIGNAL`

## Fact table (all reused by citation; none re-derived this round)

| # | Fact | Source |
|---|---|---|
| 1 | `t=0`↔`(1,2)` (`SU(2)_L` singlet, `SU(2)_R` doublet), unconditional | round83/E16/round92 Part 1 |
| 2 | `t=1`↔`(2,1)` (`SU(2)_L` doublet, `SU(2)_R` singlet), under `c0=-2` | CONVENTION_TABLE.md row 5-6 |
| 3 | Both endpoints `SU(3)_c` SINGLET | round92 Section 3a |
| 4 | `K_3 ≡ T_{3R}` (same operator) | round93 |
| 5 | `B-L=0` for twisted S⁶ kernel | round94 |
| 6 | `Y=T_{3R}+(B-L)/2 = T_{3R}` (since B-L=0) | round96, derived from #4+#5 |
| 7 | `[SU(3)_c]^3`: both endpoints already 0 alone — no forcing | round92 |
| 8 | Mixed-`U(1)_Y` conditions (3 of them): all 0, both endpoints alone AND union — no forcing | round96 |
| 9 | Witten `SU(2)` parity: `t=0` alone gives 3 `SU(2)_R` doublets (ODD); `t=1` alone gives 3 `SU(2)_L` doublets (ODD); union does not change either parity (each endpoint total singlet under the OTHER factor) | round91/92 |
| 10 | Cubic `SU(4)_{PS}³` anomaly: `A(4,2,1)=+2`, `A(4̄,1,2)=-2`, sum=0 only together — genuine forcing pattern, IF `SU(4)` gauged | round90 |
| 11 | `SU(4)`-charged content is exhaustive (no missed field) | round97 |
| 12 | `SU(4)` NOT geometrically realized as isometry of `Iso(S³×S⁶)` | gate G97 |
| 13 | Classical curvature `R^t=t(t-1)[[X,Y],Z]`: flat at `t=0,1`, curved at `t=1/2` — double-well shape available IF an action contains this term (NOT shown to) | round99, `WEAKENED` per skeptic |
| 14 | Lemma L5 (S⁶-only asymmetry) does not conflict with S³-side content, contingent on H1c staying open | round95 |
| 15 | Friedrich-Ivanov "at most one torsion connection" applicability to `S³`/n=3 | round98, `<unknown>` |

## Consistency check

**No direct contradiction found.** Facts #7-9 (all established, non-
forcing anomaly/parity channels) are mutually consistent with each other
(different anomaly TYPES — perturbative cubic vs. global mod-2 — can
independently show non-forcing without conflicting). Fact #10 (the one
GENUINE forcing signal) is consistently BLOCKED by fact #12, not
contradicted by it — a conditional ("IF `SU(4)` gauged, THEN forcing"),
not a clash. Fact #14's contingency on H1c is explicitly conditional, not
a present contradiction.

## New signal from the combination (not visible from any single round)

Reading facts #7, #8, #9, #10, #12 TOGETHER (not visible from any single
round read alone): **every perturbative and global anomaly channel this
project can currently COMPUTE (within the geometrically-realized `G_eff`)
has now been checked and shows no forcing** (#7, #8, #9) — and **the
single channel that WOULD force coexistence (#10) is the only one that
requires an ingredient this project has explicitly shown is absent (#12)**.
This means the Pati-Salam/anomaly research line (rounds 90-97) has reached
a clean, sharp, EXHAUSTIVE negative result for its own internal method: no
further anomaly-channel search within `G_eff` remains to be tried — the
entire remaining hope for THIS route is a single, precisely-named open
question (does an alternative geometric realization of `SU(4)` exist,
gate G97), not a diffuse "maybe check more anomalies" uncertainty. This
sharpening (from "promising but incomplete" to "exhausted except for one
named structural gate") is itself the useful product of this round — it
was not stated this precisely by any single prior round.

## Applying the pre-registered criteria (claim.md Section 2)

**CONSISTENT, with one sharpened summary signal** (a hybrid of the first
two options — no contradiction, and the "new signal" is a sharpening of
scope, not a new physics mechanism).

## Kill Analysis

- **What this kills:** any lingering framing of the Pati-Salam/anomaly
  route as "still has several untested anomaly channels" — it does not;
  the route is exhausted except for gate G97 specifically.
- **What survives:** gate G97 (alternative `SU(4)` geometric realization)
  as the sole remaining structural question for this specific route; the
  curvature/modulus route (round99, `WEAKENED`, B1 unattempted); the
  Friedrich-Ivanov no-go (round98, `<unknown>`).

## What this does NOT mean

Does not affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`,
`safe_for_runtime=False`. Does not modify `preprint.tex`. No new
computation performed — pure synthesis of already tool-verified facts,
each individually reused by citation.
