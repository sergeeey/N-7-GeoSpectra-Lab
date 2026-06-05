# S³ Passive-Axis Structural Audit — Smoke

## Purpose

Replace the invalidated SVD phantom-factor test (see
`CROSS_DOMAIN_SVD_PHANTOM_TEST_INVALIDATION_2026-06-04.md`).
Probe the S³ axis structure inside `H = (D_S³)² ⊗ I + I ⊗ P_S¹` using only
static matrix-algebra checks — no eigensolve, no heavy compute.

## Invalidated Prior SVD Test

Prior SVD test was invalid by construction: mode-1 and mode-2 unfolding
matrices are transpose pairs, so their singular value spectra are identical.
That test could not distinguish the two axes. The current audit avoids
the issue by not using SVD at all.

## Methods (no eigensolve)

- **A. Block-structure test** — partition `H` into `s3_dim × s3_dim` grid of
  `s1_dim × s1_dim` blocks. Compare Frobenius norm of off-diagonal vs
  diagonal blocks.
- **B. Partial-trace test** — `Tr_{S¹}(H)` (lives in S³ basis) and `Tr_{S³}(H)`
  (lives in S¹ basis). Check diagonality and triviality.
- **C. Commutator/projector test** — for each S³ sector projector `P_i`,
  compute `||[H, P_i]||_F`.

## Smoke Cases

**Planned:** 6 subcases — 3 families (`spectral_circle`, `ring`, `wilson_ring`) × 2 disorder levels (W=0, W=20).
**Actually executed:** 2 subcases (both `spectral_circle`). Run hit the 60-second time budget after the second case; remaining 4 subcases (`ring`, `wilson_ring`) did NOT run.
**Reason:** unexpectedly slow operator-construction step in `build_s3_s1_product_operator` at `j_max=3, s1_size=16`. The audit checks themselves (block / partial-trace / commutator) ran in fractions of a second per case.

Single size: `j_max=3, s1_size=16`
→ `s3_dim = s3_dimension(3) = 7`, `s1_dim = 16`, `N = 112`.

## Results

### Block-structure test (off-diagonal S³ blocks)

| Family | W | ||off||_F | ||diag||_F | ratio off/diag | max single off-block | verdict |
|---|---:|---:|---:|---:|---:|---|
| spectral_circle | 0 | 0.00e+00 | 878.3109 | 0.00e+00 | 0.00e+00 | ZERO_OFFDIAG |
| spectral_circle | 20 | 0.00e+00 | 907.9818 | 0.00e+00 | 0.00e+00 | ZERO_OFFDIAG |

### Partial-trace test

| Family | W | Tr_{S¹}→S³ diag-fraction | verdict | Tr_{S³}→S¹ diag-fraction | scalar identity? | verdict |
|---|---:|---:|---|---:|---|---|
| spectral_circle | 0 | 1.000000 | DIAGONAL | 0.970483 | False | NONDIAGONAL |
| spectral_circle | 20 | 1.000000 | DIAGONAL | 0.906170 | False | NONDIAGONAL |

### Commutator / projector test

| Family | W | max ||[H, P_i]||_F | verdict |
|---|---:|---:|---|
| spectral_circle | 0 | 0.00e+00 | ALL_ZERO |
| spectral_circle | 20 | 0.00e+00 | ALL_ZERO |

## Interpretation Limits

These tests measure structural properties of one specific construction:
`H = (D_S³)² ⊗ I + I ⊗ P_S¹` with `D_S³` implemented as a diagonal mockup
(see `cc_toy_lab/spectral/dirac_s3.py`).

- They do NOT validate or refute any physical claim about S³×S¹ geometry.
- They do NOT extend to a Dirac operator with a real spin-connection.
- They do NOT make any statement about the Gate 4B IPR contrast or the
  `DISCRETIZATION_SENSITIVE / GEOMETRY_AGNOSTIC` verdict.
- They are a smoke probe of a specific architectural property of the
  current toy operator, nothing more.

## Safe phrasing for downstream use

> "Current evidence suggests the S³ sector may be structurally passive or
> weakly coupled in the current toy operator, but this requires further
> verification."

Stronger phrasings (e.g. "all sensitivity comes from S¹", "S³ is irrelevant")
are NOT supported by these tests and must NOT be used.

## Verdict

**STRUCTURAL_AUDIT_INCONCLUSIVE**

Rationale: the auto-aggregator returned `STRUCTURAL_AUDIT_SMOKE_COMPLETED` based on the two cases that completed (both `spectral_circle`, both ZERO_OFFDIAG + ALL_ZERO + Tr_{S¹}→DIAGONAL). However, only 2 of 6 planned subcases ran due to the time budget. The cross-family confirmation (`ring`, `wilson_ring`) that the audit was designed to provide is **missing**. Honest reading: the observations for the two executed cases are internally consistent and consistent with the algebraic expectation for an `H = diag(A) ⊗ I + I ⊗ B` construction, but the cross-family coverage required to upgrade the verdict to `STRUCTURAL_AUDIT_SMOKE_COMPLETED` was not achieved in this run.

What the two completed cases show (limited to `spectral_circle` only):
- All off-diagonal S³-blocks of `H` are exactly zero.
- `Tr_{S¹}(H)` is exactly diagonal in the S³ basis.
- `Tr_{S³}(H)` is non-diagonal (the S¹ structure is non-trivial) and not a scalar multiple of identity.
- `[H, P_i] = 0` (exact) for every S³ projector `P_i`.

What this means under cautious phrasing:

> "Current evidence suggests the S³ sector may be structurally passive or weakly coupled in the current toy operator, but this requires further verification."

Total audit time: 77.401 seconds. Cases executed: 2 of 6 planned. No eigensolve was performed in any case.

**Next step (not executed in this run):** rerun with a higher time budget (e.g. 180 s) or pre-cache the operator build, so that the remaining 4 cases (`ring×{0,20}`, `wilson_ring×{0,20}`) are covered. Only then can the verdict legitimately be upgraded.

## Provenance

- Script: `scripts/audit_s3_passive_axis_structure.py`
- Replaces: `scripts/cross_domain_svd_phantom_test.py` (see invalidation report)
- No commits, no push, no external claims.
