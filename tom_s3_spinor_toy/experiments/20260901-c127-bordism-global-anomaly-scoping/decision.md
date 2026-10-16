# C127 decision -- bordism / global-anomaly scoping for OB1 (Relaxation
# Map item 8).
#
# HEADLINE, stated first and not buried: **BLOCKED.** No bordism group was
# computed for this project's frozen background. Per `claim.md`'s own
# explicit permission ("this is explicitly permitted and is not a failure of
# the round") and round86's own BLOCKED precedent, this is the honest
# verdict; the missing ingredients are named precisely in Sec. 5, not
# gestured at.
#
# THE SCOPE OF THE NEGATIVE RESULT, corrected by the FL Step 8a skeptic pass
# and stated in the header because the FIRST DRAFT OF THIS FILE OVERSTATED IT:
# the round does NOT show that "no bordism argument can bear on OB1". It
# shows that the bordism class of a SINGLE FIXED BACKGROUND is
# connection-blind, hence cannot select `t`. The standard global-anomaly
# construction attaches a class not to one background but to the MAPPING
# TORUS of the transformation relating two -- and that object is nonzero
# here (Sec. 5d). The first draft asserted a universal no-go, told future
# rounds not to retry item 8 "in this form", and listed no mapping-torus
# variant. All three are repaired below. What survives is narrower and, in
# one respect, more useful: SELECTION of a single `t` is structurally
# excluded; PAIR-FORCING (which `claim.md` pre-registers as an equally valid
# success mode -- "or force the pair together ... or the pair, or a sign")
# is NOT excluded, is well-posed, and is blocked on two named ingredients.

**Verdict (2026-09-02; FL Step 8a skeptic pass run same day, verdict
`WEAKENED`, all 12 findings answered, headline label unchanged):**
`BLOCKED__SELECTION_READING_STRUCTURALLY_EXCLUDED_A_BORDISM_CLASS_OF_A_SINGLE_FIXED_BACKGROUND_IS_CONNECTION_BLIND_SO_NO_GENERATOR_CAN_PICK_ONE_t__PAIR_FORCING_READING_IS_WELL_POSED_AND_NOT_EXCLUDED_MAPPING_TORUS_OF_C126s_WINDING_MINUS_1_GAUGE_TRANSFORMATION_CARRIES_A_NONZERO_CLASS__BUT_THAT_CLASS_IS_A_RESTATEMENT_OF_C126s_ALREADY_COMPUTED_WINDING_NUMBER_AND_THE_ANOMALY_EVALUATION_ON_IT_IS_BLOCKED_ON_TWO_NAMED_INGREDIENTS__INGREDIENT_1_WHICH_GAUGE_GROUP_ACTS_ON_NABLA_t_C125_FRAME_BUNDLE_TORSION_IS_A_TENSOR_VS_C126_YANG_MILLS_ONE_GAUGE_ORBIT_EACH_ROUND_NAMED_ITS_OWN_HALF_NEITHER_RECONCILED_AND_NO_REGISTRY_ENTRY_RECORDS_THE_PAIR_CHECKED_THIS_SESSION__INGREDIENT_2_ROUND95_MISSING_S6_S3_LINK_GIVING_A_SYMMETRIC_OR_CIRCULAR_DICHOTOMY_FOR_SELECTION__OMEGA_SPIN_13_14_AND_15_ALL_ZERO_VERIFIED_THIS_SESSION_FROM_A_CITING_TABLE_ABP67_GIA71_NOT_REPEATED_FROM_THE_EXTERNAL_DOCUMENT__EXTERNAL_DOCUMENTS_DIMENSION_IS_OFF_BY_ONE_HARMLESS_ONLY_BECAUSE_14_AND_15_ALSO_VANISH`

**Status:** OB1 stays `PARKED`. No reopen condition met. Relaxation Map
item 8 is `BLOCKED-WITH-NAMED-INGREDIENT` in its pair-forcing reading and
`STRUCTURALLY_EXCLUDED` in its selection reading -- two different verdicts
on two different readings, recorded separately rather than averaged.

**Completeness:** `PARTIAL`, in four named respects. (1) No bordism group
was computed by this round; reported values are cited. (2) Sec. 2's lemma
is an own derivation, hand, no script -- and its valid half is
**definitional**, not a discovery (Sec. 0, finding 2). (3) The pair-forcing
question (Sec. 5d) is scoped and shown blocked, **not** answered; its
anomaly evaluation is not attempted. (4) `Ω^{Spin}_5(B G_eff)`,
`Ω^{Spin×_{Z₂}SU(2)}_5`, and `Ω^{Spin}_{13}(BSU(3))` are all `[UNKNOWN]`
and deliberately not guessed.

**Gate fields assessed:** `PARENT_ACTION_GATE.md` F1 (reused unchanged;
found to carry its own obstruction, Sec. 3d), F2 (reused unchanged; found
`t`-blind, Sec. 3c), F4 (the field this round bears on, negatively). F3,
F5 reused by citation. F6, F7 not assessed.

---

## 0. ⚠️ FL STEP 8a SKEPTIC PASS RUN AND INCORPORATED, 2026-09-02, same day

Context-blind (`Agent(skeptic, model=opus)`, `claim.md` + `decision.md`
only, no session history, no reasoning chain). **Verdict returned:
`WEAKENED` -- "the top-line BLOCKED survives; the central lemma survives
only in a narrow, near-tautological form; the document is right for a
reason it does not give."** Twelve findings. **Every one is answered below
per the FL Step 8a Response Matrix; none is waved through, and the three
that are fatal to the first draft's framing are repaired in place rather
than argued away.**

