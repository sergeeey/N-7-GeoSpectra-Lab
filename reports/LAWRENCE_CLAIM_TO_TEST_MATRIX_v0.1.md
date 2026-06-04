# Lawrence Claim-to-Test Matrix — v0.1

**Date:** 2026-05-31  
**Status:** DRAFT — mapping conceptual claims to falsifiable computational signatures  
**Purpose:** Bridge between Tom Lawrence / Kaluza-Klein compact geometry ideas and GeoSpectra computational tests

---

## 1. Purpose

**What this document IS:**
- A mapping from conceptual claims (compact geometry, gauge-like fields, zero modes) to **possible** falsifiable computational signatures
- Pre-registration of potential observables **before** analyzing existing data or designing new experiments
- Framework for independent falsification tests (GeoSpectra harness can test computational signatures, NOT physical theories)

**What this document IS NOT:**
- Validation of Tom Lawrence's theory
- Proof of compactification
- Derivation of gauge groups or Standard Model
- Physical claim about Kaluza-Klein compactification

**Critical distinction:**
- **Tom's framework:** S³×S¹ / S³×S² as physical compactification candidate (geometric unification, gauge fields from geometry)
- **GeoSpectra harness:** Finite-lattice spectral toy geometry (computational falsification only, NO physical claims)

**Independence:**
GeoSpectra is an **independent computational validation harness**. If a computational signature is found, it does NOT prove Tom's theory. If NOT found, it does NOT disprove Tom's theory (finite-lattice limitations apply).

---

## 2. Safety Boundary

### ❌ Forbidden Claims (Never state, even if computational signature found)

1. ❌ "Tom Lawrence theory validated"
2. ❌ "Compactification proven"
3. ❌ "Gauge group derived from geometry"
4. ❌ "Standard Model structure reproduced"
5. ❌ "Chirality explained"
6. ❌ "Physical massless bosons detected"
7. ❌ "S³×S¹ validated as physical compactification"
8. ❌ "Kaluza-Klein mechanism confirmed"
9. ❌ "Extra dimensions detected"
10. ❌ "Unified field theory validated"

### ✅ Allowed Claims (If computational signature found)

1. ✅ "Finite-lattice spectral signature consistent with [concept]"
2. ✅ "Computational toy diagnostic shows [pattern]"
3. ✅ "Falsification condition NOT met (pattern survives negative controls)"
4. ✅ "Future candidate test identified for S³×S² geometry"
5. ✅ "Observable defined for potential falsification"
6. ✅ "Pre-registered metric shows [value] (interpretation pending)"
7. ✅ "Geometric structure [X] computationally distinguishable from [Y]"

---

## 3. Claim-to-Test Table

