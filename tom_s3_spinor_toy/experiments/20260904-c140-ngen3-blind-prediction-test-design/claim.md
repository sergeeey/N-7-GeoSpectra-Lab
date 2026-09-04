# C140 -- DESIGN-ONLY round. Scopes pearl_registry row 141's "N_gen=3
# Blind-Prediction-Test" (impact 8, pending since 2026-09-02, "no
# experiment folder yet, this is a flagged methodological gap, not yet
# scoped as an FL round") into a concrete, executable EstimandOps
# design. Per the 2026-09-04 plan, this round does NOT compute anything
# and does NOT reach a PROMOTE/REJECT physics verdict -- its only
# output is a DESIGN READY / DESIGN NOT YET READY assessment plus a
# concrete next-round spec, so that IF this is ever executed, it is not
# executed ad hoc.

## Why this is a design-only round, stated up front

Per `~/.claude/rules/falsification-ladder.md`'s Structure-Bias Guard:
"formal structure is for the output contract, not the reasoning layer."
This document's job is to do the REASONING (what would a genuinely
blind test even look like, for a claim this specific and hard to
counterfactualize) in prose first, then serialize the result into an
estimand precise enough that a LATER round could execute it without
re-litigating what "blind" means. No computation happens here.

## The question, quoted exactly (pearl_registry/INDEX.md row 141,
## 2026-09-02, source: external Gemini/MUH tangent, independently
## assessed and logged this session, tagged [WEAK] pending its own
## dedicated check)

*"This project's own headline claim N_gen=3 ... has never been tested
against a 'blind prediction' standard: was the specific
triality-symmetric structure chosen BECAUSE it is already known to
give 3 stable sectors, or would a genuinely blind construction (not
selecting for the answer) independently yield exactly 3? Today's own
G44 (triality collapses under bare G2) and G102 (an explicit,
UN-derived fiber-Spin(8)/triality postulate is needed to distinguish
the three channels at all) already show PART of N_gen=3's own credit
line rests on an assumption, not a derivation."*

Falsifiable prediction named in the pearl: *"If N_gen ... is computed
WITHOUT pre-selecting the triality/G2 structure specifically to yield
3, and the number varies, or requires additional tuning to reach
exactly 3, that demonstrates N_gen=3 is a selection effect, not a
genuine prediction."*

## The hard part, worked through honestly before any formal structure

The obvious objection to this whole line of test: `S6=G2/SU(3)` was
not chosen by this project at all -- it is Tom Lawrence's own starting
ansatz, presumably justified (in his framework) by considerations
independent of triality-channel counting (dimension, holonomy,
SUSY-preservation properties, gauge-group content). A "blind"
reconstruction that varies `S6`'s geometry freely would not be testing
Tom's theory at all, it would be testing a strawman nobody proposed.

