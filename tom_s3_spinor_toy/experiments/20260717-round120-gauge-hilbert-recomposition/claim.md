# Round120 — Claim

**Gauge/Hilbert/Triality closure program, item 5 (frame-to-gauge audit).**
Per the user's own 8-step sequence, this is the fourth deliverable file:
`GAUGE_HILBERT_RECOMPOSITION.md`.

## L0 gate (EstimandOps)

**Question type: Descriptive.** For each gauge factor this project claims
(`SU(2)_L`, `SU(2)_R`, `SU(3)_c`, `U(1)_{B-L}`, full Pati-Salam `SU(4)`),
what specific geometric mechanism produces it — full metric isometry,
holonomy/structure-group of a compatible-but-narrower additional structure,
or neither (blocked/postulated) — and is this consistent between
`preprint.tex`'s current (careful, post-G97) text and the internal
experiment registry (`docs/gates_tracker.md`, dated 2026-06-17/18, predating
G97)? This is a consistency/consolidation question, not a new physics claim.

## Falsifiable claim

`docs/gates_tracker.md` (which its own header calls "Source of truth") has a
G10 entry ("S⁶ spin connection → SO(6) gauge field... so(6)≅su(4); 15
generators") dated 2026-06-17, describing a genuine 15-generator SO(6)/SU(4)
gauge structure with no caveat — while `preprint.tex`'s later, more careful
text (lines 279-287, 425-436, informed by gate G97, dated within this
session's round90-102 work) explicitly states only `SU(3)×SU(2)_L×SU(2)_R`
(not the full `SO(6)`/`SU(4)`) is realized as an isometry, and `U(1)_{B-L}`/
full Pati-Salam completion is explicitly NOT an isometry. If true, this is a
genuine staleness gap in the project's own designated source-of-truth
tracker, of the same kind already fixed for `OB4`/`C_G67C3_THIRD_CHANNEL`
in round119 — not a new physics finding, a registry-accuracy one.

## Pre-registered check (before any interpretation)

1. Re-read `preprint.tex` lines 258-298 (gauge structure section) and
   425-436 (G97 caveat) in full to confirm the current, careful framing.
2. Re-read `docs/gates_tracker.md`'s G10/G10b rows and header in full to
   confirm the staleness claim, not assume it from a partial grep.
3. Check whether round102's own flagged "which metric — round or
   nearly-Kähler" subtlety (assumption #2, `20260717-round102-*/decision.md`)
   is actually already resolved by `preprint.tex:464` ("On S⁶ with the round
   metric, the spinor bundle splits...") — i.e. confirm the SAME round
   metric is used throughout (both for the isometry-group computation and
   for the G2-compatible almost-complex structure), not a separate,
   unaddressed NK-only metric.
4. Check `CLAIM_LEDGER.yaml` and `OPEN_BLOCKERS.md` for whether G10's status
   or round102's flagged subtlety are already tracked elsewhere (avoid
   duplicating an existing entry).

## Kill criterion (pre-registered)

- If `docs/gates_tracker.md`'s G10 entry, read in its original full context
  (not just the row grepped), already carries an adequate caveat elsewhere
  in the same document — the staleness claim is wrong, no registry fix
  needed.
- If round102's "which metric" subtlety is NOT actually resolved by
  `preprint.tex:464` (e.g. if that line describes a different, narrower
  claim than what round102's concern was about) — the subtlety remains open
  and should be tracked as its own `OPEN_BLOCKERS.md` entry, not marked
  resolved.
- If `preprint.tex`'s own gauge-structure section is found to be internally
  inconsistent (not just inconsistent with the older tracker) — this would
  be a more serious finding requiring escalation, not a routine registry fix.

## What this does NOT mean (pre-registered)

1. Does NOT change any physics conclusion — `SU(3)_c×SU(2)_L×SU(2)_R` from
   the isometry group, `U(1)_{B-L}` open, `SU(4)` blocked (G97) all remain
   exactly as established.
2. Does NOT re-derive G6/G9/G10/G69/G97/round102's own computations — all
   cited, none recomputed.
3. Does NOT affect `N_gen=3`'s conditional status, `lambda=FREE_COUPLING_
   PARAMETER`, or `safe_for_runtime=False`.
4. Does NOT regenerate `docs/exports/gates_tracker.xlsx`/`.pdf` — flagged as
   a mechanical follow-up if the markdown source changes, not attempted here.