| Concept / Claim | Mathematical Object | Possible GeoSpectra Observable | Data Needed | Existing Data? | Minimal Test | Failure Condition | Risk / Artifact |
|-----------------|---------------------|--------------------------------|-------------|----------------|--------------|-------------------|-----------------|
| **1. Product compact geometry** | M = S³ × S¹ | Kronecker product structure in Dirac operator spectrum | Eigenvalues, eigenvectors | ❓ Unknown | Tensor product decomposition: verify λ(S³×S¹) ≈ λ(S³) + λ(S¹) | Eigenvalues NOT separable, no Kronecker structure | May be lattice artifact (discretization breaks product structure) |
| **2. S³ spatial slice** | S³ Hopf fibration, SU(2) structure | Degeneracy groups in S³ Dirac operator eigenvalues | Eigenvalues, multiplicity counts | ❓ Unknown | Count multiplicity of each eigenvalue → compare to SU(2) irrep dimensions (2j+1) | Multiplicities NOT matching SU(2) irreps | Finite-lattice breaks continuous symmetry → degeneracies approximate only |
| **3. S¹ Klein/Kaluza extra circle** | U(1) fiber, Wilson loop | Zero modes at k=0 (momentum along S¹), sensitivity to S¹ discretization size | Eigenvalues near zero, IPR(k=0 modes) | ✅ Partial (IPR aggregate, eigenvalues per case?) | Plot eigenvalue density near E=0 vs s1_size → look for k=0 tower | No zero-mode tower, or tower insensitive to s1_size | Disorder (W=20) may suppress zero modes → test W=0 first |
| **4. S² Pauli non-Abelian KK direction** | S² coset space SU(2)/U(1), Pauli matrices | Spin-weighted harmonics multiplets in S³×S² spectrum | Eigenvalues, eigenvector angular structure | ❌ No (S³×S² not yet implemented) | Port to S³×S² geometry → count (2ℓ+1)-fold degeneracies for ℓ quantum number | No spin-ℓ multiplets, or degeneracies broken | S³×S² discretization may break SU(2) structure worse than S³ alone |
| **5. S³×S² future candidate** | Product of two 3-spheres (one SU(2) spatial, one Pauli KK) | Cross-geometry comparison: S³×S¹ vs S³×S² spectral differences | Full S³×S² rerun (216 cases, ~6h compute) | ❌ No | Minimal: S³×S² W=0, s1_size=16,32,64, compare IPR contrast, FSS trend vs S³×S¹ baseline | S³×S² identical to S³×S¹ → no geometric specificity | Requires new geometry implementation (~2 weeks dev) |
| **6. S³×S⁶ / harmonics / spinor multiplets** | High-dimensional product, Clifford algebra, spinor bundles | Spinor multiplet structure (Dirac 4-component → 8-component in 7D) | Eigenvector spinor components, spin structure | ❌ No (not implemented, requires 7D Clifford algebra) | Future theoretical extension (NOT in GeoSpectra v0.1 scope) | N/A (out of scope) | Computational cost prohibitive (dim ≥ 2^(7/2) = 11.3 states per site) |
| **7. Gauge-like fields from geometry** | Connection on fiber bundle, Christoffel symbols → "gauge field" | IPR sensitivity to S¹ discretization family (spectral_circle vs ring vs wilson_ring) | IPR by family, W=0 baseline | ✅ Yes (Gate 4B family contrasts) | Compare W=0 IPR across families → if wilson_ring ≠ spectral_circle at W=0, geometry matters | All families identical at W=0 → no geometric sensitivity, only disorder-driven | Gate 4B already showed family differences (~2-4× at W=20), unclear if W=0 |
| **8. Zero modes / massless modes** | ker(Dirac operator), λ ≈ 0 eigenstates | Count of near-zero eigenvalues (|λ| < ε), IPR of those states | Eigenvalues, eigenvectors | ❓ Unknown (eigenvalues may not be saved per-state) | Histogram: number of eigenvalues in [−ε, ε] vs W, s1_size → expect ≥1 for W=0 | No zero modes even at W=0 → lattice kills them, OR disorder suppresses | Lattice Dirac may have fermion doubling (spurious zero modes) |
| **9. Eigenvalue multiplicities** | SU(2) irreps → (2j+1)-fold degeneracies | Histogram of multiplicity counts → peaks at 1, 3, 5, 7, ... (SU(2) irreps) | Eigenvalues with ~1e-6 tolerance binning | ❓ Unknown | Cluster eigenvalues by proximity → count cluster sizes → compare to (2j+1) | No peaks at (2j+1), or uniform random distribution | Finite-lattice breaks degeneracies → expect broadening, not exact |
| **10. r-stat / level spacing statistics** | GOE/GUE random matrix vs Poisson (integrable) | r-stat distribution: GOE (chaotic) vs Poisson (integrable) for W=0 vs W=20 | r_stat per case (already computed) | ✅ Yes (r_stat in JSON) | Plot r_stat(W=0) vs r_stat(W=20) → expect Poisson→GOE transition | No transition, or r_stat insensitive to W | r-stat aggregate may miss energy-resolved structure (test per-band) |

---

## 4. Raw Data Availability Questions

