# C129 decision -- does the non-orientable mapping torus admit a `Pin` structure?
# (C128's Relaxation Map item Y1 = the re-specified form of C127's X6.)
#
# HEADLINE: **BOTH. `Pin^+` AND `Pin^-` both exist** -- on `M_ι` and on the
# mapping torus of EVERY map that could relate `∇⁰` to `∇¹`. `claim.md`
# explicitly permitted `BLOCKED`; the permission is **not exercised**, because
# the Stiefel-Whitney classes turned out to be computable outright:
#
#   `H²(M_f; 𝔽₂) = 0` for every self-map `f` of `S³`. Both `w₂` and `w₁²` live
#   in that group, so **both vanish for dimension reasons** -- not by
#   cancellation, not by a coincidence, and not by a choice. Both Pin
#   conditions hold because the group they live in is zero. There are
#   **exactly two structures of each type** (torsor over `H¹(M;𝔽₂) = ℤ/2`).
#
# `w₁ ≠ 0` (the manifold IS non-orientable, confirming C128 §6b by an
# independent route), so there is **no Spin structure** -- `Ω^{Spin}` really is
# the wrong functor, as C128 said.
#
# ⚠️ **SEPARATE FINDING, AND THE ONE MOST LIKELY TO MATTER LATER: `claim.md`
# lines 56-57 and C128 §6c HAVE THE TWO PIN CONDITIONS SWAPPED.** Kirby-Taylor,
# now read DIRECTLY (§2a): **`Pin^+` exists iff `w₂ = 0`; `Pin^-` exists iff
# `w₂ + w₁² = 0`.** **Harmless for THIS round's verdict** (both conditions
# hold, so both structures exist either way) -- and **load-bearing for the next
# one**, since `Ω^{Pin^+}_4 = ℤ/16` and `Ω^{Pin^-}_4 = 0` are drastically
# different and reading the label backwards would invert an anomaly conclusion.
# **C128 is internally inconsistent on this**: its Completeness item 4 (line 75)
# has it RIGHT, its §6c (line 475) has it BACKWARDS, and `claim.md` inherited
# the wrong half.
#
# NOT covered: any bordism group as evidence for this round's answer; which Pin
# type the FERMION CONTENT requires (round95, C127's ingredient 2, untouched);
# whether the TWISTED structure the anomaly actually needs exists (§7d -- the
# bare tangential question is what `claim.md` asked and what is answered); any
# 13D statement (`M₄` non-compact); `N_gen=3`; Tom Lawrence's Part 5.

**Verdict (2026-09-02; TWO independent FL Step 8a skeptic passes run,
context-blind, differently-worded -- Paraphrase-Sensitivity Probe. Both
returned the same split: the MATHEMATICS `CONFIRMED-REAL`, the EVIDENCE
APPARATUS `WEAKENED`. CONCORDANT. 26 findings; all answered, 6 code defects
repaired):**
`BOTH_PIN_PLUS_AND_PIN_MINUS_EXIST_ON_THE_BARE_TANGENTIAL_STRUCTURE_OF_THE_MAPPING_TORUS_OF_EVERY_CANDIDATE_RELATING_MAP__H2_OF_M_iota_WITH_F2_COEFFICIENTS_IS_ZERO_CONFIRMED_BY_FOUR_ROUTES_MINIMAL_CW_CELL_COUNT_AND_WANG_WHICH_ARE_THE_SAME_ALGEBRA_PLUS_TWO_GENUINELY_INDEPENDENT_ONES_pi1_PLUS_EULER_PLUS_POINCARE_DUALITY_AND_A_NON_MINIMAL_CW_MODEL_WITH_TWO_2_CELLS_WHERE_H2_IS_A_COMPUTED_RANK_NOT_A_CELL_COUNT__HENCE_w2_AND_w1_SQUARED_BOTH_VANISH_FOR_DIMENSION_REASONS_AND_BOTH_PIN_CONDITIONS_HOLD_SIMULTANEOUSLY_WITH_EXACTLY_TWO_STRUCTURES_OF_EACH_TYPE__w1_IS_NONZERO_BECAUSE_det_M_iota_EQUALS_MINUS_ONE_SO_THE_MANIFOLD_IS_NON_ORIENTABLE_AND_HAS_NO_SPIN_STRUCTURE__SECOND_INDEPENDENT_CONSTRUCTIVE_ROUTE_M_f_IS_S3_TIMES_R_QUOTIENTED_BY_A_FREE_Z_AND_CRUCIALLY_S3_TIMES_R_IS_PARALLELIZABLE_SO_THE_PIN_BUNDLE_UPSTAIRS_IS_TRIVIAL_AND_BECAUSE_Z_IS_FREE_ON_ONE_GENERATOR_A_PIN_STRUCTURE_IS_MERELY_A_LIFT_OF_THE_SINGLE_MONODROMY_MAP_WHICH_ALWAYS_EXISTS_BECAUSE_S3_IS_SIMPLY_CONNECTED__PARALLELIZABILITY_IS_LOAD_BEARING_WITHOUT_IT_CP2_TIMES_S1_SATISFIES_EVERY_OTHER_PREMISE_AND_ADMITS_NEITHER_STRUCTURE__EXPLICIT_LIFT_omega_TIMES_SPIN_ELEMENT_EXHIBITED_IN_BOTH_CLIFFORD_SIGNATURES_AND_BRIDGED_FROM_Cl3_TO_Cl4_WHERE_omega3_ANTICOMMUTES_WITH_e4_SO_THE_FIRST_DRAFTS_CENTRALITY_REASON_WAS_WRONG_THOUGH_THE_LIFT_IS_RIGHT__ANSWER_INDEPENDENT_OF_WHICH_RELATING_MAP_TWICE_OVER_THE_COMPUTATION_USES_ONLY_deg_f_MOD_2_AND_BY_CITED_CERF_ALL_ORIENTATION_REVERSING_DIFFEOS_OF_S3_ARE_ISOTOPIC__iota_IS_INDEED_SPECIAL_AN_INVOLUTION_WITH_ORIENTATION_DOUBLE_COVER_S3_TIMES_S1_BUT_THE_GENERIC_COSET_REPRESENTATIVE_IS_NOT_AN_INVOLUTION_AND_GIVES_THE_SAME_ANSWER__SEPARATE_FINDING_claim_md_AND_C128_SECTION_6c_HAVE_THE_TWO_PIN_EXISTENCE_CRITERIA_SWAPPED_RELATIVE_TO_KIRBY_TAYLOR_NOW_READ_AS_PRIMARY_PIN_PLUS_IFF_w2_ZERO_AND_PIN_MINUS_IFF_w2_PLUS_w1_SQUARED_ZERO_AND_C128_STATES_IT_BOTH_WAYS_IN_ONE_FILE__HARMLESS_HERE_LOAD_BEARING_DOWNSTREAM__Y1s_STRUCTURE_EXISTENCE_HALF_IS_CLOSED_FOR_THE_BARE_TANGENTIAL_STRUCTURE_ONLY_ITS_ANOMALY_HALF_REMAINS_BLOCKED_ON_INGREDIENT_2_ROUND95_AND_THE_TWISTED_STRUCTURE_QUESTION_IS_UNTOUCHED`

**Status:** OB1 stays `PARKED`. No reopen condition met. C125's `FALSIFIED`,
C126's `WEAKENED`, C127's `BLOCKED`, C128's `OUTCOME_B` all stand, untouched;
C128 §6b is **confirmed** by an independent route. **C128's Relaxation Map item
Y1 is CLOSED in its first half** ("first check the structure EXISTS") **for the
BARE TANGENTIAL structure**. **Y1's second half** ("then does the anomaly force
the pair?") is **still BLOCKED on C127's ingredient 2 (round95)**, and the
**twisted**-structure question (§7d) is newly named and `[UNKNOWN]`. So X6/A2
moves from *blocked on two things* to *blocked on one, plus one newly named
cheap prerequisite*.

**Completeness:** `PARTIAL`, in six named respects.
1. The question answered is the **bare tangential** one `claim.md` posed.
   Whether the **twisted** structure a Dai-Freed argument needs
   (`Pin^± ×_{ℤ₂} G`) exists is a **different** question with a different
   condition, `[UNKNOWN]` -- §7d. C127's own skeptic finding 1 made exactly
   this point for `Spin`; it applies verbatim and is not waved away.
2. Everything is at the **`S³` level**. As frozen, `M₄` is non-compact (C127
   §3, C128 §6 preamble), so no 13D mapping torus is a closed manifold.
3. No bordism group is used as evidence for this round's answer. `Ω^{Pin^±}_4`
   appears in §2c **only** to retire C128's dangling `[MEMORY, unverified]`
   tag; using it for existence would be `claim.md`'s kill criterion (b).
4. **No literature source was found stating this specific result.** Searches
   were run (§2b). The computation is elementary and is very likely folklore;
   **no novelty is claimed.**
5. `π₀(Diff(S³)) = ℤ₂` (§7b) is `[CITED]` (Cerf/Hatcher), **not** re-derived.
   The answer does not depend on it -- §7a is independent and stronger.
