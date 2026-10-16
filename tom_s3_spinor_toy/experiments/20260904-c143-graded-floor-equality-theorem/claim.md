# C143 -- DESIGN/THEOREM round, no new Dirac-operator construction. Turns
# C141's own empirical finding (graded rank-nullity floor exactly predicts
# observed kernel, 4/4) into a general LEMMA with a precise necessary-and-
# sufficient equality condition, proved from already-certified facts (not
# re-verified by brute-force enumeration of more cases). Also formalizes
# C141/C142's own emerging methodology into a standing pre-registration
# gate for all future twisted-D_S6 rounds, per the user's own explicit
# proposal (2026-09-04): compute the graded floor BEFORE building D, and
# treat any FUTURE kernel exceeding it as the actual anomaly worth
# investigating -- not kernel=1 itself.

## Mode declaration

**Design/theorem-only round.** No physics computation, no new twist
bundle built, no `results_c143.json` (no numeric verification script in
the C133+ AST-self-audit sense -- the "checks" here are proof steps, and
where a symbolic illustration is useful it is a small, explicitly-labeled
toy example, not a physics claim). Explicitly NOT "another heavy C144-
style twist round" -- this is exactly the alternative the user proposed
in place of one, and the choice to do this instead is itself the round's
first decision, stated and justified below rather than assumed.

## The question, precisely

C141 found, empirically, across 4 constructions (round59/T0, C139, C141,
T1): `dim ker(D_rho) = floor(rho)`, where `floor(rho)` is a graded rank-
nullity lower bound computed per `{connection}`-invariant summand from
pure `su(3)` branching data alone. C141 itself left open (Section 9e's
own `[INFERRED]` marker, confidence LOW-MEDIUM) whether this is a general
THEOREM or an empirical regularity holding only in the 4 cases checked.

**This round's task:** state and prove the precise, general condition
under which equality holds -- not "does it always hold" (a vague
question) but "holds IFF ___" (a checkable one), separating what is
provable NOW from already-certified facts from what remains genuinely
open.

## Background, read in full before writing anything

- `experiments/20260904-c141-matched-singlet-count-twist-m-plus-2singlets/decision.md`
  Sections 9e/10 IN FULL -- the graded-floor construction and its 4/4
  empirical match, and Section 9e's own honest `[INFERRED]` scoping of
  what is NOT yet established.
- `experiments/20260904-c142-graded-floor-candidate-scan/decision.md` IN
  FULL -- the Hom-space-dimension analysis (Section 1: every summand
  tested so far has `Hom` dimension exactly 1) and the search for a
  genuinely `>=2`-dimensional candidate (Section 2/3), found currently
  unbuildable.
- `experiments/20260714-round59-trivial-rank-certification/decision.md`
  -- re-read Section "Why the coefficient is -sqrt(3)" (the Friedrich-
  bound / Killing-spinor-eigenvalue argument for why round59's own scalar
  is forced nonzero, NOT a coset-specific accident).
- `pearl_registry/INDEX.md` row 24 (find it, quote it exactly) -- round59's
  OWN pearl, from 2026-07-14, already states the general principle this
  round's Lemma 1 formalizes: *"rank(D+|1) is thus MECHANISM-forced by
  Killing-spinor existence, not a coset-specific numerical accident...
  On any other nearly-Kahler coset admitting Killing spinors with nonzero
  Killing constant... the analogous trivial-block rank should also be 1
  by the same two-line argument."* This round's job is to connect this
  ALREADY-REGISTERED, decade-old-in-session-time principle to C141's
  graded-floor framework explicitly -- not to discover it fresh.
- `experiments/20260904-c139-twisted-s6-alternate-representation-negative-control/decision.md`
  Section 6 -- `Term2`'s own direct symbolic derivation (`c =
  -2*sqrt(3)/3`), the analogous "why this scalar is nonzero" fact for the
  `m`-twist case, established by direct computation rather than a general
  eigenvalue argument (name this distinction honestly -- round59's
  nonvanishing has a GENERAL geometric reason; C139's, so far, only a
  COMPUTED one).

## The Zero-Signal Gate check, required before proceeding

Per `falsification-ladder.md` Step -5: `(exists entity) AND (exists
falsifiable predicate) AND (exists measurable outcome)`, all three
required.

- **Entity:** the graded-floor equality `dim ker(D_rho) = floor(rho)`,
  as a general statement over the class of twisted-`D_S6` constructions
  this project's own Leibniz-rule machinery can build.
- **Falsifiable predicate:** either (a) a general, provable necessary-
  and-sufficient CONDITION for equality exists, stated precisely enough
  that a future round could check it WITHOUT building the full Dirac
  operator -- or (b) no such general condition can be established beyond
  case-by-case verification, and this should be reported honestly as a
  genuine limit of what this round's synthesis can achieve.
- **Measurable outcome:** a stated lemma (or two, per the Hom-space-
  dimension split C142 already found structurally necessary), each
  either proved from already-certified facts or explicitly flagged
  `[OPEN]`.

## What this round does NOT show

- Does NOT prove `dim ker(D_rho) = floor(rho)` holds UNCONDITIONALLY for
  every conceivable twist bundle -- Section 2 below shows precisely why
  it cannot, for Hom-spaces of dimension `>=2`.
- Does NOT build or test `W_cand=3+3bar+3bar` (C142 already found this
  currently unbuildable with existing project content) or any other new
  twist bundle.
- Does NOT reopen C123-C142's verdicts.
- Does NOT change `N_gen=3`'s CONDITIONAL status.
- Does NOT solicit Tom Lawrence's Part 5.

## Verification plan

- State Lemma 1 (Hom-dimension-1 case) precisely, and verify it is
  ALREADY implied by already-certified facts (round59's Friedrich-bound
  argument, pearl row 24, C139's Section 6, C141's Section 9e) -- not a
  new physics claim, a SYNTHESIS one.
- State Lemma 2 (Hom-dimension-`>=2` case) precisely, with an explicit,
  clearly-labeled TOY symbolic example (not a physics claim) showing why
  genericity does not trivially settle the question the way it does for
  dimension 1 -- a linear map with `>=2` independent parameters CAN be
  rank-deficient at a real, checkable (not measure-zero-and-ignorable in
  a geometrically-constructed, non-random family) locus.
- Formalize the `Delta_dyn := dim ker(D_rho) - floor(rho)` diagnostic
  (per the user's own naming) as a standing pre-registration gate for any
  future twisted-`D_S6` round, and propose its addition to
  `PARENT_ACTION_GATE.md` F2.
- Cite `[VERIFIED]`/`[CITED]`/`[INFERRED]`/`[SPECULATIVE]` throughout --
  this round leans heavily on citation of already-certified facts, so
  citation accuracy is the primary correctness bar, not new computation.
- No FL Step 8a skeptic pass required in the usual sense (no new physics
  claim, no computed kernel to falsify) -- but a plain self-check IS
  required: does Lemma 1 actually follow from the cited facts, or does it
  smuggle in an unstated assumption? State this explicitly, and have the
  orchestrating session re-verify the logical chain independently before
  registering anything, per this project's own audit-verification-gate
  discipline applied to a proof rather than a computation.