**Before designing new tests, audit what exists in `reports/RUNS/`:**

### ✅ Known to exist:
- `true_ipr_mean` — aggregate IPR across all eigenstates (W=0, W=20)
- `r_stat` — level spacing statistic (per case)
- `s1_size`, `disorder_strength`, `seed` — metadata
- `control` type (for Negative Controls)
- `family` (spectral_circle, ring, wilson_ring) for Gate 4B

### ❓ Unknown / need to check:
1. **Eigenvalues saved per-state?**  
   → Check: `grep -r "eigenvalues" reports/RUNS/gate4_fss_v0.1.24/batches/batch_01/results.json`  
   → If YES: can test zero modes, multiplicities, energy-resolved IPR  
   → If NO: need rerun to save eigenvalues

2. **Eigenvectors saved per-state?**  
   → Check: `grep -r "eigenvectors\|psi" reports/RUNS/gate4_fss_v0.1.24/batches/batch_01/results.json`  
   → If YES: can test spinor structure, Kronecker decomposition, angular harmonics  
   → If NO: need rerun (eigenvectors = largest data, may be omitted)

3. **Per-state IPR?**  
   → Check: `grep -r "ipr_per_state\|ipr_list" reports/RUNS/gate4_fss_v0.1.24/batches/batch_01/results.json`  
   → If YES: can test energy-resolved localization  
   → If NO: only aggregate `true_ipr_mean` available (already used)

4. **Raw operator matrix saved?**  
   → Unlikely (too large, not needed for current tests)  
   → If missing: cannot retroactively analyze Dirac operator structure

5. **W=0 baseline for families?**  
   → Check: Gate 4B ran W=0, W=20 → confirm family differences at W=0  
   → If W=0 family contrasts exist → "gauge-like field" test already half-done

### Audit script needed:
```bash
# Create: scripts/audit_raw_data_availability.py
# Output: reports/RAW_DATA_AVAILABILITY_AUDIT_v0.1.24.md
# Check: eigenvalues, eigenvectors, per-state IPR, W=0 family data
```

---

## 5. Low-Hanging Tests (Priority Order)

### ✅ No heavy compute required (existing data)

