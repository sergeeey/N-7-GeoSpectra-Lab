# E18 (round86) — Claim: Parent-Action Discriminator for t=0/t=1 Coexistence

**Date:** 2026-07-17
**Predecessor:** `experiments/20260717-round85-e17-sector-coexistence-gate/` (E17),
which found the representation content of `{ker D^{t=0}, ker D^{t=1}}` fully
consistent (necessary condition PASS) but left the physical, SIMULTANEOUS
coexistence of both sectors undecidable, naming the missing ingredient as "a
stated 13D parent action specifying how many independent Dirac
fields/connections the compactification actually contains" (KT-8).

## Question type (EstimandOps L0)

**Descriptive/structural**, not causal, not predictive. The question is: does
a specific mathematical/physical construction (an action, Lagrangian, or
field-theoretic derivation) already exist — either in this project's own text
or in this project's own already-cited literature — under which `t=0` and
`t=1` are NECESSARY co-present sectors of one theory, rather than two
mutually exclusive values of one free parameter? This is answered by
literature search plus direct citation-checking, not by new numerical
computation or a causal-effect estimate.

## Frozen claim (verbatim, as specified by the task)

There exists a single action or field construction in which `t=0` and `t=1`
arise as two NECESSARY left/right sectors, not as two mutually exclusive
values of one free parameter.

## Three candidate constructions (any ONE suffices for PASS)

1. **Block-diagonal operator** `D = diag(D^{t=0}, D^{t=1})` with a
   PHYSICALLY DERIVED (not postulated) two-sector Hilbert space — some
   independent physical reason (not just "we need 2 sectors so let's assume
   2") why the theory's field content naturally splits into two copies, each
   carrying one torsion value.
2. **Two independent connection fields** `∇_L`, `∇_R`, related by a parity
   symmetry, each with its own equation of motion, such that a
   parity-symmetric ACTION (not just a parity-symmetric OBSERVATION)
   naturally produces both.
3. **A single torsion/flux field whose SIGN acts differently** on left- vs.
   right- representations — one dynamical field `H` (or similar) that,
   depending on its sign (a genuine dynamical or topological choice, e.g.
   flux quantization discretely selecting a sign, or a domain-wall/kink
   structure interpolating between signs), realizes `t=0` in one
   region/sector and `t=1` in another, within ONE unified field-theoretic
   description.

## PASS requires ALL of

An action (or a field-theoretic Lagrangian/energy functional), explicit
fields, a stated symmetry, equations of motion (or a clear derivation showing
the construction is dynamically consistent, not just kinematically
assembled), an explanation for WHY both sectors are present (not merely THAT
they could be), and no manual/ad hoc duplication (i.e. the "2" must come out
of the construction, not be put in by hand).

## FAIL

None of the three constructions can be built from anything this project has
already established or can find in its own already-cited literature, and no
fourth alternative construction succeeds either.

## BLOCKED

Determining this requires genuinely new physical input (a specific parent
theory, e.g. from 11D/12D supergravity, that this project does not currently
have access to or has explicitly deferred, e.g. per this project's own
standing rule that `lambda = FREE_COUPLING_PARAMETER` and
`safe_for_runtime = False`) — i.e. the question is well-posed but not
answerable from what exists.

## Method (per this project's "Using Wheels First" principle)

1. Check the three PDFs this project already cites for the Cartan-Schouten
   connection family and nearly-Kähler geometry
   (`Agricola_2002_Dirac_naturally_reductive.pdf`,
   `Agricola_Hofmann_Lawn_2023_invariant_spinors.pdf`,
   `Charbonneau_Harland_2016_NK_instantons.pdf`) for any construction
   resembling candidates 1–3.
2. Re-examine this project's own E11 (Freund-Rubin flux, candidate 3) and
   `preprint.tex`'s Pati-Salam / left-right-symmetry text (candidate 2) for
   unexplored pieces.
3. Render a verdict: PASS / FAIL / BLOCKED, with a precise statement of what
   is missing if BLOCKED.

## Assumptions carried, unresolved (inherited from E17/E13/E11/E14)

- `SU(2)_L`=left-translation vs its mirror remains genuinely ambiguous
  (`CONVENTION_TABLE.md` row 6) — this experiment's verdict does not depend
  on resolving it, since no candidate reaches the point where the
  labeling convention would matter.
- `t=1`'s existence is established only under `c0=-2`
  (`CONVENTION_TABLE.md` row 5), not the abstractly-calibrated `c=+2` — carried
  forward, not re-litigated here.
- `D_full² = D_{S3,t}²⊗I + I⊗D_{S6,twisted}²` (E2/E12's decoupling
  assumption) is presupposed wherever prior results using it are cited.

## What this does NOT mean (pre-registered, before results are known)

1. Does not re-derive or challenge any of E2/E3/E7/E9–E17's own tool-verified
   results — all reused here purely by citation.
2. Does not resolve KT-8 (whether ANY zero mode of the full untwisted
   `D_full` exists) or H1c (physical selection of `t`) — those remain exactly
   as open as this project already has them.
3. Does not imply this project's `N_gen=3` headline claim (which rests on
   the independently-established G73/G74A/G74B S6-only chain) is affected —
   this experiment concerns only the separate S3-side torsion-escape-route
   program, already characterized in `preprint.tex` as a candidate mechanism,
   not load-bearing for `N_gen=3`.
4. A BLOCKED verdict does not mean the question is meaningless or that no
   further progress is possible — see `decision.md` for the precise missing
   ingredient, if BLOCKED is the outcome.
5. Does not claim the three PDFs were exhaustively read cover-to-cover;
   claims about their content are scoped to what was searched and read, and
   any part not read is explicitly flagged as not checked, not silently
   assumed absent.

## Kill criterion

If a fourth reading of the PASS requirement is found, at any point during
this experiment, that would only be satisfiable by manufacturing an ad hoc
"we now assume 2 copies exist" construction (duplication put in by hand
rather than derived) — that reading is explicitly excluded per the PASS
requirement's own "no manual/ad hoc duplication" clause, and must be recorded
as a rejected candidate, not silently omitted.
