# Batch Design — v0.1.22 Negative Controls
# FL Full-Ladder Step 1 (experiment.yaml equivalent)

**Date:** 2026-06-03
**Version:** v0.1.22
**Derived from:** CLAIM_v0.1.22.md + ESTIMAND_v0.1.22.md
**Skeptic audit:** SKEPTIC_AUDIT_GATE4B_v0.1.22.md

---

## What Was Planned (Pre-Registration v0.1.22)

The existing preregistration (`S3_S1_NEGATIVE_CONTROLS_PREREGISTRATION_v0.1.22.md`)
defines a pilot grid of 54 cases:
- 3 controls (random_hermitian, scrambled_geometry, broken_wilson)
- 2 disorder strengths (W=0, W=20)
- 3 sizes (s1_size = 16, 32, 64)
- 1 j_max = 3
- 3 seeds (123, 456, 789)

---

## What the Skeptic Audit Adds

The skeptic audit (2026-06-03) identified that spectral_circle requires a
dedicated diagnostic not covered by the original 3-control design.

**Required additions to pre-registered grid:**

### Addition 1: spectral_circle on scrambled_geometry

**Why:** spectral_circle shows IPR(W=20) decreasing with N on S³×S¹
(0.175 → 0.070 from s1_size=16→128). We must determine if this is
a structural artifact of the spectral_circle operator or a geometry response.

**Grid:**
- Operator: spectral_circle with scrambled geometry
  (same spectral_circle basis, but S¹ coupling indices permuted randomly)
- W: 0 and 20
- s1_size: 16, 32, 64, 128 (all 4, not just 3 — needed for trend analysis)
- j_max: 3 (primary)
- seeds: 123, 456, 789
- Cases: 1 operator × 2 W × 4 sizes × 1 j_max × 3 seeds = **24 cases**

**Expected outcomes:**
- If IPR(W=20) trend matches S³×S¹ spectral_circle (decreasing) → STRUCTURAL ARTIFACT
- If IPR(W=20) trend diverges (higher or plateau on scrambled) → GEOMETRIC SIGNAL

### Addition 2: s1_size=128 for primary controls

**Why:** Gate 4B FSS finding is strongest at s1_size=128 (contrast 24.90×).
Pre-registered grid only goes to s1_size=64. Without s1_size=128 for controls,
we cannot fully compare FSS trajectories.

**Grid extension:**
- Add s1_size=128 to all 3 existing controls (random_hermitian, scrambled_geometry,
  broken_wilson)
- W=0 and W=20
- j_max=3, seeds 123/456/789
- Additional cases: 3 controls × 2 W × 1 size × 1 j_max × 3 seeds = **18 cases**

---

## Full Revised Batch Grid

| Batch | Operator | W | s1_sizes | j_max | Seeds | Cases |
|-------|----------|---|----------|-------|-------|-------|
| Batch 1 | random_hermitian | 0,20 | 16,32,64,128 | 3 | 123,456,789 | 24 |
| Batch 2 | scrambled_geometry | 0,20 | 16,32,64,128 | 3 | 123,456,789 | 24 |
| Batch 3 | broken_wilson | 0,20 | 16,32,64,128 | 3 | 123,456,789 | 24 |
| Batch 4 | spectral_circle_scrambled | 0,20 | 16,32,64,128 | 3 | 123,456,789 | 24 |
| **Total** | | | | | | **96 cases** |

*(j_max=2 as secondary if compute budget allows)*

---

## Operator Implementations Required

### Control A: random_hermitian
```python
import numpy as np

def build_random_hermitian(N, W, seed):
    rng = np.random.default_rng(seed)
    # Off-diagonal: random Hermitian (no geometric structure)
    H_off = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    H_off = (H_off + H_off.conj().T) / (2 * np.sqrt(N))
    # Diagonal: same Anderson disorder as Gate 4B
    diag = rng.uniform(-W, W, N)
    H = H_off.copy()
    np.fill_diagonal(H, diag)
    return H
```

**Verification check:** H must be Hermitian (H == H†), eigenvalues real.

