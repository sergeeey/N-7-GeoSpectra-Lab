# AV-1c′ Report — Cross-Bilinear Dictionary for eq. 49 Radial Layer

**Experiment:** AV1C_PRIME_CROSS_BILINEAR_DICTIONARY
**Date:** 2026-06-10
**Pre-registration:** claim_av1c_prime.md (BEFORE code ran; after AV-1 commit 7fa4360)
**Code:** `tom_s3_spinor_toy/av1c_prime_cross_bilinear.py`
**Tests:** `tom_s3_spinor_toy/tests/test_av1c_prime_cross_bilinear.py` — **12/12, 0.49s**
**Raw data:** `av1c_prime_cross_bilinear_results.json`
**Null result:** `null_results/20260610-ht1-sparse-bilinear.md`
**Status:** research_only — no physical promotion

---

## Verdict

```
PRIMARY (D2, pre-registered): residual 13.0% > 10%  →  KILL
H-T1 (sparse form) = NOT_PROMOTED, recorded in null_results/
```

## Results

| Dictionary | elements | greedy 5-term | full LS | const in top-5 | residual peak α/π |
|---|---|---|---|---|---|
| D1 pure boundary bilinears | 15 | 37.9% | 37.9% | n/a | 0.365 |
| **D2 = D1 + const (PRIMARY)** | 16 | **13.0%** | 13.0% | yes | **0.500** |
| D3 extended + const | 121 | 8.9% | **0.05%** | yes | 0.500 |

Sensitivity: fine grid (8000) — unchanged; unweighted L² — also KILL (>10%). Convention-robust.

## Both pre-registered mechanism predictions CONFIRMED

**P1 — boundary-exponent obstruction [VERIFIED-tool]:**
Every bilinear vanishes ≥ cos²α at α→π/2; target sin(2α) vanishes as cos¹α.
Prediction: residual concentrates at α = π/2. Observed: peak at α/π = 0.500
exactly, in both D2 and D3. The obstruction is structural — sparse bilinear
truncations cannot fix a boundary-exponent mismatch.

**P2 — f^(φ) constant term is load-bearing [VERIFIED-tool]:**
Adding the single constant function (Tom's f^(φ) in eq. 49) drops the
residual ~3×: 37.9% → 13.0%. Greedy picks it immediately. This is direct
numerical support for the NECESSITY of the scalar term in Tom's expansion —
pure bilinears cannot represent the radial density.

## The refined picture (what replaces H-T1)

```
eq. 49 radial layer on S³ = constant f^(φ) + DENSE bilinear series
  - the span of (extended bilinears + const) contains the target
    (full-LS residual 5e-4; caveat: ill-conditioned 121-element Gram)
  - but NO sparse (≤5-term) truncation reaches <10%
  - convergence is slow at α = π/2 (boundary layer)
```

The linear-level finding (AV-1a) is untouched: tom_ansatz itself remains
φ₁₁-dominated and dictionary-robust. The kill applies only to the SPARSE
bilinear hypothesis for the squared target.

## Message for Tom (when angular sector is eventually closed)

Two structural facts about eq. 49 on the S³ factor, radial layer:
1. The scalar f^(φ) term is not optional — bilinears alone miss the
   boundary behavior of √||g|| (cos-exponent argument + numerics).
2. The bilinear part of the expansion is dense, not dominated by a few
   modes — sparse mode-truncations of eq. 49 will misrepresent the
   α → π/2 region.

## What This Does NOT Mean

1. No full spinor identification; angular sector (AV-2) still pending.
2. Nothing about S⁶, f^{αχ} cross-couplings, or 4D physics.
3. λ = FREE_COUPLING_PARAMETER; research_only.
4. D3 full-LS 0.05% is span-membership evidence, not a sparse-structure claim.
