# C133 — Decision. Which symmetry assumption buys which reduction of the
# S6-channel ↔ S3-`t`-sector pairing-rule space?
#
# ONE-LINE RESULT, class-qualified in the first line per C124/C125 precedent:
# for couplings of ENDOMORPHISM type (one channel leg in, one out) the
# pre-registered three-rung ladder holds exactly as written. Measured on the
# CHANNEL matrix — the 3×3 block acting on `{v,s,c}`, which is the object the
# question is about — the permitted space drops **9 → 3 → 1** as the assumed
# symmetry goes `G2` → `Spin(8)` → `Spin(8)+Z3`. All three rungs are now solved
# directly by the same machinery (`18 / 3 / 1` fibre-inclusive; see §3 for why
# two metrics exist and which is primary).
#
# ⚠️ READ §14 AND `skeptic_verdict.md` BEFORE QUOTING ANYTHING ABOVE IT.
# TWO context-blind FL Step 8a passes were run, differently worded. BOTH
# returned [WEAKENED]. They AGREE, so the single-run Response Matrix applies.
# Between them they found sixteen accepted defects, NONE dismissed; eight
# required re-running the script. Pass 2 found that FOUR of the repairs made in
# response to pass 1 reintroduced the same defect class they were meant to cure
# — checks incapable of failing, presented as evidence. This is the post-repair
# document.
#
# THE ARITHMETIC NEVER MOVED. What moved is what the round may claim for its
# own evidence, and three things a reader must not take from it:
#   * TWO of the three kill criteria — (a) and (c) — are NON-FALSIFIABLE AS
#     WRITTEN. Only (b) is genuinely falsifiable, and it carries the ladder.
#   * The mandatory negative control CANNOT FAIL as constructed (three copies
#     of one rep force dim ≥ 9). A stronger conjugated-basis version was added
#     and passes. Neither licenses "the whole result".
#   * FL Step 4a returns CRITERION_INVALID at rung 1 (threshold = floor), and
#     the ceiling is forced, not measured. Per FL's own third-outcome rule this
#     is NOT evidence against the claim.
# And one substantive correction of a correction: this round's own first attempt
# to fix `claim.md`'s stale credit-line premise OVER-corrected. See §7.

**Date:** 2026-09-02
**Mode:** CONVERGENT (FL Full-Ladder), per `claim.md`'s own mode declaration.
**Question type (EstimandOps L0):** DESCRIPTIVE. Not causal, not predictive.

**Verdict:**
`CONFIRMED_WITH_SCOPE_NARROWED__CHANNEL_MATRIX_LADDER_9_TO_3_TO_1_ALL_THREE_RUNGS_NOW_SOLVED_DIRECTLY_FIBRE_INCLUSIVE_18_TO_3_TO_1_TWO_METRICS_KEPT_DISTINCT__ONLY_KILL_CRITERION_b_IS_FALSIFIABLE_AS_WRITTEN_CRITERIA_a_AND_c_ARE_ENTAILED_BY_THE_CONSTRUCTION_AND_ARE_REPORTED_AS_SUCH__MANDATORY_NEGATIVE_CONTROL_PASSES_BUT_CANNOT_FAIL_STRONGER_CONJUGATED_BASIS_CONTROL_ADDED_AND_ALSO_RETURNS_9__SCOPE_1_SPIN8_ADMITS_A_NONZERO_INVARIANT_TRILINEAR_CHANNEL_MIXING_FORM_SO_NO_CHANNEL_MIXING_HOLDS_ONLY_FOR_ONE_IN_ONE_OUT_COUPLINGS__SCOPE_2_DIM_EQUALS_NUMBER_OF_ORBITS_ON_THE_THREE_CHANNELS_VERIFIED_ACROSS_ALL_SIX_SUBGROUPS_OF_THE_TRIALITY_S3_SO_TRANSITIVITY_NOT_THE_3_CYCLE_IS_THE_OPERATIVE_CONDITION__COST_CORRECTION_RUNG_2_IS_ALSO_A_POSTULATE_NOT_ONLY_RUNG_3__AND_A_CORRECTION_OF_THAT_CORRECTION_RUNGS_2_3_AND_THE_ROUND119_124_ROUTES_DRAW_ON_THE_SAME_UNDERIVED_FIBRE_INGREDIENT_G102_UNSUPERSEDED_PATH_A_NEEDS_INDEPENDENT_FIBER_SPIN8_POSTULATE_AND_USE_IT_IN_OPPOSITE_WAYS__FL_STEP_4A_FLOOR_9_MEASURED_CEILING_1_FORCED_NOT_MEASURED_EFFICIENCY_0_00_THEN_0_75_THEN_1_00_RUNG_1_IS_CRITERION_INVALID_AND_TASK_INFEASIBLE_CANNOT_FIRE__TWO_DIFFERENTLY_WORDED_SKEPTIC_PASSES_BOTH_RETURNED_WEAKENED_AND_AGREE_SIXTEEN_FINDINGS_ACCEPTED_NONE_DISMISSED`

**Status:** OB1 stays PARKED. H1c stays OPEN. `N_gen=3` stays CONDITIONAL.
No gate field is passed; this round supplies no parent action. What it supplies
is a **price list** — which symmetry assumption a future round must pay for, to
buy which reduction — plus two scope narrowings and two corrections to how that
price was previously stated.

---

## 0. Scope, stated before anything else

* Does **not** supply, derive, or verify any parent action.
* Does **not** change `N_gen=3`'s CONDITIONAL status,
  `lambda = FREE_COUPLING_PARAMETER`, or `safe_for_runtime = False`.
* Does **not** close H1c, OB1, or round95's own diagnosed gap.
* Does **not** reopen or re-litigate C123–C132.
* Does **not** solicit Tom Lawrence's Part 5.
* Does **not** edit `PARENT_ACTION_GATE.md`, `OPEN_BLOCKERS.md`,
  `null_results/INDEX.md` or `pearl_registry/INDEX.md` — registry updates are
  the orchestrating session's, per C124–C132 precedent. Pearl and Caveat-Gate
  candidates are *proposed* in §11, not written.

---

## 1. Step −5 — Zero-Signal Gate, resolved BEFORE any computation

| field | filled |
|---|---|
| **Entity** | three named groups — `G2`; `Spin(8)`; `Spin(8)` extended by the explicit order-3 triality element of `pearl_registry` row 33 — acting on the combined channel object `F = E_v ⊕ E_s ⊕ E_c` |
| **Falsifiable predicate** | each rung buys **exactly** the stated reduction: `G2` → no constraint on channel dependence; `Spin(8)` → block-diagonal, independent per-channel coefficients; `+Z3` → equal coefficients |
| **Measurable outcome** | three Schur computations returning the **dimension** of the permitted coupling space |

**GATE: PASS**, with the qualification that §4a establishes only one of the
three rungs to be falsifiable *as tested*. The predicate is a dimension, which
a computation can get wrong; that is enough for the gate. Both skeptic passes
independently narrowed how much this buys, and §4a records the narrowing rather
than the first draft's *"the predicate could have failed at rung 1"*, which is
withdrawn.

---

## 2. What was computed, and what the model actually assumes

`claim.md`'s kill criteria say, three times, *re-verify directly, do not cite*.
Everything below is built inside one self-contained script,
`c133_symmetry_ladder.py`. Verified by pass 1: it imports only
`itertools, json, os, numpy, sympy` — no repository module, matrix or basis.

**What "from scratch" does and does not mean (pass 2 finding 10, accepted).**
The first draft said the *"only inputs are the Cayley–Dickson doubling formula
and the Jordan product"*. That understates the model. The script also fixes the
`J3(O)` coordinate layout and — load-bearingly — the **ansatz** that derivations
act entrywise on the three off-diagonal slots and annihilate the diagonal. That
ansatz is what selects `so(8)` out of `f₄ = so(8) ⊕ 8_v ⊕ 8_s ⊕ 8_c`, and it
presupposes the three-channel block structure the round then measures. The
import check verifies a different and weaker proposition.

