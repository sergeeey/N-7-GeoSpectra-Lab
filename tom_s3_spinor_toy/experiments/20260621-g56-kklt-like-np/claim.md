# G56: KKLT-like non-perturbative stabilization on S³×S⁶

**Date:** 2026-06-21
**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Extends:** G55 (two-flux Dine-Seiberg runaway) → adds exponential non-perturbative term.

---

## Estimand

**Population:** S³×S⁶ compactification on SM constraint ρ₃ = C_SM × ρ₆², ρ₆ ∈ [0.85, 1.45]
**Intervention:** Adding V_np = −A_np × exp(−λ/ρ₆²)/V_int to V^EH_total
**Comparator:** V^EH_total without V_np (pure Dine-Seiberg runaway, G55)
**Endpoint:** Does an interior minimum (AdS vacuum) appear for some (A_np, λ)?
**Summary measure:** Existence of ρ₆₀ ∈ (ρ₆_min, ρ₆**) s.t. dV/dρ₆ = 0 at ρ₆₀ and V < 0
**MCID:** A_np must be order-unity compared to V_FLUX_CONST ≈ 0.286 (not exponentially small)

---

## Gates

### NP1: For (A_np=0.38, λ=0.30), a minimum exists in [0.953, 1.447]

**Claim:** The non-perturbative term V_np = −A_np × exp(−λ/ρ₆²)/V_int can overcome the
Dine-Seiberg runaway and create an interior minimum near ρ₆* ≈ 1.09.

**Minimum condition:** N'(ρ₆₀) = 12 N(ρ₆₀)/ρ₆₀  where N = V_FLUX_CONST + ζ_FP − A_np × exp(−λ/ρ₆²)

**Evidence:** [VERIFIED] Numerical root-find in derivative (finite-difference), minimum found in Casimir window

---

### NP2: At the minimum, V^EH_total < 0 (AdS vacuum)

**Claim:** The KKLT-like minimum is AdS: V^EH_total(ρ₆₀) < 0. This is generic for KKLT-type
stabilization before de Sitter uplift.

**Evidence:** [VERIFIED] V^EH_total(ρ₆₀) < 0 for two (A_np, λ) parameter points

---

### NP3: Required A_np ~ V_FLUX_CONST ≈ 0.286 (order-unity)

**Claim:** The non-perturbative amplitude A_np needed for stabilization is NOT exponentially
suppressed — it is order-unity compared to V_FLUX_CONST ≈ 0.286.

**Derivation:** Near-minimum condition gives A_np ≈ V_FLUX_CONST × exp(λ/ρ₆₀²).
For λ=0.30, ρ₆₀=1.09: exp(0.30/1.09²) = exp(0.252) ≈ 1.287 → A_np ≈ 0.368 ≈ 0.38.

**Evidence:** [VERIFIED] A_np/V_FLUX_CONST ∈ [0.5, 3] for any minimum in the Casimir window

---

### NP4: Casimir contribution << A_np × exp(−λ/ρ₆₀²) (Casimir-blind)

**Claim:** The Casimir energy at the KKLT minimum is negligible compared to the non-perturbative term.
The minimum location is determined by flux + NP competition, not Casimir.

**Evidence:** [VERIFIED] |ζ_FP(ρ₆₀)| / (A_np × exp(−λ/ρ₆₀²)) < 0.01

---

### NP5: Summary — scale and location of KKLT minimum

**Claim:** The minimum exists inside the "Casimir window" [ρ₆_min, ρ₆**] = [0.953, 1.447],
consistent with ρ₆* ≈ 1.09 where UV-finiteness holds.

**Evidence:** [VERIFIED] Minimum location ρ₆₀ ∈ (0.953, 1.447)

---

## What this does NOT mean

1. Does NOT prove de Sitter stabilization — the AdS vacuum requires uplift (anti-brane or F-term).
2. Does NOT fix A_np or λ uniquely — these are free parameters of the NP sector.
3. Does NOT change λ = FREE_COUPLING_PARAMETER (G4 Fisher rank theorem unchanged).
4. Does NOT constitute SM derivation (sm_derivation_claimed = False).
5. Does NOT prove the NP term arises from gaugino condensation — it is only an ansatz.
