# G20 — Claim: Yukawa intertwiner space dim = 4 from S³×S⁶ geometry + J_F

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:** The space of SU(3)-invariant, bidoublet-valued operators on H_F = kron(S³_4, S⁶_8)
that satisfy the J_F real-structure constraint ([D_F, J_F] = 0, KO-dim 6) has exactly
4 independent dimensions, corresponding to {Y_nu, Y_e, Y_u, Y_d}.

## Three-step reduction

### Step 1 — SU(3)-invariance + bidoublet filter → 16 pairs

SU(3)-invariant operators on S⁶_8 must, by Schur's lemma, act as the identity on each
irreducible subspace. In the natural S⁶ basis, this means the operator is diagonal with
the same value on each irrep: requires i_L % 8 == j_R % 8 (same S⁶ fiber index).

*Note:* dBL = 0 is a **consequence** of same S⁶ index, not an independent filter.
B−L depends only on the S⁶ index (BmL_32 = kron(I₄, BmL), from G15), so sharing
the same index forces identical B−L charges → dBL = 0.

The bidoublet condition (|dT3L| = |dT3R| = 1/2, dT3L + dT3R = 0) selects L→R pairs.

Result: 16 valid pairs — exactly the YUKAWA_PAIRS from G18.

### Step 2 — Group into SU(3) orbits → 8 independent parameters

All pairs sharing the same (S³-chirality, B−L) carry the same coupling by Schur's lemma.
S⁶ fiber decomposes as:
- 1_a: S⁶ index 0, B−L = −1 (leptonic singlet, ν-type)
- 3̄:  S⁶ indices {1,2,4}, B−L = −1/3 (d̄-type quarks)
- 3:   S⁶ indices {3,5,6}, B−L = +1/3 (u-type quarks)
- 1_b: S⁶ index 7, B−L = +1 (antileptonic singlet, ν̄-type)

With two S³-chirality classes (L_UP/R_UP and L_DN/R_DN), there are 8 SU(3) orbits:
- 4 singleton orbits (|B−L| = 1): one pair each
- 4 triplet orbits (|B−L| = 1/3): three pairs each (color-degenerate)

### Step 3 — J_F real-structure links orbits → 4 independent coupling groups

The constraint [D_F, J_F] = 0 (from G18 Gate K5) links each orbit to exactly its
CPT-partner orbit. The 8 → 4 pairing:

| Group | Coupling | Orbits linked by J_F | Pairs |
|-------|----------|---------------------|-------|
| 1 | Y_e | (L_DN,R_DN,B−L=−1) ↔ (L_UP,R_UP,B−L=+1) | 2 |
| 2 | Y_u | (L_DN,R_DN,B−L=−1/3) ↔ (L_UP,R_UP,B−L=+1/3) | 6 |
| 3 | Y_nu | (L_DN,R_DN,B−L=+1) ↔ (L_UP,R_UP,B−L=−1) | 2 |
| 4 | Y_d | (L_DN,R_DN,B−L=+1/3) ↔ (L_UP,R_UP,B−L=−1/3) | 6 |

Pair counts: 2 + 6 + 2 + 6 = 16. Number of free Yukawa couplings: **4**.

## Two forbidden S⁶ channels

End_{SU(3)}(S⁶_8) has dimension 6:
- E_aa (1_a→1_a), E_bb (1_b→1_b), E_33 (3→3), E_3̄3̄ (3̄→3̄) → dBL=0, **ALLOWED** (4 basis elements)
- E_ab (1_a→1_b), dBL = +2 → **FORBIDDEN** (ΔL=2)
- E_ba (1_b→1_a), dBL = −2 → **FORBIDDEN** (ΔL=2)

The forbidden channels correspond to lepton-number-violating operators with |dBL|=2.
Their absence is **geometric** — they require the mediating scalar to carry B−L charge ±2,
which would make it a non-singlet under the U(1)_{B−L} group derived from S⁶ geometry (G15).

## Gates summary

All 5/5 gates PASS [VERIFIED-sympy, 2026-06-19]:

| Gate | Content | Result |
|------|---------|--------|
| M1 | \|VALID_PAIRS\| = 16 (same S⁶ index + bidoublet filter) | PASS |
| M2 | VALID_PAIRS == G18 YUKAWA_PAIRS exactly (set match) | PASS |
| M3 | 8 SU(3) orbits; 4 singletons (size 1) + 4 triplets (size 3) | PASS |
| M4 | J_F → 4 coupling groups; pair counts = [2,2,6,6] | PASS |
| M5 | Singlet cross-channels absent; |dBL|=2 (lepton-number-violating) | PASS |

## Check

`python g20_yukawa_intertwiner.py` → `PASS_G20_YUKAWA_INTERTWINER (5/5)`
`pytest tests/test_g20_yukawa_intertwiner.py` → TBD
`pytest tests/` → TBD (expected 929 + N_new)

## What this does NOT mean

1. Does NOT derive the values of {Y_nu, Y_e, Y_u, Y_d} — they are free parameters.
2. Does NOT extend to 3 generations — H_F = ℂ^32 covers one generation only.
3. Does NOT fix the relative magnitudes between generations — mass hierarchy is unexplained.
4. Does NOT explain why SU(3) color appears in this form — the S⁶ spinor structure is
   assumed, not derived from a fiber bundle over a manifold.
5. Does NOT constrain neutrino masses — Y_nu is free (and may be zero by separate argument).
6. sm_derivation_claimed = False throughout.

**Status:** PASS_G20_YUKAWA_INTERTWINER
[VERIFIED-sympy, 2026-06-19, 5/5 gates]