6. **Both skeptic passes ran without an execution tool** (Read-only; `Write`
   denied by a scope guard). Every check they report is hand derivation against
   the committed JSON. Per the Substrate Gate that is a fact about their
   substrate, not evidence about the claim -- and here it is a **strength**:
   both re-derived `H_*(M_ι)` from scratch, independently of this round's code.
   They could not re-run the scripts, so "the JSONs match the code as
   committed" is `[UNVERIFIED]` **by them**; it is verified here by re-running.

**Gate fields assessed:** `PARENT_ACTION_GATE.md` **F4**, and only by removing
an obstruction from a route -- **no mechanism supplied**. F1/F2/F3/F5 reused by
citation. F6, F7 not assessed.

---

## 0. ⚠️ TWO FL Step 8a skeptic passes -- both split MATH-CONFIRMED / RECORD-WEAKENED

Both context-blind (`Agent(skeptic, model=opus)`, `claim.md` + `decision.md` +
both scripts + both JSONs only; no session history, no reasoning chain). Run
**twice with differently-worded falsification prompts** (formal register vs.
plain-language register) per the Paraphrase-Sensitivity Probe, because this
round closes a live Relaxation Map item.

> **Pass 1 verdict:** *"`CONFIRMED-REAL` on the central claim ... survived every
> attack I could mount, including one independent test the round itself did not
> run. `WEAKENED` on three surrounding claims."* Attacks (a) topology, (b)
> criterion, (c) bundle, (d) constructive route: **all FAILED**. (e) gate/code
> and (f) scope: **partially succeeded**.
>
> **Pass 2 verdict:** *"`WEAKENED` -- attached to `decision.md` as an
> evidentiary record, not to its mathematics. The mathematical headline itself
> is `CONFIRMED-REAL`. I attacked it three ways and could not move it, and it
> survives withdrawal of any single citation because §4 and §6 have disjoint
> citation sets."*

**Concordant**, so the single-run Response Matrix applies and no skeptic-leaning
tie-breaker is needed. They found **substantially different** defects, which is
itself the argument for running two. **Six were real CODE defects and are
repaired; the rest are repaired in the text below. Nothing is waved through.**

### Findings both passes made independently (strongest signal)

| # | Finding | Response |
|---|---|---|
| **A1** | **`Pin_minus` was a CONSTANT.** The call was `pin_verdict(H2F2_zero, H2F2_zero)` and the body tested `w2_zero == w1_sq_zero` -- the same object twice, i.e. `x == x == True`. **Half the headline was not computed by the code that claimed to compute it.** Worse, `w2_zero == w1_sq_zero` is not `w₂ = w₁²` at all: it only says "both vanish or both don't", strictly weaker once `dim H² ≥ 2`. Pass 1 supplied the counterexample: `ℝP²×ℝP²` has `w₂+w₁² = ab ≠ 0` and `w₂ ≠ 0`, so **neither** structure exists, but the boolean version returns `Pin_minus = True`. | **ACCEPTED, real defect, REPAIRED.** `pin_verdict` now takes **classes**, not booleans, and tests `w₂ = 0` / `w₂+w₁² = 0` by expansion in `𝔽₂`. `ℝP²×ℝP²` is now a gate check (`G25b`/`G25c`) and returns **neither**. The `M_ι` call now passes **two independently derived** quantities (`w₂` from `H²(M)=0`; `w₁²` from `π^*(a²)`, `a² ∈ H²(S¹;𝔽₂) = 0` -- a route that does not use PART 3 at all). Restoring the boolean form is now injection 8. |
| **A2** | **`G31` (χ=0) is a tautology.** `Σ(−1)ⁿ(C[n−1]+C[n])` telescopes to 0 for **any** input complex, and the Betti version inherits it by rank-nullity **even if `_rank_f2` is completely broken**. `G32` (palindrome) is near-vacuous for the same reason. | **ACCEPTED, repaired.** Both renamed `G31_IDENTITY_...` / `G32_IDENTITY_...` with the derivation in a comment, so no future reader counts them as evidence. |
| **A3** | **§4's "Neither is automatic from the construction ... injection 3 breaks them" is FALSE, and is contradicted by the round's own JSON**: `results_c129_injections.json` shows injection 3 fired `G18,G19,G21,G36,G37` -- **not** `G31`/`G32`. `G32` fired under **zero** of the five injections. | **ACCEPTED, real defect, sentence DELETED** and replaced by the honest statement (§4). A false claim about one's own artifact, sitting next to the artifact, is exactly the species this project polices. |
| **A4** | **No injection could move a headline quantity.** All five left every `VERDICT_INPUTS` field byte-identical. The suite showed the gate *can* fail, never that it *guards the conclusion*. Root cause: `M_ι`'s minimal CW model has **no 2-cells**, so `H₂ = 0` survives any corruption of the linear algebra. | **ACCEPTED, the most consequential process finding, REPAIRED.** Both passes independently proposed the same fix: **run the same manifold from a NON-MINIMAL CW model with `C₂ ≠ 0`**, where `H₂ = 0` is a computed rank. Implemented (`s3_nonminimal_complex`, `C = [1,1,1,1]`, `∂₂ = (1)`); the mapping torus then has **two** 2-cells and needs two genuine `𝔽₂` rank computations. **Two injections now MOVE the headline** (§11). |
| **A5** | **The `d`-handling branches of `mapping_torus_complex` were never exercised** -- `sphere_complex` never populates `d`, so every case ran with zero boundary matrices. Pass 1 gave the uncaught injection explicitly (`M[t_a+i, a_dim+j] = 0` → 38/38, `ALL_OK=True`). | **ACCEPTED, real C128-A1-species hole, REPAIRED** by the same non-minimal model, which has `∂₂ ≠ 0`. That exact injection is now **injection 6, is caught, and moves the headline.** |
| **A6** | **§6's "ω is central in odd dimension" is FALSE in `Cl(4)`**, and the structure group of a 4-manifold is `O(4)`/`Pin^±(4)`: `ω = e₁e₂e₃` **anti**commutes with `e₄`. The Cl(3)→Cl(4) bridging step is unstated and unchecked. Both passes independently supplied it: `ω` is odd, so `ρ̃(ω)e₄ = −(ωe₄ω^{-1}) = +e₄`, giving `ρ̃(ω) = diag(−1,−1,−1,+1)` and `ρ̃(ωS(x)) = (−Ad(x)) ⊕ 1` -- **the conclusion holds, the stated reason does not.** | **ACCEPTED, repaired and now COMPUTED** (`P5_Cl4_bridge`, gates `G30a`-`G30e`), with a firing control (`ω₃` does *not* commute with `e₄`: residual `4.0`). |
| **A7** | **"ω² = −1 vs +1 is precisely what distinguishes the two Pin groups" is FALSE in the relevant dimension.** For `ω₄ = e₁e₂e₃e₄`, `ω₄² = (−1)^{6}·(±1)^4 = +1` in **both** `Cl(4,0)` and `Cl(0,4)`. What distinguishes them is the square of a **vector**, `e_i² = ±1`. | **ACCEPTED, repaired.** Renamed `P5_omega_sq_in_Cl3`; new `P5_omega4_sq_is_the_SAME_in_both` and gate `G30f` record the correction explicitly. |
| **A8** | **"Two independent retrieved sources" oversells it** -- arXiv:2501.01848 §2 and arXiv:1508.02619 Prop. 2.2 **both cite Kirby-Taylor Lemma 1.3**, and the primary was not read. Two independent *retrievals* of one primary is not two independent derivations. Relatedly, the `ℝP²`/`ℝP⁴` control is discriminating against a **code-level** swap but **not** against a convention error **in the source**, because the anchors come from the same source family. | **ACCEPTED entire, and OVERTAKEN BY EVENTS.** The **primary was obtained and read this session** (§2a) -- the criteria and the dimension-4 bordism groups are now `[VERIFIED-tool, PRIMARY]`. And pass 2's genuinely source-independent anchor (**the Wu formula on closed surfaces**) is adopted into the record alongside the `ℝPⁿ` one, exactly as it recommended. |
| **A9** | **§8/§12's "the manifold imposes NO constraint" is stated one scope wider than §7d licenses.** §7d itself says the twisting "can change which bundle's `w₂` is meant". | **ACCEPTED, narrowed everywhere** to "**via its bare tangential structure**" (§8, §12, Pearl 1). §7d is judged an **honest boundary** by pass 2 ("not the shape an escape hatch takes") -- the defect was the headline not respecting it. |

### Findings unique to pass 1

