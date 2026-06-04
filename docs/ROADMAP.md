# Research Roadmap — GeoSpectra Lab

**Vision:** Build a falsification-first validation harness that can distinguish robust finite-lattice spectral signals from artifacts, discretization sensitivity, and false positives.

**Current Status:** Gate 4B v0.1.24 SIGNAL_PRESERVED, Negative Controls v0.1.22 COMPLETE, Specificity verdict: DISCRETIZATION_SENSITIVE / GEOMETRY_AGNOSTIC. *(Updated 2026-06-03)*

---

## Phase 1 — Metric-Corrected Gate 4B ✅ COMPLETED

**Goal:** Validate S³×S¹ finite-size scaling with correct eigenvector-based IPR metric.

**Status:** ✅ COMPLETED (2026-05-22)

### Deliverables

- [x] True eigenvector-based IPR implemented (`Σ|ψᵢ|⁴`)
- [x] v0.1.20 eigenvalue-mean metric identified as invalid
- [x] Full Gate 4B rerun with corrected metric
- [x] 216/216 cases executed (0 failures)
- [x] Finite-size scaling grid: s1_size = 16, 32, 64, 128 (N = 112 to 896)
- [x] Three discretization families tested: spectral_circle, ring, wilson_ring
- [x] FSS trend analysis: STRENGTHENING (3.76× → 24.90×)

### Results

**Verdict:** `GATE4B_FSS_PASS_WITH_CAVEATS`

| Metric | Value |
|--------|-------|
| Aggregate contrast (W=20 vs W=0) | 7.15× |
| FSS trend | STRENGTHENING (3.76× → 24.90×) |
| Family consistency | 3/3 PASS |
| r-statistic shift | Δr = -0.163 (toward Poisson) |

**Reports:**
- `reports/S3_S1_GATE4B_FSS_RESULTS_v0.1.21.md`
- `reports/CURRENT_STATUS_v0.1.21_GATE4B_FINAL.md`
- `reports/CLAIMS_ALLOWED_AND_FORBIDDEN_v0.1.21.md`

---

## Phase 2 — Negative Controls / Artifact Zoo ✅ COMPLETED

**Goal:** Test whether harness can reject broken, random, scrambled, or artifact-dominated baselines.

**Status:** ✅ COMPLETED (2026-06-03)

### Final Verdict: DISCRETIZATION_SENSITIVE / GEOMETRY_AGNOSTIC

| Level | Test | Verdict |
|-------|------|---------|
| L1 | Random Hermitian | ✅ REJECTS (slope -1.14, WEAKENING) |
| L2 | Scrambled geometry | ✅ REJECTS (slope -0.90, WEAKENING) |
| L3 | FFT vs lattice (spectral_circle) | ✅ DISTINGUISHES (spectral -0.48 vs ring +0.01) |
| L4 | Lattice families (ring/wilson_ring) | ✅ ACCEPTS (both STABLE) |
| L5 | Wilson details | ❌ DOES NOT DISTINGUISH (scrambled -0.07, STABLE) |

**C1 (harness discrimination): CONFIRMED** — controls A/B/C correctly rejected
**C2 (spectral_circle diagnosis): GEOMETRY-SPECIFIC** — scrambled 5× lower than S³×S¹ at s1=128

**Total cases executed:** 132 local (v0.1.22) + 54 server (v0.1.22 batches 1-6) + 36 extended

### Controls Summary

| Control | Cases | Verdict | IPR(W=20) max | vs ring ref |
|---------|-------|---------|--------------|-------------|
| A: random_hermitian | 24 local | ✅ REJECTED | 0.0024 | 0.7% |
| B: scrambled_geometry | 24 local + 18 server | ✅ REJECTED | 0.052 | 16% |
| C: broken_wilson_scrambled | 24 local + 18 server | ✅ REJECTED | 0.007 | 2% |
| D: spectral_circle_scrambled | 24+6 local | GEOMETRY-SPECIFIC | 0.014 at s1=128 | — |

**Reports:**
- `reports/S3_S1_NEGATIVE_CONTROLS_RESULTS_v0.1.22.md` ← финальный
- `reports/SKEPTIC_AUDIT_GATE4B_v0.1.22.md`
- `reports/ESTIMAND_v0.1.22.md`
- `reports/CLAIM_v0.1.22.md`
- `reports/GATE4B_SPECIFICITY_VERDICT_v0.1.24.md`
- `reports/UNIFIED_RESULT_RECONCILIATION_AUDIT_v0.1.24.md`

