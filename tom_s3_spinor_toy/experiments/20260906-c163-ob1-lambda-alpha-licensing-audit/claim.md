# C163 claim -- was C161's "all->both via lambda-alpha identification" route ever
# licensed by C133's own text, or is it a type mismatch (free Hom-space modulus vs.
# computed spectral quantity) dressed up as a missing selection principle?

## Mode declaration

**Convergent-mode round (pure audit, no construction).** C161 (2026-09-05/06) scoped
a recombination of C133's `Phi = 1_F (x) (lambda_0*w_0 + lambda_1*w_1)` with C136's
computed per-channel, per-(t,frame) `alpha` values, found the recombination
underdetermined (four literal `(w0,w1)` frame pairings, three different verdicts), and
then -- via its own Section 9 independent skeptic pass -- found a SECOND, prior and
more basic problem: C133's own SS9 text calls `lambda_0,lambda_1` "a free 2-parameter
continuum," "a Hom-space dimension count," never a computed spectral quantity, while
C136's `alpha` is explicitly "solved from a 64-dim residual" -- an eigenvalue-like
output of a specific differential/algebraic system. C161 explicitly declined to
adjudicate between two readings this creates (INCOMPLETE-MACHINERY vs. ILL-POSED) and
named, as its own corrected practical recommendation, that a future round must FIRST
audit whether the identification itself was ever licensed by C133's own text before
attempting to build a frame-selection principle. This file is that audit. It is
registered in `pearl_registry/INDEX.md` (2026-09-06 row, C161) as the required next
step before any further OB1 construction on this route.

## Question type (EstimandOps L0)