| # | Finding | Response |
|---|---|---|
| **B1** | **Constructive:** re-ran `H_*(M_ι)` from an 8-cell antipodal CW model of `S³` (`C=[2,2,2,2]`, `∂ = I∓T`) and got **the identical `(1,1,0,1,1)` and `[ℤ,ℤ,0,ℤ/2,0]`**. "The single strongest confirmation available and it is absent from the round." | **ADOPTED with credit** (implemented in the `C=[1,1,1,1]` form, which is the same idea and cheaper). It is the round's strongest verification and it came from a skeptic. |
| **B2** | **Wu-formula cross-check the round does not use:** for a closed 4-manifold `w₂ = v₂ + v₁²`; `v₂ ∈ H² = 0` and `v₁² = w₁² ∈ H² = 0`, so `w₂ = 0` **independently**. | **ADOPTED**, added to §4 as route E. |
| **B3** | **Twisted coefficients do not break it:** `π₁(S³) = 0`, so any local system restricts to a constant one on the fibre and the Wang squeeze still gives `H²(M;L) = 0` for **any** local system -- the argument is **stronger** than claimed. | **ADOPTED**, recorded in §4. |
| **B4** | §4 route B is advertised as "covers every `f`" but the **Wang sequence needs a fibration**, i.e. `f` a homeomorphism; and **"`f*−1 = 0` identically" is false for `deg ∉ {±1}`**, including this file's own deg-2 probe. | **ACCEPTED**, both corrected in §4. The conclusion is unaffected (the squeeze does the work), but a false sentence inside a correct proof is still a defect. |
| **B5** | **Cross-references to "§7c" should be "§7d"** (3 places); and **`deg ∈ {0,2,7}` mapping tori are not manifolds**, so falsifier 2 was ill-posed for 3 of its 5 entries. | **ACCEPTED**, both fixed. |
| **B6** | `G2`,`G3`,`G4` are identities of `qconj` true by construction; `G11`'s control is forced to `2√3` once `G10` passes. **"38 of 38" ≠ 38 independent discriminating checks.** | **ACCEPTED**, stated plainly in §11 rather than left for a reader to discover. |
| **B7** | §3's finite-difference determinant work is **redundant**: `H¹(M;𝔽₂) = ℤ/2` is 1-dimensional and `M` is non-orientable, so `w₁ = π^*a` follows with no measurement. | **ACCEPTED as a non-issue** (extra work, not error) and labelled as such in §3. |

### Findings unique to pass 2

| # | Finding | Response |
|---|---|---|
| **C1** | **The verdict string's compressed §6 argument is FALSE as stated** -- it omits **parallelizability**. Counterexample satisfying every premise it *does* state: **`CP² × S¹`**, the mapping torus of `id_{CP²}` (free `ℤ`, simply-connected fibre), with `w₂ = h ≠ 0` -- it admits **neither** `Pin^±` **nor** Spin. Second instance: `ℝP²×S¹`. *"The mathematics in §6 is sound; the sentence that will be grepped out of the record later is not."* | **ACCEPTED -- the sharpest finding of either pass**, because it targets exactly what survives quotation. `PARALLELIZABLE` is now **in the verdict string**, and §6 states the two hypotheses separately with `CP²×S¹` written in as the standing counterexample to the compressed form. |
| **C2** | **Injections 1 and 2 corrupt *assertions*, not *computations*** -- injection 1 rewrites the check `‖M+Ad‖` into `‖M−Ad‖`, leaving `dets_iota` (what `w1_nonzero` actually reads) untouched. | **ACCEPTED**, recorded in §11's honest accounting. |
| **C3** | **`ALL_INJECTIONS_CAUGHT = True` is an OR over 38 gates, four of which cannot fail.** It establishes that the gate can fail, not that it guards the conclusion. | **ACCEPTED**, and answered structurally: the harness now records **`headline_fields_moved` per injection** and a separate top-level `AT_LEAST_ONE_INJECTION_MOVES_THE_HEADLINE`. |
| **C4** | **`P6_F2_betti_numbers` is `cell_ranks_by_dim` copied verbatim** for `deg = ±1`, because over `𝔽₂` every differential in the minimal complex is zero. So the "consistency checks on the answer itself" restate the input. | **ACCEPTED**, and this is precisely what the non-minimal model fixes: there the differentials are non-zero and the Betti numbers are computed. |
| **C5** | **"The one place where `deg=−1` and `deg=+1` visibly part company"** -- its own table shows **two** (`H₃` and `H₄`). | **ACCEPTED**, corrected in §4. |
| **C6** | **"Without these, `H₂=0` would be an unfalsifiable output" -- with them it was STILL unfalsifiable**, because the controls exercise inputs with `C₂ ≠ 0` while the `M_ι` input has `C₂ = 0`. | **ACCEPTED**, the sharpest statement of A4; fixed by the same repair, and the claim is re-worded. |
| **C7** | **Load-bearing-citation audit:** the conclusion **survives withdrawal of any single citation**, because §4 and §6 have **disjoint** citation sets (§6 constructs both structures with no criterion at all -- the names come from the Clifford signature, a definition). *"That is the strongest structural feature of this round and it should be said louder than it is."* | **ADOPTED**, promoted into §12 as a first-class property rather than left implicit. |
| **C8** | **The single-token verdict string is unreadable**; its caveats are real but will not survive quotation. | **ACCEPTED as a genuine limitation.** Mitigated by putting the qualifiers (`BARE_TANGENTIAL`, `PARALLELIZABLE`) into the **header block** as well, which is what gets read. |
| **C9** | §4 labels routes A and B as one argument, then §12 counts "two presentations plus four textbook controls" toward the "independently-written code (Strong)" rung. **The controls are textbook checks of the tool, not of the result.** | **ACCEPTED**, §12 rewritten. |

**Nothing dismissed. Two findings answered rather than accepted outright:** B7
(redundancy is not an error) and pass 2's judgement that §7d is an honest
boundary (accepted as stated, with the *headline* narrowed instead).
**No finding moved the answer; nine moved what the record is allowed to say
about how well it is evidenced.**

---

## 1. Zero-Signal Gate (Step −5), run BEFORE any computation

| Field | Status | Content |
|---|---|---|
| Entity | **PASS** | `M_ι = (S³ × [0,1]) / ((x,1) ∼ (ι(x),0))`, `ι(g) = g^{-1}` -- a specific closed smooth 4-manifold. Verified: `ι` is exactly `diag(1,−1,−1,−1)|_{S³}` (residual `0.0`), `ι² = id` (`0.0`), `‖x·ι(x) − 1‖ ≤ 4.4e−16`. |
| Falsifiable predicate | **PASS** | "`w₂(M_ι) = 0`" and "`w₂ + w₁² = 0`" -- each a yes/no about an element of a specific finite group. |
| Measurable outcome | **PASS** | `H²(M_ι;𝔽₂)` computed exactly by four routes; `w₁` from a measured determinant. |

**Gate result: PASS.** The round proceeds and does **not** return `BLOCKED`.

---

## 2. Step −4/−3 -- literature first, actually performed

### 2a. The existence criteria -- PRIMARY, and the surprise

**[VERIFIED-tool, PRIMARY -- retrieved and read this session]** R. C. Kirby and
L. R. Taylor, *Pin structures on low-dimensional manifolds*, LMS Lecture Note
Series 151, pp. 177-242; §0 Introduction, printed p. 177 (PDF obtained from the
Ranicki archive, text extracted with `pypdf`; OCR artefacts noted inline):

> *"The obstruction to putting a Spin structure on a bundle [ξ] … is w2([ξ]) ∈
> H²(B;Z/2Z); for Pin+ it is still w2([ξ]), and for Pin- it is w2([ξ]) +
> w1²([ξ])."*

Same paragraph, the torsor fact used below:

> *"In all three cases, the set of structures on [ξ] is acted on by H¹(B; Z/2Z)
> and if we choose a structure, this choice and the action sets up a
> one-to-one correspondence between the set of structures and the cohomology
> group."*

**This upgrades §12's own "single highest-value next step" from pending to
done**, and it retires skeptic finding A8.

| | `w₂ = 0` | `w₂ + w₁² = 0` |
|---|---|---|
| **Kirby-Taylor (PRIMARY)** | `Pin^+` | `Pin^-` |
| `claim.md` lines 56-57 | *"Pin^- exists"* ❌ | *"Pin^+ exists"* ❌ |
| C128 **§6c**, lines 475-476 | *"`Pin^-` needs `w₂ = 0`"* ❌ | *"`Pin^+` needs `w₂+w₁²=0`"* ❌ |
| C128 **Completeness item 4**, lines 75-76 | `Pin^+` ✅ | `Pin^-` ✅ |

> **C128 states the criteria BOTH WAYS in the same file**, and `claim.md`
> inherited the wrong half. That is a sharper and more useful finding than "C128
> got it backwards": the error is a **local inconsistency**, not a settled
> misunderstanding, so the fix is a one-line correction, not a re-derivation.

**Two independent anchors, neither of which relies on the source's own naming:**

1. **`ℝPⁿ`** (`P4`, gates `G23`/`G24`). `w(ℝPⁿ) = (1+a)^{n+1}` gives
   `ℝP²`: `w₁ = a`, `w₂ = a²`, `w₂+w₁² = 0`; `ℝP⁴`: `w₁ = a`, `w₂ = 0`,
   `w₂+w₁² = a² ≠ 0`. They satisfy **opposite** conditions. Kirby-Taylor
   Theorem 5.2 (below) says `ℝP⁴` generates `Ω^{Pin^+}_4`, so `Pin^+ ⟺ w₂ = 0`.
2. **The Wu formula** (supplied by skeptic pass 2 as a *source-independent*
   anchor, and adopted for exactly that reason). For a closed surface `v₂ = 0`
   (Wu classes vanish above `n/2`), so `w₂ = v₁² = w₁²`, i.e. **every closed
   surface satisfies `w₂ + w₁² = 0`**. Every closed surface is `Pin^-`, and
   `Ω^{Pin^-}_2 = ℤ/8` generated by `ℝP²`. Under the swapped labelling one would
   need "every surface is `Pin^+`" and `Ω^{Pin^+}_2 = ℤ/8`, but the primary
   table gives `Ω^{Pin^+}_2 = ℤ/2`. **Contradiction -- the labelling is fixed
   without consulting either arXiv paper.** `[INFERRED]` from `[VERIFIED-tool]`
   primary values.