### Control B: scrambled_geometry
```python
def build_scrambled_geometry(H_s3s1, seed):
    """
    Take the S³×S¹ operator H and permute rows+columns randomly.
    Preserves: matrix dimension, sparsity pattern statistics, disorder amplitude.
    Destroys: S³ harmonic block structure, S¹ coupling order.
    """
    rng = np.random.default_rng(seed)
    N = H_s3s1.shape[0]
    perm = rng.permutation(N)
    H_scrambled = H_s3s1[np.ix_(perm, perm)]
    return H_scrambled
```

**Note:** Build from the W=0 S³×S¹ operator, THEN permute, THEN add disorder.
This ensures the scrambling is applied to the geometric structure, not the disorder.

### Control C: broken_wilson
```python
def build_broken_wilson(s1_size, j_max, W, seed):
    """
    wilson_ring with Wilson coefficients replaced by random values.
    Preserves: matrix dimension, diagonal disorder.
    Destroys: Wilson coefficient structure (specific hopping pattern).
    """
    # Build standard wilson_ring, then randomize all off-diagonal elements
    H_wilson = build_wilson_ring(s1_size, j_max, W=0, seed=seed)
    rng = np.random.default_rng(seed + 10000)  # Different seed from disorder
    N = H_wilson.shape[0]
    # Replace non-zero off-diagonal elements with random values of same magnitude
    off_diag = H_wilson - np.diag(np.diag(H_wilson))
    mask = off_diag != 0
    magnitudes = np.abs(off_diag[mask])
    new_vals = rng.uniform(-1, 1, mask.sum()) * magnitudes
    H_broken = np.diag(np.diag(H_wilson))
    H_broken_off = np.zeros_like(off_diag)
    H_broken_off[mask] = new_vals
    H_broken += (H_broken_off + H_broken_off.T) / 2  # Symmetrize
    # Add standard Anderson disorder
    diag_disorder = rng.uniform(-W, W, N)
    np.fill_diagonal(H_broken, np.diag(H_broken) + diag_disorder)
    return H_broken
```

### Control D: spectral_circle_scrambled
Same as Control B but applied specifically to spectral_circle operator:
```python
H_sc = build_spectral_circle(s1_size, j_max, W=0, seed=seed)
H_sc_scrambled = scramble(H_sc, seed=seed + 20000)
# Add Anderson disorder AFTER scrambling
```

---

## Analysis Plan (Post-Batch)

For each control and each s1_size, extract:
1. `true_ipr_w0` = mean(Σ|ψᵢ|⁴) for bottom 10% eigenstates at W=0
2. `true_ipr_w20` = same at W=20
3. `contrast` = true_ipr_w20 / true_ipr_w0
4. `r_stat_w0`, `r_stat_w20` = adjacent gap ratios (report PER FAMILY, NOT aggregate)

**Key comparison:**

| Metric | Gate 4B ring | Gate 4B wilson | Negative control target |
|--------|-------------|----------------|------------------------|
| IPR(W=20) s1=16 | 0.326 | 0.252 | Should NOT show plateau |
| IPR(W=20) s1=128 | 0.339 | 0.266 | Should be << 0.20 |
| Contrast s1=128 | ~29.7× | ~34.1× | Should be << 7.15× |
| IPR(W=20) trend | FLAT | FLAT | Should DECREASE |

**Decision table per control:**

| Outcome | Verdict |
|---------|---------|
| IPR(W=20) decreasing AND contrast < 2.0× | CORRECTLY REJECTED ✓ |
| IPR(W=20) decreasing AND 2.0× ≤ contrast < 7.15× | WEAK SIGNAL — investigate |
| IPR(W=20) flat AND contrast ≥ 7.15× | FALSE POSITIVE ✗ — Gate 4B specificity FAILS |

---

## Pre-Batch Checklist (Dry Run Required)

Before full 96-case run:
- [ ] Implement all 4 operator builders
- [ ] Verify H is Hermitian for each control (H == H†, tol=1e-10)
- [ ] Dry run: 1 case each (s1_size=32, W=20, seed=123) for all 4 controls
- [ ] Verify true_IPR computation uses same v0.1.21 formula as Gate 4B
- [ ] Check runtime: estimate from dry run × 96 cases
- [ ] Confirm output format matches Gate 4B merged/*.json schema

---

**Status:** DESIGN COMPLETE — ready for implementation
**FL Step:** 1 COMPLETE
**Next:** Code implementation + dry run
**Date:** 2026-06-03
