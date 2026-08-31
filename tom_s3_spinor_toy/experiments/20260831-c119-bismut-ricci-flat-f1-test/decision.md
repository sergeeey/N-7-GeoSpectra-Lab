# C119 decision -- the Bismut-Ricci-flat condition is NOT applicable to
the frozen `S³×S⁶` background. F1 = FAIL, on the compact 9-manifold
with a strict product metric and exact (no-dilaton) closure -- three
failure modes, two of which share one input, the third topological.

**Verdict (matches `results_c119.json`'s machine-readable string
verbatim -- see note under "Verification" for the one-time reconciliation):**
`F1_FAIL__S6_FACTOR_IS_BISMUT_RICCI_POSITIVE_NOT_FLAT_(rho=5_EXACTLY)__ITS_CHARACTERISTIC_TORSION_IS_CO_CLOSED_BUT_NOT_CLOSED__AND_b3(S⁶)=0_MAKES_THE_PRODUCT_CONDITION_UNRESCUABLE_BY_ANY_t_TORSION_OR_RADIUS`

**Scope qualifiers on "unrescuable" (added after FL Step 8a skeptic
pass -- the topological kill is airtight only under these three
hypotheses, all satisfied by this project's actual setup, but none
were stated in the original verdict string):** compact **9-manifold**
`S³×S⁶` (the internal factor, not the full 13d background --
Poincaré invariance restricts admissible `H` to purely-internal legs,
so this is the physically relevant reduction, but it is an assumption,
stated here explicitly for the first time); **strict product** metric
(the non-product case, round103's open fork, is NOT closed by this
round -- see caveat 4); and **exact closure** `δH=0` rather than the
dilaton-corrected `d*(e^{−2φ}H)=0` (checked by the skeptic: on a
homogeneous internal space with `φ` constant along `S⁶` the two
coincide, so this does not change the verdict, but the hypothesis is
real and is now on the record rather than silently assumed).

**Status:** RESOLVED, on the exact question `claim.md` pre-registered.
The pre-registered kill criterion fired on BOTH of its clauses
independently (`rho_{S⁶} ≠ 1` at any radius; `dT_{S⁶} ≠ 0`), plus the
pre-registered *second* kill criterion (novelty) also fired on the
surviving `S³`-only half (see reworded verdict on that sub-claim below
-- FL Step 8a narrowed "no new content" to "no new equation").
**FL Step 8a skeptic pass completed 2026-08-31 (context-blind,
artifacts only): overall F1=FAIL verdict CONFIRMED after independent
re-derivation of every load-bearing number. Several summary claims
WEAKENED as overreach -- not the result itself, the wording around it.
Full skeptic response matrix in a new section below; every accepted
correction has already been applied in place throughout this file, not
left as an addendum.**

**Gate field assessed:** `PARENT_ACTION_GATE.md` **F1 only.** F2, F4-F7
not assessed. This round is NOT a gate decision on OB1.

---

## Answers to the four pre-registered sub-questions

| Q | Answer | Evidence |
|---|---|---|
| **Q1** — is `T_{S⁶}` closed? | **NO.** `dT_{S⁶}` has **72 nonzero components**. It IS co-closed (`d*T = 0`, 0 components), i.e. `T` is co-closed but not closed. | Computed two independent ways (below). The premise that closedness is "a well-established fact in the nearly-Kähler literature" is **false** — the established facts imply the opposite (see "Correction to the incoming premise"). |
| **Q2** — is the frozen `S⁶` itself Bismut-Ricci-flat? | **NO.** `Rc − ¼T² = (4/3)·δ ≠ 0`. `rho_{S⁶} = Rc/(¼T²) = **5 exactly**`, and `rho` is radius-independent, so no `S⁶` radius repairs it. | Project's own certified `T`-table + project's own certified `Ric = 5/3`; independently confirmed by Agricola's `Ric^{∇̄} = 2·Scal/15` (= 2·10/15 = 4/3, exact match). |
| **Q3** — does the product satisfy `Rc = ¼H_tot²`? | **NO.** Cross-blocks of `H_tot²` are zero for the direct-sum ansatz `H_tot = H_{S³}⊕H_{S⁶}` (verified by explicit 9-index sums in `PART 4` -- FL Step 8a note: this shows the property of the *specific object built*, not that a *general* admissible `H` on the product must take this form; that stronger, non-trivial statement is what `PART 6(b)`'s topological argument actually establishes, via `Λ¹(𝔰𝔲(2))^{SU(2)}=Λ²(𝔰𝔲(2))^{SU(2)}=0` in the invariant sector -- credit reattributed here). Given that, the condition decomposes exactly as expected: `S³` block ⟺ `t ∈ {0,1}` (radius-independent), `S⁶` block has **no solution at any radius** (`sympy.solve` returns the empty set). | `PART 4` + `PART 6(b)`. |
| **Q4** — is `H_tot` closed and `g`-harmonic? | **NO.** `H_{S³}` alone is harmonic on the product (closed by degree, co-closed since `*₉H_{S³} ∝ vol_{S⁶}`); `H_{S⁶}` is not closed, so `dH_tot ≠ 0`. The pair `(g, H_tot)` is therefore **not even a legal "generalized metric"** in the sense the definition requires, independently of the Ricci equation. | `PART 3` + `PART 5`. |

---

## The three failure modes, in increasing order of strength (FL Step
8a note: modes 1 and 3 share one input -- both terminate on "the
frozen `S⁶` has `Ric ≠ 0`"; mode 1 additionally needs the exact value
`5/3`, mode 3 needs only the weaker fact `Ric ≠ 0`. Mode 2 is the only
one fully independent of the other two. Originally presented as
"three independent ways" -- corrected here, not silently.)