| # | Finding | Response |
|---|---|---|
| **1** | The lemma's universal quantifier is **false in the standard Dai-Freed formalism**: the tangential structure `ξ` is a *function of* the representation `R`, and `R` is `t`-dependent by the document's own citation. `(1,2)` is half-integral under `SU(2)_b` (its central `−1` acts as `(−1)^F`), so the correct structure is `Spin ×_{Z₂} SU(2)_b` at `t=0` and `Spin ×_{Z₂} SU(2)_a` at `t=1` -- **different structures, so `Ω^{ξ(t)}` is literally a `t`-dependent group.** The very paper cited `[VERIFIED-tool]` for the dimension convention (García-Etxebarria-Montero) is methodologically *about* determining `ξ` from the rep content, and the draft assumed that move away. | **ACCEPTED, real defect, repaired.** Independently re-derived: `(1,2)` is a genuine half-integral rep, the `Z₂` quotient identification with `(−1)^F` is forced, and the draft's Sec. 5 sentence *"the t-dependence enters through the content, not the group"* is **false as written and is deleted.** The lemma is restated with its actual hypothesis (*at fixed `(M, ξ-structure, f)`*), and Sec. 6's "for every tangential structure and every `G`" is withdrawn. **Note the two structures are isomorphic via `σ` (label swap), so this does not by itself create a selector -- it relocates where the `t`-dependence sits, which is exactly finding 4's point.** `[UNKNOWN]`: the value of `Ω^{Spin×_{Z₂}SU(2)}_5`; the skeptic offered a recollection and correctly declined to lean on it, as does this file. |
| **2** | The lemma is **two arguments fused**. Argument 1 (*bordism data contains no connection*) is **definitional** -- a function does not depend on a variable outside its domain -- and cannot fail. Argument 2 (*connections form an affine, contractible set*) does **zero work** for Argument 1, and in the quotient that matters is **contradicted by the document's own cited C126**: `A` is contractible, `A/G₀` is not, and C126's winding `n = −1` is exactly a discrete invariant separating them. Also the cycle description ("spin structure `s` **plus** an independent `f: M → BG`") is **wrong for the twisted `ξ` the lemma explicitly claims to cover** -- `Spin-Z₄` structures exist on non-spin manifolds; that factorization is precisely what fails. | **ACCEPTED on all three counts, repaired.** The contractibility clause is **deleted** (it was rhetorical and it pointed the wrong way). The cycle description is corrected: a `ξ`-structure is a *lift of the classifying map of the stable tangent bundle*, which for twisted `ξ` does **not** factor as spin-structure × bundle -- and the conclusion survives the correction, because a lift of a classifying map is still not a connection. **Argument 1 is now labelled definitional in the text**, which is what it is; its value is as a pre-filter (Sec. 8), not as a discovery. |
| **3** | **The strongest finding.** The "a fortiori" clause covers only invariants factoring through **one** background. **Global anomalies do not.** Witten's construction and every Dai-Freed argument attach a class to the **mapping torus of a gauge transformation** -- an invariant of a *pair*. Using the document's own cited C126: the `SU(2)` bundle over `S³ × S¹` clutched by a winding `−1` transformation has `∫c₂ = −1 ≠ 0`. So Sec. 4's *"no literature construction was found in which a connection-family parameter is selected by a bordism invariant (consistent with Sec. 2, which says one cannot exist)"* over-reads, and Sec. 6's *"should not be retried in this form"* would tell a future round to skip **the textbook mechanism for the structure C126 says this background has.** The Relaxation Map X1-X5 contained no mapping-torus variant. | **ACCEPTED, and this is the finding that reshapes the document.** Independently re-derived: the instanton number of the interpolating configuration equals the Chern-Simons difference across the ends, which is C126's own `n = −1` (computed there two independent ways), so the class is nonzero. **New Sec. 5d written; new Relaxation Map item X6; Sec. 6's instruction withdrawn and replaced by the narrow one.** This session's own scoping had considered the mapping torus and then **failed to put it in the writeup** -- recorded as a defect of the writeup, not excused. **What the repair does *not* concede:** the mapping-torus class detects the *pair*, not a member of it, and as a *number* it is a restatement of C126's already-computed winding (Sec. 5d) -- so item 8 remains BLOCKED, for better-stated reasons. |
| **4** | Horn A's inference is **valid** (`σ_*` is an isomorphism; σ need not be inner, need not act trivially on the group, survives orientation reversal and survives the two `ξ`'s of finding 1 differing) -- **but its scope claim is not.** `claim.md` pre-registers *"or force the pair together"* and *"(or the pair, or a sign)"*, and the draft's *"No discrimination, for any bordism group, computed or not"* banks a mode it never addressed. Pair-forcing asks about `α_{R(0)} ± α_{R(1)} = α_{R(0)}∘(1 ± σ_*)`; in the minus case -- exactly what an **orientation-reversing** ι produces, and C125 says the relating maps *are* orientation-reversing -- the sum can vanish while each term does not. Separately: `R(1) = (σ×id)^*R(0)` is asserted, and the **unnamed** weak link is not "naturality" (standard) but that `R(t)` is exhausted by (S³ kernel) ⊗ (t-independent S⁶ factor). | **ACCEPTED, real defect, repaired.** Horn A is split into **A1 (selection -- excluded, inference confirmed by the skeptic)** and **A2 (pair-forcing -- NOT excluded)**. The over-reaching sentence is deleted. The weak link is renamed correctly in Sec. 9's tier table. **This is the single most consequential repair after finding 3: the round had dismissed one of the two success modes `claim.md` explicitly pre-registered.** |
| **5** | The verdict string's leading clause (`NO_G_NAMEABLE_FROM_FROZEN_CONTENT_AT_THE_13D_LEVEL`) is **contradicted by the document's own Sec. 3c**, which says the map `M₁₃ → BSU(3)` classifying `E` *"genuinely exists, and it is essential"*. `SU(3)` is a nameable `G` in the frozen content at the 13D level. The Entity field **passes**; the gate fails on the predicate only. | **ACCEPTED, real defect (the stated primary reason was false), repaired.** Sec. 1's Entity row is now `PASS (qualified)`; the verdict string is rewritten; the gate result is re-derived and still FAIL, on the predicate. |
| **6** | Two mis-tags of the species the document polices elsewhere: (a) Sec. 2's lemma tagged `[VERIFIED]` on a hand derivation with no script and no independent reconstruction -- `[INFERRED]` per `integrity.md`, and not merely formal given findings 1-3; (b) arXiv:2108.13542 Table 1 called *"a primary table"* in the same paragraph that notes it *"itself attributes verbatim to [ABP67, Gia71]"* -- that is a **secondary** source, so "not repeated on the external document's authority" is weaker than presented: one secondary authority replaced another. | **ACCEPTED both, retagged.** (a) → `[INFERRED -- own derivation, scope corrected by skeptic pass]`. (b) → `[VERIFIED-tool, SECONDARY source; primaries ABP67/Gia71 not consulted]`. **Recorded, because it cuts the other way:** the skeptic independently cross-checked the *numbers* without opening the paper -- free ranks must be `p(k)` at degree `4k` (`1,2,3,5` for `d=4,8,12,16`, matching `Z, Z², Z³, Z⁵`), and the ABP `ko`-summand bottoms forced by `Ω₉=Z₂²`, `Ω₁₀=Z₂³`, `Ω₁₂=Z³` give exactly `Ω₁₃=Ω₁₄=Ω₁₅=0`. **The cited values survive an independent structural check.** Re-verified here: `p(1..4) = 1,2,3,5` ✓. |
| **7** | The `d→d+1` convention is applied **correctly** (CONFIRMED). But the *hedge* about "13D topological terms" repeats in miniature the fault the document charges: Freed-Hopkins gives `0 → Ext¹(Ω^ξ_d,Z) → [I_Z MTξ]^{d+1} → Hom(Ω^ξ_{d+1},Z) → 0`, so 13D invertible theories need `Ω₁₃` **and** `Ω₁₄`; and a 13D theory's *anomaly* needs `Ω₁₄` **and** `Ω₁₅`. The draft named one degree per reading and called it "the right degree". | **ACCEPTED, repaired, and it makes the conclusion STRONGER.** Sec. 4 now names the Anderson-dual sequence and the second degree in each reading. All of `Ω₁₃, Ω₁₄, Ω₁₅` vanish in the same verified table, so every reading closes -- and the draft's *"harmless only because 14 also vanishes"* is corrected to *"14 **and 15**"*. |
| **8** | Sec. 3b reading b1: **every step checks out and the conclusion is right for the stated reason** (parallelizability pulls back; the basepoint-image argument is correct; the reduced/unreduced concern is a non-issue). But (i) it is **the same computation as candidate (a)** -- both reduce to `Ω^{Spin}_{13}(pt)=0` -- so the walk has 3 candidates, not 4, and the duplicate is unflagged; (ii) b1 is **mis-typed**: the frame bundle is part of the tangential structure, not an independent `BG`-twist, and the parenthetical silently swaps frame-bundle group for isometry group; (iii) **ordering contradiction**: Sec. 3b says the class *"is identically zero"* for `M₁₃` while Sec. 3d says `M₁₃` *"has no bordism class at all"*. | **ACCEPTED all three, repaired.** The closed-manifold hypothesis is now stated **once, up front** (Sec. 3, preamble), so Sec. 3b is explicitly a statement about the admissible closed replacements, not about the frozen non-compact `M₁₃`; b1 is merged into (a) with the duplication flagged and the mis-typing corrected. |
| **9** | Sec. 5 leans on a premise Sec. 3b promised not to lean on: `G_eff` **is** the gauge group descending from `Isom(S³)`, the contested KK premise Sec. 3b said *"this round inherits the downgrade and does not lean on the premise either."* | **ACCEPTED, real internal contradiction, repaired.** Sec. 5, X1 and X2 are now marked **conditional on the contested `Isom₀` premise**; the "does not lean on it" sentence is scoped to Sec. 3, where it is true. |
| **10** | **Three mutually exclusive** "the only genuinely new content" claims (header, Sec. 2, Sec. 5), one of which Sec. 2 itself retracts four lines later (*"not a new discovery so much as a diagnosis"*). Combined with finding 2, the honest ledger is: one new framing (uncomputed), one definitional pre-filter, **zero new results**. | **ACCEPTED, repaired.** All superlatives removed; a single novelty ledger is written (Sec. 7a) with one entry per item and no "only". |
| **11** | Unflagged restatements beyond the one flagged: (a)≡(b1) (finding 8); and **Sec. 3c's factor-support argument is an application of the already-registered C119 factor-support/Künneth pre-filter**, presented as an independent derivation *"without Sec. 2's general lemma being needed"* -- while Sec. 8 itself calls the new pearl a "sibling to C119's filter". | **ACCEPTED, flagged in place.** Sec. 3c now states it is the existing filter applied, not new. **Sec. 5a's C125-vs-C126 conflict, which the skeptic could not settle:** checked this session (see Sec. 5a) -- it is **genuinely unrecorded**, so the "two named ingredients" does not reduce to one. |
| **12** | Summary: **kill scope too strong, novelty claim too strong, verdict label correct.** Sec. 6 spoke the language of `STRUCTURAL_NO_GO` (compare C124's verdict of that name) while the round's own claimed discovery is definitional. And the Sec. 8 pearl inherits the over-reach: its `trigger_condition` auto-fails *"a bordism/cobordism argument"* and its `observation` blanket-includes *"characteristic number"* -- which would auto-kill both the mapping-torus route (whose characteristic number is `−1 ≠ 0`) and any differential-bordism formulation, i.e. the same layer as X3, which the document says survives. | **ACCEPTED entire, repaired.** Sec. 6's kill is narrowed to the selection reading of a single fixed background; **the pearl is rescoped before it is proposed** to "topological invariants of a *single fixed* background", with an explicit carve-out naming the mapping torus and the differential layer. **The skeptic's own one-line restatement of what the round actually found is adopted as this file's framing** and is quoted in Sec. 7a. |

**Nothing dismissed. No finding overturned the headline label**; findings 3
and 4 substantially narrowed what the label is allowed to carry, and
finding 5 falsified the reason originally given for it.

---

## 1. Step 1 -- the Zero-Signal Gate, run BEFORE any computation

Per `falsification-ladder.md` Step -5: `(∃ entity) ∧ (∃ falsifiable
predicate) ∧ (∃ measurable outcome)`, all three required.

`claim.md` pre-registers **two** success modes, and they must be gated
separately -- collapsing them is exactly what the first draft did wrong:
*"select `t∈{0,1}`, **or force the pair together**"* and *"a discrete
choice that can be mapped onto `t∈{0,1}` (**or the pair, or a sign**)"*.

### Reading S -- SELECTION (pick one member of `{0,1}`)

| Field | Status | Why |
|---|---|---|
| Entity | **PASS (qualified)** | `G = SU(3)` from the `S⁶` twist is nameable in the frozen content and its classifying map is **essential** (`c₃(S⁻)=2≠0`, Sec. 3c). *(Corrected by skeptic finding 5; the first draft said no `G` was nameable, contradicting its own Sec. 3c.)* |
| Falsifiable predicate | **FAILS** | The predicate demands generators "corresponding to" `t`. Bordism generators are manifolds-with-structure; the class of a **single fixed background** is connection-blind (Sec. 2). |
| Measurable outcome | half-available | Group values citable; the generator→`t` map is what cannot exist. |

**Gate result for Reading S: FAIL, structurally.**

### Reading P -- PAIR-FORCING (force `t=0` and `t=1` together, or a sign)

| Field | Status | Why |
|---|---|---|
| Entity | **PASS** | The **mapping torus** `S³ ×_g S¹` of C126's winding-`(−1)` large gauge transformation, with its clutched `SU(2)` bundle: a class in `Ω^{Spin}_4(BSU(2))`. Sec. 5d. |
| Falsifiable predicate | **PASS** | "the relevant class is nonzero" -- it is: `∫c₂ = −1`. |
| Measurable outcome | **PASS** | Computable, and **already computed** by C126 as the winding number, two independent ways. |

**Gate result for Reading P: PASS.** The gate does **not** stop this
reading -- and the first draft's claim that it did was wrong (skeptic
finding 3). What stops it is downstream and is stated as such: the class is
a **restatement** of C126's `n = −1` (F4's mechanism-transfer gate), and the
**anomaly evaluation on it** -- the only step that could actually force the
pair -- is BLOCKED on the two ingredients of Sec. 5.

