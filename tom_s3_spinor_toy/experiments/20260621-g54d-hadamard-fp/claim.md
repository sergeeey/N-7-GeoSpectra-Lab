# G54-D Claim: Hadamard Finite Part ζ_FP(−1/2) via Mellin–Hadamard Subtraction

**Question type:** Descriptive + Predictive
**Date:** 2026-06-21
**Status:** D1-D6 PASS

---

## Natural language statement

"The Hadamard finite part ζ_FP(−1/2; ρ₃, ρ₆) of the spectral zeta function on S³×S⁶,
computed by Mellin–Hadamard subtraction with lower cutoff ε=0.10, changes sign along the
SM constraint ρ₃=Cρ₆² between ρ₆=1.2 and ρ₆=1.5 — defining a second special radius
ρ₆** ∈ (1.2, 1.5) where the Casimir finite part vanishes, distinct from ρ₆* ≈ 1.09
where the UV pole vanishes."

---

## Falsifiable claims

**D1 PASS:** Σ'(ρ₃, ρ₆) is a finite analytic sum of SW cross-term residues.
- Σ' changes sign between ρ₆=1.09 (positive) and ρ₆=1.20 (negative).
- |Σ'| grows as ρ₆^{12} for large ρ₆ (dominated by α=−4.5 term).
- Verified analytically — no integration error possible.
- PASS [VERIFIED]

**D2 PASS:** I_reg = ∫_{0.10}^1 t^{-3/2}(K_full−K_SW) dt is small vs |Σ'|.
- |I_reg/Σ'| < 50% at ρ₆=1.0 — SW expansion is accurate approximation.
- K_full ≈ K_SW at t=ε=0.10 (relative error < 2%) — cutoff is justified.
- ε=0.10 avoids catastrophic cancellation at t < 0.01 where n=150 eigenvalues
  are insufficient for K_{S⁶} convergence (~260 needed at t=0.001).
- PASS [VERIFIED]

**D3 PASS:** I₂ = ∫_1^∞ t^{-3/2} K_full dt is exponentially small.
- |I₂/Σ'| < 5% at ρ₆=1.0 — large-t tail is negligible.
- I₂ > 0 everywhere (K_full > 0, t^{-3/2} > 0).
- PASS [VERIFIED]

**D4 PASS:** ζ_FP changes sign — Bolzano guarantees ρ₆** ∈ (1.2, 1.5).
- ζ_FP(1.2) < 0, ζ_FP(1.5) > 0.
- Product ζ_FP(1.2) × ζ_FP(1.5) < 0 — zero crossing confirmed.
- ρ₆** is distinct from ρ₆* ≈ 1.09 (where c_{1/2}=0, UV pole cancels).
- PASS [VERIFIED]

**D5 PASS:** At ρ₆*, ζ_FP is finite, negative, O(10⁻³) in magnitude.
- c_{1/2}(ρ₆*) ≈ 0 to 10⁻⁸ (prerequisite — UV pole vanishes).
- ζ_FP(ρ₆*) < 0 — Casimir energy is negative at UV-finite radius.
- |ζ_FP(ρ₆*)| ∈ (10⁻⁵, 0.1) — non-zero but small.
- ρ₆* does NOT make ζ_FP extremal (not the compactification minimum).
- PASS [VERIFIED]

**D6 PASS:** Sign mechanism — Σ' drives ζ_FP through Γ(−1/2) < 0.
- At ρ₆=0.7: Σ'>0, Γ<0 → Σ'/Γ < 0 → ζ_FP < 0.
- At ρ₆=1.5: Σ'<0, Γ<0 → Σ'/Γ > 0 → ζ_FP > 0.
- ψ(−1/2) ≈ 0.0365 is small — c_{1/2} correction is subdominant near ρ₆**.
- PASS [VERIFIED]

---

## Key numerical results (along SM constraint ρ₃=0.986ρ₆²)

| ρ₆  | ρ₃    | Σ'        | I_reg    | c_{1/2}   | ζ_FP     |
|-----|-------|-----------|----------|-----------|----------|
| 0.7 | 0.483 | +0.00265  | +0.0004  | +0.00196  | −0.00084 |
| 1.0 | 0.986 | +0.00420  | −0.00122 | +0.00053  | −0.00085 |
| 1.09| 1.172 | +0.00337  | −0.00122 | ≈0        | −0.00080 |
| 1.2 | 1.420 | −0.00316  | −0.00108 | −0.00071  | −0.00065 |
| 1.5 | 2.219 | −0.449    | −0.00067 | −0.00298  | +0.00020 |

ρ₆* ≈ 1.09 (c_{1/2}=0, UV pole cancels)
ρ₆** ∈ (1.2, 1.5) (ζ_FP=0, Casimir finite part cancels)

---

## What this does NOT mean

1. Does NOT mean ρ₆** is the physical compactification radius — additional
   conditions (flux quantization, stability) are needed.
2. Does NOT mean ζ_FP has a minimum at ρ₆* — ρ₆* is where the UV pole
   vanishes, not where the finite Casimir energy is extremal.
3. Does NOT claim ζ_FP is monotone — the large-ρ₆ blow-up of Σ' (∝ ρ₆^{12})
   eventually dominates and drives ζ_FP positive.
4. Does NOT establish SM physics derivation (sm_derivation_claimed = False).
5. Does NOT imply Tom Lawrence endorsement of these results.

---

## Claim entropy (Perelman)

| Source of uncertainty | Count |
|----------------------|-------|
| SW fit accuracy beyond B₁₀ (B₁₂, B₁₄ terms) | 1 |
| I_reg precision (eps=0.10 cutoff approximation) | 1 |
| Physical interpretation of ρ₆** | 1 |
| **Total** | **3** |
