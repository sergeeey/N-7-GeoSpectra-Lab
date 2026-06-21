# G54-E: Structure of ζ_FP(−1/2) along SM constraint — three special radii

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Estimand:** Along the SM constraint ρ₃ = 0.986 ρ₆², describe the structure of
ζ_FP(−1/2; ρ₃, ρ₆) as a function of ρ₆ ∈ (0.7, 1.6).
Summary measure: locations and values of three special radii.

**Claim (natural language statement):**
We characterize ζ_FP(−1/2; 0.986 ρ₆², ρ₆) for ρ₆ along the SM constraint,
identifying three special radii — ρ₆_min (local minimum), ρ₆* (UV pole cancels),
ρ₆** (ζ_FP = 0) — with strict ordering ρ₆_min < ρ₆* < ρ₆** and numerical values
established by Hadamard subtraction from G54-D.

**What this does NOT mean:**
1. Does NOT claim ρ₆_min or ρ₆** is the physical compactification radius (no
   mechanism identifying which special radius is selected is proposed here).
2. Does NOT establish the SM gauge couplings (λ = FREE_COUPLING_PARAMETER by G4
   theorem; sm_derivation_claimed = False).
3. Does NOT provide an analytic formula for ρ₆** — it is computed numerically via
   bisection from the G54-D Hadamard formula.
4. Does NOT imply Tom Lawrence endorsement of any result.

---

## E1: Local minimum of ζ_FP at ρ₆_min ∈ (0.85, 1.05)

**Claim:** ζ_FP has a local minimum at ρ₆_min ≈ 0.953 on [0.7, 1.3].
- ζ_FP(0.95) ≈ −0.000863 (minimum) vs ζ_FP(0.80) ≈ −0.000804 and ζ_FP(1.10) ≈ −0.000777
- Derivative is negative at ρ₆ = 0.85, positive at ρ₆ = 1.05 → minimum in (0.85, 1.05)

**Evidence:** [VERIFIED] numerical — minimize_scalar on [0.7, 1.3] → ρ₆_min = 0.9529.
**Tests:** E1.1, E1.2 (bracket), E1.3 (derivative sign change), E1.4 (magnitude order)

## E2: ζ_FP = 0 at ρ₆** ∈ (1.44, 1.46)

**Claim:** ζ_FP changes sign in (1.40, 1.50); precise zero at ρ₆** ≈ 1.4469.
- ζ_FP(1.44) < 0 and ζ_FP(1.46) > 0 → Bolzano bracket
- brentq → ρ₆** = 1.4469 ± 0.001

**Evidence:** [VERIFIED] numerical — brentq in (1.44, 1.50) with xtol=1e-4.
**Tests:** E2.1 (sign at 1.40), E2.2 (sign at 1.50), E2.3 (bracket [1.44,1.46]), E2.4 (brentq value)

## E3: Three radii ordered — ρ₆_min < ρ₆* < ρ₆**

**Claim:** The three special radii are strictly ordered:
  ρ₆_min ≈ 0.953 < ρ₆* ≈ 1.090 < ρ₆** ≈ 1.447

Physical interpretation (descriptive only, no causal claim):
- ρ₆_min: Casimir energy is most attractive (most negative) here
- ρ₆*:    UV pole cancels (c_{1/2}=0); energy is still −0.0008, attractive
- ρ₆**:   Casimir energy = 0; transition from attractive to repulsive regime

**Evidence:** [VERIFIED] from E1 (ρ₆_min ≈ 0.953), G54-C formula (ρ₆* ≈ 1.090),
E2 bisection (ρ₆** ≈ 1.447).
**Tests:** E3.1 (ρ₆_min < ρ₆*), E3.2 (ρ₆* < ρ₆**), E3.3 (ζ_FP < 0 at ρ₆*),
E3.4 (full ordering summary)

---

## Numerical summary

| Radius    | Value  | Property                        | ζ_FP value |
|-----------|--------|---------------------------------|------------|
| ρ₆_min    | ≈ 0.953| local minimum of Casimir energy | ≈ −0.000863|
| ρ₆*       | ≈ 1.090| UV pole cancels (c_{1/2}=0)    | ≈ −0.000798|
| ρ₆**      | ≈ 1.447| Casimir finite part = 0         |  = 0       |

Ratio ρ₆**/ρ₆* ≈ 1.328 (no simple algebraic form identified within SW fit accuracy).
Ratio ρ₆_min/ρ₆* ≈ 0.875.

## Claim entropy (Perelman)

| Source of uncertainty | Count |
|-----------------------|-------|
| Unsupported HIGH claims | 0 |
| Hidden assumptions | 1 (SW 6-param fit accuracy) |
| Missing negative controls | 0 |
| Ambiguous definitions | 0 |
| Unresolved blockers | 0 |
| **Total** | **1** |