---

## Phase 3 — Clean Compact-Product Spectral Checks 📋 READY TO START

**Goal:** Verify that clean W=0 finite-lattice geometry has meaningful compact-product spectral structure.

**Blocker resolved:** Phase 2 complete. Phase 3 is now unblocked.

**Motivation:** Negative controls confirm DISCRETIZATION_SENSITIVE verdict. Phase 3 characterises WHY lattice product structure produces the signal — analytic comparison.

### Planned Diagnostics

1. **Harmonic sanity checks**
   - Compare W=0 eigenvalue distribution to analytic S³ × S¹ spectrum
   - Check degeneracy structure
   - Verify separation of S³ and S¹ modes

2. **Product-separability monitor**
   - Measure degree of S³/S¹ coupling in clean limit
   - Kronecker-product structure test
   - Eigenstate factorizability

3. **S³ vs S¹ directional diagnostics**
   - S³ sector localization (if applicable)
   - S¹ twist response in clean limit
   - Wilson term structure preservation

4. **Clean-limit spectral structure**
   - Spectral flow vs boundary twist
   - Kernel structure (zero modes)
   - Comparison to analytic product formula

**Estimated effort:** 2-3 weeks (implementation + validation)

**Blocker:** Requires negative controls completion first (Phase 2)

---

## Phase 4 — Extended Robustness 📋 PLANNED

**Goal:** Test robustness beyond Gate 4B baseline.

### Planned Extensions

#### 4A. W-Sweep (Disorder Strength)
- Current: W = 0, 20 (exploratory)
- Plan: W = 0, 4, 8, 12, 16, 20, 24 (full sweep)
- Purpose: Find optimal contrast, test W-dependence

#### 4B. Finite-Size Scaling (Larger Lattices)
- Current: s1_size = 16, 32, 64, 128 (N ≤ 896)
- Plan: s1_size = 256, 512 (N ≤ 3584)
- Purpose: Test FSS continuation, check for collapse
- **Constraint:** Requires remote execution (local thermal limit)

#### 4C. Null Geometry Control (T⁴ Baseline)
- Current: Only S³×S¹ tested
- Plan: T⁴ (4-torus, no curvature)
- Purpose: Test if signal requires S³ curvature
- Expected: T⁴ should show weaker or different contrast pattern

#### 4D. Cross-Geometry Transfer
- Test: S²×S² (positive curvature, different topology)
- Test: Hyperbolic product (negative curvature)
- Purpose: Generalization test
- **Warning:** Each geometry = independent validation, NO automatic transfer

#### 4E. Multi-Metric Consensus
- Current: IPR (primary), r-stat (secondary)
- Add: Participation entropy, localization length, multifractal analysis
- Purpose: Reduce single-metric artifact risk

**Estimated effort:** 6-8 weeks total (4A-4E)

---

## Phase 5 — Methodology Paper 📋 FUTURE

**Goal:** Document falsification-first validation harness as a reusable methodology.

### Potential Framing

> **"Falsification-First Validation Harness for Finite-Lattice Spectral Toy Geometries: A Metric-Corrected S³×S¹ Case Study"**

### Paper Structure (Draft)

1. **Introduction**
   - Problem: Finite-lattice spectral artifacts
   - Solution: Falsification-first harness
   - Case study: S³×S¹ Anderson disorder

2. **Methodology**
   - Controls ladder (negative, positive, intermediate)
   - Progressive profiles (quick → medium → full)
   - Pre-registration protocol
   - Negative controls / artifact zoo
   - Independent audit

3. **S³×S¹ Case Study**
   - Gate 4B v0.1.21 results
   - Metric correction transparency (v0.1.20 → v0.1.21)
   - Negative controls outcomes
   - FSS analysis

4. **Discussion**
   - What methodology validates (robustness checks)
   - What it does NOT validate (physics, continuum, generalization)
   - Reusability for other geometries
   - Limitations and future work

5. **Appendices**
   - Code availability (Zenodo DOI)
   - Reproducibility checklist
   - Null results and failed hypotheses

**Target venue:**
- arXiv (computational physics / numerical methods)
- *Computer Physics Communications*
- *SoftwareX*