| step | what is built | check | measured |
|---|---|---|---|
| 0 | octonions `O` by Cayley–Dickson `R→C→H→O` | unit; `\|uv\|²=\|u\|²\|v\|²`; alternative; NOT associative | ✓; `5.68e−14`; `1.42e−14`; **168** non-associative basis triples |
| 1 | `Der(O)` from `D(uv)=D(u)v+uD(v)`, 512×64 integer system, **exact rational** nullspace | dim; kills the unit; skew | **dim = 14 exactly**; ✓; ✓ |
| 2a | `J3(O)` (27-dim), Jordan product `(XY+YX)/2` | Hermitian; commutative; Jordan identity | `1.78e−15` / `0.0` / `1.14e−13` |
| 2b | the cyclic slot map `σ(X)=PXPᵀ`, `P: 1→2→3→1` | `σ³=id`; Jordan automorphism; slot action | `0.0`; `1.78e−15`; exactly `(x,y,z)→(z,x,y)` |
| 2c | entrywise derivations of `J3(O)` vanishing on the diagonal, **19683 × 192** | dimension + singular-value gap | **dim = 28**; kept `3.464`, dropped `5.73e−15` |
| 2d | that the 28-dim space **is** `so(8)` | projections skew; each spans a **28**-dim matrix space; **closed under brackets** | `8.33e−16`; ranks `[28,28,28]`; closure `3.09e−15` |
| **2e** | the subalgebra where the three blocks coincide (`A₁=A₂=A₃`) | its dimension | **dim = 14**, and it **is** step 1's `Der(O)`: mutual span distances `2.90e−15`, `3.73e−15` |
| 2f | `σ` conjugates the triple cyclically | is the shifted triple still in the algebra? | `2.31e−15` — **but see §4a: this is forced, not contingent** |

**On step 2e's status (pass 2 finding 10, accepted).** The first draft called it
"the falsifiable step" and said the answer *"could have come out as any integer
in `0..28`"*. That overstates the outcome space: `Fix(triality) = g₂` is a
theorem, and this project's own `pearl_registry` row 39 states it flatly
(*"`G2 = Fix(triality)`"*). Step 2e is therefore a **from-scratch reproduction
of a known result** — legitimate and useful, because it can catch a construction
bug, but not an open-outcome measurement.

**This applies to the round as a whole, and is the honest framing of its
evidence.** `14`, `28`, `2`, `168`, `Hom = 0`, `8|_{g2} = 1⊕7`, and the
`1,1,1 / 0,0` trilinear pattern are all standard `Spin(8)`/triality facts. None
was in doubt. The round's value is *not* that any of these numbers was
uncertain; it is (i) that the specific chain from Baez's `S3 ⊂ F4` to the
pairing-rule reduction was verified end-to-end rather than assumed, (ii) the
orbit-counting law (§6b), (iii) the trilinear scope narrowing (§6a), and (iv)
the two pricing corrections (§7).

**Labelling disclaimer.** The construction delivers three pairwise inequivalent
8-dimensional reps of a 28-dimensional algebra isomorphic to `so(8)`, cyclically
permuted by an order-3 automorphism fixing `g2` pointwise. Which is called
`8_v` is Baez's eq. 7 convention [`[CITED]`, arXiv:math/0105155] and is not
load-bearing. Pass 1 noted a *cyclic* slot mis-assignment would be invisible to
every check — true, and harmless for that reason; a *transposition*
mis-assignment would be caught.

---

## 3. The three rungs, computed — and which metric is which

A coupling of **endomorphism type** — one channel leg in, one out, the shape a
fermion-bilinear pairing rule has — lives in `End_G(F) ⊗ W`, with `W` the `S3`
`t`-sector space. Every group on the ladder acts on the `S6` side only, i.e.
**trivially on `W`**, so the whole constraint falls on `End_G(F)`.

**Two metrics, kept apart (pass 1 finding 7).** `End_G(F)` factorises as
*(channel matrix)* × *(fibre endomorphism)*. The question is about the
**channel** index, so the channel metric is primary.

| rung | assumed symmetry | **channel `dim M`** (primary) | fibre-inclusive `dim End_G(F)` | how obtained | shape of `M` |
|---|---|---|---|---|---|
| **1** | `G2` only | **9** | **18** | **direct 576-column solve**, agreeing with the `9 × 2` product | **arbitrary** 3×3 |
| **2** | `Spin(8)` | **3** | **3** | direct solve, and independently `Σ` pairwise `Hom` | `diag(λ₁,λ₂,λ₃)` |
| **3** | `Spin(8)` + `Z3` | **1** | **1** | direct solve | `λ·1` |

**Rung 1 is now solved on the same footing as the others (pass 2 finding 8,
accepted and fixed by computation).** In the first draft `18` was a hard-coded
product `9 * dim Hom_{g2}` and was never put through the `commutant_dim`
machinery that produced `3` and `1` — so the headline rung was the one number
not computed like the others, and §13b's confession list omitted it. Fixed:
`dim_End_g2_of_24dim_F_DIRECT_SOLVE = 18`, agreeing with the product.

**All efficiency arithmetic in §5d uses the channel metric.** Mixing the two is
how a reader could compute `efficiency(rung 1) = (9−18)/8 = −1.125`; that is a
metric error, not a result.

**Base-level caveat (pass 1 finding 7b, pass 2 confirmed the arithmetic).** `18`
is *fibre-level*. For associated bundles over `S⁶ = G2/SU(3)`, `G2`-equivariant
bundle maps correspond to `Hom_{SU(3)}` of the fibres; `8|_{SU(3)} = 1+1+3+3̄`
gives `Hom_{SU(3)} = 6`, so the base-level rung-1 number would be `9 × 6 = 54`.
**The channel metric is unaffected** — a second reason to treat it as primary.
The three rungs are also not fully commensurable as objects: rung 1's `G2` is
the geometry's own symmetry, rungs 2–3's `Spin(8)` is a postulated fibre
symmetry (§7).

### 3a. Rung 1 — `G2` constrains the fibre, not the channel

On `g2` the three blocks carry identical matrices (step 2e), so
`End_{g2}(F) = End_{g2}(O) ⊗ M₃(R)` and the channel matrix is **free**: `9` of
`9`, of which `6` are genuine channel mixing. `dim End_{g2}(O) = 2` is computed
**exactly over the rationals**.

An explicit witness: `Φ` = the identity `O_x → O_y` as one off-diagonal block,
commutator with all 14 diagonal-`g2` generators `0.0`. This is
`pearl_registry` row 34's *"A `Φ` CAN be built at the `G2`-only level"*
re-derived — **but see §4a: given step 2e this commutator is an identity.**

**This confirms C132's own correction, not C132's first draft:** `G2` acts
trivially on the channel label, so it constrains nothing about dependence on it.
`G2`-equivariance does cut the *fibre* factor from 64 dimensions to 2.

### 3b. Rung 2 — the one genuinely falsifiable rung

**Corrected statement of the numerical evidence (pass 1 finding 1).** The first
draft said the largest discarded singular value was *"exactly `0.0` — a
structural zero"*. That was a **sentinel return value** meaning *nothing was
discarded*. The helper now returns `null`, and the correct — stronger —
statement is:

> For all six off-diagonal pairs the intertwiner system has **full column rank,
> 64 of 64**, smallest **retained** singular value `1.0801`, against an actual
> tolerance of `6.29e−10`. The retained value exceeds the tolerance by about
> **nine** orders of magnitude.

*(Pass 2 finding 6a: the first repair quoted `~6.5e−13` — the factor-`1` value,
not the factor-`1e3` default actually used — and claimed "twelve orders". Both
corrected here and in the code; the JSON now prints the tolerance per probe.)*

