# LAMBDA-B5-P14B — S³ Hopf measure normalization robustness

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:**
The S³ Hopf measure sin(α)cos(α)dα is internally self-consistent:
it yields the correct round-S³ volume (2π² for unit sphere, 2π²ρ³ for radius ρ),
the bilinear φ₀₀·g₀₀ = cosα·sinα from AV-2 E1 is normalizable and phase-invariant
under this measure, and the measure is equivalent to its sin(2α)/2 form.

This gate runs autonomously — it does not depend on Tom Q4 (α-convention confirmation).
It verifies that the measure used throughout the project is internally consistent,
which holds regardless of whether Tom confirms or corrects the replacement basis.

**Kill target (Strong Inference):**
- FAIL (volume wrong, bilinear non-integrable, or measure inconsistent) →
  All previous normalizations throughout the project require re-examination.
  AV-2 E1 result φ₀₀·g₀₀ = cosα·sinα would need normalization correction.
  P13H coefficient (16π²ρ³/15)·λ would need re-derivation.
- PASS → Measure confirmed self-consistent; Q4 is a question about Tom's CHOICE
  of basis frame, not about the validity of the measure itself.

**Checks planned (7 checks):**
- T1: Radial part of volume: ∫₀^{π/2} sin(α)cos(α) dα = 1/2 (exact)
- T2: Full S³ volume (unit sphere): (1/2) × (2π)² = 2π² (exact)
- T3: Measure equivalence: sin(α)cos(α) == sin(2α)/2 (symbolic identity)
- T4: Bilinear norm (radial): ∫₀^{π/2} sin²(α)cos²(α) · sin(α)cos(α) dα = 1/12 (exact)
- T5: Full bilinear norm with angular factors: (1/12) × 4π² = π²/3 (finite and exact)
- T6: Phase invariance: |e^{iχ}·cosα·sinα|² = cos²α·sin²α (independent of χ)
- T7: Radius scaling: S³(ρ) volume = 2π²ρ³ (Jacobian from coordinate rescaling)

**Caveat / What this does NOT mean:**
- Does NOT confirm Tom's replacement basis U(α,θ,θ̃) is the correct spinor frame
- Does NOT fix the normalization of individual spinor modes (that requires Tom Q4)
- Does NOT re-derive the (16π²ρ³/15) coefficient from scratch
- Does NOT resolve the spin structure fork (Case 6)

**Fence (unchanged):**
- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

**Verdict:** PASS_S3_MEASURE_SELF_CONSISTENT [VERIFIED-sympy 7/7, 2026-06-11]

**Key numbers:**
- S³ volume (unit sphere): `2π²` — exact
- S³ volume (radius ρ): `2π²ρ³` — exact
- Bilinear radial norm ∫|cosα·sinα|²·sinα cosα dα: `1/12` — exact
- Full bilinear norm (with angular factors): `π²/3` — finite and exact
- Phase factor |e^{iχ}|² = 1 → bilinear norm is phase-invariant

**Separation of concerns (key insight):**
Tom Q4 asks WHICH spinor modes are canonical in the replacement basis U(α,θ,θ̃).
This gate shows the S³ measure itself is valid and consistent.
These are independent questions — the measure passes regardless of Tom's answer.

**Status:** CLOSED PASS_S3_MEASURE_SELF_CONSISTENT
