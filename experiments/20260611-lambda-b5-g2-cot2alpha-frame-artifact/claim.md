# LAMBDA-B5-G2: cot(2α) Frame-Artifact Hypothesis

**Date:** 2026-06-11
**Tier:** FL Standard (research, structural/geometric claim)
**Question type:** [x] descriptive (structural) [ ] predictive [ ] causal
**Status:** CLOSED — **PASS_FRAME_ARTIFACT_CONFIRMED**

---

## Claim

The cot(2α) obstruction encountered in Tom Lawrence's S³ Dirac operator analysis
is a **Hopf-coframe frame artifact**, not a physical singularity.

Specifically:

1. **Algebraic identity:**  tan α − cot α = −2cot(2α)  [exact, no approximation]

2. **Hopf coframe spin connection** (metric ds²=dα²+cos²α dθ²+sin²α dφ²,
   coframe e¹=dα, e²=cosα dθ, e³=sinα dφ):
   ```
   ω¹₂ = +tan(α) e²   ← α-dependent
   ω¹₃ = −cot(α) e³   ← α-dependent
   ω²₃ = 0
   sum of coefficients: tan(α) + (−cot α) = tan α − cot α = −2cot(2α)
   ```

3. **Invariant (left-invariant) frame:** the Maurer-Cartan structure of the
   left-invariant 1-forms σ₁, σ₂, σ₃ satisfies
   ```
   dσ₃ = k · σ₁∧σ₂   with k = 2  (integer constant, no α-dependence)
   ```
   The connection structure constants in this frame are pure integers, not functions of α.

**Conclusion:** cot(2α) arises from the α-dependent spin connection of the Hopf
orthonormal frame. In the left-invariant frame the same S³ geometry has integer
(constant) connection coefficients — cot(2α) is absent by construction.

---

## Evidence (two independent lines)

| Line | Source | Marker |
|---|---|---|
| Sympy symbolic: Cartan equations, curvature, MC ratio | `evidence_sympy_g2_frame_artifact.py` — 14/14 checks, exit 0 | [VERIFIED-sympy 2026-06-11] |
| Convention consistency | Same coframe and Killing form as G0 (`evidence_sympy_invariant_sector.py`); σ₃ = ξ̃ verified there with *d eigenvalue −2 | [VERIFIED-sympy G0 session] |

---

## Controls

- **Positive control:** Hopf coframe Cartan equations are satisfied [T6–T8] → the
  Hopf frame connection (ω¹₂=+tanα e², ω¹₃=−cotα e³) is the unique torsion-free
  connection for this coframe.
- **Negative control (α-dependence):** d/dα[cot α] = −1/sin²α ≠ 0 [T2] — the
  Hopf connection coefficients are genuinely α-dependent, not constants.
- **Frame-independence check:** curvature R^{ab} = e^a∧e^b [T11–T13] gives the
  unit S³ value in the Hopf frame — this is a frame-invariant test confirming the
  geometry is correct and unmodified.
- **Invariant frame MC ratio:** dσ₃/(σ₁∧σ₂) = 2 [T14] — integer, no α, θ, φ
  dependence → the invariant frame has constant structure, no cot(2α) obstruction.

---

## Kill Conditions (what would falsify this claim)

1. Any Cartan equation has non-zero residual → Hopf connection wrong → claim void.
2. Curvature R¹₂ ≠ e¹∧e² → geometry not unit S³ → setup wrong.
3. dσ₃/(σ₁∧σ₂) = f(α,θ,φ) (α-dependent) → invariant forms not truly left-invariant → claim void.
4. tan α − cot α ≠ −2cot(2α) algebraically → fundamental identity wrong.

None triggered. [VERIFIED-sympy 14/14 exit 0]

---

## Verdict

```
LAMBDA-B5-G2 = PASS_FRAME_ARTIFACT_CONFIRMED
```

## Consequence: Candidate Answer to Tom's Q2

Tom's Q2: "Does cot(2α) vanish with the correct SO(4) spinor basis?"

G2 provides the candidate mechanism:
- In the Hopf coframe (which is the natural coordinate frame for Hopf coordinates),
  the spin connection has coefficients tanα and −cotα.
- Their combination, tanα − cotα = −2cot(2α), may appear in the Dirac operator.
- In the left-invariant frame, the same geometry has integer spin connection
  coefficients — no α-dependent obstruction.
- If Tom's "correct SO(4) spinor basis" corresponds to the left-invariant frame,
  then yes, cot(2α) vanishes.

**Status: [HYPOTHESIS → VERIFIED/scoped]**
Scoping: the mechanism is confirmed at the level of spin connection coefficients
and MC structure. The precise identification with Tom's specific operator term
requires Tom's confirmation (pending his reply to the 2026-06-09 message).

---

## λ Status (unchanged from G0 — use verbatim)

```
λ total      = NOT fixed  (S³-only mode-expanded λ remains free; P14 no-go intact)
λ_geom       = MAY be canonically normalized IF V_ω is identified with the
               geometric Dirac spin-connection term (Tom's Q3 — still open)
c_i (modes)  = free
```

G2 confirms the geometric spin connection exists and has a canonical form (ε_ijk σᵏ/ρ
in the invariant frame). This does NOT fix λ — it clarifies what V_ω would be IF
the geometric sector were included in the ansatz.

---

## What This Result Does NOT Mean

1. Does NOT mean "λ fixed."
2. Does NOT mean Tom's operator is fully understood — only the spin connection
   frame-artifact mechanism is confirmed.
3. Does NOT prove the invariant frame is the correct physical frame for Tom's problem —
   that identification awaits Tom's reply.
4. Does NOT select geometry (S³×S¹ vs S³×S²) — GEOMETRY_AGNOSTIC intact.
5. Does NOT promote any V operator physically — PROMOTION_BLOCKED intact.
6. Does NOT mean cot(2α) vanishes in ALL contexts — only in the invariant frame.

---

## Next Gates

- **G1:** canonical Dirac in invariant frame reproduces ±(n+3/2) spectrum
  (positive control = existing E0 harness).
- **G3:** [D_a,D_b] curvature kill-test, su(2)_L ⊂ su(4) embedding (Dereli eq 4.12).
- **BG-GATE §4:** geometry discrimination — still requires Tom's reply.

Order: G0 ✅ → G2 ✅ → G1/G3 (if still relevant after Tom replies)

---

**Fence:** lambda = FREE_COUPLING_PARAMETER; runtime = research_only;
GEOMETRY_AGNOSTIC intact; safe_for_runtime = False.
Nothing written to Tom until he replies to the 2026-06-09 four-question message.
