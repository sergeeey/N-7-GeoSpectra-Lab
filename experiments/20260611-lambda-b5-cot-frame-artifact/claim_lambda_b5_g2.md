# LAMBDA-B5-G2: cot(2α) Frame-Artifact Hypothesis

**Date pre-registered:** 2026-06-11 (design only — implementation NOT started)
**Tier:** FL Standard (mathematical/structural claim, sympy verification)
**Question type:** [x] descriptive (structural)  [ ] predictive  [ ] causal
**Status:** research_only — no physical promotion
**Parent gate:** LAMBDA-B5-G0 `STRUCTURAL_SPLIT_REQUIRED` (experiments/20260611-lambda-b5-structural-split/)

---

## Claim (pre-registered, written before code runs)

**The cot(2α) term appearing in the S³ Dirac operator in Hopf coordinates is a
spin-connection frame artifact, not a coordinate-independent obstruction.**

Specifically:

1. In the Hopf coframe `(e¹=dα, e² =cosα dθ, e³=sinα dφ)`, the torsion-free
   spin connection has components:
   ```
   ω₁₂ = +tanα  (coefficient of e² in ω^1_2)
   ω₁₃ = −cotα  (coefficient of e³ in ω^1_3)
   ω₂₃ =  0
   ```

2. Their combination entering the Dirac term `γ^a ω_a` gives:
   ```
   tanα − cotα = −2cot(2α)     (exact algebraic identity)
   ```
   This is the source of the cot(2α) term in Tom's S³ operator.

3. In the left-invariant (Maurer-Cartan) frame `{σ₁, σ₂, σ₃}` on S³ = SU(2),
   the spin connection has **constant** coefficients:
   ```
   ω_ij = ε_ijk σ^k / ρ        (ρ = radius, structure constants of su(2))
   ```
   No cot(2α) appears. The Dirac operator in the invariant frame contains no
   frame-dependent trigonometric singularities.

**Candidate answer to Tom's Q2** (from 2026-06-09 message):
> *"cot(2α) — expected to vanish with correct SO(4) spinor basis?"*

---

## Motivation (from LAMBDA-B5-G0, section 5)

G0 identified the Hopf-frame spin connection as `[HYPOTHESIS]` in the bonus
finding (g0_structural_split_report.md §5). The invariant one-forms ξ̃/ξ̃′ in the
structural split have the geometric form `ω_ij = ε_ijk σ_k/ρ` in the invariant
frame (G0 claim.md §4: λ_geom may be canonical IF V_ω identified with geometric
spin connection term). G2 verifies this identification is self-consistent by
explicitly comparing the two frame representations.

This is falsifiable and decisive:
- PASS → cot(2α) is a frame artifact; invariant Dirac is "clean"
- FAIL → cot(2α) is coordinate-independent; Tom's Q2 has no clean answer here

---

## Estimand

*Population:* S³ of radius ρ = 1 in two coordinate systems:
  (a) Hopf diagonal coordinates: ds² = dα² + cos²α dθ² + sin²α dφ²
  (b) Left-invariant frame: σ-basis satisfying dσᵢ = −ε_ijk σⱼ ∧ σₖ

*Endpoint:* Spin connection components in each frame, computed via Cartan's
torsion-free structure equation `de^a + ω^a_b ∧ e^b = 0`.

*Summary measure:* presence/absence of cot(2α) (or tanα, cotα) in spin
connection coefficients, and whether `tanα − cotα = −2cot(2α)` accounts for
the discrepancy between frames.

*MCID:* Any nonzero cot(2α) term surviving in the invariant frame counts as
FAIL. Any nonzero cotα or tanα term in the Hopf frame, combining to −2cot(2α),
counts as PASS (together with showing the invariant frame is cot-free).

---

## Verification Plan (3 independent checks)

### C1 — Algebraic identity (trivial, sympy)

```
tan(α) − cot(α) = sin(α)/cos(α) − cos(α)/sin(α) = −2cos(2α)/sin(2α) = −2cot(2α)
```

Verify symbolically: `sp.simplify(sp.tan(a) - sp.cot(a) + 2*sp.cot(2*a)) == 0`

### C2 — Hopf-frame spin connection (Cartan structure equations, sympy)

Given the Hopf vielbein:
```
e¹ = dα,   e² = cosα dθ,   e³ = sinα dφ
```
Compute `de^a`:
```
de¹ = 0
de² = −sinα dα ∧ dθ = −tanα (e¹ ∧ e²)
de³ = +cosα dα ∧ dφ = +cotα (e¹ ∧ e³)
```
Torsion-free + antisymmetry `ω_{ab} = −ω_{ba}` → unique solution:
```
ω₁₂ = +tanα e²,   ω₁₃ = −cotα e³,   ω₂₃ = 0
```
Verify: substitute back into `de^a + ω^a_b ∧ e^b = 0` → all components zero.