| Test | Data Source | ETA | Output | Blocks |
|------|-------------|-----|--------|--------|
| **1. Raw Data Availability Audit** | `reports/RUNS/gate4_fss_v0.1.24/`, `negative_controls_v0.1.22/` | 1 hour | `RAW_DATA_AVAILABILITY_AUDIT_v0.1.24.md` | All downstream tests (must know what's available first) |
| **2. r-stat aggregate by control/size** | Negative Controls JSON (`r_stat` field) | 2 hours | `R_STAT_BY_CONTROL_v0.1.22.md` | Negative Controls Full Pattern Audit (adds r-stat dimension) |
| **3. W=0 family contrast check** | Gate 4B W=0 cases (if `true_ipr_mean` by family exists) | 1 hour | `W0_FAMILY_CONTRAST_v0.1.24.md` | "Gauge-like field" test (Item 7 in claim-to-test table) |
| **4. Claim-to-test mapping review** | This document + Tom's CAMP framework docs | 4 hours | Updated `LAWRENCE_CLAIM_TO_TEST_MATRIX_v0.2.md` | None (docs-only) |
| **5. Clean low-spectrum test design** | Claim-to-test table + RAW_DATA_AVAILABILITY_AUDIT | 6 hours | `LOW_SPECTRUM_TEST_DESIGN_v0.1.md` | Raw Data Availability Audit |

### ⚠️ Rerun required (new experiments)

| Test | Why rerun needed | Compute cost | ETA | Blocks |
|------|------------------|--------------|-----|--------|
| **6. Energy-resolved IPR** | Per-state IPR not saved (only aggregate) | ~6 hours (216 cases rerun) | 1 week | Multiplicity tests, zero-mode tests |
| **7. Multiplicity histograms** | Eigenvalues not saved per-state (unknown) | ~6 hours (if eigenvalues missing) | 1 week | SU(2) irrep test (Item 2) |
| **8. D₂ multifractal spectrum** | Requires eigenvector components (unknown if saved) | ~12 hours (if eigenvectors needed) | 2 weeks | Multifractal analysis (out of v0.1 scope) |
| **9. Matched eigenvector null** | Eigenvectors not saved (likely) | ~12 hours | 2 weeks | Spinor structure test (Item 6) |
| **10. S³×S² geometry port** | S³×S² not implemented | ~6 months (2 weeks dev + 2 weeks validation + 4 months full run) | 6 months | Cross-geometry comparison (Item 5) |

---

## 6. Recommended Next Step

**Sequential path (no parallelism until audit complete):**

### Step 1: Finish Negative Controls Full Pattern Audit ✅ DONE
- Status: **COMPLETED** (commit `e3f3b95`)
- Verdict: **HARNESS_NONSPECIFIC** (broken_wilson_term reproduced full pattern)
- Outcome: Cannot strengthen S³×S¹-specific claims until Wilson term diagnostic complete

### Step 2: Raw Data Availability Audit (NEXT IMMEDIATE ACTION)
**Why:** Must know what exists before designing any new test.

**Action:**
```bash
# Create script
scripts/audit_raw_data_availability.py

# Audit:
# - Gate 4B v0.1.24 (216 cases)
# - Negative Controls v0.1.22 (54 cases)

# Output:
reports/RAW_DATA_AVAILABILITY_AUDIT_v0.1.24.md

# Questions to answer:
# - Eigenvalues saved per-state? YES/NO
# - Eigenvectors saved per-state? YES/NO
# - Per-state IPR? YES/NO
# - W=0 family data available? YES/NO
# - r_stat only aggregate or per-band? AGGREGATE/PER-BAND
```

**ETA:** 1–2 hours (read JSON structure, grep for fields, document findings)

### Step 3: Choose clean-spectrum mini-test (AFTER Step 2)

**Decision tree:**
- IF eigenvalues saved → Test zero modes (Item 3) OR multiplicities (Item 9)
- IF eigenvectors saved → Test Kronecker decomposition (Item 1)
- IF only aggregate metrics → Test r-stat by control (Item 10) OR W=0 family contrast (Item 7)
- IF nothing useful saved → Skip to Wilson term diagnostic (broken_wilson_term control construction review)

**Do NOT design new test before Step 2 complete** — risks wasting time on test requiring unavailable data.

---

## 7. Final Verdict

**Status:** ✅ **CLAIM_TO_TEST_MATRIX_READY_FOR_REVIEW**

**What this document provides:**
- 10 conceptual claims mapped to computational observables
- Safety boundary (forbidden vs allowed claims)
- Pre-registered metrics BEFORE looking at data (prevents p-hacking)
- Data availability questions (must audit before test design)
- Low-hanging tests prioritized (existing data first)
- Recommended sequential path (audit → test design → execution)

**What this document does NOT provide:**
- Validation of Tom Lawrence's theory (out of scope)
- Physical interpretation of computational signatures (forbidden)
- New experiment designs (blocked on Raw Data Availability Audit)

**Next action:**
1. Review this document for scientific accuracy
2. Run Raw Data Availability Audit (Step 2)
3. Update this document to v0.2 based on audit findings
4. Choose ONE low-hanging test from Table in Section 5

**Caveats:**
- Claim-to-test mappings are **hypothetical** — computational signature may NOT exist
- Even if signature found, does NOT prove physical theory (finite-lattice toy only)
- Current Gate 4B status (HARNESS_NONSPECIFIC) weakens S³×S¹-specific claims
- Wilson term diagnostic must complete before ANY geometric-specificity claims

---

**Last updated:** 2026-05-31  
**Status:** DRAFT — ready for review  
**Next review trigger:** After Raw Data Availability Audit complete  
**Version:** v0.1 (initial mapping, pre-audit)
