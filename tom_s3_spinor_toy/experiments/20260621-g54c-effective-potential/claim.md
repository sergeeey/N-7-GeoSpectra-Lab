# G54-C Claim: Full Casimir Pole Residue and Pole Cancellation

**Question type:** Descriptive + Predictive
**Date:** 2026-06-21
**Status:** C1-C3 PASS · C4 OPEN

---

## Natural language statement

"For the product heat kernel K(t; ρ₃, ρ₆) = K_{S³}(t/ρ₃²) × K_{S⁶}(t/ρ₆²), the
coefficient of t^{1/2} in the SW expansion has TWO contributing cross-terms —
A₂_S3×B₈_S6 (found in G54-B) and A₀_S3×B₁₀_S6 (missed in G54-B) — and their
combination produces a zero at ρ₆* ≈ 1.09 along the SM constraint ρ₃=Cρ₆²."

---

## Falsifiable claims

**C1:** B₁₀_S6 (coefficient of τ² in K_{S⁶} SW expansion) is non-zero.
- Measured: B₁₀ ≈ −0.0033 (small-τ fit, stable across 6- and 7-param fits)
- Compare: |B₁₀/B₈| ≈ 0.43 — not a tiny perturbation
- PASS [VERIFIED]

**C2:** Full c_{1/2}(ρ₃, ρ₆) = A₂_S3 × B₈ × ρ₃/ρ₆² + A₀_S3 × B₁₀ × ρ₃³/ρ₆⁴
varies with ρ₆ along the SM constraint ρ₃ = C ρ₆².
- Implicit in G54-B B4: only A₂×B₈ term was included (INCOMPLETE).
- G54-B B4 used 5-param fit that absorbed B₁₀ effects into effective B₈.
- Full 6-param fit reveals: c_{1/2} changes sign at ρ₆ ≈ 1.09.
- PASS [VERIFIED]

**C3:** c_{1/2} = 0 at a specific ρ₆* satisfying:
  ρ₆*² = −(A₂_S3 × B₈) / (A₀_S3 × B₁₀ × C²) ≈ 1.19 → ρ₆* ≈ 1.09
- Numerically confirmed: c_{1/2}(ρ₆*) < 0.002 × c_{1/2}(0.1)
- Sign flip confirmed across ρ₆*
- PASS [VERIFIED]

**C4 (OPEN):** Does ζ_FP(−1/2; ρ₃, ρ₆) (Hadamard finite part) have a minimum
along the SM constraint? Does it also vanish at ρ₆*?

---

## Revision of G54-B B4

G54-B B4 claimed: "c_{1/2} = A₂_S3 × B₈ × C = CONSTANT along SM constraint."

This was based on a 5-parameter fit that fitted K_{S⁶} with {τ^{-3}, τ^{-2}, τ^{-1}, τ^0, τ^1}.
The 5-param fit gives B₈_eff ≈ −0.0108, which absorbs the B₁₀ contribution into an
effective B₈. The resulting c_{1/2} = A₂×B₈_eff×C appears constant because both the
A₂×B₈ and A₀×B₁₀ terms are lumped together — but they have DIFFERENT ρ₆ dependences.

Correct picture:
  c_{1/2} = (A₂_S3 × B₈ × C) + (A₀_S3 × B₁₀ × C³) × ρ₆²
           = const_pos         + const_neg × ρ₆²

This vanishes at ρ₆* ≈ 1.09, then becomes increasingly negative for larger ρ₆.

---

## What this does NOT mean

1. Does NOT mean the SM constraint fixes ρ₆ (the constraint only fixes ρ₃/ρ₆²).
2. Does NOT mean c_{1/2} = 0 at ρ₆* implies ζ_FP = 0 at that point.
3. Does NOT mean ρ₆* ≈ 1.09 has a physical interpretation without units/normalization.
4. Does NOT invalidate the Poisson theorem (A₄=0 for S³ still exact).
5. Does NOT change G54-A (V_flux) — the Freund-Rubin flux is still scale-invariant.

---

## Claim entropy (Perelman)

| Source of uncertainty | Count |
|----------------------|-------|
| B₁₀ stability (higher-order τ contamination) | 1 |
| Physical meaning of ρ₆* | 1 |
| Relation to ζ_FP (G54-C4 open) | 1 |
| **Total** | **3** |
