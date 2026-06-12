# LAMBDA-B5-S6-BRANCH-G0 — S⁶ branching compatibility discriminator

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:**
The KK isometry group SU(4) acting on S⁶, when branched as SU(4) → SU(3) × U(1),
produces U(1) charges in the fundamental representations that are COMPATIBLE with
Pati-Salam identification of quarks (+1/3) and leptons (-1):

    4  → 3_{+1/3}  ⊕  1_{-1}     [quarks + lepton]
    4̄  → 3̄_{-1/3}  ⊕  1_{+1}     [anti-quarks + anti-lepton]
    6  → 3_{+2/3}  ⊕  3̄_{-2/3}   [colour sextet, conjugate pair]
    15 → 8_0 ⊕ 3_{+4/3} ⊕ 3̄_{-4/3} ⊕ 1_0   [adjoint]

The U(1) generator is T = diag(1/3, 1/3, 1/3, -1) (traceless, exact fractions).

**Kill target (Strong Inference):**
- FAIL: charges are irrational or incompatible with SM assignments → S³×S⁶
  needs additional structure beyond SU(4) isometry to produce SM hypercharges
- PASS: fractional charges {+1/3, -1/3, +2/3, -2/3, ±1} all appear → necessary
  compatibility confirmed (NOT sufficient to claim "SM derived from S³×S⁶")

**Checks planned (7 checks):**
- T1: T = diag(1/3,1/3,1/3,-1) is traceless (SU(4) consistency)
- T2: Eigenvalues of T on the 4-rep = {1/3 (×3), -1 (×1)}
- T3: Tracelessness check: 3×(1/3) + (-1) = 0
- T4: 4̄ charges = negated 4 charges = {-1/3 (×3), +1 (×1)}
- T5: 6 = [4⊗4]_antisym charges = {2/3 (×3), -2/3 (×3)} — conjugate pair ✓
- T6: Adjoint 15 = [4⊗4̄]_traceless charges include 0, ±4/3 — no irrational charges
- T7: The set of all U(1) charges is a subset of ℚ (all rational) — no irrational charges

**Verdict:** PASS_SU4_BRANCHING_SM_COMPATIBLE [VERIFIED-sympy 7/7, 2026-06-11]

All charges rational: {-4/3, -1, -2/3, -1/3, 0, +1/3, +2/3, +1, +4/3} ⊂ ℚ
Pati-Salam identification: T = (B-L)/4; quarks +1/3, lepton -1

**Status:** CLOSED PASS_SU4_BRANCHING_SM_COMPATIBLE

**Fence (unchanged):**
- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

**Caveat / What this does NOT mean:**
- Does NOT claim S³×S⁶ reproduces the Standard Model
- Does NOT prove SU(4) isometry is the correct gauge group
- Does NOT fix the spin structure or determine which representations are physical
- Does NOT establish Tom Q1 (replacement basis) answer
- Does NOT constrain λ in any way
- NECESSARY but NOT SUFFICIENT: compatible ≠ derived

**Physical context:**
Pati-Salam unification: SU(4)_PS → SU(3)_c × U(1)_{B-L} where
the 4th colour is lepton number. The T generator here is (B-L)/4 in PS notation.
The charges {1/3, -1} match known Pati-Salam assignments for one SM generation.
This is a cheap algebraic discriminator: if charges were incompatible,
S³×S⁶ would be ruled out as a candidate for producing SM-like matter content.
