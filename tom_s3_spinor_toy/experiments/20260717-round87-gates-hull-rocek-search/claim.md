# E19 (round87) — Claim: Gates-Hull-Roček / Bi-Hermitian WZW Construction as Candidate 2 Instantiation

**Date:** 2026-07-17
**Predecessor:** `experiments/20260717-round86-parent-action-discriminator/` (E18),
verdict `BLOCKED__NO_PARENT_ACTION_FOUND_IN_PROJECT_OR_CITED_LITERATURE__MISSING_INGREDIENT_NAMED`.
E18's own Relaxation Map named, as the most concrete unexplored next step:
"Search Strominger-Hull flux-compactification literature directly for an
explicit H-flux-sources-contorsion construction with a stated `q↔(2t-1)`
normalization" (`decision.md:436`). This experiment executes exactly that
next step, entering via the Gates-Hull-Roček (1984) / bi-Hermitian /
generalized-complex-geometry literature this project has NOT previously
cited, plus the specific WZW-model-on-a-group-manifold literature
(Spindel-Sevrin-Troost-Van Proeyen 1988 and successors) that provides the
natural worked example closest to this project's own `S³=SU(2)` setting.

## Question type (EstimandOps L0)

**Descriptive/structural**, not causal, not predictive — identical framing to
E18's own L0 classification. The question is: does a *specific*, externally
sourced construction (Gates-Hull-Roček twisted multiplets / bi-Hermitian
geometry / N=(2,2) WZW models) supply what E18's candidate 2 requires — an
action with two independent, symmetry-related connection fields, each with
its own equation of motion, and a genuine ("why both, not put in by hand")
necessity argument for `t=0` and `t=1` (or a directly analogous pair of
values) to coexist? Answered by literature search and structural comparison,
not by new numerical computation.

## Scope — this experiment tests ONE candidate, not the whole parent-action question