**Secondary corroboration, retrieved earlier the same session and kept for the
record:** arXiv:2501.01848v1 §2 (Bais) and arXiv:1508.02619 Prop. 2.2 both state
the same criteria; **both cite Kirby-Taylor Lemma 1.3**, so they are two
retrievals of one primary, not two independent derivations (finding A8).

### 2b. The mapping-torus side -- searched, nothing special-case found

Searched this session for: Stiefel-Whitney classes of mapping tori; the Wang
sequence route; closed 4-manifolds fibring over `S¹` with `S³` fibre; mapping
tori of finite-order isometries of `S³`. **The standard general tools are
confirmed and cited below; no source stating this manifold's SW classes was
retrieved.** J. Hillman, arXiv:math/0212142, **ch. 11 ("Manifolds covered by
`S³×ℝ`"), §11.4 ("`𝕊³×𝔼¹`-manifolds")** is the right place -- table of contents
retrieved, statement **not**. Recorded as `[CITED-LOCATION-ONLY]` and **not used
as evidence anywhere.** The most likely explanation for the null result is that
the computation is folklore; **§9a claims no novelty.**

### 2c. `Ω^{Pin^±}_4` -- retiring C128's dangling tag, and NOT using it

**[VERIFIED-tool, PRIMARY]** Kirby-Taylor **Theorem 5.2**, printed p. 215:

> *"The group Ω₄^{Spin} ≅ Z generated by the Kummer surface; Ω₄^{Pin-} = 0; and
> the group Ω₄^{Pin+} ≅ Z/16Z generated by RP⁴."*

and the summary table, printed p. 178 (dims 1-4):
`Ω^{Pin^-}: ℤ/2, ℤ/8, 0, 0` and `Ω^{Pin^+}: 0, ℤ/2, ℤ/2, ℤ/16`.

> **C128 recorded these as `[MEMORY, unverified, LOW]` after two arXiv searches
> failed; they are now PRIMARY-verified and correct.** They are **not used as
> evidence for structure existence** anywhere in §3-§7 -- that substitution is
> `claim.md`'s kill criterion (b). *(Corrected per skeptic finding: the first
> draft's blanket "not used as evidence anywhere" was false, since §2a's
> `ℝP⁴` anchor does use `Ω^{Pin^+}_4 = ℤ/16`. The honest statement is the
> narrow one: not used for **existence**; used only for **labelling**, where a
> second, source-independent anchor (the Wu argument) now also stands.)*
>
> They do show **why §2a's swap matters downstream**: `ℤ/16` versus `0` is the
> difference between "there is a 16-fold anomaly to cancel" and "there is
> nothing to cancel at all."

---

## 3. `w₁` -- the manifold is non-orientable

`M_f` fibres over `S¹` with fibre `S³`, so `TM_f ≅ T^{vert} ⊕ π^*TS¹` with
`π^*TS¹` trivial; hence `w(M_f) = w(T^{vert})` [CITED, standard]. `S³` is
parallelizable, so `T^{vert}` is the rank-3 bundle clutched by `M_f`.

**Measured this session, reproducing C128 §2b from scratch** (`P2`, no project
code imported):

| quantity | value |
|---|---|
| `‖M_ι(x) + Ad(x)‖`, i.e. `M_ι = −Ad` | `2.1e−10` |
| wrong-sign negative control | `3.464` |
| `‖M_{φ_{a,b}}(x) − Ad(b)‖` | `4.5e−10` |
| `det M_ι` over 60 base points | `[−1.0000000002, −0.9999999998]` |
| `det M_{φ_{a,b}}` -- **negative control** | `[+0.9999999996, +1.0000000003]` |
| `det M_{φ_{a,b}∘ι}` (the coset) | `[−1.0000000004, −0.9999999997]` |

`π₁(S³) = 0` gives `π₁(M_f) ≅ ℤ`, so `H¹(M_f;𝔽₂) = ℤ/2` and every class is
pulled back from `S¹`. The determinant line bundle has monodromy `−1`, so

> **`w₁(M_ι) = π^*(a) ≠ 0`.** `[INFERRED]` from the `[VERIFIED]` determinant.

This **confirms C128 §6b** (non-orientable, no `Spin` structure) by an
independent route: C128 argued from the general fact about orientation-reversing
mapping tori; here the transition function is exhibited and measured.

**Honest note (skeptic B7):** this measurement is **redundant**. `H¹(M;𝔽₂)` is
1-dimensional and `M` is non-orientable, so `w₁ = π^*a` follows with no
numerics. Retained as an independent cross-check of C128, not as the argument.

**And `w₁² = 0`, for two independent reasons:** (i) `w₁² = π^*(a²)` and
`a² ∈ H²(S¹;𝔽₂) = 0` because `S¹` is a 1-complex -- **this route does not use
§4 at all**, which is why the code now derives it separately; (ii) `H²(M;𝔽₂)=0`
outright (§4), which kills every degree-2 class at once.

---

## 4. `w₂` -- the whole group it lives in is zero

**Theorem (C129).** *Let `f : S³ → S³` be any self-homeomorphism, `M_f` its
mapping torus. Then `dim_{𝔽₂} H^k(M_f;𝔽₂) = (1,1,0,1,1)`, `k = 0…4`. In
particular `H²(M_f;𝔽₂) = 0`, hence `w₂(M_f) = 0` and `w₁(M_f)² = 0`,
unconditionally.*

**Route A (cell count).** Minimal CW structure on `S³`: one 0-cell, one 3-cell.
`f` may be taken cellular with the 0-cell at a fixed point (for `deg f = −1` one
exists: `L(f) = 1 − deg f = 2 ≠ 0`; for `ι` the fixed set is exactly `{±1}`, via
the exact identity `‖ι(x)−x‖² = 4‖Im x‖²`, residual `0.0`). The mapping torus
then has cells in dimensions **0, 1, 3, 4 and none in dimension 2**, so
`C₂ = 0`, so `H₂(M_f;A) = 0` for **every** coefficient group `A`. ∎
*(Skeptic B4: the Lefschetz detour is unnecessary -- cellular approximation
suffices, and mapping tori of homotopic maps are homotopy equivalent. Retained
because it is concrete for the actual map.)*

**Route B (Wang).** `… → H^{n−1}(S³) --(f^*−1)--> H^{n−1}(S³) → H^n(M_f) →
H^n(S³) --(f^*−1)--> …`. Degree 2 is squeezed between `H¹(S³;𝔽₂) = 0` and
`H²(S³;𝔽₂) = 0`, so `H²(M_f;𝔽₂) = 0` **regardless of `f^*`**. ∎
*(Two corrections, skeptic B4: the Wang sequence needs a **fibration**, so this
covers self-**homeomorphisms**, not literally "every `f`"; and the first draft's
"`f^* − 1 = 0` identically" is **false for `deg ∉ {±1}`**, including this file's
own deg-2 probe. Neither matters -- the squeeze is what does the work, and it
needs nothing about `f^*`. Both sentences are corrected rather than deleted.)*

> **Routes A and B are the SAME LINEAR ALGEBRA** -- the algebraic mapping cone
> of `(f_# − id)` *is* the Wang sequence. Two presentations, not two independent
> computations. Stated plainly because the first draft's §12 counted them toward
> an independence claim (skeptic C9).

**Route C (`π₁` + `χ` + Poincaré duality) -- genuinely independent, no chain
complex, no CW structure, no Wang sequence.** Inputs: (1) `π₁(M_f) ≅ ℤ` from the
fibration LES, so `b₁ = dim Hom(ℤ,𝔽₂) = 1`; (2) `χ(M_f) = χ(S³)·χ(S¹) = 0`, as
every mapping torus has; (3) mod-2 Poincaré duality for a **closed** manifold
(valid regardless of orientability), so `b₄ = b₀ = 1` and `b₃ = b₁`. Then
`0 = χ = 1 − b₁ + b₂ − b₁ + 1 = 2 − 2b₁ + b₂`, so **`b₂ = 2b₁ − 2 = 0`.** ∎
This shows the result is **forced**: any closed 4-manifold with `π₁ = ℤ` and
`χ = 0` has `b₂ = 0` mod 2.

**Route D (a NON-MINIMAL CW model) -- the check that makes the headline
corruptible.** Both skeptic passes independently proposed this and it is the
single most valuable thing they produced. Give `S³` the model `C = [1,1,1,1]`
with `∂₂ = (1)` (a 1-cell killed by a 2-cell): simply connected with `S³`'s
homology, hence homotopy equivalent to `S³`, but with `C₂ ≠ 0`. The mapping
torus then has **two 2-cells**, and `H₂ = 0` requires two genuine `𝔽₂` rank
computations. Result: **identical** `(1,1,0,1,1)` and `[ℤ,ℤ,0,ℤ/2,0]`
(`G37a`-`G37c`). Pass 1 ran the same check by hand on a different (8-cell,
antipodal) model and got the same answer.

**Route E (Wu formula) -- a fifth, and it needs no cohomology computation at
all.** For a closed 4-manifold `w₂ = v₂ + v₁²`; `v₂ ∈ H²(M;𝔽₂)` and
`v₁² = w₁² ∈ H²(M;𝔽₂)`, both zero. `[INFERRED]`, supplied by skeptic pass 1.

