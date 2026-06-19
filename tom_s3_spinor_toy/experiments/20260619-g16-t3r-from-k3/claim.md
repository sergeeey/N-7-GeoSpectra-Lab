# G16 — Claim: T3R from S³ K-generators, completing Y = T3R + (B−L)/2

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:** The K₃ eigenvalue of the SU(2)_R generator (G11) gives T3R = ±1/2 for
the right-handed sector of the 32-dim S³×S⁶ spinor. Combined with B−L from G15,
the hypercharge

  Y = K₃^{32} + (B−L)/2

is a purely geometric operator on S³×S⁶, with no additional assumptions.

## 32-dim spinor decomposition

In the kron(S³_4, S⁶_8) basis (row = S³_index × 8 + S⁶_index):

| Rows | S³ state | T3L | T3R |
|------|----------|-----|-----|
| 0–7 | \|L,↑⟩⊗S⁶ | +1/2 | 0 |
| 8–15 | \|L,↓⟩⊗S⁶ | −1/2 | 0 |
| 16–23 | \|R,↑⟩⊗S⁶ | 0 | **+1/2** |
| 24–31 | \|R,↓⟩⊗S⁶ | 0 | **−1/2** |

## Right-handed sector Y table (T6 + T7)

| State | Row | T3R | B−L | Y = T3R + B−L/2 | SM |
|-------|-----|-----|-----|------------------|----|
| ν_R | 16 | +1/2 | −1 | **0** | ✓ |
| u_R (×3) | 19,21,22 | +1/2 | +1/3 | **+2/3** | ✓ |
| d̄_R (×3) | 17,18,20 | +1/2 | −1/3 | **+1/3** | CPT |
| ē_R | 23 | +1/2 | +1 | **+1** | CPT |
| e_R | 24 | −1/2 | −1 | **−1** | ✓ |
| d_R (×3) | 27,29,30 | −1/2 | +1/3 | **−1/3** | ✓ |
| ū_R (×3) | 25,26,28 | −1/2 | −1/3 | **−2/3** | CPT |
| ν̄_R | 31 | −1/2 | +1 | **0** | CPT |

Right-handed sector = one generation SM fermions + CPT conjugates (16 states = 4×2×2 color).

## Left-handed sector bonus (T8)

With T3R=0: Y = B−L/2 reproduces SM left-handed doublet hypercharges:
- Lepton doublet (B−L=−1): Y = −1/2 ✓
- Quark doublet (B−L=+1/3): Y = +1/6 ✓

## Gates summary

All 10/10 gates PASS [VERIFIED-sympy, 2026-06-19]:

| Gate | Content | Result |
|------|---------|--------|
| T1 | K₃^{32} is diagonal | PASS |
| T2 | Eigenvalues: 16×0 + 8×(+1/2) + 8×(−1/2) | PASS |
| T3 | [K₃^{32}, J₃^{32}] = 0 (T3R ⊥ T3L) | PASS |
| T4 | [K₃^{32}, C_i^{32}] = 0 for all 8 SU(3) generators | PASS |
| T5 | Y_32 = K₃^{32} + BmL_32/2 is diagonal | PASS |
| T6 | SM right-handed fermion Y: ν_R(0), u_R(+2/3), e_R(−1), d_R(−1/3) | PASS |
| T7 | SM antifermion Y: ν̄_R(0), ē_R(+1), ū_R(−2/3), d̄_R(+1/3) | PASS |
| T8 | Left sector: lepton Y=−1/2, quark Y=+1/6 (SM doublets) | PASS |
| T9 | [Y_32, C_i^{32}] = 0 (charge-color separation) | PASS |
| T10 | Y_32 is Hermitian | PASS |

## Check

`python g16_t3r_k3.py` → `PASS_G16_T3R_GEOMETRIC_ORIGIN` (10/10)
`pytest tests/test_g16_t3r_k3.py` → 20 passed
`pytest tests/` → 870 passed, 2 skipped

## Connection to prior gates

| Gate | G16 connection |
|------|----------------|
| G11 | K_S3[2] (K₃, 4×4) directly provides T3R eigenvalues ±1/2 in R block |
| G15 | BmL (8×8) extends to BmL_32 = kron(I4, BmL); T8 identity reused |
| G12 | Anomaly cancellation on 32-component spinor consistent with Y structure |
| G13 | \|111⟩ zero mode = ν̄_R (Y=0) at row 31 via T3R=−1/2, B−L=+1 |
| G14 | Quark triplet {3,5,6} → u_R rows {19,21,22} and d_R rows {27,29,30} |

## What this does NOT mean

1. Does NOT fix λ — λ = FREE_COUPLING_PARAMETER throughout.
2. Does NOT derive the left-handed T3L structure from geometry — J_S3 is taken from G11
   without an independent topological argument (analogous gap as T3R was before G16).
3. Does NOT address fermion masses, Yukawa couplings, or the Higgs mechanism.
4. Does NOT prove the SM gauge group is SU(3)×SU(2)×U(1) — only the quantum numbers
   of one generation of right-handed fermions are correctly assigned.
5. Does NOT identify which states are particles vs. antiparticles in a Lagrangian sense —
   the 32-component spinor contains both; CPT conjugation maps rows by the chirality operator.
6. Does NOT show B−L is conserved in the full S³×S⁶ compactification — λ-dependent.
7. sm_derivation_claimed = False throughout.

**Status:** PASS_G16_T3R_GEOMETRIC_ORIGIN
[VERIFIED-sympy, 2026-06-19, 10/10 gates, 20 tests]
