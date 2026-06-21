# G57: UV-selection principle — ρ₆* as intersection of two independent conditions

**Date:** 2026-06-21
**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Extends:** G54-C (UV-finite point on SM constraint) → generalizes to full 2D structure.

---

## Estimand

**Population:** S³×S⁶ moduli space (ρ₃, ρ₆) ∈ (0,∞)²
**Intervention:** Imposing UV-finiteness of Casimir energy (c_{1/2} = 0)
**Comparator:** Imposing SM gauge coupling constraint only (ρ₃ = C_SM × ρ₆²)
**Endpoint:** Does the intersection of UV condition + SM condition uniquely select ρ₆*?
**Summary measure:** Number of intersection points (should be exactly 1 for ρ₆ > 0)
**MCID:** A unique selection is "more restrictive than either condition alone"

---

## New structural result

**c_{1/2}(ρ₃, ρ₆) is homogeneous of degree −1:**

  c_{1/2}(λρ₃, λρ₆) = λ⁻¹ c_{1/2}(ρ₃, ρ₆)

**Consequence:** The zero set {c_{1/2} = 0} is a CONE — it is a RAY from the origin:

  ρ₃/ρ₆ = C_UV  where  C_UV = √(−A₂_S3 B₈/(A₀_S3 B₁₀)) ≈ 1.0743

This ray crosses the SM parabola ρ₃ = C_SM × ρ₆² at EXACTLY ONE POINT:

  ρ₆* = C_UV / C_SM ≈ 1.0743 / 0.986 ≈ 1.090

**Two independent conditions jointly select ρ₆*:**
- UV-finiteness alone: selects the ray (1 constraint, infinitely many solutions in 2D)
- SM couplings alone: selects the parabola (1 constraint, infinitely many solutions in 2D)
- Both together: select ρ₆* (2 constraints, 1 solution = unique compactification scale)

---

## Gates

### UV1: c_{1/2} is homogeneous of degree −1

**Evidence:** [VERIFIED] c_{1/2}(λ×r3, λ×r6) = λ⁻¹c_{1/2}(r3,r6) to 10-decimal precision for λ ∈ {0.5, 1.5, 2.0, 3.0}

---

### UV2: {c_{1/2}=0} is a RAY ρ₃/ρ₆ = C_UV ≈ 1.0743

**Evidence:** [VERIFIED] c_{1/2} ≈ 0 at 5 points on the UV ray (r6 ∈ {0.5, 0.8, 1.0, 1.5, 2.0}).
C_UV from SW formula: √(−A₂B₈/(A₀B₁₀)) ≈ 1.0743, matches C_SM×ρ₆* = 1.0747.
Sign: c_{1/2} > 0 below UV ray (ρ₃/ρ₆ < C_UV), c_{1/2} < 0 above.

---

### UV3: SM constraint intersects UV ray at unique ρ₆* ≈ 1.090

**Evidence:** [VERIFIED] ρ₆* = C_UV/C_SM = 1.0743/0.986 = 1.089 ≈ 1.090. SM constraint
meets UV ray only at ρ₆*: verified for 5 values of ρ₆ ∈ {0.7, 0.85, 1.0, 1.2, 1.4}.

---

### UV4: Both conditions needed — neither alone fixes ρ₆

**Evidence:** [VERIFIED] Along the UV ray, g₂²/g₃² varies by factor >2 across r6 ∈ {0.5,0.8,1.0,1.2,1.5};
coupling is NOT fixed by UV condition alone. Only at ρ₆* does g₂²/g₃² = V_FLUX_SM.

---

### UV5: Sign pattern of c_{1/2} consistent with UV ray picture

**Evidence:** [VERIFIED] c_{1/2} > 0 for ρ₆ < ρ₆* on SM constraint (ρ₃/ρ₆ < C_UV),
c_{1/2} < 0 for ρ₆ > ρ₆* (ρ₃/ρ₆ > C_UV). Sign change at ρ₆* matches G54-C.

---

## What this does NOT mean

1. Does NOT prove ρ₆* is the physical vacuum (not stabilized without NP term, G56)
2. Does NOT fix ρ₃ independently — on UV ray ρ₃ = C_UV × ρ₆, only ρ₆* is the physical point
3. Does NOT change λ = FREE_COUPLING_PARAMETER (G4 Fisher rank unchanged)
4. Does NOT constitute SM derivation (sm_derivation_claimed = False)
5. Does NOT mean c_{1/2}=0 is a quantum gravity requirement — it is a condition for UV-finiteness
   of the zeta-function regularization without counterterms