**Computed exactly** (`P3`, integer Smith normal form + `𝔽₂` rank):

| mapping torus | cells by dim | `H_*(·;ℤ)` | `H_*(·;𝔽₂)` |
|---|---|---|---|
| **`M_ι` (`deg = −1`), minimal** | `[1,1,0,1,1]` | `ℤ, ℤ, 0, ℤ/2, 0` | `1,1,**0**,1,1` |
| **`M_ι`, NON-minimal model** | `[1,2,2,2,1]` | `ℤ, ℤ, 0, ℤ/2, 0` | `1,1,**0**,1,1` |
| `S³×S¹` (`deg = +1`) | `[1,1,0,1,1]` | `ℤ, ℤ, 0, ℤ, ℤ` | `1,1,**0**,1,1` |
| `deg = 0` | `[1,1,0,1,1]` | `ℤ, ℤ, 0, 0, 0` | `1,1,**0**,0,0` |
| `deg = 2` | `[1,1,0,1,1]` | `ℤ, ℤ, 0, 0, 0` | `1,1,**0**,0,0` |
| `deg = 7` | `[1,1,0,1,1]` | `ℤ, ℤ, 0, ℤ/6, 0` | `1,1,**0**,1,1` |

`deg = −1` and `deg = +1` part company in **two** places, not one (skeptic C5):
`H₃(·;ℤ) = ℤ/2` vs `ℤ`, and `H₄(·;ℤ) = 0` vs `ℤ` (the orientability difference).

**Controls that the machinery can return a NONZERO `H₂`:** `S²×S¹` and the
`S²`-antipodal mapping torus both give `H₂(·;𝔽₂) = ℤ/2 ≠ 0`; the **Klein
bottle** reproduces `H₁ = ℤ⊕ℤ/2`, `H₂ = 0` and the **torus** reproduces
`H₂ = ℤ`, both textbook-exact.

**Consistency identities**, correctly labelled after skeptic findings A2/A3:
`χ(M_ι) = 0` and the palindromic `𝔽₂` Betti vector are **identities of the
mapping-cone construction**, true for any input, and they did **not** fire under
any injection. *(The first draft claimed "neither is automatic from the
construction; both would break under a mis-indexed complex (injection 3 breaks
them)" -- **false, and contradicted by this round's own
`results_c129_injections.json`**, which records injection 3 firing
`G18/G19/G21/G36/G37`. Sentence deleted, checks renamed `G31_IDENTITY_…`,
`G32_IDENTITY_…`.)*

**Bonus robustness (skeptic B3):** since `π₁(S³) = 0`, any local system on `M`
restricts to a constant one on the fibre, so the Wang squeeze gives
`H²(M;L) = 0` for **any** local system -- stronger than the `𝔽₂` statement.

**Therefore `w₂(M_ι) = 0` and `w₁(M_ι)² = 0`, and by §2a's PRIMARY criteria
`M_ι` admits BOTH a `Pin^+` and a `Pin^-` structure -- exactly two of each**
(torsor over `H¹(M;𝔽₂) = ℤ/2`, Kirby-Taylor §0).

---

## 5. Why "both", stated so it is not mistaken for a coincidence

A manifold with `w₂ = 0`, `w₁² ≠ 0` is `Pin^+` only (`ℝP⁴`). One with
`w₂ = w₁² ≠ 0` is `Pin^-` only (`ℝP²`). One with `w₂ ≠ 0` and `w₂+w₁² ≠ 0` is
**neither** (`ℝP²×ℝP²`, now a gate check). Getting **both** requires `w₂ = 0`
**and** `w₁² = 0` simultaneously -- here not a fine-tuning but a consequence of
one fact: **`H²(M_ι;𝔽₂)` is the zero group**, so *every* degree-2 characteristic
class vanishes at once.

Structural reason, in one sentence: **the fibre `S³` is 2-connected**, so the
mapping torus has no room in degree 2 for any obstruction to live.

---

## 6. Independent constructive route -- exhibit the structures

§4 shows an obstruction group is zero. This section **builds** the structures,
using none of §4's machinery. **It has TWO hypotheses and both are load-bearing.**

`M_f = (S³ × ℝ)/ℤ`, generator acting freely by `γ(x,s) = (f(x), s+1)`.

> **(a) `S³ × ℝ` is PARALLELIZABLE** (`S³` is a Lie group), so its frame bundle
> is trivial and it carries a trivial `Pin^±(4)` bundle. A `Pin^±` structure on
> `M_f` is then exactly a lift of the `ℤ`-action.
> **(b) `S³` is SIMPLY CONNECTED**, so the single map `u : S³ → O(4)`,
> `u(x) = M_f(x) ⊕ 1`, lifts through the double cover `Pin^±(4) → O(4)` (the
> lifting criterion `u_*π₁(S³) = 0` is satisfied trivially).
> **And `ℤ` is free on one generator, so there is no relation to satisfy:** any
> lift of that single map generates a `ℤ`-action, automatically free (it covers
> a free action), whose quotient is a `Pin^±` structure on `M_f`. The only
> property of `Pin^±` used is that both are 2-fold covers of `O(n)`, so the
> argument runs identically for `Pin^+` and `Pin^-`.

> ⚠️ **HYPOTHESIS (a) IS NOT OPTIONAL, and the first draft's verdict string
> dropped it** (skeptic C1, the sharpest finding of either pass). Without
> parallelizability the argument is **false**: **`CP² × S¹`** is the mapping
> torus of `id_{CP²}` -- free `ℤ`, simply-connected fibre, every other premise
> satisfied -- yet `w₂(CP²) = h ≠ 0`, so it admits **neither** `Pin^+` nor
> `Pin^-` nor Spin. (`ℝP²×S¹` is a second instance.) The step that fails is
> exactly the unstated one: `CP²×ℝ` is not parallelizable, so there is no
> structure upstairs to lift. **`PARALLELIZABLE` is now in the verdict string.**

**The lift written out explicitly** (`P5`). For `f = ι`, `u(x) = −Ad(x) ⊕ 1`.
Put `ω := e₁e₂e₃` and let `S(x)` be the `Spin(3)` element covering `Ad(x)` (the
tautological lift -- `Ad` *is* the covering map). Then `ũ(x) := ω·S(x)` covers
`−Ad(x)`. Verified in **both** signatures:

| | `Cl(3,0)`, `e_i²=+1` | `Cl(0,3)`, `e_i²=−1` |
|---|---|---|
| Clifford relations residual | `0.0` | `0.0` |
| `‖ρ̃(S(x)) − Ad(x)‖` | `8.3e−16` | `7.3e−16` |
| **`‖ρ̃(ω·S(x)) + Ad(x)‖`** | **`8.3e−16`** | **`7.3e−16`** |
| wrong quaternion-embedding sign (**non-vacuity control**) | `2.825` | `2.814` |

**The Cl(3) → Cl(4) bridge, which the first draft omitted** (findings A6/A7).
The clutching function lives in `O(4)`, not `O(3)`, and **`ω` is NOT central in
`Cl(4)`** -- it anticommutes with `e₄`, so the first draft's stated reason
("`ω` is central in odd dimension") **does not apply**. The correct step, now
computed (`P5_Cl4_bridge`, `G30a`-`G30e`): `ω` is **odd**, so the twisted
adjoint gives `ρ̃(ω)e₄ = −(ωe₄ω^{-1}) = +e₄` while `ρ̃(ω)e_i = −e_i` for
`i = 1,2,3`. Hence `ρ̃(ω·S(x)) = (−Ad(x)) ⊕ (+1) = u(x)` exactly.
Measured: relations `0.0`; `ω₃e₄ + e₄ω₃ = 0.0`; **control** `ω₃e₄ − e₄ω₃ = 4.0`
(so "central" is measurably false); `ρ̃(ω₃)|_{e₁e₂e₃} = −1` (`0.0`);
`ρ̃(ω₃)|_{e₄} = +1` (`0.0`).

**And a second correction (A7): `ω² = −1` vs `+1` is a fact about `Cl(3)`, not
about the two Pin groups in the relevant dimension.** For `ω₄ = e₁e₂e₃e₄`,
`ω₄² = (−1)^{6}·(±1)^4 = +1` in **both** signatures (`G30f`). What distinguishes
`Pin^+` from `Pin^-` is the square of a **vector**, `e_i² = ±1` (`G26`).

---

## 7. Does the answer depend on WHICH relating map? -- `claim.md`'s degeneracy question

Required explicitly by `claim.md` kill criterion (c). Checked three ways;
the answer is **no**.

### 7a. The computation never sees more than `deg f mod 2`

Route B uses only `f^*` on `H^*(S³;𝔽₂)`, i.e. `deg f mod 2 = 1` for every
self-homeomorphism; routes A, C, D do not see `f` at all. Computed for
`deg ∈ {−1,0,+1,2,7}`, all `0` (`G14`). `w₁` **does** depend on `f`; `w₂` and
`w₁²` do not. **So `ι` and `f_{a,b}∘ι` give the same Pin verdict, as would any
relating map C125/C128 had missed.**

### 7b. And the manifolds are in fact the same one