**Descriptive.** Does a specific piece of text (C133's decision.md, and anything it or
C132 cites) contain a license -- a stated constraint, gauge-fixing condition, or
normalization convention -- for identifying two named symbols (`lambda_0`, `lambda_1`)
with a differently-sourced computed quantity (C136's `alpha`)? This is a textual/
argument-provenance question about what a prior round's own words say, not a physics
claim about the world, not causal, not predictive.

## Background, stated honestly before any computation

Read, in full, before doing anything else (all confirmed read this session):
- `experiments/20260902-c133-symmetry-ladder-pairing-space/decision.md` in full
  (916 lines), especially SS3 (the three-rung table, channel/fibre/sector factors),
  SS7 (the credit-line correction, "parent action" language), SS9 ("What the reduction
  actually is, stated precisely" -- where `Phi`, `lambda_0`, `lambda_1`, `w_0`, `w_1`
  are defined), and SS12 ("What this round does NOT show").
- `experiments/20260902-c133-symmetry-ladder-pairing-space/claim.md` in full (the
  pre-registration -- to check whether any constraint on `lambda_0,lambda_1` was
  pre-registered but dropped from the executed round).
- `experiments/20260902-c132-13d-parent-action-survey/decision.md` -- grepped for
  `lambda_0`/`lambda_1` (zero hits) and for the `P0` sketch C133 was built from.
- `experiments/20260902-c136-joint-killing-spinor-constraint/decision.md` in full,
  especially SS4 (the two readings of the constraint, `A = diag(0,alpha*1_3,beta*1_6)`)
  and SS5 (the 3x2 table, "`alpha` solved from the 64-dim residual").
- `experiments/20260905-c161-all-to-both-construction-scoping/claim.md` and
  `decision.md` in full, especially Section 9 (the independent skeptic pass that
  first surfaced this exact question) and Section 7 Attack 2 (C161's own
  self-adversarial pass, which flagged but did not close the same gap).
- `experiments/20260901-c125-full-gauge-equivalence-gate/decision.md` lines ~200-235,
  520-545 -- confirms what "C38" (cited by C133 for `w_0,w_1` "spanning the two S3
  t-sectors") actually supplies: two kernel LABELS, `ker(t=0)=(1,2)`, `ker(t=1)=(2,1)`
  -- not coefficients, not a normalization, not a spectral computation.
- `pearl_registry/INDEX.md` 2026-09-06 row (C161) -- the exact wording of the required
  next step this file executes.

## The Zero-Signal Gate check, required before proceeding

Per `falsification-ladder.md` Step -5: `(exists entity) AND (exists falsifiable
predicate) AND (exists measurable outcome)`, all three required.

- **Entity:** two named symbols in C133's own decision.md SS9 -- `lambda_0`, `lambda_1`
  -- and their proposed identification (made in C161's claim.md Intervention section,
  not in C133 or C136) with C136's computed `alpha(t, frame)` values from
  `results_c136.json`'s `E_table_3x2`.
- **Falsifiable predicate:** C133's own text (its exact definitions, any stated
  constraint, gauge-fixing condition, or normalization convention appearing anywhere in
  C133, C132, or a round they cite) either DOES or DOES NOT contain language that
  licenses treating `lambda_0,lambda_1` as identifiable with a computed spectral
  quantity from a different construction.
- **Measurable outcome:** a direct quotation-level reading of C133 SS3/SS9/SS12, C132,
  and C38 (via C125's citation of it), checked against C136's SS4/SS5 definition of
  `alpha`, producing one of two mutually exclusive verdicts (see Kill criterion).

**GATE: PASS.** All three fields fillable from primary text already in the repository.

## AI-Hypothesis Pre-Gates (novelty check)

**Step -4, Source Trace.** Every input is this project's own already-written text,
re-quoted directly from primary files (not from summary or memory) -- no external
literature claim is being audited here.

**Step -3, Novelty Check.** Grepped `null_results/INDEX.md` and `pearl_registry/
INDEX.md` this session for prior instances of this exact audit. Found: the 2026-09-06
`pearl_registry/INDEX.md` row for C161 states this question in almost the exact words
of this file's own title and marks it **`pending`** -- i.e., named as the required next
step, not yet executed. No other row addresses it. **0 hits** for a prior EXECUTED
audit of this specific licensing question. This file is the first attempt to resolve
it, as expected (C161 named it as a next step the same day it was written, so a
pre-existing resolution would be surprising and is not found).

## Falsifiable claim

C133's own decision.md (its exact SS9 definition of `Phi = 1_F (x) (lambda_0*w_0 +
lambda_1*w_1)`, its SS3 factor table, and its SS12 scope list), together with C132's
decision.md and the round C133 cites for `w_0,w_1` (C38, via C125's confirmation of
what C38 actually supplies), contain **no** stated constraint, gauge-fixing condition,
or normalization convention that identifies `lambda_0,lambda_1` with any computed
spectral/eigenvalue-type quantity from a differential or algebraic operator -- C133
treats them exclusively as free coordinates on an unconstrained 2-dimensional Hom-space
(the "sector" factor, dimension 2 at every rung of the symmetry ladder, never touched
by `G2`, `Spin(8)`, or `+Z3`), used only to define a bookkeeping "support convention"
for classifying nonzero patterns -- not as physical coupling constants awaiting a
value from a specific equation of motion.

## Kill criterion (mutually exclusive verdicts)

| # | fires if | consequence |
|---|---|---|
| **(a) NO-LICENSE / ILL-POSED** | Close reading of C133 SS3/SS9/SS12 (and C132, and C38 via C125) finds `lambda_0,lambda_1` are defined ONLY as free coordinates of an unconstrained Hom-space dimension count, with no textual pointer -- anywhere -- to a specific dynamical equation (Killing-spinor or otherwise) whose solution would supply their values | The "all->both via lambda-alpha identification" route is a **category error**, not a missing ingredient. Closes THIS specific sub-route of OB1 (identifying C133's moduli with C136's alpha specifically). Does **not** close OB1 in general, and does not rule out that some OTHER, as-yet-unbuilt physical coupling term could legitimately fix `lambda_0,lambda_1`'s values -- only that C136's Killing-spinor `alpha` was never a licensed candidate for doing so. |
| **(b) LICENSE EXISTS / INCOMPLETE-MACHINERY STANDS** | A normalization, gauge-fixing condition, or explicit forward-reference to a dynamical equation (Killing-spinor-type or otherwise) is found in C133, C132, or C38/C125, that identifies `lambda_0,lambda_1` with a computed quantity of that kind | `INCOMPLETE-MACHINERY` stands as C161 first framed it; the real next task becomes finding which convention picks the correct `(w0,w1)` frame pairing (C161 Section 3's four-pairing table), not auditing whether the identification itself is legitimate. State the exact license found, quoted verbatim, with file:line. |

**Falsifier for (a):** a single verbatim quotation, anywhere in C133, C132, or C38 (as
cited), that ties `lambda_0` or `lambda_1` to a solved/computed/spectral value rather
than to a bare dimension count or free coefficient. Absence of any such quotation after
a full re-read of all cited files is what would confirm (a).

**Falsifier for (b):** absence of any such quotation is also what would falsify (b) --
the two verdicts are constructed to be exhaustive and mutually exclusive over the same
evidence.

## What this round does NOT show

- Does NOT construct any new physics, run any new computation, or build a frame-
  selection principle -- pure textual/argument audit.
- Does NOT close OB1 in general -- only adjudicates whether ONE specific identification
  route (C133's lambda's = C136's alpha) was ever textually licensed.
- Does NOT reopen or re-litigate C133's or C136's own verdicts (both stand as written;
  this file only asks what C133's text licenses downstream, not whether C133's own
  arithmetic is correct -- already independently reconfirmed by two skeptic passes).
- Does NOT edit `OPEN_BLOCKERS.md`, `pearl_registry/INDEX.md`, `CLAIM_LEDGER.yaml`,
  `null_results/INDEX.md`, or run `git add`/`git commit` -- orchestrating session's job.
- Does NOT change `N_gen=3`'s CONDITIONAL status, `lambda = FREE_COUPLING_PARAMETER`,
  or `safe_for_runtime = False`.
- Does NOT solicit Tom Lawrence's Part 5.

## Verification plan

- Read all cited files in full (already done this session per Background above) and
  quote exact wording, with file:line references, for every load-bearing claim.
- No script needed -- pure textual audit. If a specific numeric claim needs
  re-verification (e.g., that C136's `alpha` really is solved from a residual and not
  fit), reuse `c136_joint_killing_spinor_check.py` via
  `importlib.util.spec_from_file_location`, do not re-type formulas. (Not expected to
  be necessary -- C161's own skeptic pass already independently reconfirmed this.)
- Recommend, at the end of `decision.md`, whether an independent context-blind skeptic
  pass is warranted before this finding is registered, per this project's convention
  (C159/C161/C162) of doing so whenever a verdict resolves an ambiguity with opposing
  practical consequences -- which this one does (ILL-POSED forecloses a
  frame-selection follow-up; INCOMPLETE-MACHINERY licenses one).
