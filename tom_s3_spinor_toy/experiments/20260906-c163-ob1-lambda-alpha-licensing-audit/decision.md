# C163 -- Decision (convergent-mode, FL Full-Ladder, pure textual/argument audit)

**Date:** 2026-09-06
**Experiment:** `20260906-c163-ob1-lambda-alpha-licensing-audit`
**Question type (EstimandOps L0):** Descriptive -- does a prior round's own text license
a specific downstream identification, or not. Explicitly **not** causal, **not**
predictive, and **not** a claim about the physical world.

## Verdict

**CORRECTED 2026-09-06, after independent context-blind skeptic pass -- see
Section 8. Original verdict box below is struck through, not deleted; the
corrected verdict follows it.**

~~```text~~
~~ILL_POSED__NO_LICENSE_FOUND_ANYWHERE_IN_C133_C132_OR_C38_VIA_C125~~
~~  __C133_SS9_LINE586_DEFINES_LAMBDA0_LAMBDA1_AS_COEFFICIENTS_OF_AN_UNCONSTRAINED~~
~~  __2DIM_HOM_SPACE_SECTOR_FACTOR_DIM2_AT_EVERY_RUNG_NEVER_TOUCHED_BY_G2_SPIN8_OR_Z3~~
~~  __LINE604_CALLS_IT_A_CONTINUUM_A_SCHUR_COMPUTATION_YIELDS_A_DIMENSION_NOT_A_FINITE_SET~~
~~  __C133_NEVER_MENTIONS_KILLING_SPINORS_TORSION_GRAVITINO_OR_ANY_FIELD_EQUATION_ANYWHERE~~
~~  __GREP_CONFIRMED_ZERO_HITS__ITS_ONLY_MISSING_INGREDIENT_LANGUAGE_IS_GENERIC~~
~~  __UNDEFINED_PARENT_ACTION_LINES_43_52_676_NEVER_POINTING_AT_A_SPECIFIC_CONSTRUCTION~~
~~  __C38_VIA_C125_LINE211_SUPPLIES_ONLY_TWO_KERNEL_LABELS_NOT_COEFFICIENTS_NOT_A_NORM~~
~~  __C132_GREPPED_ZERO_HITS_FOR_LAMBDA_0_LAMBDA_1~~
~~  __C136S_ALPHA_IS_A_DIFFERENT_TYPE_OF_OBJECT_SOLVED_FROM_A_64DIM_RESIDUAL_OF_A~~
~~  __SPECIFIC_JOINT_KILLING_SPINOR_SYSTEM_C133_NEVER_CONSTRUCTS_OR_CITES~~
~~  __CLOSES_ONLY_THIS_SPECIFIC_SUBROUTE_OF_OB1_NOT_OB1_ITSELF__SEE_SECTION_5~~
~~  __SKEPTIC_PASS_RECOMMENDED_BEFORE_REGISTRY_ENTRY__SEE_SECTION_6~~
~~```~~

**Corrected verdict:**

```text
NO_LICENSE_FOUND__IN_THE_ROUNDS_ACTUALLY_CHECKED__C133_C132_C38_VIA_C125
  __NOT_SETTLED_WHETHER_UNLICENSABLE_IN_PRINCIPLE_OR_MERELY_UNLICENSED_SO_FAR
  __SKEPTIC_CORRECTION_THE_TWO_PREMISES_ARE_NOT_FULLY_INDEPENDENT__SEE_SECTION_8
  __FREE_2PARAM_CONTINUUM_LANGUAGE_IS_NEUTRAL_TOWARD_FUTURE_DYNAMICAL_FIXING_NOT_A_DENIAL_OF_IT
  __ALPHA_IS_ALSO_A_FREE_MODULUS_AT_AN_EARLIER_STAGE_BEFORE_SOLVE_CELL_PINS_IT
  __DIFFERENCE_IS_DEGREE_OF_CONSTRAINT_APPLIED_NOT_A_CATEGORICAL_OBJECT_KIND_MISMATCH
  __C132_SYNONYM_GREP_RUN_BY_ORCHESTRATING_SESSION_ALSO_ZERO_HITS__GAP_CLOSED
  __PRACTICAL_CONCLUSION_UNCHANGED_DO_NOT_BUILD_A_FRAME_SELECTION_RULE_ON_THIS
  __RECOMBINATION_WITHOUT_AN_EXPLICIT_LICENSE__BUT_ILL_POSED_WAS_TOO_STRONG_A_WORD
  __CLOSES_ONLY_THIS_SPECIFIC_SUBROUTE_OF_OB1_NOT_OB1_ITSELF__SEE_SECTION_5
```

