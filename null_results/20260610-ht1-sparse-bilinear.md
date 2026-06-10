# NULL RESULT — H-T1 Sparse Boundary-Family Bilinear Structure

**ID:** 20260610-ht1-sparse-bilinear
**Date:** 2026-06-10
**Verdict:** REJECT (sparse form)
**Pre-registration:** experiments/20260610-spinor-geometry-pivot-v0.2.0/claim_av1c_prime.md
**Evidence:** [VERIFIED-tool] — av1c_prime_cross_bilinear.py, 12/12 tests

## Claim that was killed

*"The radial layer of Tom's eq. (49) — sin(2α) = 2√||g|| on S³ — admits a
SPARSE (≤5-term) reconstruction over cross-bilinears of the n=l
boundary-family Dirac modes."*

## Why it was falsified

| Dictionary | 5-term residual | Pre-registered threshold |
|---|---|---|
| D1 pure boundary bilinears | 37.9% | — |
| D2 + constant f^(φ) (PRIMARY) | **13.0%** | KILL if > 10% |
| D3 extended + constant | 8.9% | (sensitivity, not primary) |

Root cause (analytic, pre-registered as P1, numerically confirmed):
every bilinear φ_{nl}·φ_{n'l'} vanishes ≥ cos²α at α→π/2 while the target
vanishes as cos¹α. Residual peaks at exactly α = π/2 in all dictionaries
with constant. No sparse bilinear truncation can fix a boundary-exponent
mismatch — convergence at the boundary is slow and distributed.

## What SURVIVED the kill (do not lose this)

1. **P2 CONFIRMED:** the constant f^(φ) term in eq. 49 is load-bearing
   (37.9% → 13.0% when added). Numerical support for the necessity of the
   scalar term in Tom's expansion.
2. **Dense representability:** full LS over D3 (120 pairs + const) gives
   residual ~5e-4 — the target IS in the span. Eq. 49 radial layer is a
   DENSE bilinear series, not a sparse one. (Caveat: ill-conditioned Gram.)
3. AV-1a finding untouched: tom_ansatz (not its square) remains
   φ₁₁-dominated, dictionary-robust.

## Retry condition

Do NOT retry sparse reconstruction with bigger bilinear dictionaries — the
boundary-exponent obstruction is structural. A fundamentally different
approach would be required, e.g.:
- weighted/fractional dictionaries with cos¹ boundary behavior, or
- reformulating the target (expand √||g|| instead of 2√||g||... i.e. tom
  ansatz itself, which AV-1a already handles at the linear level), or
- the full angular treatment (AV-2) where half-integer weights change the
  boundary exponents.
