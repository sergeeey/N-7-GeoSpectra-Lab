# Round64-Universality-CP3-Probe Decision

**Date:** 2026-07-15
**Verdict: ILL-POSED** — the probe itself cannot be executed as scoped; the
needed object is not defined by the cited source, and independent evidence
(full-text re-read, not Round 51's summary) suggests it may not have a
well-defined analog on CP³ at all within Charbonneau-Harland's framework.

---

## What was done

Charbonneau-Harland 2016 ("Deformations of nearly Kähler instantons",
arXiv:1510.07720v2) was re-read **in full** directly from the PDF
(`Charbonneau_Harland_2016_NK_instantons.pdf`), independently of Round 51's
summary, per claim.md's Estimand ("re-read directly by the executing agent,
not from memory or from Round 51's summary"). No script was run — this is a
literature-comprehension probe with a documented STOP condition, matching
the kill criterion's own "no computation to force" language.

## What CH2016 actually contains (independent confirmation)

1. **The paper's object of study is instanton *rigidity/deformation
   theory*, not fermion zero-mode counting.** Every substantive result
   (Theorem 1, Theorem 2, Theorem 3, Proposition 7) concerns the space of
   solutions to the *linearised instanton equation* `d^A ε · ψ = 0`,
   `d^A * ε = 0` for a connection perturbation `ε` — i.e. the moduli-space
   dimension of the canonical connection as an instanton. This is
   identified (Proposition 2) with the kernel of a Dirac-type operator
   `D^{t,A}` acting on `ε · ψ`, but the *bundle* `ε` lives in is always
   `Ad_P ⊗ T*M` (a Lie-algebra-valued 1-form) — never a spinor bundle in
   its own right.

2. **The general Weitzenböck/Schrödinger-Lichnerowicz formula (Proposition
   3) is representation-agnostic in the auxiliary bundle `E`** — `η ∈
   Γ(EM ⊗ SM)` for "some representation `E` of `H`" is the stated
   generality. This is the one place the paper's machinery is *formally*
   broad enough to look reusable.

3. **But every concrete instantiation in the paper sets `E` to an avatar of
   the adjoint bundle, never the fundamental/tangent representation "3".**
   Concretely, `E = h_C` (isotropy Lie algebra, Proposition 7 / Theorem 3
   "structure group H" column) or `E = su(3)_C` (Theorem 3 "structure
   group SU(3)" column). For `S⁶ = G₂/SU(3)` these two cases coincide
   (`H = SU(3)` exactly), which is presumably why Round 48's original
   scoping mistook the machinery for directly portable — the coincidence
   is `S⁶`-specific and does **not** hold for `CP³ = Sp(2)/(Sp(1)×U(1))`,
   where `H = Sp(1)×U(1)` is a proper rank-2 subgroup of the rank-2 `SU(3)`
   structure group, and the paper explicitly treats "structure group H" and
   "structure group SU(3)" as two *different* deformation problems with
   different answers (5-dim `W^R_{(1,0)}` vs. `W_{(1,0)} ⊕ 2𝔤`).

4. **This project's own L4A object is a different Dirac operator on a
   different bundle.** `preprint.tex`'s Weitzenböck identity
   `(D_{S⁶}⊗S⁻)² = ∇*∇ + R/4 + F_{S⁻}` twists the *spinor* Dirac operator
   by an auxiliary bundle `S⁻` whose curvature endomorphism `F_{S⁻}` is
   bounded "via SU(3) Casimir for **3**" — i.e. the twisting representation
   is the *fundamental* representation of the isotropy `SU(3)`, not its
   adjoint. `S⁻` itself is this project's own construction (a chirality
   half of the ambient `S⁺⊗S⁻` fibre built from the octonionic/triality
   embedding `G₂ ⊂ Spin(7) ⊂ Spin(8)` specific to `S⁶`, per the
   `20260708-dolan-casimir-g2su3` and `G73`/`G74A` experiments) — CH2016
   never constructs or needs any such object, because instanton
   deformation theory has no zero-mode/generation-counting interpretation.
   The `8/45` ratio's own citation in `preprint.tex` is to **Agricola
   2002** (Kostant-Parthasarathy on `G₂/SU(3)`), **not** to CH2016 — CH2016
   was never the source of this project's own `S⁶` number in the first
   place; it was flagged by Round 48/51 only as a *candidate reusable tool*
   for the CP³ generalization, a candidacy this round tests directly.

5. **The `S⁻`-analog for CP³ is not just "missing a formula" — it may not
   have a well-defined referent at all inside CH2016's framework, and quite
   possibly not inside this project's own framework either.** This
   project's `S⁻` traces its existence to the triality automorphism
   `ℤ₃ ⊂ Aut(SO(8))` and the `G₂`-fixed structure specific to `S⁶`
   (confirmed elsewhere in this project: `G67`, `G68`, `G73` — the
   three-channel Dirac/triality construction). `Sp(2) = Sp(2)`
   (quaternionic symplectic group) has no analogous relationship to
   `Spin(8)` triality that would license an analogous three-channel
   spinor construction on `CP³`. Whether *some* other well-defined analog
   of `S⁻` exists for `CP³` is a genuinely open representation-theoretic
   question this probe is explicitly not licensed to answer (per claim.md's
   escape route: "do NOT improvise a derivation").

## Kill criterion classification

Per claim.md's pre-registered table:

> "The `S^+⊗S^-`-analog bundle on CP³ is not even the right object (CH2016
> studies instanton deformations of the CANONICAL CONNECTION on the
> ADJOINT bundle, not a spinor kernel problem, per Round 51's own T3
> finding)" → **ILL-POSED**