**Overall: `BLOCKED`, not `REFUSE(no_falsifiable_claim)`**, because the
missing ingredients are **specifically nameable** -- which is round86's own
stated operative criterion for BLOCKED over a bare refusal
(`experiments/20260717-round86-parent-action-discriminator/decision.md`,
"Why BLOCKED, not FAIL").

---

## 2. The structural obstruction, stated at its true strength

**Corrected twice by the skeptic pass (findings 1, 2, 3). What follows is
what survives, with the valid half labelled for what it is: definitional.**

> **Observation (connection-blindness of a single background's class), a
> restatement of the definition, not a discovery.** For any tangential
> structure `ξ`, a `ξ`-structure on `M` is a **lift of the classifying map
> of the stable tangent bundle** through `Bξ → BO`. For twisted `ξ`
> (`Spin-ℤ₄`, `Spin-G`, `Spin ×_{Z₂} SU(2)`) this datum does **not**
> factor as "spin structure × independent `G`-bundle" -- that factorization
> is precisely what fails, and the first draft's cycle description was
> wrong on this point. What survives the correction is the only thing
> needed: **a lift of a classifying map is not a connection.** Hence the
> class `[M, ξ-structure, f] ∈ Ω^ξ_n(X)` of one fixed background does not
> vary as `∇^t` varies. ∎

**Deleted from the first draft, and why** (skeptic finding 2): the clause
"connections form an affine, hence contractible, space" did no work for
this observation and **pointed the wrong way** -- `A` is contractible but
`A/G₀` is not, and C126's winding `n = −1` is exactly a discrete invariant
separating `∇⁰` from `∇¹` in that quotient. Using contractibility to
suggest nothing discrete can separate them, and then citing C126, was a
self-contradiction.

**What this does and does not license:**

1. **Licensed:** Reading S dies. A selector for `t` cannot be a
   topological invariant *of one background*.
2. **NOT licensed, and asserted anyway in the first draft** (finding 3):
   nothing here constrains invariants of a **relation between two
   backgrounds**. Global anomalies are exactly such invariants. See
   Sec. 5d.
3. **NOT licensed, and asserted anyway in the first draft** (finding 1):
   the quantifier "for every `ξ`" was applied as though `ξ` were
   independent of the fermion content. It is not. `R(0) = (1,2)` is
   half-integral under `SU(2)_b`, so its central `−1` is `(−1)^F` and the
   forced structure is `Spin ×_{Z₂} SU(2)_b`; at `t=1` it is
   `Spin ×_{Z₂} SU(2)_a`. **`ξ` itself moves with `t`.** The two are
   isomorphic by the label swap `σ`, which is why this relocates rather
   than creates a selector -- but "the group is fixed, only the content
   moves" is false and is withdrawn.
4. **Diagnosis that survives all three corrections, and the round's most
   useful output:** every object in this project's history that has ever
   shown `t`-sensitivity -- round99's `R^t`, C121's `η(D^t)`, C123/C124's
   `CS₃`, C126's winding number -- lives in the **differential/secondary**
   layer, or in the **relation** between two backgrounds. Nothing lives in
   the topological invariants of one background. That is a real pre-filter
   (Sec. 8) and it is why C121 and C124 landed where they did.

---

## 3. Step 1 candidates, walked one at a time

**Hypothesis stated once, up front (skeptic finding 8(iii)), because the
first draft contradicted itself by stating it only at the end:** the frozen
`M₄` is **non-compact and Lorentzian** (F1), so `M₁₃` as frozen has **no
bordism class at all**. Everything below is therefore a statement about the
**admissible closed manifolds** an anomaly argument quantifies over, not
about the frozen background itself. *This is not a technicality -- it is the
reformulation: an anomaly constrains field content, never a background
connection parameter.*

### 3a. Candidate (a) -- `G` trivial, **and (b1), which is the same computation**

*(Merged per skeptic finding 8(i): the first draft presented these as two
candidates; both reduce to the same group and the duplication was
unflagged.)*

**Present in frozen content?** The manifold, yes. A global `Spin(13)` /
`Spin(1,12)` structure, **no**:

> [VERIFIED, direct read this session, `SPIN13_TO_SPIN4_DECOMPOSITION.md`
> lines 10-16] *"There is no established `Spin(1,12)` structure group in
> this project — standard supergravity caps at 11D (Nahm's theorem), and no
> consistent 13D parent theory is claimed."* The `4 × S³ × S⁶` product is
> *"treated as independent factors from the start."*

C124 granted the same hypothetical explicitly in order to ask its question;
the courtesy is extended here and the answer is still negative.

**Value:** `Ω^{Spin}_{13}(pt) = 0`. Verified this session against a citing
table (Sec. 4), not repeated on the external document's authority.

**The `S³`-frame-bundle sub-case, and its mis-typing corrected** (skeptic
finding 8(ii)): the frame bundle of `S³` is part of the **tangential
structure**, not an independent `f: M → BG`; treating it as a `BG`-twist
double-counts the tangential data, and the first draft's parenthetical
"`BSO(3)` (or `BSO(4)`)" silently swapped frame-bundle group for isometry
group. Taken on its own terms it is still correct and still dies here:
`S³` is a Lie group, hence parallelizable, so the pullback bundle on any
product is trivial, its classifying map is null-homotopic, and the class
lies in the image of the basepoint map from `Ω^{Spin}_{13}(pt) = 0`.
**[INFERRED** -- verified table + standard parallelizability + basepoint
naturality; the skeptic independently checked every step and found the
conclusion correct for the stated reason, including that the
reduced/unreduced splitting is a non-issue.**]**

### 3b. Candidate (b2) -- `G` from `Isom(S³)`, at the 4D level

Present (rounds 90-112's `G_eff`), but it is a **4-dimensional** gauge
group, so the relevant degree is `Ω^{Spin}_5`, not 13. Deferred to Sec. 5.

**Premise flagged, and Sec. 5 marked conditional on it** (skeptic finding
9): "the 4D gauge group descends from `Isom₀`" is `[CITED]` standard
Kaluza-Klein lore and is **contested**; C125 downgraded it from
`[VERIFIED]` and rebuilt its own argument so as not to depend on it. **Sec.
3 does not lean on it. Sec. 5, X1 and X2 DO** -- the first draft claimed
otherwise and that was an internal contradiction.

### 3c. Candidate (c) -- `G = SU(3)` from the `S⁶` twist bundle

**Present in frozen content?** In a qualified sense C124 already analysed:

> [VERIFIED, direct read this session, C124 `decision.md` Step (a)] The
> twist bundle is `E = S⁻ = T^{1,0}S⁶ ⊕ ℂ` (G69/G73) -- *"a summand of `S⁶`'s
> own spinor bundle, constructed from the `S⁶` `SU(3)`-structure, i.e. it
> exists only after the product ansatz and the `SO(6)→SU(3)` reduction."*

The classifying map is **essential**: `c₃(S⁻) = χ(S⁶) = 2 ≠ 0` [CITED,
G73, 29/29 tests, reused not re-derived]. So this `G` **is** nameable, and
it is what makes Sec. 1's Entity field pass.

**And it is still useless**, because `E` lives entirely on `S⁶` and `t`
lives entirely on `S³`: the class is manifestly the same element at `t=0`
and `t=1`. **Flagged, per skeptic finding 11: this is the already-registered
C119 factor-support / Künneth pre-filter applied, not an independent
derivation.** The first draft presented it as one.

`Ω^{Spin}_{13}(BSU(3))` is `[UNKNOWN]` -- not computed, deliberately: its
value is moot, and computing it would be exactly the "force a computation
onto whatever group is easiest to look up" failure mode `claim.md`
pre-registered against.

### 3d. Candidate (d) -- combinations

Inherits both diagnoses; nothing new.

---

## 4. Step 2 -- literature-first, actually performed

**[VERIFIED-tool, retrieved this session via the arXiv tool; SECONDARY
source -- see the tier correction below]** Y. Tachikawa and M. Yamashita,
*Topological modular forms and the absence of all heterotic global
anomalies*, arXiv:2108.13542v2, **Appendix A, Table 1**, which the paper
attributes verbatim to *"[ABP67, Gia71]"* (Anderson-Brown-Peterson 1967;
Giambalvo 1971):

```
d                    0   1    2    3  4  5  6  7  8    9      10     11  12   13  14  15  16
Ω^spin_d(pt)         Z   Z₂   Z₂   0  Z  0  0  0  Z²   (Z₂)²  (Z₂)³  0   Z³   0   0   0   Z⁵
```

**Tier correction (skeptic finding 6b):** this is a *citing* table, hence
**secondary**; the primaries ABP67/Gia71 were **not** consulted, and the
first draft's "a primary table" was wrong. One secondary authority replaced
another -- which is still a real improvement over inheriting the external
document's bare assertion, but not what was claimed.

**Independent structural cross-check, performed by the skeptic without
opening the paper and re-verified here** (this is the round's only genuine
corroboration of the numbers): rationally `Ω^{Spin} ⊗ Q ≅ Q[p₁,p₂,…]`, so
the free rank in degree `4k` must be the partition number `p(k)`;
`p(1..4) = 1, 2, 3, 5`, matching `Z, Z², Z³, Z⁵` at `d = 4, 8, 12, 16`
exactly. And the ABP `ko`-summand bottoms forced by `Ω₉ = Z₂²`,
`Ω₁₀ = Z₂³`, `Ω₁₂ = Z³` give exactly `Ω₁₃ = Ω₁₄ = Ω₁₅ = 0`. **The cited
values survive an independent check.**

Three things this settles:

1. **`Ω^{Spin}_{13}(pt) = 0` is TRUE.** The external `Kimi_Agent` number is
   correct; `claim.md` was right to demand it be checked, and it survives.
2. **`Ω^{Spin}_{14}(pt) = 0` and `Ω^{Spin}_{15}(pt) = 0` as well** -- neither
   stated by the external document, and both needed (see 3.).
3. **The external document's dimension is off by one, and the first draft's
   own hedge about this was also off** (skeptic finding 7).
   [VERIFIED-tool, direct quotation retrieved this session from
   I. García-Etxebarria and M. Montero, *Dai-Freed anomalies in particle
   physics*, arXiv:1808.00009v3, §2.1.1]: *"The `d`-dimensional theory will
   only be anomaly free if a certain topological invariant constructed out
   of a particular `(d+1)`-dimensional Dirac operator … actually
   vanishes."*

   **In full Anderson-dual form** (Freed-Hopkins), deformation classes of
   `d`-dimensional reflection-positive invertible theories sit in
   `0 → Ext¹(Ω^ξ_d, Z) → [I_Z MTξ]^{d+1} → Hom(Ω^ξ_{d+1}, Z) → 0`, so **two**
   degrees enter each reading, not one:
   * 13D **topological terms** (invertible theories): needs `Ω₁₃` **and**
     `Ω₁₄`;
   * a 13D parent's own **anomaly** (a 14D invertible theory): needs `Ω₁₄`
     **and** `Ω₁₅`;
   * the **4D** effective theory's anomaly: `Ω₅` **and** `Ω₆`;
   * `Ω^{Spin}_{13}` alone is `Hom(Ω₁₃, R/Z)`-shorthand for the global
     anomaly of a **12**-dimensional theory, which this project does not
     have.

   **Every degree that appears in any 13D reading vanishes** -- `Ω₁₃ = Ω₁₄
   = Ω₁₅ = 0` in the same verified table -- so all readings close. That is
   luck, not correctness, and is recorded as such: the first draft wrote
   *"harmless only because 14 also vanishes"*; correctly it is **"14 and
   15"**.

**Searched and not found:** no computation of `Ω^ξ_n(BG)` matching this
project's frozen content. **The first draft's accompanying sentence -- "no
literature construction was found in which a connection-family parameter is
selected by a bordism invariant (consistent with Sec. 2, which says one
cannot exist)" -- is DELETED as false** (skeptic finding 3): Witten's SU(2)
anomaly is precisely a bordism construction attached to a
connection-relating gauge transformation.

**Honest scope note:** neither paper read in full; sections read are named.
`Ω^{Spin}_5(BSU(2))`, `Ω^{Spin×_{Z₂}SU(2)}_5`, and `Ω^{Spin}_5(B G_eff)`
were **not** resolved to values. A web summary offering one was not
corroborated by any primary source and is therefore not reported at all.

---

## 5. Step 3 -- the well-posed reformulations, and why each is BLOCKED

### 5a. Missing ingredient 1 -- *which gauge group acts on `∇^t`?*

`Ω^ξ_n(BG)` cannot be written without `G`, and **this project carries two
live, mutually incompatible descriptions of what `∇^t` is:**

| | description | consequence for `G` | source |
|---|---|---|---|
| **C125** | a **metric affine connection**; torsion `T^t = (2t−1)[·,·]` is a **tensor**, so no frame rotation relates `∇⁰`,`∇¹`; the only relating maps are orientation-reversing isometries | frame bundle's group; `t=0,1` **not** gauge-related; the exchange is **parity** | C125 §0a, §2a |
| **C126** | a **Yang-Mills connection** in `Ω¹(S³, 𝔰𝔬(3))`; `∇⁰`,`∇¹` are **ONE point of `𝒜/𝒢`**, separated in `𝒜/𝒢₀` by a large gauge transformation of **winding `n = −1`** (computed two independent ways) | `SO(3)`/`SU(2)`; `t=0,1` **are** gauge-related, by a large transformation | C126 (N3), §"(2)" |

Both are correct about their own object -- the discrepancy is the
**soldering form**: an affine connection carries the vielbein as part of
its data; a Yang-Mills connection does not.

**Checked this session, because the skeptic could not settle it and it
determines whether this is one new ingredient or zero** (skeptic finding
11): each round **named its own half** -- C126 says verbatim *"the metric
`g` itself is never varied anywhere in this round … the connection/metric
split is exactly what `S_YM` cannot see"*, and C125's §0a makes the
tensor-versus-frame-rotation point -- but **neither reconciled them, and
`grep` over `OPEN_BLOCKERS.md` and `CLAIM_LEDGER.yaml` finds no entry
recording the pair or the choice between them.** The ingredient is real and
unrecorded.

This is not bookkeeping: the C126 reading is *precisely* the setting where
global anomalies live (a transformation not connected to the identity,
`π₃(SO(3)) = Z`), while under the C125 reading there is no gauge
transformation to be anomalous about at all.

### 5b. The 4D reformulation, and Horn A split into A1 / A2

**Conditional on the contested `Isom₀` premise** (Sec. 3b). Fix
`Ω^{Spin}_5(B G_eff)` -- or, per skeptic finding 1, the correct twisted
structure `Ω^{Spin×_{Z₂}…}_5`, since `R` is half-integral. The `t`-dependence
enters through the content: `R(0)` on `ker(D_{S³},t=0) = (1,2)`, `R(1)` on
`ker(D_{S³},t=1) = (2,1)` [CITED, C38 via C125 §3a], `S⁶` side identical.

This is **not** a mechanism-transfer duplicate of rounds 90-112, which
computed *perturbative* anomalies only (triangle channels, mixed `U(1)_Y`,
`[SU(2)]³`) and never a Dai-Freed/global one.

**A1 -- SELECTION: excluded.** [CITED, C125 §2a] `ι` is an isometry of `S³`
with `ι_*∇⁰ = ∇¹`, realizing `σ: SU(2)_a ↔ SU(2)_b` (`ι∘φ_{a,b}∘ι =
φ_{b,a}`, C125 `A2`); `S⁶` untouched. So `R(1) = (σ×id)^*R(0)`, and
`α_{R∘σ} = α_R ∘ σ_*` with `σ_*` an **isomorphism** -- hence `α_{R(1)} ≡ 0
⟺ α_{R(0)} ≡ 0`. **The skeptic independently confirmed this inference and
its robustness:** it does *not* need `σ` inner, does not need `σ_*` trivial
(surjectivity suffices), survives realization by an orientation-reversing
map (`α(−M) = −α(M)`), and survives the two `ξ`'s of finding 1 differing
(`σ_*` is then an isomorphism *between* two groups, and the "iff" is
unaffected). `[INFERRED]`. **The weak link is not naturality (standard) but
that `R(t)` is exhausted by (S³ kernel) ⊗ (t-independent S⁶ factor)** --
asserted, not shown, and correctly renamed here per skeptic finding 4.

**A2 -- PAIR-FORCING: NOT excluded.** *(The first draft banked
"No discrimination, for any bordism group, computed or not"; that sentence
is DELETED.)* `claim.md` pre-registers pair-forcing as an equally valid
success mode. It asks about `α_{R(0)} ± α_{R(1)} = α_{R(0)}∘(1 ± σ_*)`. In
the **minus** case -- exactly what an orientation-reversing `ι` produces,
and C125 says every relating map is orientation-reversing -- **the sum can
vanish identically while each term does not**, which is the standard
mirror/vector-like cancellation (it is how even numbers of `SU(2)` doublets
evade Witten's anomaly). That is a positive result of precisely the
pre-registered shape: *neither `t` alone is admissible; the pair is
forced.* **Unattempted. Not excluded. Blocked on Sec. 5a.**

**Horn B -- the circularity, unchanged.** Discrimination via a specific
SM-like subgroup requires declaring which `SU(2)` is `SU(2)_L`. But *"the
L/R labelling of the two factors is a convention; only the exchange is
invariant"* [CITED, C125 §3a], and fixing it is exactly C125's `UNDECIDED`
`ε₄ε₆` question, traced to **round95's recorded absence of an `S⁶`-channel
↔ `S³`-`t`-sector link**. Choosing it inputs the answer -- the circularity
`claim.md`'s own kill criterion forbids.

### 5c. Restatement check (mechanism-transfer gate), run honestly

The reason A1 and Horn B close is the `ι`-exchange symmetry, and that is
**not new** -- it restates C125 §5 point 3 (*"the odd datum must be an
`S³`-orientation pseudo-invariant … and it must not be accompanied by a
compensating `M₄` or `S⁶` orientation flip, or the two `ℤ₂`s cancel and the
selector goes blind"*). Stated here only because it explains in one
sentence why C121's `η mod 2` came out constant, why C124's reduced
`V(t) = A + B·t(1−t)` came out even, and why round116 found "no
`n`-dependent structure privileging `n=0`". **No novelty claimed.**

### 5d. The mapping-torus route -- the object the first draft omitted

**Written entirely in response to skeptic finding 3.** This session's
scoping did consider the mapping torus and then failed to put it in the
writeup; that is a defect of the writeup and is recorded, not excused.

The standard global-anomaly construction attaches a bordism class not to
one background but to the **mapping torus of the transformation relating
two** [CITED, arXiv:1808.00009 §2.1.1, eqs. (10)-(11): *"One constructs an
auxiliary `(d+1)` dimensional space as the quotient `X×[0,1]/r`"*, with an
interpolating gauge field `A_t = (1−t)A₀ + tA₀^g` -- structurally the same
shape as this project's own `∇^t` family].

Applied here, under the C126 reading of Sec. 5a: `∇¹ = g·∇⁰` with
`winding(g) = −1`, so the `SU(2)` bundle over `S³ × S¹` clutched by `g`
carries `∫c₂ = −1 ≠ 0` [**INFERRED** -- the instanton number of the
interpolating configuration equals the Chern-Simons difference across the
ends, which is C126's own `n = −1`, computed there two independent ways;
the identity is standard and was **not** re-derived here]. `S³ × S¹` is
spin, so this is a genuinely nonzero class in `Ω^{Spin}_4(BSU(2))`, and
**the nonzero-ness needs no group computation** -- a nonzero characteristic
number on it suffices.

**Why this does not rescue item 8, stated without softening the concession:**

1. **As a number it is a restatement.** `∫c₂ = −1` *is* C126's winding
   number. Under F4's own pass criterion and
   `feedback-mechanism-transfer-gate-2026-07-17`, that is round116's fate
   ("equivalent restatement, no new content"), not a new mechanism.
2. **It detects the pair, not a member of it.** Consistent with A1: this
   is a `Z`-valued (or `Z₂`-valued after `η`) invariant of the *relation*,
   and no reading of it privileges `t=0` over `t=1`.
3. **The only step that could force the pair -- evaluating the anomaly
   homomorphism (`η` / mod-2 index) on this class for the actual fermion
   content -- is exactly A2, blocked on Sec. 5a.** Which gauge group acts
   decides whether the mapping torus even exists as a physical object.

**But it does mean the first draft's instruction to future rounds was
wrong**, and it is withdrawn in Sec. 6.

---

## 6. Kill Analysis (Anti-Overfitting Gate)

### What this round KILLS

* **Relaxation Map item 8 in its SELECTION reading only.** A topological
  invariant of a single fixed background cannot select `t` (Sec. 2).
  **Narrowed from the first draft, which killed the whole item** -- see
  "does NOT kill" below.
* **The reading of `Ω^{Spin}_{13} = 0` as *the* answer.** Correct number
  (Sec. 4, verified and independently cross-checked), wrong dimension, and
  incomplete even in its own reading (needs `Ω₁₄`; the anomaly reading
  needs `Ω₁₄` and `Ω₁₅`). The external argument is right on three
  accidents at once.
* **The `S⁶`-twist route (candidate c) as a `t`-selector**: `E`'s
  classifying map is essential (`c₃ = 2`) but sits on the factor `t` does
  not touch, so its class is literally the same element at `t=0,1`.

### What this round does NOT kill

* **The mapping-torus / pair-forcing route (Sec. 5d, A2).** Well-posed,
  nonzero, unattempted, blocked -- not falsified. **The first draft's
  "item 8 should not be retried in this form" is WITHDRAWN and replaced
  by the narrow form: it should not be retried as *a bordism class of the
  single frozen background*.**
* **The 4D global-anomaly question** (Sec. 5b). Not a duplicate of rounds
  90-112 (perturbative only). Unanswered.
* **Differential / secondary invariants.** In particular **C121's own
  surviving variant, the APS reduced eta `ξ = (η+h)/2 mod 1`** [CITED,
  C121 via `PARENT_ACTION_GATE.md` F4] -- unattempted, and in the layer
  that *can* see `t`.
* **A parent action with an independent 13D gauge field** (C124's V1);
  **non-product / warped backgrounds**; **the `Spin(1,12)` hypothetical**.
* C123's `PARTIAL`, C124's `STRUCTURAL_NO_GO`, C125's `FALSIFIED`, C126's
  finding, C119's F1 `FAIL`, C121's `NULL` -- untouched, none re-litigated.
* `N_gen=3`'s CONDITIONAL status, `lambda = FREE_COUPLING_PARAMETER`,
  `sm_derivation_claimed = False`, `safe_for_runtime = False`, OB1's
  `PARKED` -- unaffected, as pre-registered.

### Relaxation Map (one assumption changed per variant, none attempted here)

| Variant | Single assumption changed | Kill criterion |
|---|---|---|
| **X6** *(new, from skeptic finding 3 -- the first draft had no mapping-torus variant)* | Ask for the class of the **mapping torus** of C126's winding-`(−1)` transformation, and evaluate `η` / the mod-2 index on it for the actual content | Does it force the pair (`α_{R(0)} + α_{R(1)} ≡ 0` with each term nonzero), or does it merely re-report `n = −1`? The class alone is a restatement; only the anomaly evaluation is new. Prerequisite: X2. |
| X1 | Ask about the **anomaly homomorphism** on a fixed `Ω^ξ_5(B G_eff)`, not about generators (Sec. 5b) | Does it escape Horn B's circularity without inputting the L/R labelling? **Conditional on the contested `Isom₀` premise.** |
| X2 | **Reconcile C125's frame-bundle reading against C126's Yang-Mills reading** (Sec. 5a) | Prerequisite for X1 and X6, and cheap: both readings are already computed; only the choice is missing. Confirmed unrecorded in `OPEN_BLOCKERS.md` / `CLAIM_LEDGER.yaml` this session. |
| X3 | Move to the **differential** layer: APS reduced eta `ξ = (η+h)/2 mod 1` | Does `ξ` distinguish `t∈{0,1}` from other crossing pairs, given `h` also jumps at each crossing? C121 says materially different from `η mod 2`; untested. |
| X4 | Treat C126's `n = −1` as a `Z`-valued (not `Z₂`) datum and ask what a selector built on it needs | C126's own second pearl predicts any CS-built or winding-built functional distinguishes them; C124 killed the 13D-covariant CS route. Does an `S³`-internal one survive F6? |
| X5 | Grant an independent 13D gauge field (C124's V1); ask for `Ω^{Spin}_{14}(BG)` | Sec. 2 still applies to the single background's class; only the relation or the content can move. Listed so it is not silently retried as "the twisted version we never did". |

---

## 7. What this round does NOT show

1. Does **not** resolve OB1 or move it out of `PARKED`. No reopen
   condition from `OPEN_BLOCKERS.md`'s 4-item list is met.
2. Does **not** compute any bordism group; reported values are cited from
   a **secondary** table (Sec. 4).
3. Does **not** show that no bordism argument can bear on OB1 -- only that
   no invariant of a *single fixed background* can **select** `t`. The
   first draft claimed the stronger thing and was wrong (Sec. 0, findings
   3 and 12).
4. Does **not** answer, or attempt, the pair-forcing question (A2 / X6).
5. Does **not** claim novelty for the `ι`-exchange explanation (Sec. 5c),
   for the factor-support argument (Sec. 3c, = C119's filter applied), or
   for Sec. 2's observation (definitional).
6. Does **not** resolve C125's `UNDECIDED` `ε₄ε₆` question or round95's
   missing link -- only shows a second route terminates there.
7. Does **not** adjudicate C125-vs-C126 (Sec. 5a); named as X2.
8. Does **not** read arXiv:2108.13542 or arXiv:1808.00009 in full, nor
   consult ABP67/Gia71 directly.
9. Does **not** change `N_gen=3`, `lambda`, `sm_derivation_claimed`, or
   `safe_for_runtime`.
10. Does **not** solicit Tom Lawrence's Part 5 or initiate any contact.

### 7a. Novelty ledger (single, per skeptic finding 10)

*The first draft asserted "the only genuinely new content" three times, of
three different things, and retracted one of them four lines later.*

| Item | Status |
|---|---|
| Sec. 2's connection-blindness observation | **Definitional.** A restatement of what a bordism cycle is. Useful as a pre-filter; not a result. |
| Sec. 5b's 4D Dai-Freed framing (A1/A2) | **New framing, uncomputed.** Not a duplicate of rounds 90-112. |
| Sec. 5a's C125-vs-C126 gap | **New, and confirmed unrecorded** this session. |
| Sec. 5d's mapping torus | **Not new as a number** (= C126's `n = −1`); new only as the observation that the route was omitted. |
| Sec. 4's `Ω₁₄ = Ω₁₅ = 0` and the Anderson-dual second degrees | **New to this project's record**, cited not derived. |
| **New *results*** | **Zero.** |

**Adopted as this file's framing, from the skeptic's own one-line
summary:** *"the class of a single frozen background is connection-blind,
so any `t`-selector must be built from the relation between two backgrounds
-- and every such relation in this project is a symmetry (`σ`/`ι`), which
kills selection but leaves pair-forcing open and blocked on Sec. 5a."*

---

## 8. Proposed pearl (not written to `pearl_registry/INDEX.md` by this
round -- editing the registry is outside this round's brief, per C124's and
C125's precedent)

**Rescoped before proposal, per skeptic finding 12** -- the first draft's
version would have auto-killed both the mapping-torus route (whose
characteristic number is `−1 ≠ 0`) and the differential layer (X3), which
this same file says survive.

* **observation:** a selector for a parameter entering **only through a
  connection** cannot be a topological invariant **of a single fixed
  background** (bordism class, characteristic number, homotopy class of a
  classifying map) -- those are connection-blind by construction. It must
  be either a **differential/secondary** invariant (Chern-Simons, APS `η`,
  holonomy) **or** an invariant of the **relation between two backgrounds**
  (mapping torus, spectral flow, relative index). **Both carve-outs are
  part of the pearl, not exceptions to it.**
* **falsifiable_prediction:** every future OB1 F4 candidate phrased as "a
  topological invariant of the background that distinguishes `t=0` from
  `t=1`" fails with no computation; every candidate that has *ever* shown
  `t`-sensitivity in this project (round99's `R^t`, C121's `η`,
  C123/C124's `CS₃`, C126's winding number) falls in one of the two
  carve-outs.
* **impact_score:** 4 *(revised down from 5 after the skeptic pass showed
  the underlying observation is definitional and the first draft's scope
  was wrong -- recorded, not hidden)*.
* **trigger_condition:** any future F4 candidate described as a
  topological invariant **of the background**. **Explicitly NOT triggered
  by** "a bordism/cobordism argument" in general -- the first draft's
  trigger was that broad and would have been wrong.
* **next_check:** 2026-12-01.
* **Scope limit:** the filter says *where* a `t`-selector must live, not
  that one exists there.

---

## 9. Verification

| Tier | Claim |
|---|---|
| `[VERIFIED-tool, SECONDARY source]` | `Ω^{Spin}_d(pt)`, `d=0…16`, incl. `Ω₁₃ = Ω₁₄ = Ω₁₅ = 0` -- arXiv:2108.13542v2 App. A Table 1, itself citing `[ABP67, Gia71]`; primaries not consulted. **Independently cross-checked structurally** (free rank `= p(k)` at degree `4k`: `1,2,3,5` ✓; ABP `ko`-bottoms at 0, 8, 10 force 13/14/15 to vanish). |
| `[VERIFIED-tool]` | The `d → d+1` convention -- direct quotation from arXiv:1808.00009v3 §2.1.1, retrieved this session, together with its mapping-torus eqs. (10)-(11). |
| `[CITED]` | Freed-Hopkins Anderson-dual sequence `0 → Ext¹(Ω_d,Z) → [I_Z MTξ]^{d+1} → Hom(Ω_{d+1},Z) → 0` -- standard, **not** re-derived here; supplied by the skeptic pass and accepted. |
| `[INFERRED -- own derivation, scope corrected twice by the skeptic pass]` *(downgraded from `[VERIFIED]`, skeptic finding 6a)* | Sec. 2's connection-blindness observation, in its corrected (single-background, lift-of-classifying-map) form. |
| `[VERIFIED]` (direct read this session, not memory) | `SPIN13_TO_SPIN4_DECOMPOSITION.md:10-16`; C124 Step (a); C125 §0a/§2a/§3a/§5; C126 (N3), §"(2)", and its "the connection/metric split is exactly what `S_YM` cannot see"; `PARENT_ACTION_GATE.md` F1/F2/F4/F5; round86's "Why BLOCKED, not FAIL". **`grep` of `OPEN_BLOCKERS.md` + `CLAIM_LEDGER.yaml`: no entry reconciling the C125/C126 readings of `∇^t`.** |
| `[INFERRED]` | Sec. 3a's "class is identically zero" (table + parallelizability + basepoint naturality; every step independently checked by the skeptic and found correct). Sec. 5b A1's `α_{R∘σ} = α_R ∘ σ_*` (standard; skeptic-confirmed robust). Sec. 5d's `∫c₂ = −1` (CS-difference = instanton-number identity, standard, using C126's own `n = −1`). |
| `[CITED]` | `c₃(S⁻) = χ(S⁶) = 2`, `ind = +1` (G73, 29/29). `ker(D_{S³},t=0)=(1,2)`, `t=1 → (2,1)` (C38). Round95's missing link. Round113's F3. C121's `η` NULL and its surviving `ξ`. **Kaluza-Klein "gauge group from `Isom₀`" -- contested lore; Sec. 5, X1, X2 are conditional on it (skeptic finding 9).** |
| `[UNKNOWN]` -- deliberately not computed and not guessed | `Ω^{Spin}_{13}(BSU(3))`; `Ω^{Spin}_5(BSU(2))`; `Ω^{Spin×_{Z₂}SU(2)}_5`; `Ω^{Spin}_5(B G_eff)`; `Ω^{Spin}_4(BSU(2))`'s full structure (only "the class is nonzero" is used, which needs no group computation). Everything in Sec. 6's "does NOT kill" and X1-X6. Whether `R(t)` is genuinely exhausted by (S³ kernel) ⊗ (t-independent S⁶ factor) -- A1's real weak link. |

**No script, no `results_c127.json`.** A scoping-and-literature round whose
output is a gate verdict, matching round86's own precedent. Claiming a
computation here would be the exact failure mode `claim.md` pre-registered
against.

**No pytest suite touched, no shared code modified.**

## Check (reproduces this decision)

1. arXiv:2108.13542 App. A Table 1 -- the `Ω^spin_d(pt)` row must read
   `Z, Z₂, Z₂, 0, Z, 0, 0, 0, Z², (Z₂)², (Z₂)³, 0, Z³, 0, 0, 0, Z⁵`,
   attributed in the paper's own text to `[ABP67, Gia71]`.
2. arXiv:1808.00009 §2.1.1 -- the sentence beginning *"The `d`-dimensional
   theory will only be anomaly free…"*, and eqs. (10)-(11)'s mapping torus.
3. `grep -n -i -E "reconcil|frame bundle|yang-mills connection|soldering"
   CLAIM_LEDGER.yaml` and the same over `OPEN_BLOCKERS.md` -- must return
   **no** entry reconciling C125's and C126's readings of `∇^t` (Sec. 5a).
4. **Falsifier for the SELECTION half, stated so it can fail:** exhibit a
   tangential structure `ξ`, a group `G`, and two members of the
   Cartan-Schouten family whose classes in `Ω^ξ_n(BG)` **for one and the
   same closed background** differ. Per Sec. 2 this is impossible.
   *Note the hypothesis carefully -- the mapping torus of Sec. 5d is NOT a
   counterexample, because it is a class of a relation between two
   backgrounds, not of one. The first draft's falsifier omitted the
   hypothesis and was therefore refuted by this file's own Sec. 5d.*
5. **Falsifier for the PAIR-FORCING half:** there is none yet -- A2/X6 is
   unattempted. That is the honest state, and it is why the verdict is
   BLOCKED rather than a no-go.