**Tolerance sensitivity, measured, and now covering the headline solves.**
Seven factors spanning twelve orders:

| probe | dims across all seven factors |
|---|---|
| `Hom(ρ₂→ρ₁)` (expect 0) | `0,0,0,0,0,0,0` |
| `Hom_{g2}` (expect 2) | `2,…,2` |
| entrywise derivations (expect 28) | `28,…,28` |
| **commutant `so(8)` — rung 2** (expect 3) | `3,…,3` |
| **commutant `so(8)+U` — rung 3** (expect 1) | `1,…,1` |
| **commutant `g2` — rung 1** (expect 18) | `18,…,18` |
| `End(ρ₁)` (expect 1) | `0,1,1,1,1,1,1` — **moves at one extreme** |

**Two corrections here (pass 2 finding 6b, 6c).** The first repair swept only
four small systems and *not* the three 576-column solves that produce the
headline — now added, all stable. And it reported "every verdict-bearing
dimension is stable" via a **hard-coded exclusion list** that dropped the one
mover — but `End(ρ₁) = 1` **is** verdict-bearing (it gives rung 2 by the
pairwise route and is the sole basis for the absolute-irreducibility claim).
The exclusion list is removed. Honest statement: **every probe including the
mover is stable from factor `1e−1` upward**; `End(ρ₁)` drops to 0 only at factor
`1e−3`, where its tolerance (`6.50e−16`) falls *below* the `6.70e−16`
floating-point noise floor of the true zero singular value — a degenerate
tolerance at which no numerical zero could be detected at all.

**The inequivalence certificate — sound, but it has no failable control
(pass 2 finding 5, accepted).** The certificate compares basis-independent power
traces `tr(ρ_a(X)^k)`, `k = 2,4,6,8`:

| quantity | measured |
|---|---|
| **smallest** relative separation between two **different** reps (20 random algebra elements) | **`0.0228`** |
| deviation for an orthogonally conjugated copy of `ρ₁` | **`3.88e−15`** |

The logic is sound in the direction used: equivalent reps *must* agree on power
traces, so a nonzero separation proves inequivalence. **But the `3.88e−15` is
not a control that could fail** — trace of a power is a similarity invariant, so
comparing it against a conjugated copy is an algebraic identity, and the number
measures numpy roundoff. It is an implementation smoke test and a **scale
calibration** (it shows `0.0228` is not what the statistic returns for
equivalent pairs), not a falsifiable control. The first repair advertised it as
*"the control can fail"*; that is withdrawn. **This certificate is
theorem-based and needs no control** — which is the honest thing to say, rather
than manufacturing one.

*(This replaced a worse first version — pass 1 finding 2 — whose control was
literally `spec[0] − spec[0]` and whose sorted-eigenvalue statistic was unsound
for real skew matrices. The old headline `3.033` is withdrawn.)*

`dim End_R(block) = 1` for each block ⇒ **absolute irreducibility** ⇒ every
dimension holds over `C`.

**Kill criterion (b) did not fire, and could have** — this is the one criterion
of which that is true.

### 3c. Rung 3 — the explicit `Z3`, re-derived from Baez

* Baez, `[CITED]`: *"there are other automorphisms coming from the permutation
  group on 3 letters, which acts on `(x,y,z)` in an obvious way"*
  (arXiv:math/0105155, on `J3(O)`).
* Implemented as `σ(X) = P X Pᵀ`, `P` the 3-cycle permutation matrix. **Reason
  corrected (pass 2 finding 10):** the first draft said it is an automorphism
  *"because `P` has real entries"*. That is insufficient as written — it fails
  for `P = 2I`. The correct reason is that `P` is **orthogonal** (`PᵀP = I`),
  which permutation matrices are; then `(PXPᵀ)(PYPᵀ) = P(XY)Pᵀ` and Hermiticity
  is preserved, with no octonion identity needed. The conclusion stands.
* `σ³ = id` (`0.0`); slot action exactly `(x,y,z) → (z,x,y)` with no
  conjugations (`0.0`); commutes with the diagonal `g2` (`0.0`); normalises the
  `so(8)` image (`2.32e−15`). **All four are entailed by the construction — see
  §4a.**
* Since it permutes three *inequivalent* summands it is **outer**, i.e.
  triality. `[INFERRED]`: `ρ₁ ∘ φ = ρ₃` exactly, so `φ = Ad(g)` would force
  `ρ₃ ≅ ρ₁`, contradicting the computed `Hom = 0`; order 3 + outer ⇒ a 3-cycle
  in `Out(D₄) ≅ S₃`. Nothing computed establishes outerness *directly*, and
  this is the step where rung 3 genuinely depends on rung 2.

With `M = diag(λ₁,λ₂,λ₃)`, `U M U⁻¹ = diag(λ₃,λ₁,λ₂)`, so `[M,U]=0 ⟺
λ₁=λ₂=λ₃`. The direct 24×24 solve returns **1**.

---

## 4. Kill criteria — all three evaluated, and only one is falsifiable

| # | fires if | measured | verdict |
|---|---|---|---|
| **(a)** | a `G2`-equivariant channel-mixing map does **not** exist | `dim Hom_{g2} = 2 > 0` (exact); `Φ ≠ 0`, commutator `0.0` | **DID NOT FIRE — and COULD NOT, as written (§4a)** |
| **(b)** | `Hom_{Spin(8)}(8_v, 8_s) ≠ 0` | `= 0`, six times, full column rank 64/64, stable over 12 orders of tolerance; independently certified by a power-trace separation of `0.0228` | **DID NOT FIRE, and could have** |
| **(c)** | the row-33 triality element does **not** conjugate the three blocks into one another | `σ` normalises the algebra, `2.32e−15` | **DID NOT FIRE — and COULD NOT, as written (§4a)** |

### 4a. Criteria (a) AND (c) are non-falsifiable as written — accepted, not argued away

**(a), from pass 1 finding 3.** The script sets the `G2` action on `F` to three
*identical* blocks, so `Φ`'s equivariance is automatic. Re-verified by reading
the code: correct.

**(c), from pass 2 finding 2 — and the first repair confessed (a) while leaving
(c) advertised five times as *"did not fire and could have"*.** Re-derived
independently this session: conjugating a derivation by a Jordan automorphism
yields a derivation; `σ` permutes the three off-diagonal slots and preserves the
diagonal, so it preserves the shape of the entrywise/diagonal-annihilating
ansatz. **Therefore `σ L σ⁻¹ = L` necessarily**, and `2.32e−15` is roundoff on a
theorem. The `0.919` graded-control failure does **not** rescue this: that case
fails precisely because `(ρ₁,ρ₁,ρ₂)` is not a cyclically symmetric arrangement,
so it shows a *different* object fails, not that the covariant one could have.
**A partial confession is worse than none** — it buys credibility for what was
not confessed — and this document made exactly that mistake in its first repair.

**Where the contingent content actually is.** Both (a) and (c) reduce to facts
that are theorems (`Fix(triality) = g₂`; automorphism-conjugation preserves the
derivation algebra). **The ladder's entire contingent content is criterion (b) —
inequivalence — plus orbit counting (§6b).** That is a smaller claim than three
independent kill criteria, and it is the accurate one.

**Supporting evidence that rung 1 discriminates against nearby groups** (real,
but not a restoration of falsifiability): adding **one** generator from outside
the diagonal `g2` collapses the permitted space `18 → 3` and breaks `Φ`
outright (commutator `0.347`).

---

## 5. MANDATORY negative control — passes, and cannot fail

