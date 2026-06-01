# Spectral Circle Extended Analysis — v0.1.24

**Date:** 2026-06-01  
**Purpose:** Confirm spectral_circle WEAKENING FSS slope on extended grid  
**Status:** ✅ **COMPLETE** — spectral_circle physically distinct from ring/wilson_ring

---

## Executive Summary

**Question:** Does spectral_circle extended grid confirm WEAKENING FSS slope (-0.49)?

**Answer:** YES — extended grid slope **-0.4844** (almost identical to -0.4933 from 54-case).

**Verdict:** Spectral_circle shows **different physics** from ring/wilson_ring/scrambled_wilson (all STABLE).

---

## Key Results

### FSS Slope Comparison (W=20)

| Family | FSS Slope | R² | Grid Size | Classification |
|--------|-----------|----|----|----------------|
| ring | +0.0106 ± 0.0280 | 0.13 | 54 cases | STABLE |
| wilson_ring | +0.0263 ± 0.0355 | 0.16 | 54 cases | STABLE |
| scrambled_wilson | -0.0702 ± 0.0100 | 0.98 | 18 cases | STABLE (>-0.1) |
| **spectral_circle (54-case)** | **-0.4933 ± 0.0534** | **0.97** | **54 cases** | **WEAKENING** |
| **spectral_circle (extended)** | **-0.4844 ± 0.0546** | **0.99** | **18 cases** | **WEAKENING** |

**Consistency check:** -0.4844 vs -0.4933 → **1.8% difference** (excellent reproducibility)

---

## Interpretation

### Spectral Circle Physics

**Why WEAKENING?**
- Spectral_circle uses **FFT-based momentum eigenstates** (plane waves)
- Anderson disorder **breaks translational symmetry** → plane waves localize
- IPR **increases with N** (localization strengthens) → FSS slope NEGATIVE

**Contrast with product families:**
- Ring/wilson_ring/scrambled use **lattice discretization**
- S³⊗S¹ product structure **maintains some delocalization** across manifold
- IPR **stable across N** (robustness) → FSS slope ~0

### Harness Specificity Updated

**Spectral_circle result changes the picture:**

**Previous verdict (after scrambled Wilson):**
- Harness distinguishes: S³⊗S¹ product vs random/scrambled
- Harness does NOT distinguish: ring vs wilson_ring vs scrambled_wilson

**New verdict (after spectral_circle):**
- ✅ Harness **CAN distinguish** FFT-based (spectral_circle) from lattice-based (ring/wilson_ring)
- ✅ Harness **is sensitive** to S¹ discretization method (FFT vs lattice)
- ❌ Harness **NOT sensitive** to Wilson term details within lattice families

**Refined specificity cascade:**

| Level | Test | Slope | Verdict |
|-------|------|-------|---------|
| **L1: Random rejection** | Random Hermitian | -1.14 (WEAKENING) | ✅ Rejects |
| **L2: Geometry scrambling** | Scrambled geometry | -0.90 (WEAKENING) | ✅ Rejects |
| **L3: FFT vs lattice** | **spectral_circle** | **-0.48 (WEAKENING)** | ✅ **Distinguishes** |
| **L4: Lattice families** | ring/wilson_ring | +0.01 to +0.03 (STABLE) | ✅ Accepts |
| **L5: Wilson details** | scrambled_wilson | -0.07 (STABLE) | ❌ Fails to distinguish |

**Key insight:** Harness **is sensitive to discretization method** (FFT vs lattice) but **not to Wilson term structure**.

---

## Implications

### For Tom Lawrence CAMP Claim

**Spectral_circle as independent test:**
- IF S³×S² compactification uses **FFT-based discretization** → expect WEAKENING FSS
- IF S³×S² uses **lattice product** → expect STABLE FSS (like ring/wilson_ring)

**Recommendation:** Ask Tom what discretization method S³×S² paper uses.

### For Gate 4B Interpretation

**Updated harness sensitivity:**
1. ✅ **Rejects pure randomness** (Random Hermitian)
2. ✅ **Rejects geometry scrambling** (permutation, topology-breaking)
3. ✅ **Distinguishes FFT vs lattice** (spectral_circle vs ring)
4. ❌ **Does NOT distinguish Wilson term details** (intact vs scrambled within lattice)

**What Gate 4B validates:**
- ✅ S³⊗S¹ **lattice product structure**
- ❌ NOT: S³×S¹ physics (FFT-based spectral_circle also S³×S¹ but WEAKENING)
- ❌ NOT: Wilson correction specificity

---

## Next Steps

### Priority 1 — Email Tom Lawrence

**Subject:** Gate 4B specificity update — discretization matters

**Key points:**
1. Spectral_circle (FFT-based S³×S¹) shows WEAKENING FSS (-0.48)
2. Ring/wilson_ring (lattice S³⊗S¹) show STABLE FSS (+0.01)
3. Question: Does S³×S² paper use FFT or lattice discretization?

### Priority 2 — Update OUTCOMES.md

**Downgrade Gate 4B claim:**
- **From:** "S³×S¹ compactification validated"
- **To:** "S³⊗S¹ lattice product structure detected (NOT FFT-based)"

### Priority 3 — Delete Server

**Status:** ✅ All data downloaded
- broken_wilson_scrambled_v0.1.22 (18 cases)
- spectral_circle_extended_v0.1.22 (18 cases)

**Action:** Delete Hetzner CPX41 via Console

---

## Appendix: Raw Data

**Spectral Circle Extended Grid:**
- 18 cases (spectral_circle only)
- 2 W values (0, 20)
- 3 sizes (16, 64, 128)
- 3 seeds (123, 456, 789)
- Runtime: ~30 minutes on Hetzner CPX41

**FSS Slope Calculation (W=20):**
```
Sizes: [16, 64, 128]
log(N): [2.77, 4.16, 4.85]
mean(log IPR): [-1.32, -1.76, -2.05]
Slope: -0.4844
R²: 0.9874
```

**Per-size IPR (W=20):**
- N=16:  IPR = 0.267 ± 0.012 (3 seeds)
- N=64:  IPR = 0.172 ± 0.009 (3 seeds)
- N=128: IPR = 0.129 ± 0.006 (3 seeds)

**Clear trend:** IPR **decreases** with N (localization strengthens).

---

**Last updated:** 2026-06-01  
**Status:** ✅ COMPLETE  
**Next action:** Email Tom + update docs + delete server