So the estimand must be precise about WHAT is allowed to vary and WHAT
is held fixed. The candidate population cannot be "all 6-manifolds" --
it must be the SMALLEST class of alternatives that (a) satisfies
whatever independent constraints Tom's framework already imposes on
`S6` (homogeneity, a compatible `SU(3)`-structure, real dimension 6,
compatibility with the `S3` factor's own already-fixed role), and (b)
is independently classifiable -- i.e. NOT invented ad hoc for this
test, but a closed, citable mathematical list that existed before this
question was asked.

**Candidate population identified (needs Step -4 source-trace
verification before use, marked `[CITED, unverified this session]`):**
the classification of homogeneous nearly-Kähler 6-manifolds is a
classical, closed, small list (commonly cited as four members:
`S^6=G2/SU(3)`, `S^3xS^3`, `CP^3`, and the flag manifold
`F_{1,2}=SU(3)/T^2`; attributed to Butruille 2005, building on
Wolf's classification of homogeneous 3-symmetric spaces). If this
citation checks out, it supplies exactly the kind of blind population
this test needs: a list that was fixed by pure differential geometry
LONG before this project or Tom's framework existed, not curated to
make `S^6` special. `S^6` is one of four, not the only option, in this
classification.

**Why this would be a genuine blind test, not a strawman:** all four
members of this list admit a metric cone construction with holonomy
contained in `Spin(7)`/related to `G2` structures (this needs
independent verification, not assumed), and all four are homogeneous
(matching this project's own repeated reliance on homogeneous-space
machinery throughout -- round59, G102, the whole `Sigma`/Peter-Weyl
apparatus). So the SAME general recipe this project already uses
(build a twisted Dirac-type operator compatible with the manifold's
own natural structure, count stable/protected zero-mode sectors) could
in principle be attempted on all four, without knowing in advance
which one is `S^6`-shaped. If the recipe only produces a well-defined,
finite "3 stable sectors" answer for `S^6` and not for the other
three (or gives a different number, or requires ad hoc tuning to reach
3 for the other three), that is *some* evidence against pure
selection. If multiple members give exactly 3, or the recipe cannot
even be meaningfully applied to the other three (the more likely
outcome, honestly), the test may turn out to be inconclusive by
construction -- state this risk up front, do not discover it after
investing effort.

## Question type (EstimandOps L0)

**Descriptive**, with an important scope note: this asks about the
STRUCTURE of a specific mathematical classification and a specific
construction recipe's behavior across it, not about the physical
world. It is explicitly NOT a claim about which manifold is "really"
correct (that remains Tom's framework's own choice, for reasons this
project does not adjudicate) -- it asks only whether the framework's
choice happens to be privileged by the channel-counting construction
itself, among the independently-known alternatives, or not.

## Estimand (L1 attributes, per EstimandOps)

- **Population:** the four (pending verification) homogeneous nearly-
  Kähler 6-manifolds classified independently of this project.
- **Intervention:** apply this project's own triality/channel-counting
  construction (the G102 `dim c_{so(8)}(g)=0`-style obstruction check,
  or its natural analogue) to each manifold's own structure group,
  without presupposing which one is `S^6`.
- **Comparator:** none in the causal sense -- this is a within-list
  comparison across all four members, not a treatment-vs-control
  design.
- **Endpoint:** for each manifold, either (a) a well-defined count of
  "independently distinguishable channels" analogous to `N_gen`, or
  (b) an explicit statement that the construction does not transfer
  (the recipe may be `G2`-specific in ways that make it inapplicable
  to `S^3xS^3`/`CP^3`/the flag manifold at all -- this itself would be
  informative, not a null result to hide).
- **Summary measure:** the distribution of endpoint values across the
  four-member population -- is `S^6`'s "3" an outlier, typical, or
  the only well-defined case at all?
- **ICE (intercurrent events) and strategy:** if the construction
  cannot be meaningfully transferred to a given manifold (very likely
  for at least `CP^3`/flag manifold, whose isotropy structure differs
  substantially from `G2/SU(3)`'s), that manifold's endpoint is
  recorded as `NOT-APPLICABLE`, treated as a genuine outcome (a
  "composite" ICE strategy: inapplicability counts against the
  construction being a general, non-`G2`-specific recipe), not
  silently excluded from the population.

## What this round does NOT show, and why the test may be weaker than
## it looks -- named honestly, not discovered later

- Even a clean result (only `S^6` gives 3, robustly) would NOT prove
  `N_gen=3` is a genuine, externally-blind prediction of Tom's full
  theory -- it would only show the channel-COUNTING construction
  specifically does not trivially generalize away from `G2/SU(3)`. Tom's
  own choice of `S^6` over the other three, within his broader
  framework, may still rest on reasons this project cannot access or
  test (again: DO NOT INITIATE CONTACT).
- A likely, honestly-anticipated outcome is that the construction is
  simply NOT APPLICABLE to 2 or 3 of the other members (different
  isotropy representation theory, no analogous `Spin(8)`-fiber
  obstruction structure) -- if so, the test would be INCONCLUSIVE by
  construction, not a clean PROMOTE or REJECT. This should be stated
  as the single most likely outcome, per this project's own house
  discipline of predicting failure modes honestly before running
  anything.
- This design does not itself resolve pearl row 141's risk -- it only
  turns "not yet scoped as an FL round" into "scoped, with named
  execution risk," which is the entire and only point of this round.

## Zero-Signal Gate (Step -5)

| field | content |
|---|---|
| Entity | the 4-member (pending verification) classification of homogeneous nearly-Kähler 6-manifolds, and this project's own triality/channel-counting recipe applied across it |
| Falsifiable predicate | the recipe gives a well-defined endpoint for more than one member AND those endpoints differ from 3 in a way not requiring ad hoc tuning -- OR the recipe is well-defined for all four and only `S^6` gives 3 |
| Measurable outcome | an explicit 4-row table: manifold, endpoint value or NOT-APPLICABLE, brief justification |

All three fillable => gate PASSES for a DESIGN. (Execution readiness is
a separate, lower bar -- see below.)

## Design-readiness kill criterion (this round's own verdict, NOT a
## physics verdict)

**DESIGN READY** if: (a) the Butruille/Wolf classification citation is
confirmed as real, primary-sourced, and genuinely independent of this
project (i.e. it existed as a closed mathematical fact before 2026);
(b) at least a plausible, stated construction recipe exists for
applying the channel-counting logic to at least one of the other three
manifolds (does not need to be built, just shown non-vacuous in
principle); (c) the ICE/inapplicability handling above is judged
sufficient to prevent the test from being silently vacuous.

**DESIGN NOT YET READY** if: the citation cannot be confirmed this
session, or no plausible construction recipe can even be sketched for
ANY of the other three manifolds (in which case the test as designed
would be vacuous by construction and needs a different population or
should be abandoned, reported honestly as such).

## Verification plan (for THIS design round only)

- Run FL Steps -4/-3 (source trace + novelty check) on the Butruille/
  Wolf classification claim specifically -- this is exactly the kind
  of factual citation this project's own AI-Hypothesis Pre-Gates exist
  to catch if wrong (`~/.claude/rules/falsification-ladder.md`).
  Verify via a real literature search (WebSearch/arXiv/Semantic
  Scholar), not from memory -- this session's own drafting of this
  claim.md used `[CITED, unverified this session]` deliberately for
  this reason.
- Check `null_results/INDEX.md` and `pearl_registry/INDEX.md` for any
  prior attempt at exactly this comparison under a different name
  (Mechanism-Transfer-Gate discipline) before treating the design as
  novel.
- If DESIGN READY: propose (do not build) a minimal C141-shaped
  execution spec -- which manifold to attempt first (the one most
  likely to have an applicable analogous construction, stated with
  reasoning), and the smallest computation that would produce a real
  data point.
- If DESIGN NOT YET READY: report exactly what is missing and whether
  a different candidate population (not the Butruille/Wolf list) might
  serve the same purpose, or whether pearl row 141's risk should stay
  open, unscoped, pending a better idea.
- No FL Step 8a skeptic pass required for a design-only round with no
  computed claim to falsify -- but a plain read-through self-check
  IS required: does the proposed design actually test what row 141
  asks, or does it quietly answer an easier, adjacent question? State
  this explicitly in the resulting decision.md.
