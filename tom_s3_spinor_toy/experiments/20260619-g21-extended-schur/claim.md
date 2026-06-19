# G21 — Claim: Extended Schur — dim(End_G(H_F)) reveals role of B−L geometry

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:** The commutant of SU(2)_L × SU(2)_R × SU(3) acting on H_F = ℂ^{32} has
dimension 12. Adding U(1)_{B−L} (from S⁶ geometry, G15) reduces it to 8.

## Method

For each generator G_k of the group, construct the linear map [G_k, ·]: End(H_F) → End(H_F)
via the commutator super-operator (I⊗G − G^T⊗I) on the vectorized space ℂ^{1024}.
The commutant = joint null space of all these maps.
Dimension computed via SVD rank of the stacked constraint matrix.

## Results (numerical, [VERIFIED-numpy, 2026-06-19])

| Generator set | dim(commutant) | Schur decomposition |
|---|---|---|
| Cartan (J3, K3, BmL only) | 80 | 4 sectors × (9+9+1+1) = 80 |
| SU(2)_L × SU(2)_R × SU(3) | **12** | M₂(ℂ) ⊕ ℂ ⊕ ℂ ⊕ M₂(ℂ) ⊕ ℂ ⊕ ℂ |
| + U(1)_{B−L} | **8** | ℂ^8 (one scalar per irrep) |

### Why 12 without B−L

Under SU(2)_L × SU(2)_R × SU(3), the S⁶ fiber decomposes into 4 SU(3) sectors:
1_a (B−L=−1) and 1_b (B−L=+1) are BOTH trivial under SU(3) — indistinguishable.

Distinct SU(2)_L × SU(2)_R × SU(3) irreps in H_F and their multiplicities:

| Irrep | Multiplicity | Commutant contribution |
|---|---|---|
| (j_L=½, 0, SU(3)-singlet) | **2** (1_a and 1_b) | 2² = 4 |
| (j_L=½, 0, SU(3)-3̄) | 1 | 1 |
| (j_L=½, 0, SU(3)-3) | 1 | 1 |
| (0, j_R=½, SU(3)-singlet) | **2** | 2² = 4 |
| (0, j_R=½, SU(3)-3̄) | 1 | 1 |
| (0, j_R=½, SU(3)-3) | 1 | 1 |
| **Total** | | **12** |

### Why 8 with B−L

U(1)_{B−L} distinguishes 1_a (B−L=−1) from 1_b (B−L=+1). All 8 irreps now distinct,
each with multiplicity 1. Commutant ≅ ℂ^8 — one free parameter per SM particle type.

The 4-unit reduction (12→8) = two M₂(ℂ) blocks resolved into 4 scalars.
Each M₂(ℂ) → 2 scalars: net change per block = 4−2 = 2, two blocks → 4. ✓

## Physical meaning

The 8 irreps correspond to the 8 SM fermion types in one generation:

| Irrep | B−L | SM particle |
|---|---|---|
| (j_L=½, 0, 1, B−L=−1) | −1 | ν_L |
| (j_L=½, 0, 3̄, B−L=−1/3) | −1/3 | d̄_L (×3 colors, same coupling) |
| (j_L=½, 0, 3, B−L=+1/3) | +1/3 | u_L (×3 colors) |
| (j_L=½, 0, 1, B−L=+1) | +1 | ē_L |
| (0, j_R=½, 1, B−L=−1) | −1 | ν_R |
| (0, j_R=½, 3̄, B−L=−1/3) | −1/3 | d̄_R (×3 colors) |
| (0, j_R=½, 3, B−L=+1/3) | +1/3 | u_R (×3 colors) |
| (0, j_R=½, 1, B−L=+1) | +1 | ē_R |

Each has exactly one free parameter in the commutant ↔ one free mass scale (Yukawa coupling).

## Relation to G20

G20 counted the intertwiner space dim(Hom_G(H_L, H_R)) = 4 (the Yukawa coupling count).
G21 counts the commutant dim(End_G(H_F)) = 8 (independent mass scales in the full Hamiltonian).
These are DIFFERENT questions:
- Commutant = "how many diagonal scalings preserve the symmetry?" (8)
- Intertwiners = "how many L→R Yukawa operators preserve the symmetry?" (4)

The Yukawa count 4 follows from the fact that each of the 8 mass parameters pairs with its
CPT partner (J_F links them, G18 Gate K5), giving 8/2 = 4 independent Yukawa couplings.

## Gates summary [VERIFIED-numpy, 2026-06-19]

| Gate | Assertion | Result |
|---|---|---|
| E1 | dim(End_{J3,K3,BmL}(H_F)) = 80 | PASS |
| E2 | dim(End_{SU(2)_L×SU(2)_R×SU(3)}(H_F)) = 12 | PASS |
| E3 | dim(End_{SU(2)_L×SU(2)_R×SU(3)×U(1)_{B-L}}(H_F)) = 8 | PASS |
| E4 | Reduction from adding B-L = 4 (two M₂(ℂ) → 4 scalars) | PASS |
| E5 | 8 = 8 irrep types × 1² | PASS |

## What this does NOT mean

1. Does NOT prove the Higgs representation is uniquely forced — the commutant measures
   diagonal scalings, not the off-diagonal L→R intertwiners (that was G20).
2. Does NOT derive mass values — the 8 free parameters remain free.
3. Does NOT extend to 3 generations — H_F = ℂ^{32} covers one generation.
4. Does NOT explain S³ × S⁶ compactification — assumes the product structure.
5. sm_derivation_claimed = False throughout.

**Status:** PASS_G21_EXTENDED_SCHUR (5/5)
[VERIFIED-numpy, 2026-06-19, SVD on 14336×1024 system]
