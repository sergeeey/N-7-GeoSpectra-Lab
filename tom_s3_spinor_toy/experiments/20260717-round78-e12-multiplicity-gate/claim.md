# E12 (round78) — Claim: does the S³ torsion-crossing zero mode really have
# complex dimension 2, and if so, does the escape-route program survive it?

**Date:** 2026-07-17
**FL tier:** [x] Full (research claim; methodology per project CLAUDE.md; this
experiment was flagged by an external reviewer as potentially "the most
consequential finding of the day, possibly undermining the entire
torsion-escape-route program" — treated at correspondingly high rigor)
**Question type:** [x] descriptive [ ] predictive [ ] causal

Descriptive: for the torsion-deformed S³=SU(2)/{e} Dirac operator family `D^t`
(Agricola, arXiv:math/0202094 — same presentation as E2/E3/E7/E9/E9-followup/
E11), what is the EXACT complex dimension of `ker(D^t)` at the Cartan–Schouten
flat values `t=0` and `t=1` — is it 1 (as implicitly assumed by treating "the
zero mode" as a single physical state) or 2 (as E2's own claim.md line 73
already flags via the `(n+1)(n+2)` multiplicity formula at `n=0`) — and, given
`ker(D_full) = ker(D_{S3,t}) ⊗ ker(D_{S6,twisted})` for the decoupled
sum-of-squares product operator, what is the resulting total internal
zero-mode count across the 3 postulated triality channels?

## Stakes
**External-facing risk, internal-only artifact for now.** This experiment does
not modify `preprint.tex` or any existing experiment folder. But its subject —
whether the torsion-escape-route program (E2/E3/E7/E9/E9-followup) is
internally consistent — bears directly on whether that program could ever be
promoted to `preprint.tex`. Per the Stakes-check discipline, this is treated
as Standard-tier-or-above rigor regardless of its current internal-only status.

## Background (established, not re-derived here — see full citations in the script)
- E2 (`experiments/20260717-round67-e2-s3-torsion-deformation/claim.md`, line
  ~73): "'j=0 constant-spinor sector = n=0, one specific sigma, sector of the
  known ±(n+3/2) ladder' identification: [INFERRED] — justified by the
  multiplicity match (dim of constant-spinor space = dim(V_0)·dim(Δ_m) = 1·2 =
  2, which equals the project's own established multiplicity (n+1)(n+2)=2 at
  n=0 for ONE sign), but not independently cross-checked against a second
  source." **This is the exact passage this experiment interrogates.**
- E9 (`experiments/20260717-round73-e9-explicit-parallel-spinor/`): explicitly
  constructed the t=0 parallel spinor for e1=(1,0), e2=(0,1), AND a generic
  symbolic (a,b) — i.e. E9's OWN data already shows the full 2-dimensional
  space is ∇⁰-parallel, though E9's decision.md does not itself flag this as a
  "multiplicity problem."
- E9-followup/E10 (`experiments/20260717-round76-e9followup-right-invariant-frame/`):
  found an explicit t=1 parallel spinor `ψ(x)=ḡ(x)ψ₀` with `ψ₀=(a_,b_)` a
  GENERIC symbolic 2-vector (confirmed by reading the script:
  `psi0 = sp.Matrix([a_, b_])`), under the concrete `c0=-2` sign convention —
  i.e. the FULL 2-dimensional family is parallel there too, not a single
  spinor.
- E11 (`experiments/20260717-round77-su2lr-correspondence-test/`):
  tool-verified that `ψ⁽⁰⁾` (t=0) is an EXACT `SU(2)_L` singlet and a GENUINE
  `SU(2)_R` doublet (non-degenerate, checked at concrete θ); `ψ⁽¹⁾` (t=1,
  `c0=-2`) is the mirror (SU(2)_L doublet / SU(2)_R singlet).
- G74A (`experiments/20260621-g74a-lichnerowicz-gap/decision.md`): dim
  ker(D_{S⁶,twisted}) = 1 EXACTLY per triality channel (Lichnerowicz gap +
  G₂-Schur bound, both directions closed).
- `preprint.tex:292-298`: "the Dirac spinor on S³×S⁶ decomposes under
  SO(4)×G₂ into (rep_S3)⊗(rep_S6) pairs, with rep_S3 the **4-component** SO(4)
  spinor representation... Restricting to one generation, the 32 complex
  spinor components decompose into exactly the particle content of one SM
  generation." This is a DIFFERENT object (the full, untwisted Levi-Civita
  spinor-bundle fiber, applied identically at every KK level per G7's own
  script) from `ker(D_{S3,t=0 or 1})`, which this experiment shows is a single
  2-dimensional SU(2) doublet, not the full 4-dimensional SO(4) spinor.

## Claim (falsifiable, frozen verbatim per task instructions)

**"Torsion crossing at t=0 or t=1 gives exactly one physical internal mode per
S⁶ zero mode."**

## Preliminary expectation (stated honestly, BEFORE running anything further)

Without additional projection conditions, `dim_C ker(D_{S3,t=0 or 1}) = 2`, so
this claim preliminarily appears **FALSE**.

## PASS / FAIL / OPEN criteria (pre-registered)

| Verdict | Condition |
|---|---|
| **PASS** | A physically-motivated projection is found (Majorana/reality condition, an existing orbifold quotient, or a pre-existing gauge-multiplet-counting convention ALREADY used consistently elsewhere in this project) that leaves exactly one physical mode per channel, NOT invented ad hoc to force this answer |
| **FAIL** | `dim_C ker(D_{S3,t=0 or 1}) = 2` is confirmed by direct, tool-verified computation, AND no such natural projection is found — multiplicity 2 stands |
| **OPEN** | The core kernel-dimension computation itself does not resolve cleanly (e.g. sign/convention ambiguity blocks a definite answer) |