| triple | pairwise `Hom` | `dim End_{so(8)}(F)` | block-diagonality forced? |
|---|---|---|---|
| `(ρ₁, ρ₂, ρ₃)` — the real case | `1` diagonal, `0` off | **3** | **yes** |
| `(ρ₁, ρ₁, ρ₁)` — **the control** | `1` in all nine entries | **9** | **NO — mixing permitted** |
| **`(ρ₁, Q₂ρ₁Q₂ᵀ, Q₃ρ₁Q₃ᵀ)` — STRONGER control, added after pass 2** | — | **9** | **NO** |
| `(ρ₁, ρ₁, ρ₂)` — graded control | `1,1,0 / 1,1,0 / 0,0,1` | **5** | no |

**The control passes — and could not have failed (pass 2 finding 3, accepted).**
Three literal copies of one array force `commutant ⊇ M₃ ⊗ End(ρ₁)`, hence
`dim ≥ 9`, before any computation. `NEGATIVE_CONTROL_PASSES = (dim > 3)` is
therefore forced true, and can fail only through a coding bug in the solver.
That *is* what `claim.md` asked it to detect — a machinery that manufactures
block-diagonality — so the control does its stated job. **It does not license
"the whole result", and §15 no longer treats it as a ground that "could have
failed".**

**Stronger control added, because the script already had the ingredients.**
Pass 2 pointed out that conjugated copies were being built elsewhere and never
fed to the control. Three copies of `ρ₁` in three *different bases* (blocks
differ by `0.313`, not identical) still return **9** — so the solver is doing
representation theory, not exploiting array identity. Still forced, but a
strictly better test of the implementation.

**What the control does NOT cover.** It varies only the representation triple
fed to the Schur solver, so it supplies **zero** evidence about the two upstream
steps that could actually be wrong: the extraction of the triples from `J3(O)`,
and `U24`'s correspondence to `σ`. *(The first draft said the latter was
"covered by the `0.919` failure demonstration". Pass 2 correctly called that a
non sequitur — a demonstration that the normalisation test can return `O(1)` is
not evidence that `U24` corresponds to `σ`. The actual evidence exists in the
JSON — `U24` equals `slot_perm([1,2,0])[3:27,3:27]`, which pass 2 verified index
by index — and was never invoked. It is invoked now.)*

**A second thing the control shows.** Applying `U` to the equivalent triple
gives **3**, not 1: with equivalent blocks the `Z3` forces only *circulant*
structure, which still mixes channels. The rung-3 collapse is a joint
consequence of inequivalence **and** transitivity.

**Honest flag on the graded control.** `U` normalises the algebra image in the
real case (`2.32e−15`) and the equivalent control (`6.69e−16`) but **not** in
`(ρ₁,ρ₁,ρ₂)` (residual `0.919`), so that case's "+`U`" number is an arbitrary
extra linear condition, not a symmetry statement.

### 5c. A third control, on the input side

`G44`'s `8|_{G2} = 7 ⊕ 1` was recovered rather than cited: the `g2` commutant on
`R⁸` is 2-dimensional and a generic element has eigenvalue multiplicities
`{1, 7}`. Matches `G44` and `G102`'s `Hom_{g2} = 2`.

### 5d. FL Step 4a — Floor–Ceiling Interval

Metric: `dim M`, the **channel matrix**, *lower = more reduction*.

| end | construction | value | status |
|---|---|---|---|
| **FLOOR** | mechanism (inequivalence) removed — §5's mandatory control | **9** | **measured** |
| **CEILING** | minimum attainable over all six subgroups of the triality `S3` | **1** | **FORCED, not measured** — see below |

```
efficiency = (floor − observed) / (floor − ceiling),  floor = 9, ceiling = 1

  rung 1  G2       observed 9  ->  efficiency  0.00
  rung 2  Spin(8)  observed 3  ->  efficiency  0.75
  rung 3  +Z3      observed 1  ->  efficiency  1.00
```

**The ceiling repair was cosmetic, and that is now stated (pass 2 finding 4,
accepted).** The first draft asserted `ceiling = 1` by definition; the first
repair "measured" it by sweeping all six subgroups and claimed this converted
`TASK_INFEASIBLE` from a dead check into a live one. It did not: every
commutant contains `ℝ·I`, so every sweep entry is `≥ 1`, and the sweep includes
`Z3`, whose value **is** the rung-3 headline. So `1 ≤ ceiling ≤ 1` is fixed
before the sweep runs, and `TASK_INFEASIBLE` (which needs `ceiling < 1`) remains
**structurally unable to fire**. The claim that it became a real check is
withdrawn. **What the sweep genuinely bought is the orbit-counting law (§6b)** —
a real result, obtained from a check that was not.

**The three stop conditions:**

* **`CRITERION_INVALID`: FIRES AT RUNG 1** (pass 1 finding 3). Rung 1's observed
  value `9` **equals the floor**, because rung 1's predicate ("no constraint")
  *is* the mechanism-free answer. Per FL's own rule, threshold ≤ floor ⇒
  `CRITERION_INVALID`. **Rungs 2 and 3 are unaffected** — the null model gives
  `9` and `3` against thresholds `3` and `1`. Per FL's third-outcome discipline
  **this is not evidence against the claim**; it means rung 1 carries no
  discriminating information, which is itself rung 1's finding, stated as
  `efficiency = 0.00`.
* **`TASK_INFEASIBLE`: cannot fire**, as above. Reported as a check that does
  not exist for this metric rather than one that passed.
* **`NO_HEADROOM`: no.** Floor `9` vs ceiling `1`, observed at three distinct
  interior points.

**Floor/ceiling not swapped:** with *lower = better*, the mechanism-removed
construction gives the **larger** number, so `9` is the floor.

---

## 6. Two scope narrowings this round found — neither inherited from C132

### 6a. `Spin(8)` does NOT forbid channel mixing in general

| invariant trilinear form | `dim Hom_{so(8)}` |
|---|---|
| `ρ₂ ⊗ ρ₃ → ρ₁` / `ρ₃ ⊗ ρ₁ → ρ₂` / `ρ₁ ⊗ ρ₂ → ρ₃` | **1** each |
| *controls* `ρ₁ ⊗ ρ₁ → ρ₁`, `ρ₁ ⊗ ρ₂ → ρ₁` | 0, 0 |

A nonzero `Spin(8)`-invariant trilinear form couples all three channels —
octonion multiplication itself. Pass 1 checked the hand-indexing term by term
and confirmed it; both passes independently confirmed the pattern is what
`so(8)` forces (`8_s⊗8_c ⊃ 8_v`, while `8_v⊗8_v = 1+28+35_v` and
`8_v⊗8_s = 8_c+56_c` contain no `8_v`).

**What this does and does not do.** It does **not** fire criterion (b), which is
about an endomorphism — one leg in, one out — still exactly `0`. It **does**
mean "no channel mixing" must carry its class: *among couplings with one channel
leg in and one out*. A pairing rule between a channel label and a `t`-sector is
bilinear in the channel-carrying fields, so the endomorphism class is the right
one here — but the unqualified phrase would be false if reused elsewhere.

### 6b. Transitivity, not the 3-cycle — and this is a law, not two data points

The subgroup sweep gives an exact law, **verified across all six subgroups of
the triality `S3`** (`law_holds = true`):

```
dim M  =  number of ORBITS of the assumed subgroup on {v, s, c}
```

| subgroup | `dim M` | orbits |
|---|---|---|
| trivial `{e}` | 3 | 3 |
| `Z2` `(01)` / `(02)` / `(12)` | 2 each | 2 each |
| `Z3` `(012)` | **1** | 1 |
| `S3` | **1** | 1 |

Hence `dim M = 1 ⟺ the subgroup acts transitively`. `Z3` is the *minimal*
transitive subgroup; `S3` also works, which settles Relaxation Map V3 by
measurement. "Only invariance under the triality `Z3`" is correct **as a
statement about the three rungs tested**, not as a uniqueness claim about `Z3`.

*(Computed: the 3-cycle permutes slots with no conjugations, while the
transposition acts as `(x,y,z) → (ȳ, x̄, z̄)`.)*

