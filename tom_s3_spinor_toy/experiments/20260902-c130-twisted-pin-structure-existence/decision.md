# C130 decision -- does the TWISTED Pin structure `Pin^± ×_{Z₂} G` exist on
# the mapping torus `M_ι`?  (C129's Relaxation Map item Z1.)
#
# HEADLINE, and it is already narrower than the first draft's because TWO
# independent FL Step 8a skeptic passes cut it back (§0):
#
# **AS A THEOREM ABOUT `M_ι`: IT EXISTS, uniformly in `G`.** For every Lie group
# `G` with a central element of order 2 and every `Ḡ = G/⟨z⟩`-bundle on `M_ι`,
# both `Pin^+ ×_{Z₂} G` and `Pin^- ×_{Z₂} G` structures exist, exactly two of
# each over any fixed underlying pair. Both passes attacked this and neither
# could move it; one verified it by hand-recomputing every load-bearing number.
#
# **AS AN ANSWER TO Z1: CONDITIONAL, and the condition is NOT satisfied on the
# record.** `M_ι` is a **4-manifold**, and it is a substitute -- C128 §6 chose
# it because as frozen `M₄` is non-compact so no 13D mapping torus is closed at
# all. C127 §4's own dimension audit enumerates every reading this project has
# (13D topological terms → `Ω₁₃,Ω₁₄`; a 13D parent's anomaly → `Ω₁₄,Ω₁₅`; the 4D
# effective theory's anomaly → `Ω₅,Ω₆`) and **`Ω₄` appears in none of them.**
# `Ω₄` is the home of a *3-dimensional* theory's anomaly, and this project has
# no 3D theory. So the relevance of `M_ι` is not merely untested -- it is
# **adversely indicated by this project's own already-verified table**. The
# first draft called this "inherited unexamined" and "cheap to decide"; skeptic
# pass 2 established it is stronger than that, and the correction is carried
# into the verdict string rather than left in a pearl.
#
# **THE TRANSFER FROM C129 IS PROVED, NOT ASSUMED** -- which is what `claim.md`
# demanded. Three things are supplied instead of the forbidden shortcut:
#   (a) a THEOREM about where the obstruction lives, valid for any `G` (§4);
#   (b) the obstruction GROUPS, recomputed here: `H²(M_ι;A) = 0` for **every**
#       abelian `A` (not just `𝔽₂`), `H³(M_ι;Z) = 0` so the Bockstein-type
#       "choose-your-own-bundle" escape closes too (§5);
#   (c) the CONVERSE exhibited FALSE, so (a)+(b) are not vacuous: `CP²` has no
#       bare Pin structure but a twist with `w₂(E)=h` rescues it, and `S²×S²` is
#       spin but a twist with `w₂(E)=a` destroys it (§7).
#
# ⚠️ **SEPARATE FINDING #1 -- REWRITTEN AFTER THE SKEPTIC PASSES, because the
# first draft's version was WRONG.** The first draft accused C129's Z1 row of
# *misattributing* to C128 §5 a naming of `G`. **That accusation is withdrawn.**
# C127 §5a's own table gives "frame bundle's group" as the consequence-for-`G`
# of the C125 reading, so C129 chained C127 §5a + C128 §5 **correctly**. What is
# actually wrong is one step further on and is a different kind of error: the
# frame bundle's group **cannot serve as a twisting group at all** -- the twist
# would be the tangential structure itself. And even that is **not new**:
# C127 §0 finding 8(ii) already diagnosed exactly this type error ("the frame
# bundle is part of the tangential structure, not an independent `BG`-twist"),
# in a different candidate, and nothing propagated it forward into Z1. This
# round's contribution is the propagation, not the diagnosis.
#
# ⚠️ **SEPARATE FINDING #2 -- ALSO NARROWED.** `ι` exchanges `SU(2)_a` and
# `SU(2)_b` is **not new**: it is C125 `A2`, and C127 §5b already used it.
# What is new is only its consequence here -- that on the mapping torus of `ι`
# any isometry-derived gauge datum has **swap monodromy**, so the twist bundle
# cannot be "the `SU(2)_b` bundle", and the honest base group is
# `Isom(S³) = O(4)` (whose identity component is `SO(4) = (SU(2)_a×SU(2)_b)/Z₂`
# and whose other component realizes the swap), i.e. a **semidirect** rather
# than a direct product. §4's theorem covers that; the phrase
# `Pin^± ×_{Z₂} G` as literally written does **not**, and §4a says so.
#
# NOT covered: which Pin type the fermion content SELECTS (round95 = C127's
# ingredient 2, untouched); any anomaly evaluation; any 13D statement; whether
# `M_ι` is the right manifold (the point above); `N_gen=3`; Tom Lawrence's Part 5.

**Verdict (2026-09-02; TWO independent FL Step 8a skeptic passes RUN,
context-blind, differently-worded -- Paraphrase-Sensitivity Probe. Both
returned `WEAKENED`, CONCORDANT: the MATHEMATICS confirmed by both, the RECORD
and the EVIDENCE APPARATUS cut back by both. 23 findings; 22 accepted and
repaired, 1 tool-verified and DISMISSED. Full matrices in §0):**
`AS_A_THEOREM_ABOUT_M_iota_THE_TWISTED_STRUCTURE_EXISTS_UNIFORMLY_IN_G__FOR_EVERY_LIE_GROUP_G_WITH_A_CENTRAL_ORDER_2_ELEMENT_AND_EVERY_Gbar_BUNDLE_BOTH_PIN_PLUS_AND_PIN_MINUS_TWISTED_STRUCTURES_EXIST_EXACTLY_TWO_OF_EACH_OVER_ANY_FIXED_UNDERLYING_PAIR__BUT_AS_AN_ANSWER_TO_Z1_THIS_IS_CONDITIONAL_ON_M_iota_BEING_THE_DAI_FREED_OBJECT_AND_THAT_CONDITION_IS_ADVERSELY_INDICATED_NOT_MERELY_UNTESTED_BECAUSE_M_iota_IS_4_DIMENSIONAL_AND_C127_SECTION_4s_OWN_VERIFIED_DIMENSION_AUDIT_LISTS_OMEGA_13_14_15_AND_5_6_AND_NEVER_OMEGA_4__ROUTE_1_OBSTRUCTION_THEORY_B_OF_A_Z2_CENTRAL_EXTENSION_OVER_B_OF_ITS_BASE_IS_A_PRINCIPAL_K_Z2_1_FIBRATION_SO_THERE_IS_EXACTLY_ONE_OBSTRUCTION_AND_IT_IS_THE_PULLBACK_OF_THE_EXTENSION_CLASS_INTO_H2_OF_M_WHATEVER_G_IS_MECHANISM_FROM_DEBRAY_YU_LEMMA_3_9_READ_THIS_SESSION_THOUGH_THAT_LEMMAS_STATEMENT_IS_ORIENTED_AND_SPIN_AND_SU8_SO_ONLY_THE_MECHANISM_TRANSFERS__AND_H2_OF_M_iota_VANISHES_FOR_EVERY_ABELIAN_COEFFICIENT_GROUP_BECAUSE_H2_HOMOLOGY_IS_ZERO_AND_H1_IS_FREE_AND_H3_WITH_INTEGER_COEFFICIENTS_IS_ZERO_TOO_SO_THE_BOCKSTEIN_ESCAPE_CLOSES__ROUTE_2_CONSTRUCTIVE_S3_TIMES_R_IS_PARALLELIZABLE_AND_EVERY_Gbar_BUNDLE_ON_IT_IS_TRIVIAL_BECAUSE_PI2_OF_ANY_LIE_GROUP_VANISHES_SO_THE_STRUCTURE_IS_A_LIFT_OF_ONE_MONODROMY_MAP_THROUGH_A_DOUBLE_COVER__THE_TWO_ROUTES_HAVE_DISJOINT_CITATIONS_BUT_A_SHARED_STRUCTURAL_CAUSE_S3_IS_2_CONNECTED_AND_PARALLELIZABLE__NON_VACUITY_DEMONSTRATED_TWISTING_FLIPS_THE_ANSWER_IN_BOTH_DIRECTIONS_ON_OTHER_MANIFOLDS_CP2_RESCUED_AND_S2xS2_DESTROYED__ENTITY_HALF_OF_THE_ZERO_SIGNAL_GATE_FAILS_G_IS_NOT_NAMEABLE_FROM_FROZEN_CONTENT_AND_THE_ROUND_SURVIVES_ONLY_BY_UNIFORMITY_WHICH_IS_A_POST_HOC_READING_OF_ITS_OWN_PRE_REGISTERED_KILL_CRITERION_RECORDED_AS_SUCH__FIRST_DRAFTS_ACCUSATION_THAT_C129s_Z1_MISATTRIBUTED_TO_C128_IS_WITHDRAWN_C129_CHAINED_C127_SECTION_5a_CORRECTLY_THE_REAL_ERROR_IS_A_TYPE_ERROR_ALREADY_DIAGNOSED_BY_C127_FINDING_8ii_AND_NEVER_PROPAGATED__Z1_CLOSED_FOR_EXISTENCE_CONDITIONALLY_ON_THE_MANIFOLD__Z2_NOW_BLOCKED_ON_TWO_THINGS_ROUND95_AND_NAMING_G`

**Status:** OB1 stays `PARKED`. No reopen condition met. C125's `FALSIFIED`,
C126's `WEAKENED`, C127's `BLOCKED`, C128's `OUTCOME_B`, C129's verdict all
stand, untouched. **C129's Relaxation Map item Z1 is closed in its existence
half CONDITIONALLY on `M_ι` being the right object** -- and that condition is
now the round's own top open item (W1), promoted above round95. **Z2 is blocked
on TWO things**, not one: round95's missing link *and* the naming of `G`.

**Completeness:** `PARTIAL`, in seven named respects.

1. **The manifold's relevance is adversely indicated** (header; W1; §9). This
   is the largest single qualifier and it is not a formality.
2. **The specific `G` is `[UNKNOWN]`**, and §3 shows it is not supplied by the
   frozen content. The existence answer is uniform in `G`, so this blocks Z2,
   not this question -- but that uniformity is a **post-hoc reading of a
   pre-registered kill criterion**, recorded as such in §1.
3. Everything is at the **`S³` level**; no 13D statement is made.
4. **Existence is necessary, not sufficient.** No mechanism, no `t`-selector.
5. `π₂(G) = 0` for every Lie group is `[CITED]` (É. Cartan), not re-derived.
6. No bordism group is used as evidence anywhere.
7. **No literature source states the `Pin` analogue of the cited `Spin` lemma.**
   Searched (§2b). §4a derives it by the identical argument. **No novelty
   claimed** for the mathematics (§10a).

**Gate fields assessed:** `PARENT_ACTION_GATE.md` **F4**, and only by removing
an obstruction from a route -- **no mechanism supplied**. F1/F2/F3/F5 reused by
citation. F6, F7 not assessed.

---

## 0. ⚠️ TWO FL Step 8a skeptic passes -- both `WEAKENED`, both CONCORDANT

