# C128 decision -- which mathematical category is `∇^t`?  C125's affine
# connection vs C126's Yang-Mills connection.
# (C127 Relaxation Map item X2; prerequisite for X1 and X6.)
#
# HEADLINE, stated first and already demoted by TWO independent FL Step 8a
# skeptic passes (both returned `WEAKENED`; 27 findings; every one answered
# below, 24 accepted and repaired, 3 answered-with-reason, none waved through):
#
# **OUTCOME (B) on the LITERAL pre-registered predicate, and the strongest
# form of that answer was supplied by the skeptic pass, not by the first
# draft:**
#
#   No smooth map `f` of `S³` whatsoever -- diffeomorphism or not, global or
#   local -- has frame-transition function `M_f = +Ad`. The obstruction is
#   Maurer-Cartan integrability: `M_f = Φ` forces `dΦ + Φ∧Φ = 0`, and for
#   `Φ_λ(X_j) = λ·xT_jx^{-1}` that expression equals
#   `λ(1+λ)·ε_{ijk}xT_kx^{-1}`, which vanishes **iff `λ ∈ {0,−1}`**.
#   `λ = −1` is `M_ι` (integrable, and realized by `ι`); `λ = +1` is C126's
#   `g = Ad` (NOT integrable). Measured across 8 values of `λ` against the
#   closed form to `4.5e−11`; residual `2.3e−11` at `λ=−1` vs `0.9903` at
#   `λ=+1`.
#
# **BUT THE FIRST DRAFT'S GLOSS IS WITHDRAWN.** It billed this as "genuinely
# different transformation groups" locked by a `det`↔`winding` correlation.
# The second skeptic pass showed that is wrong in two ways, and it is right:
#   * `M_ι = (−I)·g`. The difference between "geometric" and "gauge" is **one
#     central constant `−I`**, which CANCELS in `u^{-1}du` -- so if the
#     structure group is taken as `O(3)` rather than C126's stated `SO(3)`,
#     `−Ad` is simultaneously a gauge transformation AND `dι`, and it does
#     carry `ω⁰` to `ω¹`. "Genuinely different groups" is not the right
#     description; "the same group up to a central `ℤ₂`" is.
#   * The winding half of the "lock" is **not even trivialisation-invariant**:
#     under a change of global frame `R`, `[M'_f] = [M_f] + [R] − f^*[R]`, and
#     `f^*[R] = deg(f)[R] = −[R]` for exactly the orientation-reversing maps
#     that carry nonzero winding. `det M_f` IS invariant (it is the
#     orientation character). **So the operative obstruction is `det` -- which
#     is C125's already-certified `ℤ₂` -- and winding plays no role**, exactly
#     as this file's own §3b already said and its §2 headline contradicted.
#
# **WHAT IS GENUINELY NEW, after both passes stripped the overclaims (§9a):**
# §4's theorem (any diffeomorphism carrying `∇⁰` to `∇¹` is automatically an
# orientation-reversing ISOMETRY -- hypothesis weakened from `Isom` to `Diff`,
# now with an exact symbolic proof) and §6b's orientability observation. The
# reconciliation itself is **NOT new**: C126's own Step 6 SCOPE paragraph --
# which this round cites -- already states it in plain words.
#
# NOT covered: whether a `t`-selector exists; C125's `UNDECIDED` Family C /
# `ε₄ε₆`; round95's missing link (C127's ingredient 2, untouched, so X1/X6
# stay BLOCKED); whether a `Pin` structure exists on §6's mapping torus;
# `N_gen=3`'s CONDITIONAL status; Tom Lawrence's Part 5.

**Verdict (2026-09-02; TWO independent FL Step 8a skeptic passes run, both
`WEAKENED`, both incorporated -- Paraphrase-Sensitivity Probe CONCORDANT):**
`OUTCOME_B_ON_THE_LITERAL_PREDICATE_VIA_MAURER_CARTAN__NO_SMOOTH_MAP_AT_ALL_HAS_M_f_EQUALS_PLUS_Ad_BECAUSE_dPHI_PLUS_PHI_WEDGE_PHI_EQUALS_LAMBDA_TIMES_ONE_PLUS_LAMBDA_TIMES_EPS_VANISHING_ONLY_AT_LAMBDA_ZERO_OR_MINUS_ONE__MINUS_Ad_IS_INTEGRABLE_AND_IS_M_iota__GENUINELY_DIFFERENT_GROUPS_GLOSS_WITHDRAWN_THE_DIFFERENCE_IS_THE_SINGLE_CENTRAL_CONSTANT_MINUS_I_WHICH_CANCELS_IN_u_INV_du_SO_UNDER_AN_O3_STRUCTURE_GROUP_THE_PREDICATE_WOULD_FLIP__DET_WINDING_LOCK_DEMOTED_WINDING_IS_NOT_TRIVIALISATION_INVARIANT_FOR_ORIENTATION_REVERSING_MAPS_AND_THE_OPERATIVE_OBSTRUCTION_IS_DET_WHICH_IS_C125s_ALREADY_CERTIFIED_Z2__RECONCILIATION_IS_NOT_NEW_C126_STEP_6_SCOPE_STATES_IT_VERBATIM_AND_THIS_ROUND_CITES_IT__GENUINELY_NEW_IS_ONLY_SECTION_4_THEOREM_ANY_DIFFEOMORPHISM_CARRYING_NABLA0_TO_NABLA1_IS_AN_ORIENTATION_REVERSING_ISOMETRY_NOW_PROVEN_SYMBOLICALLY_BY_GROEBNER_IDEAL_MEMBERSHIP_PLUS_SECTION_6b_MAPPING_TORUS_OF_THE_ACTUAL_RELATING_MAP_IS_NON_ORIENTABLE_SO_OMEGA_SPIN_IS_THE_WRONG_FUNCTOR_FOR_C127_X6__PHYSICAL_ATTRIBUTION_IS_C125s_CATEGORY_BUT_THAT_ATTRIBUTION_IS_C126s_OWN_STRUCTURE_USAGE_FACT_RESTATED__X2_CLOSED_X1_AND_X6_STILL_BLOCKED_ON_INGREDIENT_2_ROUND95`

**Status:** OB1 stays `PARKED`. No reopen condition met. C125's `FALSIFIED`
stands, **strengthened** (§4). C126's `WEAKENED` stands **unchanged** and is
**credited more than the first draft credited it** (§5, §9a). C127's
`BLOCKED` stands; **ingredient 1 (X2) is closed**, ingredient 2 (round95)
untouched, so X1/X6 remain blocked on ingredient 2 alone, and X6's object
must be re-specified first (§6).

**Completeness:** `PARTIAL`, in five named respects.
1. §2's Maurer-Cartan result is **complete and hypothesis-free** for the
   literal predicate. The *classification* of `M_f` over `Isom(S³)` (§2a) is
   exact but **conditional on the `[CITED]`, un-re-derived enumeration
   `O(4) = SO(4) ⊔ SO(4)ι`**, and is a statement in the project's own
   left-invariant trivialisation, not a trivialisation-free one.
2. The physical attribution (§5) is a **restatement of C126's own boxed
   conclusion**, with one added row and the converse direction. It is a
   reading of the frozen construction, not a computation.
3. §6 is worked at the `S³` level. The 13D version is **not defined at all as
   frozen** (`M₄` non-compact), so §6d is conditional on a compactification
   this project does not have -- the caveat now precedes the conclusion.
4. Whether §6's non-orientable mapping torus **admits** a `Pin^±` structure
   (`w₂ = 0`, resp. `w₂ + w₁² = 0`) is `[UNKNOWN]` and is the real gate, not
   the bordism group values.
5. **No literature search was run.** §2a and §4 are elementary and may well be
   standard; the header no longer asserts novelty without this caveat.

**Gate fields assessed:** `PARENT_ACTION_GATE.md` **F4**, and only by
sharpening a pre-filter -- no mechanism supplied. F1/F2/F3/F5 reused by
citation. F6 not assessed (C126 owns it).