`[CITED, Cerf 1968 / Hatcher 1983, already in this project's set via C125]`
`π₀(Diff(S³)) = ℤ₂`, detected by degree, so **all** orientation-reversing
diffeomorphisms of `S³` are isotopic to `ι` and their mapping tori are
diffeomorphic. `[INFERRED]` from a `[CITED]` theorem. **A bonus, not the
argument** -- §7a is independent of it and stronger.

### 7c. Is `ι` degenerate? -- yes, in a named way, and it does not matter

`ι² = id` **exactly** (`0.0`), so `M_ι` carries extra structure:

* a **flat** `S³`-bundle with `ℤ/2` monodromy, `M_ι = (S³×ℝ)/ℤ`;
* its **orientation double cover is `S³ × S¹`** (the mapping torus of `ι² = id`).
  Consistent: `H^*(S³×S¹;𝔽₂)` also has dimensions `(1,1,0,1,1)`, and `χ = 0`;
* fixed set `{±1}` nonempty -- irrelevant, the `ℤ` action is free regardless
  (it translates the `ℝ` factor).

**The generic coset representative is NOT an involution**, checked rather than
assumed: `(φ_{a,b} ∘ ι)² = φ_{ab,\,ba}` (residual `5.6e−16`), which is the
identity only when `ab = ba = ±1`. Over 60 random `(a,b)` the minimum
displacement `‖g²(x) − x‖` is `0.179` -- **never** an involution in the sample.
So the generic case has **infinite-order** monodromy and none of `M_ι`'s extra
structure, **and gives the same answer**, by §7a.

**Net: `ι`'s specialness is real, is named here, and is not load-bearing.**

### 7d. What this does NOT settle -- the twisted structure

A Dai-Freed argument needs the mapping torus **with the tangential structure the
fermion content requires**, which for a half-integral representation is a
twisted one (`Pin^± ×_{ℤ₂} G`), **not** the bare `Pin^±`. **Existence of the
bare structure is necessary, not sufficient**, and the twisted condition is a
different cohomological condition this round does not evaluate. This is C127's
own skeptic finding 1 applied here. `[UNKNOWN]`.

`H²(M_ι;𝔽₂)` being **zero** makes the twisted case *plausibly* also work, since
an obstruction of the form `w₂ + (something in H²)` also lands in the zero group
-- **but the twisting can change which bundle's `w₂` is meant, so this is a
plausibility remark, not a result, and is counted nowhere below.**

*(Skeptic pass 2 judged this section "an honest boundary, by a margin ... not the
shape an escape hatch takes" -- while finding that the **headline** did not
respect it. That is fixed in §8 and §12.)*

---

## 8. Kill Analysis (Anti-Overfitting Gate)

### What this round KILLS

* **`claim.md`'s own permitted `BLOCKED` outcome.** The classes were computable.
* **The framing in which "which `Pin` type does the manifold admit?" is a live
  discriminating question -- for the BARE TANGENTIAL structure.** The manifold
  admits both, so **via its bare tangential structure** it contributes **no**
  constraint; any selection must come from the fermion content (round95). *This
  is the round's most useful negative content: it removes a route people would
  otherwise try.* **The narrowing to "bare tangential" is required by §7d and
  was missing from the first draft** (skeptic A9/C-scope).
* **C128 §6c's and `claim.md`'s stated Pin criteria**, as written (§2a).
* **C128's dangling `[MEMORY, unverified, LOW]` tag** on `Ω^{Pin^±}_4` -- now
  PRIMARY-verified (§2c), though deliberately not used for existence.

### What this round does NOT kill

* **The anomaly half of Y1 / C127's A2 and X6.** Well-posed, unattempted, still
  blocked -- now on **one** ingredient (round95) plus §7d's newly named
  prerequisite.
* **The twisted-structure question** (§7d). Named, unevaluated.
* **C125's `FALSIFIED`, C126's `WEAKENED`, C127's `BLOCKED`, C128's
  `OUTCOME_B`** -- none re-litigated; C128 §6b **confirmed** independently.
* **Whether a `t`-selector exists**; Family C / `ε₄ε₆`; round80/Round117's open
  tension; round95's missing link.
* `N_gen=3`'s CONDITIONAL status, `lambda = FREE_COUPLING_PARAMETER`,
  `sm_derivation_claimed = False`, `safe_for_runtime = False`, OB1's `PARKED`.

### Relaxation Map (one assumption changed per variant; none attempted here)

| Variant | Single assumption changed | Kill criterion |
|---|---|---|
| **Z1** | Ask for the **twisted** structure the fermion content needs, not the bare tangential one (§7d) | Does the twisted obstruction also land in `H²(M;𝔽₂) = 0`, or does the twisting move it to a group that is not zero? Prerequisite: knowing `G`, which C128 §5 settled as the **frame bundle's** group. **Cheaper than round95 -- this is now the first thing to do.** |
| **Z2** | Grant round95's missing link and ask which `Pin` type the content **selects** | Both types exist, so the content alone decides. Does `Ω^{Pin^+}_4 = ℤ/16` vs `Ω^{Pin^-}_4 = 0` then force the pair (C127's A2) or merely re-report C126's winding? **Must use the §2a labelling, not `claim.md`'s.** |
| **Z3** | Drop `S³` for a fibre that is **not** 2-connected | §4's whole argument is "the fibre has no `H¹` or `H²`". On a fibre with `H¹ ≠ 0` the mapping torus has 2-cells and `w₂` can be anything -- `CP²×S¹` (§6) is the standing example. Does any physically relevant variant have such a fibre? (`S⁶` does not; `S³×S⁶` does not.) |
| **Z4** | Ask for the 13D object rather than the `S³`-level one | Blocked ab initio: `M₄` non-compact as frozen. Listed so it is not silently retried. |
| **Z5** | Literature check on §4 (partially run, §2b) | Is the theorem in Hillman ch. 11/§11.4? Would remove nothing (no novelty claimed) but would settle whether §4 is folklore. |

---

## 9. What this round does NOT show

1. Does **not** resolve OB1 or move it out of `PARKED`.
2. Does **not** supply an F4 mechanism, or any `t`-selector.
3. Does **not** use the `Ω^{Pin^±}_4` values as evidence for structure
   **existence** (`claim.md` kill criterion (b)); they are used only for
   **labelling**, where a source-independent anchor also stands (§2a).
4. Does **not** evaluate any anomaly, or attempt C127's A2 / X6.
5. Does **not** touch round95's missing `S⁶`↔`S³` link -- so it does **not** say
   which `Pin` type the fermion content requires.
6. Does **not** establish that the **twisted** structure exists (§7d).
7. Does **not** make any 13D statement (`M₄` non-compact).
8. Does **not** reopen C125's, C126's, C127's or C128's verdicts.
9. Does **not** claim literature novelty (§2b).
10. Does **not** consult ABP67/Gia71 or Hillman directly. Kirby-Taylor **is**
    now consulted directly (§2a, §2c).
11. Does **not** change `N_gen=3`, `lambda`, `sm_derivation_claimed`, or
    `safe_for_runtime`.
12. Does **not** edit `PARENT_ACTION_GATE.md`, `OPEN_BLOCKERS.md`,
    `null_results/`, `CLAIM_LEDGER.yaml`, or `pearl_registry/` -- the
    orchestrating session's, per C124-C128 precedent.
13. Does **not** solicit Tom Lawrence's Part 5 or initiate any contact.

### 9a. Novelty ledger

| Item | Status |
|---|---|
| §4's theorem (`H²(M_f;𝔽₂) = 0` for every self-map of `S³`) | **New to this project's record. NOT claimed new to mathematics** -- elementary, no source found but none seriously expected (§2b). |
| §4's routes C, D, E | **New to this round**; D and E were **supplied by the skeptic passes**, not by the first draft. |
| §6's constructive route | **New to this project's record.** Elementary; "ℤ is free so a mapping torus never obstructs a lift" is folklore. Its **parallelizability hypothesis** was missing from the first draft's compressed form and is the round's most important correction. |
| §2a's Pin-criteria **swap** in `claim.md`/C128 §6c, and C128's **internal inconsistency** | **New, and a correction to this project's own record.** Found by literature retrieval. |
| §3's `w₁ ≠ 0` | **Not new** -- C128 §6b states it. Re-derived here from a measured transition function. |
| §2c's `Ω^{Pin^±}_4` values | **Not new to the record**; the tag moves `[MEMORY, unverified, LOW] → [VERIFIED-tool, PRIMARY]`. |
| §7c's `(φ_{a,b}∘ι)² = φ_{ab,ba}` | **Minor, new to the record.** Answers `claim.md`'s degeneracy question concretely. |
| **New results bearing on OB1's own question** | **Zero.** The round removes an obstruction from a route; it supplies no mechanism. |

---

## 10. Proposed pearls (NOT written to `pearl_registry/INDEX.md` -- outside this round's brief, per C124-C128 precedent)

**Pearl 1 -- Pearl Gate. The fibre's connectivity, not the monodromy, decides.**
* **observation:** for a mapping torus `M_f` of a self-map of a `k`-connected
  fibre `F`, every **bare tangential** characteristic-class obstruction in
  degrees `2…k` vanishes automatically, because `H^j(M_f) = 0` there -- the
  monodromy is irrelevant. For `F = S³` this kills `w₂` outright and makes
  `Pin^+`, `Pin^-` **both** available on **every** mapping torus of **every**
  self-map.