Both context-blind (`Agent(skeptic, model=opus)`), given `claim.md`,
`decision.md`, both scripts and both JSONs, plus read access to the C127/C128/
C129 files this round makes factual claims *about* (in scope, because one of
those claims was an accusation). **No session history, no reasoning chain.** Run
**twice with differently-worded falsification prompts** (formal register vs.
plain-language register), per the Paraphrase-Sensitivity Probe, because this
round closes a live Relaxation Map item.

> **Pass 1:** `WEAKENED`. Had Bash; ran and corrupted the scripts.
> **Pass 2:** `WEAKENED`. Had **no execution tool**; every check is hand
> derivation, and it **hand-recomputed the entire non-minimal mapping-torus
> complex, the local-coefficient Betti vectors and all of §7** and reproduced
> the JSON exactly. Its own summary: *"The central mathematics is correct and I
> could not break it. The record around it overclaims in eight specific places."*

**CONCORDANT** (both `WEAKENED`, both split math-confirmed / record-weakened),
so the single-run Response Matrix applies and no skeptic-leaning tie-breaker is
needed. They found substantially different defects, which is the argument for
running two. **22 findings accepted and repaired; 1 DISMISSED on tool
verification; none waved through.**

### Findings both passes made independently (strongest signal)

| # | Finding | Response |
|---|---|---|
| **A1** | **Two of the nine headline `VERDICT_INPUTS` fields are logical tautologies -- and they are the two encoding the round's *new* content.** `G16` was `twisted_adjoint(−I, gens, parity=0) == I`, true for **any** matrices since `(−I)e(−I)^{-1} = e`; `G18` was `max‖(−I)p − p(−I)‖`, a scalar commutator, identically `0`. Pass 2 found the tell in the JSON: residual **exactly `0.0`**, not `~1e−16`. So `extension_is_Z2_central_so_single_H2_obstruction` could not be `False`, and `G16` was also a conjunct of both `TWISTED_Pin_*` fields, contributing nothing. | **ACCEPTED, real defect, REPAIRED and DEMONSTRATED.** Both checks deleted. Replaced by (i) a **normality** test that actually conjugates the generator `(−1,z)` by random `(p,q)` and tests membership -- residual `4.4e−16` for central `z`, and **`1.99` for `z = iσ₃`**, so it fires (`G16`/`G16b`); (ii) a **computed kernel order**: enumerate the four elements `(±1,{1,z})` and count classes modulo `⟨(−1,z)⟩` → **2**, with the same routine returning **4** without the identification (`G18`/`G18b`). Verdict field rewired to the conjunction of all four. |
| **A2** | **`no_kunneth_cross_term` is a third tautology, and §12's claimed repair of it did not repair it.** §12 said the first draft's `p·1·p⁻¹·1 − 1` test was *"Repaired: replaced by a shared `commutator_pairing` routine"*. But that routine multiplies tuples **componentwise**, so `mul((p,1),(1,q)) = (p,q) = mul((1,q),(p,1))` and the commutator is the identity for any input. **Still the same tautology, one layer down.** The `Q8` control does not rescue it: `Q8` is encoded as a **1-tuple** where the commutator is a real computation, so "the same routine returns 0 here and 1 there" compares a forced result with a real one **across two different encodings** -- which is §12's own defect 2 ("the answer encoded in the encoding") surviving in PART 2. | **ACCEPTED entire, and the repair is a RETRACTION, not a better measurement.** The field is **deleted from `VERDICT_INPUTS`**. §4a's boldfaced *"The cross-term claim is NOT true by construction... that distinction is measured, not asserted"* is **DELETED as false** -- it also directly contradicted §12's own accounting, which said the opposite four sections later. The honest statement is now given: for a quotient of a **direct** product the cross term vanishes **definitionally**; and pass 2 supplied a better reason nobody had stated -- **for connected `Ḡ`, `H¹(BḠ;𝔽₂) = Hom(π₀Ḡ,𝔽₂) = 0`, so the cross-term group is itself zero and there is nothing to compute.** `Q8` is retained, relabelled: it shows the direct-product hypothesis is **not vacuous**, not that our own check discriminates. |
| **A3** | **The degree sweep is vacuous for 3 of its 5 degrees.** The non-minimal CW model ran only for `deg ∈ {−1,+1}`; `deg ∈ {0,2,7}` existed only in the minimal model, where `D₂ = C₂ ⊕ C₁ = 0` identically, so `H₂ = 0` is a **cell-count artifact surviving any corruption** -- C129's own finding A4, re-committed. §12's boast that the non-minimal model *"was built in from the start rather than retrofitted"* was true for the headline and false where §8 leans on it. | **ACCEPTED, repaired.** The non-minimal model now runs at **every** degree; `G07`/`G08` gate the **whole table** rather than `deg = −1`; new `G09b` requires `H₂ = 0` at every degree in the model where it is a computed rank; new `G09c` requires the degrees to be **distinguishable** (`H₃ = Z/2, 0, Z, 0, Z/6` -- five degrees, **four** distinct values), so the sweep is not degenerate. All five non-minimal rows reproduce the minimal ones exactly. |
| **A4** | **The scope claim "the manifold contributes no constraint at all, bare or twisted" (§9) contradicts §9's own W4 three paragraphs later** (`H⁴(M_ι;Z) = Z/2 ≠ 0`, so a degree-4 obstruction could be nonzero). **Verbatim repeat of C129's skeptic finding A9**, which C129 accepted and *"narrowed everywhere"*. | **ACCEPTED, narrowed everywhere.** Every occurrence now reads "no constraint **via any structure whose existence obstruction is a degree-2 class**". §11's Pearl 1 carried the scope limit already; the kill claim and the headline did not. |
| **A5** | **Provenance labels that do not protect their adjacent rows.** §7's table carried a blanket *"`[VERIFIED]`, exact `𝔽₂` arithmetic in truncated cohomology rings"* over an `M_ι` row the script **explicitly refuses** to evaluate in the ring engine, and whose `w₁ = π^*a ≠ 0` entry is **imported by citation** from C128/C129, not computed here. §4a cited `G20` as *"the same construction with a non-central `z` -- fires"*, but the code never built the quotient; it measured `‖zq − qz‖`, restating the input. | **ACCEPTED both.** §7's `M_ι` row is now labelled separately and its provenance stated per cell. `G20` is **deleted**; `G16b` performs the actual conjugation-and-membership test and fires. This is C129's own Pearl 3 species (a tag not protecting the sentence beside it) and is recorded as a recurrence, not a first. |
| **A6** | **§12's "honest accounting of the checks" is itself incomplete**: it omits `G05, G06, G09, G18, G28` entirely -- including the unfalsifiable `G18` and the headline-conjunct `G28` -- and lists `G32` **twice**, under "fixed-constant controls" *and* under "genuinely discriminating". | **ACCEPTED, rewritten.** §12's accounting now covers every gate exactly once. |

### Findings unique to pass 1 (formal register)

| # | Finding | Response |
|---|---|---|
| **B1** | **"Two routes with disjoint inputs" is inflated at exactly the point it is used as a strength.** Both routes are consequences of a **single** structural fact -- `S³` is 2-connected (route 1: `H¹(S³)=H²(S³)=0`; route 2: `π₁(S³)=0` and `[S³,BḠ]=π₂(Ḡ)`). The two counts of "exactly two" are **the same computation in two languages**: `\|H¹(M;𝔽₂)\| = \|Hom(π₁M,Z/2)\| = 2` *is* the number of lifts of the single monodromy generator. And route 2 still needs PART 2's "`H` is a double cover", which is route 1's input. | **ACCEPTED, all three.** §6's *"from completely different inputs. Cross-check, not a repetition"* is **deleted**. The claim is narrowed to what is true: the **citation** sets are disjoint (withdraw any one source and one route survives); the **structural cause** is shared and is named. C129's own verdict string flags this species ("`WHICH_ARE_THE_SAME_ALGEBRA`") -- recorded as a recurrence. |
| **B2** | **§4's theorem is missing hypotheses.** As stated for "topological groups" it needs `H → K` to admit local sections (automatic for Lie groups); `M` must have the homotopy type of a CW complex; and part 3's "the set of them is a torsor" should read "isomorphism classes of lifts over a **fixed** classifying map". | **ACCEPTED, all stated in §4.** Harmless for `M_ι` (a closed smooth manifold, all groups Lie), but a theorem quoted out of this file would need them. |
| **B3** | **`ext_into`'s torsion branch is dead in this round** (every UCT call has `H₂ = 0` or free `H₁`), and *"returning `FGAb(0,[])` for `coeff != 0` is a real UCT bug -- `Ext¹(Z/2,Z/2) = Z/2`, not 0"*. | **SPLIT: the "dead branch" half ACCEPTED; the "real bug" half DISMISSED, tool-verified.** Ran it: `Ext¹(Z/2,Z/2) = Z/2`, `Ext¹(Z/2,Z) = Z/2`, `Ext¹(Z/4,Z/2) = Z/2`, `Ext¹(Z,Z/2) = 0`, `Hom(Z/2,Z/4) = Z/2` -- **all correct**. Per `audit-verification-gate.md`, an agent's `[VERIFIED]` is this session's `[INFERRED]` until re-checked, and this is the one finding re-checking overturned. The **untested-in-context** half stands and is recorded in §12. |
| **B4** | **Recomposition gate:** the four sub-claims are individually true, but recomposition adds (i) the assumption that the structure the physics needs **is** in this family **on this manifold**, and (ii) a quantifier shift where §9/Pearl 1 drop the degree-2 scope. | **ACCEPTED, and answered in §13a rather than argued away.** The conjunction licenses a narrower statement than the first draft's headline, and that narrower statement is now what the headline says. |

### Findings unique to pass 2 (plain register)

