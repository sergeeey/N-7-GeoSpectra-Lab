# Round65-SU3T2-Killing-Spinor-Test Decision — PROMOTE (second data point for the Round 59 pearl)

**Date:** 2026-07-15
**Verdict: PROMOTE** — Round 59's two-line trivial-block rank-forcing argument
(Killing eigenvalue nonzero + Term2-analog vanishes) goes through, re-derived
independently for `SU(3)/T²`'s own Killing-spinor data and its own `T²`
representation theory, per claim.md's kill-criterion table row 1.

---

## Step 1 — does `SU(3)/T²` admit a source-stated Killing spinor?

**Yes, but not from AHL2023.** Two sources checked, one excluded, one used:

1. **`Agricola_Hofmann_Lawn_2023_invariant_spinors.pdf` (AHL2023) — CONFIRMED
   OUT OF SCOPE**, exactly as the risk warning predicted. Full-text search
   (pymupdf) for `T^2`, `flag manifold`, `SU(3)/T`, `torus`, `U(1)xU(1)`
   returns **zero hits** anywhere in the 53-page paper. The Table of
   Contents (read directly, p.1-2) confirms the paper's actual scope: it
   classifies invariant spinors on **nine homogeneous presentations of the
   sphere `Sⁿ`** (title: "Invariant spinors on homogeneous spheres"; §5
   "Exceptional Spheres" covers only `S⁶=G₂/SU(3)`, `S⁷=Spin(7)/G₂`,
   `S¹⁵=Spin(9)/Spin(7)`). `SU(3)/T²` is the flag manifold `F₁,₂,₃` — not a
   sphere, never mentioned. This confirms the exact Round-64-symmetric
   failure mode this round was designed to test for: AHL2023 "looks general"
   (classifies Killing spinors on homogeneous spaces) but its actual scope
   is spheres only.

2. **`Charbonneau_Harland_2016_NK_instantons.pdf` (CH2016) — DOES cover
   `SU(3)/T²` directly, with an explicit, source-stated Killing constant.**
   §4 (p.11-12 of the PDF, just before eq. numbering restarts at the section):
   > "There are precisely four homogeneous nearly Kähler six-manifolds:
   > `S⁶ = G₂/SU(3)`, `S³×S³ = SU(2)³/SU(2)`, `CP³ = Sp(2)/Sp(1)×U(1)`,
   > `F₁,₂,₃ = SU(3)/U(1)²`. In all four cases, the nearly Kähler metric on
   > `G/H` is induced from a multiple of the Cartan–Killing form... the
   > metric normalised as in Section 2 is induced from [`B(X,Y) =
   > −1/12·Tr_g(ad(X)ad(Y))`]."
   §2 (p.3) defines nearly-Kähler via the real Killing spinor equation
   `∇ᴸᶜ_X ψ = λ X·ψ` with `λ` a **nonzero** real constant by definition, and
   fixes the convention `λ = 1/2` "for simplicity" (metric-scale choice).
   §2 also proves generally (not S⁶-specifically) that `Vol_g·ψ` is a second
   Killing spinor with eigenvalue `−λ`. Because §4 states the SAME
   `B(X,Y)`-normalised metric (hence the SAME `λ=1/2` convention) applies
   "in all four cases" — including `F₁,₂,₃ = SU(3)/U(1)²` — this is a
   direct, source-stated, nonzero Killing eigenvalue for `SU(3)/T²`, not
   something requiring a fresh derivation. **Step 1 succeeds.**

---

## Step 2 — re-derived Term2-analog check for `T²=U(1)×U(1)` isotropy

### What generalizes without new derivation (isotropy-independent facts)

CH2016 §2 (p.3-4, eq. (4)-(6), Lemma 2) builds the entire spinor/SU(3)-structure
machinery (`S ≅ Λ⁰V⊕Λ¹V⊕Λ⁶V`, the forms `P,Q`, the complex structure `J`)
from an **abstract** Killing spinor `ψ` on a general `(V,g)` — this
construction never references a specific isotropy group. Consequently, the
following hold for **any** homogeneous nearly-Kähler 6-manifold, not just
`S⁶`:
- The two Killing spinors `ψ, Vol_g·ψ` correspond to `1` and the
  "top-wedge" analog of `y₁₂₃` in the `Σ=Λ*(m^{1,0})` model (`m^{1,0}` = the
  `(1,0)`-part of the complexified isotropy representation `m_C`).
- The top wedge (`Λ³(m^{1,0})`) is automatically isotropy-invariant, because
  `m^{1,0} ⊂ su(3)_C` as a rank-3 representation (det = 1 forced by
  `SU(3)`-structure) — **verified explicitly for `T²` below**, not merely
  asserted.
- Clifford multiplication by a single generator on the top wedge
  (`Λ³ → Λ²` only, since `Λ⁴(C³)=0`) is pure exterior-algebra, independent
  of which group acts on `L'`.
