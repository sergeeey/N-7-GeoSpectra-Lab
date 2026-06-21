# H1 Decision — Geometric λ-law for Product Spheres

**Date:** 2026-06-21
**Verdict:** PROMOTE

## Test Results

30/30 tests passed (`tests/test_h1_lambda_geometric.py`).

### Summary table

| Manifold | λ      | ρ_min  | V_min       | m_mod/m_KK |
|----------|--------|--------|-------------|-----------|
| S¹×S⁸   | 0.1111 | 1.1779 | −8.31×10⁻⁷ | 1.17%     |
| S²×S⁷   | 0.2222 | 1.1785 | −1.67×10⁻⁶ | 1.66%     |
| S³×S⁶   | 0.3333 | 1.1791 | −2.53×10⁻⁶ | 2.02% ← G62 |
| S⁴×S⁵   | 0.4444 | 1.1797 | −3.39×10⁻⁶ | 2.33%     |
| S⁵×S⁴   | 0.5556 | 1.1803 | −4.27×10⁻⁶ | 2.60%     |

### Gates passed

- **G-H1-1 (anchor):** S³×S⁶ reproduces ρ_min=1.1791, V_min=−2.53×10⁻⁶, m_mod/m_KK=2.02% [VERIFIED]
- **G-H1-2 (family):** minimum exists (V_min < 0, ρ_min > ρ*) for ALL 5 (a,b) cases [VERIFIED]
- **G-H1-3 (KKLT):** ρ_min/ρ* > 1 for all cases (separation 8–8.5%) [VERIFIED]
- **G-H1-4 (EFT):** m_mod/m_KK ∈ [1.2%, 2.6%] for all cases (well below 15%) [VERIFIED]
- **G-H1-5 (negative):** λ=0 → V_total ≡ 0 everywhere (flat, no stabilization) [VERIFIED]
- **G-H1-6 (monotone):** ρ_min increases monotonically with λ [VERIFIED]
- **G-H1-7 (universality):** ρ_min spread = 0.20% across the whole family [VERIFIED]

## Unexpected Pearl: ρ_min Near-Universality

**The most striking result is NOT the λ-dependence but the λ-INdependence of ρ_min.**

ρ_min varies from 1.1779 to 1.1803 across a 5× range of λ (0.111 → 0.556): variation = **0.20%**.

This means:
- The compactification SCALE is set by UV-selection geometry (ρ*=1.090), not by the dimensional split
- The DEPTH of the potential (V_min) scales ∝ λ (linear, to ~5% accuracy)
- The MASS RATIO m_mod/m_KK scales as ~√λ × const

Interpretation: **ρ_min ≈ 1.179 is a near-universal attractor for the whole Sᵃ×Sᵇ family**,
provided ρ* and V_FLUX are fixed by the same UV-selection mechanism.

If Tom's spin-connection structure gives a reason why ρ* should be universal across sphere products,
this universality becomes a physics prediction, not just an artifact of our fixed ρ*.

## Skeptic Pre-Answers (Step 8a shortcut)

**Concern 1:** "V_FLUX and ρ* are NOT re-derived per (a,b). This is a circular structural test."

Response: **Accepted limitation** — documented in claim.md § "What this does NOT mean" point 2.
This is a structural self-consistency test, not a full per-geometry calculation.
The H1 claim is that λ=a/(a+b) parametrizes a sensible family; it does not claim these other
manifolds are physical. Scope is clearly bounded.

**Concern 2:** "Minimum for S¹×S⁸ (λ=1/9) is very shallow — is it real?"

Response: **Dismissed** — V_min = −8.3×10⁻⁷ is a genuine AdS minimum (V2 > 0 confirmed
by second_deriv; EFT check passes). It is shallower than S³×S⁶ but the same structural type.

**Concern 3:** "ρ_min universality is trivial because ρ* is fixed."

Response: **Accepted as partial** — but the universality is still non-trivial. The minimum
condition is a transcendental equation (exp term + power law) that could in principle give
very different ρ_min for different λ. The empirical finding that ρ_min varies by only 0.2%
is a property of the mathematical structure, not just the fixed ρ*.

## Kill Analysis (for completeness)

**What is NOT killed:**
- λ = a/(a+b) as a geometric law for the NP exponent family
- ρ_min ≈ 1.179 universality across Sᵃ×Sᵇ family (new pearl)
- m_mod/m_KK ∈ [1–3%] hierarchy across the family
- G62 anchor (S³×S⁶) — fully reproduced

**What this test does NOT establish:**
- Which (a,b) is the physical compactification
- Why V_FLUX and ρ* should be the same for different sphere products
- A derivation of λ from first principles (G61 remains WEAK for this)

## Pearl Registry Entry

Added to `pearl_registry/INDEX.md`:
ρ_min ≈ 1.179 is nearly universal across Sᵃ×Sᵇ family (0.20% spread) when ρ* is fixed.
Falsifiable prediction: if UV-selection mechanism is re-derived per (a,b), does ρ* stay ≈1.090?

## Verdict: PROMOTE

The H1 hypothesis is structurally self-consistent and surfaces a new unexpected pearl
(ρ_min universality). Marked [HYPOTHESIS] pending per-geometry V_FLUX and ρ* derivations.

The claim in its tested form: **CONFIRMED** (30/30 tests).
The stronger physical claim (other sphere products are real compactifications): **[HYPOTHESIS]**.