| # | Finding | Response |
|---|---|---|
| **C1** | **THE SHARPEST FINDING. The wrong-manifold risk is adversely indicated, not open, and the file it says it read in full already contains the arithmetic that says so.** C127 §4's dimension audit lists `Ω₁₃,Ω₁₄` / `Ω₁₄,Ω₁₅` / `Ω₅,Ω₆` -- **`Ω₄` appears in none.** A 4-manifold is the home of a *3-dimensional* theory's anomaly and this project has no 3D theory. Meanwhile the all-caps verdict string carried **five** other qualifiers and **zero** dimension caveat -- *"the sentence that will be grepped out of the record later"*, which is C129's own finding `C1` re-committed one round later, after C129 fixed it by putting `PARALLELIZABLE` **into** its string. | **ACCEPTED, and it reshapes the document.** The dimension caveat is now in the **header**, in the **verdict string**, in **Completeness item 1**, and the Status line's "Z1 CLOSED" is made **conditional**. W1 is promoted to the round's top open item, above round95, and Pearl 2 is rewritten from "untested" to "adversely indicated". |
| **C2** | **Finding #1's accusation against C129 is mis-framed, and C130's own body says so.** C127 §5a's table gives "frame bundle's group" as the consequence-for-`G` of the C125 reading, so C129 chained C127 §5a + C128 §5 **correctly**. C130's own §3b conceded it (*"What C128 §5 settles is which mathematical category `∇^t` belongs to"*) while its header said the opposite. And the thing C130 got right -- that the frame bundle's group is not a well-formed **twisting** group -- is a **type error in an inference** already recorded as **C127 §0 finding 8(ii)**, which C130 cites in the very row where it claims novelty. | **ACCEPTED ENTIRE. The accusation is WITHDRAWN and the header is rewritten.** The novelty row is downgraded from *"New, and a correction to this project's own record"* to *"the propagation of an already-recorded diagnosis into a Relaxation Map row"*. |
| **C3** | **§3b's *"the frozen content supplies no independent gauge bundle to twist by at all"* is over-broad**, contradicted at that generality by C127 §3c: `G = SU(3)` from the `S⁶` twist bundle is nameable **and essential** (`c₃ = 2 ≠ 0`), and it is what makes C127's own Entity field pass. | **ACCEPTED, and repaired with the two narrowings the pass itself supplied, both of which make the corrected point sharper than the over-broad one:** (i) `SU(3)` lives on `S⁶`, which `M_ι` does not touch; (ii) **`Z(SU(3)) = Z₃` has no element of order 2**, so it cannot supply the `Z/2`-central extension a half-integral rep requires. §3b now says this. |
| **C4** | **Semidirect vs direct.** The universally-quantified headline is about `Pin^± ×_{Z₂} G`, a quotient of a **direct** product, while §3c says the honest object is **semidirect** -- not of that form for any `G`. Three **mutually inconsistent** group expressions appear for the same object (`(SO(3)_a×SO(3)_b)⋊Z₂` in the header, `O(n)⋉Ḡ` in §3c, `O(4)⋉(SO(3)×SO(3))` in §13a), and the header's is wrong: `Isom₀(S³) = (SU(2)_a×SU(2)_b)/Z₂ = SO(4)` is a **double cover** of `SO(3)×SO(3)`. | **ACCEPTED, all of it.** One expression is used throughout now: **`Isom(S³) = O(4)`, identity component `SO(4) = (SU(2)_a×SU(2)_b)/Z₂`, with `ι` in the other component realizing the swap.** §4a states explicitly that the theorem covers the semidirect case but the phrase `Pin^± ×_{Z₂} G` does not, so the criteria blockquote is scoped where it stands rather than in a footnote. |
| **C5** | **§5c is offered as the check that discharges C4 and does not.** For a **central** `Z/2` kernel the coefficients are **untwisted by definition** -- `π₁` acts trivially on a central kernel -- so the swap local system on `M` is not the obstruction's home. The header's *"Checked rather than assumed... so the finding does not change the answer"* rested on a computation of the wrong group. | **ACCEPTED, a real category error, repaired.** §5c is relabelled: the actual resolution is the one-liner (**the kernel is central ⟹ `Z/2` coefficients are untwisted ⟹ `H²(M;Z/2) = 0` suffices**), now stated as the argument; the swap computation is demoted to what it is -- an **independent robustness check on a different object**, still worth having because it is the only computation specific to this background. |
| **C6** | **A sabotage test that slips through completely: neuter the local-coefficient monodromy** (force `ρ = id`). `G29` checked only that both degree-2 entries are 0 -- true for the trivial system too; `G30`'s control **never exercised a nontrivial `ρ`**; and in the minimal model `ranks[2] = k·(C₂+C₁) = 0` identically, so half of `G29` could not fail. Result: **all gates green, headline unmoved**, while destroying the one computation §10a calls specific to this background. Second slip-through: make `commutator_pairing` key on **tuple length**. | **ACCEPTED, repaired three ways and then RE-TESTED as an injection.** New `G29b` gates the non-minimal model separately; new **`G29c` requires the swap and trivial monodromies to give DIFFERENT Betti vectors** (`[1,1,0,1,1]` vs `[2,2,0,2,2]`) -- which is exactly what dies under neutering; `G30` now runs the control with a nontrivial `ρ` as well. **The pass's own corruption is now injection 9 and is caught by `G29c`.** The tuple-length slip-through is moot: the tautological use is deleted (A2). |
| **C7** | **The cited lemma does not cover the case.** Debray-Yu Lemma 3.9 **as quoted** is about (a) an **oriented** manifold, (b) **Spin**, (c) **`SU₈`**. This round's case is **non-orientable** (`w₁ ≠ 0` is the whole premise), **Pin**, arbitrary `G`. Two gaps are acknowledged (Pin, general `G`); **the orientability gap is never separately named.** The tier table said `[VERIFIED-tool, PRIMARY] | the mechanism AND ITS STATEMENT` -- only the **mechanism** transfers. | **ACCEPTED, repaired.** §2a and §4 now name all three gaps, orientability included; the tier line is corrected to "**the mechanism**"; §4's tag stays `[INFERRED from VERIFIED-tool]`, which was already right. |
| **C8** | **The "independent corroboration" of the Pin criteria is asserted, not shown.** The claim that arXiv:2405.04649 *"does not cite Kirby-Taylor for these two lines"* was offered with no evidence -- the exact species of C129's own finding A8. | **ACCEPTED, weakened to what is checkable.** In the passage read, items (1) and (2) cite `[Pet68]` and `[Sto88]` for the Thom-spectrum splittings and state the two criteria **without attribution at that point**; Kirby-Taylor is not cited there. That is **a second author stating a standard fact**, i.e. corroboration of C129's reading -- **not** an independent derivation. §2a now says exactly that. |
| **C9** | **Smaller false statements.** (i) §8's *"§5's computation sees only `deg f mod 2`"* is falsified by §5's own output: `H₃ = Z/2` at `deg −1` but `Z/6` at `deg 7`, so `H³(M;Z/3)` differs. (ii) The verdict string's *"for every local system"* was supported by **two examples**, one of which is identically zero for any `ρ`. (iii) *"SECOND_NEW_FINDING"* -- the `ι`-swap fact is C125 `A2`, already used by C127 §5b. | **ACCEPTED all three.** (i) §8 now says: the **`H²`** claim is degree-independent; **`H³` is not**, and the `Z/6` row is printed. (ii) The **general** statement is now argued, not exemplified -- the Wang squeeze gives `H²(M;L) = 0` for **any** local system because `L` restricts to a constant system on the simply-connected fibre and `H¹(S³;L\|) = H²(S³;L\|) = 0` -- with C129's finding B3 credited as the prior statement and the two computations demoted to checks. (iii) The header's finding #2 is narrowed to its consequence only. |
| **C10** | **The pre-registered gate is graded by the party being graded.** `claim.md` kill criterion (b) says the round *"fails its own purpose"* if it cannot name `G` and computes anyway, and *"should return `BLOCKED`"*. C130's Entity field **FAILS** and it returns **EXISTS**, on a uniformity ground the pass accepts as sound -- but which is a **post-hoc reinterpretation of a pre-registered criterion, made by the round about itself**, over a family (`Z/2`-central extensions of `O(n)×Ḡ`) that §3c says the honest entity sits outside of *as instantiated*. | **ACCEPTED and RECORDED rather than argued away**, in §1 and in Completeness item 2. This is the same species as C128 §9b's own recorded pre-registration defect. The uniformity ground is retained because both passes judged it sound; the fact that the round graded itself against its own kill criterion is now permanent record. |

**Nothing dismissed without tool verification. One finding (B3's "real UCT bug"
half) DISMISSED after running the function against five textbook values. No
finding moved the mathematical answer; twelve moved what the record is allowed
to say about it, and two (C1, C2) overturned framing the first draft had put in
its headline.**

---

## 1. Zero-Signal Gate (Step −5), run BEFORE any computation

`claim.md` requires this split honestly and permits `BLOCKED`. One field fails.

| Field | Status | Content |
|---|---|---|
| **Entity** | **SPLIT: PASS on the structure TYPE, FAIL on the specific `G`** | *Passes:* C127 §0 finding 1 establishes `R(0) = (1,2)` is half-integral under `SU(2)_b`, its central `−1` acting as `(−1)^F` -- so the identification is by a **central element of order exactly 2**, i.e. the structure is a **`Z/2`-central extension**. That names the *kind* of object with no ambiguity. *Fails:* the **group `G` is not nameable from the frozen content** (§3b). |
| **Falsifiable predicate** | **PASS** | "the pullback of the extension class `ζ` to `H²(M_ι;Z/2)` is zero" -- a yes/no about an element of a specific group, with a cited general formula (§4). |
| **Measurable outcome** | **PASS** | `H²(M_ι;A)` computed for eight coefficient groups in two CW models at five degrees, plus local coefficients, plus `H³(M_ι;Z)` (§5). |

**Gate result: PASS on the predicate, and the round proceeds -- but this is a
post-hoc reading of its own pre-registered kill criterion, and is recorded as
such** (skeptic finding C10). `claim.md` (b) says a round that *"cannot precisely
name `G` ... but proceeds to compute anyway"* fails its purpose. The ground for
proceeding is that **§4's theorem is uniform in `G`**, so the answer does not
depend on the missing ingredient; both skeptic passes independently judged that
ground sound. It remains a self-grading, and it is why **Z2 -- which genuinely
needs `G` -- is recorded as `BLOCKED (missing ingredient: the twisting group
`G`, named)`** in §9 rather than merely "not attempted".

---

## 2. Steps −4 / −3 -- literature first, actually performed

### 2a. The general obstruction formula -- retrieved and read this session

**[VERIFIED-tool, PRIMARY for the MECHANISM, retrieved and read this session]**
A. Debray and M. Yu, *What bordism-theoretic anomaly cancellation can do for U*,
arXiv:2210.04911v2, **Lemma 3.9** and its proof:

> *"Let `M` be an oriented manifold and `P → M` be a principal `SU₈/{±1}`-bundle.
> The data of a spin-`SU₈`-structure inducing this orientation and principal
> `SU₈/{±1}`-bundle is equivalent to a trivialization of `w₂(M) + a(P)`, where
> `a` is the unique nonzero element of `H²(B(SU₈/{±1});Z/2)`."*

and, in the proof, the mechanism this round actually needs -- stated there for
an **arbitrary space `X`**, not just a manifold:

> *"Apply the classifying space functor to the short exact sequence (3.7) to
> obtain a fibration `B(Spin ×_{±1} SU₈) → B(SO × SU₈/{±1}) → K(Z/2,2)` …
> implying that for any space `X` and map `f : X → B(SO × SU₈/{±1})`, the data
> of a lift of `f` to a map `f̃ : X → B(Spin ×_{±1} SU₈)` … is equivalent data
> of a null-homotopy of `(w₂ + a)∘f`."*

> ⚠️ **SCOPE, stated because skeptic finding C7 caught it missing: the quoted
> STATEMENT is (a) oriented, (b) `Spin`, (c) `SU₈`. This round's case is (a)
> NON-orientable -- `w₁ ≠ 0` is the whole premise -- (b) `Pin`, (c) arbitrary
> `G`. All three gaps are real. What transfers is the MECHANISM (the
> `K(Z/2,2)`-fibration), which is stated in the proof at full generality in
> `X` and is insensitive to all three. §4 is therefore tagged
> `[INFERRED from VERIFIED-tool]`, not `[VERIFIED-tool]`.**

Same paper, **Remark 3.11**, recorded because it cuts *against* the easy version:

> *"If we knew `a` was `w₂` of the associated vector bundle to a representation
> `ρ` of `SU₈/{±1}`, then Lemma 3.9 would follow from [DDHM23, Corollary 10.23].
> However, no such `ρ` exists."*

