# G19 — Claim: Higgs bidoublet from D_F Yukawa structure on S³×S⁶

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:** For every Yukawa pair (i_L, j_R) in D_F (G18), the mediating scalar φ
must carry quantum numbers dX = X[j_R] − X[i_L]. All 16 pairs require φ in the
(2, 2)₀ bidoublet of SU(2)_L × SU(2)_R — the Pati-Salam Higgs. After
SU(2)_R → U(1)_T3R breaking, the neutral component becomes the SM Higgs
doublet H with Y = +1/2: representation (1, 2)_{1/2}.

## Required Higgs quantum numbers per pair

For each (i_L, j_R) ∈ YUKAWA_PAIRS, compute dX = X[j_R] − X[i_L]:

| Fermion sector  | L-row | R-row | dT3L | dT3R | dBL | dY   | dQ |
|-----------------|-------|-------|------|------|-----|------|----|
| ν_L ↔ ν_R       |  0    |  16   | −1/2 | +1/2 |  0  | +1/2 | 0  |
| ē_L ↔ e_R       |  7    |  24   | −1/2 | +1/2 |  0  | +1/2 | 0  |
| ν̄_L ↔ ν̄_R      | 15    |  31   | +1/2 | −1/2 |  0  | −1/2 | 0  |
| e_L ↔ e_R       |  8    |  24   | +1/2 | −1/2 |  0  | −1/2 | 0  |
| u_L ↔ u_R ×3   | 3,5,6 |19,21,22| −1/2| +1/2 |  0  | +1/2 | 0  |
| ū_L ↔ ū_R ×3   |9,10,12|25,26,28| +1/2| −1/2 |  0  | −1/2 | 0  |
| d_L ↔ d_R ×3   |11,13,14|27,29,30| +1/2|−1/2 |  0  | −1/2 | 0  |
| d̄_L ↔ d̄_R ×3  |1,2,4  |17,18,20| −1/2| +1/2 |  0  | +1/2 | 0  |

All 16 pairs: dQ = 0, dBL = 0, |dT3L| = |dT3R| = 1/2, dT3L + dT3R = 0.

## Two bidoublet components

```
(dT3L, dT3R) = (−1/2, +1/2)  →  8 uptype pairs   (ν,u and their CPT partners ē,d̄)
(dT3L, dT3R) = (+1/2, −1/2)  →  8 downtype pairs  (e,d and their CPT partners ν̄,ū)
```

These are the anti-diagonal neutral components of the (2, 2)₀ bidoublet Φ:

```
Φ = [ Φ⁺   Φ⁰′ ]     Y = T3R + B−L/2 = ±1/2 + 0
    [ Φ⁰   Φ⁻  ]
```

Neutral (Q = 0) entries at (T3L = −1/2, T3R = +1/2) and (T3L = +1/2, T3R = −1/2).

## Gates summary

All 8/8 gates PASS [VERIFIED-sympy, 2026-06-19]:

| Gate | Content | Result |
|------|---------|--------|
| T1 | dQ = 0 for all 16 pairs — neutral Higgs only | PASS |
| T2 | \|dT3L\| = 1/2 for all pairs — SU(2)_L doublet | PASS |
| T3 | \|dT3R\| = 1/2 for all pairs — SU(2)_R doublet | PASS |
| T4 | dT3L + dT3R = 0 for all pairs — anti-diagonal bidoublet | PASS |
| T5 | dBL = 0 for all pairs — Higgs is B−L singlet (lives in S³) | PASS |
| T6 | dY = dT3R for all pairs — Y entirely from T3R when dBL = 0 | PASS |
| T7 | Exactly 2 distinct (dT3L, dT3R) values: {(−1/2,+1/2),(+1/2,−1/2)} | PASS |
| T8 | Equal split: 8 pairs per component | PASS |

## Check

`python g19_higgs_bidoublet.py` → `PASS_G19_HIGGS_BIDOUBLET (8/8)`
`pytest tests/test_g19_higgs_bidoublet.py` → 19 passed
`pytest tests/` → 929 passed, 2 skipped

## Geometric interpretation

**Why dBL = 0 for all Yukawa pairs:**

`BmL_32 = kron(I₄, BmL)` — the B−L operator lives entirely in the S⁶ fiber.
Both partners (i_L, j_R) in a Yukawa pair share the same S⁶ fiber index
(L/R sector differences are in S³, not S⁶):
- Row i_L is in S³-sector ⊗ S⁶-index
- Row j_R = i_L + 16 is in the flipped S³-sector ⊗ (same S⁶-index)

Therefore BmL[j_R] = BmL[i_L] → dBL = 0.

**Consequence:** the Higgs φ mediating Yukawa vertices has no S⁶ quantum numbers.
It is a **pure S³ object**, built entirely from SU(2)_L × SU(2)_R structure of S³.

**The bidoublet is the minimal representation:**
- |dT3L| = 1/2 rules out singlet (0) and adjoint (0,±1)
- |dT3R| = 1/2 rules out singlet and adjoint for SU(2)_R
- Combined (2, 2) is minimal: 4 components, 2 neutral (the ones we find)

## Connection to Pati-Salam symmetry breaking

Our S³×S⁶ spinor realizes:
```
SU(2)_L [from J-generators, G11] × SU(2)_R [from K-generators, G16] × U(1)_{B−L} [from G15]
```

G19 shows D_F requires φ ∈ (2, 2)₀ — the Pati-Salam Higgs bidoublet.
After SU(2)_R breaking:
- The (dT3L = −1/2, dT3R = +1/2) neutral component → H⁰ (SM Higgs, Y = +1/2)
- The (dT3L = +1/2, dT3R = −1/2) neutral component → H̃⁰ = (H⁰)* (conjugate)

The SM Yukawa couplings from D_F:
- Uptype (ν,u): ψ̄_L H⁰ ψ_R     (using the (−1/2,+1/2) component)
- Downtype (e,d): ψ̄_L H̃⁰ ψ_R   (using the (+1/2,−1/2) component)

## Connection to prior gates

| Gate | G19 connection |
|------|----------------|
| G11 | T3L (J₃) provides dT3L ≠ 0 → SU(2)_L doublet structure |
| G15 | B−L entirely in S⁶ → dBL = 0 → Higgs lives in S³ |
| G16 | K₃ provides dT3R ≠ 0 → SU(2)_R doublet structure |
| G17 | Q conservation: dQ = 0 for all pairs → neutral Higgs only |
| G18 | YUKAWA_PAIRS defines which (i_L, j_R) pairs enter; 4 free couplings remain |

## What this does NOT mean

1. Does NOT fix the Higgs mass or self-coupling — spectral action not computed.
2. Does NOT explain SU(2)_R breaking — the scale at which SU(2)_R → U(1)_T3R is free.
3. Does NOT produce the charged Higgs — dQ = 0 means only the neutral H⁰ component
   acquires a VEV in the SM limit; the charged Higgs H⁺ requires a different vertex.
4. Does NOT verify the kinetic term of φ — only the representation, not the dynamics.
5. Does NOT extend to 3 generations — YUKAWA_PAIRS covers one generation (H_F = ℂ^32).
6. Does NOT identify the gauge group — SU(2)_L × SU(2)_R × (B−L) is inferred from the
   quantum number structure, not derived from a first-principles gauge principle.
7. sm_derivation_claimed = False throughout.

**Status:** PASS_G19_HIGGS_BIDOUBLET
[VERIFIED-sympy, 2026-06-19, 8/8 gates, 19 tests, 929 total]
