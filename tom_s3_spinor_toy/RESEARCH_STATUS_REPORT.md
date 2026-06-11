# N-7 GeoSpectra Lab — Research Status Report
**Date:** 2026-06-11  
**Branch:** main @ 93e681e  
**Test suite:** 415 passed, 2 skipped  
**Author:** Sergey Boyko

---

## Overview

Three independent research threads (контуры) completed. All gated via Falsification Ladder (FL) Standard protocol: claim.md → evidence script → results JSON → decision.

External dependency: **Tom Lawrence** (4 questions sent 2026-06-09, no reply yet).  
Hard fences active: λ = FREE_COUPLING_PARAMETER, GEOMETRY_AGNOSTIC = True, safe_for_runtime = False.

---

## Контур 1 — AV-2: Angular/Bilinear Operator Analysis

**Status: COMPLETE ✅ (5/5 gates PASS)**

### Gates

| Gate | Verdict | Key number | Commit |
|------|---------|------------|--------|
| G0 | PASS | Source trace: C-H eqs 3.27-3.38 VERIFIED_FROM_PDF | — |
| G1 | PASS | 24/24 tests; eq 3.28 ≤2.3e-15; FD ≤5e-7 | — |
| G2 | PASS | g_l0≈−0.096 (≈0), mixed_l0=0.928 (≈cosα); 45 tests | — |
| E1 | STRONG_PASS | 1 term: φ₀₀·g₀₀ = cosα·sinα = sin(2α)/2 EXACT; 26 tests | — |
| E2 | PASS | CG singlet = √2/2, C²=0.5>0; 21 tests | — |

### Consolidated Result
**item40 = RADIAL + ANGULAR_BILINEAR_SUPPORTED**

The angular operator is consistent with a bilinear Clebsch-Gordan structure.  
The sparse E1 reconstruction shows the dominant term is analytically exact (zero residual).

### Key Insights
- **E1 STRONG_PASS:** The exact 1-term reconstruction cosα·sinα = sin(2α)/2 is not a numerical accident — it is an analytic identity from S³ geometry. This is the strongest positive result in this thread.
- **E2:** The CG singlet √2/2 is the same as the V-RATIO-G0 ratio (different computation path, same CG algebra — consistent).
- **G2 boundary exponent:** g_l0 → 0 at l=0 (boundary vanishes), mixed_l0 ≈ 1 (dominant cos-component) — boundary geometry selects a specific angular family.
- **What it does NOT mean:** Does not prove S³ is the physical compactification space; does not fix λ; does not select spin structure.

---

## Контур 2 — BG-H1: S³×S¹ KK Bridge Hypothesis

**Status: COMPLETE ✅ (4/4 gates PASS)**

### Pre-registered claim
Kaluza-Klein spectrum on S³×S¹:

    λ² = (n + 3/2)² + (m/R)²
    δ₁(R) = √(9/4 + (m₁/R)²) − 3/2

Both spin structures forked: m ∈ ℤ (periodic) vs m ∈ ℤ+1/2 (anti-periodic). No selection made.

### Gates

| Gate | Verdict | Key number | Commit |
|------|---------|------------|--------|
| G0 | PASS v1.1 | Product Dirac additivity from C-H eqs (2.1),(2.4),(2.10),(3.46)-(3.48) | 9f022a0 |
| G1 | PASS | D₄²=−(k²+p²)·I₄, max_rel_error=0.0 (machine precision); 58 tests | 56d8c38 |
| E1 | PASS | k₀_disc(N=4000)=1.4999999561; max_rel_err=2.93e-08; O(h²) convergence; 72 tests | 3a9237d |
| E2 | PASS | W=0.5, 30 seeds; max_frag_ratio=0.998 (<10); max_mean_err=2.54e-04 (<0.05); 67 tests | 5629942 |

### Consolidated Result
**S3XS1_KK_BRIDGE_SUPPORTED_ROBUST**

The KK spectral formula λ²=(n+3/2)²+(m/R)² is consistent across analytic derivation, discrete S³×S¹ proxy, and disorder stress-test.

### Key Insights
- **G0 adversarial re-audit** (critical): First pass had phantom file reference and overclaims. After adversarial re-audit, the cross-term cancellation mechanism was pinned: it requires **both** {Γʲ,Γ⁴}=0 AND [∇ⱼ,∂_y]=0 jointly — neither alone suffices (|X|≈13.9 and 22.1 poодиночке vs 0 jointly).
- **E1:** Discrete k₀=1.4999999561 vs analytic 3/2 — difference 4.4e-7 at N=4000 nodes. Finite-size correction, not error. Confirmed O(h²) convergence.
- **E2 disorder:** frag_ratio ≤ 1 analytically (δ=f(k₀) is deterministic, not stochastic) — the disorder robustness is a structural property, not a tuning accident.
- **Spin structure fork**: m ∈ ℤ gives bosonic KK tower (δ₀=0 in spectrum — ground state exists!); m ∈ ℤ+1/2 gives fermionic tower. Selection awaits Tom Q1.
- **What it does NOT mean:** Does not prove S³×S¹ is the physical product. Does not select spin structure. Does not establish the full Dirac operator beyond the product approximation.

