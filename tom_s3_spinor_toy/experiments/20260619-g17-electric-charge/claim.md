# G17 — Claim: Electric charge Q = T3L + Y on the 32-dim S³×S⁶ spinor

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:** Q = J₃^{32} + Y_32 = (T3L from G11) + (T3R + B−L/2 from G16) is the electric
charge operator on the 32-dimensional kron(S³_4, S⁶_8) spinor. Every one of the 32 states
takes Q ∈ {0, ±1/3, ±2/3, ±1} and is identified with a Standard Model particle or its
CPT conjugate. The global sum Σ Q_i = 0.

## Q table — all 32 states

| Sector | Row | State | T3L | T3R | B−L | Y | Q |
|--------|-----|-------|-----|-----|-----|---|---|
| L,↑ | 0 | ν_L | +1/2 | 0 | −1 | −1/2 | **0** |
| L,↑ | 1 | d̄_L | +1/2 | 0 | −1/3 | −1/6 | **+1/3** |
| L,↑ | 2 | d̄_L | +1/2 | 0 | −1/3 | −1/6 | **+1/3** |
| L,↑ | 3 | u_L | +1/2 | 0 | +1/3 | +1/6 | **+2/3** |
| L,↑ | 4 | d̄_L | +1/2 | 0 | −1/3 | −1/6 | **+1/3** |
| L,↑ | 5 | u_L | +1/2 | 0 | +1/3 | +1/6 | **+2/3** |
| L,↑ | 6 | u_L | +1/2 | 0 | +1/3 | +1/6 | **+2/3** |
| L,↑ | 7 | ē_L | +1/2 | 0 | +1 | +1/2 | **+1** |
| L,↓ | 8 | e_L | −1/2 | 0 | −1 | −1/2 | **−1** |
| L,↓ | 9 | ū_L | −1/2 | 0 | −1/3 | −1/6 | **−2/3** |
| L,↓ | 10 | ū_L | −1/2 | 0 | −1/3 | −1/6 | **−2/3** |
| L,↓ | 11 | d_L | −1/2 | 0 | +1/3 | +1/6 | **−1/3** |
| L,↓ | 12 | ū_L | −1/2 | 0 | −1/3 | −1/6 | **−2/3** |
| L,↓ | 13 | d_L | −1/2 | 0 | +1/3 | +1/6 | **−1/3** |
| L,↓ | 14 | d_L | −1/2 | 0 | +1/3 | +1/6 | **−1/3** |
| L,↓ | 15 | ν̄_L | −1/2 | 0 | +1 | +1/2 | **0** |
| R,↑ | 16 | ν_R | 0 | +1/2 | −1 | 0 | **0** |
| R,↑ | 17 | d̄_R | 0 | +1/2 | −1/3 | +1/3 | **+1/3** |
| R,↑ | 18 | d̄_R | 0 | +1/2 | −1/3 | +1/3 | **+1/3** |
| R,↑ | 19 | u_R | 0 | +1/2 | +1/3 | +2/3 | **+2/3** |
| R,↑ | 20 | d̄_R | 0 | +1/2 | −1/3 | +1/3 | **+1/3** |
| R,↑ | 21 | u_R | 0 | +1/2 | +1/3 | +2/3 | **+2/3** |
| R,↑ | 22 | u_R | 0 | +1/2 | +1/3 | +2/3 | **+2/3** |
| R,↑ | 23 | ē_R | 0 | +1/2 | +1 | +1 | **+1** |
| R,↓ | 24 | e_R | 0 | −1/2 | −1 | −1 | **−1** |
| R,↓ | 25 | ū_R | 0 | −1/2 | −1/3 | −2/3 | **−2/3** |
| R,↓ | 26 | ū_R | 0 | −1/2 | −1/3 | −2/3 | **−2/3** |
| R,↓ | 27 | d_R | 0 | −1/2 | +1/3 | −1/3 | **−1/3** |
| R,↓ | 28 | ū_R | 0 | −1/2 | −1/3 | −2/3 | **−2/3** |
| R,↓ | 29 | d_R | 0 | −1/2 | +1/3 | −1/3 | **−1/3** |
| R,↓ | 30 | d_R | 0 | −1/2 | +1/3 | −1/3 | **−1/3** |
| R,↓ | 31 | ν̄_R | 0 | −1/2 | +1 | 0 | **0** |

