# Global Recomposition Audit (Round122, 2026-07-17)

**Gauge/Hilbert/Triality closure program, item 7** — the last audit before
item 8 (preprint rewrite, only after this verdict). Applies this project's
own `falsification-ladder.md` Recomposition Gate to `CLAIM_LEDGER.yaml`
(22 entries as of this round — corrected below, first draft miscounted)
and `DERIVATION_GRAPH.yaml`'s 3 chains, given everything established
through round121.

**Scope correction, made by mandatory skeptic review of this round itself
[skeptic correction]:** first draft claimed "no silent-assumption
smuggling found anywhere in the 20-claim ledger." Skeptic found this
overreaches — §2-4 below substantively re-examine only `C19`, `C20`,
`C_G67C3` against `D2`, plus a one-line "unaffected" pass on `D1`/`D3`;
the other ~18 claims were not individually re-audited this round (they
were simply unaffected by rounds 111-121's own work, which is a weaker,
narrower claim than "checked and found clean"). **The accurate scope: for
the claims actually touched this session, recomposition holds; the
remainder were not re-examined here, not confirmed clean.** Corrected
throughout below, not silently smoothed over.

**A genuine gap the skeptic pass itself caught, and this round then
fixed (not deferred):** `DERIVATION_GRAPH.yaml`'s own `D2` inference text
cited `sign(ind)=+1 (proved, G74B)` as part of the counting argument, but
this fact had no dedicated entry in `CLAIM_LEDGER.yaml` and was missing
from `D2`'s own `premises` list — exactly the "individually-verified
pieces reassemble with a hidden additional ingredient" failure mode the
Recomposition Gate exists to catch, and which this round's own first draft
did not catch on its own. Fixed this round: added `C21_G74B_CHIRALITY_
SIGN` to `CLAIM_LEDGER.yaml` and to `D2`'s premises list (ledger-accuracy
fix, in scope for this round per the established pattern — unlike the
`preprint.tex` punch-list items below, which are deferred to item 8).

**What this file is:** a final consistency check, not new physics. It asks
one question of the whole ledger: do the individually-verified pieces still
combine to license exactly what's currently claimed — or does recomposing
them silently add an assumption, or silently drop a caveat, that no single
piece actually licenses?

## 1. D1 — KT-8 blocks N_gen=3 as physical (re-checked, unaffected)

Premises `C1` (index=1), `C2` (kernel dim=1), `C3` (KT-8 no zero mode) are
all unaffected by rounds 111-121's work (none of that work touched the S³
factor's zero-mode question). **Verdict: unchanged, still the standing
blocking finding.**

## 2. D2 — the N_gen=3 headline chain (re-checked, the main question)

**Premises:** `C1` (`ind=1`), `C2` (`dim ker=1`), `C_G67C3` (3 channels
physically distinct), with `C3` as the load-bearing negative premise.

**The recomposition question this round actually investigates:** two new
claims were added to the ledger this session — `C19_SPINOR_DECOMPOSITION_
AUDIT` and `C20_MATTER_GENERATION_FACTORIZATION_THREE_WAY`. Do either need
to be added to `D2`'s premise list, or are they legitimately parallel
investigations?

**Traced explicitly, claim by claim:**