**One line (corrected).** No license for identifying `lambda_0,lambda_1` with
C136's `alpha` was found in C133, C132, or C38 (via C125) -- neither under the
literal notation nor, per the orchestrating session's follow-up grep, under
plausible synonyms ("coupling coefficient", "mixing constant", "modulus",
`w_0`/`w_1`/"sector space") in C132. **The original "ILL-POSED / category
error" framing overclaimed**, per the independent skeptic pass (Section 8):
the "free 2-parameter continuum" language (line 604) is neutral toward future
dynamical fixing, not a denial of it (standard physics usage: "free until the
Lagrangian is written down"), and C136's own `alpha` is itself a free modulus
of `A=diag(0,alpha*1_3,beta*1_6)` at an earlier stage, only pinned by a later,
additional constraint (`solve_cell`'s residual-vanishing) -- so the asymmetry
between `lambda_0,lambda_1` and `alpha` is a difference in how much
constraint has been APPLIED so far, not a categorical mismatch of object
kind. **The practical, actionable conclusion is unchanged**: no license
currently exists for this specific recombination, so a frame-selection round
should not be built on it without first supplying one -- but the honest
verdict is `NO-LICENSE-FOUND` (in the rounds actually checked), not the
stronger `ILL-POSED`, and whether the identification is unlicensable IN
PRINCIPLE remains genuinely open.

---

## 1. What the entity actually is: exact quotation, not paraphrase

C133's `decision.md` line 586, Section 9 ("What the reduction actually is, stated
precisely"):

> "At rung 3 the coupling is `Φ = 1_F ⊗ (λ₀ w₀ + λ₁ w₁)`, with `w₀, w₁` spanning the
> two `S³` `t`-sectors [`[CITED]`, C38]."

Immediately followed (lines ~601-605), the load-bearing sentence:

> "So 'the pairing-rule space is exactly `{all→t=0, all→t=1, all→both}`' is precise
> only as: the set of nonzero SUPPORT PATTERNS of a channel-uniform coupling has
> exactly three elements. **The coupling space is a 2-parameter continuum**; a Schur
> computation yields a dimension, not a finite set, unless a support convention is
> imposed on top -- and one is."

And the SS3 factor table (line 595-599), which fixes what "sector" means at every rung:

| rung | channel | fibre | sector | total parameters |
|---|---|---|---|---|
| 1 (`G2`) | 9 | 2 | **2** | 36 |
| 2 (`Spin(8)`) | 3 | 1 | **2** | 6 |
| 3 (`+Z3`) | 1 | 1 | **2** | 2 |

**Reading, stated plainly.** The "sector" column -- `dim W`, spanned by `w₀,w₁` -- is
`2` at every single rung of the ladder, `G2`, `Spin(8)`, and `+Z3` alike. None of the
three symmetry groups this round's entire argument is built around ever acts on `W` at
all: line 141 states this explicitly, "[every rung]... acts **trivially on `W`**, so the
whole constraint falls on `End_G(F)`" -- i.e. the whole 9->3->1 ladder is a statement
about the CHANNEL factor exclusively. `lambda_0,lambda_1` are therefore never subjected
to a Schur-lemma computation of any kind (unlike the channel factor's `9`, `3`, `1`,
each obtained by an explicit solve, per SS13a); they are bare coordinates on a
2-dimensional vector space whose dimension is asserted (cited to C38), not derived.
"A Schur computation yields a dimension, not a finite set" (line 604) refers to the
**channel** dimension count that produces `9/3/1` -- carried over by loose phrasing to
describe the whole rung-3 coupling, but the sentence's own subject, read exactly, is
about turning a dimension into a finite set of *support patterns*, which is a labeling
operation on the free coefficients, not a computation *of* their values.

**This is the same reading C161's own independent skeptic pass (Section 9) reached**,
now confirmed by re-reading the primary text directly rather than through C161's
paraphrase: `lambda_0,lambda_1` are "free moduli of an abstract `Hom`-space dimension
count," "never spectral outputs of any operator."

---

## 2. Is there ANY license, anywhere, tying lambda_0/lambda_1 to a computed quantity?

Searched exhaustively, this session, by direct grep of the primary files (not by
memory or by trusting C161's own characterization):

**C133's decision.md, full text (916 lines), grepped for `Killing`, `gravitino`,
`torsion`, `parent action`, `equation of motion`, `dynamically`, `field equation`:**
zero hits for the first five terms. `parent action` appears exactly SIX times
(lines 43, 52, 480, 623, 666, 676) -- **correction, orchestrating session,
2026-09-06:** this file originally undercounted (three), missing lines 480, 623,
666; re-grepped directly and confirmed six. This does not change the finding --
lines 480 (a verbatim quote of C132's own "triality-symmetric parent action"),
623 ("No mechanism, no parent action..."), and 666 (a pearl-registry-style row,
"any round assuming a triality-symmetric parent action") are all the SAME
generic disclaimer/citation pattern as the other three, none of them pointing at
a specific dynamical equation either. Every occurrence is the SAME generic
disclaimer:

> "No gate field is passed; this round supplies no parent action." (line 43)
> "Does **not** supply, derive, or verify any parent action." (lines 52, 676)

None of the three occurrences names, describes, or points at ANY specific
construction -- Killing-spinor-based or otherwise -- as the thing that would eventually
fix `lambda_0,lambda_1`'s values. "Parent action" here is a placeholder for "whatever
future physical Lagrangian would exist," used identically throughout this project's
other C1xx rounds (C132, C136, C161 all use the same generic phrase) to mean "we have
not built a Lagrangian, so we make no claim about dynamically-fixed values" -- it is
not a forward-reference to a specific equation, and specifically never to a
generalized/torsionful Killing-spinor constraint of the kind C136 builds.

**C132's decision.md**, the round C133's own claim.md says this file was "built
directly from" (its Sketch A): grepped this session for `lambda_0`, `lambda_1`,
`λ₀`, `λ_0`, `λ0`, `λ_1`, `λ1` -- **zero hits**. C132 never mentions these symbols at
all; they are introduced for the first time in C133 itself.

**C38 (cited by C133 line 586 for `w0,w1` "spanning the two S3 t-sectors"):** no
experiment folder named `c38` exists (checked via `find`/`ls`); "C38" is this
project's internal round-label from the 2026-08-10 session, referenced by later
rounds. C125's `decision.md` line 211 states directly what C38 actually supplies:
"C125 cited C38 only for the two kernel labels" -- i.e., `ker(t=0)=(1,2)`,
`ker(t=1)=(2,1)` (confirmed at `.claude/checkpoints/20260810_c37-c42-frontier-
narrowed.md:15` and `.claude/memory/history/activeContext-archive-2026-09-04.md:3206`).
**C38 supplies labels for which representation realizes each `t`-sector -- it supplies
no coefficients, no normalization, and no computation of any kind.** It cannot be the
source of a license either.

**Conclusion of the search: there is no license, anywhere in the cited chain (C133,
C132, C38/C125), for identifying `lambda_0,lambda_1` with any computed spectral
quantity from any specific operator.** This is not merely "C133 doesn't happen to
mention C136 by name" (C136 postdates C133 by the same session, so it could not) --
it is that C133 never frames `lambda_0,lambda_1` as the kind of object a differential
or algebraic operator would produce, under ANY named future construction, Killing-
spinor-based or otherwise.

---

## 3. What kind of object C136's `alpha` actually is, confirmed by direct re-read

`experiments/20260902-c136-joint-killing-spinor-constraint/decision.md`, Section 4
(the `A = diag(0₄, α1₃, β1₆)` reading), and Section 5 header, quoted exactly:

> "## 5. The `3×2` table (reading (ii); `α` **solved from the 64-dim residual**)"

and, in the kill-branch discussion:

> "`solve_cell` solves for `α` from the residual, so `χ₆` reaches the cell content"

`α` is the output of solving a specific linear/residual system derived from the
decomposed generalized-Killing-spinor equation on `M4 x S3 x S6` -- an eigenvalue-like
quantity of a named, constructed differential operator, computed by a script
(`c136_joint_killing_spinor_check.py:640-675`, `solve_cell`), independently
re-confirmed by C161's own reproduction (checks `1a/1b`, `2a/2b`) and by C161's
skeptic pass.

**This is categorically different from `lambda_0,lambda_1`** as C133 defines them:
one is a solved output of a specific equation; the other is an unconstrained
coordinate on a bare 2-dimensional vector space that no equation in this project's
record was ever pointed at. The type mismatch C161's skeptic flagged is confirmed,
not merely plausible, by this direct re-read of both primary sources.

---

## 4. Addressing the charitable counter-reading directly

**Could "free" in C133 just mean "not fixed by symmetry, but fixable by ANY future
dynamics" -- making the INCOMPLETE-MACHINERY reading still viable in principle, even if
C136 specifically was never named?** This is the strongest version of the
INCOMPLETE-MACHINERY reading and deserves a direct answer, not a dismissal.

**Answer: this weaker, more charitable reading is available in the abstract (a
physicist could reasonably say "any coupling has free coefficients until the
Lagrangian is written down"), but it still does not license C161's SPECIFIC
recombination.** Even granting that `lambda_0,lambda_1` are, in the abstract, the kind
of quantity SOME future dynamical equation might fix, C133's text gives no pointer --
none, anywhere, per the exhaustive grep in Section 2 -- to that equation being a
Killing-spinor constraint, let alone specifically C136's construction. Licensing
`lambda_i := alpha(t_i, frame_i)` requires TWO things: (i) that `lambda_0,lambda_1` are
the kind of object a dynamical equation fixes at all, and (ii) that THE SPECIFIC
equation is a generalized Killing-spinor constraint of C136's kind. C133 supplies
textual support for neither -- (i) is actively contradicted by the "free 2-parameter
continuum"/"Hom-space dimension count" framing (Section 1), and (ii) has zero support
under any reading (Section 2's grep). **Both premises failing independently is why
this file's verdict is ILL-POSED rather than the milder "under-specified": the
identification fails on two separate grounds, not one ambiguous one.**

This also directly answers C161 Section 9's own open question ("this file does not
adjudicate between the two [readings]") -- the adjudication is: ILL-POSED, on textual
grounds stronger than the single clause C161's skeptic pass had time to weigh, because
this file additionally checked (Section 2) whether ANY dynamical-equation pointer
exists in C133 at all, not only whether the "free continuum" language is present.

---

## 5. Scope, stated precisely (what this DOES and does NOT close)

**Closes:** the specific claim, made operational in C161's claim.md Intervention
section ("Extend... C136's existing script to compute the actual `(lambda_0,
lambda_1)` coefficients the joint constraint's solution set implies"), that C136's
already-computed `alpha` table is a legitimate source of values for C133's
`lambda_0,lambda_1`. That specific recombination is a category error: C136's `alpha`
was never a candidate for filling in C133's moduli, because C133 never treats those
moduli as fillable by ANY named spectral computation, Killing-spinor-based or
otherwise.

**Does NOT close:**
- **OB1 in general.** OB1's question -- does some `t`-selector exist -- remains open.
  Untried Relaxation Map candidates from C132's own ranking (`P4`, `P13`, `P8`, `P1`,
  `P6`, `P7`, `P10`, `P12`) are untouched by this finding.
- **Whether `lambda_0,lambda_1` could ever be legitimately fixed by SOME other,
  as-yet-unbuilt physical coupling term.** This file finds no license for C136's
  SPECIFIC construction, not a proof that no construction could ever supply values.
  A future round proposing a genuinely new coupling-term construction (not a
  recombination of two already-built, differently-typed artifacts) is not foreclosed.
- **C133's or C136's own arithmetic or verdicts.** Both stand exactly as written,
  including their own skeptic-confirmed evidence tiers. This file only audits what
  C133's text licenses for DOWNSTREAM use, not whether C133's internal computation is
  correct.
- **C161's own four-pairing table (Section 3 of its decision.md).** That table remains
  a correct, independently-reconfirmed computation of what C136's SS5 data literally
  contains; this file's finding is that USING that table to fill C133's `lambda`'s was
  never licensed, not that the table itself is wrong.
- Does not change `N_gen=3`'s CONDITIONAL status, `lambda = FREE_COUPLING_PARAMETER`,
  or `safe_for_runtime = False`.
- Does not solicit Tom Lawrence's Part 5.

### Relaxation Map (one assumption changed per variant; none attempted here)

| Variant | Single assumption changed | Status |
|---|---|---|
| **R1** | A future round proposes a genuinely NEW coupling-term construction (not a recombination of C133+C136) whose coefficients are `lambda_0,lambda_1` by explicit, stated construction | Not foreclosed by this file -- would need its own claim.md, estimand, and license check from scratch, since this file's finding is specific to the C133+C136 recombination |
| **R2** | Someone amends C133's own `decision.md` to explicitly name a specific dynamical equation (Killing-spinor or otherwise) as the intended source of `lambda_0,lambda_1`'s eventual values | Would retroactively supply the missing license -- but this is authoring NEW content into C133, not reading an existing one; out of scope here (this file audits, does not amend, prior rounds) |
| **R3** | Treat "free parameter, fixed by symmetry to zero" as itself informative (i.e., ask whether C133's own ladder, at some FOURTH, stronger symmetry rung, might eventually constrain `dim W` below 2) | Not attempted -- C133 Section 6 Relaxation Map V5 already names "let `W` carry a non-trivial action of the assumed symmetry" as its own untried variant; this file does not re-open it |

---

## 6. Kill Analysis (Anti-Overfitting Gate)

**What this round KILLS.** The specific framing, present in C161's claim.md
Intervention section and left unresolved by C161's own decision.md, that identifying
C133's `lambda_0,lambda_1` with C136's `alpha` is merely "underdetermined" (a missing
selection rule away from being valid). **Killed and replaced with:** the identification
was never licensed in the first place, on two independent grounds (Section 4) -- this
is a stronger, more specific finding than "underdetermined."

**What this round does NOT kill.** Nothing about the physical world; no candidate
mechanism (`P2`, `P3`, `P4`, `P5`, `P13`, `P14`, etc.) is newly ruled in or out.
`all->both`'s status as "assumed, not derived" (C133 SS8a) is unchanged -- if anything,
narrowed further: it was never even partially derivable via this specific route.
C161's own arithmetic (Sections 1-6 of its decision.md) is fully preserved; only the
INTERPRETIVE conclusion drawn from that arithmetic is corrected.

---

## 7. Recommendation on an independent skeptic pass

**Yes, warranted, before this finding is written into `pearl_registry/INDEX.md` or
cited elsewhere.** Reasoning, per this project's stated convention (C159/C161/C162):
this verdict resolves an ambiguity C161 explicitly left open (ILL-POSED vs.
INCOMPLETE-MACHINERY), and the two readings license opposite follow-up actions --
exactly the "opposing practical consequences" trigger condition this project's own
convention names. Specifically worth an adversarial check: whether Section 4's
two-premises argument (that BOTH "lambda's are fixable at all" and "the fixing
equation is Killing-spinor-shaped" fail independently) is actually as airtight as
presented, or whether a differently-worded reading of C133's generic "parent action"
language could be read as implicitly gesturing at exactly this class of construction
in a way this file's grep-based method would miss (grep catches literal absence of
keywords, not absence of intent). A context-blind pass given only this file's claim.md
+ decision.md + the exact C133/C136 quotations above (no session history) would be the
correct scope, per this project's Context Asymmetry Rule.

---

## Check

* Every quotation above is reproduced verbatim from the cited file, with a line number,
  confirmed by direct `Read`/`Grep` this session -- none taken from C161's own
  paraphrase or from memory.
* The `parent action`/`Killing`/`gravitino`/`torsion`/`equation of motion`/
  `dynamically`/`field equation` grep against C133's full decision.md was run this
  session and its exact hit count (0 for the first five terms, 3 for "parent action")
  is reported above, not estimated.
* The `lambda_0`/`lambda_1` grep against C132's decision.md was run this session
  (0 hits), not assumed from C133's claim.md framing alone.
* C38's actual content was confirmed via C125's `decision.md:211` and two independent
  `.claude/` memory files, not taken on C133's citation alone.
* No code was written or run -- pure textual audit, consistent with this file's own
  claim.md Verification plan (no script needed unless a numeric re-check was required;
  none was, since C161's own skeptic pass already independently reconfirmed C136's
  `alpha`-as-residual-solution characterization).

---

## Evidence tier of the central conclusion

**Central conclusion:** *No reading of C133's own text, nor C132's, nor C38's (via
C125), licenses identifying `lambda_0,lambda_1` with C136's computed `alpha` -- the
identification is a category error (free Hom-space coordinate vs. computed spectral
output), not a missing selection principle.*

**Tier: `[VERIFIED-tool]` for the textual/grep facts** (zero hits for the five
dynamical-equation keywords in C133; zero hits for `lambda_0/lambda_1` in C132; C38's
content confirmed via C125) -- all directly reproducible by re-running the same greps.

**Tier: `[INFERRED]`, HIGH confidence, for the ILL-POSED verdict itself** -- chain: C133
defines `lambda_0,lambda_1` exclusively as Hom-space coordinates (verified quotation)
-> C133 never points at any dynamical equation as their source (verified grep) ->
C136's `alpha` is a solved spectral output of a specific, differently-motivated
equation (verified quotation) -> therefore no license exists for the identification.
Each link is independently verified; the chain itself is the inference, and is why a
skeptic pass (Section 7) is recommended before this enters the permanent registry
record, even though the underlying textual facts are `[VERIFIED-tool]`.

**Marker on the whole round:** this is an audit finding, not a promoted physical claim.
No PROMOTE/REJECT/ARCHIVE registry action is proposed; the orchestrating session
decides whether/how to update `pearl_registry/INDEX.md`'s C161 row (2026-09-06) to
reflect this resolution.

---

## 8. Update -- independent context-blind skeptic pass (orchestrating session,
   2026-09-06), verdict WEAKENED, Skeptic Response Matrix applied

Per Section 7's own recommendation, ran an independent `Agent(skeptic)` pass:
this file's claim.md + decision.md + the exact C133/C136/C161 quotations, no
session history. **Verdict: `WEAKENED`** -- the core no-license finding
survives, but the `ILL-POSED`/"category error" framing overclaimed.

**Concern 1 -- the two premises (Section 4) are not fully independent, and
"free 2-parameter continuum" is neutral toward future dynamical fixing, not a
denial of it.** **Accepted, fixed.** The verdict box and one-line summary
above are corrected: the practical conclusion (no license currently exists)
stands, but is no longer framed as two independently-failing grounds, and no
longer claims the continuum language itself rules out future fixing.

**Concern 2 -- does grep-based absence of keywords actually establish "no
implicit pointer", or could a human reading in full context find one grep
misses?** **Checked directly by the skeptic itself, independently, and
confirmed: no implicit pointer found** ("No sentence I found gestures at a
Killing-spinor-type equation, even implicitly"). This concern, on
investigation, SUPPORTS the audit's original finding rather than weakening it
-- **dismissed as a live weakness**, kept in the record because the skeptic's
own independent re-derivation (not merely trusting the grep) is itself
stronger evidence than the grep alone, and is worth preserving as such.

**Concern 3 -- is `alpha` really an unambiguous "computed spectral output",
or itself partly a free modulus?** **Accepted, fixed.** Confirmed by
independent re-reading of C136 Section 4 (`A=diag(0,alpha*1_3,beta*1_6)`,
"alpha free ⇒ every t solves (E4)") vs Section 5 (`solve_cell` pins alpha
per-cell via residual-vanishing): `alpha` starts as a free modulus of `A`,
identically in KIND to `lambda_0,lambda_1`'s own status, and is pinned only
by an ADDITIONAL constraint C133 never imposes on its own sector factor. The
type-mismatch claim is corrected from "categorical" to "degree of applied
constraint" in the verdict box above.

**Concern 4 -- C132 was only grepped for literal `lambda_0/lambda_1`
notation, not synonyms ("coupling coefficient", "mixing constant",
"modulus", `w_0`/`w_1`).** **Checked directly by the orchestrating session
(not left open):** re-grepped C132's `decision.md` (`experiments/
20260902-c132-13d-parent-action-survey/decision.md`) for `coupling
coefficient`, `mixing constant`, `moduli`, `modulus`, `coupling constant`,
`hom.space`, `w_0`, `w_1`, `w0`, `w1`, `t-sector`, `sector space` -- **one
incidental hit** (`t` called a "4D modulus" in an unrelated `V(t)` scalar-
potential mechanism, Section on 4D moduli stabilization, not the `S3`
`t`-sector coupling object at all) and otherwise **zero hits** for every
sector-space-related term. **Gap closed: C132 does not discuss this object
under any notation checked, literal or synonymous.**

**Concern 5 -- `ILL-POSED`/"category error" is stronger wording than the
evidence supports; the honest verdict is `NO-LICENSE-FOUND` (as checked),
leaving open whether the identification is unlicensable in principle.**
**Accepted, fixed** -- this is the central correction applied throughout the
Verdict section above. `ILL-POSED` (which this project's own vocabulary
reserves for "nothing to select, category error") is downgraded to
`NO-LICENSE-FOUND`, an intentionally narrower claim: no license currently
exists in the rounds actually checked, full stop, with the stronger
in-principle question left explicitly open.

**Net effect on downstream action: unchanged.** Do not build a frame-
selection round on the C133+C136 recombination without first supplying an
explicit license (a genuinely new construction naming its coefficients
`lambda_0,lambda_1` from the start, per Relaxation Map variant R1, Section 5
above, is not foreclosed). The correction is entirely in how strongly the
negative finding is stated, not in what follow-up work it permits or
forecloses.