- Hence `Term1 = ⟨w, D(top-wedge)⊗1⟩ = (nonzero constant)·w` and
  `Term2 = Σᵢ eᵢ⊗∇ᵢ(v_b)` **structurally lands entirely inside
  `Λ²(m^{1,0})⊗Λ²(m^{1,0})`**, for ANY isotropy group `H ⊂ SU(3)`.

**The one part that is genuinely isotropy-dependent, and is NOT assumed to
transfer, is whether `Λ²(m^{1,0})⊗Λ²(m^{1,0})` contains an `H`-invariant
(target-reachable) component.** For `SU(3)` isotropy (Round 59) this was the
Clebsch-Gordan fact `3⊗3` has no singlet. For `T²` isotropy this becomes:
does `Λ²(m^{1,0})⊗Λ²(m^{1,0})` contain a weight-`(0,0)` term? **This is the
computation this round actually performed, from CH2016's own stated data.**

### The computation (script: `round65_t2_weight_check.py`, output: `run_output.txt`)

Primary-source inputs, transcribed directly from CH2016 §4 (p.21-22):
- Cartan generators of `h = t² = u(1)⊕u(1)`: `H1 = i·diag(1,−1,0)`,
  `H2 = i·diag(0,1,−1)`.
- eq. (35): "A basis for `m^{1,0}_C` is given by" `C1, C2, C3` — transcribed
  exactly as the 3×3 elementary matrices printed in the PDF, confirmed by
  the script (Step 0) to equal `E₁₂, E₂₃, E₃₁`.
- The paper's own summary statement of the full `m*_C` weight decomposition
  (`V(2,−1)⊕V(−1,2)⊕V(−1,−1)⊕V(−2,1)⊕V(1,−2)⊕V(1,1)`) is used **only as an
  independent cross-check**, not as an input.

Script results (full output in `run_output.txt`):
1. Weights of `E₁₂,E₂₃,E₃₁` computed directly via `ad(H)(Eᵢⱼ)=(Hᵢ−Hⱼ)Eᵢⱼ`:
   `(2,−1), (−1,2), (−1,−1)`. The full 6-root-vector weight set computed
   this way **matches CH2016's own stated `m*_C` list exactly** (`match: True`)
   — an independent confirmation the transcription and Cartan-generator
   convention are correct.
2. `m^{1,0} = {(2,−1),(−1,2),(−1,−1)}`; sum `= (0,0)` — confirms the top
   wedge `Λ³(m^{1,0})` is `T²`-invariant, as required (not assumed).
3. `Λ²(m^{1,0}) = {(1,1),(1,−2),(−2,1)}` (pairwise sums).
4. `Σ_even = Λ⁰∪Λ² `(4 weights), `Σ_odd = Λ¹∪Λ³` (4 weights).
5. **Domain** (`Σ_odd⊗Σ_even` weight-`(0,0)` pairs): **dim = 4** (including
   `v_b = (top-wedge)⊗(1)`, confirmed present). This is larger than Round
   59's `SU(3)` domain (dim 2) — a genuine structural consequence of abelian
   isotropy having many more accidental zero-weight coincidences than a
   non-abelian group's Clebsch-Gordan rules allow. **This does not weaken
   the argument**: since the target is 1-dimensional, the rank is capped at
   1 regardless of domain size — only whether `v_b`'s image is nonzero
   matters.
6. **Target** (`Σ_even⊗Σ_even` weight-`(0,0)` pairs): **dim = 1** (only
   `1⊗1`), matching Round 59's `SU(3)` target dimension exactly.
7. **`Λ²(m^{1,0})⊗Λ²(m^{1,0})` weight-`(0,0)` check: zero matches found**
   (exhaustive check over all 9 ordered pairs of the 3-element weight set).
   This is the `T²` analog of "`3⊗3` has no `SU(3)` singlet" — computed
   fresh from `T²` charges, not copy-pasted.

**Conclusion of the computation:** `Term2`'s image is structurally confined
to `Λ²⊗Λ²`, which has no weight-`(0,0)` component — so `⟨w, Term2(v_b)⟩ = 0`
is forced by `T²` weight arithmetic, exactly parallel to (but independently
computed from) Round 59's `SU(3)` rep-theory argument. Combined with Term1
`≠ 0` (Step 1), `b = ⟨w, D⁺v_b⟩ = Term1 ≠ 0`, and since the target is
1-dimensional, `rank(D⁺|trivial-block) = 1` on `SU(3)/T²`, by the same
two-line argument as `S⁶`.

---

## Kill criterion classification

Per claim.md's pre-registered table: **PROMOTE** —
"Killing eigenvalue nonzero AND `Term2`-analog vanishes by an
honestly-rechecked `T²` rep-theory argument." Both conditions are met, with
citations and a from-scratch, script-verified weight computation (not an
assumption that the `SU(3)` result transfers).