**Its honest weight** (skeptic finding, accepted): this is **scope-bearing, not
load-bearing**. Nothing computed here changes if it is false -- on a manifold
with `H²= 0` both formulations give the same verdict. It matters only because it
justifies stating §4 at the level of `Z/2`-central extensions rather than of
vector-bundle twists. **And it cuts back:** §7, the only place a twist is ever
exercised, uses **exclusively vector-bundle twists** (`w₂(E) = h, a, a+b, a²`),
i.e. the strictly-less-general form. So the non-vacuity demonstration is one
notch narrower than the theorem it certifies. Recorded, not hidden.

**[VERIFIED-tool, SECONDARY -- cites Debray-Yu]** N. Kuroda, arXiv:2504.15014v1,
§4.1, the same statement in the form this round uses:

> *"given an oriented manifold `M` and a map `f_M : M → BH`, the obstruction to
> inducing a `Spin-G` structure is given by `w₂(M) + f_M^* ζ`. Here, `ζ` is the
> element of `H²(BH;Z₂)` that corresponds to the central extension
> `{±1} → G → H`, as described in [7, Lemma 3.9]."*

**[VERIFIED-tool]** A. Debray et al., *The Smith Fiber Sequence and Invertible
Field Theories*, arXiv:2405.04649v2, §6 -- the `Pin` criteria and the general
"twisted spin structure" framework:

> *"(1) A pin`-` structure is a trivialization of `w₂(M) + w₁(M)²`, with no
> condition on `w₁`. … (2) A pin`+` structure is a trivialization of `w₂(M)`,
> with no condition on `w₁`."*
> *"(5) A spin`h` structure is data of a trivialization of `w₁(M)` and a rank-3
> oriented vector bundle `E → M` and a trivialization of `w₂(M) − w₂(E)`."*

**Corroboration, at its true strength** (skeptic finding C8): in the passage
read, items (1) and (2) cite `[Pet68]` / `[Sto88]` for the *Thom-spectrum
splittings* and state the two criteria **without attribution at that point**;
Kirby-Taylor is not cited there. That makes this **a second author stating a
standard fact**, which corroborates C129 §2a's reading -- it is **not** a second
independent derivation, and the first draft's implication that it was is
withdrawn. Item (5) is `Spin^h = Spin ×_{Z₂} SU(2)`, i.e. C127 finding 1's
structure, with obstruction `w₂(M) + w₂(E)`.

**[VERIFIED-tool]** Wang-Wen-Witten, arXiv:1810.00844v4 §2.4 -- the definition in
C127 finding 1's exact shape: *"`Spin_{SU(2)}(4) = (Spin(4) × SU(2))/Z₂`"*,
*"`Z₂` is embedded … as the product of the element `(−1)^F ∈ Spin(4)` and the
element `−1 ∈ U(1)`"*. **[VERIFIED-tool]** Beckett, arXiv:2511.03627v2 §1 --
*"`Spin^G(s,t) := (Spin(s,t) × G)/Z₂` by a Lie group `G` with a central subgroup
isomorphic to `Z₂`"*, the generality this round needs.

### 2b. The `Pin`-twisted case specifically -- searched, no special-case source

Searched this session for the `Pin` analogue of Lemma 3.9 as a named lemma, and
for this manifold's twisted result. **Neither retrieved.** The general framework
of arXiv:2405.04649 §6 covers it and §4a derives it by the identical
`K(Z/2,2)`-fibration argument -- a two-line extension, not a new idea. **No
novelty claimed** (§10a). Folklore is the likeliest explanation.

**Not consulted:** Kirby-Taylor directly (C129 did, this session); Freed-Hopkins;
[DDHM23]; ABP67/Gia71. **None of the five papers above read in full**; the
sections read are named.

---

## 3. Naming `G` -- the round's first job, and it fails

### 3a. What IS fixed

**[VERIFIED, direct read this session, C127 `decision.md` §0 finding 1]**
`R(0) = ker(D_{S³},t=0) = (1,2)` is **half-integral** under `SU(2)_b`, its
central `−1` acting as `(−1)^F`; at `t=1` it is `(2,1)` under `SU(2)_a`
[CITED, C38 via C125 §3a]. Two consequences, both used:

1. The identification is by an element of **order exactly 2**, central. Whatever
   `G` is, the structure is a **`Z/2`-central extension**. *This is what makes
   §4 applicable, and it is all §4 needs.*
2. `σ` (label swap) carries the `t=0` factor to the `t=1` one, so the structure
   **type** is `t`-independent. §8.

### 3b. What is NOT fixed -- and the correction, rewritten after the skeptic passes

**The first draft accused C129's Z1 row of misattribution. That accusation is
WITHDRAWN** (skeptic finding C2). Checked against the sources:

* C129's Z1 reads: *"Prerequisite: knowing `G`, which C128 §5 settled as the
  **frame bundle's** group."*
* **C127 §5a's own table** [VERIFIED, direct read this session] gives, in its
  consequence-for-`G` column for the C125 reading, the words *"frame bundle's
  group"*. C128 §5 settles that the frozen ansatz uses **C125's category**.
* **So C129 chained C127 §5a + C128 §5 correctly.** No misattribution.

**What is actually wrong is one step further on, and is a different kind of
error.** The frame bundle's group cannot serve as a **twisting** group:
`Pin^± ×_{Z₂} G` with the frame bundle playing the role of the `Ḡ`-bundle
**double-counts the tangential data** -- the "twist" would be the tangential
structure itself. **And this is not new either:** C127 §0 finding 8(ii) already
recorded exactly this type error --

> *"the frame bundle is part of the **tangential structure**, not an independent
> `BG`-twist, and the parenthetical silently swaps frame-bundle group for
> isometry group"*

-- against a different candidate, and **nothing propagated it forward into Z1.**
This round's contribution is the propagation, not the diagnosis (§10a).

**The other candidate, and why it is also not available:**

| reading | `G` | status |
|---|---|---|
| (i) the Z1 gloss: `G` = the frame bundle's group | `O(n)` | **Type error**, per C127 §0 finding 8(ii) above. |
| (ii) `G = SU(2)_b` (`t=0`), `Ḡ = SO(3)_b`, from the isometry group | `SU(2)` | **Conditional on the contested `Isom₀` KK premise** [CITED; C127 §3b records the downgrade, C125 rebuilt its argument to avoid it]. Also runs into §3c. |
| (iii) `G = SU(3)` from the `S⁶` twist bundle (C127 §3c: nameable **and essential**, `c₃ = 2 ≠ 0`) | `SU(3)` | **Excluded, twice over.** It lives entirely on `S⁶`, which `M_ι` does not touch; and **`Z(SU(3)) = Z₃` has no element of order 2**, so it cannot supply the `Z/2`-central extension a half-integral rep requires. |

> **Verdict on the Entity field: `[UNKNOWN]`.** The first draft's blanket *"the
> frozen content supplies no independent gauge bundle to twist by at all"* is
> **withdrawn as over-broad** (skeptic finding C3) -- C127 §3c names one. The
> correct statement is narrower and sharper: **no `G` available in the frozen
> content is both located where `M_ι` can see it and equipped with a central
> element of order 2.**

### 3c. `ι` exchanges the two `SU(2)` factors -- and the group, written once

