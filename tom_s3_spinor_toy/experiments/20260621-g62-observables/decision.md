# G62 decision — PROMOTE (zero-fit observables)

**Date:** 2026-06-21
**Verdict:** PROMOTE — concrete physical predictions from geometry alone

## Observable summary (19/19 tests pass)

**Input parameters (zero-fit):**
| Parameter | Value | Source |
|-----------|-------|--------|
| λ | 1/3 (exact) | G61 dimensional: dim(S³)/dim(S³×S⁶) |
| A_np | 0.3787 | G60 Minkowski pearl: V_FLUX·exp(λ/ρ₆*²) |
| ρ₆* | 1.090 | G57 UV-selection c_{1/2}=0 |

**Predictions (no fitting):**
| Observable | Value | Units | Notes |
|-----------|-------|-------|-------|
| O1: ρ₆_min | **1.1791** | string | AdS minimum position |
| O2: V_min | **−2.53×10⁻⁶** | string | Shallow AdS (KKLT-like) |
| O3: m²_moduli | **2.95×10⁻⁴** | string² | Moduli mass squared |
| O4: m²_KK | **0.7193** | string² | KK mass squared |
| O5: m_mod/m_KK | **2.02%** | — | Key hierarchy prediction |
| O6: UV-split | **8.2%** | — | ρ₆_min vs ρ₆* (uplift needed) |

## Key findings

**Finding 1:** UV-selection (ρ₆*=1.090) and potential minimum (ρ₆_min=1.179) are DIFFERENT.
- UV-selection = Casimir UV-pole cancellation (c_{1/2}=0) → spectral regularization
- Minimum = NP stabilization → KKLT AdS vacuum
- An uplift term (anti-brane, D-term) must lift AdS→Minkowski at ρ₆*

**Finding 2:** m_mod/m_KK = 2% — moduli are light.
- EFT is self-consistent (moduli below KK threshold)
- But: light moduli → potential cosmological moduli problem (late-decaying moduli reheat)

**Finding 3:** V_min = −2.53×10⁻⁶ — shallow AdS, typical of NP stabilization.
- Consistent with KKLT literature (|W₀|² ≈ |A·exp(-aT)|²)
- Uplift energy needed: ΔV ≈ 2.53×10⁻⁶ (string units)

## What's promoted

The entire parameter-free prediction chain:
  S³×S⁶ geometry → [G17] SM charges → [G57] UV-selection ρ₆* → [G61] λ=1/3 →
  [G60] A_np from Minkowski → [G62] ρ₆_min, V_min, m_mod/m_KK

No numerical tuning at any step.

## What's NOT claimed

- Physical units for the predicted masses (requires string coupling identification)
- That m_mod/m_KK=2% matches any observed particle
- That the Casimir correction (neglected here) doesn't shift predictions by ~20%

## Next steps

1. **Tom ping** — this is the first clean prediction table. Send to Tom Lawrence.
2. **G63** (optional): Add Casimir correction to ρ₆_min and m_mod/m_KK
3. **Preprint** — G62 completes the prediction chain; enough for arXiv section
