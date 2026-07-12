---
experiment_id: 20260708-dolan-casimir-g2su3
round: 46
date: 2026-07-13
tier: Full-Ladder
status: skeptic_reviewed_duplicate_of_round30_not_promoted_as_new_science
parent: round45 (blind Leibniz-correction test, REJECTED — L4A branch
  parked); this round pursued the user's own chosen next scientific
  target — the "Casimir_su3-vs-Jac_h identity question" — believing it
  was still open per Round 39's own text. **Skeptic review found this
  is a REDISCOVERY of `round30_claim.md` (2026-07-11), which already
  established and closed this exact question, two days earlier, with a
  stronger structural derivation, through TWO independent review
  passes (FL Step 8a + `/boyko-triangle-audit`). Round 39 (2026-07-12)
  incorrectly reopened a question Round 30 had already closed one day
  prior — a real project-continuity gap, and this round inherited the
  stale framing without checking.**
---

# claim.md — Round 46: NOT new science — a redundant re-verification
of Round 30's own already-closed `Ch_tilde = Casimir_su3` result

## What actually happened (read this first)

This round set out to test whether `Casimir_su3` (this project's own
su(3) Casimir) equals Agricola's own Jac_h-induced `C~h` object,
believing this was genuinely open (Round 39's own text: "does NOT
determine whether Casimir_su3 IS or merely resembles Agricola's own
Jac_h term"). **Three independent FL Step 8a reviewers (2 skeptics +
synthesis) found `round30_claim.md`/`g2su3_round30_ch_casimir_
structural.py` (2026-07-11, same experiment directory) already
established and closed this exact identity, on the same full 8×8
scope this round claims as its own rigor, with a considerably STRONGER
argument (a 9-step structural derivation tracing the identity to
Agricola's own page-10 definition, surviving TWO review passes
including a `/boyko-triangle-audit` pass that caught a subtle gap
neither skeptic had found).**

**Compounding findings (synthesis agent, independent verification):**
- This round's own "independent primitive sources" claim is FALSE:
  `AD_NU_M_BIVECTOR` (feeding `C~h`) and `SU3_GENERATORS` (feeding
  `Casimir_su3`) are BYTE-IDENTICAL — a fact Round 30's own docstring
  ALREADY disclosed in its own "HONEST SCOPE" section, uncited here.
- This round's `jac_h`/`h_bracket_action_on`/`clifford_quad` functions
  are VERBATIM COPIES of Round 26's functions (diffed programmatically
  — identical bodies) — and Round 30's own STEP E already imported and
  ran this EXACT code, at the EXACT same scope. This round has ZERO
  methodological novelty over Round 30 — not just a shared data table,
  but a shared code path and a shared scope.
- Agricola 2002's own page 10 (read directly, pp.9-11) DEFINES `C~h`
  as "the lift of the Casimir operator of h" BEFORE Proposition 3.3 —
  meaning the identity is near-definitional, not an independent
  discovery to make in the first place. Round 30 already cited this.
- The "genuine conceptual simplification (fewer primitives)" framing
  this round originally used is BACKWARDS: `Casimir_su3` is the
  SIMPLER object (direct sum of squares); `C~h` requires MORE
  machinery (`Qh_sum` + `Jac_h` quartic Clifford products) built from
  the SAME underlying generator table. Re-expressing via `C~h` adds
  primitives, it does not remove any.
- The negative control (`H ≠ Casimir_su3`) is largely tautological
  given this project's OWN Round 43 (chirality no-go theorem):
  `H` is odd-Clifford-degree, `Casimir_su3`/`C~h` are even-degree —
  this project's own prior theorem already guarantees they differ,
  regardless of numeric content. It demonstrates parity discrimination,
  not the same-parity discriminating power the actual C3 identity
  needed.

## Root cause (the actual, valuable finding of this round)

Round 39 (2026-07-12) reopened "Casimir_su3-vs-Jac_h" as an explicit
open question a full DAY after Round 30 (2026-07-11) had already
closed it in the SAME directory, with NO citation connecting them —
confirmed by `grep -in "round30\|round 30"` across `round39_claim.md`,
`round46_claim.md`, and this round's own script: ZERO hits in all
three, before this correction. This is this project's own
`research-methodology.md` § Классификатор Type 4 lag failure mode
("новый NULL не применён к старым PROMOTE"), inverted: an OLD PROMOTE
was not carried forward and cited by a LATER round, causing genuinely
wasted, duplicate investigative effort (Round 39's own uncertainty,
and now this entire Round 46).

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — the underlying computation (`C~h =
Casimir_su3` on the full 8-dim Σ) is real and tool-verified, but this
round adds NO new information beyond Round 30's own already-closed,
already-caveated result.

## What survives from this round's own work

- **[CONFIRMED-REAL]** The raw 64-entry numeric identity `C~h -
  Casimir_su3 = 0` — re-verified once more (a harmless, if redundant,
  regression check), consistent with Round 30's own STEP E.
- A clean, explicit trace of the "why this isn't new" chain (this
  document), which corrects the record for any FUTURE round that might
  otherwise re-encounter Round 39's own stale "explicitly open" framing
  a third time.

## Falsifiable Claims (as originally stated, with post-skeptic verdicts)

**C1:** `Casimir_su3` eigenvalues `{0:2, 4/3:6}`. RESULT:
`[CONFIRMED-REAL]` — tool-verified, consistent with Round 17-20.

**C2:** `C~h` Hermitian, `(C~h)_0=1`. RESULT: `[CONFIRMED-REAL]` —
tool-verified.