This is confirmed, not merely repeated from Round 51: the full-text re-read
found zero instances anywhere in CH2016 of the fundamental/tangent
representation `"3"` used as the twisting bundle `E` for a Dirac-kernel
computation. Every computed number in the paper (Proposition 7's
eigenvalue tables, Theorem 3's representation table) answers "does the
canonical connection admit infinitesimal deformations as an instanton" —
a structurally different question from "does the twisted spinor Dirac
operator on `S⁺⊗S⁻` have a kernel of dimension 3." Round 51's T3 finding
(different SU(3)-representations, `(1,0)` vs `(1,1)`) is the *representation
mismatch* symptom; this round's finding is the *question mismatch* root
cause — CH2016 is a deformation-theory paper, and no substitution of `E`
converts a deformation-space computation into a fermion zero-mode count.

## What this round did NOT do (per claim.md's explicit scope limits)

- Did not attempt to define a bespoke `S⁻`-analog for CP³ from first
  principles — that would be exactly the "improvised derivation" the kill
  criterion forbids.
- Did not compute any ratio, bound, or spectrum for CP³. There is no
  number to report; `‖F_{S^-}‖_F/(R/4)` is undefined for CP³ absent a
  definition of `S⁻`.
- Did not extend into a second session. This is a one-session probe,
  closed here.

## Partial value recovered (procedural pearl, not a physics result)

One universal fact, independently confirmed from CH2016's Proposition 1
and the surrounding text, is directly transferable and does not require
any new derivation: the scalar curvature `R = 30/ρ²` (equivalently
`Ric¹ = 4g` for the canonical connection, in the `λ = 1/2` convention)
holds for **any** round nearly-Kähler 6-manifold, not just `S⁶` — CH2016
states this generally before specializing to the four homogeneous spaces.
This confirms the `R = 30/ρ6²` half of the `preprint.tex` L4A ratio is
NOT S⁶-specific; only the `F_{S^-}` half is. This is a minor, already-low
priority observation (the numerator, not the denominator, was always the
open problem) and does not change Round 51's cost re-estimate or this
round's ILL-POSED verdict.

## What this does NOT mean (carried from claim.md, unchanged)

- Does NOT mean a PROMOTE verdict here proves the L4 mechanism generalizes
  to CP³ — moot, no PROMOTE was reached.
- Does NOT mean this ILL-POSED verdict closes Universality for ALL nearly
  Kähler spaces — only for the specific route this probe tested (reusing
  CH2016's adjoint-bundle machinery for CP³ specifically).
- Does NOT commit to redoing the full L4A/L4B derivation for CP³ regardless
  of outcome — Round 51's cost re-estimate (priority ~0.3–0.5, lowest on
  the shortlist) stands unchanged and is, if anything, reinforced: this
  probe found the cheapest available route is not just expensive but
  possibly not even well-posed without first resolving whether CP³ admits
  any analog of this project's own triality-built `S⁻` construction at
  all — a strictly harder prerequisite than Round 51 had scoped.

## Kill Analysis (OSA — required for a NULL-adjacent verdict)

**What was killed:** The specific hope that CH2016's *directly stated*
Casimir/branching formulas could be substituted, with no new derivation,
into this project's own L4A construction to produce a CP³ number. This
hope is killed for the reason Round 51 already gave (adjoint-bundle vs.
tangent-bundle representation mismatch) and reinforced by a new reason
this round: the twisting bundle CH2016 would need to supply (`E =`
fundamental "3") is never instantiated anywhere in the paper, because the
paper's question is categorically different from a fermion zero-mode
count.

**What was NOT killed:**
- Round 51's own extracted value (reusable Casimir eigenvalue formulas
  for `𝔤₂, 𝔰𝔲(3), 𝔰𝔲(2), 𝔰𝔭(2), 𝔲(1)⊕𝔲(1)`) remains valid and reusable
  *if* a future session independently derives what plays the role of `S⁻`
  on CP³ — this round only shows CH2016 cannot supply that definition
  ready-made.
- The universal `R = 30/ρ²` fact (this round's own finding, see above).
- Round 51's cost re-estimate (priority ~0.3–0.5) — unchanged, arguably
  should be revised downward further given the new prerequisite surfaced
  here, but that revision is out of scope for this probe (no new priority
  arithmetic was run).

**Relaxation Map:** Not applicable in the usual sense — this is not a
hypothesis-revision NULL, it is a probe that correctly identified its own
target as ill-posed before any computation was attempted. The only
"relaxation" available is: define `S⁻` for CP³ independently (a
multi-round project Round 51 already correctly declined to greenlight at
this priority level), which is explicitly out of scope here.

## Files

- `claim.md` — this round's FL Standard-tier artifact, frozen before this
  decision was written.
- No script — per the kill criterion's own allowance ("no computation to
  force" for ILL-POSED/INCOMPLETE-MACHINERY verdicts), and consistent with
  Round 51's own precedent (pure literature-reading, no numeric artifact).