* **falsifiable_prediction:** any future round asking "does the mapping torus of
  [some map of `S³`] admit [some degree-2 **tangential** structure]?" gets
  **yes**, with no computation, and therefore **cannot** discriminate `t=0`
  from `t=1`. Counter-example would be a structure whose obstruction is **not**
  a degree-2 class of the manifold's own tangent bundle -- e.g. a twist by a
  bundle carrying its own `H²`-valued data (§7d).
* **impact_score:** 5. **trigger_condition:** any future round proposing a
  mapping-torus / `S¹`-fibred object over `S³` as a discriminator.
  **next_check:** 2026-12-01.
* **Scope limit:** uses `S³`'s 2-connectivity, **and** (for the constructive
  form) parallelizability of the fibre. **Does NOT transfer to `S⁶`, to
  `S³×S⁶`, or to any non-parallelizable fibre** -- `CP²×S¹` is the standing
  counterexample. Does not cover twisted structures.

**Pearl 2 -- Caveat Gate** (a specific, buildable alternative named in §7d and
not attempted):
* **observation:** the **bare tangential** `Pin^±` question and the **twisted**
  one the anomaly actually needs are different questions with different
  obstructions; this round answers the first only. C127's skeptic finding 1 had
  already made the identical point for `Spin`.
* **falsifiable_prediction:** building the twisted version either (i) also lands
  in `H²(M;𝔽₂) = 0` and existence is again automatic, or (ii) introduces an
  `H²`-valued datum from the twisting bundle and existence becomes a real
  condition. Exactly one holds, and it is cheap to decide once `G` is fixed --
  C128 §5 already fixed `G` as the frame bundle's group.
* **impact_score:** 6 -- the actual gate on C127's A2/X6, and **cheaper than
  round95**. **trigger_condition:** any attempt on C127 X6/A2, or closure of
  round95. **next_check:** 2026-12-01.

**Pearl 3 -- methodological, and it is a correction to this project's own files.**
* **observation:** a `[MEMORY, unverified]` tag correctly refuses to *use* a
  fact, but does **not** protect the surrounding prose. C128 §6c stated the two
  Pin **criteria** with `Pin^+`/`Pin^-` interchanged, **untagged**, four lines
  from the values it *did* quarantine -- and `claim.md` inherited the swap
  verbatim into a pre-registered predicate. **The quarantined item was the
  harmless one; the unquarantined sentence next to it was the wrong one.**
  Sharper still: C128 states the criteria **correctly** in its Completeness
  section and **incorrectly** in §6c, so the file contradicts itself and the
  downstream round copied the wrong half.
* **falsifiable_prediction:** when a round quarantines a remembered *value*, the
  remembered *definitions* around it come from the same unverified source and
  fail at a comparable rate. Testable by auditing untagged definitional
  sentences adjacent to any `[MEMORY]` tag in this project's history; the
  prediction is that at least one more is wrong.
* **impact_score:** 5 -- cheap, general, and it already caught a real error that
  survived one round and was copied into a second.
  **trigger_condition:** any `[MEMORY, unverified]` tag written next to a stated
  definition or criterion. **next_check:** 2026-11-15.

**Pearl 4 -- methodological, from this round's own gate failure.**
* **observation:** a result that is true "for dimension reasons" (the group it
  lives in is zero) is **structurally untestable by injection** in the model
  where the dimension is read off the input -- no corruption of the machinery
  can move it. The fix is to recompute the same object in a **non-minimal
  presentation** where the answer is a computed rank, not a free consequence of
  the encoding.
* **falsifiable_prediction:** any verification suite whose headline quantity is
  determined by an input's shape rather than by a computation will show
  `ALL_INJECTIONS_CAUGHT = True` while **no** injection moves the headline;
  adding a non-minimal presentation flips at least one injection to
  headline-moving. **Confirmed once here** (2 of 8 now move it, 0 of 5 before).
* **impact_score:** 6 -- applies to every FL round whose verdict is
  "the obstruction group is zero", which is a recurring shape in this project.
  **trigger_condition:** any round whose headline is a vanishing statement.
  **next_check:** 2026-12-01.

---

## 11. Verification

**Gate: 49 of 49 pass** (`ruff check` clean, `ruff format` applied).

**Injection tests -- 8 injections, all caught, and TWO now move the headline:**