**Status:** NOT started (Phase 2-4 must complete first)

---

## Alternative Paths

### Path A: Gate 5 Before Negative Controls

**Tradeoff:**
- **Gate 5** = more S³×S¹ data (strengthen positive claim)
- **v0.1.22 Negative Controls** = specificity check (strengthen confidence in existing claim)

**Recommendation:** Complete negative controls first (Phase 2) before scaling up to Gate 5.

**Rationale:** If negative controls reveal harness lacks specificity, Gate 5 wastes compute on non-specific signal.

---

### Path B: Cross-Geometry Before Extended S³×S¹

**Tradeoff:**
- Test T⁴ / S²×S² before finishing S³×S¹
- Risk: Premature generalization claim

**Recommendation:** Finish S³×S¹ validation (Phases 2-4) before cross-geometry.

**Rationale:** Deep validation of one geometry > shallow validation of many.

---

## Success Criteria by Phase

| Phase | Success = | Failure = | Next Step |
|-------|-----------|-----------|-----------|
| 1 (Gate 4B) | ✅ FSS STRENGTHENING, family consistency | FSS COLLAPSE or metric artifact | ✅ DONE |
| 2 (Neg Controls) | Controls fail as expected | Any control reproduces Gate 4B pattern | Report harness lacks specificity |
| 3 (Clean Checks) | W=0 matches analytic product spectrum | W=0 anomalous or non-separable | Investigate clean-limit artifact |
| 4 (Extended) | Robustness survives W-sweep, FSS, T⁴ | Signal collapses or T⁴ matches S³×S¹ | Revise claim scope |
| 5 (Paper) | Methodology paper accepted | Methodology flaws identified in review | Fix methodology, revalidate |

---

## Timeline Estimate

| Phase | Duration | Dependencies |
|-------|----------|--------------|
| 1 — Gate 4B | ✅ 3 weeks | DONE |
| 2 — Negative Controls | 1-2 weeks | Remote execution setup |
| 3 — Clean Checks | 2-3 weeks | Phase 2 completion |
| 4A — W-Sweep | 1 week | Phase 2 completion |
| 4B — Extended FSS | 2 weeks | Remote execution (thermal constraint) |
| 4C — T⁴ Baseline | 1-2 weeks | Phase 2 completion |
| 4D — Cross-Geometry | 3-4 weeks | Phase 4C completion |
| 4E — Multi-Metric | 2 weeks | Phase 2 completion |
| 5 — Methodology Paper | 4-6 weeks | Phases 2-4 completion |

**Total:** ~20-30 weeks from current state to methodology paper.

**Bottleneck:** Remote execution availability (thermal constraint on local hardware).

---

## Long-Term Vision (Beyond Current Roadmap)

### Geometry Expansion (Conditional)

**Only if Phases 1-4 succeed AND show geometry-specific signal:**

- S⁶ (6-sphere)
- S³×S⁶ (product of 3-sphere and 6-sphere)
- Higher-dimensional products

**WARNING:** These are NOT next steps. They require:
1. S³×S¹ fully validated (Phases 1-4)
2. Cross-geometry transfer protocol established (Phase 4D)
3. Each geometry = independent multi-month validation

### Continuum Extrapolation (Far Future)

**Requirements:**
- Rigorous N → ∞ finite-size scaling study
- Analytical continuum comparison
- Error bounds and convergence proof

**Status:** NOT feasible with current resources (N ≤ 896 max on local hardware)

---

## What This Roadmap Does NOT Include

❌ Physical compactification validation  
❌ Standard Model gauge group derivation  
❌ Chiral fermion construction (beyond toy controls)  
❌ Witten/Lichnerowicz bypass  
❌ Real cosmology or extra-dimensional stabilization  

**This roadmap is for computational validation harness development, not physics theory.**

---

## How to Contribute / Collaborate

**Current status:** Solo project (Sergey Boyko)

**Open to:**
- Independent verification / reproduction attempts
- Code review and methodology critique
- Computational resources (cloud credits, cluster access)

**Not seeking:**
- Co-authorship without substantial contribution
- Endorsement of premature claims
- Overgeneralization to physics conclusions

**Contact:** sergeikuch80@gmail.com

---

**Last updated:** 2026-05-24  
**Next review:** After Phase 2 (negative controls) completion  
**Status:** ACTIVE — Phase 2 in progress, Phase 3-5 planned
