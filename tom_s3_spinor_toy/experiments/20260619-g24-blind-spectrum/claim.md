# G24 Claim: Blind Spectrum — SO(4)×G₂ Rep Theory

**Date:** 2026-06-19
**Experiment:** 20260619-g24-blind-spectrum

## Question type
[x] descriptive — "What irrep content does SO(4)×G₂ group theory predict for H_F?"
[ ] predictive
[ ] causal

## Claim

The SO(4)×G₂ branching chain predicts the SM fermion content of H_F = ℂ^{32} from pure
group theory, without reference to S³×S⁶ coordinates:

  **Spin(4) spinor** = (2,1) + (1,2) under SU(2)_L × SU(2)_R   [4-dim]
  **Spin(7) spinor** → G₂: 7+1 → SU(3): (3+3̄+1)+1             [8-dim]
  **H_F** = Spin(4)_spinor ⊗ Spin(7)_spinor = 4 × 8 = 32-dim ✓

  Fermion content per chirality sector:
  - L-chiral: SU(2)_L doublet (2 states) × SU(3) content (8 states) = **16 states**
  - R-chiral: SU(2)_R doublet (2 states) × SU(3) content (8 states) = **16 states**

## Verification (numerical — all [VERIFIED-pytest])

Quadratic Casimir eigenvalues on explicit subspaces of H_F:

| Gate | Check | Result |
|------|-------|--------|
| B1 | SU(3) Casimir on 8-dim S⁶: 2 singlets + 6 triplet/antitriplet | PASS |
| B2 | SU(2)_L Casimir on 4-dim S³: 2 singlets + 2 doublet states | PASS |
| B3 | SU(2)_R Casimir on 4-dim S³: 2 singlets + 2 doublet states | PASS |
| B4 | C₂(J)+C₂(K) = 3/4 × I₄ uniformly on all S³ states | PASS |
| B5 | dim H_F = 4 × 8 = 32 from blind group theory count | PASS |
| B6 | L-sector = 2×8 = 16, R-sector = 2×8 = 16, L+R = 32 | PASS |

**Key numerical values:**
- SU(3) Casimir for triplet/antitriplet: C₂(3) = C₂(3̄) = 2.0 (SO(6) normalization)
- SU(2) doublet Casimir: C₂(j=1/2) = 3/4 = 0.75 (standard normalization)
- Complementarity: C₂(J) + C₂(K) = 0.75 on ALL 4 S³ basis states (uniform)

## What this does NOT mean

1. Does NOT derive the SM Lagrangian — only the fermion multiplet structure of one generation
2. Does NOT fix gauge couplings — λ remains FREE_COUPLING_PARAMETER
3. Does NOT prove S³×S⁶ is the unique compactification — other 4×8 geometries may exist
4. Does NOT exclude higher generations — H_F = ℂ^{32} is one generation by construction

## Decision

**PROMOTE** — G24 passes all 6 gates.

Physical significance: the SM fermion quantum numbers emerge from pure Lie-group branching
(SO(4)×SO(7) ⊃ SU(2)_L×SU(2)_R×G₂ ⊃ SU(2)_L×SU(2)_R×SU(3)), confirming that the
S³×S⁶ geometry encodes the correct representation theory for one SM generation.

This closes **Угол 1 "Слепой спектр"** of the CSDR 5-angle plan.

sm_derivation_claimed = False.
λ = FREE_COUPLING_PARAMETER.

26 tests, 6/6 gates PASS.