## Q spectrum summary

| Q | States | Count |
|---|--------|-------|
| 0 | ν_L(0), ν̄_L(15), ν_R(16), ν̄_R(31) | 4 |
| −1 | e_L(8), e_R(24) | 2 |
| +1 | ē_L(7), ē_R(23) | 2 |
| +2/3 | u_L(3,5,6), u_R(19,21,22) | 6 |
| −2/3 | ū_L(9,10,12), ū_R(25,26,28) | 6 |
| −1/3 | d_L(11,13,14), d_R(27,29,30) | 6 |
| +1/3 | d̄_L(1,2,4), d̄_R(17,18,20) | 6 |
| **Total** | | **32** |

## Gates summary

All 10/10 gates PASS [VERIFIED-sympy, 2026-06-19]:

| Gate | Content | Result |
|------|---------|--------|
| T1 | Q_32 diagonal | PASS |
| T2 | Q_32 Hermitian | PASS |
| T3 | [Q_32, C_i^{32}] = 0 for all 8 SU(3) generators | PASS |
| T4 | Right-handed fermion Q: ν(0), u(+2/3), e(−1), d(−1/3) | PASS |
| T5 | Right-handed antifermion Q: CPT conjugates | PASS |
| T6 | Left-handed up-type (T3L=+1/2): ν_L(0), u_L(+2/3), ē_L(+1), d̄_L(+1/3) | PASS |
| T7 | Left-handed down-type (T3L=−1/2): e_L(−1), d_L(−1/3), ν̄_L(0), ū_L(−2/3) | PASS |
| T8 | All 32 Q values in {0, ±1/3, ±2/3, ±1} | PASS |
| T9 | Distinct Q values = {0, ±1/3, ±2/3, ±1} (exactly 7) | PASS |
| T10 | Global charge neutrality: Σ Q_i = 0 | PASS |

## Check

`python g17_electric_charge.py` → `PASS_G17_ELECTRIC_CHARGE_GEOMETRIC (10/10)`
`pytest tests/test_g17_electric_charge.py` → 20 passed
`pytest tests/` → 890 passed, 2 skipped

## Connection to prior gates

| Gate | G17 connection |
|------|----------------|
| G11 | J_S3[2] (T3L) directly read as J3_32 |
| G15 | B−L structure on S⁶ → Q values in left and right sectors |
| G16 | Y_32 = K₃^{32} + BmL_32/2 → Q = J3_32 + Y_32 is one line |
| G12 | Anomaly-free 32-component spinor → Q spectrum closes correctly |
| G13 | Chirality on S⁶ → Q=0 for neutrino rows (rows 0, 15, 16, 31 all charged-neutral) |
| G14 | Quark triplet {3,5,6} → u_L(+2/3) and d_L(−1/3) in L sector |

## What this does NOT mean

1. Does NOT fix λ — λ = FREE_COUPLING_PARAMETER throughout.
2. Does NOT derive T3L geometrically — J_S3 is taken from G11 without an independent
   topological justification. The analogous gap as T3R had before G16.
3. Does NOT address the Higgs mechanism, spontaneous symmetry breaking, or fermion masses.
4. Does NOT prove SU(3)×SU(2)×U(1) is the gauge group — only that Q eigenvalues
   of one generation match the SM assignment.
5. Does NOT show the spinor decomposes into SM multiplets (doublets, triplets) under
   gauge transformations — that requires a covariant action, not quantum numbers alone.
6. Does NOT address three generations — the 32-dim spinor accounts for one generation
   plus CPT conjugates.
7. Does NOT claim anomaly cancellation is exact in the full compactification — only that
   the 32-component spectrum is anomaly-free in isolation (G12).
8. sm_derivation_claimed = False throughout.

**Status:** PASS_G17_ELECTRIC_CHARGE_GEOMETRIC
[VERIFIED-sympy, 2026-06-19, 10/10 gates, 20 tests]