[CITED, C125 `A2`, already used by C127 §5b -- **not new**, per skeptic finding
C9(iii); only the consequence below is this round's] `ι∘φ_{a,b}∘ι = φ_{b,a}`.

`M_ι` is the mapping torus of `ι`, so going once around the `S¹` any datum
derived from the isometry group comes back **swapped**. Written once, correctly
(skeptic finding C4 found three inconsistent versions in the first draft):

> **`Isom(S³) = O(4)`. Its identity component is
> `SO(4) = (SU(2)_a × SU(2)_b)/Z₂`. `ι` lies in the other component and its
> conjugation action swaps the two `SU(2)` factors.** So the honest base group
> for reading (ii) is a **semidirect** rather than a direct product.

Consequences:

* there is **no `SO(3)_b`-bundle on `M_ι`** in the naive sense;
* the fermion content is `(1,2)` at `t=0` and `(2,1)` at `t=1`, and the swap
  monodromy is exactly what makes the fermion bundle over `M_ι` well defined --
  the *pair* structure C127's A2 pointed at, reached from another direction;
* **`Pin^± ×_{Z₂} G` as literally written does NOT cover this object** (skeptic
  finding C4). **§4's theorem does** -- a `Z/2`-central extension of a semidirect
  product is still a `Z/2`-central extension -- and §4a says so where the
  criteria are stated, not in a footnote. `[INFERRED]`.

---

## 4. The theorem -- where a twisted obstruction can and cannot live

**Theorem (C130).** *Let `1 → Z/2 → H → K → 1` be a central extension of Lie
groups (or of topological groups such that `H → K` admits local sections), with
class `ζ ∈ H²(BK;Z/2)`. Let `M` have the homotopy type of a CW complex and carry
a `K`-structure classified by `f : M → BK`. Then:*

1. *an `H`-structure refining `f` exists **iff** `f^*ζ = 0` in `H²(M;Z/2)`;*
2. *there are **no higher obstructions**;*
3. *the set of isomorphism classes of such structures **over the fixed `f`** is
   a torsor over `H¹(M;Z/2)`.*

**Proof.** `B(−)` applied to the extension gives a fibration `BH → BK` with fibre
`B(Z/2) = K(Z/2,1)`, principal, classified by `ζ : BK → K(Z/2,2)`. Lifting `f` is
exactly null-homotoping `ζ∘f`, i.e. `f^*ζ = 0`; lifts over a fixed `f`, up to
homotopy, are `[M, K(Z/2,1)] = H¹(M;Z/2)`. The fibre has homotopy concentrated in
degree 1, so the obstruction sequence has one term. ∎

*Hypotheses (1)-(3) were missing from the first draft and are stated per skeptic
finding B2. All are satisfied here: `M_ι` is a closed smooth manifold and every
group involved is Lie.*

**This is not this round's invention** -- it is Debray-Yu Lemma 3.9's own proof
restated at general `G`, with the three scope gaps of §2a named.
`[INFERRED from VERIFIED-tool]`.

### 4a. Instantiation

Put `H = (Pin^±(n) × G)/⟨(−1,z)⟩`, `K = O(n) × Ḡ`, `Ḡ = G/⟨z⟩`, `z` central of
order 2 in `G`. Then:

* **`H → K` is a `Z/2`-central extension.** `[VERIFIED]`, and now by a check
  that can fail (the first draft's version could not -- skeptic finding A1):
  the identification subgroup `⟨(−1,z)⟩` is shown **normal** by explicit
  conjugation and membership testing (deviation `4.4e−16` for central `z`;
  **`1.99`, i.e. firing, for `z = iσ₃`**), and the kernel's **order is computed
  as 2** by enumerating the classes of `(±1,{1,z})`, with the same routine
  returning **4** without the identification.
* **The extension class is `ζ = ζ_± + ζ_G`**, with `ζ_± ∈ {w₂, w₂+w₁²}` and
  `ζ_G` the class of `1 → Z/2 → G → Ḡ → 1`, by restricting to the two Künneth
  factors. **The Künneth cross term `H¹(BO(n))⊗H¹(BḠ)` vanishes, for two
  reasons, and NEITHER is a measurement** *(the first draft claimed it was
  measured; that claim is deleted -- skeptic finding A2)*: (i) for **connected**
  `Ḡ`, `H¹(BḠ;𝔽₂) = Hom(π₀Ḡ,𝔽₂) = 0`, so the cross-term **group is zero**;
  (ii) for general `Ḡ`, `H` is a quotient of a **direct** product, so lifts of
  the two factors commute **definitionally**. That the direct-product hypothesis
  is not vacuous **is** measured: `Q8 → Z/2×Z/2` is a `Z/2`-central extension of
  a **product** whose commutator pairing is **1**, so centrality alone does not
  suffice. `[INFERRED]` for the decomposition; `[VERIFIED]` for the `Q8` witness.
* Hence, by §2a's `Pin` criteria:

  > **`Pin^+ ×_{Z₂} G` exists ⟺ `w₂(M) + c(E) = 0`**
  > **`Pin^- ×_{Z₂} G` exists ⟺ `w₂(M) + w₁(M)² + c(E) = 0`**
  >
  > with `c(E) := f_E^*ζ_G ∈ H²(M;Z/2)`; `c(E) = 0` recovers C129's bare case.
  >
  > ⚠️ **SCOPE, in the same box as the criteria** (skeptic finding C4): this
  > form assumes `K` is a **product**. For §3c's honest object -- a semidirect
  > product, where `ι` swaps the gauge factors -- **the decomposition above does
  > not apply**, and the criteria must be read from `ζ` directly. **The
  > Theorem still applies** (the extension is still `Z/2`-central), so the
  > obstruction is still a single class in `H²(M;Z/2)` -- and on `M_ι` that
  > group is zero, so the verdict is unchanged either way.

### 4b. What this rules out -- `claim.md`'s trap, answered directly

| worry from `claim.md` | answer |
|---|---|
| obstruction on the total space of `E → M` rather than on `M` | **No.** Obstruction theory for lifting the *classifying map* lives on the base; `H²(E;𝔽₂)` is a different question and not what a structure on the `(d+1)`-manifold requires. |
| a class not factoring through `H²(M;𝔽₂)` | **Only for a non-`Z/2` central kernel.** For `Z/n` the same argument puts it in `H²(M;Z/n)` -- and §5a computes `H²(M_ι;A) = 0` for **every** abelian `A`, closing that escape. |
| higher obstructions | **None.** Fibre `K(Z/2,1)` has one nonzero homotopy group. |
| twisted / local coefficients (§3c's semidirect base) | **Not the obstruction's home**, because the kernel is **central**, so `π₁` acts trivially on it and the `Z/2` coefficients are untwisted (skeptic finding C5 -- the first draft got this backwards). §5c computes the local-coefficient case anyway, as an independent check on a different object. |
| the "choose your own `E`" version, whose obstruction can move to a **Bockstein** in `H³(M;Z)` (the `Spin^c ⇒ W₃` species) | **Closed:** `H³(M_ι;Z) = 0` (§5b). |

---

## 5. The obstruction groups -- recomputed here, not inherited

`c130_twisted_pin_obstruction.py` **imports no project code and reuses no C129
output as an input.** Where the numbers overlap with C129 they agree exactly;
that agreement is a cross-check, not a dependency. Skeptic pass 2 additionally
**hand-recomputed the entire non-minimal complex and every table below** without
an execution tool and reproduced the JSON exactly.

### 5a. `H²(M_f;A) = 0` for **every** abelian `A`

Integral homology of the mapping torus of a self-map of `S³` of degree `d`, by
Smith normal form, in **two CW models at every degree** *(the first draft ran the
non-minimal model only at `d = ±1`; skeptic finding A3)*:

| `d` | cells (non-min.) | `H_*(M_d;Z)` | `𝔽₂`-Betti | `H₂` in the non-minimal model |
|---|---|---|---|---|
| **−1 (`= M_ι`)** | `[1,2,2,2,1]` | `Z, Z, 0, Z/2, 0` | `1,1,**0**,1,1` | **0, a computed rank** |
| 0 | `[1,2,2,2,1]` | `Z, Z, 0, 0, 0` | -- | **0, computed** |
| +1 | `[1,2,2,2,1]` | `Z, Z, 0, Z, Z` | -- | **0, computed** |
| 2 | `[1,2,2,2,1]` | `Z, Z, 0, 0, 0` | -- | **0, computed** |
| 7 | `[1,2,2,2,1]` | `Z, Z, 0, Z/6, 0` | -- | **0, computed** |

The minimal model agrees at every degree; `d² = 0` exactly in both. **The
non-minimal rows are the ones that carry evidential weight**: there `C₂ = Z²`
and `H₂ = 0` is a rank computation, not "there are no 2-cells". And the sweep is
**not degenerate** -- `H₃` takes **four** distinct values across the five
degrees (`Z/2, 0, Z, 0, Z/6`), gated by `G09c`.

Then by the universal-coefficient theorem:

```
H₂(M_ι;Z) = 0   and   H₁(M_ι;Z) = Z  (free)
  =>  Hom(H₂,A) = 0  and  Ext¹(Z,A) = 0  for EVERY abelian A
  =>  H²(M_ι;A) = 0  for every abelian A.
```

Computed for `A ∈ {Z, Z/2, Z/3, Z/4, Z/5, Z/8, Z/9, Z/16}` in both models: **all
zero.** `[VERIFIED]`, exact arithmetic. **The eight values are a check on the
implementation, not accumulating evidence** -- the proof above covers every `A`,
including non-finitely-generated ones.

**The pipeline is not degenerate:** the identical code returns
`H²(CP²×S¹;𝔽₂) = Z/2 ≠ 0` (`G13`) and `H³(M_ι;𝔽₂) = Z/2 ≠ 0` (`G12`).

### 5b. `H³(M_ι;Z) = 0`

`H³(M;A) = Hom(H₃,A) ⊕ Ext¹(H₂,A) = Hom(Z/2,A) = A[2]`. Computed:
`Z, Z/3, Z/5, Z/9 → 0`; `Z/2, Z/4, Z/8, Z/16 → Z/2`. `[VERIFIED]`. So the
Bockstein-type escape of §4b closes. (Belt and braces: `w₂ = 0` already, so
`β(w₂) = 0` regardless.)

### 5c. Local coefficients -- relabelled, because the first draft mis-sold it

**What actually discharges §3c** (skeptic finding C5, a real category error in
the first draft): the kernel `Z/2` is **central**, so `π₁(M)` acts trivially on
it and the coefficients in `H²(M;Z/2)` are **untwisted by definition**. The swap
local system is not the obstruction's home. `[INFERRED]`, one line.

**The general local-coefficient statement, argued rather than exemplified**
(skeptic finding C9(ii)): `π₁(S³) = 0`, so any local system `L` on `M_f`
restricts to a **constant** system on the fibre; the Wang sequence then squeezes
`H²(M_f;L)` between `H¹(S³;L|) = 0` and `H²(S³;L|) = 0`, so **`H²(M_f;L) = 0`
for every local system.** `[INFERRED]`; **credited to C129's own skeptic finding
B3**, which stated it first.

**And computed anyway, as an independent check on a different object:**

| monodromy `ρ` on `𝔽₂²` | `𝔽₂`-Betti, minimal | non-minimal |
|---|---|---|
| **swap** (`SU(2)_a ↔ SU(2)_b`) | `1,1,**0**,1,1` | `1,1,**0**,1,1` |
| trivial | `2,2,**0**,2,2` | `2,2,**0**,2,2` |

`[VERIFIED]`. Controls: the same routine on `S²×S¹` returns `b₂ ≠ 0` for **both**
a trivial and a nontrivial `ρ` (`G30`), and a gate requires the two monodromies
to give **different** Betti vectors (`G29c`) -- which is what the first draft was
missing and what makes "neuter `ρ`" a caught corruption rather than a
slip-through (skeptic finding C6; it is now injection 9).

### 5d. Therefore

`w₂(M_ι) = 0`, `w₁(M_ι)² = 0` and `c(E) = 0` for **every** `Ḡ`-bundle and
**every** `G`, because the group they live in is zero. By §4a:

> **Both `Pin^+ ×_{Z₂} G` and `Pin^- ×_{Z₂} G` exist on `M_ι`, for every such
> `G` and every `E` -- exactly two of each over any fixed underlying pair**
> (torsor over `H¹(M_ι;𝔽₂) = Hom(Z,𝔽₂) = Z/2`).

`w₁(M_ι) ≠ 0` still [CITED, C128 §6b / C129 §3 -- **reused, not re-derived
here**], so there is no Spin and no `Spin ×_{Z₂} G` structure.

---

## 6. Second route -- construct the structures, using none of §5

`M_f = (S³ × ℝ)/Z`, generator acting freely by `γ(x,s) = (f(x), s+1)`.

> **(a) `S³ × ℝ` is PARALLELIZABLE** (`S³` is a Lie group), so its frame bundle
> is trivial.
> **(b) EVERY `Ḡ`-bundle on `S³ × ℝ ≃ S³` is TRIVIAL**, because principal
> `Ḡ`-bundles on `S^n` are classified by `π_{n−1}(Ḡ)` and `π₂(Ḡ) = 0` **for
> every Lie group** [CITED, É. Cartan -- **not** re-derived]. *New relative to
> C129 §6, which had no gauge bundle.*
> **(c) `S³` is SIMPLY CONNECTED**, so the single monodromy map
> `u : S³ → O(4) × Ḡ` lifts through the double cover `H → O(4) × Ḡ` in exactly
> **two** ways; and **`Z` is free on one generator**, so there is no relation to
> satisfy. Any lift generates a free `Z`-action whose quotient is the structure.
> The only property of `H` used is that it is a **double cover**, so the argument
> runs identically for `Pin^+`, `Pin^-`, and every `G`.

> ⚠️ **HYPOTHESES (a) AND (b) ARE NOT OPTIONAL.** C129's standing counterexample
> to dropping (a) is recomputed here rather than cited: **`CP² × S¹`** has free
> `Z` monodromy and a simply-connected fibre yet `H²(CP²×S¹;𝔽₂) = Z/2 ≠ 0`
> (`G04`) and it admits neither `Pin^+` nor `Pin^-` nor Spin.

**Explicit lift** (`P5`): for `f = ι`, `u(x) = −Ad(x) ⊕ 1`; with `ω := e₁e₂e₃`
and `S(x)` the `Spin(3)` element covering `Ad(x)`, `ũ(x) = ω·S(x)` covers
`−Ad(x)` -- residual `4.5e−16`, with a firing control (without `ω`: `1.998`).
Reproduces C129 §6 from an independent implementation.

**How independent are the two routes, honestly** (skeptic finding B1 -- the first
draft overstated this at exactly the point it used it as a strength):

* **Citation sets ARE disjoint.** §5 uses the UCT and the Pin criteria, no
  parallelizability, no `π₂`, no Cartan; §6 uses parallelizability, `π₂(Lie)=0`
  and covering-space theory, and **no existence criterion at all**. Withdraw any
  single source and one route still stands. *That claim survives.*
* **The structural cause is SHARED, not disjoint:** both are consequences of
  `S³` being 2-connected (§5: `H¹(S³)=H²(S³)=0`; §6: `π₁(S³)=0` and
  `[S³,BḠ]=π₂(Ḡ)`). C129 §5 states that cause in one sentence.
* **The two counts of "exactly two" are the same computation in two languages**
  (`|Hom(π₁M,Z/2)| = 2` *is* the number of lifts of the single generator). The
  first draft's *"from completely different inputs. Cross-check, not a
  repetition"* is **deleted**.

---

## 7. Non-vacuity -- the twist genuinely matters, in BOTH directions

If twisting could never change the answer, §4-§6 would be an elaborate
restatement of C129. It can:

| manifold | `w₁` | `w₂` | twist `c(E)` | `Pin^+` tw. | `Pin^-` tw. | provenance |
|---|---|---|---|---|---|---|
| `CP²` | `0` | `h ≠ 0` | `0` (bare) | **NO** | **NO** | `[VERIFIED]` ring engine |
| `CP²` | `0` | `h` | `w₂(E) = h` | **YES** | **YES** | `[VERIFIED]` ring engine |
| `S²×S²` | `0` | `0` | `0` (bare) | **YES** | **YES** | `[VERIFIED]` ring engine |
| `S²×S²` | `0` | `0` | `w₂(E) = a` | **NO** | **NO** | `[VERIFIED]` ring engine |
| `S²×S²` | `0` | `0` | `w₂(E) = a+b` | **NO** | **NO** | `[VERIFIED]` ring engine |
| `RP⁴` | `a` | `0` | `0` (bare) | **YES** | NO | `[VERIFIED]` ring engine |
| `RP⁴` | `a` | `0` | `w₂(E) = a²` | NO | **YES** | `[VERIFIED]` ring engine |
| `RP²` | `a` | `a²` | `0` (bare) | NO | **YES** | `[VERIFIED]` ring engine |
| `RP²×RP²` | `a+b` | `a²+ab+b²` | `0` (bare) | NO | NO | `[VERIFIED]` ring engine |
| **`M_ι`** | `π^*a ≠ 0` | `0` | **any -- the group is `0`** | **YES** | **YES** | `w₁`: `[CITED]` C128 §6b / C129 §3. `w₂`, `c(E)`: `[VERIFIED]` §5, **not** the ring engine |

*The `M_ι` row's provenance is stated per cell, per skeptic finding A5: the
script deliberately refuses to evaluate it in the ring engine (encoding the
answer in a rigged truncation would be circular), and its `w₁` entry is imported,
not computed here.*

> **So "untwisted vanishes ⟹ twisted vanishes" is FALSE (row 3→4), and
> "untwisted fails ⟹ twisted fails" is FALSE (row 1→2).** The transfer holds on
> `M_ι` for a reason -- `H²(M_ι;A) = 0` -- computed in §5, not assumed.

**And the table can fail:** injection 5 makes `pin_verdict` silently drop the
twist class -- exactly the corruption that would make this vacuous -- and it
**moves the headline field** `twist_can_change_the_answer_in_general` (§12).
The `RP²`/`RP⁴`/`RP²×RP²` rows reproduce C129's `G23`/`G24`/`G25b` independently
and pin the labelling to C129 §2a's PRIMARY reading (`Pin^+ ⟺ w₂ = 0`), not to
`claim.md`'s or C128 §6c's swapped one.

**Honest narrowing** (skeptic finding, §2a): every twist exercised here is a
**vector-bundle** twist, i.e. the strictly-less-general form Remark 3.11 warns
about. The non-vacuity demonstration is one notch narrower than §4's theorem.

---

## 8. Does the answer depend on `t`, or on which relating map?

* **On `t`:** the half-integral factor is `SU(2)_b` at `t=0`, `SU(2)_a` at
  `t=1`; `σ` carries one to the other, so the structure type and the obstruction
  are the same element of the same (zero) group. `[INFERRED]` from §3a.2.
* **On the relating map:** **the `H²` computation sees only `deg f mod 2`**, and
  by `[CITED]` Cerf/Hatcher all orientation-reversing diffeomorphisms of `S³` are
  isotopic anyway. *Corrected, per skeptic finding C9(i): the first draft said
  "§5's computation sees only `deg f mod 2`" without qualification, and that is
  **false for `H³`** -- `H₃ = Z/2` at `deg −1` but `Z/6` at `deg 7`, so
  `H³(M;Z/3)` differs across degrees. The `H²` claim is degree-independent; the
  `H³` one is not.* `H₂ = 0` at every degree computed (five degrees, non-minimal
  model).

> **Consequence, the round's most useful negative content: the TWISTED structure
> question cannot discriminate `t=0` from `t=1` either.** C129 removed the bare
> tangential structure as a discriminator; this removes the twisted one -- the
> last cheap candidate before round95.

---

## 9. Kill Analysis (Anti-Overfitting Gate)

### What this round KILLS

* **`claim.md`'s permitted `BLOCKED` outcome, on the EXISTENCE question only**
  -- and by uniformity in `G`, not by naming `G`.
* **The framing in which "which twisted `Pin` type does the manifold admit?" is
  a live discriminating question.** Both exist, for every `G`. Combined with
  C129: **the manifold contributes no constraint via any structure whose
  existence obstruction is a degree-2 class.** *Narrowed from the first draft's
  "no constraint at all, bare or twisted", which contradicted this section's own
  W4 -- skeptic finding A4, a verbatim repeat of C129's A9.*
* **The reading in which the `SU(2)_b` bundle survives to `M_ι` intact.** §3c.
* **Reading (iii), `G = SU(3)`, as a candidate twisting group:** `Z(SU(3)) = Z₃`
  has no order-2 element. §3b.
* **The first draft's own accusation against C129's Z1** (skeptic finding C2) --
  killed by this round about itself.

### What this round does NOT kill

* **The anomaly half of Z1 / C127's A2 and X6.** Well-posed, unattempted, still
  blocked -- on round95, and now also on §3b.
* **Z2**, which needed `G`: now `BLOCKED (missing ingredient: `G`, named)`.
* **Whether `M_ι` is the right Dai-Freed object.** W1 -- and it is now
  **adversely indicated**, not merely open.
* **Degree-4 and higher structures.** `H⁴(M_ι;Z) = Z/2 ≠ 0`, so that door is open.
* **C125's `FALSIFIED`, C126's `WEAKENED`, C127's `BLOCKED`, C128's
  `OUTCOME_B`, C129's verdict** -- none re-litigated; C129 §4 and C128 §6b are
  independently reproduced.
* **Whether a `t`-selector exists**; Family C / `ε₄ε₆`; round80/Round117's open
  tension; round95's missing link.
* `N_gen=3`'s CONDITIONAL status, `lambda = FREE_COUPLING_PARAMETER`,
  `sm_derivation_claimed = False`, `safe_for_runtime = False`, OB1's `PARKED`.

### Relaxation Map (one assumption changed per variant; none attempted here)

| Variant | Single assumption changed | Kill criterion |
|---|---|---|
| **W1** *(promoted to top priority by skeptic finding C1)* | Fix the DIMENSION of the Dai-Freed object instead of inheriting `M_ι` from C128 §6 | C127 §4's verified audit lists `Ω₁₃,Ω₁₄` / `Ω₁₄,Ω₁₅` / `Ω₅,Ω₆` and **never `Ω₄`**. Either exhibit a reading in which a 4-manifold is the right home, or accept that C128 §6b, C129 and C130 answer a well-posed question about the **wrong manifold**. **Cheaper than round95 and now ahead of it.** |
| **W2** | Supply `G` by **granting** C124's V1 (an independent gauge sector) rather than deriving it | Then `G` is nameable and Z2 becomes attemptable -- but about a hypothetical this project does not freeze. Prerequisite for Z2. |
| **W3** | Drop `S³` for a fibre that is not 2-connected (C129's Z3, unchanged) | `CP²×S¹` is the standing example. Any physically relevant variant with such a fibre? (`S⁶` does not; `S³×S⁶` does not.) |
| **W4** | Ask for a structure whose obstruction is **not** degree 2 -- e.g. a String / 2-group structure in `H⁴` | `H⁴(M_ι;Z) = Ext¹(H₃,Z) = Z/2 ≠ 0`, so a degree-4 obstruction **could** be nonzero here. This is the one door §9's kill claim must not be read as closing. |
| **W5** | Literature check on §4a's `Pin` instantiation (partially run, §2b) | Is the `Pin` analogue of Lemma 3.9 written down? Would remove nothing (no novelty claimed) but settles whether §4a is folklore. |

---

## 10. What this round does NOT show

1. Does **not** resolve OB1 or move it out of `PARKED`.
2. Does **not** supply an F4 mechanism or any `t`-selector.
3. Does **not** name `G`; shows it is not available from the frozen content.
4. Does **not** evaluate any anomaly, or attempt C127's A2 / X6.
5. Does **not** touch round95's missing `S⁶`↔`S³` link.
6. Does **not** establish that `M_ι` is the physically relevant object -- and
   C127 §4's own audit **counts against** it (W1).
7. Does **not** make any 13D statement.
8. Does **not** use any bordism group as evidence; does **not** consult
   Kirby-Taylor directly (C129 did).
9. Does **not** re-derive `π₂(G)=0`, `π₀(Diff(S³))=Z₂`, or `w₁(M_ι) ≠ 0`.
10. Does **not** claim literature novelty (§2b, §10a).
11. Does **not** exercise a non-vector-bundle twist anywhere (§7's narrowing).
12. Does **not** reopen C125's, C126's, C127's, C128's or C129's verdicts -- and
    **withdraws its own first draft's accusation against C129's Z1** (§0, C2).
13. Does **not** change `N_gen=3`, `lambda`, `sm_derivation_claimed`, or
    `safe_for_runtime`.
14. Does **not** edit `PARENT_ACTION_GATE.md`, `OPEN_BLOCKERS.md`,
    `null_results/`, `CLAIM_LEDGER.yaml`, or `pearl_registry/` -- the
    orchestrating session's, per C124-C129 precedent.
15. Does **not** solicit Tom Lawrence's Part 5 or initiate any contact.

### 10a. Novelty ledger (rewritten after both passes)

| Item | Status |
|---|---|
| §4's theorem | **Not new.** Debray-Yu Lemma 3.9's own proof, restated at general `G`, with three scope gaps named. Cited, not claimed. |
| §4a's `Pin` instantiation | **New to this project's record; almost certainly folklore.** No source found (§2b). |
| §5a's `H²(M_ι;A) = 0` for **every** abelian `A`; §5b's `H³(M_ι;Z) = 0` | **New to this project's record** (C129 computed the `𝔽₂` case only). Elementary. |
| §5c's swap-monodromy computation | **New**, and the only computation specific to this background -- but **demoted**: it does not discharge §3c (the kernel is central), it is an independent check on a different object. |
| §5c's "for every local system" | **Not new** -- it is C129's own skeptic finding B3, credited. |
| §6's hypothesis (b) (`π₂(Lie) = 0`) | **New relative to C129 §6**, which needed no gauge bundle. Folklore. |
| §7's non-vacuity table | **New to this round as a control**; the individual facts are textbook. |
| Header finding #1 | **DOWNGRADED.** The first draft claimed a misattribution; that is **withdrawn**. What remains is the **propagation** of C127 §0 finding 8(ii)'s already-recorded type error into a Relaxation Map row -- useful, not a discovery. |
| Header finding #2 | **DOWNGRADED.** The `ι`-swap fact is C125 `A2`, already used by C127 §5b. Only the consequence for the twist bundle, and the correct group `Isom(S³)=O(4)`, are this round's. |
| §8's `t`-independence | **Not new in mechanism** -- the `ι`/`σ` exchange argument C127 §5c already declined to claim novelty for. |
| **New *results* bearing on OB1's own question** | **Zero.** |

---

## 11. Proposed pearls (NOT written to `pearl_registry/INDEX.md` -- outside this round's brief, per C124-C129 precedent)

**Pearl 1 -- Pearl Gate. On a manifold with vanishing `H²`, no degree-2
refinement of the tangential structure can discriminate anything.**
* **observation:** every structure in the `Spin`/`Pin`/`Spin^c`/`Spin^h`/
  `Spin-G`/`Pin-G` family is a lift through a `Z/2`-central extension, so its
  existence obstruction is a **single degree-2** class on the base, whatever the
  gauge group and bundle. On a manifold with `H²(M;A) = 0` for all `A`, all of
  them exist and **none** can discriminate -- dead on arrival, no computation.
* **falsifiable_prediction:** any future round proposing a *refinement* of the
  tangential structure on `M_ι` (or on any mapping torus of a self-map of a
  2-connected parallelizable fibre) as a `t`-discriminator gets "it exists, both
  types, every `G`". **Counter-example: a structure whose obstruction is not
  degree 2 -- and `H⁴(M_ι;Z) = Z/2 ≠ 0`, so that door is genuinely open (W4).**
* **impact_score:** 6. **trigger_condition:** any refined-tangential-structure
  discriminator proposal. **next_check:** 2026-12-01.
* **Scope limit:** degree-2 obstructions, `Z/n`-central extensions. Does **not**
  cover higher structures. *(This limit is the pearl, not an exception to it --
  §9's kill claim dropped it in the first draft and had to be narrowed.)*

**Pearl 2 -- Caveat Gate, REWRITTEN from "untested" to "adversely indicated"
after skeptic finding C1. This is the round's highest-impact open item.**
* **observation:** C128 §6b, C129 and C130 all analyse a **4-manifold**, chosen
  by C128 §6 because as frozen `M₄` is non-compact so no 13D mapping torus is
  closed. **C127 §4's own verified dimension audit lists `Ω₁₃,Ω₁₄` / `Ω₁₄,Ω₁₅` /
  `Ω₅,Ω₆` and never `Ω₄`.** `Ω₄` is the home of a *3-dimensional* theory's
  anomaly, and this project has no 3D theory. The relevance of the object three
  consecutive rounds analysed is therefore **counter-indicated by a table this
  project already verified**, not merely unexamined.
* **falsifiable_prediction:** fixing `d` either (i) exhibits a reading in which a
  4-manifold is the right home -- and three rounds stand -- or (ii) does not,
  in which case C128 §6b / C129 / C130 are correct about the **wrong manifold**
  and must be re-run. Exactly one holds; it is cheap, and it is cheaper than
  round95.
* **impact_score:** 8 *(raised from 7: the first draft scored it as an open
  question; it is an adversely-indicated one)*. **trigger_condition:** any
  attempt on C127 X6/A2 or on Z2. **next_check:** 2026-10-01.

**Pearl 3 -- methodological, and it is about this project's hand-off tables.**
* **observation:** C129's Relaxation Map row Z1 stated a **prerequisite as
  already satisfied** by chaining two sources correctly and then drawing an
  inference neither supports -- that the frame bundle's group can serve as a
  *twisting* group. The Relaxation Map is the artifact a future round reads
  *instead of* re-reading the sources, so an unchecked **inference** there
  propagates by design. Worse, the correcting diagnosis (C127 §0 finding 8(ii))
  was already on the record and simply never reached the row. Same shape as
  C129's own Pearl 3, one file further downstream: the unprotected sentence is
  in a **hand-off table**, and the protection that existed was in a *different
  file's skeptic matrix*.
* **falsifiable_prediction:** auditing the `Kill criterion` cells of the
  Relaxation Maps in C124-C129 against their cited sources will find at least
  one more inference the sources do not support. **And the cheap fix is
  testable: a Relaxation Map row that names a prerequisite should cite the file
  AND the section that supplies it, so the chain is checkable without
  re-deriving it.**
* **impact_score:** 5. **trigger_condition:** any round opening a Relaxation Map
  item by trusting that row's stated prerequisite. **next_check:** 2026-11-15.

**Pearl 4 -- methodological, from this round's own repeated gate failure.**
* **observation:** this round's first draft shipped **three** checks that could
  not fail (`G16`, `G17`, `G18`), one of which was a *repair* of an identical
  defect the same file had already recorded and "fixed" (§12 defect 1 moved the
  plumbing, not the tautology). The pattern across C128 (`A3`), C129 (`A1`) and
  C130 is the same: **a check of the form "verify that `X` commutes with a
  central element" or "verify `x·1·x⁻¹·1 = 1`" is a tautology in any
  implementation**, and it keeps being written because it *reads* like the
  property being claimed.
* **falsifiable_prediction:** grepping this project's verification scripts for
  checks whose expected residual is **exactly `0.0`** rather than `~1e−16`
  isolates this species with near-perfect precision -- exact zero means no
  floating-point arithmetic happened, i.e. nothing was computed. **Confirmed
  twice here** (`G16`'s `0.0` and `G18`'s `0.0`, both caught by pass 2 via
  exactly this tell; the repaired versions read `4.4e−16`).
* **impact_score:** 6 -- cheap, mechanical, and it has now caught the same
  species in three consecutive rounds. **trigger_condition:** any verification
  script reporting a residual of exactly `0.0` for a non-integer computation.
  **next_check:** 2026-11-15.

---

## 12. Verification

**Gate: 37 of 37 pass** (`ruff check` clean, `ruff format` applied).
`c130_twisted_pin_obstruction.py` imports only `numpy` and the stdlib; **no
project code, no C129 output as input.**

**Injection tests -- 11 injections, all caught, and EIGHT move the headline:**

| injection | gates | headline fields moved |
|---|---|---|
| Smith-normal-form returns no divisors | `31/37` | `H2_..._every_abelian`, `H2_..._every_degree_NONMINIMAL`, `H3_..._Z`, both `TWISTED_Pin_*` |
| mod-`p` rank routine returns `0` | `32/37` | `H2_..._local_coefficients`, `H2_..._every_degree_NONMINIMAL`, both `TWISTED_Pin_*` |
| monodromy term `(f−id)` dropped | `33/37` | `H3_M_iota_Z_vanishes` |
| UCT broken: `Ext¹(Z,A) = A` | `36/37` | `H2_..._every_abelian`, both `TWISTED_Pin_*` |
| **`pin_verdict` ignores the twist class** | `34/37` | **`twist_can_change_the_answer_in_general`** |
| non-minimal `∂₂` zeroed | `31/37` | `H2_..._every_abelian`, `H2_..._local`, `H2_..._every_degree_NONMINIMAL`, both `TWISTED_Pin_*` |
| `su2_to_so3` returns the identity | `36/37` | `constructive_route_lift_exhibited` |
| twisted adjoint transposed | `36/37` | `constructive_route_lift_exhibited` |
| `Pin^+`/`Pin^-` criteria swapped | `34/37` | none -- **correctly**, both hold on `M_ι` |
| commutator-pairing always `0` | `36/37` | none (the `Q8` gate fires) |
| **local-coefficient monodromy neutered** *(skeptic pass 2's own slip-through, now caught)* | `36/37` | none -- caught by the new `G29c` |

> **8 of 11 move a headline field.** More importantly, **the two corruptions the
> skeptic passes found slipping through the first version are now caught**, and
> the two headline fields that *could not move by construction* have been
> deleted or rewired.

**Defects found in this round's own scripts -- three by self-audit, three more by
the skeptic passes. Recorded, not silently corrected:**

*Self-caught (because 34/34 passing on the first run is a skeptic trigger, not a
result):*
1. **A tautological check** (`p·1·p⁻¹·1 − 1`). "Repaired" by routing it through a
   shared routine -- **which did not repair it**; see (4).
2. **A rigged ring**: the `M_ι` verdict was first evaluated in a truncated `𝔽₂`
   ring whose generator bound was `1`, i.e. with the answer in the encoding.
   Repaired: it now reads the *computed* `dim H²(M_ι;𝔽₂)`.
3. **A false comment**: an unused `from fractions import Fraction` whose `noqa`
   claimed it was "used by exactness assertions below". Removed.

*Skeptic-caught:*
4. **The (1) repair moved the plumbing, not the tautology** (finding A2):
   componentwise tuple multiplication makes the commutator the identity for any
   input, and the `Q8` control compared a forced result against a real one
   across two encodings. **Retracted rather than re-measured.**
5. **Two headline fields could not fail** (finding A1): `G16`/`G18`, tell = a
   residual of exactly `0.0`. Replaced by normality + kernel-order computations
   with firing controls.
6. **Three of five degrees were computed only in the model where the answer
   cannot fail** (finding A3), and **one corruption slipped through entirely**
   (finding C6). Both repaired and the latter is now injection 11.

**Honest accounting of every gate, exactly once** (skeptic finding A6 -- the
first draft's version omitted five and double-listed one):

* **Checks of the tool, not of the result:** `G01`-`G04` (Klein bottle, torus,
  `S²×S¹`, `CP²×S¹`), `G05`/`G09` (`d²=0`), `G14`/`G15` (Clifford relations,
  reflection image), `G19` (`e₁²=±1`), `G21` (`SU(2)→SO(3)` double cover).
* **Consistency re-runs, not independent evidence:** `G06` (minimal `M_ι`
  homology), `G28` (reads PART 1's computed dimension).
* **Definitional, and labelled so in the text rather than gated as evidence:**
  the vanishing of the Künneth cross term (§4a). `G17` gates only the **`Q8`
  witness**, i.e. that the direct-product hypothesis is non-vacuous.
* **Fixed-constant control, discriminating a global error and nothing else:**
  `G32` (lift without `ω`, `1.998`).
* **Genuinely discriminating:** `G07`/`G08`/`G09b`/`G09c` (non-minimal model at
  every degree, agreement, `H₂=0` as a computed rank, degrees distinguishable),
  `G10`-`G13` (`H²` vanishes / `H³` does **not**, same pipeline; nonzero on the
  `CP²×S¹` control), `G16`/`G16b` (normality, **fires** on non-central `z`),
  `G18`/`G18b` (kernel order 2, control returns 4), `G22`-`G27` (§7's table,
  both twist-flips), `G29`/`G29b`/`G29c`/`G30` (local coefficients, monodromies
  must differ, controls with nontrivial `ρ`), `G31`.

| Tier | Claim |
|---|---|
| `[VERIFIED-tool, PRIMARY -- for the MECHANISM only]` | The `K(Z/2,2)`-fibration argument -- Debray-Yu arXiv:2210.04911v2 Lemma 3.9's **proof**, read this session. **Its STATEMENT is oriented / Spin / `SU₈` and does NOT cover this case** (§2a); only the mechanism transfers. Plus **Remark 3.11**, whose weight is scope-bearing, not load-bearing. |
| `[VERIFIED-tool]` | `Pin^±` criteria and the twisted-spin framework -- arXiv:2405.04649v2 §6 (1),(2),(5); **corroborates** C129 §2a's Kirby-Taylor reading (a second author stating a standard fact, **not** an independent derivation). `Spin-G` general form -- arXiv:2504.15014v1 §4.1 (**SECONDARY**). Definitions -- arXiv:1810.00844v4 §2.4, arXiv:2511.03627v2 §1. **None read in full.** |
| `[VERIFIED]` -- exact arithmetic, two CW models, five degrees | `H_*(M_d;Z)` for `d ∈ {−1,0,1,2,7}` in **both** models; `H²(M_ι;A) = 0` for eight `A`; `H³(M_ι;Z) = 0` with `H³(M_ι;𝔽₂) = Z/2 ≠ 0` as non-vacuity; `H₃` taking four distinct values across the five degrees; `𝔽₂`-Betti with swap and trivial local systems; §7's table (except its `M_ι` row -- see there). Controls: Klein bottle, torus, `S²×S¹`, `CP²×S¹`. **Skeptic pass 2 hand-recomputed all of this without an execution tool and reproduced it exactly.** |
| `[VERIFIED]` -- explicit construction, both signatures, firing controls | Normality of `⟨(−1,z)⟩` (`4.4e−16`; **`1.99` on non-central `z`**); kernel order `2` (control: `4`); `Q8` pairing `1`; the explicit lift `ω·S(x)` (`4.5e−16`, control `1.998`). |
| `[INFERRED from VERIFIED-tool]` | §4's theorem at general `G`, with hypotheses stated. |
| `[INFERRED]` | §4a's `ζ = ζ_± + ζ_G` (product case only); the connected-`Ḡ` cross-term argument; "exactly two of each over a fixed pair"; §5c's centrality argument and the Wang squeeze for all local systems (**credited to C129 finding B3**); §6's lifting argument; §3c's consequence. |
| `[CITED]` -- standard, not re-derived | `π₂(G) = 0` for every Lie group (É. Cartan); `Ḡ`-bundles on `S^n` ↔ `π_{n−1}(Ḡ)`; `S³` parallelizable; `Pin^±(n) → O(n)` a double cover; UCT; Wang sequence; Cerf 1968 / Hatcher 1983. |
| `[CITED]` -- project facts | C38; C125 (`A2`, `ι`, `φ_{a,b}`, §3a); C126; **C127 (§0 findings 1 and 8(ii), §3b, §3c, §4's dimension audit, §5a's table, §5b)**; **C128 (§3, §5 + converse, §6 preamble, §6b, Y1)**; **C129 (§2a, §3, §4, §5, §6, §7, Z1, finding B3, Pearls 3-4)**; round95; `PARENT_ACTION_GATE.md` F4. |
| `[UNTESTED-IN-CONTEXT]` *(skeptic finding B3, accepted half)* | `ext_into`'s torsion branch: correct (tool-verified against five textbook values, which is why the "real bug" half was **DISMISSED**), but never exercised by this round's headline, since every UCT call has `H₂ = 0` or free `H₁`. |
| `[UNKNOWN]` -- deliberately not guessed | Whether `M_ι` is the right Dai-Freed object (**adversely indicated**, W1). The group `G`. Which Pin type the content selects (round95). Whether §4a is in the literature. Degree-≥4 structures (W4). Everything in §9's "does NOT kill". |

**No pytest suite touched, no shared project code modified.**

### Check (reproduces this decision)

```bash
cd experiments/20260902-c130-twisted-pin-structure-existence
python c130_twisted_pin_obstruction.py   # expect 37 / 37, ALL_OK = True
python c130_injection_tests.py           # expect ALL_INJECTIONS_CAUGHT = True
                                         #    and 8 of 11 moving the headline
```

Independently of the code:

1. arXiv:2210.04911v2 Lemma 3.9's **proof** -- *"the data of a lift of `f` … is
   equivalent data of a null-homotopy of `(w₂ + a)∘f`"*, for **any space `X`**.
   Its **statement** is oriented / Spin / `SU₈`.
2. arXiv:2405.04649v2 §6 (1),(2) -- `pin⁻ ⟺ w₂ + w₁²`, `pin⁺ ⟺ w₂`, agreeing
   with C129 §2a and disagreeing with C128 §6c.
3. `results_c130.json` → `PART1_cohomology.nonminimal_model` must show
   `cell_ranks_by_dim = [1,2,2,2,1]` at **all five** degrees with
   `betti_F2[2] = 0` -- `H₂ = 0` computed over a complex with two 2-cells.
4. `results_c130.json` → `PART2_extension.Cl(4,0)`:
   `normality_deviation_noncentral_z_MUST_BE_LARGE ≈ 1.99` while
   `normality_deviation_central_z ≈ 4.4e−16`, and
   `kernel_order_with_identification = 2` vs `..._without_identification = 4`.
5. **C127 §4's dimension audit** must list `Ω₁₃,Ω₁₄` / `Ω₁₄,Ω₁₅` / `Ω₅,Ω₆` and
   **no `Ω₄`** -- the basis for W1 / Pearl 2.
6. **C127 §5a's table** must contain the words *"frame bundle's group"* in its
   consequence-for-`G` column -- which is why the first draft's accusation
   against C129's Z1 is withdrawn.

**Falsifiers, stated so they can fail:**

1. **Exhibit a nonzero degree-2 class on `M_ι`**, any coefficients. Injections
   1, 2, 4, 6 produce nonzero answers when the machinery is corrupted; the
   correct code does not.
2. **Exhibit a `G`, a bundle `E`, and a `Pin^± ×_{Z₂} G` structure that fails to
   exist on `M_ι`.** Would require a non-`Z/n`-central extension or an error in §5.
3. **Break §4's generality:** a structure in this family whose obstruction is not
   a degree-2 class. A String-type structure is not a counterexample -- it is
   outside the family, and W4 records that `H⁴(M_ι;Z) = Z/2 ≠ 0`.
4. **Falsifier for non-vacuity:** show twisting can never change a Pin verdict.
   §7 rows 1→2 and 3→4 exhibit both directions; injection 5 hides it.
5. **Falsifier for W1, and it is the one most likely to succeed:** exhibit a
   reading of this project's content in which a **4-manifold** is the right
   Dai-Freed home. C127 §4 lists none.

---

## 13. Evidence tier of the central conclusion, and what would raise it

**Central conclusion, as it stands after both passes:** *As a theorem about
`M_ι`: for every Lie group `G` with a central element of order 2 and every
`Ḡ`-bundle, both `Pin^+ ×_{Z₂} G` and `Pin^- ×_{Z₂} G` structures exist --
exactly two of each over a fixed underlying pair -- because the single
obstruction of any `Z/2`-central extension is a class in `H²(M;Z/2)`, and
`H²(M_ι;A)` vanishes for every abelian `A`. The transfer from C129 is proved,
not assumed, and the converse is exhibited false on other manifolds. **As an
answer to Z1 this is conditional on `M_ι` being the Dai-Freed object, and that
condition is adversely indicated by C127 §4's own audit.** The group `G` is not
available from the frozen content.*

* **`[VERIFIED]`** -- the cohomology (§5: two models, five degrees, eight
  coefficient groups, two local systems, `H³` as well), the extension's
  normality and kernel order with firing controls (§4a), §7's table, the
  explicit lift (§6). Eleven corruptions caught, eight moving a headline field.
* **`[VERIFIED-tool, PRIMARY -- mechanism only]`** -- the obstruction-theoretic
  mechanism (§2a); its cited **statement** does not cover this case.
* **`[INFERRED]`** -- §4 at general `G`; §4a's decomposition (product case);
  "exactly two"; §5c; §3c.
* **`[UNKNOWN]`, and one of them adversely indicated** -- whether `M_ι` is the
  right manifold (W1); `G`; which type the content needs.

**Structural property, at its corrected strength** (skeptic finding B1): the
conclusion **survives withdrawal of any single citation**, because §5 and §6
have **disjoint citation sets** -- §5 needs the UCT and the Pin criteria, §6
needs parallelizability, `π₂(Lie)=0` and covering-space theory and no criterion
at all. But the two routes are **not** structurally independent: both are
consequences of `S³` being 2-connected, and their two counts of "exactly two"
are the same computation in two languages. The first draft claimed the stronger
thing and it is withdrawn.

**Independent Verification Strength Ladder.** The cohomology sits at
**"independently-written code" (Strong)**: no project code imported; reproduced
in two CW presentations, five degrees, eight coefficient groups, two local
systems, plus a second route sharing no machinery. **Both skeptic passes are
"same model, isolated context" (Weak-Medium)** however thorough -- though pass 2
hand-recomputed every load-bearing number without an execution tool, which makes
its confirmation genuinely independent of this round's code.

**What would raise the rest:**
* **W1 → resolved.** Fix the dimension of the Dai-Freed object. **The single
  highest-value next step, ahead of round95**, because it decides whether three
  completed rounds are on-target.
* **`G` → named:** requires W2 or closing round95. Until then Z2 is blocked on two.
* **§4a → a literature hit** (W5). Low value; two routes already agree.
* **A non-vector-bundle twist in §7**, to exercise the generality §4 claims and
  §7 does not reach.
* **What would NOT raise it:** more coefficient groups. `H₂ = 0` with `H₁` free
  *proves* `H²(M_ι;A) = 0` for all `A`; the eight values check the implementation.

### 13a. Recomposition gate (skeptic finding B4)

The sub-claims (§4's theorem, §5's computation, §6's construction, §7's
non-vacuity) are individually true. **Their conjunction licenses:**

> *"On `M_ι`, every tangential structure arising as a lift through a `Z/2`- or
> `Z/n`-central extension of a group `K` for which `M_ι` has a `K`-structure
> exists, in exactly two isomorphism classes over each fixed underlying pair,
> for every Lie group `G` and every `Ḡ`-bundle."*

**It does not license** the research claim "Z1 is closed", because recomposition
silently adds two assumptions neither sub-claim tests: (i) that the structure
the physics needs **is** in that family, which §3b shows is not established; and
(ii) that it lives on **`M_ι`**, which W1 shows is adversely indicated. The
headline and the verdict string are now written to the licensed statement, with
both assumptions named in them rather than in a pearl.

### 13b. FL Step 8a skeptic passes

**RUN -- twice, context-blind, differently-worded prompts (Paraphrase-Sensitivity
Probe), because this round closes a live Relaxation Map item. Both returned
`WEAKENED`; CONCORDANT, so the single-run Response Matrix applies and no
skeptic-leaning tie-breaker is needed. 23 findings; 22 accepted and repaired,
1 DISMISSED on tool verification, 0 waved through. Full matrices in §0.**

Their principal effects on this file: **the wrong-manifold risk was upgraded
from "untested" to "adversely indicated by this project's own verified table",
and put into the verdict string**; **the first draft's accusation against C129's
Z1 was shown wrong and is withdrawn**; **three checks that could not fail were
deleted or rebuilt**, including one the file itself had already claimed to
repair; **two corruptions that slipped through are now caught**; the
"disjoint routes" and "for every local system" claims were cut to what is
argued; §5c was shown to answer the wrong question and relabelled; and the
degree sweep, which existed only in the model where the answer cannot fail, now
runs in the model where it is a computed rank.
