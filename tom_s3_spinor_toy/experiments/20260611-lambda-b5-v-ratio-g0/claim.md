# LAMBDA-B5-V-RATIO-G0 — λ-free ratio gate

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:**
Within a fixed S³ V-operator sector (j_L_in, j_L_out, j_R fixed), all matrix elements
share the SAME reduced matrix element vred and the SAME geometric factor. Therefore:

    M_a = λ · vred · geom · CG_a
    M_b = λ · vred · geom · CG_b

and the ratio R = M_a/M_b = CG_a/CG_b depends only on Clebsch-Gordan coefficients —
λ cancels exactly.

Specifically: for the sector (j_L_in=1/2, j_L_out=3/2, J=1), the column m_tgt=1/2 has
two nonzero source rows whose CG values differ:
  CG(m_src=+1/2, q=0 → m_tgt=+1/2) = √6/3  [larger]
  CG(m_src=-1/2, q=+1 → m_tgt=+1/2) = √3/3  [smaller]
Their ratio R = CG_larger/CG_smaller = √2 exactly.

This is a structural prediction from S³ representation theory: observable in principle
without measuring λ or fixing the normalization of V.

**Kill target (Strong Inference):**
- FAIL-A: sector (j_L=1→j_L=1) has <2 nonzero CG elements → trivial sector, no testable ratio
- FAIL-B: sector (j_L=1/2→j_L=3/2) has <2 nonzero CG for fixed m_tgt → ratio undefined
- FAIL-C: ratio in sector B is ±1 (trivial, no structural information beyond phase)
- FAIL-D: ratio is normalization-dependent (vred or geom do NOT cancel)

Any FAIL → V-RATIO program requires either extended basis (k_max≥3) or different
operator structure.

**Checks planned (7 checks):**
- T1: Sector A (j=1→j=1, J=1): ≥2 nonzero CG elements exist
- T2: Sector A: ratio R = CG_a/CG_b — verify numerically exact (±1 expected)
- T3: Sector A: λ derivative dR/dλ = 0 symbolically (λ-free)
- T4: Sector B (j=1/2→j=3/2, J=1), m_tgt=1/2: ≥2 nonzero CG elements exist
- T5: Sector B: R = CG(1/2,+1/2;1,0|3/2,1/2) / CG(1/2,-1/2;1,1|3/2,1/2) = √6/√3 = √2 exactly
- T6: Sector B ratio is non-trivial (R ≠ ±1)
- T7: Sector B: λ derivative dR/dλ = 0 symbolically (λ-free)

**Verdict:** PASS_LAMBDA_FREE_RATIO_CONFIRMED [VERIFIED-sympy 7/7, 2026-06-11]

**Key numbers:**
- Sector A (j_L=1→1, j_R=1/2): 6 nonzero CG elements, ratio = ±1 (trivial, phase only)
- Sector B (j_L=1/2→3/2, j_R=1): 6 nonzero CG elements, 2 per fixed m_tgt=1/2 column
- CG(m_src=+1/2 → m_tgt=+1/2) = √6/3 = √(2/3)
- CG(m_src=-1/2 → m_tgt=+1/2) = √3/3 = √(1/3)
- R = √(2/3)/√(1/3) = √2 — exact, independent of λ and vred

**Status:** CLOSED PASS_LAMBDA_FREE_RATIO_CONFIRMED

**Fence (unchanged):**
- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

**Caveat / What this does NOT mean:**
- Does NOT fix λ (ratios are λ-free, not λ-fixing)
- Does NOT require the full P13B matrix build — uses CG algebra directly
- Does NOT promote V to physical operator
- Does NOT claim j_L=3/2 states are in the k_max=1 basis (they're in k_max=2)
- Does NOT establish which spin structure to select (Tom Q1 still open)

**Separation of concerns:**
The ratio √2 is a PROPERTY OF S³ GEOMETRY (CG coefficients of SU(2)×SU(2)
representation theory). It holds regardless of λ, regardless of normalization of V,
and regardless of whether V is physical. It is a structural fingerprint that could
be tested once V-matrix elements are observationally accessible (k_max=2 spectrum).