### C3 — Invariant-frame spin connection (Maurer-Cartan, sympy)

Left-invariant forms σᵢ on S³ satisfy: `dσᵢ = −ε_ijk σⱼ ∧ σₖ`

In terms of Hopf coordinates:
```
σ¹ = cosα cosθ dθ − sinα cosθ dφ + sinθ dα    (or the standard SU(2) lift)
```
Torsion-free in this frame gives `ω_ij = ε_ijk σ^k` (constant coefficients per
basis form, no α-dependence in the structure).

Verify: compute spin connection in σ-basis, confirm all components are constant
multiples of σ^k (no tanα, cotα, or cot(2α)).

---

## Pre-registered Verdict Rules

```
PASS (frame artifact confirmed):
  C1 identity holds [expected: trivial]
  AND C2: ω₁₂ = tanα e², ω₁₃ = −cotα e³, ω₂₃ = 0  [torsion-free, no free parameters]
  AND C3: invariant-frame spin connection = constant × σ^k (no trigonometric singularities)
  → Finding: "cot(2α) in Hopf frame is tanα − cotα frame artifact; clean in invariant frame"
  → item40 and λ_geom picture: no change (this answers Tom Q2 structurally)

PARTIAL (ambiguous):
  C1 and C2 hold, but C3 cannot be fully simplified (coordinate transform too complex)
  → Record as HYPOTHESIS_SUPPORTED but not VERIFIED; note what remains open

FAIL (cot(2α) is coordinate-independent):
  C3: invariant-frame connection retains non-constant trigonometric coefficients
  → "cot(2α) is not a frame artifact; represents a genuine structural feature"
  → Record in null_results/; update Tom Q2 answer to "no clean resolution here"

BLOCKED:
  Cannot pin the σ-basis ↔ Hopf coordinate transformation uniquely
  → Identify the missing convention, record as NEEDS_CONVENTION_FIX
```

---

## Controls

**Positive control:** S² spin connection as a 2-sphere sanity check.
The standard S² with e¹=dθ, e²=sinθ dφ gives ω₁₂ = cotθ e². This is a known
result — confirms the Cartan method is implemented correctly.

**Negative control:** Flat R³ in spherical coordinates should give zero spin
connection (no curvature). If any nonzero term appears → implementation broken.

**Convention pin:** Use the same metric signature and orientation as G0
(`vol = +sinα cosα dα ∧ dθ ∧ dφ`, `METRIC = diag(1, cos²α, sin²α)`).
Same sympy conventions as `evidence_sympy_invariant_sector.py`.

---

## Sensitivity Checks

1. **Radius ρ ≠ 1:** introduce radius ρ and verify cot(2α) structure holds for any ρ
   (frame artifact should be radius-independent).
2. **Different orientation convention:** flip `vol → −vol`; connection components
   flip sign but cot(2α) structure preserved.

---

## What This Does NOT Mean (pre-declared)

1. Does NOT mean "Tom's Dirac operator is wrong" — it may be in Hopf frame by design.
2. Does NOT mean λ is fixed — G2 is about frame structure, not coupling constants.
3. Does NOT mean eq. 49 is solved or tom_ansatz is a full mode.
4. Does NOT mean S³×S¹ geometry is solved (BG-GATE §4 is a separate track).
5. Does NOT select between spin structures (m∈ℤ vs m∈ℤ+1/2).
6. PASS here is a necessary condition for a clean invariant-frame Dirac, not sufficient for
   a physical derivation of the V operator.

---

## Source Grounding

Hopf spin connection derivation: standard differential geometry (Cartan structure
equations). Primary reference confirming S³ spin connection in this form:
Camporesi-Higuchi gr-qc/9505009, eqs 3.5-3.9 (spin connection in geodesic polar
frame on S^N). Local PDF: `references/camporesi_higuchi_grqc9505009.pdf`.

G0 provenance: `experiments/20260611-lambda-b5-structural-split/` — conventions
inherited (metric, orientation, sympy approach).

---

## Files to Create (implementation not started)

```
experiments/20260611-lambda-b5-cot-frame-artifact/
  claim_lambda_b5_g2.md          ← this file (pre-registration)
  evidence_sympy_cot_frame.py    ← sympy verification of C1, C2, C3
  g2_cot_frame_artifact_report.md  ← written AFTER code runs
  results.json                   ← written by evidence script (machine-readable)
```

**Rule:** `g2_cot_frame_artifact_report.md` and `results.json` do NOT exist until
the evidence script runs. If they exist before the script runs, pre-registration
is violated.

---

**Fence:** lambda = FREE_COUPLING_PARAMETER; runtime = research_only;
selection_rules = smoke_only; safe_for_runtime = False.
Nothing here is written to Tom until he replies to the 2026-06-09 message.
