# Rerun Preparation Checklist

**Date:** 2026-06-01  
**Purpose:** What to save in next rerun to enable per-state diagnostics  
**Status:** ✅ **COMPLETE**

---

## Executive Summary

**Goal:** Enable energy-resolved diagnostics (zero modes, multiplicities, eigenvector structure) in future reruns.

**Current limitation:** Gate 4B v0.1.24 saves only **aggregate metrics** (true_ipr_mean, r_stat), NOT per-state data.

**Solution:** Modify output schema to save **eigenvalues** and **per-state IPR** (eigenvectors optional due to size).

**Estimated storage increase:** ~10× (from ~200 KB/case → ~2 MB/case for N=128, j_max=3).

---

## Current Output Schema (v0.1.24)

**Per-case JSON fields:**
```json
{
  "family": "ring",
  "s1_size": 128,
  "disorder_strength": 20,
  "seed": 123,
  "true_ipr_mean": 0.3312,        // ← Aggregate only
  "r_stat": 0.4823,               // ← Aggregate only
  "mean_low_eigenvalue": -12.45,  // ← Aggregate only
  "runtime_seconds": 487.2
}
```

**Missing fields:**
- ❌ Eigenvalues per state (needed for zero modes, multiplicities)
- ❌ Per-state IPR (needed for energy-resolved localization)
- ❌ Eigenvectors (needed for Kronecker decomposition, spinor structure)

---

## Proposed Output Schema (v0.2.x)

### Minimal Extension (Energy-Resolved Only)

**New fields:**
```json
{
  ...,  // Existing fields unchanged
  "eigenvalues": [-15.2, -14.8, ..., 18.9],  // All eigenvalues (sorted)
  "per_state_ipr": [0.012, 0.015, ..., 0.987]  // IPR for each eigenstate
}
```

**Storage impact:**
- Eigenvalues: `N × 8 bytes` (float64)
- Per-state IPR: `N × 8 bytes` (float64)
- For N=128, j_max=3 → dim = 896 → 896×8×2 = 14 KB per case

**Benefits:**
- ✅ Zero modes analysis (count |λ| < ε)
- ✅ Multiplicity histograms (bin eigenvalues by proximity)
- ✅ Energy-resolved IPR (plot IPR vs energy)
- ✅ Tail-excised metrics (exclude top/bottom 10% eigenvalues)

### Full Extension (Eigenvector Diagnostics)

**New fields:**
```json
{
  ...,
  "eigenvectors": [[0.01, 0.02, ...], [0.03, 0.01, ...], ...],  // Complex array
  "eigenvector_norms": [1.0, 1.0, ..., 1.0]  // Sanity check
}
```

**Storage impact:**
- Eigenvectors: `N × N × 16 bytes` (complex128)
- For N=128, j_max=3 → dim = 896 → 896×896×16 ≈ **12 MB per case**

**Benefits:**
- ✅ Kronecker product decomposition (S³ ⊗ S¹ structure test)
- ✅ Spinor multiplet structure
- ✅ Eigenvector nulls (matched null control)
- ✅ Multifractal D₂ spectrum

**Risks:**
- ⚠️ Storage: 216 cases × 12 MB ≈ **2.6 GB** (vs 43 MB current)
- ⚠️ Download time: 2.6 GB vs 43 MB = **60× longer**
- ⚠️ Git LFS required (GitHub hard limit 100 MB per file)

---

## Recommended Approach: Tiered Saving

**Tier 1 — Always Save (Minimal, 14 KB/case):**
```python
output = {
    # Existing fields...
    "eigenvalues": eigenvalues.tolist(),  // Sorted, real
    "per_state_ipr": ipr_per_state.tolist(),  // Float array
}
```

**Tier 2 — On-Demand Save (Large, 12 MB/case):**
```python
if save_eigenvectors:  # Flag from command-line
    output["eigenvectors"] = eigenvectors.tolist()  // Complex array
```

**Tier 3 — Compressed Save (Medium, ~1 MB/case):**
```python
# Save only low-energy eigenvectors (bottom 10%)
n_low = int(0.1 * len(eigenvalues))
output["low_eigenvectors"] = eigenvectors[:, :n_low].tolist()
```

