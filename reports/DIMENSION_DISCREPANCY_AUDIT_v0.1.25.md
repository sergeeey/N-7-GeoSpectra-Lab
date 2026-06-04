# Dimension Discrepancy Audit — v0.1.25

**Date:** 2026-06-03
**Trigger:** Pre-flight check of Gate 5 FSS feasibility revealed reported "N ≤ 896" inconsistent with actual operator size.
**Status:** RESOLVED — labeling error confirmed, science intact
**Severity:** MEDIUM (public-facing number wrong; scientific conclusions unaffected)

---

## 1. Claim Under Audit

All reports, README, and `.zenodo.json` state:

> "Finite-lattice only (N ≤ 896)"
> FSS table: "Max N: 896 (j_max=3, s1_size=128)"

This N = 7 × s1 = (2·j_max + 1) × s1 — i.e. a **single SU(2) shell** of the S³ Dirac operator.

---

## 2. Evidence

### [VERIFIED-git] Actual operator dimension at Gate 4B commit (f7eff32)

`git show f7eff32:cc_toy_lab/spectral/dirac_s3.py` — s3_dimension formula:
```
Total dimension: sum_{k=1}^{j_max+1} 2(k+1)²
return int(sum(2 * (k + 1) ** 2 for k in k_values))
```

For j_max=3: k ∈ {1,2,3,4} → 2(4+9+16+25) = 2×54 = **108**

Therefore Gate 4B actual matrix dimension:
- s1=16:  N = 108 × 16  = 1728
- s1=32:  N = 108 × 32  = 3456
- s1=64:  N = 108 × 64  = 6912
- s1=128: N = 108 × 128 = **13824**  (NOT 896)

### [VERIFIED-run] Negative controls used identical dimension

This session's negative-controls batches recorded N=13824 at s1=128 (108×s1).
Gate 4B and negative controls are therefore **dimension-matched** — the
specificity comparison (C1/C2) is valid.

### [VERIFIED-tool] Current code dimension (post-merge)

The v0.1.24 fix (commits 093573b, 13e7861, "restore S3 Dirac k=0 negative branch")
added a k=0 term: `s3_dimension = 2 + sum_{k=1}^{j_max+1} 2(k+1)²`
→ s3_dimension(3) = **110**. Current build_s3_s1_product_operator: N=110×s1.

Difference from Gate 4B (108 vs 110): +2 dimensions, negligible (<2%).

### [DISMISSED] Initial runtime-based hypothesis (N≈75×s1)

A first reconstruction from runtimes (Gate 4B 182s vs neg-controls 535s at s1=128)
suggested N≈75×s1. This was WRONG: it assumed equal hardware. Gate 4B ran on a
faster machine (Hetzner CX52). Direct git evidence (108×s1) supersedes the
runtime inference. Lesson: cross-machine runtime ≠ valid dimension proxy.

---

## 3. Root Cause

The number "896 = 7×s1" comes from `(2·j_max+1)` — the dimension of a **single**
S³ angular-momentum shell. But the operator sums **all** shells k=1..j_max+1
(dimension 108). The report author labeled N with the single-shell formula while
the code correctly built the full multi-shell operator.

**This is a labeling error in documentation, NOT a computation error in code.**

---

## 4. Impact Assessment

| Item | Affected? | Severity |
|------|-----------|----------|
| Gate 4B scientific verdict (7.07× contrast, SIGNAL_PRESERVED) | NO | — |
| Negative controls verdict (DISCRETIZATION_SENSITIVE) | NO | dimension-matched |
| C1/C2 comparisons | NO | both 108×s1, valid |
| Public "N ≤ 896" label (README, Zenodo, CLAIMS) | YES | wrong by ~15× |
| Gate 5 feasibility (s1=512) | YES | see §6 |

**Scientific conclusions stand.** Only the reported lattice size is wrong.

---

## 5. Correction Required

Replace "N ≤ 896" with the true operator dimension across **forward-facing** docs:

> Corrected: "Finite-lattice, S³ Hilbert dimension 108 per S¹ site (full SU(2)
> shell sum k=1..4 for j_max=3); largest operator N = 108 × 128 = 13824."

**Do NOT edit frozen documents** (v0.1.21 results, v0.1.16 papers, pre-registrations) —
immutability rule. This audit is the erratum that supersedes the "896" label in those.

Forward-facing docs to fix:
- `docs/CLAIMS_AND_CAVEATS.md`
- `README.md`
- `.zenodo.json`
- `docs/ROADMAP.md` (if it cites 896)

---

## 6. Gate 5 Feasibility Re-Assessment

At s3_dim=110, full diagonalization (`eigh`, O(N³), dense complex128):

| s1 | N = 110×s1 | Matrix RAM | eigh peak RAM | Feasible? |
|----|-----------|-----------|---------------|-----------|
| 128 | 14080 | 3.2 GB | ~13 GB | ✅ (done) |
| 192 | 21120 | 7.1 GB | ~28 GB | ⚠️ borderline 32GB server |
| 256 | 28160 | 12.7 GB | ~50 GB | ❌ OOM on 32GB |
| 512 | 56320 | 50.7 GB | ~200 GB | ❌ infeasible |

**Pre-registered Gate 5 grid (s1=256, 512 with claimed N=1792, 3584) is INVALID.**
The N=1792/3584 figures used the wrong 7×s1 formula.

**Corrected Gate 5 options:**
- (a) Cap at s1=192 (N=21120) — borderline, needs 64GB server
- (b) Use sparse/iterative eigensolver (ARPACK `eigsh`) for bottom-k eigenvalues
      with eigenvectors — O(N·k²) instead of O(N³), enables s1≥256
- (c) Reduce j_max to 2 (s3_dim=60) → s1=512 gives N=30720, still large

**Recommendation:** Rewrite Gate 5 with option (b) sparse solver OR cap at s1=192.

---

## 7. Verdict

```
DIMENSION_LABEL_ERROR_CONFIRMED — SCIENCE_INTACT
```

- Reported N=896 is wrong; true N=13824 at s1=128 (108×s1).
- Gate 4B and negative controls were dimension-matched → all comparisons valid.
- Forward-facing docs require N correction before any external release.
- Gate 5 grid requires feasibility rewrite (s1=512 is OOM-infeasible).

---

**Status:** FINAL
**Next:** (1) fix N label in forward docs, (2) rewrite Gate 5 grid
**Date:** 2026-06-03