---

## Контур 3 — Lambda-B5: V-Operator and λ Coupling Analysis

**Status: COMPLETE for current scope ✅ (8/8 gates PASS + 1 STRUCTURAL_SPLIT)**

This is the deepest thread. It started as an attempt to fix λ from S³ geometry and evolved into a rigorous proof that λ is non-identifiable from S³ alone.

### Gates

| Gate | Verdict | Key result | Commit |
|------|---------|-----------|--------|
| G0 | STRUCTURAL_SPLIT_REQUIRED | Invariant 1-forms ξ̃,ξ̃′ ∉ span(E_i, E′_i); E(L=0)≡0 by algebra; λ_geom conditionally canonical | ae05133 |
| G1 | PASS | D_phys = −iγ^a∇_a; spectrum ±(n+3/2); Lichnerowicz D²=9/4 ✓; λ₀=3/2 matches k₀_disc | 5469658 |
| G2 | PASS | cot(2α)=Hopf-frame spin-connection artifact; dσ₃/(σ₁∧σ₂)=2 (integer, frame-invariant) | fc30a28 |
| G3 | PASS | F_{ab}=(1/4)[γ_a,γ_b]=(i/2)ε_{abc}γ^c; su(2) algebra; Casimir=−(3/4)I j=1/2 | 5469658 |
| G4 | PASS | rank(J_phys)=2 (λ non-identifiable); rank(J_full)=3 (identifiable IFF V promoted); det(J_full)≠0 | dce2156 |
| P14B | PASS | S³ Hopf measure sin(α)cos(α)dα: volume=2π², bilinear norm=π²/3; phase-invariant | 282eb1c |
| V-RATIO-G0 | PASS | R=√2 EXACT in sector (j_L=1/2→3/2, j_R=1); λ-free by Wigner-Eckart | 65fc64d |
| S6-BRANCH-G0 | PASS | SU(4)→SU(3)×U(1): all charges ∈ ℚ; Pati-Salam necessary condition satisfied | bbe7bb8 |

### Structural Split (G0) — Critical Finding
The V-operator decomposes as:

    V = λ_geom · V_ω + Σ cᵢ · V_modes

where V_ω is the canonical invariant-form component and V_modes are the E_i/E′_i tower contributions. These two components live in **different sectors** of the function space — no tuning of cᵢ can reproduce V_ω. This rules out the Dereli-style single-coupling ansatz.

### G2 — Candidate Answer to Tom Q2
cot(2α) vanishes in the SO(4) / quaternionic frame (it is a Hopf-frame artifact of the spin connection, not a geometric invariant). This is a candidate answer to Tom Q2 ("cot(2α) expected to vanish with correct basis?").

### G4 — Formal Theorem: λ is Non-Identifiable
Fisher information matrix analysis:
- Observables {o₁, o₂} = {spectrum, bilinear norm} → rank(J_phys) = 2 (λ does NOT appear)
- With V-matrix element added: rank(J_full) = 3 (λ IS identifiable)
- Conclusion: **λ = FREE_COUPLING_PARAMETER is a mathematical theorem**, not just a discipline fence. λ can only be measured if V is promoted to physical status.

### V-RATIO-G0 — First Positive Prediction
Within any fixed sector (j_L_in, j_L_out, j_R), the Wigner-Eckart theorem guarantees:

    R = M_a/M_b = CG_a/CG_b   (λ, vred, geom all cancel)

Sector B (j_L=1/2→3/2, j_R=1): **R = √2 EXACT**  
This is the first structural prediction testable without measuring λ. Observable once k_max=2 states are in the spectrum.

### S6-BRANCH-G0 — Algebraic Kill Test for S³×S⁶
SU(4) isometry of S⁶, branched SU(4)→SU(3)×U(1) via T=diag(1/3,1/3,1/3,−1):
- All charges rational: {−4/3,−1,−2/3,−1/3,0,+1/3,+2/3,+1,+4/3} ⊂ ℚ
- Pati-Salam: T = (B-L)/4; quarks +1/3, lepton −1
- Kill branch "irrational charges" is CLOSED — S³×S⁶ not ruled out at algebraic level

