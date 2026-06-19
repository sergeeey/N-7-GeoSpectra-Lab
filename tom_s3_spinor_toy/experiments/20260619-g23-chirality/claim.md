# G23 — Claim: Chiral decomposition of H_F from γ_F

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:** The Z₂ grading γ_F of the finite spectral triple (KO-dim 6, G18) decomposes
H_F = ℂ^{32} into equal L and R chiral sectors (Witten index = 0). SM chirality is NOT
from spinor count asymmetry but from the gauge quantum numbers: SU(2)_L acts exclusively
on H_F^- (γ_F = −1, states 0-15), while SU(2)_R acts exclusively on H_F^+ (γ_F = +1,
states 16-31). The Yukawa D_F is off-diagonal in chirality ({D_F, γ_F} = 0).

## Setup

- H_F = ℂ^{32} = S³_4 ⊗ S⁶_8 (one SM generation, from G11-G21)
- γ_F = diag(−I_{16}, +I_{16}) (from G18, KO-dim 6 spectral triple)
- J_F = charge conjugation permutation matrix (G18, J_F² = I, {J_F, γ_F} = 0)
- D_F = SM Yukawa (G18, 4 free couplings Y_ν, Y_e, Y_u, Y_d)
- Gauge algebra: SU(2)_L × SU(2)_R × SU(3) × U(1)_{B-L} (Pati-Salam, 15 generators)

## Results [VERIFIED-numpy, 2026-06-19]

### Chiral partition

| Sector | States | dim | γ_F eigenvalue | S³ components |
|---|---|---|---|---|
| H_F^- (L) | 0–15 | 16 | −1 | 0, 1 (ν_L,e_L,d̄_L,u_L + colors) |
| H_F^+ (R) | 16–31 | 16 | +1 | 2, 3 (ν_R,e_R,d̄_R,u_R + colors) |

**Witten index = dim(H_F^+) − dim(H_F^-) = 16 − 16 = 0**

### Algebraic relations

| Relation | Value |
|---|---|
| γ_F² = I | True (Z₂ grading) |
| {D_F, γ_F} = 0 | True (Yukawa maps L↔R) |
| {J_F, γ_F} = 0 | True (KO-dim 6, CPT flips chirality) |
| max [γ_F, G] over all 15 PS gens | 0.000e+00 (chirality is gauge-invariant) |
| max D_F[L,L] | 0.000e+00 (no intra-L Yukawa) |
| max D_F[R,R] | 0.000e+00 (no intra-R Yukawa) |
| max D_F[L,R] | 1.000e+00 (Yukawa L←R coupling) |
| max D_F[R,L] | 1.000e+00 (Yukawa R←L coupling) |

### SM chirality assignment (gauge sectors)

- **SU(2)_L ⊂ End(H_F^-):** J_1, J_2, J_3 act ONLY within states 0-15.
  All off-diagonal blocks J_k[R,R], J_k[R,L], J_k[L,R] = 0 exactly.
- **SU(2)_R ⊂ End(H_F^+):** K_1, K_2, K_3 act ONLY within states 16-31.
  All off-diagonal blocks K_k[L,L], K_k[L,R], K_k[R,L] = 0 exactly.
- **SU(3) × U(1)_{B-L}:** generators act within each sector independently
  (color and B-L are chirality-neutral).

## Physical interpretation

The Witten vanishing theorem (1985) states that on a compact Riemannian manifold of
positive scalar curvature, the index of the Dirac operator is zero. S³×S⁶ has positive
curvature, so ind(D) = 0 is required — our H_F satisfies this automatically.

**SM chirality does NOT arise from an imbalance of L and R spinors** (both = 16).
It arises from the fact that the electroweak SU(2) representations are chiral:
SU(2)_L sees only the L-sector, SU(2)_R only the R-sector.

This is the geometric origin of SM chiral gauge theory from S³×S⁶ spinor geometry:
the grading γ_F selects which sector each electroweak SU(2) acts on, while the total
Hilbert space remains balanced (Witten index = 0).

## Gates summary

| Gate | Assertion | Result |
|---|---|---|
| C1 | γ_F² = I (Z₂ grading property) | PASS |
| C2 | {D_F, γ_F} = 0 (Yukawa flips chirality) | PASS |
| C3 | {J_F, γ_F} = 0 (KO-dim 6 relation) | PASS |
| C4 | [γ_F, G] = 0 for all 15 Pati-Salam generators | PASS |
| C5 | Witten index = 0 (dim H_F^+ = dim H_F^- = 16) | PASS |
| C6 | SU(2)_L ⊂ End(H_F^-) (L-sector only) | PASS |
| C7 | SU(2)_R ⊂ End(H_F^+) (R-sector only) | PASS |

## What this does NOT mean

1. Does NOT derive SM chirality from first principles — we put in γ_F from G18 (KO-dim 6
   is an axiom of the NCG spectral triple, not derived from S³×S⁶ alone here).
2. Does NOT explain why SU(2)_L but not SU(2)_R is gauged in the SM — only that each
   acts within a specific chiral sector, consistent with the Pati-Salam breaking pattern.
3. Does NOT reproduce three generations — H_F = ℂ^{32} is one generation.
4. Does NOT imply massless neutrinos — D_F has Y_ν coupling connecting ν_L↔ν_R.
5. sm_derivation_claimed = False throughout.

**Status:** PASS_G23_CHIRALITY (7/7)
[VERIFIED-numpy, 2026-06-19, tests: test_g23_chirality.py]