### 1. Numerical (the frozen data) — off by a factor of exactly 5

In the project's own `S⁶` normalization (`build_T_table`, `Ric = 5/3`,
`Scal = 10`, all from the same Round-16 primitives):

```
(T_{S⁶}²)_ab  = 4/3 · δ        [computed, exact]
Rc(g_{S⁶})_ab = 5/3 · δ        [project-certified, Round 16, triple-verified]
Rc − ¼T²      = 4/3 · δ  ≠ 0
rho_{S⁶}      = 5              exactly, and radius-independent
```

The rescaling that *would* satisfy it is `T → √5·T` — not a member of any
canonical connection family, and not the characteristic connection the
project's `S⁶` index-theory chain uses.

**Independent literature confirmation of this exact number.** Agricola's
Srní lectures state that any 6-dimensional nearly-Kähler manifold is
`∇̄`-Einstein with `Ric^{∇̄} = 2(Scal^g/15)·g`. Since `T` is parallel
(Kirichenko) hence co-closed, `Ric^{∇̄}` is symmetric and equals exactly
`Rc(g) − ¼T²` — the Bismut-Ricci tensor. For the project's `Scal = 10`
this predicts `2·10/15 = 4/3`, **the exact defect computed above**. The
literature therefore says outright what this round independently
computes: **the Bismut-Ricci of a strict nearly-Kähler 6-manifold is
`2Scal/15 · g`, which is never zero for `Scal > 0`. No strict
nearly-Kähler 6-manifold is Bismut-Ricci-flat.** This is not a property
of the project's particular `S⁶`; it is a property of the class.

### 2. Bianchi — the torsion is co-closed but NOT closed

`dT_{S⁶} ≠ 0`, computed two structurally independent ways which agree:

- **Route A** — the Chevalley-Eilenberg differential for invariant forms
  on a reductive homogeneous space, `dα(X₀..X_p) = Σ_{i<j}(−1)^{i+j}
  α([X_i,X_j]_m, …)`, fed with the project's own structure constants
  `[Z_i,Z_j]_m = T(i,j,·)`. **72 nonzero components.**
- **Route B** — the purely algebraic parallel-torsion identity
  `dT = 2σ_T`, `σ_T = ½Σ_i(e_i⌟T)∧(e_i⌟T)`. **72 nonzero components**,
  and `dT_A = −2·σ_T` component-for-component.

Route A's machinery passed a nontrivial validity test that would have
caught a wrong formula: **`d(dω) = 0` exactly**, which is *not* automatic
(`[·,·]_m` alone does not satisfy Jacobi), and it reproduced both
nearly-Kähler structure equations exactly:

```
d(omega)  = -sqrt(3) · psi^+          = -3λ·psi^+ ,  λ = 1/sqrt(3)
d(psi^+)  = 0                          (0 components)
d(psi^-)  = (2sqrt(3)/3) · omega^omega = +2λ·omega^2
d(*T)     = 0                          (0 components)  ->  T is co-closed
```

against Foscolo arXiv:1601.04400 eq. (2.15), read verbatim from the paper
body: `dω = 3 Re Ω`, `d Im Ω = −2ω²`. The two overall signs differ from
the literature's *consistently* (both flipped), which is a phase/
orientation convention on `Ω`, not a discrepancy — see "Honest caveats".

Since `dψ⁻ ∝ ω∧ω ≠ 0` and `T = −λψ⁻` (proved component-by-component
below), `dT ≠ 0` is forced by the nearly-Kähler structure equations
themselves. **Closedness of the `S⁶` characteristic torsion is not merely
unproven — it is incompatible with the structure that makes `S⁶` nearly
Kähler in the first place.**

### 3. Topological — the strongest, and it kills every rescue at once

This was not asked for and is the round's main free finding.

The definition requires `H` **closed** and **`g`-harmonic**, i.e.
`dH = 0` and `δH = 0`, i.e. `H` is a **harmonic 3-form**. On a compact
oriented manifold Hodge's theorem makes the space of harmonic 3-forms
isomorphic to `H³(M;ℝ)`. By Künneth,

