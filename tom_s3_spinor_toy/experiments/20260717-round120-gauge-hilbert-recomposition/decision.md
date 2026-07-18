# Round120 — Decision

**Date:** 2026-07-17
**Verdict:** `REGISTRY_STALENESS_CONFIRMED_AND_FIXED` (narrower than first
draft — two findings corrected by skeptic review, both accepted, neither
dismissed)

**Go/no-go:** `docs/gates_tracker.md`'s G10 row genuinely lacked the G97
caveat and has been fixed. Two claims in the first draft were themselves
imprecise, caught by the mandatory context-asymmetric skeptic review, and
corrected inline in `GAUGE_HILBERT_RECOMPOSITION.md` (marked, not silently
rewritten).

## Single skeptic pass — two findings, both fixed

Ran the mandatory skeptic review (claim.md + the audit document only, no
reasoning chain) per `falsification-ladder.md` Step 8a. Verdict:
`WEAKENED`. Two concrete corrections:

1. **§3's "round102 subtlety resolved" was too strong.** First draft
   treated `preprint.tex:464` (confirms the round metric is used) as fully
   closing round102's flagged concern. Skeptic found this resolves only the
   metric-identity sub-question ("not necessarily round" → it is round);
   it does not settle whether `SO(7)` (bare metric) or `G_2` (metric+`J`)
   is the physically correct ambient group to check isometry against — a
   genuinely separate, unaddressed framing question. Consequential impact
   is low (`G97`'s `SO(7)` result implies the `G_2` case a fortiori by
   dimension count, `14<21`), but the claim was corrected to reflect this
   precisely rather than overstate a full resolution.
2. **§4's "tracker stops at G1-G30ish" was factually wrong.** Verified
   directly (`grep -n "^| G9[0-9]\|^| G10[0-9]\|Last updated"
   docs/gates_tracker.md`): the tracker was kept current through `G106`
   (2026-07-06, header "Last updated: 2026-07-07") — includes `G90`, `G91`,
   `G100`, `G102`-`G106`. The accurate finding: `G97` and its round102/108/
   109 corroborations, all dated 2026-07-17 (this session, after the
   tracker's last update), simply haven't been folded back yet — an
   ordinary same-day lag, not a stopped-early tracker. Corrected inline.

Skeptic separately confirmed (b) the `G_2`-as-stabilizer-of-`J` framing in
§2's table is correct (checked specifically because it was flagged as a
possible conflation risk) — no correction needed there — and (c) that the
core registry-staleness finding itself (G10's row genuinely lacks the `G97`
caveat, verified by reading the full 149-line tracker file) is accurate.

## What was actually verified this round

- Re-read `preprint.tex` lines 180-300, 415-436, 460-470 in full.
- Re-read `docs/gates_tracker.md` in full (149 lines, not just the grepped
  row) — confirmed via `grep -n "^| G9[0-9]\|^| G10[0-9]\|Last updated"`
  that coverage extends to G106, correcting the first-draft claim.
- Re-read round102's own "Assumptions carried, unresolved" section in full
  to ground the §3 correction in its exact wording, not a paraphrase.

## Kill Analysis

- **What this kills:** the first draft's two overstatements (full
  resolution of round102's metric subtlety; tracker "stops early").
- **What this does NOT kill:** the core finding (G10's tracker row lacked
  the G97 caveat, now fixed), or any physics conclusion (SU(3)_c×SU(2)_L×
  SU(2)_R from isometry, U(1)_{B-L} open, SU(4) blocked all unchanged).
- **What survives as a scoped next step:** folding G97/round102/108/109
  into `docs/gates_tracker.md` as proper rows (not just a caveat on G10),
  and regenerating the `.xlsx`/`.pdf` exports — both flagged, neither
  attempted here.

## Relaxation Map

| Option | What it would require |
|---|---|
| Add G97/round102/108/109 as proper tracker rows | Mechanical, low-risk — same format as existing rows, not attempted here to keep this round scoped |
| Regenerate `.xlsx`/`.pdf` exports | Run `python scripts/export_results.py --all` — not attempted, flagged as a follow-up mechanical step |
| Resolve the SO(7)-vs-G_2 ambient-group framing question properly | Would require deciding, with an explicit argument, which group is "the" physically relevant one to check any future candidate gauge structure against — not attempted here, low urgency given the dimension-count argument already covers current needs |

## What this does NOT mean

1. Does NOT change any physics conclusion — see §5 of the main document.
2. Does NOT claim `preprint.tex` itself is inconsistent — the staleness is
   between the older tracker and the newer, already-correct preprint text.
3. Does NOT fully resolve round102's ambient-group framing question — only
   its narrower metric-identity component.
4. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.

## Standing lesson (consistent with round118/119's pattern)

Third consecutive round (118, 119, 120) where a first-draft consolidation
claim was found by skeptic review to be more confident than the cited
source actually supports — twice on a verdict label (round119: `PARTIAL`
too strong; round120: "resolved" too strong), once on a supporting factual
claim about scope (round120: "tracker stops early," factually checkable and
wrong). The common thread: consolidation/audit rounds carry their own
overclaim risk distinct from new-physics rounds — summarizing existing work
accurately is not automatically lower-risk than deriving new results, and
needs the same skeptic discipline.

## Check (reproduces the verification)

```
grep -n "^| G9[0-9]\|^| G10[0-9]\|Last updated" docs/gates_tracker.md
```
Expect: rows through G106, "Last updated: 2026-07-07" — confirming the
tracker's actual coverage, not the first draft's "stops at G30" claim.
