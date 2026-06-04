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
| s1_size | 160, 192 |
| W | 0, 20 |
| j_max | 3 |
| seeds | 123, 456, 789 |
| alpha | 0.0 |
| **Total** | **2 × 2 × 2 × 1 × 3 = 24 cases** |

True matrix dimensions (110×s1):
- s1=160, j_max=3: N = 110 × 160 = 17600  (eigh peak ~20 GB — feasible on 32GB)
- s1=192, j_max=3: N = 110 × 192 = 21120  (eigh peak ~28 GB — borderline on 32GB)

**Infeasible with dense eigh:** s1=256 (N=28160, ~50GB), s1=512 (N=56320, ~200GB).
To reach s1≥256, a sparse iterative eigensolver (ARPACK `eigsh` for bottom-10%
eigenpairs) is required — separate work item, NOT this pre-registration.

Runtime estimate: s1=160 ~700s/case, s1=192 ~1200s/case → ~6 hours total for 24
cases. Server-only (Hetzner CX52 or larger).

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