This experiment is scoped, per the task, to candidate 2 ONLY (E18's "two
independent connection fields `∇_L`, `∇_R`, related by a parity symmetry,
each with its own equation of motion, such that a parity-symmetric ACTION
... naturally produces both") as specifically instantiated by the
Gates-Hull-Roček / bi-Hermitian / WZW-model literature. If this candidate
FAILS, E18's overall `BLOCKED` verdict for the broader parent-action question
is **not** automatically reopened or re-verdicted here — it may still stand,
unless this candidate itself resolves it (which would flip the OVERALL
verdict, not just this candidate's).

## Frozen claim (verbatim, reusing E18's own PASS bar exactly)

There exists a single action or field construction — instantiated here
specifically via the Gates-Hull-Roček twisted-multiplet / bi-Hermitian /
N=(2,2)-WZW-model construction — in which `t=0` and `t=1` (or a directly
analogous torsion-connection pair, under an explicit, stated normalization)
arise as two NECESSARY left/right sectors of ONE physical theory relevant to
this project's `S³=SU(2)` compactification, not as two mutually exclusive
values of one free parameter chosen by hand.

## PASS requires ALL of (reusing E18's bar verbatim)

An action (or a field-theoretic Lagrangian/energy functional), explicit
fields, a stated symmetry, equations of motion (or a clear derivation showing
the construction is dynamically consistent, not just kinematically
assembled), an explanation for WHY both sectors are present (not merely THAT
they could be), and no manual/ad hoc duplication (i.e. the "2" must come out
of the construction, not be put in by hand) — **AND**, specific to this
experiment's added scope: the construction, as actually stated in its own
source literature, must be shown to be the SAME kind of mathematical/physical
object as this project's `∇^t` family (Agricola 2002 convention,
`CONVENTION_TABLE.md` row 5), not merely a superficially similar-sounding
"torsionful connection pair," AND its own stated reason for requiring
both signs must be shown to be applicable to this project's actual physical
setting (a Kaluza-Klein compactification of a higher-dimensional spacetime
theory on `S³`, not a 2D string worldsheet sigma model) — not merely
assumed applicable because both are "torsionful connections with a plus and
a minus sign."

## FAIL

The Gates-Hull-Roček / bi-Hermitian / WZW-model construction, on direct
inspection of its own primary/secondary sources, either (a) cannot be built
on `S³=SU(2)` at all for a structural reason stated in that literature itself
(not merely "no one has done it"), or (b) can be built formally but its own
stated reason for requiring both connection signs is shown to depend on
physical structure (e.g. a 2D worldsheet with independent left/right-moving
sectors) that has no counterpart anywhere in this project's actual
Kaluza-Klein compactification framework, so that importing it to explain
`t=0`/`t=1` coexistence would itself be the kind of ad hoc, manually-inserted
duplication the PASS bar's own "no manual/ad hoc duplication" clause
excludes.

## BLOCKED

The literature search cannot determine, from what is accessible, whether the
construction transfers or not — e.g. because the exact normalization linking
the WZW level/flux to this project's `t` parameter cannot be pinned down from
available sources, leaving the question open rather than resolved either way.

## Method (per this project's "Using Wheels First" principle)

1. `WebSearch`/`WebFetch` for the actual Gates-Hull-Roček (1984) paper and at
   least one modern, accessible secondary source (review, lecture notes, or
   paper) giving the precise bi-Hermitian/N=(2,2)-sigma-model construction
   (two complex structures `J±`, two torsionful — Bismut — connections
   `∇^± = ∇^{LC} ± (1/2)H`).
2. `WebSearch` specifically for whether `S³=SU(2)` (alone, not as a factor of
   a larger even-dimensional product) appears as a worked example in the
   WZW-model-on-a-group-manifold literature, and what condition on the group
   `G` is required for the construction to exist at all.
3. Compare, precisely, against this project's own `∇^t` family
   (`CONVENTION_TABLE.md` §§2,4,5): is `∇^± = ∇^{LC}±(1/2)H` the SAME object
   as `∇^t_XY=t[X,Y]_m` at `t=0,1` (up to a stated normalization), or
   structurally different despite superficial resemblance?
4. Render a verdict for THIS candidate only: PASS / FAIL / BLOCKED.

## Assumptions carried, unresolved (inherited from E11/E13/E14/E17/E18)

- `t=0`/`t=1` ↔ left-invariant/right-invariant frame correspondence,
  established only under `c0=-2` for `t=1` (`CONVENTION_TABLE.md` row 5).
- `SU(2)_L`/`SU(2)_R` physical (geometric) identification remains genuinely
  ambiguous (`CONVENTION_TABLE.md` row 6) — this experiment's verdict does
  not depend on resolving it.
- `D_full² = D_{S3,t}²⊗I + I⊗D_{S6,twisted}²` (E2/E12's decoupling
  assumption), presupposed wherever prior results using it are cited.

## What this does NOT mean (pre-registered, before results are known)

1. Does not re-derive or challenge any of E2/E3/E7/E9–E18's own tool-verified
   results — all reused here purely by citation.
2. Does not resolve KT-8 (whether ANY zero mode of the full untwisted
   `D_full` exists) or H1c (physical selection of `t`) — untouched.
3. Does not affect this project's `N_gen=3` headline claim (rests on the
   independently established G73/G74A/G74B S6-only chain) — this experiment
   concerns only the separate S3-side torsion-escape-route program.
4. A FAIL verdict for this ONE candidate does not, by itself, re-verdict
   E18's overall `BLOCKED` finding for the broader parent-action question —
   other routes in E18's own Relaxation Map remain untouched (a genuinely new
   13D parent-action derivation; the AHL 2023 cone-construction pearl).
5. Does not claim exhaustive coverage of the entire bi-Hermitian/generalized-
   complex-geometry literature (a large field) — scoped to what was actually
   searched and read this round, with any gap flagged explicitly.
6. External sources cited here (Gates-Hull-Roček 1984, Spindel-Sevrin-Troost-
   Van Proeyen 1988, and any modern review found) are used ONLY as
   comparison/citation material for this project's own internal question —
   this is not a submission or claim about the external literature itself,
   and nothing here is submitted anywhere (`arXiv` submission remains
   forbidden per this project's standing rules).

## Kill criterion

If, at any point, satisfying this candidate's PASS bar would require
asserting that this project's `S³=SU(2)` Kaluza-Klein compactification
secretly IS (or can be reinterpreted as) a 2D string worldsheet sigma model
— a claim this project's own `preprint.tex` and `activeContext.md` nowhere
make or need — that reading must be recorded as a rejected, ad hoc candidate,
not silently adopted to force a PASS.