## Method (see `e12_multiplicity_gate.py` for full implementation)

1. **Section A** — independent derivation of the `(n+1)(n+2)` multiplicity via
   Peter–Weyl / SU(2) representation theory (not merely trusting E2's own
   citation): build the round-S³ Dirac operator's action on each Peter–Weyl
   block (labelled by SU(2) spin `j`), using standard angular-momentum
   matrices `J_i^{(j)}`, calibrated so `X_i^{(1/2)} ≡ Z_i = i·σ_i` exactly
   (verified). Diagonalize `D^{1/2}|_{V_j⊗ℂ²} = Σ_i X_i^{(j)}⊗Z_i + (3/2)I`.
2. **Section B** — self-contained (not merely citing E9/E10), exact symbolic
   re-verification that the FULL 2-dimensional space of constant spinors is
   ∇⁰-parallel at t=0 (generic `(a,b)`, not spot-checked basis vectors), and
   that the full 2-dimensional family `ψ(x)=ḡ(x)ψ₀` (generic `ψ₀=(a_,b_)`) is
   ∇¹-parallel in the right-invariant frame under `c0=-2`.
3. **Section C** — toy explicit verification of the tensor-product kernel
   identity `ker(A²⊗I+I⊗B²) = ker(A)⊗ker(B)` for a concrete 2×2+2×2 example,
   via actual nullspace computation (not merely asserting the general
   positive-semi-definite argument).
4. **Section D** — total internal zero-mode count:
   `dim ker(D_{S3,t}) × dim ker(D_{S6,twisted}) × 3 channels`.
5. **Section E** — investigate (NOT force) possible reductions: search
   `preprint.tex` for Majorana/reality/Weyl conditions; reuse E11's SU(2)
   doublet finding and check it against this project's OWN existing
   "32 complex components = one generation" convention (`preprint.tex:292-298`,
   `G7`'s own script); search for any existing orbifold/projection
   construction that could apply to the S³ factor specifically (as opposed to
   G27/G30/G31's S⁶- or adjoint-bundle-only null results).

## Kill criterion

If Section A's `n=0` level does NOT reproduce eigenvalue `+3/2` with
multiplicity 2 (independently of E2's citation), OR Section B's generic
`(a,b)`/`(a_,b_)` checks do NOT hold for the FULL 2-parameter family (only a
proper subspace), the core multiplicity-2 claim would be **FALSIFIED** (i.e.
the preliminary expectation would be WRONG, and the frozen claim might
actually hold). Kill signal:
`verdict.core_multiplicity_2_confirmed_at_t0 == False`.

## Assumptions (status)

| Assumption | Status |
|---|---|
| `D_full² = D_{S3,t}²⊗I + I⊗D_{S6,twisted}²` (exact decoupling for the torsion-deformed S³ factor) | [INFERRED, inherited from E2's own claim.md caveat #1] — NOT independently re-verified for the torsion-deformed case in this experiment either; this experiment assumes it holds (as E2/E3 already do) purely to compute WHAT THE CONSEQUENCE WOULD BE if it holds — if it does NOT hold, the whole premise of E2/E3's candidate mechanism is separately in question, unaffected by this experiment's own finding |
| G74A's dim ker(D_{S6,twisted}) = 1 per channel | [VERIFIED-tool, PROMOTE, inherited from G74A, not re-derived here] |
| The "32-state, one generation" convention (`preprint.tex:292-298`) and `ker(D_{S3,t})` are talking about the SAME S3-side object | **[OPEN, explicitly NOT resolved here]** — Section E argues they are likely different objects (full untwisted spinor fiber vs. a specific connection's kernel), but this project has never reconciled them explicitly |
| Standard Peter–Weyl / Lie-theory facts used in Section A | [DOCS] — standard representation theory, application to this specific operator is [VERIFIED-tool] here |

## What this does NOT mean

1. Does **not** resolve H1c (which of t=0/t=1, if either, is physically
   selected) — untouched, unaffected either way by this experiment's finding.
2. Does **not** verify the generalized product-decoupling formula
   `D_full² = D_{S3,t}²⊗I + I⊗D_{S6,twisted}²` for the torsion-deformed case —
   this remains E2's own [INFERRED, NOT independently literature-verified]
   assumption; this experiment computes the CONSEQUENCE of that formula, not
   its own validity.
3. Does **not** claim the SU(2)-doublet structure (E11) is irrelevant or
   uninteresting — it is a genuine, tool-verified structural fact; this
   experiment argues only that it does not, BY ITSELF, license reducing the
   multiplicity from 2 to 1 without further work reconciling it against this
   project's own existing 32-state generation-counting convention.
4. Does **not** claim Section A's higher-`n` (n≥1) mismatch invalidates
   anything upstream — that mismatch is reported honestly as an open
   side-finding about extending Agricola's shift-operator formula beyond
   constant spinors; it is orthogonal to this experiment's actual question
   (which concerns only n=0, i.e. t=0,1).

## Check
`python e12_multiplicity_gate.py` →
`verdict.core_multiplicity_2_confirmed_at_t0 == true`,
`verdict.multiplicity_2_confirmed_at_t1_under_c0 == true`,
`verdict.natural_physical_reduction_found == false`,
`verdict.label == "FAIL_MULTIPLICITY_2_CONFIRMED__NO_NATURAL_PROJECTION_FOUND"`.