- **`C19`** re-verifies the 32-state spinor decomposition (16 particle +
  16 CPT-conjugate), the chirality result (conditional on `C3`, already a
  `D2`/`D1` dependency), and the triality-channel independence claim (`G73`,
  already `C_G67C3`'s own evidence). It adds ONE genuinely new item: `OB10`,
  a gap in the geometric spinor bundle's own reality/Majorana (KO-dimension)
  condition. **This is a question about the bundle's algebraic type — not
  a premise the zero-mode COUNTING argument depends on.** `D2`'s counting
  doesn't use or require a resolved reality condition; it uses index,
  kernel dimension, and channel count. **Verdict: `C19`/`OB10` correctly
  NOT added to `D2` — no change needed.**
- **`C20`** tests the user's own proposed `H_matter⊗H_generation`
  hypothesis, put forward to EXPLAIN already-established facts (the
  `SU(4)`-singlet property, `B-L=0`) — it is not itself a premise `D2`'s
  counting argument was ever built from. The STRONG reading is `BLOCKED`
  (by `C7`, already a `D3`-chain fact, unrelated to `D2`); the WEAK
  reading's sufficiency (`OB11`, no Dirac-operator channel-mixing) is
  open. **Sharper reasoning than "unrelated" [skeptic correction]:** `OB11`
  is not a free-standing new question — it is testing content that
  already lives INSIDE `C_G67C3`'s own statement ("3 geometrically
  distinct channels all INDEPENDENTLY REALIZED as physical Dirac zero-mode
  channels" already implicitly requires no channel-mixing). So `OB11`
  doesn't need to be added as a NEW `D2` premise for a more precise reason
  than "it's unrelated" — it is already subsumed by `C_G67C3`'s own
  `OPEN` status, which `D2` already carries as a premise. **Verdict:
  `C20`/`OB11` correctly NOT added to `D2` as a separate premise — but
  because it is absorbed by `C_G67C3`, not because it is unrelated to it.**

**`C_G67C3` itself — the one premise this round's own work (`round119`)
directly touched:** its status update (`GATE 1 OF 7 DONE / GATES 2-6 OPEN`,
replacing a flatter "not internally derivable" framing) does NOT change
`D2`'s conclusion — `C_G67C3` was `OPEN` before and remains `OPEN` now,
just with a more precise, evidence-richer description of WHY. `D2`'s
`CONDITIONAL` status and its two named open premises (`C_G67C3`, `C3`)
are exactly as accurate now as before this session's rounds.

**Recomposition verdict for D2: `CONDITIONAL`, unchanged, for the three
claims actually re-examined this round (`C19`, `C20`, `C_G67C3`) — they
recompose to `D2` without introducing a new premise `D2` needs (with one
fix applied: `C21`/`sign(ind)=+1`, previously cited in `D2`'s own inference
text without a ledger entry, added this round — see above).** This is a
narrower, more defensible finding than "the whole ledger is clean": five
rounds of substantial new work (118-121) genuinely advanced the project's
understanding without changing the headline claim's logical status for the
claims those rounds actually touched — exactly what honest incremental
research on an open conditional claim should look like. The other ~18
claims in the ledger were not individually re-audited this round; they are
unaffected by rounds 111-121 because that work never touched them, not
because this round re-verified each one clean.

## 3. D3 — Pati-Salam parent-action search (re-checked, unaffected)

Untouched by rounds 118-121 (which concern triality/matter-generation
questions downstream of `D3`'s own conclusion, not `D3`'s own premises
`C5`-`C11`). **Verdict: unchanged, `SUPPORTED` within the product-manifold
framework, `OPEN` beyond it via `C11`.**

## 4. Public-wording staleness found (understatement, not overclaim)

`preprint.tex`'s Open Problems L3b entry (lines ~1271-1296) reads, in its
current form, "all internal geometric avenues ruled out... Confirming this
physical input is the remaining open question, to be addressed in
collaboration with T. Lawrence" — accurately describing the state as of
gate `G102` (2026-07-05), but **not mentioning** the `SO(4)×SO(4)`
block-chirality candidate found later the same session
(`L3B_SPIN8_INTERFACE_SPEC.md`, 2026-07-15) — the first candidate in the
project's own investigation to algebraically distinguish all three
triality channels (not just `v` from `{s,c}`) — nor round119's own gate
application (`TRIALITY_DISTINGUISHABILITY_GATE.md`, `GATE 1 OF 7 DONE`).

**This is an understatement, not an overclaim** — the public text is
MORE conservative than the project's own internal state warrants, the
opposite risk from what this project's audit discipline usually screens
for. Still worth fixing: a reader of `preprint.tex` alone would not know
this partial advance exists.

**Not fixed this round** — per this project's own established practice
(round53's deferred editorial update; "one round, one deliverable"),
this is queued as a precise, actionable item for item 8 (preprint
rewrite), not applied pre-emptively here.

## 5. Punch list for item 8 (preprint rewrite) — precise, not applied here

1. **`preprint.tex` L3b entry (~line 1271-1296):** add a paragraph after
   the existing `G102` discussion, citing `L3B_SPIN8_INTERFACE_SPEC.md`'s
   `SO(4)×SO(4)` candidate and round119's `GATE 1 OF 7 DONE / GATES 2-6
   OPEN` status — algebraic distinguishability found, physical realization
   remains the open item pending Part 5. Do not claim L3b is closer to
   resolved than `GATE 1 OF 7` warrants.
2. **Cross-reference check (not yet done, scoped for item 8):**
   `docs/gates_tracker.md`'s coverage stops at `G106` (2026-07-06, per
   round120's own finding) — decide whether to fold `G97` and
   round102/108/109/118/119/120/121 into the tracker as proper rows, or
   leave this as a documented, accepted lag (round120 flagged this,
   did not fix it).
3. **No change needed** to the `N_gen=3` headline conditional wording
   itself (abstract, `README.md`, `CLAIM_LEDGER.yaml` `C4`) — this round's
   own verdict (§2 above) confirms it remains accurate as currently
   stated.
4. **No change needed** to `OPEN_BLOCKERS.md` OB1 (parked) or the
   round118/OB11 matter-generation status — both remain correctly scoped
   as open, no recomposition issue found there.

## 6. Final recomposition verdict

**Corrected scope [skeptic correction — see note at top]:** for the claims
this round actually re-examined (`C1`, `C2`, `C3`, `C19`, `C20`,
`C_G67C3`, and now `C21`, added this round), the ledger recomposes to
license exactly what `CLAIM_LEDGER.yaml`'s `C4_NGEN3_HEADLINE` already
states: `N_gen=3` is `CONDITIONAL`, blocked on two independent open
premises (`C_G67C3` channel-distinguishability, `C3` KT-8 zero-mode),
unchanged by this session's substantial rounds 111-121 work — with one
ledger-accuracy fix applied (`C21`, a previously-uncaptured premise). The
other ~18 claims in the ledger were not individually re-audited this
round; this file does not claim to have verified them clean, only that
rounds 111-121 never touched them. The one concrete editorial finding is
that `preprint.tex`'s L3b text understates the project's own progress and
should be updated — precisely scoped above, deferred to item 8, not
applied here.

## What this does NOT mean

1. Does NOT change `N_gen=3`'s status, `lambda=FREE_COUPLING_PARAMETER`,
   or `safe_for_runtime=False`.
2. Does NOT edit `preprint.tex` — item 8's job, not this round's.
3. Does NOT claim the ledger is exhaustive over the project's ~157
   experiments (per `CLAIM_LEDGER.yaml`'s own stated scope) — this is a
   recomposition check of the LOAD-BEARING claims specifically.
4. Does NOT claim all 22 ledger entries were individually re-audited this
   round for recomposition consistency — only `C1`, `C2`, `C3`, `C19`,
   `C20`, `C_G67C3`, `C21` were actually traced against `D2`; the rest were
   confirmed only as "untouched by rounds 111-121," a narrower claim.
5. Does NOT resolve `OB10`, `OB11`, or the `SO(4)×SO(4)` physical-
   realization gap — all remain exactly as open as before.

## Sources

- `tom_s3_spinor_toy/CLAIM_LEDGER.yaml` (22 entries as of this round)
- `tom_s3_spinor_toy/DERIVATION_GRAPH.yaml` (all 3 chains)
- `tom_s3_spinor_toy/preprint.tex` lines 1256-1296 (Open Problems L3a/L3b)
- `tom_s3_spinor_toy/L3B_SPIN8_INTERFACE_SPEC.md`
- `tom_s3_spinor_toy/TRIALITY_DISTINGUISHABILITY_GATE.md`
- `tom_s3_spinor_toy/GAUGE_HILBERT_RECOMPOSITION.md`
- `tom_s3_spinor_toy/experiments/20260717-round118-matter-generation-factorization-test/decision.md`
- `tom_s3_spinor_toy/experiments/20260717-round121-independent-round59-agricola2002-crosscheck/decision.md`
