# C123 claim -- Novelty Check + PARENT_ACTION_GATE F1 pre-check on two
candidate OB1 mechanisms surfaced by an external multi-model panel review
(6 LLMs independently asked to solve the torsion-selection problem;
mechanisms extracted, not the panel's own confidence)

## Question type (EstimandOps L0)
**Descriptive.** Does a specific proposed mechanism (a) duplicate existing
project content, and (b) pass existing gate-fill checks (F1 topological
pre-filter, C121 collapse-check)? No causal or predictive claim about
physical reality.

## Background

An external multi-model panel (7 independent LLM responses to the
Torsion Selection Problem homework artifact) converged, among other
things, on two related candidate mechanisms for OB1 (t-selection):

1. A Yang-Mills-type curvature-energy functional `S_YM[∇^t] =
   ∫_{S³}|R^t|² dvol` on the S³ factor alone.
2. A transgression/Kaluza-Klein-reduction term `S_mix = k∫_{M13}
   CS₃(ω_{S³}) ∧ P₄(M₄) ∧ ch₃(E_{S⁶})`, coupling the S³ torsion sector
   to this project's own already-certified S⁶ twist-bundle topology
   (the same `ch₃`/`c₃` data underlying `N_gen=3`, G73→G74A→G74B).

Per this project's own discipline (`PARENT_ACTION_GATE.md` reopen
condition 4: "Any candidate MUST pass PARENT_ACTION_GATE.md's checklist
before being attempted"), before either mechanism is treated as a live
OB1 candidate, this round runs: (a) a Novelty Check (FL Step -3) against
`round86-89`, `round99`/OB13, and `C119`; (b) a cheap, reuse-only F1-style
check (does the S⁶-coupling piece survive C119's own topological
pre-filter, and is its input data actually nonzero, using ALREADY
CERTIFIED project data, no new computation).

## Falsifiable claims

**Claim 1 (duplication):** `S_YM[∇^t]` is not new content as an OB1 F4
mechanism -- it duplicates `round99`'s "curvature-norm toy" (cited in
`OPEN_BLOCKERS.md` OB13), because `R^t = t(t-1)·T` with `T` t-independent
forces every quadratic curvature invariant into the identical `[t(t-1)]²`
shape up to a positive constant.

**Kill criterion:** if `round99`'s actual script computes a DIFFERENT
t-dependence (not proportional to `[t(t-1)]²`), or if the duplication
does not hold at the specific gate field that matters (F4 selection vs
F6 background-equations), claim 1 as stated is FALSIFIED or must be
narrowed.

**Claim 2 (nonvanishing / gate-survival):** the transgression term's
S⁶-coupling factor `∫_{S⁶}ch₃(E_{S⁶})` is nonzero (reusing this
project's own already-certified `c₃(S⁻)=2`, `Â(S⁶)=1` data, G73/G74B),
AND this specific construction survives C119's topological pre-filter
(any candidate requiring a harmonic k≤3-degree form with a nonzero leg
on S⁶ is dead-on-arrival, `b₁=b₂=b₃(S⁶)=0`) because `ch₃` is a degree-6,
not degree≤3, class.

**Kill criterion:** if `ch₃(E)≡c₃(E)/2` is not actually a valid
identification for this specific bundle (a Type-1 symbol-overload error,
per `research-methodology.md`'s classifier), or if the C119 pre-filter's
own stated scope actually does cover degree-6 classes, claim 2 is
FALSIFIED.

## SUBSTRATE UPDATE (2026-09-01, FL Step 8a skeptic pass, context-blind
-- claim.md + file pointers only, no session history) -- both claims
partially reclassified; a new, more decisive kill test surfaced

Skeptic (context-blind, `Agent(skeptic, model=opus)`) independently
re-derived every load-bearing number rather than trusting the claim
text. Full response in `decision.md`. Summary of reclassification:

- **Claim 1**: CONFIRMED as a duplicate at gate field **F4** (selection)
  specifically -- but explicitly NOT a duplicate at **F6** (background
  equations), since `round99`'s own script had no volume integral, no
  action framing (its own `decision.md` records this as a skeptic-
  accepted gap). More significantly, the skeptic found the REASON this
  round's claim.md gave for expecting the duplication (`OPEN_BLOCKERS.md`
  OB13's "any even functional carries no information, selector must be
  linear") is itself **FALSIFIED as literally written** -- see
  `decision.md` for the full three-part refutation, independently
  triggered by defending claim 1 rather than being the round's own
  target.
- **Claim 2**: all three narrow technical checks (c₃(S⁻)=2 real;
  `ch₃≡c₃/2` valid, not overload; C119 pre-filter genuinely scoped k≤3)
  CONFIRMED. Overall viability WEAKENED by two gaps not in the original
  kill criterion: (a) possible collapse of `CS₃(ω^t)` into C121's
  already-REJECTED `η(D^t)` (flagged as unresolved hypothesis by
  skeptic, resolved this session -- see decision.md, NOT proportional,
  confirmed by direct coefficient comparison); (b) `∫_{M4}P₄(M4)=0` on
  this project's actual (topologically trivial) frozen 4D background --
  a fatal, previously-unnoticed gap in the construction AS STATED,
  independent of the S⁶ side entirely.

## What this round does NOT show

- Does not resolve OB1. Stays PARKED (per `OPEN_BLOCKERS.md`'s own
  framing, this round's findings do not meet any of the 4 reopen
  conditions on their own -- see decision.md).
- Does not fix `OB13`'s own overstated text in place -- flags the defect,
  does not edit `OPEN_BLOCKERS.md` OB13's prose (a separate, explicit
  editorial step, not bundled into this gate-check round).
- Does not attempt to rescue Claim 2 by finding a non-topological
  `P₄(M₄)` (e.g. from a bosonic field strength rather than pure
  spacetime curvature) -- named as an unattempted next step only.
- Does not change `N_gen=3`'s CONDITIONAL status, `lambda=
  FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.
- Does not solicit Tom Lawrence's Part 5.

## Verification plan

- Reuse only: `c₃(S⁻)=2` (G73), `Â(S⁶)=1` (G50 via G73), `ind=+1`
  (G73→G74A→G74B) -- no new numerical computation on the S⁶ side.
- `round99`'s actual script read directly, not summarized from memory.
- FL Step 8a skeptic pass, context-blind (claim.md + file pointers only).
- This session's own follow-up algebra (CS₃ vs η(D^t) coefficient
  comparison) shown in full in `decision.md`, marked as this session's
  own re-derivation, not yet independently skeptic-reviewed.