```
H³(S³×S⁶; R) = ⊕_{p+q=3} H^p(S³)⊗H^q(S⁶)
             = H³(S³)⊗H⁰(S⁶)  ⊕  H²(S³)⊗H¹(S⁶)  ⊕  H¹(S³)⊗H²(S⁶)  ⊕  H⁰(S³)⊗H³(S⁶)
             = R⊗R  ⊕  0⊗0  ⊕  0⊗0  ⊕  R⊗0
             = R
```
(FL Step 8a: the full Künneth sum, not just the `b₃(S⁶)=0` term --
the `(1,2)`/`(2,1)` cross terms vanish because `b₁(S³)=b₂(S³)=0`, not
because of anything about `S⁶`. A reader quoting only "`b₃(S⁶)=0`"
gets an incomplete proof; both factors' Betti numbers are needed.
**Stronger, transferable form** (also flagged by the skeptic): since
`b₁(S⁶)=b₂(S⁶)=b₃(S⁶)=0`, harmonic forms on a Riemannian product being
tensor products of harmonic forms on the factors means **no harmonic
3-form on ANY product `M×S⁶` has a single leg on `S⁶`**, regardless of
what `M` is -- this kills every mixed component `H_{pμν}, H_{pqμ},
H_{pab}` too, on the full 13d background, not only the `S³`-only
mixing this section originally covered. See the `pearl_registry`
recommendation at the end, now phrased in this stronger form.)

so for a product metric the *entire* space of admissible `H` is
`ℝ·vol_{S³}`, forcing `H|_{S⁶} = 0`. The `S⁶` block of `Rc = ¼H²` then
reads

```
Ric(g_{S⁶}) = 0        —  the S⁶ factor would have to be RICCI-FLAT.
```

The frozen `S⁶` is Einstein with `Ric = (5/3)δ > 0`. **Contradiction, and
no choice of `t`, of the `S⁶` torsion, or of either radius can repair it,
because `b₃(S⁶) = 0` is a topological fact about the frozen background,
not a normalization.**

An explicit `G₂`-invariant exhaustion confirms the same thing from the
other direction. The general `G₂`-invariant 3-form on `S⁶ = G₂/SU(3)` is
`H = αψ⁺ + βψ⁻` (the `SU(3)`-invariant part of `Λ³𝔪*`), and:

```
(H^2)_aa = 4(alpha^2 + beta^2)     ->  Rc = (1/4)H^2  requires  a^2+b^2 = 5/3
dH   = 0   <=>  beta  = 0
d*H  = 0   <=>  alpha = 0
BOTH       <=>  alpha = beta = 0   ->  H = 0            (harmonic => zero)
=> no (alpha,beta) satisfies all three.  Verified by sympy.solve.
```

Note the near-miss this exhaustion exposes and closes: `H = √5·λ·ψ⁺`
*does* satisfy `Rc = ¼H²` **and** `dH = 0`. It fails only `δH = 0`. That
is the single closest configuration to a rescue, and it is dead.

---

## What survives (narrow, stripped of interpretation)