---

## 7. The credit line — a correction, and then a correction of the correction

This is the round's most consequential non-arithmetic section and it was wrong
twice before settling. Both errors are recorded.

**What stands: C132 under-priced rung 2.** C132's `P0` says *"New ingredient
required. For the `G₂` and `Spin(8)` rungs: none. For the `Z₃` rung: a
triality-symmetric parent action"* (verbatim, C132 `decision.md:236-237`,
confirmed by both passes). The frozen background is `S⁶ = G2/SU(3)`, whose
relevant automorphism group is `G2`; **there is no `Spin(8)` acting on it.**

| rung | what it costs |
|---|---|
| **1 — `G2`** | **free** — the background's own symmetry, and it buys nothing about the channel label (`efficiency 0.00`) |
| **2 — `Spin(8)`** | **a postulate** the geometry does not supply |
| **3 — `+Z3`** | **the same postulate, plus two more:** that it be extended by triality, **and** that the three channels be one combined object rather than three separate bundles — which `pearl_registry` row 34 says the current construction does **not** provide |

**Error 1 (`claim.md`'s premise, and this round was required to assert it).**
`claim.md` demanded the round *"state plainly that it draws on the same
un-derived fibre-`Spin(8)`/triality credit line that `N_gen=3` itself already
rests on (G102)"*. But `pearl_registry` row 7 is marked verbatim
**`SUPERSEDED-IN-PLACE 2026-08-10 — DO NOT ASK THIS QUESTION AS WRITTEN`**, and
its superseding text says channel distinguishability is now CLOSED by two routes
(round119 `SO(4)×SO(4)`, round124 `su(3)+u(1)+u(1)`), with the live question
narrowed to *"does that rank-4 structure act GLOBALLY on the compactification"*.
So the pre-registration cited a row's superseded framing as a required
deliverable.

**Error 2 — this round's own first correction OVER-corrected (pass 2 finding 7,
the single most consequential finding of either pass).** The first repair
concluded that rungs 2–3 and the round119/124 routes are *"two different and
oppositely-directed un-derived assumptions, not one shared credit line."* That
is wrong, for two reasons pass 2 caught and this session re-verified against the
primary files:

1. **The first repair quoted `null_results` G102 one clause too early.** It
   quoted *"`c_so8(g2)=0`: no continuous fiber symmetry beyond geometric `G2`
   exists"* and stopped. The same row — **not** marked superseded — continues:
   *"…Path A needs independent fiber-Spin(8) **POSTULATE**; G67-C3 third channel
   = model-building input."* That omitted clause is precisely the
   shared-ingredient content the repair was withdrawing. [Re-verified by reading
   `null_results/INDEX.md` line 35 in full.]