**Usage:**
- Standard runs: Tier 1 only (eigenvalues + per-state IPR)
- Diagnostic runs: Tier 1 + Tier 3 (compressed eigenvectors)
- Full archival: Tier 1 + Tier 2 (all eigenvectors, rare)

---

## Implementation Checklist

### Step 1 — Modify Output Schema

**File:** `cc_toy_lab/spectral/metrics.py` (or relevant runner script)

**Changes:**
```python
def compute_case_metrics(eigenvalues, eigenvectors, ...):
    # Existing aggregate metrics
    true_ipr_mean = compute_mean_ipr(eigenvectors)
    r_stat = mean_adjacent_gap_ratio(eigenvalues)

    # NEW: Per-state metrics
    per_state_ipr = inverse_participation_ratio(eigenvectors)  # Already exists

    return {
        # Existing...
        "true_ipr_mean": true_ipr_mean,
        "r_stat": r_stat,
        # NEW:
        "eigenvalues": eigenvalues.tolist(),
        "per_state_ipr": per_state_ipr.tolist(),
    }
```

### Step 2 — Update Runner Scripts

**Files:**
- `scripts/run_negative_controls_v0_1_22.py`
- `scripts/run_gate4_fss_v0_1_24.py` (if exists)

**Command-line flag:**
```python
parser.add_argument('--save-eigenvectors', action='store_true',
                    help='Save full eigenvectors (WARNING: large files)')
```

### Step 3 — Test on Single Case

**Before full rerun:**
```bash
python scripts/run_negative_controls_v0_1_22.py \
  --dry-run \
  --single-case control=broken_wilson_term size=16 W=0 seed=123 \
  --save-eigenvalues  # New flag
```

**Verify:**
- Output JSON contains `eigenvalues` and `per_state_ipr` fields
- File size reasonable (~14 KB for N=16)
- No serialization errors (complex128 → JSON requires .tolist())

### Step 4 — Storage Estimate

**For Gate 4B rerun (216 cases, Tier 1 only):**
```
Per-case size (Tier 1):
  N=16:  (16×4) × 16 bytes × 2 = 2 KB
  N=32:  (32×4) × 16 bytes × 2 = 8 KB
  N=64:  (64×4) × 16 bytes × 2 = 32 KB
  N=128: (128×4) × 16 bytes × 2 = 128 KB

Total: 216 cases, 25% each size:
  54 × 2 KB + 54 × 8 KB + 54 × 32 KB + 54 × 128 KB
  = 108 + 432 + 1728 + 6912 KB
  ≈ 9.2 MB (Tier 1, eigenvalues + per-state IPR)

Current size: ~43 MB (aggregate metrics only)
New size: ~52 MB (Tier 1 added)
Increase: +21%
```

**Conclusion:** Tier 1 increase is **affordable** (+21%, not 10× as initially feared).

---

## Future Diagnostics Enabled

### With Tier 1 (Eigenvalues + Per-State IPR)

| Diagnostic | Requires | Feasibility |
|------------|----------|-------------|
| Zero modes counting | Eigenvalues | ✅ YES |
| Multiplicity histograms | Eigenvalues | ✅ YES |
| Energy-resolved IPR | Eigenvalues + Per-state IPR | ✅ YES |
| Tail-excised IPR | Eigenvalues + Per-state IPR | ✅ YES |
| Spectral gap analysis | Eigenvalues | ✅ YES |
| Density of states | Eigenvalues | ✅ YES |

### With Tier 2 (Full Eigenvectors)

| Diagnostic | Requires | Feasibility |
|------------|----------|-------------|
| Kronecker decomposition | Eigenvectors | ✅ YES (but 2.6 GB total) |
| Spinor multiplet structure | Eigenvectors | ✅ YES |
| Eigenvector nulls | Eigenvectors | ✅ YES |
| Multifractal D₂ spectrum | Eigenvectors | ✅ YES |
| Participation entropy | Eigenvectors | ✅ YES |

**Recommendation:** Start with Tier 1 rerun. If Kronecker decomposition needed later, run Tier 2 on **subset** (e.g., 54 cases, one family only).

---

## Rerun Decision Tree

