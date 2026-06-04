# Gate 5 — Extended FSS Pre-Registration v0.1.25

**Date:** 2026-06-03
**Status:** PRE-REGISTERED (written before any s1≥256 execution)
**Prerequisite:** Gate 4B v0.1.24 SIGNAL_PRESERVED (7.07×), Negative Controls COMPLETE
**Question type:** Descriptive

---

## Purpose

Gate 4B FSS trend (s1=16→128): STRENGTHENING (3.76× → 24.90×).
Gate 5 asks: does the trend continue, saturate, or reverse at s1=256 and 512?

**This matters because:**
- Trend saturating → finite localization length estimated, stronger claim
- Trend continuing → signal robust at larger N, no crossover
- Trend reversing → finite-size artifact, Gate 4B claim weakened

---

## Estimand

**Population:** ring and wilson_ring families only (genuine plateau confirmed).
spectral_circle excluded from primary analysis (plateau absent per v0.1.22).

**Intervention:** Anderson disorder W=20, diagonal U(r) ∈ [-W, W]

**Comparator:** Gate 4B values at s1=128:
- ring IPR(W=20) ≈ 0.339, contrast ≈ 29.7×
- wilson_ring IPR(W=20) ≈ 0.266, contrast ≈ 34.1×

**Endpoint:** true_IPR(W=20) by s1_size — plateau vs growth vs decay

**Summary measures:**
- FSS slope (log-log regression of contrast vs N)
- IPR(W=20) absolute value at s1=256, 512

**MCID:**
- SATURATION: IPR(W=20) stable within ±15% of s1=128 value → localization length estimated
- CONTINUING: contrast grows >15% at each doubling → no saturation in range
- REVERSAL: IPR(W=20) drops >30% at s1=256 → finite-size artifact

---

## Grid (REVISED 2026-06-03 — dimension correction)

**Original grid (s1=256, 512) was INVALID** — based on the erroneous N=7×s1 label.
True operator dimension is 110×s1 (current code, S³ dim 110). See
DIMENSION_DISCREPANCY_AUDIT_v0.1.25. Corrected feasible grid:

| Parameter | Values |
|-----------|--------|
| Families | ring, wilson_ring |
| s1_size | 160, 192, 256 |
| W | 0, 20 |
| j_max | 3 |
| seeds | 123, 456, 789 |
| alpha | 0.0 |
| **Total** | **2 × 3 × 2 × 1 × 3 = 36 cases** |

True matrix dimensions (110×s1):
- s1=160: N = 17600  (dense op 5.0 GB)
- s1=192: N = 21120  (dense op 7.1 GB)
- s1=256: N = 28160  (dense op 12.7 GB — fits 32GB)

### Solver: exact block diagonalization (NOT eigsh)

The S³×S¹ operator is EXACTLY block-diagonal in the S³ index: 110 independent
S¹ chains of size s1 (verified: `connected_components` → 110 blocks). Each row
has 3 nonzeros. We diagonalize each s1×s1 block with dense `eigh` and combine.

**Verified correctness:** block solver reproduces full dense-`eigh` IPR AND
r_stat to machine precision (diff ≤ 2e-14) across ring/wilson_ring, W=0/20,
s1=32/64. Speedup ~88× (0.71s vs 62s at s1=64). Module:
`cc_toy_lab/spectral/block_ipr_solver.py` (asserts block structure at runtime).

**Why NOT sparse eigsh:** benchmarked `eigsh(which='SA', k=N//10)` at s1=64 —
returned WRONG IPR (0.036 vs true 0.296, non-convergence for 10% of eigenpairs)
AND was 6× SLOWER (399s vs 62s). ARPACK is unsuited to "bottom 10%". Recorded
in DIMENSION_DISCREPANCY_AUDIT_v0.1.25 follow-up.

**Remaining limit:** `build_s3_s1_product_operator` returns a DENSE N×N array, so
the operator itself caps at s1≈256 (12.7GB) / s1≈300 (~17GB) on 32GB. s1≥320
(op ≥20GB) and s1=512 (op 51GB) require sparse OPERATOR CONSTRUCTION — future
work item, NOT this pre-registration.

Runtime estimate (block solver): ~3–10s/case → **~3 min total for 36 cases**.
Operator build dominates at large s1. Local-feasible up to s1=256 on ≥16GB.

---

## Decision Rules (Pre-Registered)

Gate 4B FSS slope (log contrast vs log N): +1.0 (approx doubling per doubling)

| s1=160/192 IPR(W=20) for ring | Verdict |
|-------------------------------|---------|
| 0.288–0.390 (within ±15% of 0.339) | SATURATION — plateau confirmed |
| > 0.390 (growth >15%) | CONTINUING — no saturation |
| < 0.237 (drop >30%) | REVERSAL — investigate artifact |

Same criteria apply to wilson_ring (reference 0.266: SATURATION 0.226–0.306).

**Gate 5 PASS:** Both families show SATURATION or CONTINUING.
**Gate 5 WARN:** One family REVERSAL → investigate before Gate 6.
**Gate 5 FAIL:** Both families REVERSAL → Gate 4B FSS claim requires re-evaluation.

---

## What This Result Does NOT Mean

1. SATURATION does NOT prove thermodynamic limit — only that trend slows within N≤3584.
2. CONTINUING does NOT prove infinite-N localization — only finite robustness.
3. Does NOT generalize to other geometries (S²×S¹, S⁶).
4. Does NOT change negative controls verdict.

---

## Protocol Immutability

Grid, thresholds, and decision rules locked at this commit.
No post-hoc changes after s1=256 results are visible.

**Status:** PRE-REGISTERED — awaiting server execution
**Next step:** `scripts/run_gate5_fss_v0.1.25.py --dry-run`