> 1. **The `S³` computation is correct and reproduces round111 exactly.**
>    `Rc(g_{S³}) − ¼H_{S³}² = 8t(1−t)·δ` **identically in `t`** — not
>    merely at the roots — which is round111's own certified
>    `Ric^t = 8t(1−t)δ`, re-derived here from scratch by an independent
>    route (Killing form / Cartan-Schouten torsion, vs. round111's
>    `R^t`-contraction). Roots: `t ∈ {0,1}`, independent of the `S³`
>    radius.
> 2. **The project's frozen `S⁶` torsion is exactly the standard
>    `SU(3)`-structure form.** `T_{S⁶} = −λ·ψ⁻` with `λ = 1/√3`,
>    component-by-component, where `ψ⁻ = Im Ω` in the basis
>    `ω = e¹²+e³⁴+e⁵⁶`. Independently: `‖T‖² = 4/3` equals the literature's
>    nearly-Kähler identity `(2/15)Scal^g = (2/15)·10 = 4/3` exactly, and
>    `Ric = 5λ² = 5/3` equals the project's own certified value. This
>    **cross-validates the project's `S⁶` normalization** (`Scal = 10`,
>    `radius² = 3`) against external nearly-Kähler theory for the first
>    time, closing a caveat that had been open since Round 16 ("Scal=10 vs
>    the unit-round-`S⁶` value 30 … documented as a caveat, not dismissed
>    outright"). `Scal = 10` is confirmed correct-and-consistent, simply
>    in `radius²=3` units.
> 3. **`(H_tot²)` has zero cross-blocks on a Riemannian product** — verified
>    by explicit 9-dimensional index sums, not assumed. The
>    Bismut-Ricci-flat condition therefore decomposes into one independent
>    condition per factor, exactly as expected.
> 4. **`T_{S⁶}` is co-closed (`δT = 0`) but not closed (`dT ≠ 0`)**, with
>    `dT = ∓2σ_T`, two independent routes agreeing.

## What does NOT survive

- **"Bismut-Ricci-flatness selects `t ∈ {0,1}` for this project."** It does
  so for `S³` *in isolation*. It does not transfer to the frozen
  `S³×S⁶`, which admits no Bismut-Ricci-flat generalized metric at all.
  Per Gate 1's non-transfer rule: a verdict established for artifact A
  does not transfer to artifact B because they share a factor. This
  round is the check that was owed.
- **The `S³`-only half as a new *equation*, even taken alone.** This is the
  second pre-registered kill criterion, and it fires at the equation level.
  The computation shows `Rc(g_{S³}) − ¼H_{S³}² ≡ Ric^t` **as an identity in
  `t`**, so "Bismut-Ricci-flat on `S³`" is *literally the same equation* as
  "the Cartan-Schouten connection `∇^t` is Ricci-flat", which round111
  certified on 2026-07-17 — and `t ∈ {0,1}` are the points where `∇^t` is
  outright **flat** (`R^t = t(t−1)[[·,·],·]`, round99; classically,
  Cartan-Schouten's `±1` connections). The mechanism is an **equivalent
  restatement** of the equation, the same verdict shape round116's "spectral
  flow" attempt received. **FL Step 8a correction:** the original wording
  ("supplies no new content on `S³` either") overreached -- whether the
  generalized-Ricci-flow framing supplies a new *justification* for that
  equation (why this condition rather than another) is exactly gate field
  **F4**, which this round explicitly declines to assess (see "What this
  round does NOT show" below). A round cannot decline F4 and simultaneously
  rule the F4-shaped content empty. Corrected claim: **no new equation on
  `S³`; whether there is a new justification is an unassessed F4
  question.**
- **The read-only round's characterization of Fusi-Lafuente-Stanfield.** Two
  corrections from the abstract itself (arXiv:2608.25619, tool-verified):
  the stability result is for **Bismut-FLAT** standard bi-invariant metrics
  (strictly stronger than Bismut-Ricci-flat), and the same paper
  *constructs dynamically **unstable** Bismut-flat metrics which are
  non-standard*. "Dynamical stability of exactly this condition" overstates
  it in two directions at once.

---

## Correction to the incoming premise

The task framing asserted that closedness of the nearly-Kähler `S⁶`
characteristic torsion "is a well-established fact in the nearly-Kähler
literature" and asked for a citation. **There is no such fact to cite; the
established facts entail its negation.** Recorded explicitly so this does
not get re-attempted:

- Foscolo arXiv:1601.04400 (2.15), read verbatim: `dω = 3 Re Ω`,
  `d Im Ω = −2ω²`.
- The characteristic torsion of a strict nearly-Kähler 6-manifold is
  proportional to `Im Ω` (verified here directly: the project's own
  certified table *is* `−λ·Im Ω`, exactly), whose differential is
  `−2λω² ≠ 0`.
- What *is* true, and is presumably the fact being half-remembered:
  `T` is **parallel** (Kirichenko's theorem — Alexandrov-Friedrich-
  Schoemann arXiv:math/0403131, abstract, first sentence) and
  **co-closed** (`d*T = 0`, verified here, 0 components), because
  `*T ∝ ψ⁺` and `dψ⁺ = 0`. Parallel and co-closed, not closed.

The previous round's own `[INFERRED, not verified]` prediction — "S⁶'s
torsion likely isn't closed, or the combined condition likely fails" —
was **correct on both counts**. This round upgrades it `[INFERRED] →
[VERIFIED]` and adds the topological no-go, which was not predicted.

---

## Honest caveats (stated here, not left for a reviewer to find)

1. **Global sign ambiguity on `T`, verdict-irrelevant.** Route A gives
   `dT = −2σ_T` where the textbook identity for parallel torsion reads
   `dT = +2σ_T`. Two candidate explanations, not distinguishable from this
   data: (i) the project's `torsion_T(i,j,k) = +⟨[Z_i,Z_j]_𝔪, Z_k⟩` is the
   negative of the canonical connection's torsion `T(X,Y) = −[X,Y]_𝔪`
   (`T → −T` flips `dT`, leaves `σ_T` invariant since it is quadratic);
   (ii) a global sign convention in this round's `d_invariant`. The same
   single flip explains `dω = −3λψ⁺` vs the literature's `+3λψ⁺`.
   **No verdict depends on it:** `H²` is quadratic in `H`, and
   "`dT = 0` or not" is sign-blind (linear map, `d_{−C}=−d_C`, `0→0`
   and nonzero→nonzero regardless of sign). The *magnitude* 2 matches
   exactly, which is the nontrivial content. **FL Step 8a strengthening:**
   "72 nonzero components" is not merely plausible corroboration, it is
   FORCED given `dT ∝ ω∧ω = 2(e^{0123}+e^{0145}+e^{2345})` (3 basis
   4-forms; the script's dense totally-antisymmetric storage gives each
   `4!=24` entries; `3×24=72` is the only possible count for a nonzero
   answer of this shape) -- this is the round's single strongest
   corroboration and was not called out as such in the original text.
2. **`Ric(S⁶) = 5/3` is cited, not re-derived here.** It is the project's
   own Round-16 value, stated as triple-verified and computed from the
   same shared primitives as the `T`-table (so the normalization is
   guaranteed consistent — that consistency is the reason it was used
   rather than an external value). It is *independently corroborated* this
   round via `Ric = 5λ²` with `λ` read off the structure equation
   `dω = 3λψ⁺` computed from the same table, and via `‖T‖² = (2/15)Scal`.
   Not re-derived from `𝔤₂` structure constants — the project does not have
   the full `𝔥`-part built (`g2su3_H_element.py`'s own note).
3. **Agricola's `Ric^{∇̄} = 2Scal/15` was extracted via a WebFetch
   summarizer on the ar5iv HTML of arXiv:math/0606705**, not by a verbatim
   in-paper text search (the arXiv MCP's text-search cache path failed for
   legacy IDs). Marked `[VERIFIED-tool, secondary extraction]`. Its
   numerical content is independently confirmed by this round's own
   computation (`2·10/15 = 4/3` = computed defect), so nothing load-bearing
   rests on the extraction alone. Foscolo (2.15) and the Alexandrov-
   Friedrich-Schoemann abstract were read directly.
4. **The non-product case is NOT closed by this round.** The topological
   argument's `dim H³(S³×S⁶;ℝ) = 1` step is metric-independent, but the
   step "the harmonic representative is `vol_{S³}`, hence `H|_{S⁶}=0`" uses
   productness. A genuinely non-product metric on `S³×S⁶` (round103's
   still-open fork) would need this redone. Named below as the one
   surviving branch, not silently assumed dead.
5. **Whether *any* metric on `S⁶` can be Ricci-flat is deliberately not
   claimed either way.** The argument only needs that the *frozen* `S⁶`
   (nearly-Kähler, Einstein, `Ric > 0`) is not.
6. **[Added by FL Step 8a skeptic pass]** No dilaton. The physical
   fixed-point system this project's target setting would actually use
   carries `Rc − ¼H² + 2∇²φ = 0`, `d*(e^{−2φ}H) = 0`, not the constant-
   dilaton `δH=0` tested here. Checked (not merely noted) by the
   skeptic: on a homogeneous internal space with `φ` constant along
   `S⁶`, `∇²φ|_{S⁶}=0` and `e^{−2φ}` is an internal constant, so both
   equations reduce to the ones this round tests -- **the verdict
   survives**, but the no-dilaton hypothesis was invisible in the
   original write-up and is now explicit.
7. **[Added by FL Step 8a skeptic pass]** `Ric(g_{S⁶})=5/3` relies on
   the `S⁶` torsion table's frame being orthonormal for the metric that
   value is stated for. `PART 0` asserts this explicitly for `S³`
   (`met3 == eye(3)`); no symmetric assert exists for the imported `S⁶`
   frame. The nearly-Kähler structure equations coming out with the
   exact right coefficients (`dω=3λψ⁺`, `‖T‖²=(2/15)Scal`) is strong
   indirect evidence the frame is in fact orthonormal, but it is
   indirect -- one assert would close this residual gap. Not fixed
   retroactively in the already-run script/JSON, per this project's
   convention (corrections live in decision.md, raw output is not
   mutated after the fact); named here as unattempted future hygiene.

---

## FL Step 8a skeptic pass (2026-08-31, context-blind -- artifacts only,
no session history)

| Object | Verdict |
|---|---|
| **F1 = FAIL** (Bismut-Ricci-flat inapplicable to frozen `S³×S⁶`) | **CONFIRMED** -- independently re-derived every load-bearing number (Ricci of `S³` via two routes, `‖T‖²=4/3`, `Ric(S⁶)=5/3` via `λ`-scaling with no citation needed, the 72-count as forced, Künneth) |
| "`dT≠0`, 72 components" | **CONFIRMED**, and shown to be the *only possible* nonzero count, not merely plausible |
| "`ρ_{S⁶}=5` exactly, radius-independent" | **CONFIRMED**, independently re-derived from Gray's identity alone |
| "unrescuable by any `t`/torsion/radius" | **WEAKENED** -- correct as proved, but proved under three unstated hypotheses (compact 9-manifold, product metric, exact `δH=0`); skeptic extended the proof to the 13d background and to the no-dilaton case and confirmed it survives both -- so this is a **documentation gap, not a hole in the result**. Now stated explicitly above. |
| "three independent failure modes" | **WEAKENED** -- modes 1 and 3 share one input (`Ric(S⁶)≠0`); corrected above |
| "`S³` half supplies no new content" | **WEAKENED** -- overreaches into unassessed gate field F4; corrected to "no new equation" above |
| Global sign ambiguity is verdict-irrelevant | **CONFIRMED**, for a stronger reason than originally given (linear map argument, not just "checked and it didn't matter") |
| `Ric(S⁶)=5/3` citation strength | **REJECTED-WITH-REASON** as a live concern -- the number is independently re-derivable from data this round already has (`λ²=1/3` from `‖T‖²`, `Ric=5λ²`), with no citation needed at all; the round under-sold its own strongest evidence by leading with the citation instead |
| Künneth argument correctness | **CONFIRMED** as stated in the script; **ACCEPTED as a documentation defect** in `decision.md`'s compressed version (fixed above, plus a stronger transferable form supplied) |
| "Harmonic" is the literature's real hypothesis, not a strengthening | **CONFIRMED** -- generalized Ricci flow fixed points require `H` closed by Courant-algebroid construction, `d*H=0` from the flow equation; this is not the round's own stricter-than-necessary reading |

Full adversarial detail (five interrogated concerns, five additional
findings not in the original brief, one steelman-and-attack on the
strongest single objection, a Recomposition Gate check, and nine
concrete edit recommendations) is preserved in the session transcript;
every accepted correction from it has been applied in place above, not
appended as an unintegrated addendum. Nothing in the skeptic pass
reversed F1=FAIL.

---

## Kill Analysis (per the Anti-Overfitting Gate discipline)

**What was killed.** The claim "the Bismut-Ricci-flat condition
`Rc(g) = ¼H_g²` is a `t`-selection mechanism for this project's
background." Killed at gate field **F1**, before F4 was ever reached: the
mechanism's own geometric hypothesis is unsatisfiable on the frozen
`S³×S⁶`. Additionally killed, separately: the claim that the `S³`-only
root is *new information*, since it is an identity-level restatement of
round111/round99.

**What was NOT killed.**

- **The `S³` arithmetic.** Fully correct, and now cross-validated against
  round111 by a second independent route. `t = 0,1` are genuinely the
  Bismut-Ricci-flat (indeed Bismut-flat) points of `S³ = SU(2)`. That is
  a true statement about `S³`; it is simply not a statement about the
  project's background.
- **OB1 itself.** Untouched. It stays `PARKED`. This round meets none of
  its four reopen conditions — indeed it *closes* the candidate that
  looked like reopen-condition 2 ("a directly relevant parent mechanism
  is published somewhere new"): the mechanism is real and newly
  published, but not relevant to this background.
- **The Lauret-Will / Gutiérrez / Fusi-Lafuente-Stanfield results
  themselves.** All correct and all verified real. Their construction
  produces Bismut-Ricci-flat metrics on spaces of the form
  `G₁×G₂/ΔK` with `Gᵢ` compact simple. `S³×S⁶ = SU(2) × G₂/SU(3)` is a
  product of a group and a coset, **not** of that form — a structural
  reason, independent of everything above, why the literature's own
  examples do not reach this background.
- **`N_gen=3`'s CONDITIONAL status.** Unchanged, in either direction, as
  pre-registered. Also unchanged: `lambda = FREE_COUPLING_PARAMETER`,
  `safe_for_runtime = False`.
- **The `S⁶` index-theory chain (G73/G74A/G74B).** Untouched. This round
  reads the same `S⁶` torsion data but asks a different question of it,
  and in fact *strengthens confidence in that data's normalization*
  (survivor 2 above).

**Relaxation Map** — one assumption changed per row, per the Minimal
Relaxation Rule. None attempted this round.

| Assumption relaxed | What it would take | Status |
|---|---|---|
| Drop "`H` closed & harmonic", keep only `Rc = ¼H²` | `S⁶` still fails by the factor 5 unless `T → √5·T`, which is no canonical-family connection and would break the `S⁶` index chain. And the whole *motivation* evaporates: without `dH=0`/`δH=0` the configuration is not a generalized-Ricci-flow fixed point, so none of the stability results apply. | **Dead as stated** |
| Weaken "flat" to constant-`λ` ("soliton-shaped"): `Rc − ¼H² = λg` | Computed this round (`PART 7`, scoped: this is only the *necessary metric equation* of a homogeneous soliton, not the full system). Matching the two blocks gives `t(1−t) = c₃²/(6c₆²) > 0`, i.e. **`0 < t < 1` strictly — `t = 0` and `t = 1` are EXCLUDED**, the opposite of what OB1 needs, and it leaves a one-parameter curve rather than a discrete selection. It also does not repair `dH ≠ 0`. | **Actively unhelpful**, computed, not merely asserted |
| Replace the frozen `S⁶` by a Ricci-flat 6-manifold | Would satisfy the topological constraint, but destroys the `N_gen=3` chain, which needs the nearly-Kähler/`G₂` structure. Would require re-deriving G73/G74A/G74B from scratch on a new space. | Out of scope; would be a background modification, and `PARENT_ACTION_GATE.md` F1 requires such a modification to state explicitly whether the `S⁶`-only chain survives |
| Leave the strict product ansatz (round103's open fork) | `dim H³ = 1` still holds (metric-independent), but the harmonic representative need not vanish on the `S⁶` directions, so the "`Ric(g_{S⁶}) = 0`" step must be redone. | **The one surviving branch.** Not closed by this round |

---

## What this round does NOT show (scope boundary, repeated verbatim from
`claim.md`)

1. Tests **ONLY** `PARENT_ACTION_GATE.md` field **F1** — geometric
   applicability to the frozen background. F2 and F4-F7 not assessed. In
   particular **F6 (background equations) remains NOT SUPPLIED**, and a
   generalized-Ricci-*flow* fixed-point condition would not have filled it
   anyway: a flow on the space of generalized metrics is not an action
   principle for the physical background.
2. Does **NOT** re-derive round111's `S³`-only result as a new finding —
   cited, and used only as a cross-check target (which it passed exactly).
3. Does **NOT** change `N_gen=3`'s CONDITIONAL status, in either
   direction. Not the `S⁶` index computation.
4. Does **NOT** by itself move OB1 out of `PARKED`. Per OB1's reopen
   condition 4, a candidate must pass the whole `PARENT_ACTION_GATE`
   checklist; one field's verdict is not a gate decision. Any status
   change requires a separate, explicit gate decision.
5. Does **NOT** show that no parent action exists for OB1, nor that
   generalized Ricci flow is irrelevant to this project in general — only
   that this specific condition is unsatisfiable on this specific frozen
   background.
6. Does **NOT** solicit Tom Lawrence's Part 5.
7. No registry file was edited (`CLAIM_LEDGER.yaml`, `OPEN_BLOCKERS.md`,
   `ALIVE_BRANCHES.md`, `pearl_registry/INDEX.md` all untouched), and
   nothing was committed. A separate FL Step 8a skeptic pass and a
   separate registry-update step are owed before any of this is treated
   as certified.

---

## Named, unattempted next steps (in cost order)

1. **Nothing, most likely.** The honest recommendation: the candidate is
   dead at F1 for a topological reason, and further investment in this
   specific mechanism is not warranted. Recorded so a future session does
   not re-derive the `S³` root and re-experience it as a discovery.
2. If anything: **the non-product branch** (caveat 4). Cheapest form —
   for a general (non-product) metric on `S³×S⁶`, is the unique harmonic
   3-form forced to be "vertical"? If yes, the no-go is fully general for
   this manifold and round103's fork is closed for this mechanism too.
3. **A candidate `pearl_registry` entry, per the Caveat Gate** (registry
   edit done in the follow-up integration step, not by this script/round
   itself): the topological obstruction generalizes past this mechanism,
   in the STRONGER form the skeptic pass identified. *Any* proposed
   background-selection principle whose statement requires a harmonic
   k-form (k=1,2,3) with a nonzero leg on the `S⁶` factor is
   dead-on-arrival for ANY product `M×S⁶`, not just `S³×S⁶` — because
   `b₁(S⁶)=b₂(S⁶)=b₃(S⁶)=0` and harmonic forms on a Riemannian product
   are tensor products of harmonic forms on the factors. This is a
   cheap, reusable pre-filter for future OB1 candidates (and for any
   other candidate parent action stated as a harmonic-form condition),
   and costs one line to check.

---

## Verification

- `python -m ruff check experiments/20260831-c119-bismut-ricci-flat-f1-test/`
  — **clean**.
- `python -m pytest tests/ -q` — **2524 passed, 4 skipped**, 379 s
  (no shared code was modified; run as a regression check only).
- All arithmetic exact (`sympy` Rationals and `sqrt(3)`); no floating
  point enters any verdict-bearing quantity.
- `S⁶` torsion **imported directly** from
  `experiments/20260708-dolan-casimir-g2su3/g2su3_H_element.py`
  (`build_T_table`), not re-typed — so the object tested is provably the
  frozen one (Gate 1, artifact identity).
- Independent internal cross-checks that all passed and would each have
  caught an error: `Rc − ¼H² ≡ Ric^t` (round111); `‖T‖² = (2/15)Scal`;
  `Ric = 5λ²` vs the project's `5/3`; `d(dω) = 0`; both nearly-Kähler
  structure equations; `dT` by two independent routes; `T = −λψ⁻`
  component-by-component; `Ric^{∇̄} = 2Scal/15` vs the computed defect.
- Environment recorded in `results_c119.json` (`provenance`): Python and
  sympy versions, platform, and the file-level source of every imported
  or cited input.
- Raw console output persisted to `run_output.txt`; machine-readable
  results to `results_c119.json`.
- **Not** self-certified: FL Step 8a skeptic pass is a separate, still-owed
  step.

## Reproduce

```
cd experiments/20260831-c119-bismut-ricci-flat-f1-test
python c119_bismut_ricci_flat_product_check.py
```

Expect: `equals_round111_Ric_t: True`, `rho` (S³) `= (2t-1)**(-2)`,
`rho` (S⁶) `= 5`, `agricola_matches_computed_defect: True`,
`T_equals_minus_lambda_psi_minus: True`, `dd_omega_is_zero_validity_test:
True`, `d_psi_plus_is_zero: True`, `route_A_dT_is_zero: False`,
`routes_proportional: True`, `T_is_co_closed: True`,
`cross_block_of_H_squared_is_zero_VERIFIED: True`,
`S6_block_roots_c6: []`, `harmonic_forces_H_zero: True`,
`any_invariant_H_satisfying_all_three: False`, `F1_pass: False`.

---

## Sources (every one tool-verified this round; none from model memory)

**External** — all arXiv IDs resolved and abstracts/text read this session:

| Ref | What was taken from it | How verified |
|---|---|---|
| **arXiv:2301.02335** — Lauret & Will, *Bismut Ricci flat generalized metrics on compact homogeneous spaces (incl. Corrigendum)* | The definition under test, **verbatim**: "(g,H), where g is a Riemannian metric and H a **closed** 3-form … is a fixed point of the generalized Ricci flow iff … H is g-harmonic and `ric(g)=¼H_g²`". Also the `G₁×G₂/ΔK` shape of their construction. | `mcp__arxiv__get_abstract` |
| **arXiv:2401.03332** — Gutiérrez, *Generalized Ricci flow on aligned homogeneous spaces* | Same definition, independently worded; asymptotic stability on `G₁×G₂/ΔK`. | `mcp__arxiv__get_abstract` |
| **arXiv:2608.25619** — Fusi, Lafuente & Stanfield, *Homogeneous Generalized Ricci flows II* (2026-08-26) | Dynamical stability is for **standard bi-invariant, Bismut-FLAT** metrics on compact simply-connected semisimple Lie groups; the same paper constructs **unstable** non-standard Bismut-flat examples. (Two corrections to the incoming characterization.) | `mcp__arxiv__get_abstract` |
| **arXiv:1601.04400** — Foscolo, *Deformation theory of nearly Kähler manifolds* | Eq. **(2.15)** read from the paper body: `dω = 3 Re Ω`, `d Im Ω = −2ω²`; and "nearly Kähler manifolds are Einstein … normalised so that `Scal = 30`". | `mcp__arxiv__download_paper` + `mcp__arxiv__search_paper_text` (in-body, §"SU(3)") |
| **arXiv:math/0403131** — Alexandrov, Friedrich & Schoemann, *Almost Hermitian 6-Manifolds Revisited* | "A Theorem of Kirichenko states that the torsion 3-form of the characteristic connection of a nearly Kähler manifold is parallel." | `mcp__arxiv__get_abstract` |
| **arXiv:math/0606705** — Agricola, *The Srní lectures on non-integrable geometries with torsion* | `‖(∇^g_X J)Y‖² = (Scal^g/30)[‖X‖²‖Y‖² − g(X,Y)² − g(X,JY)²]` (Gray); Kirichenko parallel torsion; **`Ric^{∇̄} = 2(Scal^g/15)g` for any 6-dim nearly-Kähler manifold**. | `WebFetch` on the ar5iv HTML — **secondary extraction**, see caveat 3; numerically re-confirmed independently in `PART 1` |

**Internal (this project)** — all read directly this round:

| File | What was used |
|---|---|
| `experiments/20260708-dolan-casimir-g2su3/g2su3_H_element.py` | `build_T_table()` — the frozen `S⁶` Ambrose-Singer torsion 3-form, **imported and executed**, not transcribed |
| `experiments/20260708-dolan-casimir-g2su3/decision.md` (≈ll. 1926-1929, 2121-2130) | `Ric(e_p,e_p) = 5/3`, `Scal = 10`, "triple-verified in Round 16"; the `radius²=3` normalization note |
| `experiments/20260717-round111-codex-item6-scalar-curvature-action/decision.md` | `Ric^t = 8t(1−t)δ`, `Scal(t) = 24t(1−t)`, `Scal_LC = 6` — the `S³` cross-check target |
| `experiments/20260717-round113-t-convention-reconciliation/claim.md` | `T^t = (2t−1)c·vol`, `c = 2`; `PARENT_ACTION_GATE.md` F3 resolved — cited, not re-derived |
| `PARENT_ACTION_GATE.md` | The 7-field gate; F1's pass criterion |
| `OPEN_BLOCKERS.md` OB1 | PARKED status, the four reopen conditions, the prior-attempt register (rounds 114-117, C107, C58, round115, round116) |
