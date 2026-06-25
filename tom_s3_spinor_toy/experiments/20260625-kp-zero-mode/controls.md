---
experiment_id: 20260625-kp-zero-mode
date: 2026-06-25
---

# controls.md — KP Zero-Mode Analysis

## Positive Control (known-good input)

**Test:** C₂(G₂; 0,0) = 0, C₂(SU(3); 0,0) = 0 → λ²=0 (trivial rep IS a zero mode)

```
g2_casimir(0,0) = 0  ✓
su3_casimir(0,0) = 0  ✓
Trivial rep: λ² = 0-0 = 0  ✓  (expected: zero mode exists)
```

**Result:** PASS — trivial representation correctly identified as zero mode.

---

## Negative Control (known-bad input, must NOT give zero mode)

**Test 1:** G₂(1,0) = 7-dim fundamental — must NOT give zero mode via σ=(0,0)
```
g2_casimir(1,0) = 4
su3_casimir(0,0) = 0
λ²(G₂(1,0), σ=(0,0)) = 4 - 0 = 4 > 0  ✓  (expected: NOT a zero mode)
```

**Test 2:** G₂(0,1) = 14-dim adjoint — must NOT give zero mode via any fibre σ
```
g2_casimir(0,1) = 8
su3_casimir(1,1) = 3  (max in fibre)
λ²_min(G₂(0,1)) = 8 - 3 = 5 > 0  ✓  (expected: NOT a zero mode)
```

**Test 3:** σ=(1,1) in fibre via G₂(1,0) — most dangerous candidate (largest fibre Casimir)
```
g2_casimir(1,0) = 4
su3_casimir(1,1) = 3
λ²(G₂(1,0), σ=(1,1)) = 4 - 3 = 1 > 0  ✓  (expected: NOT a zero mode, gap=1)
```

**Result:** All 3 negative controls PASS — no non-trivial zero modes.

---

## No-Collapse Tests

| Test | What changes | Expected | Actual |
|------|-------------|----------|--------|
| Data swap: S⁺⊗S⁻ decomp | Check dim=16 | dim=16 | PASS |
| Noise: swap source↔target | 1 trivial source, 2 trivial target | ind=-1≠+1 | Asymmetry confirmed (not symmetric) |
| Scale: larger G₂ reps (m+n≤6) | C₂(G₂) grows fast | gap stays ≥1 | PASS (min gap=1 at G₂(1,0)) |
| Alternative: ind formula | ind=src-tgt=2-1=1 | ind=1 | PASS |
| Negative control | G₂(1,0) not zero mode | λ²≥1 | PASS |

---

## Additional Verification

### Tensor product dimensions (dim check)
- S⁺ = (0,1)⊕(0,0), dim = 3+1 = 4 ✓
- S⁻ = (1,0)⊕(0,0), dim = 3+1 = 4 ✓
- S⁺⊗S⁻: dim = 4×4 = 16 ✓
- S⁻⊗S⁻: dim = 4×4 = 16 ✓

### Consistency with ind=1 (Atiyah-Singer)
ind = dim ker - dim coker = 1 - 0 = 1 ✓

The trivial G₂-rep component gives:
- Source dimension: 2 (two G₂-invariant sections of S⁺⊗S⁻)
- Target dimension: 1 (one G₂-invariant section of S⁻⊗S⁻)
- dim ker = 2-1 = 1, dim coker = 1-1 = 0 → ind=1 ✓

### Normalization note (see kp_zero_mode.py docstring)
The KP spectral gap is computed in mixed normalization:
- G₂ Casimir: |α_long|²=2 convention
- SU(3) Casimir: SU(3) self-normalization (|α_{SU(3)}|²=2)

In G₂-consistent normalization, C₂_G₂-norm(SU(3)) = C₂_self(SU(3))/3.
Correct gap: C₂(G₂;1,0) - C₂_G₂-norm(SU(3);1,1) = 4 - 1 = 3.
Computed gap: 4 - 3 = 1 (conservative bound, still positive → conclusion holds).
