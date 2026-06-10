# AV-1c′ — Pre-registered Claim: Cross-Bilinear Dictionary for eq. 49 Radial Layer

**Experiment:** AV1C_PRIME_CROSS_BILINEAR_DICTIONARY
**Date pre-registered:** 2026-06-10 (BEFORE running code; written after AV-1 commit 7fa4360)
**Question type:** [x] descriptive  [ ] predictive  [ ] causal
**Status:** research_only — no physical promotion

---

## Context

AV-1c FAILED its pre-registered threshold: diagonal bilinears {φ_{nl}²} give
5-term residual 12.38% > 10% against target sin(2α) = tom_ansatz² = 2√||g||.
Hypothesis: Tom's eq. (49) radial layer requires cross-bilinears φ_{nl}·φ_{n'l'}.

## Analytic Prior (declared BEFORE running)

Boundary-exponent obstruction: every radial mode φ_{nl} ∝ cos^{l+1}α near
α = π/2, so EVERY bilinear vanishes at least as cos²α there. The target
sin(2α) vanishes only as cos¹α. Therefore:

1. **Prediction P1:** pointwise mismatch is structural at α → π/2 for any
   pure-bilinear dictionary; the residual should concentrate near α = π/2.
2. **Prediction P2:** Tom's eq. (49) contains a scalar term f^(φ) BEFORE the
   bilinear sum. The constant function has cos⁰ boundary behavior — adding it
   to the dictionary is faithful to eq. 49 AND is the only available term
   that can compensate the cos¹ boundary layer in L².

If the constant-augmented dictionary (D2) succeeds where pure bilinears (D1)
fail, that is direct numerical support for the NECESSITY of the f^(φ) term
in eq. 49 — a structural statement about Tom's expansion.

## Dictionaries (pre-registered)

- **D1** — pure cross-bilinears of the boundary family
  B = {(0,0), (1,1), (2,2), (3,3), (4,4)}: all 15 unordered pairs φ_a·φ_b.
- **D2 (PRIMARY)** — D1 ∪ {constant 1} (16 elements; faithful to eq. 49:
  f^(φ) + Σ f^{(ψ)} ψψ).
- **D3 (extension, sensitivity)** — near-boundary modes
  {(n,l): 0 ≤ l ≤ 4, l ≤ n ≤ l+2} (15 modes → 120 pairs) ∪ {constant}.

## Endpoints and Verdict Rules (pre-registered)

Primary endpoint: greedy 5-term residual of normalized sin(2α) under D2,
weighted L²(sinα cosα dα).

| Outcome | Verdict |
|---|---|
| residual < 5% with ≤ 5 terms | **PROMOTE H-T1 → RADIAL_BILINEAR_STRUCTURE_SUPPORTED** (still NOT full angular identification) |
| 5% ≤ residual ≤ 10% | IMPROVED_BUT_INSUFFICIENT — H-T1 stays EXPLORATORY |
| residual > 10% | KILL — H-T1 stays NOT_PROMOTED; record constraint in null-results note |

Secondary (mechanism check, P1/P2):
- D1 vs D2 comparison: if D2 ≪ D1 residual → constant term is load-bearing → P2 supported.
- Residual spatial profile: max |residual(α)| location reported; P1 predicts near π/2.

## Sensitivity (≥2, pre-registered)

1. Unweighted L²(dα).
2. Grid refinement n_grid 4000 → 8000.

## Natural Language Statement

*We estimate the L² reconstruction residual of sin(2α) (the radial density
in Tom's eq. 49 on S³) over a sparse dictionary of cross-bilinears of
boundary-family Dirac radial modes, with and without the constant f^(φ)
term, comparing greedy 5-term reconstructions; deterministic numerics, no ICE.*

## What This Does NOT Mean (pre-declared)

1. PROMOTE here ≠ full spinor identification; angular sector (AV-2) stays pending.
2. Nothing about S⁶, f^{αχ} cross-couplings, or 4D physics.
3. Does NOT claim Tom's ansatz "solved"; λ = FREE_COUPLING_PARAMETER.
4. The dictionary choice (boundary family) is motivated by AV-1a ranking —
   D3 sensitivity guards against this selection being the bottleneck.