### Key Insights (Lambda-B5)
- **λ non-identifiability is structural**, not a computational artifact. The Fisher rank theorem is the cleanest proof.
- **G2+G3 together**: the Hopf frame has a spin connection cot(2α) that is a frame artifact; the curvature is SU(2) (j=1/2, Casimir −3/4). These two facts together pin the spinor geometry of S³ without any free parameters.
- **V-RATIO-G0 redirects the program**: instead of "we can't measure λ", we now have "we CAN test V-structure ratios as λ-free predictions". This is the first positive observable.
- **S6-BRANCH-G0**: the Pati-Salam embedding of SU(4) into SM is the simplest algebraic test for S³×S⁶ viability. PASS means we proceed; FAIL would have killed the whole compactification direction.

---

## Cross-Cutting: ACH Falsification Matrix

**File:** `TOM_RECONSTRUCTION_ACH_MATRIX.md`  
6 competing hypotheses evaluated:

| Case | Hypothesis | Status |
|------|-----------|--------|
| 1 | λ fixed by S³ measure alone | KILLED (G4 Fisher rank) |
| 2 | Dereli single-coupling suffices | KILLED (G0 structural split) |
| 3 | cot(2α) is a physical term | KILLED (G2 frame artifact) |
| 4 | V-matrix ratios are λ-dependent | KILLED (V-RATIO-G0 Wigner-Eckart) |
| 5 | S³×S⁶ charges incompatible with SM | KILLED (S6-BRANCH-G0 rationality) |
| 6 | λ identifiable with V promoted | OPEN (G4: rank(J_full)=3 ≠ 0, but V not physical yet) |

---

## Open: Tom Lawrence Questions (sent 2026-06-09)

Status: **hang fire / no reply**

| Q# | Question | Relevance |
|----|---------|-----------|
| Q1 | Is replacement basis U(α,θ,θ̃) the correct spinor frame for S³? | Spin structure selection: m∈ℤ vs m∈ℤ+1/2 |
| Q2 | cot(2α) — expected to vanish in correct SO(4) basis? | Candidate answer: YES (G2 frame artifact) |
| Q3 | Is λ free at S³ stage, or fixed by S³×S⁶/gauge? | G4 says free; Tom may know additional constraints |
| Q4 | α convention and S³ measure sin(α)cos(α)dα correct? | P14B says autonomous PASS — may not need answer |

**Rule:** Do NOT write to Tom until he replies to the 4-question message.

---

## Current State Summary

| Thread | Status | Blocked by |
|--------|--------|-----------|
| AV-2 | COMPLETE | Nothing — self-contained |
| BG-H1 | COMPLETE | Spin structure fork awaits Tom Q1 |
| Lambda-B5 | Phase 1 complete | V-promotion decision awaits Tom Q3 |
| ACH Matrix | 5/6 cases killed | Case 6 (V-promotion) awaits physics |

**Test suite:** 415 passed (415 on main, 191 additional on preserve branch)  
**Next actions when Tom replies:**
1. Tom Q1 → select spin structure → close BG-H1 fork
2. Tom Q2 → confirm G2 candidate answer → update ACH matrix
3. Tom Q3 → decide V-promotion path → open Lambda-B5 Phase 2
4. Tom Q4 → P14B is autonomous but confirmation is welcome

**Without Tom reply**, autonomous next directions:
- Direction B: Hermitianization of full k_max=2 V-matrix — does R=√2 survive?
- Direction C: More V-ratio sectors at k_max=2 (k=2 positive: j_L=3/2, j_R=1)
- Direction E: S³×S⁶ dimensional analysis — does the KK mass scale match?

---

## Repository Structure (key files)

```
tom_s3_spinor_toy/
├── tests/                          # 415 tests on main
├── experiments/
│   ├── 20260611-lambda-b5-v-ratio-g0/   # V-RATIO-G0 (FL Standard)
│   └── 20260611-lambda-b5-s6-branch-g0/ # S6-BRANCH-G0 (FL Standard)
├── TOM_RECONSTRUCTION_ACH_MATRIX.md     # ACH falsification matrix
├── PROJECT_CURRENT_STATE.md            # authoritative state sync
├── reports/
│   ├── P5_P14_REAUDIT_REPORT.md
│   ├── g1_product_dirac_cross_check_report.md
│   ├── e1_product_proxy_report.md
│   └── e2_disorder_report.md
├── null_results/
│   └── 20260610-ht1-sparse-bilinear.md  # AV-1c′ KILLED
└── preserve/tom-s3-p5-p14-scaffold      # P5-P14 / V-operator (191 tests, never merge to main)
```

---

*Generated 2026-06-11. Last commit: 93e681e. For resume: `git checkout main && git pull origin main`.*
