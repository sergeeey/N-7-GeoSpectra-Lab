# Round122 — Decision

**Date:** 2026-07-17
**Verdict:** `RECOMPOSITION HOLDS FOR CLAIMS EXAMINED, SCOPE CORRECTED,
ONE LEDGER GAP FOUND AND FIXED` (narrower than first drafted — corrected
by skeptic review)

**Go/no-go:** `N_gen=3` remains `CONDITIONAL` — no change to the headline
claim's status. This round's own first draft overreached in stating the
scope of what was checked; corrected. One genuine ledger-accuracy gap
(a premise cited in `DERIVATION_GRAPH.yaml`'s own inference text but
missing from its formal premises list and from `CLAIM_LEDGER.yaml`
entirely) was found and fixed directly, not deferred.

## Single skeptic pass — three findings

Ran the mandatory context-asymmetric skeptic review (claim.md + the audit
document only, no reasoning chain) per `falsification-ladder.md` Step 8a.
Verdict: `WEAKENED`. Three findings, all fixed:

1. **Claim count was wrong.** First draft said "20-claim ledger" — the
   ledger actually has 22 entries (confirmed by direct read), and its own
   pre-existing header note ("~16 entries") was also stale. Fixed both.
2. **"No silent-assumption smuggling found anywhere in the 20-claim
   ledger" overreached.** Skeptic found this round's own analysis (§2-4 of
   the audit document) substantively re-examines only `C19`, `C20`,
   `C_G67C3` against `D2`, plus a one-line pass on `D1`/`D3` — the
   remaining ~18 claims were confirmed only as "untouched by rounds
   111-121," a narrower claim than "checked and found clean." Corrected
   the verdict's scope throughout, not just in one place.
3. **A genuine silent premise found in `D2` itself, missed by this
   round's own first draft.** `DERIVATION_GRAPH.yaml`'s `D2` inference
   text cites `sign(ind)=+1 (proved, G74B)` as part of the counting
   argument — but this fact had no dedicated `CLAIM_LEDGER.yaml` entry and
   was absent from `D2`'s own `premises` list. This is precisely the
   "individually-verified pieces reassemble with a hidden additional
   ingredient" failure mode the Recomposition Gate exists to catch — and
   this round's own recomposition audit missed it on the first pass.

Skeptic also confirmed two things held up: the `preprint.tex` L3b
staleness claim (verified directly, `SO(4)` does not appear anywhere in
lines 1256-1296), and the core `C19`/`C20` "not needed as `D2` premises"
conclusion — though it sharpened the `C20` reasoning: `OB11` isn't
"unrelated" to `D2`, it's already absorbed by `C_G67C3`'s own `OPEN`
status (which `D2` already carries).

## Fix applied this round (not deferred)

Added `C21_G74B_CHIRALITY_SIGN` to `CLAIM_LEDGER.yaml` (citing
`experiments/20260621-g74b-chirality-from-index/decision.md:8-40`,
depends_on `[C1, C2]`) and added it to `D2`'s `premises` list in
`DERIVATION_GRAPH.yaml`. This is a ledger-accuracy fix, in scope for this
round per the established pattern from rounds 119/120 — unlike the
`preprint.tex` punch-list items, which are genuinely deferred to item 8
(preprint rewrite), this is not a public-facing edit and carries no
"one round, one deliverable" concern.

## What was actually verified this round

- Read `CLAIM_LEDGER.yaml` in full (all entries, confirmed count of 22 —
  corrected once more after an initial "21" miscount, verified directly
  with `grep -c "^  - id:" CLAIM_LEDGER.yaml`).
- Read `DERIVATION_GRAPH.yaml`'s all 3 derivation chains in full.
- Read `preprint.tex` lines 1256-1296 (Open Problems L3a/L3b) in full,
  confirmed no mention of `SO(4)×SO(4)` or round119's gate application.
- Read `experiments/20260621-g74b-chirality-from-index/decision.md` to
  confirm the exact content of the newly-added `C21` entry, not asserted
  from memory.

## Kill Analysis

- **What this kills:** the first draft's overreached "no smuggling
  anywhere in the ledger" verdict, and the ledger's own pre-existing
  miscounted header note.
- **What this does NOT kill:** `N_gen=3`'s `CONDITIONAL` status (unchanged,
  correctly so), or any of the 21 pre-existing claims' own individual
  verdicts (none were found wrong, only `D2`'s premises list was found
  incomplete).
- **What survives as a scoped next step:** the ~18 untouched claims remain
  formally un-re-audited for recomposition consistency this round — a
  future full pass could check each one explicitly, though nothing found
  this round suggests urgency.

## Relaxation Map

| Option | What it would require |
|---|---|
| Full per-claim recomposition audit of all 22 entries | Trace each claim's `depends_on` against every derivation chain it touches, not just `D2` — a larger undertaking than this round's scope, not attempted |
| Execute the item-8 punch list (`preprint.tex` L3b update, `gates_tracker.md` extension) | The user's own next named step — not this round's job |

## What this does NOT mean

1. Does NOT change `N_gen=3`'s status, `lambda=FREE_COUPLING_PARAMETER`,
   or `safe_for_runtime=False`.
2. Does NOT edit `preprint.tex` — deferred to item 8.
3. Does NOT claim all 22 ledger entries were re-audited for recomposition
   — see corrected scope above.

## Standing lesson (fifth consecutive round, 118-122)

**A recomposition audit is itself subject to the same overclaim risk it
exists to catch in others.** This round's own first draft both (a)
overstated its own coverage ("anywhere in the ledger" when only 3 claims
were traced) and (b) missed exactly the kind of hidden-premise gap
(`sign(ind)=+1`/`C21`) the Recomposition Gate is designed to surface —
caught only by the mandatory skeptic pass, not by the audit's own design.
Fifth consecutive round where skeptic review corrected a first-draft
consolidation claim — the pattern now spans positive findings (118),
verdict labels (119), factual scope claims (120), a cautionary near-miss
(121), and now a meta-level audit auditing itself (122).

## Check (reproduces the verification)

```
grep -c "^  - id:" CLAIM_LEDGER.yaml
```
Expect: 22 (confirms the corrected count, including the newly-added `C21`).
```
grep -n "SO(4)" preprint.tex | sed -n '1,5p'
```
Expect: no hits within the L3a/L3b line range (1256-1296), confirming the
staleness finding.
