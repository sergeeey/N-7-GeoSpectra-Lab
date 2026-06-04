# Block Solver Verification — v0.1.25

**Date:** 2026-06-04
**Module:** `cc_toy_lab/spectral/block_ipr_solver.py`
**Test:** `tests/test_block_ipr_solver.py` (committed, reproducible)
**Status:** VERIFIED — dense-vs-block equivalence to machine precision
**Scope:** Engineering verification only. NO new scientific claims.

---

## 1. Why eigsh was rejected

A sparse iterative eigensolver (`scipy.sparse.linalg.eigsh`, `which='SA'`,
`k=N//10`) was benchmarked first, to get the bottom-10% eigenpairs for the IPR
metric. It FAILED on two counts (s1=64, N=7040):

| Method | true_ipr_mean | runtime |
|--------|---------------|---------|
| dense eigh (reference) | 0.29586 | 62 s |
| eigsh (SA, k=N//10) | **0.03571 (WRONG)** | **399 s (6× slower)** |

Cause: ARPACK is designed for `k ≪ N`. Requesting 10% of the spectrum
(704 eigenpairs) does not converge within default iterations, returning
poorly-converged, near-delocalized eigenvectors → wrong IPR. It is also slower
than a full dense solve at this fraction. eigsh is therefore unsuitable for the
"bottom 10%" metric. `[REJECTED]`

---

## 2. The correct exploit: exact block diagonalization

The S³×S¹ product operator `H = kron(D_S3², I_S1) + kron(I_S3, P_S1)` is EXACTLY
block-diagonal in the S³ index because `D_S3²` is diagonal (verified: off-diagonal
== 0). Each row has only 3 nonzeros (diagonal + 2 S¹ ring neighbours). The operator
decomposes into `s3_dimension(j_max)` independent S¹ chains of size `s1_size`
(e.g. 110 blocks of size s1 for j_max=3).

`solve_block_ipr_rstat` diagonalizes each `s1×s1` block with dense `eigh`,
concatenates the spectra, takes the global bottom-fraction for IPR, and computes
the r-statistic on the combined spectrum.

---

## 3. Dense-vs-block equivalence [VERIFIED-test]

Committed test `tests/test_block_ipr_solver.py` — `pytest -v`:

```
8 passed in 22.59s
```

Cases (all assert |Δ| < 1e-10 for BOTH true_ipr_mean and r_stat):

| family | s1 | W | result |
|--------|----|----|--------|
| ring | 16 | 0 | PASS |
| ring | 16 | 20 | PASS |
| wilson_ring | 16 | 0 | PASS |
| wilson_ring | 16 | 20 | PASS |
| ring | 32 | 20 | PASS |
| wilson_ring | 32 | 20 | PASS |

Plus structural guards:
- `test_operator_is_block_diagonal`: ring operator → uniform blocks of size s1.
- `test_block_solver_rejects_non_block_diagonal`: a dense (single-component)
  Hermitian matrix raises `ValueError` — the solver cannot silently mis-solve a
  non-block operator.

Observed agreement in-session was ~1e-14 to 1e-16 (machine precision); the test
threshold 1e-10 is a conservative guard.

---

## 4. What this unlocks

- Replaces dense `eigh` (O(N³), OOM at s1≥192 for the full operator) with cheap
  per-block diagonalization (~88× faster at s1=64: 0.71 s vs 62 s).
- Used by `run_gate5_fss_v0.1.25.py` and `run_w_sweep_v0.1.25.py` (W-sweep result
  in `W_SWEEP_PREREGISTRATION_v0.1.25.md` was produced with solver=block).

---

## 5. Limitations & block-structure caveat

1. **Validity is conditional on exact block-diagonality.** The solver ASSERTS the
   structure at runtime and raises otherwise; callers fall back to dense `eigh`.
   For ring / wilson_ring / spectral_circle (verified block-diagonal) it is exact.
2. **Operator construction is still dense.** `build_s3_s1_product_operator` returns
   a dense N×N array, so the operator build (not the eigendecomposition) caps the
   reachable size: s1≈256 (op 12.7 GB) on 32 GB; s1≥320 needs sparse construction.
3. **r-statistic equivalence** holds because block-diagonal eigenvalues are the
   union of block eigenvalues (identical multiset to dense eigh).
4. **No claim about other operators.** Verified only for the S³×S¹ product family
   tested here.

---

## 6. No new scientific claims

This document records an ENGINEERING verification (numerical equivalence of two
solvers). It makes no claim about localization, geometry, compactification, or any
physical result. It only certifies that block-solver outputs equal dense-eigh
outputs for the tested operators.

---

**Status:** FINAL
**Date:** 2026-06-04