---

## 0. ⚠️ TWO FL Step 8a skeptic passes -- both `WEAKENED`, 27 findings, all answered

Both context-blind (`Agent(skeptic, model=opus)`, `claim.md` + `decision.md` +
script only; no session history, no reasoning chain). Run **twice with
differently-worded falsification prompts** per `falsification-ladder.md`'s
Paraphrase-Sensitivity Probe, because this round closes a live Relaxation Map
item. **Both returned `WEAKENED` -- concordant, so the single-run Response
Matrix applies and no skeptic-leaning tie-breaker is needed.** They found
substantially DIFFERENT defects, which is itself the argument for running two.

**Substrate note, per the Substrate Gate:** neither pass had an execution
tool (Read/Write/Edit only). Every check they ran was hand derivation. Per the
gate that is a fact about their substrate, not evidence about the claim -- and
here it is a *strength*: both independently re-derived §2a's three closed
forms and every step of §4 from scratch, so their confirmations are genuinely
independent of this round's code rather than re-runs of it. **The deliberate-
error injections they each asked for but could not run have now been run by
this session (§10).**

### Findings both passes made independently (strongest signal)

| # | Finding | Response |
|---|---|---|
| **A1** | **The gate misses the two headline items.** `ok_keys` collects keys ending `_ok`; `P2_lock_holds` does not, and `C8` had no gate. The det↔winding lock and the `M_ι = (−I)g` factorisation could both break while the script printed `ALL_OK = True`. | **ACCEPTED, repaired, and the repair is DEMONSTRATED.** Renamed `P2_lock_holds → P2_ok`. **Injection run this session:** forcing `const = True` (a false lock) now gives `P2_ok = False`, `14/15`, `ALL_OK = False`; the *identical* corruption under the old gate name gives `14/14`, `ALL_OK = True`. Both passes were right and the fix works. |
| **A2** | **`VERDICT_INPUTS` was hard-coded**, consulting nothing in `out`, while §10 told the reader to verify the round's conclusion against it. | **ACCEPTED, repaired.** Every verdict field is now computed from a measured, gated quantity. The prose reason now names the Maurer-Cartan obstruction and states that `det`, not winding, is operative. |
| **A3** | **`P5_etilde_minus_e_at_identity` computes `\|T_j − T_j\|`** -- no `x`, no `Ad`, no `ẽ`; identically `0.0` for any implementation. A tautology of exactly the species the module docstring claims to avoid, and the same shape as the `B1` defect C125's second pass caught. | **ACCEPTED, repaired.** Now evaluated *through* the real machinery at `x = ±I` (`0.0`, `0.0`) and paired with a **non-central control** (`0.0978`), so the pair discriminates; gated via `P5_center_test_discriminates`. |
| **A4** | **§2b proves a statement about `Isom`; the headline claims `Diff`.** The bridging lemma ("`M_f` is `O(3)`-valued ⟺ `f` is an isometry") lives in the code and in §4 but is never stated in §2b, the section carrying the headline. | **ACCEPTED.** Repaired twice over: the lemma is now stated in §2b, **and** §2 is re-founded on the Maurer-Cartan argument (pass 1's own construction, adopted with credit), which needs neither the lemma nor `Isom(S³) = O(4)` nor Cerf/Hatcher, and covers *all smooth maps*. |
| **A5** | **Five "negative controls" are fixed constants** (`1.0`, `2.00`, `2.00`, `2√6`, `≥2/√3`), so their thresholds cannot fail. §10 cited two of them as evidence the checks can fail. | **ACCEPTED.** §10 now states exactly what they do discriminate (a global sign error, and nothing else) and names the genuinely discriminating controls: `C2`/`C3`/`P8` medians, `P3`'s non-isometric falsifier, `P7`'s `c=+I`, and the new `P9` λ-sweep. |
| **A6** | **`P2` cannot discover anything** -- it draws from the two families already solved in closed form, alternating on `k % 2`, so `250/250` is by construction. It is not a completeness test. | **ACCEPTED.** Demoted in the docstring and in §2a to "consistency re-run"; completeness is explicitly inherited from the `[CITED]` `O(4)` enumeration. Pass 1's two-line topological argument (continuity + `\|π₀(O(4))\| = 2`) is adopted as the real reason. |
| **A7** | **§2c's winding formula is trace-inconsistent** -- `g` is defined as `Ad` (`so(3)`-valued) but the trace is evaluated in the 2-dimensional rep; the same integral in `so(3)` carries a Dynkin factor 4 and gives `−4`. | **ACCEPTED.** Repaired to match C126's own careful wording, which C128 had dropped: the integral computes the winding of the **`SU(2)` lift** (the identity map), and `\|n\| = 1` for `Ad` follows from the `[CITED]` `π₃` isomorphism. The factor-4 risk is flagged as travelling downstream into C127 §5d's `∫c₂`. |
| **A8** | **C126 already stated the reconciliation**, in its Step 6 SCOPE paragraph, which C128's own `[CITED]` list names. Also §5's attribution is C126's boxed "structure-usage fact". Also claim.md's premise *"neither aware of the other"* is **false** -- C126 names C125 four times. | **ACCEPTED entire.** §9a's novelty ledger is rewritten; §3 and §5 now open by quoting C126 and stating what is added rather than what is discovered; the claim.md pre-registration defect is recorded in §9b rather than hidden. |

### Findings unique to pass 1 (formal register)

| # | Finding | Response |
|---|---|---|
| **B1** | Constructive: the **Maurer-Cartan obstruction** is a three-line, stronger replacement for §2b. | **ADOPTED with credit, verified, and implemented as `PART 9`** with a discriminating λ-sweep. This is the single largest improvement to the round and it came from the skeptic, not from the first draft. |
| **B2** | §4 has an **unstated hypothesis**: `μ > 0` needs `c` invertible (the script silently filters `\|det c\| > 0.1`). | **ACCEPTED**, stated in §4 (invertibility follows from `f` being a diffeomorphism). |
| **B3** | §4 **does not prove too much**: running the same argument on `f_*∇⁰ = ∇⁰` gives `c ∈ SO(3)`. | **ACCEPTED and implemented as a check** (`PART 10`): swap branch `det ∈ [−1.0000000001, −1.0]`, preserve branch `det ∈ [1.0, +1.0000000007]`, 0 non-orthogonal in either. The machinery discriminates. |
| **B4** | §6(a) is **true but vacuous** -- a mapping torus glued by any `g ∈ 𝒢` joins gauge-equivalent configurations by construction. Also a mapping torus is closed and has no "ends"; the intended object is the cylinder. Also §6a upgrades C127's `[INFERRED]` `∫c₂` to "arithmetic that stands". | **ACCEPTED all three**, repaired in §6. |
| **B5** | §6(c) names `Pin^±` without checking the manifold **admits** such a structure. | **ACCEPTED** -- existence is now named as the real prerequisite and marked `[UNKNOWN]`. |
| **B6** | §3's fibre is misstated: with the metric varying it is `Maps(S³,GL(3))/SO(3)`, not `𝒢/SO(3)`. | **ACCEPTED**; §3 now fixes the metric explicitly, which is what the frozen ansatz does. |
| **B7** | §4's steps 1-2 are **C125 (0c)**, uncited; and C125 closed the non-isometric escape *first* by (0a). | **ACCEPTED**, cited in §4. |
| **B8** | §7 kills a position neither round held. | **ACCEPTED**, rewritten. |

### Findings unique to pass 2 (paraphrased register)

| # | Finding | Response |
|---|---|---|
| **C1** | **The file issued a verdict and a `[VERIFIED]` tier while its own §12 said the mandatory Step 8a pass was NOT YET RUN.** | **ACCEPTED, and recorded rather than quietly fixed by the passes having since run.** The first draft asserted a settled verdict before its own gate. That is a process defect of the same family C127 recorded about its own first draft, and it is logged here permanently. |
| **C2** | **The `det`↔`winding` "lock" is partly a trivialisation artifact**, and the whole obstruction is the single central constant `−I`; under an `O(3)` structure group the predicate would flip to YES. | **ACCEPTED -- the most consequential finding of either pass.** Independently re-derived this session: `det M_f` is trivialisation-invariant (it is the orientation character); the winding of `M_f` shifts by `2[R]` under a change of frame `R` for orientation-reversing `f`, so it is **not** invariant exactly where it is nonzero. And `u = −Ad` gives `u^{-1}du = Ad^{-1}dAd`, identical to `u = Ad` -- the `−I` cancels. The header's "genuinely different transformation groups" is **WITHDRAWN**; §2d is rewritten; the verdict string now says so. |
| **C3** | The header's "the geometric image is **precisely the locus** where they are locked" **contradicts §2d's own** "the image in `π₀` is two points and is not a subgroup". | **ACCEPTED** -- a real internal contradiction, the headline was the wrong half. Corrected to "hits exactly two classes, `(0,+1)` and `(∓1,−1)`; contained in, and not exhausting, the diagonal". |
| **C4** | §3's two-quotient diagram is **a dressed-up way of saying one side is quotiented and the other is not**: at fixed metric `𝒞/𝒢 ≅ 𝒜`, so the "forgetful map" is just `𝒜 → 𝒜/𝒢`. | **ACCEPTED**, and the plain version is *better*, so it replaces the diagram: **fixing the vielbein is a complete gauge-fixing of `𝒢`** (it acts freely on orthonormal frames), so the frozen ansatz's configuration space **is `𝒜` itself**, and C126 quotiented by a group the ansatz had already gauge-fixed. Pearl 3 is demoted accordingly. |
| **C5** | C126's skeptic finding **E9** (the `T_a = −Z_a/2` bridge carries an unremarked orientation flip; do not reuse in an orientation-sensitive round) is cited once and then disregarded -- and this round is orientation-sensitive end to end. | **ACCEPTED as a real omission, and ANSWERED rather than merely conceded** (§10a): every conclusion this round transports is either a **determinant** (frame-independent) or a **relative** sign, and both are invariant under the flip -- flipping all three `X_i` sends `[X_i,X_j] = +ε → −ε` *and* `[Y_i,Y_j] = −ε → +ε`, leaving §4's equation and its `det c = −1` unchanged. The one quantity that is *not* invariant is the **sign of `n`**, which C126 had already flagged and which this round does not use. |
| **C6** | `Ω^{Pin^±}_4` labelled `[UNKNOWN] -- deliberately not guessed` is **too stingy**; they are standard (`ℤ/16`, `0`), and the label converts a lookup into a research task. | **ACCEPTED as procedure, PARTIALLY DISMISSED as fact.** The procedural point is right and the label is fixed. But the pass's own values were marked `[ФАКТ, memory-sourced, not tool-verified]`, and **two arXiv searches this session failed to confirm them**, so adopting them would replace a too-stingy tag with an unverified one. Recorded as `[MEMORY, unverified, LOW]` with attribution, and the genuinely load-bearing `[UNKNOWN]` restated: whether the manifold **admits** a `Pin^±` structure, and which one the frozen content carries (gated on round95). |
| **C7** | Bookkeeping: "every check carries a negative control" is false; "`det M_ι` over 50 maps" is one map at 50 points; the header's "NEW, and stronger" is unhedged against §9's own "very likely standard"; claim.md was written with C126's admission named as "the seed of the resolution" **before** the Zero-Signal Gate, making the round exploratory rather than pre-registered. | **ACCEPTED entire**, all four fixed or recorded (§9b for the pre-registration defect). |
| **C8** | §6d's "third independent route" is not independent (same certified inputs), and its `M₄`-non-compactness caveat **voids** rather than qualifies it, being placed after the conclusion. | **ACCEPTED**, §6d rewritten with the caveat first and the independence claim withdrawn. |

**Nothing dismissed without reason. Three items answered rather than accepted
outright** (C5's transport concern, answered with an invariance argument;
C6's factual half; and A6's implication that `P2` should be deleted -- it is
retained, correctly labelled, because it does catch drift in the closed
forms). **No finding overturned the literal predicate's answer; two of them
(C2, C3) overturned the framing the first draft wrapped around it.**

---

## 1. Zero-Signal Gate (Step −5), run before any computation

| Field | Status | Content |
|---|---|---|
| Entity | **PASS** | `g = Ad : SU(2) → SO(3)`, C126's winding-`(−1)` transformation; re-derived independently (`Ad(x)^{-1}X_i(Ad)(x) = ad(T_i)`, finite differences, err `3.0e−11`, wrong-sign control `2.00`). |
| Falsifiable predicate | **PASS** | Is `g` realizable as the frame action of a map of `S³`? Made precise as `M_f`, defined by `df_x(X_j(x)) = M_f(x)^i{}_j X_i(f(x))`. |
| Measurable outcome | **PASS** | An explicit obstruction with a closed-form predicted value at every point of a one-parameter family. |

The round was pre-registered as permitted to conclude "genuinely incompatible
readings, no reconciliation exists". **It did not, and the permission is not
exercised** -- but see §9b: the pre-registration itself named the resolution in
advance, which is a defect in the *other* direction.

---

## 2. The answer, in its strongest form

**Setup** (C126's conventions verbatim): `T_a = −iσ_a/2`, `[T_i,T_j] = ε_{ijk}T_k`;
`X_i(x) = xT_i`, `Y_i(x) = T_ix`; `⟨A,B⟩ := −2tr(AB)`; `Ad(x)_{ij}` by
`xT_jx^{-1} = Ad(x)_{ij}T_i`; `∇^t_{X_i}X_j = tε_{ijk}X_k`.

### 2a. Maurer-Cartan: no smooth map at all has `M_f = +Ad`

[VERIFIED, `results_c128.json` P9. **Route supplied by FL Step 8a pass 1 and
adopted with credit -- it is strictly stronger than the first draft's.**]

`M_f = Φ` is equivalent to `f^*θ = Φ` for the Maurer-Cartan form `θ`. Pullback
preserves the MC identity, so `dΦ + Φ∧Φ = 0` is **necessary**. For
`Φ_λ(X_j) := λ·xT_jx^{-1}`:

```
dΦ_λ(X_i,X_j)      = λ   · ε_{ijk} x T_k x^{-1}
(Φ_λ∧Φ_λ)(X_i,X_j) = λ²  · ε_{ijk} x T_k x^{-1}
sum                = λ(1+λ) · ε_{ijk} x T_k x^{-1}   = 0  ⟺  λ ∈ {0, −1}
```

Measured against that closed form at the same base points, deviation
`4.5e−11` across `λ ∈ {−2,−1.5,−1,−0.5,0,0.5,1,2}`:

| `λ` | `−2` | `−1.5` | **`−1` (= `M_ι`)** | `−0.5` | `0` | `0.5` | **`+1` (= C126's `g`)** | `2` |
|---|---|---|---|---|---|---|---|---|
| residual | `0.9903` | `0.3714` | **`2.3e−11`** | `0.1238` | `0.0` | `0.3714` | **`0.9903`** | `2.9710` |

> **`λ = −1` integrates and is realized by `ι`. `λ = +1` does not integrate.
> So `g = Ad` is not `M_f` for ANY smooth map `f` -- not a diffeomorphism, not
> an isometry, not even a local one.**

This needs **no** classification of `Isom(S³)`, no `Isom(S³) = O(4)`, no
Cerf/Hatcher, no de Rham splitting, and no `H³` argument. It answers the
literal predicate outright. `claim.md`'s escape clause ("or some winding-`(−1)`
representative of its class") is closed with it: every element of
`𝒢 = Maps(S³,SO(3))` is `det ≡ +1`, and §2c shows the geometric image's
`det ≡ +1` part is constant.

**Bridging lemma, now stated because both passes found it missing from the
first draft's §2b** [VERIFIED, elementary; falsified numerically in `P3`]:
`⟨df X_i, df X_j⟩ = (M_f^TM_f)_{ij}` and `{X_i}` is orthonormal at both ends,
so **`M_f` is `O(3)`-valued at every point iff `f` is an isometry.**

### 2b. The classification over `Isom(S³)` -- correct, and correctly scoped

[VERIFIED -- own derivation, confirmed by finite differences AND independently
re-derived by hand by both skeptic passes]

* `M_{f_{a,b}}(x) = Ad(b)`, **constant**, `det = +1`. Err `2.4e−11`; spread
  over `x` `3.4e−11`; control vs `Ad(a)` median `1.42`.
* `M_ι(x) = −Ad(x)`, non-constant, `det = −1`. Err `1.8e−11`; control vs
  `+Ad(x)` `1.42`. `det M_ι ∈ [−1.0000000000, −0.9999999999]` (**one map,
  `ι`, at 50 points** -- the first draft said "50 maps").
* `M_{f_{a,b}∘ι}(x) = −Ad(bx)`. Err `2.6e−11`; min spread `1.60`; control
  median `1.40`.

> `Im(Isom(S³) → Maps(S³,O(3))) = {constants in SO(3)} ⊔ {(−I)·Ad∘L_b}`.

**Scope, per both passes:** exhaustiveness is **conditional on the `[CITED]`,
un-re-derived `O(4) = SO(4) ⊔ SO(4)ι`**. The cheap reason the image meets only
two components is topological and needs no closed form (pass 1): `f ↦ M_f` is
continuous and `O(4)` has two components. `P2`'s 500-map sweep
(`250/0/0/250`, `|det|−1 ≤ 2.2e−11`) draws from those same two families by
`k % 2` and is therefore a **consistency re-run, not a completeness test** --
relabelled as such.

### 2c. What is invariant, and what the first draft got wrong

**`det M_f` is trivialisation-invariant** and equals the orientation character
of `f`: under a change of global frame `k`, `M'_f(x) = k(f(x))M_f(x)k(x)^{-1}`,
and `det k` cancels. **The winding of `M_f` is NOT invariant**:
`[M'_f] = [M_f] + [R] − f^*[R]` and `f^*[R] = deg(f)·[R] = −[R]` for
orientation-reversing `f`, so it shifts by `2[R]` -- precisely on the maps that
carry nonzero winding. Concretely, in the right-invariant trivialisation
`M'_ι = −Ad(x^{-1})`, whose class is `−n₀`, not `n₀`.

> **Therefore the first draft's "`det`↔`winding` LOCK" is demoted.** `det` is
> the invariant half and is the operative obstruction; **winding is not
> invariant and is not the obstruction** -- which is what §3b already said and
> which the headline contradicted. `[VERIFIED]` for `det`'s invariance;
> `[INFERRED]` for the winding shift, chain as stated. Found by skeptic pass 2.

**And the whole difference is one central constant.** `M_ι = (−I)·Ad`
(measured `1.6e−11`; this is `C1` with `g := Ad` substituted, **not an
independent measurement** -- pass 1's finding, accepted). Equivalently, under
the canonical splitting `O(3) ≅ SO(3) × {±I}` (which exists because 3 is odd),
the projection `A ↦ det(A)·A` sends `M_ι ↦ Ad = g`: **C126's `g` is exactly
the `SO(3)`-component of C125's map, and C125's `ℤ₂` is exactly its
determinant component.** Each round read one projection of the same object.

**Crucially, and this is why "genuinely different groups" is withdrawn:**
`−I` is central and constant, so for `u = −Ad`,
`u^{-1}du = (−Ad^{-1})(−dAd) = Ad^{-1}dAd` -- **identical to `u = Ad`**. If the
structure group is taken as `O(3)` rather than C126's stated `SO(3)`, then
`−Ad` is simultaneously an `O(3)`-gauge transformation *and* `dι`, and it does
carry `ω⁰` to `ω¹`. **The A/B dichotomy is therefore convention-dependent at
the level of the group; what is NOT convention-dependent is the physics**, §3.

### 2d. Winding, reproduced with C126's own qualifier restored

[VERIFIED, `results_c128.json` C9] `Σε_{ijk}tr(T_iT_jT_k) = −3/2 + 0i`;
`K = 1/4`, `R = 2`, `Vol = 16π²`; `(1/24π²)(−3/2)(16π²) = −1.0`.

**Tier and attribution, corrected after both passes:** this trace is in the
**2-dimensional** rep, so what the integral computes is the winding of the
**`SU(2)` lift** (the identity map `S³→SU(2)`) -- C126 said exactly this and
the first draft dropped the clause. `|n| = 1` for `Ad` then follows from the
`[CITED]` fact that `Ad` induces an isomorphism on `π₃`. Written directly in
`so(3)` the same integral carries a Dynkin factor 4 and is `−4`, **not** `−1`.
`C9` takes **no measured input** -- it is closed-form arithmetic -- so it is
tagged `[INFERRED, arithmetic reproduced]`, and calling it a "reproduction by
a separate implementation" was generous. ⚠ **Flagged downstream:** if C127
§5d's `∫c₂ = −1` is for an adjoint/`SO(3)` bundle, the same factor-4 ambiguity
travels with it, unremarked there and here until checked.

---

## 3. The category question, stated plainly (the two-quotient diagram is withdrawn)

**Withdrawn, per skeptic pass 2.** The first draft drew `𝒞/𝒢 → 𝒜/𝒢` and called
it "two quotients by the same group". At fixed metric, `𝒢` acts **freely** on
orthonormal frames (`Λe = e ⟺ Λ = I`), so `𝒞/𝒢 ≅ 𝒜` canonically and the
"forgetful map" is just the quotient `𝒜 → 𝒜/𝒢`. The plain version is better:

> **Fixing the vielbein IS a complete gauge-fixing of `𝒢`. The frozen ansatz's
> configuration space is `𝒜` itself, not `𝒜/𝒢`. C126 quotiented by a group the
> ansatz had already gauge-fixed.** In `𝒜`, `ω⁰ ≠ ω¹`. In `𝒜/𝒢`, `[ω⁰]=[ω¹]`.
> Both are correct; they are the same connection before and after a quotient.

**And C126 said this first.** Its Step 6 SCOPE, verbatim, which this round
cites: *"This is gauge equivalence of the `SO(3)` CONNECTION alone, i.e. after
forgetting the soldering form. As AFFINE connections on `TS³` the two are NOT
equivalent... Nothing here settles C125's question."* **This round formalizes
that sentence; it does not discover it.**

### 3a. Made concrete: the gauge transformation moves the vielbein

[VERIFIED, `results_c128.json` P5] `ẽ_j = Ad(x)^k{}_jX_k(x) = x²T_jx^{-1}`
(err `1.4e−16`) vs `e_j(x) = xT_j`. Median `‖ẽ−e‖ = 0.60`; `ẽ` orthonormal
(`1.6e−15`). Now **checked through the real machinery** at the two central
points (`0.0`, `0.0`) with a non-central control (`0.0978`) — the previous
version of this check was the tautology A3.

### 3b. Why no gauge transformation, large or small, can do it

[VERIFIED, `results_c128.json` P6] `T^t_{ij}{}^k = (2t−1)ε_{ijk}`, and under a
frame rotation `R` the `ε` tensor goes to `det(R)·ε`: `SO(3)` fixes it
(`6.7e−16`), `O(3)⁻` negates it (`6.7e−16`), control `2.00`.

**`𝒢` is `det ≡ +1` by definition, so every element of it -- large or small --
leaves `T⁰ = −ε` at `−ε`.** Winding is irrelevant. This is the section that,
read against §2c, shows the first draft's headline was billing the wrong
character.

---

## 4. The round's one genuinely new theorem

C125 §2a proved its result over `Isom(S³)` and closed the non-isometric escape
by (0a) — condition (i) fixes the vielbein, so the map is metric-preserving *by
the claim's own wording* — and, independently, by `[CITED]` Cerf/Hatcher.
**Steps 1-2 below are C125 (0c) verbatim** and are cited as such (pass 1, B7).

**Theorem.** Let `f ∈ Diff(S³)` with `f_*∇⁰ = ∇¹`. Then `f` is an isometry of
the round metric and reverses orientation; in particular `det M_f ≡ −1`.

**Proof.** Both connections are flat and `S³` simply connected, so each has a
global parallel frame unique up to a **constant** matrix [C125 (0c)]; `∇⁰`'s is
`{X_i}`, `∇¹`'s is `{Y_a}` [VERIFIED here, `2.8e−11`]. So `f_*X_i = c_{ai}Y_a`,
`c` constant and **invertible because `f` is a diffeomorphism** (hypothesis
added per pass 1, B2). With `[X_i,X_j] = +ε_{ijk}X_k` and
`[Y_i,Y_j] = −ε_{ijk}Y_k` (both verified by finite-difference Lie brackets,
`1.0e−11` / `1.4e−11`):

```
−ε_{abm} c_{ai} c_{bj}  =  ε_{ijk} c_{mk}          for all i,j,m.        (E)
```

Contracting with `c_{mk'}` gives `c^Tc = −det(c)·I`; with `μ := −det(c) > 0`,
`c/√μ ∈ O(3)` and `det(c) = ±μ^{3/2} = −μ` forces the `−` sign and `μ = 1`.
Hence `c ∈ O(3)` with `det c = −1`. Both frames are orthonormal, so `f` is an
isometry; they are equi-oriented (`Y_a = Ad(y^{-1})_{ka}X_k`, `Ad ∈ SO(3)`), so
`f` reverses orientation. Finally `M_f(x) = Ad(f(x)^{-1})·c`, so
`det M_f = det(Ad)·det(c) = −1`. ∎

**EXACT SYMBOLIC PROOF of the load-bearing implication** [VERIFIED,
`c128_symbolic_lemma.py`, **a second, independent implementation** —
Groebner-basis ideal membership over **Q**, not a floating-point search]:
all **9** entries of `c^Tc + det(c)·I` reduce to `0` modulo the ideal generated
by (E); the negative control `c^Tc − det(c)·I` does **not** reduce; `c = −R_z(θ)`
satisfies (E) identically for symbolic `θ` while `c = +R_z(θ)` does not;
`diag(1,1,−1)` satisfies it and `diag(1,−1,−1)` does not; residual at `c = +I`
is exactly `2√6`, matching the independent numerical `4.898979485566356` to
all printed digits.

**It does not prove too much** [VERIFIED, `P10`, pass 1's B3 implemented]: the
same argument on `f_*∇⁰ = ∇⁰` gives `c^Tc = +det(c)I`, hence `c ∈ SO(3)`.
Measured: swap branch `det ∈ [−1.0000000001, −1.0]` (103 roots), preserve
branch `det ∈ [1.0, 1.0000000007]` (97 roots), **0 non-orthogonal in either**.

**Scope, per pass 1 (B7/F11):** the *route* is independent of C125's
torsion-is-the-volume-tensor identity, but the **mechanism is the same `ℤ₂`** —
the sign flip of `ε_{ijk}`. "Independent" applies to the derivation, not to the
underlying fact. And per §9, **no literature search was run**: this may well be
the classical Cartan-Schouten statement.

---

## 5. Physical attribution -- which reading the frozen ansatz uses

**Credit first, per finding A8: this is C126's own conclusion.** C126 Step 6,
boxed: *"functionals of `ω` alone are blind to `t=0` vs `t=1`...; functionals
that use the soldering form are not blind, and **every `t`-dependent quantity
this project has ever computed lives in the second class**."* C126 also lists
`T⁰=−T¹`, round111's `Scal(∇^t)`, C124's `B₃`, C120's `(2t−1)Vol`, and the
Dirac/soldering point. **Five of the six rows below are C126's, with C126's
citations.** What this round adds is the `η(D^t)` row, the converse direction,
and the observation that the gauge-fixing is complete (§3).

| object | why it needs the soldering form | source |
|---|---|---|
| `D_{S³,t}`; `ker(D,t=0)=(1,2)`, `ker(D,t=1)=(2,1)` | Clifford multiplication **is** the soldering form | [CITED] C38; C126 |
| torsion `T^t = (2t−1)[·,·]` | `T = De` | [CITED] C124, round99/113 |
| `Scal(∇^t) = Scal_LC − 6(2t−1)²` | contorsion contracted with the metric | [CITED] round111 |
| `B₃ = e_i∧T^i` | `e` explicit | [CITED] C124 Sector II |
| `(2t−1)·Vol·Vol` | volume form from `e` | [CITED] C120 |
| `η(D^t)` | spectrum of a Dirac operator | [CITED] C121 — **the one row C126 did not list** |

**Converse (this round's own increment):** nothing in the frozen ansatz commits
to C126's category. `𝒜`/`𝒢` are the right objects only for an `SO(3)` bundle
with **no** soldering, i.e. an independent Yang-Mills sector — C124's variant
V1, a hypothetical this project does not freeze.

`[VERIFIED]` for the table (direct read of the cited rounds, plus §3b).
`[INFERRED]` for the step to "the ansatz commits to the C125 category".

### 5a. Which question does OB1 F4 need? -- with the "parity" gloss FIXED

**⚠ The first draft wrote "the only relating maps are orientation-reversing,
*i.e. parity*". That gloss is withdrawn.** It slides from a geometric fact
(`det M_f = −1`) to a physics claim (that the map is *parity*, a symmetry of
the action) — which is **exactly** the inference
`null_results/INDEX.md`'s Round117 entry exists to forbid: *"do not treat
isometry-group component membership as a proxy for action-symmetry or
physical-mechanism-invocation in any future round."* See §5b.

| question | whose category | answer on record |
|---|---|---|
| Are `(e,ω⁰,E,ψ)` and `(e,ω¹,E,ψ)` the same physical configuration? | C125's (i.e. in `𝒜`, after the ansatz's own complete gauge-fixing) | No: `T⁰ ≠ T¹` as tensors. Every relating map is **orientation-reversing**. Whether any such map is a *symmetry of the action* is a **separate, open** question this round does not touch. |
| Can a functional `F[ω]` select `t`? | C126's; valid in either category | No if `𝒢`-invariant and `ω`-only. Possibly yes if it uses the soldering form, or is only `𝒢₀`-invariant. |

### 5b. Reconciliation with Round117's standing warning (FL Step −3, novelty check)

`null_results/INDEX.md` records Round117 (`FALSIFIED`): it compared `S³`'s `ι`
and `S⁶`'s orientation flip, confirmed both lie in `O(n)\SO(n)`, and was
**killed by its own skeptic for testing the wrong question** — component
membership is not action-symmetry, and the two `ℤ₂`s act on structurally
different data. Round80 §D adds, grep-verified: **`ι` is never invoked by any
established construction in this project.**

**Does C128 repeat that error? Checked line by line: no, with one wording
exception now fixed.**
* §2/§4's use of `det M_f` answers a **mathematical** question (is `g` in the
  image?), not a physical one. Not a proxy.
* §3b is a **direct tensor computation** (`ε` is `SO(3)`-invariant), which is
  precisely the "real criterion" Round117 said was missing from its own test.
* §5's attribution enumerates **which objects contain `e`** — structural, not
  group-membership.
* **The exception:** the "i.e. parity" gloss in §5a, now removed. It was the
  one place this round let a component-membership fact carry a physics
  connotation.

**This round therefore does not revive Round117's dead branch, and it does not
claim to advance round80's tension**, which remains exactly as open as
round80 left it.

---

## 6. Consequence for C127's X6 (the mapping torus)

**Caveat first, per pass 2 (C8) — it voids rather than qualifies what
follows:** as frozen, `M₄` is **non-compact** (C127 §3), so **no 13D mapping
torus is a closed manifold at all** and carries no bordism class. Everything
below is at the `S³` level, or conditional on a compactification this project
does not have.

**(a) The mapping torus of `g` is not the `t=0 ↔ t=1` relation** — but this is
weaker than the first draft made it sound (pass 1, B4). A mapping torus glued
by *any* `g ∈ 𝒢` joins gauge-equivalent configurations **by construction**;
that is not a finding. The non-vacuous content is only §3a's `ẽ ≠ e`. (Also:
a mapping torus is closed and has no "ends" — the intended object is the
cylinder before gluing.) C127 §5d's `∫c₂ = −1` remains **`[INFERRED]`, as
C127 tagged it** — the first draft upgraded it to "arithmetic that stands",
which it should not have, and see §2d's factor-4 flag.

**(b) The mapping torus of the map that *does* relate the two frozen
configurations is non-orientable.** By §4 that map is orientation-reversing;
the mapping torus of an orientation-reversing diffeomorphism of an oriented
manifold is non-orientable [CITED, standard — the Klein bottle is the `S¹`
case], so `w₁ ≠ 0`, no Spin structure, **no class in `Ω^{Spin}_4`.**
`Ω^{Spin}` is the wrong functor. `[INFERRED]`, chain as stated. **This is the
round's second genuinely new item.**

**(c) The honest reformulation, and what is actually unknown.** The object is a
`Pin^±` (or twisted-`Pin`) class on a non-orientable 4-manifold. Per pass 1
(B5), **existence is the prerequisite**: `Pin^+` needs `w₂ + w₁² = 0`, `Pin^-`
needs `w₂ = 0`, and neither is checked here — `[UNKNOWN]`. Skeptic pass 2
supplied `Ω^{Pin^+}_4 = ℤ/16`, `Ω^{Pin^-}_4 = 0` from memory, explicitly
un-tool-verified; **two arXiv searches this session failed to confirm them**,
so they are recorded as `[MEMORY, unverified, LOW]` with attribution and are
**not used**. Pass 2's procedural point is accepted: the group values are not
the blocker — the structure's existence and the fermion content's `Pin` type
are, and the latter is gated on round95. **Caveat-Gate-pearled below.**
Note also, per pass 2, that parity ↔ `Pin` bordism is textbook Dai-Freed
practice, so §6c claims no novelty either.

**(d) 13D bookkeeping — conditional, and NOT an independent route** (pass 2,
C8). Given a compactification, C125's certified `ε₁₃` table gives: `ι̃` has
`ε₁₃ = −1` (non-orientable); the only `ε₁₃ = +1` relating maps are Families B
and C; B is already dead on `(ii-twist)`. So the only orientable candidate is
**Family C** — the `UNDECIDED` residue. **This is a re-derivation from the same
certified inputs C125 and C127 already used, not a third independent route**;
the first draft's claim of independence is withdrawn.

**Net: X2 is CLOSED. Ingredient 2 is untouched. X1 and X6 stay BLOCKED, and
X6's object must be re-specified (Y1) before it can be attempted.**

---

## 7. Kill Analysis (Anti-Overfitting Gate)

### What this round KILLS

* **Outcome (A) of its own pre-registration**, on the literal predicate, by an
  obstruction valid for all smooth maps (§2a).
* **Its own first-draft framing**: "genuinely different transformation groups"
  and the "`det`↔winding lock" as billed. Withdrawn, not softened (§2c).
* **The reading in which a LARGE gauge transformation could do what a small one
  cannot.** `𝒢` is `det ≡ +1` by definition; the obstruction is `det` (§3b).
* **C125's non-isometric escape as a citation-dependent closure** — §4 derives
  it, with an exact symbolic proof of the load-bearing step.
* **C127 §5d's mapping torus as an object whose ends are the two frozen
  configurations** (§6a), and `Ω^{Spin}` as its functor (§6b).

### What this round does NOT kill

* **C125's `FALSIFIED`** (strengthened), **C126's `WEAKENED`** (unchanged, and
  more credited than the first draft credited it), **C127's `BLOCKED`**
  (ingredient 2 untouched).
* **Round80's Reading 3 / Lemma L5 tension** and **Round117's** open state —
  untouched, per §5b.
* **Family C / LRSM parity and the `ε₄ε₆` question.** Still `UNDECIDED`.
* **Whether a `t`-selector exists.**
* **The `Pin` reformulation (Y1)** — named, unattempted, not falsified.
* **A future construction that legitimately moves into C126's category** by
  adding an independent `S³` gauge sector (C124's V1).
* `N_gen=3`'s CONDITIONAL status, `lambda = FREE_COUPLING_PARAMETER`,
  `sm_derivation_claimed = False`, `safe_for_runtime = False`, C123's
  `PARTIAL`, C124's `STRUCTURAL_NO_GO`, C119's F1 `FAIL`, C121's `NULL`,
  OB1's `PARKED`.

### Relaxation Map (one assumption changed per variant; none attempted here)

| Variant | Single assumption changed | Kill criterion |
|---|---|---|
| **Y1** | `Ω^{Spin}_4` → `Ω^{Pin^±}_4` on §6b's non-orientable mapping torus | **First check the structure EXISTS** (`w₂`, `w₂+w₁²`); then does the anomaly force the pair? Still gated on ingredient 2 (round95) for the fermion content's `Pin` type. |
| **Y2** | Adopt an `O(3)` structure group instead of C126's `SO(3)` (§2c) | Then `−Ad` is both gauge and geometric and the predicate flips to YES — **without changing any physics**, since `T⁰≠T¹` at fixed `e` either way. Kill criterion: does any physical quantity in this project distinguish the two conventions? If none does, the A/B dichotomy is a convention and should be retired as a question. |
| **Y3** | Grant C124's V1 (independent 13D gauge field) | Then `𝒢` is a genuine gauge group and C127 X6 as originally written becomes legitimate. |
| **Y4** | Drop the bi-invariant / product background | §2b uses the Lie-group structure; §4 uses flatness of both endpoints. Does either survive a squashed `S³`? |
| **Y5** | Literature check on §2b/§4 (unrun, §9) | Are they the classical Cartan-Schouten statements? A positive result would remove this round's last novelty claim, which is the honest default until checked. |

---

## 8. Proposed pearls (NOT written to `pearl_registry/INDEX.md` — outside this round's brief, per C124/C125/C126/C127 precedent)

**Pearl 1 — Pearl Gate. The invariant is `det`, not winding.**
* **observation:** on `S³`, `M_ι = (−I)·g` — the geometric map and the
  Yang-Mills gauge transformation differ by one **central** constant, which
  cancels in `u^{-1}du`. `det M_f` is trivialisation-invariant (it is the
  orientation character); the winding of `M_f` is **not** invariant for
  orientation-reversing maps. So a `t=0`↔`t=1` claim built on winding is built
  on a non-invariant.
* **falsifiable_prediction:** every future claim of the form "a **large** gauge
  transformation relates/dissolves `t=0` vs `t=1`" is wrong with no
  computation — `𝒢` is `det ≡ +1` and the torsion tensor is `SO(3)`-invariant.
  Conversely any transformation that *does* relate them has `det = −1` and
  therefore moves the vielbein or reverses orientation.
* **impact_score:** 5 *(revised down from 6 after both passes showed the
  winding half of the original observation was not invariant — recorded, not
  hidden)*.
* **trigger_condition:** any claim that a gauge transformation relates two
  members of the `∇^t` family.
* **next_check:** 2026-11-01.
* **Scope limit:** uses `dim = 3` twice (`det(−I_n) = −1` needs `n` odd;
  `π_n(SO(n)) = ℤ` at `n = 3`). Do not reuse on another factor without
  checking the dimension. *(Same shape as the correction C125's second pass
  made to that round's own pearl.)*

**Pearl 2 — Caveat Gate** (a specific, buildable alternative named in §6c and
not attempted):
* **observation:** the mapping torus of the map that actually relates the two
  frozen `S³` configurations is non-orientable, so C127's X6 is posed for the
  wrong bordism functor; its honest form is a `Pin^±` question — **whose first
  step is checking the structure exists**, not looking up a group.
* **falsifiable_prediction:** building it either (i) forces the pair (C127's
  pre-registered A2 success mode) or (ii) terminates at round95's missing
  link like every other route — a fourth independent confirmation that round95
  is the single blocker.
* **impact_score:** 5. **trigger_condition:** any attempt on C127 X6/A2, or
  closure of round95. **next_check:** 2026-12-01.

**Pearl 3 — methodological. DEMOTED after skeptic pass 2 (C4).** The first
draft proposed "two quotients by the same group" as a reusable mechanism.
That framing was wrong: at fixed metric it is simply `𝒜 → 𝒜/𝒢`. What survives
is smaller and, stated plainly, still useful:
* **observation:** when a frozen ansatz **gauge-fixes** a symmetry completely
  (here: fixing the vielbein fixes `𝒢` freely), a later round that quotients by
  that same symmetry is answering a question about a *different* configuration
  space, and the two rounds will appear to contradict each other while both are
  correct.
* **falsifiable_prediction:** when two rounds return incompatible equivalence
  verdicts on the same object, ask whether one of them quotiented by a group
  the frozen construction had already gauge-fixed. A counter-example is two
  rounds disagreeing while demonstrably working in the same configuration
  space.
* **impact_score:** 3 *(revised down from 5)*. **trigger_condition:** two
  rounds with incompatible equivalence verdicts. **next_check:** 2026-12-01.
* **Novelty, honestly:** the *existence* of this gap was already recorded by
  C127 §5a and in this project's session memory; C126 Step 6 SCOPE states the
  resolution outright. Only the gauge-fixing phrasing is added.

---

## 9. What this round does NOT show

1. Does **not** resolve OB1 or move it out of `PARKED`.
2. Does **not** supply an F4 mechanism.
3. Does **not** reopen or move C125's, C126's, or C127's verdicts.
4. Does **not** decide Family C, `ε₄ε₆`, round95's link, or round80/Round117's
   open tension.
5. Does **not** compute any bordism group, or check that any `Pin` structure
   exists.
6. Does **not** discover the reconciliation — C126 Step 6 SCOPE states it, and
   this round cites that paragraph (§3).
7. Does **not** claim literature novelty for §2b or §4. **No search was run.**
8. Does **not** establish that winding is the obstruction — it is not (§2c).
9. Does **not** change `N_gen=3`, `lambda`, `sm_derivation_claimed`, or
   `safe_for_runtime`.
10. Does **not** edit `PARENT_ACTION_GATE.md`, `OPEN_BLOCKERS.md`,
    `null_results/`, `CLAIM_LEDGER.yaml`, or `pearl_registry/` — the
    orchestrating session's, per precedent.
11. Does **not** solicit Tom Lawrence's Part 5.

### 9a. Novelty ledger (rewritten after both passes)

| Item | Status |
|---|---|
| §2a Maurer-Cartan obstruction | **New to this round — but supplied by skeptic pass 1**, not by the first draft. Elementary; literature novelty unchecked. |
| §2b closed-form classification of `M_f` | **Partly new.** C125's `B0`-`B2` already **measured** frame transitions and recorded the constant-vs-non-constant dichotomy across the two cosets. The closed form and the exhaustive statement are added. *The first draft's "the object neither C125 nor C126 wrote down" was **false** and is retracted.* |
| §2c `det` invariant / winding not | **New to this project's record — and it CORRECTS this round's own first draft.** Found by skeptic pass 2. |
| §3 the category diagnosis | **Not new.** C126 Step 6 SCOPE states it; C127 §5a restates it. Only the "complete gauge-fixing" phrasing is added. |
| §4 theorem (`Diff`, not `Isom`) + exact symbolic proof | **New**, and the round's principal content. Steps 1-2 are C125 (0c). Literature novelty unchecked. |
| §5 physical attribution | **Not new.** C126's boxed "structure-usage fact", plus one row (`η(D^t)`) and the converse direction. |
| §6b non-orientability of the relating map's mapping torus | **New**, and it re-specifies a live Relaxation Map item. |
| §6d 13D bookkeeping | **Not new, and not independent** — same certified inputs as C125/C127. |
| C9 winding, C6 `Ad^{-1}dAd` | **Not new** — deliberate reproduction; C9 has no measured input. |
| **New *results* bearing on OB1's own question** | **Zero.** |

### 9b. Pre-registration defect, recorded rather than hidden (pass 2, C7)

`claim.md` names C126's soldering admission as *"the seed of the resolution
[which] should NOT be re-derived from scratch"* — **before** its own
Zero-Signal Gate. The estimand was therefore written with the answer already
in hand, which by `estimand-ops.md`'s own anti-pattern table makes this round
**exploratory, not pre-registered**, on the reconciliation question. Its
premise *"neither aware of the other"* is also factually **false**: C126 names
C125 four times. Recorded here permanently, in the same spirit as C126's
record of its own unfalsifiable kill criterion. **The `Diff`-vs-`Isom` theorem
(§4) and §6b were not anticipated by claim.md and are unaffected by this.**

Separately: **the first draft of this file issued a verdict, a `Status` of
"X2 closed", and a `[VERIFIED]` tier while its own §12 read "skeptic pass NOT
YET RUN"** (pass 2, C1). Both passes have now run; the defect is logged.

---

## 10. Verification

**Gate checks: 15 of 15 pass** (`ruff check` clean, `ruff format` applied).

**Injection tests — run this session, since neither skeptic pass had an
execution tool and both asked for them:**

| injection | result |
|---|---|
| Force a **false lock** (`const = True`) in `P2` | `P2_ok = False`, **`14/15`, `ALL_OK = False`** — caught. |
| The **same** injection with only the gate-name fix reverted (`P2_ok → P2_lock_holds`) | **`14/14`, `ALL_OK = True`** — *not* caught. **This is the direct demonstration that finding A1 was real and that the repair works.** |
| Transpose `ad(T_i)` (`EPS[i,k,j]`) | `13/15`, `ALL_OK = False` — caught. |
| Flip the sign in `C1`'s comparison | `14/15`, `ALL_OK = False` — caught. |
| Force both `P2` branches to the same family | Hard failure (empty-sequence exception) — caught, though by crash rather than by gate. |

**Honest accounting of the controls** (finding A5; the first draft claimed
"every check carries a negative control", which is **false**):
* **No negative control:** `C7`, `C9`, `P2`, `P5_etilde_closed_form_err`,
  `P7_nabla1_right_frame_parallel_err`, and both structure-constant errors.
* **Fixed-constant controls, which discriminate a global sign error and
  nothing else:** `bracket_wrong_sign_control` (`1.0`), `C1_control` (`1.42`),
  `C6_control` (`2.00`), `P6_control` (`2.00`), `P7_c_plus_I_residual` (`2√6`).
* **Genuinely discriminating:** `C2`/`C3`/`P8` medians, `P3`'s non-isometric
  falsifier, `P7`'s `c=+I`, `P10`'s two-branch split, `P5`'s non-central
  control, and **`P9`'s λ-sweep**, which has a predicted value at every λ.

**Methodological note, recorded because the same mistake occurred four times
in this one file.** A comparison *statistic* was wrong, not a result, on four
occasions: three negative controls used a `min` over random draws where null
and alternative coincide on a positive-measure set (`Ad(a)` vs `Ad(b)` at
`a=±b`; `Ad(bx)` vs `Ad(xb)` at `[b,x]=0`; `Ad(y)` vs `Ad(y^{-1})` when
`Ad(y)` is symmetric — minima down to `0.0049` against medians `1.42`/`1.40`/
`0.45`), and `P9` first compared against the **supremum** `0.5` instead of the
`x`-dependent `base(x)`, mispredicting by `1.4e−2`. **All four were fixed by
correcting the statistic, never by loosening a threshold.**

| Tier | Claim |
|---|---|
| `[VERIFIED]` — own derivation + finite differences + **both skeptic passes re-derived them by hand independently** | §2b's three closed forms (`2.4e−11` / `1.8e−11` / `2.6e−11`); §4 every step. |
| `[VERIFIED]` — closed-form predicted at 8 values | **P9 Maurer-Cartan**: deviation `4.5e−11`; `λ=−1` → `2.3e−11`; `λ=+1` → `0.9903`. |
| `[VERIFIED]` — **exact, symbolic, second implementation** | `c128_symbolic_lemma.py`: 9/9 entries of `c^Tc+det(c)I` reduce to 0 mod the ideal; control does not reduce; `c=−R_z(θ)` solves (E) symbolically, `c=+R_z(θ)` does not; `c=+I` residual exactly `2√6`. |
| `[VERIFIED]` | `P10` two-branch discrimination; `P5` (`1.4e−16`, median `0.60`, centre `0.0`/`0.0` vs control `0.0978`); `P6` (`6.7e−16` both ways); `P8` (`7.8e−16`, `c` constant `3.8e−11`, `O(3)⁻` 60/60); `P3` falsifier (`0.047`–`0.541`). |
| `[VERIFIED, CONSISTENCY RE-RUN — not a completeness test]` | `P2`: `250/0/0/250`, `\|det\|−1 ≤ 2.2e−11`. Draws from the two closed-form families by construction. |
| `[VERIFIED, RESTATEMENT — not an independent measurement]` | `C8` (`M_ι = (−I)g`, `1.6e−11`) is `C1` with `g := Ad` substituted. Counted once, not twice. |
| `[INFERRED, arithmetic reproduced, no measured input]` | `C9` winding. The integral computes the **`SU(2)` lift's** degree; `\|n\|=1` for `Ad` needs the `[CITED]` `π₃` isomorphism. `so(3)` normalisation would give `−4`. |
| `[INFERRED]` | `det M_f` trivialisation-invariance and the winding shift `[M'_f]=[M_f]+[R]−f^*[R]`; §6a/§6b; the step from §5's table to the attribution. |
| `[CITED]` — standard, not re-derived | `Isom(S³)=O(4)`; `π₃(SO(3))=ℤ`; `Ad` iso on `π₃`; parallel frames of a flat connection on a simply-connected base; mapping torus of an orientation-reversing diffeomorphism is non-orientable; `O(3)≅SO(3)×ℤ₂`. |
| `[CITED]` — project facts | C38; C120; C121; C123; C124; **C125 (0a), (0c), §2a, §3a, §3c, §5, `ε₁₃`**; **C126 (Step 6 SCOPE — the paragraph containing this round's own conclusion —, Step 6b, skeptic E9)**; C127 (§3, §4, §5a/b/d, X1/X2/X6); **round80 §D; Round117 (`null_results/INDEX.md`)**; round95; round99; round111; round113; `PARENT_ACTION_GATE.md` F4. |
| `[MEMORY, unverified, LOW]` — supplied by skeptic pass 2, **not used** | `Ω^{Pin^+}_4 = ℤ/16`, `Ω^{Pin^-}_4 = 0`. Two arXiv searches this session failed to confirm; not adopted. |
| `[UNKNOWN]` | Whether §6b's mapping torus **admits** `Pin^±`; which `Pin` type the frozen content carries; any twisted `Ω^ξ_n(BG)`; whether §2b/§4 are novel (no search run); everything in §7's "does NOT kill" and Y1-Y5. |

### 10a. Answer to C126's skeptic finding E9 (pass 2, C5)

E9 warns that the `T_a = −Z_a/2` bridge composes a rescaling with an
orientation flip and must not be reused in an orientation-sensitive round.
**This round is orientation-sensitive, so the warning applies and was omitted
from the first draft.** Answering it rather than conceding it: every quantity
this round transports is a **determinant** (frame-independent by definition) or
a **relative** sign. Flipping all three `X_i → −X_i` sends
`[X_i,X_j] = +ε → −ε` **and** `[Y_i,Y_j] = −ε → +ε` simultaneously, so
equation (E) is multiplied through by `−1` and `det c = −1` is unchanged;
`det M_f`, `det Ad`, and C125's `ε₃`/`ε₁₃` are all frame-independent.
**The one quantity that is not invariant is the SIGN of `n`** — already flagged
by C126, and not used by this round for anything.

### Check (reproduces this decision)

```bash
cd experiments/20260902-c128-nabla-t-gauge-group-reconciliation
python c128_nabla_t_category_reconciliation.py   # expect 15 / 15, ALL_OK = True
python c128_symbolic_lemma.py                    # expect 9/9 reduce to 0, control False
```

Every `VERDICT_INPUTS` field is now **computed from a gated measurement** — the
first draft's version was hard-coded literals (finding A2).

**Falsifiers, stated so they can fail:**
1. Exhibit a smooth `f` with `M_f = +Ad`. §2a says the Maurer-Cartan residual
   is `λ(1+λ)ε ≠ 0` there; measured `0.9903`.
2. Exhibit `c ≠ 0` solving (E) with `det c > 0`. Symbolically impossible
   (§4); `c=+I` residual `2√6`.
3. Corrupt any headline measurement and confirm the gate fires — **run above,
   and shown to fire now where it did not before**.

---

## 11. Evidence tier of the central conclusion, and what would raise it

**Central conclusion, as it stands after both passes:** *No smooth map has
`M_f = +Ad` (outcome **B** on the literal predicate). The two rounds are not
in contradiction; they differ by whether the soldering form is retained — a
fact C126 itself recorded — and the operative invariant is `det`, i.e. C125's
already-certified `ℤ₂`, not winding. The frozen ansatz uses C125's category.*

* **`[VERIFIED]`** — the literal predicate (§2a), §2b's closed forms, and §4's
  theorem. §4's load-bearing algebraic step is additionally **exact and
  symbolic** (Groebner ideal membership over Q), which is a genuinely second
  implementation, and both skeptic passes re-derived §2b and §4 by hand
  without execution tools and confirmed every step.
* **`[INFERRED]`** — the physical attribution (§5), §2c's winding
  non-invariance, and §6's consequences.
* **`[UNKNOWN]`** — everything in §6 beyond orientability.

**Independent Verification Strength Ladder — where this actually sits.** Two
context-blind same-model skeptic passes are **"same model, isolated context"
(Weak-Medium)**, not more, however thorough they were. The symbolic lemma
raises **one step** of §4 to **"symbolic solver" (Strong)**. To raise the rest:

* **"Independently-written code" (Strong):** a second implementation of §2b
  and §2a not derived from this script — e.g. a quaternionic or fully symbolic
  route. Cheap; the single highest-value next step.
* **"Different model" (Medium):** a cross-model re-derivation. Note this
  project's own recorded caution that numeric agreement is not independence
  unless inputs are withheld.
* **A literature check** (unrun, §9 item 7) would not raise the tier but would
  settle whether §2b/§4 are reproductions — the honest default is that they
  are, and Y5 records it.

**What would NOT raise it:** more random samples. §2b is a closed-form law and
`P2` is a consistency re-run, not evidence of completeness.

---

## 12. FL Step 8a skeptic pass

**RUN — twice, context-blind, differently-worded prompts (Paraphrase-
Sensitivity Probe). Both returned `WEAKENED`; verdicts CONCORDANT. 27
findings; 24 accepted and repaired, 3 answered with reason, 0 waved through.
Full response matrices in §0.** Their principal effects on this file: the
headline framing was withdrawn and replaced (C2, C3); the strongest form of
the answer (§2a) was supplied by a skeptic rather than by the author; the
gate was found unable to fail on its own two headline items and is now
demonstrated to fail on them; one check was a tautology and is rebuilt; and
the novelty ledger was cut to two genuinely new items.