| injection | gate | caught | moves a headline field? |
|---|---|---|---|
| Clutching sign flipped (`M_ι = +Ad`) | `48/49` | ✔ `G10` | no |
| **Pin^+/Pin^- criteria swapped** (the error `claim.md` contains) | `47/49` | ✔ `G23`,`G24` | no |
| Monodromy term `(f_#−id)` dropped | `44/49` | ✔ 5 checks | no |
| **`𝔽₂` rank routine forced to `0`** | `45/49` | ✔ `G35`,`G36`,… | **YES** -- `w2_zero`, `Pin_plus_exists`, `Pin_minus_exists`, `H2_..._nonminimal` |
| Quaternion embedding sign hard-coded | `47/49` | ✔ `G28`,`G29` | no |
| **Boundary of a `b`-generator dropped** (pass 1's uncaught injection) | `47/49` | ✔ | **YES** -- same four fields |
| `pin_verdict` forgets the mod-2 reduction | `48/49` | ✔ `G23` | no |
| `pin_verdict` boolean form restored | `48/49` | ✔ `G25b` | no |

> **This is the repair of the deepest process finding.** Before the non-minimal
> CW model was added, **five injections were caught and ZERO moved any headline
> field** -- the suite showed the gate could fail, never that it *guarded the
> conclusion*. Both passes found this independently; the first draft had noticed
> it only for one injection and called the headline "more robust than the
> machinery". **Recorded, not hidden.**

**Two defects the gate caught in this round's own repairs, recorded rather than
silently corrected:**
1. Hard-coding the quaternion embedding sign broke `Cl(3,0)` (residual `2.825`);
   `G28` fired, `ALL_OK = False`. Now determined per signature with a
   non-vacuity check (one sign `4.4e−16`, the other `2.825`).
2. The `pin_verdict` repair first expanded over **ℤ**, so `ℝP²`'s
   `w₂ + w₁² = a² + a²` read as `2a² ≠ 0` and **`G23` flipped to False on the
   very commit meant to fix `pin_verdict`.** Fixed by `_f2_reduce`; both failure
   modes are now injections 7 and 8.

**Honest accounting of the checks** (skeptic B6/C2/A2):
* **Identities, not tests:** `G31_IDENTITY` (χ=0) and `G32_IDENTITY`
  (palindrome) -- true for any input complex.
* **True by construction:** `G2`,`G3`,`G4` are identities of `qconj`;
  `G11`'s value is forced to `2√3` once `G10` passes.
* **Corrupt an assertion, not a computation:** injections 1 and 2 rewrite
  checks, leaving the underlying `dets_iota` untouched.
* **Genuinely discriminating:** `G16`/`G17` (machinery *can* return non-zero
  `H₂`), `G18`-`G20` (Klein bottle, torus), `G23`/`G24`/`G25b` (Pin labelling,
  incl. the `ℝP²×ℝP²` case), `G29b` (embedding-sign non-vacuity), `G30c`
  (`ω₃` measurably not central in `Cl(4)`), `G35`-`G37c` (rank routine,
  deg-2 probe, non-minimal model), `P1_det_dPhi` (`SO(4)` control).

| Tier | Claim |
|---|---|
| `[VERIFIED-tool, PRIMARY]` | The Pin existence criteria and the `H¹`-torsor fact -- Kirby-Taylor §0, printed p. 177, **read directly this session**. `Ω₄^{Spin}=ℤ`, `Ω₄^{Pin^-}=0`, `Ω₄^{Pin^+}=ℤ/16` gen. by `ℝP⁴` -- their Theorem 5.2, printed p. 215. |
| `[VERIFIED-tool, SECONDARY]` | arXiv:2501.01848v1 §2 and arXiv:1508.02619 Prop. 2.2 -- same criteria, **both citing Kirby-Taylor Lemma 1.3**; two retrievals of one primary, not two derivations. |
| `[VERIFIED]` -- exact arithmetic, no floating point | `H_*(M_f;ℤ)` and `H_*(M_f;𝔽₂)` for `deg ∈ {−1,0,1,2,7}` in the minimal model **and for `deg ∈ {±1}` in a non-minimal model with two 2-cells**; `H²(M_ι;𝔽₂) = 0` in both; the two models agree in every degree. Controls: Klein bottle `H₁ = ℤ⊕ℤ/2`, torus `H₂ = ℤ`, `S²×S¹` and `S²`-antipodal with `H₂(·;𝔽₂) ≠ 0`. `ℝPⁿ` and `ℝP²×ℝP²` Pin verdicts. |
| `[VERIFIED]` -- finite differences, firing negative control | `M_ι = −Ad` (`2.1e−10`; control `3.464`); `M_{φ_{a,b}} = Ad(b)` (`4.5e−10`); `det M_ι = det M_{φ_{a,b}∘ι} = −1` vs `SO(4)` control `+1`. Reproduces C128 §2b, no project code imported. |
| `[VERIFIED]` -- exact | `ι = diag(1,−1,−1,−1)\|_{S³}` (`0.0`); `ι² = id` (`0.0`); `‖ι(x)−x‖² = 4‖Im x‖²` (`0.0`) so `Fix(ι) = {±1}` exactly; `(φ_{a,b}∘ι)² = φ_{ab,ba}` (`5.6e−16`), generically **not** an involution (min displacement `0.179`); the coset map is linear with `det = −1` and always has eigenvalue `+1`. |
| `[VERIFIED]` -- both signatures + the Cl(4) bridge, with firing controls | `ũ(x) = ω·S(x)` covers `−Ad(x)`: `8.3e−16` / `7.3e−16`; wrong-embedding-sign control `2.825`/`2.814`; `ω₃` anticommutes with `e₄` (`0.0`) with commuting-control `4.0`; `ρ̃(ω₃)` is `−1` on `e₁e₂e₃` and `+1` on `e₄` (`0.0`). |
| `[INFERRED]` -- chain as stated | `w₁(M_ι) = π^*(a) ≠ 0`. `w₂ = 0`, `w₁² = 0`. Route C (`π₁`+`χ`+PD) and route E (Wu). The §6 lifting argument (standard covering-space theory). "Exactly 2 of each type" (`H¹`-torsor). The Wu-formula labelling anchor. |
| `[CITED]` -- standard, not re-derived | `TM_f ≅ T^{vert} ⊕ π^*TS¹`; the Wang sequence; universal coefficients over a field; `Pin^±(n) → O(n)` is a double cover; Lefschetz; **Cerf 1968 / Hatcher 1983**; mapping tori of isotopic diffeos are diffeomorphic; `S³` parallelizable; `w(CP²) = (1+h)³`. |
| `[CITED]` -- project facts | C125 (`ι`, `φ_{a,b}`, `ι∘φ_{a,b}∘ι = φ_{b,a}`, the coset); C126; C127 (§3, §5d, X6, skeptic finding 1); C128 (§2b, §4, §6b, §6c, Y1, Completeness item 4); round95; `PARENT_ACTION_GATE.md` F4. |
| `[CITED-LOCATION-ONLY]` -- **not used as evidence** | Hillman, arXiv:math/0212142, ch. 11 / §11.4. |
| `[UNKNOWN]` -- deliberately not guessed | Whether the **twisted** structure exists (§7d, Z1). Which `Pin` type the fermion content requires (round95). Whether §4/§6 are in the literature. Everything in §8's "does NOT kill" and Z1-Z5. |

**No pytest suite touched, no shared project code modified.** Both scripts are
self-contained and import only `numpy`/`sympy`.

### Check (reproduces this decision)

```bash
cd experiments/20260902-c129-pin-structure-existence-mapping-torus
python c129_pin_structure_mapping_torus.py   # expect 49 / 49, ALL_OK = True
python c129_injection_tests.py               # expect ALL_INJECTIONS_CAUGHT = True
                                             #    and AT_LEAST_ONE_INJECTION_MOVES_THE_HEADLINE = True
```

Independently of the code:

1. Kirby-Taylor §0 (printed p. 177) -- the sentence assigning `w₂` to `Pin^+`
   and `w₂+w₁²` to `Pin^-`, **opposite to `claim.md` lines 56-57 and C128 §6c**,
   and **agreeing with C128's own Completeness item 4**.
2. `results_c129.json` →
   `P3_mapping_tori.NONMINIMAL_S3_iota_deg_minus1.cell_ranks_by_dim` must read
   `[1,2,2,2,1]` (two 2-cells) while its `H_F2[2]` is `"0"` -- **that pair is
   the result**: `H₂ = 0` computed, not counted.

**Falsifiers, stated so they can fail:**

1. **Exhibit a 2-cycle.** Produce `0 ≠ x ∈ H₂(M_ι;𝔽₂)`. Attacked by injections
   4 and 6, which do move it -- and the correct code does not.
2. **Exhibit a self-homeomorphism of `S³` whose mapping torus has `w₂ ≠ 0`.**
   §7a says the computation sees only `deg f mod 2 = 1`. *(Restricted to
   `deg = ±1`: for other degrees the mapping torus is not a manifold and `w₂` is
   undefined -- the first draft's version was ill-posed for 3 of its 5 entries.)*
3. **Break the criterion labelling.** If `Pin^+ ⟺ w₂ = 0` were wrong, `ℝP⁴`
   would fail to be `Pin^+`, contradicting Kirby-Taylor Thm 5.2; and every
   closed surface would have to be `Pin^+` with `Ω₂^{Pin^+} = ℤ/8`, contradicting
   their table's `ℤ/2`. Injection 2 makes the code-level substitution and
   `G23`/`G24` fire.
4. **Falsifier for the "both" verdict specifically:** find a degree-2 obstruction
   that is **not** a class of `M_ι`'s own tangent bundle -- i.e. §7d's twisted
   case. That is Z1, **unattempted**. This is why §8 does not claim the anomaly
   route is closed.
5. **Falsifier for §6:** exhibit a mapping torus with free-`ℤ` monodromy and
   simply-connected fibre admitting no Pin structure. **This SUCCEEDS against the
   compressed form** -- `CP²×S¹` -- and is why parallelizability is stated as a
   separate hypothesis and put into the verdict string.

---

## 12. Evidence tier of the central conclusion, and what would raise it

**Central conclusion:** *`M_ι` -- and the mapping torus of every candidate
relating map -- is a closed non-orientable 4-manifold (`w₁ ≠ 0`, no `Spin`
structure) whose **bare tangential** structure admits **both** a `Pin^+` and a
`Pin^-` structure, two of each, because `H²(M;𝔽₂) = 0` forces `w₂ = 0` and
`w₁² = 0` simultaneously. Via its bare tangential structure the manifold
therefore imposes **no** constraint on which Pin type an anomaly argument may
use; that choice is made by the fermion content (round95) and by the twisted
structure (§7d), neither of which this round touches.*

* **`[VERIFIED]`** -- the cohomology (§4, five routes, two CW models), the
  transition function (§3), the explicit Clifford lift and its Cl(4) bridge
  (§6), independence from the relating map (§7a), `ι`'s involution/coset
  structure (§7c). All exact or with firing controls; all eight deliberate
  corruptions are caught and two move the headline.
* **`[VERIFIED-tool, PRIMARY]`** -- the criteria that turn `w₁,w₂` into a Pin
  verdict (§2a), now read from Kirby-Taylor directly, plus a **source-
  independent** Wu-formula anchor.
* **`[INFERRED]`** -- the step from the classes to existence; "exactly two of
  each"; §6's lifting argument.
* **`[UNKNOWN]`** -- §7d's twisted structure; which type the content needs.

**The strongest structural property, promoted here at skeptic pass 2's
insistence: the conclusion survives withdrawal of ANY SINGLE citation**, because
§4 and §6 have **disjoint citation sets**. §6 constructs both structures with no
existence criterion at all (the names come from the Clifford signature, a
definition); §4 needs no parallelizability, no Cerf, no Lefschetz. Withdraw
Kirby-Taylor and §6 still builds them; withdraw parallelizability and §4 still
proves the obstructions vanish.

**Independent Verification Strength Ladder -- where this actually sits.** The
cohomology is at **"independently-written code" (Strong)**: the scripts import no
project code, and the answer is reproduced in **two different CW presentations**
plus **two argument routes (C, E) sharing no machinery with the chain complex**.
Both skeptic passes re-derived `H_*(M_ι)` by hand, without execution tools, and
got the identical five numbers -- that is genuinely independent of this round's
code, though it remains **"same model, isolated context" (Weak-Medium)** on the
ladder however thorough it was.

**What would raise the rest:**
* **§7d → resolved:** evaluate the twisted obstruction (Z1). **The single
  highest-value next step**, and cheaper than round95.
* **§4 → "symbolic solver":** a `Lean`/`GAP`-HAP recomputation. Low value -- the
  answer is now confirmed by five routes.
* **§2b's null → resolved:** read Hillman ch. 11/§11.4. Would settle whether §4
  is folklore, which §9a already assumes.
* **What would NOT raise it:** more random samples in `P1`/`P2`/`P5`. §4 is exact
  arithmetic and §3's determinant is a constant, not a statistic. *(And, per
  skeptic C9: the textbook controls check the tool, not the result -- they do
  not count toward independence of the conclusion.)*

### 12a. FL Step 8a skeptic pass

**RUN -- twice, context-blind, differently-worded prompts (Paraphrase-Sensitivity
Probe). Both returned the same split: MATHEMATICS `CONFIRMED-REAL`, EVIDENCE
APPARATUS `WEAKENED`. CONCORDANT, so no tie-breaker needed. 26 findings; all
answered, six code defects repaired, nothing waved through. Full response
matrices in §0.**

Their principal effects on this file: **half the headline (`Pin_minus`) was a
constant in the code and is now computed**; the injection suite could not move
any headline quantity and **now two injections do**; the §6 argument's
**parallelizability** hypothesis was missing from the verdict string and is
restored, with `CP²×S¹` as the standing counterexample to the compressed form;
the Cl(3)→Cl(4) bridge was unstated and its stated reason was false in dim 4,
both now computed; four claims about what the tests establish were false (one
contradicted by the JSON in the same folder) and are deleted or corrected; the
"two independent sources" framing was overstated and has been **overtaken** by
reading the primary; and the headline's scope is narrowed to the **bare
tangential** structure everywhere §7d requires it.
