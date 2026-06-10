# AV-2 E1 — Pre-registered Claim: Sparse Reconstruction over Mixed Bilinear Dictionary

**Gate:** AV2-E1
**Date pre-registered:** 2026-06-10 (BEFORE any fitting)
**Question type:** [x] descriptive  [ ] predictive  [ ] causal
**Status:** research_only — no physical promotion
**Precondition:** AV-2 G2 PASS (g_l0≈0, mixed_l0≈cos¹) — confirmed 2026-06-10

---

## Estimand

*Can the two-component radial bilinear dictionary {φφ, gg, φg, gφ} + const
reconstruct sin(2α) (the target eq.49 radial layer) more sparsely than the
phi-only dictionary that failed in AV-1c′?*

Population: S³ Dirac eigenmodes, levels from the pre-registered mode set (see below).
Comparator: AV-1c′ phi-only dictionary (residual 12.38%, dense, FAIL).
Endpoint: greedy sparse reconstruction residual (weighted L2) on α ∈ [0, π/2].
Summary measure: residual % at ≤5 terms (and separately ≤8 terms).
MCID: residual drops below 5% = obstruction is lifted.

---

## Pre-registered Mode Set (written BEFORE fitting)

Modes included in dictionary (from G2 scope):

| Mode (n,l) | Included | Reason |
|------------|----------|--------|
| (0,0) | YES | Lowest boundary-family, g_l0 KEY mode |
| (1,0) | YES | Next l=0 mode |
| (2,0) | YES | Next l=0 mode |
| (1,1) | YES | First l=1 mode for control |
| (2,1) | YES | l=1 control |
| (3,2) | NO  | l=2 — excluded (boundary exponent too high, l=0 sufficient) |

Dictionary atoms for each mode (n,l) in set:

| Atom type | Formula | Count |
|-----------|---------|-------|
| phi_sq | φ_nl(α)² | 3 modes (l=0: n=0,1,2) |
| g_sq | g_nl(α)² | 3 modes (l=0: n=0,1,2) |
| mixed_phi_g | φ_nl(α) · g_nl(α) | 3 modes (l=0: n=0,1,2) |
| cross_phi_phi | φ_nl · φ_n'l' | all ordered pairs |
| cross_g_g | g_nl · g_n'l' | all ordered pairs |
| cross_phi_g | φ_nl · g_n'l' | all ordered pairs |
| constant | 1 | 1 |

Total atoms (approximate): ~40-60 before deduplication.

**Priority ordering for greedy selection:**
By G2 result, atoms expected to be selected first:
1. mixed_phi_g (l=0) — exponent ≈ cos¹, expected to dominate
2. g_sq (l=0) — exponent ≈ cos⁰, expected to set the boundary level
3. phi_sq (l=0) — cos² contribution to interior
4. constant — DC offset

---

## Pre-registered Pass Criteria

| Outcome | Condition | Meaning |
|---------|-----------|---------|
| **STRONG_PASS** | residual < 5% using ≤5 terms | Sparse; obstruction lifted; E2 warranted |
| **WEAK_PASS** | residual < 5% using ≤8 terms | Moderate sparsity; E2 warranted |
| **MIXED** | residual 5–10% OR 5–15 terms | Partial; boundary improved but not sparse |
| **FAIL** | residual > 10% regardless of terms | Obstruction persists at full level |

---

## Pre-registered Algorithm

1. Normalize all dictionary atoms to unit L2 norm on α ∈ [0, π/2].
2. Greedy matching pursuit: at each step select atom with maximum inner product
   with current residual.
3. After each selection: solve least-squares projection onto selected atoms.
4. Report residual at each step (1, 2, 3, 4, 5 terms).
5. Sensitivity: also report with C-H weight sin²α (eq. 3.38 convention).

Both unweighted and sin²α-weighted residuals must be < 5% for STRONG_PASS.

---

## Kill Conditions (pre-registered)

- If STRONG_PASS: proceed to E2 (angular singlet check).
- If WEAK_PASS: proceed to E2 with note "moderate sparsity, E2 will determine if singlet structure holds."
- If FAIL: record in `null_results/` as `20260610-e1-mixed-reconstruction-fail.md`.
  Conclusion: "AV-1c′ obstruction persists at full two-component level; dense-series conclusion final."

---

## What This Does NOT Mean

1. NOT full angular verification — angular quantum numbers not yet checked.
2. NOT "Tom's ansatz solved" — this is radial layer only.
3. NOT H-T1 promoted — H-T1 remains in null_results/.
4. NOT physical λ fixed (λ = FREE_COUPLING_PARAMETER).
5. NOT safe_for_runtime.
6. PASS does NOT mean the reconstruction uses physically correct bilinears —
   that requires E2 angular singlet check.
