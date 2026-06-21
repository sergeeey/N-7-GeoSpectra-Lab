# G57 Decision: PROMOTE (UV-selection principle established)

**Date:** 2026-06-21
**Verdict:** PROMOTE (structural result — UV ray + SM constraint uniquely select ρ₆*)
**Tests:** 16/16 PASS

---

## Summary

The UV-finite locus {c_{1/2}(ρ₃,ρ₆) = 0} in full 2D moduli space is a RAY:
  ρ₃/ρ₆ = C_UV ≈ 1.0743 (homogeneity of degree −1 forces the zero set to be a cone = ray in 2D)

The SM coupling constraint ρ₃ = C_SM × ρ₆² is a parabola in moduli space.
These two curves (ray and parabola) intersect at EXACTLY ONE POINT: ρ₆* = C_UV/C_SM ≈ 1.090.

**G57 = the geometric reason ρ₆* is special.**
G54-C found it numerically; G57 explains WHY it's the unique UV-finite + SM-coupling point.

---

## Gates summary

| Gate | Verdict | Key finding |
|------|---------|-------------|
| UV1 | PASS | c_{1/2} is homogeneous of degree −1 (algebraic, exact) |
| UV2 | PASS | {c_{1/2}=0} = UV ray ρ₃/ρ₆ = C_UV ≈ 1.0743, verified at 5 off-constraint points |
| UV3 | PASS | Intersection: ρ₆* = C_UV/C_SM = 1.0743/0.986 ≈ 1.089 ≈ 1.090 (unique) |
| UV4 | PASS | UV ray alone doesn't fix ρ₆: g₂²/g₃² varies 2×+ along the ray |
| UV5 | PASS | Sign pattern consistent: c > 0 below UV ray, c < 0 above |

---

## Physical interpretation

**Homogeneity is the key:** c_{1/2}(ρ₃,ρ₆) = A₀_S3ρ₃³B₁₀/ρ₆⁴ + A₂_S3ρ₃B₈/ρ₆²
Each term scales as λ³/λ⁴ = λ⁻¹ and λ/λ² = λ⁻¹ under (ρ₃,ρ₆)→(λρ₃,λρ₆).
So the full function is homogeneous of degree −1, and its zero set is scale-invariant (a ray).

**The UV ray is NOT specific to the SM point:** it exists everywhere on the ray ρ₃ = C_UV ρ₆.
The SM coupling constraint then picks the unique ρ₆ on this ray that reproduces the observed ratio.

**Sign asymmetry:** c_{1/2} > 0 for ρ₃/ρ₆ < C_UV (Casimir UV divergence in one direction) and
c_{1/2} < 0 for ρ₃/ρ₆ > C_UV (opposite sign). This means ρ₆* is NOT a local minimum of |c_{1/2}|
— it's a zero crossing. The sign pattern is fixed by the SW coefficients B₈ < 0, B₁₀ < 0.

---

## Pearl: UV-finiteness selects a 1D locus in 2D moduli space

The zero set {c_{1/2} = 0} is a single ray (1-dimensional curve) in 2D moduli space.
This is a consequence of homogeneity: degree-k functions in 2 variables have zero sets of codimension 1.
By combining with the 1D SM constraint, we select a 0-dimensional (point) solution = ρ₆*.

This "intersection principle" may generalize: any pair of spectral constraints that factor as
one homogeneous condition + one non-homogeneous condition will select a unique scale.

---

## Connection to G54-G56

| Gate | What it established |
|------|-------------------|
| G54-C | c_{1/2}(ρ₃*,ρ₆*) ≈ 0 at ρ₆* ≈ 1.090 (numerical, on SM constraint only) |
| G57-UV1 | c_{1/2} is homogeneous of degree −1 (algebraic reason) |
| G57-UV2 | {c_{1/2}=0} is a ray in full 2D space (geometric consequence) |
| G57-UV3 | SM parabola ∩ UV ray = {ρ₆*} (unique intersection = compactification selection) |

---

## Kill Analysis

**What is NOT killed:**
- Stabilization itself requires NP sector (G56) — UV selection doesn't stabilize
- λ = FREE_COUPLING_PARAMETER (G4 result, unchanged)
- sm_derivation_claimed = False