---

## Pre-answered skeptic concerns (`[SKEPTIC-PRE-ANSWERED]`, in lieu of a
full Step 8a — this is a Standard-tier, one-session probe per claim.md, not
Full-Ladder; concerns anticipated and addressed inline rather than via a
separate agent call)

| Concern | Response |
|---|---|
| Is `m^{1,0}_C = {E₁₂,E₂₃,E₃₁}` (eq. 35) really the right object, or does CH2016's own 3-symmetry definition of `J` (via `J=(2s+1)/√3`, a DIFFERENT passage) pick out a different eigenspace? | Used the paper's own **explicitly stated** eq.(35) basis directly (their own claimed answer), verified by transcription (Step 0) and cross-checked the resulting weight set against the paper's own independently-stated `m*_C` list (Step 1, exact match) — two independent confirmations, no reliance on re-deriving the 3-symmetry sign convention myself. |
| Domain dimension (4) is larger than Round 59's (2) — does this signal something is wrong? | No: the rank-forcing argument only needs the TARGET to be 1-dimensional (verified, dim=1) and `v_b`'s image to be nonzero — domain size is irrelevant to this specific claim (it would matter for a full-rank-of-the-whole-block claim, which this round does not attempt). |
| Is "`Term2` structurally confined to `Λ²⊗Λ²`" really isotropy-independent, or specific to `S⁶`'s Nomizu-connection formula? | It is pure Clifford/exterior-algebra: Clifford multiplication by one generator changes `Λ`-degree by exactly `±1`, and `Λ⁴(C³)=0`, so acting on the top wedge (`Λ³`) can only produce `Λ²`. This depends only on `dim_C L' = 3`, never on which group acts on `L'`. CH2016 §2 (eq. 4-6, Lemma 2) independently confirms the whole `P,Q`/spinor-module construction is built from an abstract Killing spinor on a general `(V,g)`, with no isotropy-group input. |
| Is `Term1 ≠ 0` actually established, or just "plausible by NK definition"? | Established via CH2016's own general derivation (§2): `ψ, Vol·ψ` are Killing spinors with eigenvalues `+λ,−λ`; combined with the Clifford-algebra fact `Vol` swaps `Λ⁰↔Λ³` and `Σeᵢ²=−n`, this forces `D(top-wedge) = −nλ·(Λ⁰ generator)`, nonzero exactly because `λ≠0` is part of the definition of nearly-Kähler, and CH2016 §4 explicitly states `SU(3)/U(1)²` carries the SAME nonzero-`λ` metric convention as the other three spaces. |

---

## What this does NOT mean (carried from claim.md, unchanged)

- This PROMOTE verdict does **NOT** close the Universality open problem — it
  is one more data point (**2 of 4** Butruille spaces checked: `S⁶`, now
  `SU(3)/T²`), not a full generalization proof, and does not touch L4A's own
  still-open norm-bound tension.
- Does **NOT** commit to checking the remaining two Butruille spaces
  (`CP³` already ILL-POSED via a *different* route in Round 64 — that route
  concerned reusing CH2016's instanton-deformation Weitzenböck formulas for
  a different mechanism (L4A), not this round's Killing-spinor trivial-block
  mechanism, so `CP³` is NOT thereby excluded from this specific mechanism;
  `S³×S³` untested) regardless of this round's outcome.
- Does **NOT** establish that the FULL 4-dimensional `T²`-invariant domain
  has any particular total rank — only that the specific `v_b` vector maps
  to a nonzero multiple of the (1-dimensional) target, which alone forces
  `rank ≥ 1` and, since the target is 1-dimensional, exactly `rank = 1`.
- Does **NOT** mean the mechanism is proven universal for *arbitrary*
  isotropy groups — the `Λ²⊗Λ²`-no-singlet / no-zero-weight condition was
  verified for `SU(3)` (Round 59) and `T²` (this round) specifically; a
  future isotropy group (e.g. `Sp(1)×U(1)` for `CP³`, or `SU(2)` for
  `S³×S³`) would need its own fresh check, exactly as this round's own
  premise required.

---

## Recommendation (not applied here, per task scope)

A pearl_registry update recording this confirmation on a second,
structurally different (abelian) isotropy group would be a natural
follow-up — left to the orchestrator, per the explicit instruction not to
touch anything beyond `decision.md` and the supporting script this round.

---

## Files

- `claim.md` — frozen before this round's computation.
- `round65_t2_weight_check.py` — from-scratch `T²`-weight verification
  script (transcribes CH2016 eq.35 + Cartan generators, computes weights,
  cross-checks against CH2016's own stated `m*_C` list, builds `Σ_odd`,
  `Σ_even`, domain/target invariant dimensions, and the `Λ²⊗Λ²` no-zero-weight
  check).
- `run_output.txt` — actual run output of the script (all numbers in this
  decision trace to this file, none hand-typed independently of it).