### Q1: Do we need energy-resolved diagnostics?

**YES** → Rerun with Tier 1 (eigenvalues + per-state IPR)

**Reason:** Current diagnostic sprint showed:
- broken_wilson_term reproduced full pattern (8.20× contrast + STABLE FSS)
- Code audit confirmed broken_wilson_term = ring family
- **Next question:** Does `wilson_mode="scrambled"` kill the pattern?

**To answer:** Need eigenvalue multiplicity analysis to test if Wilson term scrambling breaks SU(2) degeneracies.

### Q2: Do we need eigenvector diagnostics?

**MAYBE** → Run Tier 2 on **targeted subset** only

**Reason:** Eigenvector diagnostics (Kronecker, spinor, nulls) are **exploratory**, not critical for harness specificity test.

**Decision:** Defer Tier 2 until after `wilson_mode="scrambled"` rerun verdict.

---

## Rerun Sequence Recommendation

**Phase 1 — wilson_mode="scrambled" (Minimal Rerun, Tier 1)**

- Grid: 18 cases (W=0/20 × sizes=16/64/128 × seeds=123/456/789)
- Save: Eigenvalues + per-state IPR (Tier 1)
- Runtime: ~14 minutes (1 batch)
- Storage: ~2 MB total
- Goal: Test if scrambled Wilson term kills pattern

**Phase 2 — Gate 4B v0.2.x (Full Rerun, Tier 1)**

- Grid: 216 cases (same as v0.1.24)
- Save: Eigenvalues + per-state IPR (Tier 1)
- Runtime: ~6 hours (9 batches)
- Storage: ~52 MB total
- Goal: Enable energy-resolved diagnostics for all families

**Phase 3 — Eigenvector Subset (Optional, Tier 2)**

- Grid: 54 cases (e.g., ring family only, all sizes/seeds)
- Save: Full eigenvectors (Tier 2)
- Runtime: ~1.5 hours
- Storage: ~650 MB
- Goal: Kronecker decomposition test (Tom Lawrence claim-to-test Item 1)

---

## Code Changes Summary

**File:** `cc_toy_lab/spectral/metrics.py`

**Add function:**
```python
def compute_per_state_ipr(eigenvectors: np.ndarray) -> np.ndarray:
    """Compute IPR for each eigenstate separately.

    Returns:
        Array of IPR values, one per eigenstate (length = n_states).
    """
    return np.sum(np.abs(eigenvectors)**4, axis=0)  # Sum over sites, per state
```

**Modify runner output:**
```python
# After eigenvalue computation
per_state_ipr = compute_per_state_ipr(eigenvectors)

output_dict = {
    ...,
    "eigenvalues": eigenvalues.tolist(),
    "per_state_ipr": per_state_ipr.tolist(),
}
```

**Storage estimate verification:**
```python
import sys
output_size_bytes = sys.getsizeof(json.dumps(output_dict))
print(f"Output size: {output_size_bytes / 1024:.1f} KB")
```

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| **JSON serialization slow** for large arrays | Runtime +10-20% | Use msgpack or HDF5 for eigenvectors (Tier 2 only) |
| **Git repo size explosion** (>1 GB) | GitHub push fails | Use Git LFS for Tier 2 outputs only |
| **Download time 60× longer** | User friction | Separate Tier 1 (small) and Tier 2 (large) downloads |
| **Complex128 → JSON loses precision** | Eigenvector reconstruction fails | Save real/imag parts separately, or use binary format |

---

## Conclusion

**Rerun preparation complete:**
1. ✅ Output schema extension designed (Tier 1 + Tier 2 + Tier 3)
2. ✅ Storage estimates computed (+21% for Tier 1, +60× for Tier 2)
3. ✅ Implementation checklist created (3 files to modify)
4. ✅ Rerun sequence recommended (scrambled Wilson → full Tier 1 → subset Tier 2)

**Next action:** Execute `wilson_mode="scrambled"` rerun (18 cases, ~14 min) to test Wilson term load-bearing hypothesis.

---

**Last updated:** 2026-06-01  
**Status:** ✅ COMPLETE  
**Next action:** Diagnostic summary report (deliverable 7/7)