**C3 (the identity, as originally framed — "independent," "novel,"
"resolves an open question," "conceptual simplification"):** RESULT:
**`[WEAKENED]`, effectively withdrawn as a novelty claim.** The bare
64-entry equality is real (`[CONFIRMED-REAL]` as a numeric fact alone)
— but every interpretive claim wrapped around it is false: not
independent (shared generator table + verbatim-copied code), not novel
(Round 30 already established this, more rigorously, two days earlier),
not a simplification (backwards — `C~h` needs strictly more machinery
than `Casimir_su3` alone).

**C4 (negative control):** RESULT: `[WEAKENED]` — real but structurally
guaranteed by this project's own Round 43 chirality theorem (odd- vs
even-Clifford-degree), not a demonstration of genuine same-parity
discriminating power.

## Kill Conditions

- The overarching kill condition this round itself specified
  ("hidden shared dependency... check the import graph directly") —
  **TRIGGERED, confirmed by all three reviewers.** `AD_NU_M_BIVECTOR ≡
  SU3_GENERATORS` (byte-identical dict), and `jac_h`/
  `h_bracket_action_on`/`clifford_quad` are verbatim copies of Round
  26's own functions, already run by Round 30 at the same scope.

## What this does NOT mean

- **Does NOT add new mathematics or new evidence beyond Round 30's own
  already-closed, already-caveated result** — this is the round's
  central, honest finding.
- **Does NOT mean Round 30's own result was ever in doubt** — it
  survived two independent review passes on its own and remains solid;
  this round's redundant re-verification is mildly corroborating at
  best, not load-bearing.
- **Does NOT resolve the L4A tension** (parked, untouched) or `RHO`/
  `NU`'s notation question (Round 34, untouched).
- **Does NOT touch `preprint.tex`.**
- **Concrete next step, NOT started:** the user's own next scientific
  target should be chosen fresh, now correctly informed that
  Casimir_su3-vs-Jac_h was ALREADY closed (Round 30) — not a live
  open question. `RHO`/`NU`'s literal AHL2023 notation question
  (Round 34) remains the one standing, genuinely unaddressed item from
  the user's own prior list.

## Skeptic Verdict (FL Step 8a)

Two context-blind skeptics + a synthesis agent, all working
independently, converged on the SAME decisive finding via slightly
different routes.

| Claim | Skeptic 1 | Skeptic 2 | Synthesis (independent 3rd verification) |
|---|---|---|---|
| C1 | CONFIRMED-REAL | CONFIRMED-REAL | CONFIRMED-REAL |
| C2 | CONFIRMED-REAL | CONFIRMED-REAL | CONFIRMED-REAL |
| C3 | WEAKENED (Agricola p.10 definitional; shared generator table) | **FALSIFIED on framing** (found Round 30 prior closure directly) | WEAKENED, redundancy confirmed at code-path level (verbatim-copied functions, not just shared table) |
| C4 | WEAKENED (Round 43's own chirality theorem makes this near-tautological) | WEAKENED (same finding) | WEAKENED (confirmed) |

**Skeptic 1** independently found (without searching for prior rounds)
that Agricola 2002's own page 10 DEFINES `C~h` as the Casimir-of-h
lift — meaning Proposition 3.3 (which this round and Round 26 both
build from) is Agricola's OWN re-expansion of an object she had ALREADY
defined as the Casimir, not an independent geometric quantity that
happens to coincide with one. Also independently traced
`AD_NU_M_BIVECTOR`/`SU3_GENERATORS`'s shared-table dependency via the
import graph, exactly as this round's own kill condition specified.

**Skeptic 2** went further and found the MOST decisive fact neither the
claim nor Skeptic 1 had: `g2su3_round30_ch_casimir_structural.py`
(2026-07-11, two days prior) already established this exact identity
at the same full-8×8 scope, already disclosed the shared-table fact in
its OWN "HONEST SCOPE" section, and already cited Agricola's page-10
definition as its own starting insight — surviving two independent
review passes (FL Step 8a, then a `/boyko-triangle-audit` pass that
caught a subtler gap in Round 30's OWN first-pass argument, which
Round 30 itself then fixed).

**The synthesis agent independently re-verified BOTH findings from
scratch** (ran Round 30's own script directly, read Agricola's PDF
pages 9-11 directly, diffed the generator tables in Python, diffed
Round 26's vs this round's `jac_h` function bodies programmatically)
and found a THIRD compounding fact neither skeptic had caught: this
round's `jac_h`/`h_bracket_action_on`/`clifford_quad` functions are not
merely analogous to Round 26's — they are byte-identical copies, and
Round 30's own STEP E already imported and ran this exact code at the
exact same scope this round claims as its distinguishing rigor. The
"not imported, to avoid shared-state circularity" framing in this
round's original docstring masked a Python-implementation-detail
distinction (copy-paste vs import) as if it were independent
mathematical derivation.

**Response: full rewrite, not dismissal.** Per FL Step 8a's own
response matrix, this is neither a clean PROMOTE nor a true-kill
REJECT — the underlying math is correct and uncontested, but the
round's ENTIRE interpretive framing (independence, novelty, resolving
an open question, simplification) was false. This document has been
rewritten in full to honestly record: what was actually found (a
redundant rediscovery), why it happened (Round 39's own uncited lag
relative to Round 30), and what genuinely survives (a harmless,
non-load-bearing re-confirmation of an already-solid prior result).

**Verdict: NOT PROMOTED as new science. Recorded as a process/
continuity finding.** No claim about the underlying physics/algebra is
false — `C~h = Casimir_su3` is true and remains established (by Round
30, not this round). What is corrected is the false novelty/
independence narrative this round originally wrapped around a true but
already-known fact.
