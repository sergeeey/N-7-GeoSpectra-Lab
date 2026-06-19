# G18 — Claim: NCG finite Dirac operator D_F on the 32-dim S³×S⁶ spinor

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:** The 32-dimensional S³×S⁶ spinor H_F carries the objects of the SM finite
spectral triple (γ_F, J_F, D_F) satisfying the KO-dimension 6 constraints. D_F is
a Hermitian 32×32 matrix with 4 free Yukawa couplings connecting L↔R sectors exactly
along the SM fermion-antifermion pairings identified in G11–G17.

## Core objects

### Chirality γ_F

```
γ_F = diag(−1×16, +1×16)
     = −1 on L-sector (rows 0–15, T3L ≠ 0)
     = +1 on R-sector (rows 16–31, T3R ≠ 0)
```

### Charge conjugation J_F (16 CPT transpositions)

| Particle | Row | CPT partner | Row |
|----------|-----|-------------|-----|
| ν_L | 0 | ν̄_R | 31 |
| ν̄_L | 15 | ν_R | 16 |
| e_L | 8 | ē_R | 23 |
| ē_L | 7 | e_R | 24 |
| u_L (color 1,2,3) | 3,5,6 | ū_R | 25,26,28 |
| ū_L (color 1,2,3) | 9,10,12 | u_R | 19,21,22 |
| d_L (color 1,2,3) | 11,13,14 | d̄_R | 17,18,20 |
| d̄_L (color 1,2,3) | 1,2,4 | d_R | 27,29,30 |

### Finite Dirac operator D_F (Yukawa structure)

D_F is zero on L×L and R×R blocks. Non-zero entries connect L-row ↔ R-row
with equal Q and equal B−L:

| Particle pair | L-row(s) | R-row(s) | Coupling |
|---------------|----------|----------|---------|
| ν Dirac | 0, 15 | 16, 31 | Y_nu |
| e lepton | 8, 7 | 24, 23 | Y_e |
| u quark (×3 colors) | 3,5,6 / 9,10,12 | 19,21,22 / 25,26,28 | Y_u |
| d quark (×3 colors) | 11,13,14 / 1,2,4 | 27,29,30 / 17,18,20 | Y_d |

Total: 16 non-zero matrix elements (8 particle pairs + 8 CPT-partner pairs).

## Gates summary

All 8/8 gates PASS [VERIFIED-sympy, 2026-06-19]:

| Gate | Content | Result |
|------|---------|--------|
| T1 | γ_F² = I₃₂ | PASS |
| T2 | {D_F, γ_F} = 0 — D_F is chiral | PASS |
| T3 | D_F = D_F† — Hermitian | PASS |
| T4 | [D_F, Q_32] = 0 — charge conservation | PASS |
| T5 | J_F² = I₃₂ | PASS |
| T6 | {J_F, γ_F} = 0 — KO-dimension 6, ε' = −1 | PASS |
| T7 | [D_F, J_F] = 0 — KO-dimension 6, ε'' = +1 | PASS |
| T8 | Exactly 4 Yukawa couplings: {Y_nu, Y_e, Y_u, Y_d} | PASS |

## Check

`python g18_ncg.py` → `PASS_G18_NCG_DIRAC_DF (8/8)`
`pytest tests/test_g18_ncg.py` → 20 passed
`pytest tests/` → 910 passed, 2 skipped

## Physical interpretation

In the Connes-Chamseddine-Marcolli NCG approach to the SM, the Higgs boson
is an **inner fluctuation** of D_F: after replacing D_F → D_F + A, where A
is a bounded operator built from the algebra A_F = ℂ⊕ℍ⊕M₃(ℂ) acting on H_F,
the off-diagonal Yukawa entries become Yukawa couplings multiplied by the Higgs
field φ. The mass eigenvalues of D_F + A give fermion masses once φ acquires a VEV.

Our H_F = kron(S³_4, S⁶_8) is the same 32-dimensional space. The quantum numbers
from G11–G17 map exactly onto the NCG A_F representation, making D_F geometrically
natural rather than postulated.

## Connection to prior gates

| Gate | G18 connection |
|------|----------------|
| G11 | T3L sectors identify L-rows (0–15) for γ_F = −1 side |
| G15 | B−L distinguishes quarks from leptons in Yukawa pairs |
| G16 | Y = T3R + B−L/2 → correct Q for both L and R partners |
| G17 | Q[i] = Q[j] for all 16 Yukawa pairs — verified in T4 |
| G12 | 32-component anomaly-free spectrum = H_F of SM spectral triple |

## What this does NOT mean

1. Does NOT fix Y_nu, Y_e, Y_u, Y_d — these remain FREE_YUKAWA_PARAMETERS.
   Physical values require a moduli potential fixing λ and the Higgs VEV.
2. Does NOT include Majorana mass for ν_R — the D_F constructed here is
   purely Dirac. Majorana entry D_F[16, 31] = M_R would extend to seesaw.
3. Does NOT compute the Higgs mass — the spectral action ℐ_B[D_A] is not
   calculated here; it requires heat-kernel expansion on M⁴ × F.
4. Does NOT verify the first-order condition [[D_F, π(a)], J_F π(b) J_F⁻¹] = 0
   for all a, b ∈ A_F — this requires explicit algebra representation.
5. Does NOT produce three generations — H_F = ℂ^32 for 1 generation. Three
   generations require H_F = ℂ^96.
6. Does NOT fix the gauge group — A_F = ℂ⊕ℍ⊕M₃(ℂ) is assumed, not derived
   from S³×S⁶ geometry alone.
7. sm_derivation_claimed = False throughout.

**Status:** PASS_G18_NCG_DIRAC_DF
[VERIFIED-sympy, 2026-06-19, 8/8 gates, 20 tests, 910 total]