2. **The "opposite direction" route lives inside the postulated group.**
   `pearl_registry` row 40 (round119) describes its own construction: *"split
   `O=R^8` into two 4-dim blocks, **full SO(4)xSO(4)** (NOT restricted to
   octonion automorphisms) … rank 4 = rank(SO(8)), cannot embed in SO(7)."*
   `SO(4)×SO(4) ⊂ SO(8)` — a postulated fibre `Spin(8)` **supplies** it.
   Enlarge-then-break is one coherent chain. C132's own taxonomy files them
   together (`decision.md:201-202`: *"an independent structure outside the `S⁶`
   frame bundle — G102's fiber-`Spin(8)` postulate, C124's V1 gauge field"*).

**The accurate statement, which is neither the pre-registration's nor the first
repair's:**

> Rungs 2–3 and the round119/124 routes **draw on the same un-derived
> ingredient** — structure acting on the fibre beyond the geometric `G2`, which
> `G102` says the geometry does not supply — and **use it in opposite ways**:
> rungs 2–3 keep the enlarged symmetry unbroken to force channel-uniformity;
> round119/124 break it to distinguish the channels. The shared *ingredient* is
> real; the shared *credit line* framing of `pearl_registry` row 7 is
> superseded as to what `N_gen=3` now depends on (the **global** action of that
> structure, per the 2026-08-10 note), which is a narrower and still-open
> question.

**A directly relevant open item this round did NOT close.** `pearl_registry`
row 40's own `next_check` reads: *"verify whether the known triality `Z3`
(already built this session via octonion/g2 tools) cyclically permutes the
`(Γ_A, Γ_B)` sign patterns of `v,s,c` in a consistent single-symmetry way."*
This round built that `Z3` and verified it cyclically permutes the three
channels — but **in the octonion/`J3(O)` basis, not against row 40's
`(Γ_A, Γ_B)` sign structure**. The two are adjacent and this round does **not**
close row 40. Named in §11 as the sharpest available next step.

---

## 8. The four things this round was pre-registered NOT to claim

Both passes checked these adversarially and independently, pass 2 under an
explicit instruction to be uncharitable. **Neither found any re-committed, in
direct or reworded form.**

### 8a. The anomaly step does not discriminate

`round95` §3: with `A(4,2,1)=+2`, `A(4̄,1,2)=−2` and `E17`'s exhaustive
`{(1,2),(2,1)}` content, `n_L = n_R`; with `n_L + n_R = N_gen`, the one-sector
options give `{0, N_gen}` and fail for **every** `N_gen ≥ 1`. It is a
**consistency filter**, not a differentiator, and its survivor is the assumed
Pati-Salam content. **Nothing in §§3–6 uses it.**

**Evidence tier:** round95's own assumptions section marks round90's
coefficients *"reused from … **Wikipedia** quote and **`[WEAK]`**-sourced
modern-paper cluster; not independently re-verified"*. Tagged **`[WEAK]`**,
**not `[DOCS]`**.

### 8b. No "3 → 2 up to `t↔1−t` relabelling" reduction

**Not claimed.** C125's verdict is the opposite (*"`t=0` vs `t=1` remains a
genuine physical choice"*) and its Family C question is **`UNDECIDED`**, gated
on round95.

### 8c. The `Z3` rung is not free and not derived

**Not claimed free.** §7 prices it and rung 2. Its physical realization is
`pearl_registry` row 33's still-open conditions 2–5.

### 8d. Round90's coefficients are not tagged `[DOCS]`

**Not claimed.** `[WEAK]` in §8a and §13c.

---

## 9. What the reduction actually is, stated precisely

At rung 3 the coupling is `Φ = 1_F ⊗ (λ₀ w₀ + λ₁ w₁)`, with `w₀, w₁` spanning
the two `S³` `t`-sectors [`[CITED]`, C38].

**Factor collision fixed (pass 2 finding 9).** The full coupling space is
*(channel) × (fibre) × (sector)*. A previous draft wrote rung 1 as "18 real
parameters" in a *channel × sector* column — colliding with §3's `18 = 9 channel
× 2 fibre`, which is a different product that coincides only because both
secondary factors equal 2. All three factors are now named:

| rung | channel | fibre | sector | total parameters | nonzero support patterns on `{t=0, t=1}` |
|---|---|---|---|---|---|
| 1 (`G2`) | 9 | 2 | 2 | **36** | no reduction — the channel matrix is continuous |
| 2 (`Spin(8)`) | 3 | 1 | 2 | **6** | 63 (`2⁶−1`) |
| 3 (`+Z3`) | 1 | 1 | 2 | **2** | **3** — `all→t=0`, `all→t=1`, `all→both` |

**So "the pairing-rule space is exactly `{all→t=0, all→t=1, all→both}`" is
precise only as: the set of nonzero SUPPORT PATTERNS of a channel-uniform
coupling has exactly three elements.** The coupling space is a 2-parameter
continuum; a Schur computation yields a dimension, not a finite set, unless a
support convention is imposed on top — and one is.

**Two caveats on `W` itself.** (i) This treats `W` as a bare 2-dimensional
space; C38 gives the sectors as `(1,2)` and `(2,1)`, *inequivalent*
`SU(2)_L × SU(2)_R` reps, and no rung considers an `S³`-side symmetry acting on
`W` (Relaxation Map V5 covers only an `S⁶`-side one). (ii) **Restored after
pass 2 finding 10:** round95's own assumptions section says the `t=1` entry
*"holds only under `c0=−2` (`CONVENTION_TABLE.md` row 5), **carried forward
unresolved**"* — a caveat present in a file this round read and dropped in
citation. Harmless for `9/3/1` (`W` is 2-dimensional either way), but it is
carried now.

---

## 10. Kill Analysis (Anti-Overfitting Gate)

### What this round KILLS

* **Nothing about the world.** No mechanism, no parent action, no prior round's
  claim is falsified.
* **One piece of C132's cost accounting** — `P0`'s "no new ingredient" for rung
  2 (§7).
* **Its own first draft's evidentiary framing**, in six places, all retracted
  above rather than quietly amended: the sentinel "structural zero" (§3b); the
  sorted-eigenvalue certificate and its `x−x` control (§3b); "criterion (a)
  could have fired" (§4a); "criterion (c) could have fired" (§4a); "the negative
  control could have failed" (§5); "the ceiling is measured / `TASK_INFEASIBLE`
  is now a real check" (§5d).
* **Its own first correction of `claim.md`'s credit-line premise** (§7,
  Error 2) — an over-correction, itself corrected.
* **Two unqualified phrasings**, if reused outside this class: "`Spin(8)`
  forbids channel mixing" (§6a) and "only the `Z3` forces equal coefficients"
  (§6b).

### What this round does NOT kill

* Any of the three rungs. All survive as pre-registered, within the
  endomorphism class.
* `pearl_registry` rows 33, 34, 37, 39, 40; `null_results` `G44`, `G102`;
  C125's verdict; round95's `TENSION_DISSOLVES`.
* `pearl_registry` row 40's own `next_check` — adjacent, explicitly **not**
  closed (§7).
* The physical realizability question (row 33's conditions 2–5).
* Whether a `t`-selector exists — OB1's own question.

### Relaxation Map (one assumption changed per variant; none attempted here)

| Variant | Single assumption changed | Kill criterion |
|---|---|---|
| **V1** | Allow a **trilinear** channel coupling | §6a: the invariant trilinear form exists and is unique up to scale. Does a pairing rule ever take that shape? If it needs three channel legs it is a generation-mixing operator, not a pairing rule. |
| **V2** | Do the analysis at **base** level over `S⁶ = G2/SU(3)` | `Hom_{SU(3)} = 6` gives rung 1 as `54`, not `18`. The **channel** metric is unaffected. Does the `SU(3)`-level commutant change any *channel* conclusion? |
| **V3** | Assume `S₃` instead of `Z₃` | **Settled by measurement** (§6b): still 1. Recorded so it is not re-run. |
| **V4** | Check the `Z3` against round119's `(Γ_A, Γ_B)` sign structure instead of the octonion basis | **`pearl_registry` row 40's own named `next_check`.** This round built the `Z3` but in the other basis. Kill criterion: does a single `Z3` cyclically permute row 40's three sign patterns consistently — or is that basis, in row 40's own words, *"a convenient basis with no real symmetry manifest"*? **Sharpest available next step, and cheaper than it was before this round.** |
| **V5** | Let `W` carry a non-trivial action of the assumed symmetry | Every rung uses "acts trivially on `W`". If a parent symmetry acted on both factors jointly the constraint would not factorise and none of `9/3/1` survives. |

---

## 11. Pearl / Caveat-Gate candidates (PROPOSED, not written to the registry)

| gate | observation | falsifiable prediction | impact | trigger | next_check |
|---|---|---|---|---|---|
| Pearl | **`dim M = number of orbits`** of the assumed channel symmetry on `{v,s,c}`, given inequivalence — verified across all six subgroups of the triality `S3` | Any assumed channel symmetry's reduction is predictable by counting orbits, with no Schur computation; and any argument "assume triality ⟹ channel-uniform" that does not *also* invoke inequivalence is incomplete (three **equivalent** blocks plus the same `Z3` give 3, not 1) | 6 | any round assuming a triality-symmetric parent action | at the next H1c / round95 / OB1 pairing proposal |
| Pearl | `Spin(8)` forbids channel mixing **only** for one-in-one-out couplings; the invariant **trilinear** form mixes all three (`dim Hom = 1`, two zero controls) | Any "the symmetry forbids channel mixing" claim must name the tensor type of the coupling | 6 | any round invoking a representation-theoretic no-mixing argument | before any `P0`-style symmetry-ladder reuse |
| Pearl (**method**) | **Repairs made in response to a skeptic pass reintroduced the same defect class they were curing — four times in one round.** A sentinel `0.0` was replaced by a control that was an algebraic identity; a definitional ceiling was replaced by a swept ceiling that was still forced; a confessed non-falsifiable criterion (a) sat next to an unconfessed one (c) advertised five times as falsifiable | A second, differently-worded pass over the **repaired** document finds defects *in the repairs* at a rate comparable to the first pass over the original; predicted that ≥1 repair-introduced defect appears whenever ≥4 repairs are made in one cycle. **A partial confession is worse than none — it buys credibility for what was not confessed.** Cheap test: after any repair cycle, re-ask "can this new check fail?" of each new check | 7 | any round making ≥3 repairs in response to a review | at the next FL Step 8a repair cycle |
| **Caveat Gate** | `pearl_registry` row 40's own `next_check` — verify the triality `Z3` against round119's `(Γ_A, Γ_B)` sign structure — is **adjacent to but not closed by** this round, which built the same `Z3` in the octonion/`J3(O)` basis | If a single `Z3` does not cyclically permute row 40's three sign patterns consistently, then in row 40's own words that construction is *"a convenient basis with no real symmetry manifest"* — and the two independent channel-distinguishing routes lose their triality interpretation | 7 | any round pursuing round119/round124's rank-4 structure | at the next OB1 F4 attempt, or 2026-11-01 |
| **Caveat Gate** | A `claim.md` pre-registered as a **required deliverable** a premise its own registry had marked `SUPERSEDED-IN-PLACE — DO NOT ASK THIS QUESTION AS WRITTEN` 23 days earlier; and the round's first attempt to correct it **over-corrected**, by quoting an un-superseded row one clause short of the clause that contradicted the correction | A pre-registration citing a registry row must quote that row's **current** status line; and a correction to a registry-based premise must quote the **whole** row, not the part that supports the correction. Sibling to C132's own "superseded table inside a still-cited `decision.md`" pearl — same failure, one document type upstream, plus a new failure mode (partial quotation in the corrective direction) | 6 | any `claim.md` citing a registry row, or any round correcting one | at the next pre-registration citing a registry row |

---

## 12. What this round does NOT show

1. Does **not** supply, derive, or verify any parent action.
2. Does **not** show any of the three symmetry assumptions is physically
   realized. Rungs 2–3 are postulates priced, not granted (§7).
3. Does **not** show the triality `U` acts on physical zero-mode wavefunctions
   or commutes with the actual Dirac operator (row 33, conditions 2–5).
4. Does **not** close `pearl_registry` row 40's `next_check` — same `Z3`,
   different basis (§7, V4).
5. Does **not** claim the anomaly step discriminates (§8a), nor upgrade
   round90's `[WEAK]` coefficients.
6. Does **not** claim a "3 → 2 up to relabelling" reduction (§8b).
7. Does **not** establish the pairing-rule space is a *finite set* (§9).
8. Does **not** cover couplings outside the endomorphism class (§6a).
9. Does **not** re-derive anything at **base**-space level (§3, V2).
10. Does **not** provide a falsifiable test of kill criteria (a) or (c) as
    written (§4a), nor a negative control or ceiling that could fail (§5, §5d).
11. Does **not** establish that rungs 2–3's postulate is the *same credit line*
    `N_gen=3` rests on — nor that it is a *different* one; the accurate
    statement is a shared ingredient used in opposite ways (§7).
12. Does **not** change `N_gen=3`'s CONDITIONAL status,
    `lambda = FREE_COUPLING_PARAMETER`, or `safe_for_runtime = False`.
13. Does **not** close H1c or OB1, and does not re-litigate C123–C132.
14. Does **not** solicit Tom Lawrence's Part 5.

---

## 13. Verification

**Script:** `c133_symmetry_ladder.py` · **Output:** `results_c133.json`
**Skeptic record:** `skeptic_verdict.md` (both passes, both prompts)
**Lint:** `python -m ruff check experiments/20260902-c133-symmetry-ladder-pairing-space/` — clean.
**Determinism:** seeded (`default_rng(20260902)`).

### 13a. Falsifiable residuals — checks that could have come out otherwise

| tag | claim | evidence |
|---|---|---|
| `[VERIFIED-tool]` | `O` is a composition algebra, alternative, non-associative | `5.68e−14` / `1.42e−14` / 168 triples |
| `[VERIFIED-tool, EXACT]` | `dim Der(O) = 14`; kills the unit; skew | exact rational nullspace, no floating point |
| `[VERIFIED-tool]` | `J3(O)` is a commutative Jordan algebra | `1.78e−15` / `0.0` / `1.14e−13` |
| `[VERIFIED-tool]` | the 28-dim space is a Lie algebra with all projections onto `so(8)` | nullity 28 (kept `3.464`, dropped `5.73e−15`); skew `8.33e−16`; ranks `[28,28,28]`; **bracket closure `3.09e−15`** |
| `[VERIFIED-tool]` | the diagonal locus is 14-dim and **is** `Der(O)` | span distances `2.90e−15`, `3.73e−15` *(a reproduction of `Fix(triality)=g₂`, not an open-outcome measurement — §2)* |
| `[VERIFIED-tool, EXACT + numeric]` | rung 1: `dim M = 9`, fibre factor 2, **direct solve `18`** agreeing with the product | exact rational `2`; direct 576-column solve |
| `[VERIFIED-tool]` | rung 2: `dim M = 3`; all six off-diagonal `Hom` vanish | **full column rank 64/64**, smallest retained `1.0801` vs tolerance `6.29e−10`; stable across 7 tolerance factors |
| `[VERIFIED-tool]` | rung 3: `dim M = 1` | direct 24×24 solve; stable across 7 factors |
| `[VERIFIED-tool]` | the three blocks are pairwise inequivalent, without any rank decision | power-trace separation `0.0228` (a **theorem-based** certificate — its `3.88e−15` companion is a smoke test and scale calibration, **not** a failable control, §3b) |
| `[VERIFIED-tool]` | each block is absolutely irreducible ⇒ counts hold over `C` | `dim End_R = 1` ×3 |
| `[VERIFIED-tool]` | **NEGATIVE CONTROL passes**, in both forms | identical code path (bit-identical singular-value gaps); **and** three copies in *different bases* (blocks differ by `0.313`) still give **9**. *Forced, not failable — §5* |
| `[VERIFIED-tool]` | graded control gives `5`, the hand-predicted value; `U` does **not** normalise there (`0.919`) | shows the normalisation test can return `O(1)` |
| `[VERIFIED-tool]` | `8\|_{g2} = 1 ⊕ 7`, reproducing `G44` | commutant dim 2; multiplicities `{1, 7}` |
| `[VERIFIED-tool]` | a `Spin(8)`-invariant channel-mixing **trilinear** form exists, `dim Hom = 1` | `1,1,1` distinct; `0,0` controls; indexing verified term-by-term by pass 1 |
| `[VERIFIED-tool]` | **`dim M = #orbits`** on `{v,s,c}` | all six subgroups; `law_holds = true` |
| `[VERIFIED-tool]` | one extra generator outside `g2` collapses `18 → 3` and breaks `Φ` | commutator `0.347` |
| `[VERIFIED-tool]` | no verdict-bearing dimension is tolerance-sensitive | 7 factors, 12 orders, **including all three 576-column headline solves**; the single mover moves only below the noise floor and is named |

### 13b. Entailed by the construction — reported, but they could NOT have failed

Listed separately so they do not over-count the evidence. **This list is longer
than the first draft's**, because pass 2 found four items the first draft had
placed in 13a:

| reported | value | why it cannot fail |
|---|---|---|
| `σ³ = id`, `U³ = id` | `0.0` | pure index shifts |
| `σ` acts as `(x,y,z)→(z,x,y)` | `0.0` | `from_matrix` reads only the three off-diagonal positions |
| `σ δ σ⁻¹ = δ_{A₃A₁A₂}` | `0.0` | slot bookkeeping, true for any triple |
| **`σ` normalises the `so(8)` image** | `2.32e−15` | **σ-covariance of the ansatz is a theorem — §4a** |
| `U` commutes with the diagonal `g2` | `0.0` | a block permutation commutes with three identical blocks |
| `Φ`'s commutator with the diagonal `g2` | `0.0` | automatic given step 2e — §4a |
| **the negative control returning `9`** | `9` | `commutant ⊇ M₃ ⊗ End(ρ₁)` forces `dim ≥ 9` — §5 |
| **the FL ceiling being `1`** | `1` | every commutant contains `ℝ·I`; the sweep contains `Z3` — §5d |
| **the inequivalence certificate's `3.88e−15`** | `3.88e−15` | `tr(M^k)` is a similarity invariant — §3b |
| `three_blocks_are_literally_the_same_matrices` | `true` | a hardcoded literal |

### 13c. Non-computational tags

| tag | claim |
|---|---|
| `[CITED]` | Baez, arXiv:math/0105155 — `J3(O) = R³ ⊕ V8 ⊕ S8⁺ ⊕ S8⁻` and the `S3` permuting the slots. The slot-permutation automorphism itself **was** re-derived |
| `[CITED]` | `null_results` `G44`, `G102` (**quoted in full, including the `Path A needs independent fiber-Spin(8) POSTULATE` clause** — §7); `pearl_registry` rows 7 (incl. its `SUPERSEDED-IN-PLACE` line), 33, 34, 37, 39, 40; C38; C125; round95 §3 **and its `c0=−2` caveat**; C132 `P0` |
| `[WEAK]` | round90's cubic anomaly coefficients — Wikipedia + unverified modern-paper cluster. **Not** `[DOCS]`. Not load-bearing for §§3–6 |
| `[INFERRED]` | `σ` is an **outer** automorphism (triality). Chain in §3c; depends on criterion (b) |
| `[INFERRED]` | rung 2 is a postulate. Chain: `S⁶ = G2/SU(3)` has automorphism group `G2` → `G102`'s `c_so8(g2)=0` and its "Path A needs a POSTULATE" clause |
| `[INFERRED]` | rungs 2–3 and round119/124 share an **ingredient** and use it oppositely (§7). Both the pre-registration's framing and this round's first correction of it are withdrawn |
| `[SPECULATIVE]` | that a `G2`-breaking route would give a different answer on channel-uniformity. Not computed — V4 |

### Check (reproduces this decision)

```bash
python experiments/20260902-c133-symmetry-ladder-pairing-space/c133_symmetry_ladder.py
python -m ruff check experiments/20260902-c133-symmetry-ladder-pairing-space/
```

Expect: `step1_g2.dim_Der_O_exact = 14`; `step2c…nullity_numeric = 28`;
`step2e…dim_diagonal_subalgebra = 14`; `step3_rung1_G2.dim_End_g2_of_24dim_F_DIRECT_SOLVE
= 18` with `direct_solve_agrees_with_the_9x2_product = true`;
`step6_ladder = {18, 3, 1}`; `step4_negative_control_equivalent.dim_commutant_so8
= 9` **and** `step4_negative_control_conjugated_basis.dim_commutant_so8 = 9`
with `blocks_are_NOT_literally_identical_max_difference ≈ 0.31`;
`step5b…reps_are_pairwise_inequivalent_by_invariants = true`;
`step5g…law_holds = true`; `step5h…probes_that_move` listing exactly
`End(ρ₁)` and `all_probes_including_the_mover_stable_from_factor_1e-1_upward
= true`.

**Falsifiers that remain able to fire** (and, per §13b, the ones that do not):
* *Negative control:* `control([0,1,2])` is already run as
  `step4_control_inequivalent_reference` and returns 3, so the `9 → 3` flip is
  confirmed without a re-run. **But the control's own `9` is forced** (§5).
* *Triality normalisation:* returns `0.919` on the graded control, so the
  **test** can return `O(1)` — though not on the covariant arrangement (§4a).
* *Tolerance:* `End(ρ₁)` genuinely moves at factor `1e−3`, and is reported.

---

## 14. FL Step 8a — two context-blind skeptic passes (BOTH RUN)

Full record, including both prompts verbatim-in-substance and every finding:
**`skeptic_verdict.md`**, in this directory.

**Disclosure, carried rather than deleted.** An earlier state of this file said
in this section *"Status: SEE §15 (run and incorporated)"* **before any pass had
run**; pass 1 caught it. The first repair then **cited `skeptic_verdict.md` as
written when it did not exist**; pass 2 caught that. Both are recorded because a
process gate falsely marked done is exactly the failure FL's third-outcome
discipline exists to prevent — and this round committed the same act twice, one
layer apart.

| | Pass 1 | Pass 2 |
|---|---|---|
| prompt register | formal, enumerated attack list `A`–`H` | narrative ("a colleague hands you a finished write-up"), same semantic content, different structure |
| reviewed | the pre-repair document | the **post-repair** document |
| **verdict** | **`[WEAKENED]`** | **`[WEAKENED]`** |

**The two verdicts AGREE**, so per `falsification-ladder.md`'s
Paraphrase-Sensitivity rule the single-run Response Matrix applies and no third
pass is required. Pass 2 was run because pass 1's findings 3 and 4 changed the
direction of a recorded **gate** sub-verdict (FL Step 4a: "no stop condition
fires" → `CRITERION_INVALID` at rung 1).

**Sixteen findings accepted across the two passes. None dismissed.** Eight
required re-running the script. Per `audit-verification-gate.md` every finding
was independently re-verified by this session before acceptance.

**Pass 2's most valuable result:** **four of the repairs made in response to
pass 1 reintroduced the very defect class they were meant to cure** — a
similarity-invariant "control" replacing an `x−x` control; a swept ceiling that
was still forced; a confessed criterion (a) sitting beside an unconfessed
criterion (c); a "verdict-bearing dims all stable" flag secured by excluding the
dimension that moves. **A partial confession is worse than none.** That
observation is proposed as a methodological pearl (§11).

**Pass 2's single most consequential finding** is §7's Error 2: the first
repair quoted an un-superseded registry row **one clause short of the clause
that contradicted the repair**. Re-verified directly against
`null_results/INDEX.md` line 35 and `pearl_registry` row 40.

**Both passes' limitation, stated by each:** neither could execute code. Pass 1
flagged two items, pass 2 one, as needing a re-run. **This session ran all
three** — the tolerance sweep, the rebuilt inequivalence certificate, and the
576-column robustness check — and every repair in this document was re-executed,
not merely argued.

**What the passes confirmed rather than broke** is recorded in
`skeptic_verdict.md` and is substantial: the headline arithmetic (pass 2: *"I am
not disputing the arithmetic"*), all eleven reported numbers traced to the JSON,
the shared code path proved by bit-identical floats, the trilinear indexing
checked term by term, `168 = 7·6·5 − 7·3!` re-derived independently,
`Hom_{SU(3)} = 6` and the `54` caveat confirmed, `U24 = slot_perm([1,2,0])`
verified index by index, **every documentary citation accurate and verbatim**,
and **none of `claim.md`'s four forbidden claims re-committed**.

---

## 15. Evidence tier of this round's central conclusion

**Central conclusion:** *For couplings of endomorphism type between the `S⁶`
triality-channel label and any structure carrying no action of the assumed
symmetry, the permitted **channel matrix** has dimension `9` under `G2`, `3`
under `Spin(8)`, and `1` under `Spin(8)` extended by the triality `Z3` — and
more generally its dimension equals the number of orbits of the assumed channel
symmetry on `{v,s,c}`, so `G2` constrains the channel dependence not at all,
`Spin(8)` forces block diagonality with independent per-channel coefficients,
and equal coefficients are forced exactly by transitivity.*

**Tier: `[VERIFIED-tool]`, MEDIUM-HIGH confidence** — downgraded from the first
draft's HIGH, on both passes' findings, and on a narrow, explicitly named class.

Grounds that survive:

* Every number is a computed dimension from a self-contained from-scratch
  construction, with an auditable singular-value gap at every rank call, exact
  rational arithmetic where it matters most, and a tolerance sweep over twelve
  orders covering **all three headline solves** showing no verdict-bearing
  dimension moves.
* All three rungs are now solved by the **same** machinery.
* Kill criterion (b) — the one that carries the ladder — did not fire and could
  have, and is independently certified by a theorem-based invariant with a
  measured separation of `0.0228`.
* The orbit-counting law is verified on all six subgroups, upgrading `§6b` from
  two data points to a law.
* Three registry facts were reproduced, not assumed (`G44`'s `7⊕1`, `G102`'s
  `Hom_{g2}=2`, row 34's `G2`-level `Φ`).
* Two differently-worded context-blind passes **agree**, and neither found a
  mathematical error.

Why not HIGH:

* **Only one of three kill criteria is falsifiable as written** (§4a). The
  round's contingent content is narrower than "three independent checks passed".
* **Three of its checks cannot fail** — the mandatory negative control, the FL
  ceiling, and the inequivalence certificate's companion number (§13b). One was
  strengthened by re-run; none was removed, and none is now claimed as a
  ground.
* **FL Step 4a returns `CRITERION_INVALID` at rung 1** (§5d) — not evidence
  against the claim, but rung 1 carries no discriminating information.
* **Essentially every individual number reproduces a standard `Spin(8)`/triality
  fact** (§2). The round's contribution is the verified chain and the four new
  findings, not the numbers.

**Tier for rung 1 specifically: `[VERIFIED-tool, NON-FALSIFIABLE AS TESTED]`.**
The number is right and now directly solved, but the check could not have come
out otherwise and its FL criterion is `CRITERION_INVALID`.

**What keeps the whole from being more:**

* It is **fibre-level** representation theory — silent on whether any of these
  symmetries acts on the physical compactification, which is precisely
  `pearl_registry` row 7's own current live question (§7, V2).
* It covers the **endomorphism class only** (§6a).
* Rungs 2–3 are **postulates priced, not established** (§7). The conclusion has
  the form "if you assume `X`, you may conclude `Y`"; the `[VERIFIED-tool]` tier
  attaches to the implication, **not** to `X`.

**The downstream statement, after two corrections.** That rungs 2 and 3 are both
postulates is `[INFERRED]`, chain in §7. That they draw on the *same credit
line* as `N_gen=3` (pre-registered) and that they draw on a *different* one
(this round's first correction) are **both withdrawn**; the accurate statement —
a shared un-derived **ingredient**, used in opposite ways — is `[INFERRED]`,
grounded in `G102`'s un-superseded full text and `pearl_registry` row 40. *The
first draft closed by calling this withdrawal `[VERIFIED-tool]`; reading a
markdown status line is not tool-verification, and that tag is retracted.*
