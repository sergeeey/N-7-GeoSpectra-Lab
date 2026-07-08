# Phase 4E v2b Report: Additive Disorder on Analytic Eigenvalues

**Date:** 2026-07-08
**Status:** v2b COMPLETE — concept validated, limitations documented
**Evidence:** [ANALYTIC-SPECTRUM] [ADDITIVE-DISORDER] [REPRODUCED] [PARTIAL]

---

## What Changed from MVP

| | MVP v1 | v2b |
|---|---|---|
| Disorder | Multiplicative: λ→λ×(1+Wu) | **Additive: λ→λ+V** |
| Effect | Conformal (rescales) | **Non-conformal (shifts)** |
| Geometry discrimination | None | **None under disorder** |
| Clean spectra | Heat zeta differs | **Heat zeta differs** |

---

## Key Result: Heat Zeta Discriminates Clean Spectra

| Geometry | ζ(t=0.1) | ζ(t=0.5) | Rank |
|----------|----------|----------|------|
| **S³×S⁶ (physical, κ=√(7/6))** | **302.1** | 0.2 | 🥇 Densest |
| S⁴×S⁵ | 252.3 | 0.2 | 🥈 |
| S³×S⁶ (equal R) | 221.4 | 0.1 | 🥉 |
| S²×S⁷ | 166.1 | 0.0 | 4th |

**Physical interpretation:** κ=√(7/6) ≈ 1.08 compresses S³ relative to S⁶, increasing low-lying eigenvalue density → higher heat zeta at small t.

---

## Disorder Behavior

All geometries: **RECOVERABLE** even at W=20.

**Why:** Additive noise of size ~mean_spacing to dense spectrum produces small relative perturbation. Heat zeta ratios:
- ζ(0.1): 1.000 (unchanged, short times suppress noise)
- ζ(1.0): 1.017–1.022 (small change at longer times)

---

## Limitations

1. **No geometry discrimination under disorder** — all identical behavior
2. **Additive disorder doesn't capture Anderson localization** (mode mixing)
3. **Importance sampling** introduces variance in spacing metrics

---

## Path to v3: True Anderson on Kronecker Matrix

Required for geometry discrimination under disorder:
1. Sparse Kronecker Laplacian: `L = Lₐ ⊗ I + I ⊗ Lᵦ`
2. On-site potential: `H = L + diag(Vᵢ)`, `Vᵢ ~ Uniform(-W, W)`
3. Sparse re-diagonalization via `eigsh` with proper shift
4. Compare heat zeta decay curves

**Challenge:** Spatial discretization of S⁶ Laplacian without catastrophic null space.

---

## Files

| File | Description |
|------|-------------|
| `phase4e_v2b_additive_eigenvalues.py` | Main script |
| `phase4e_v2b_results.json` | Results |
| `PHASE4E_V2B_REPORT.md` | This report |

---

## Conclusion

Phase 4E v2b validates **heat zeta as geometry discriminator** in clean spectra. Physical geometry S³×S⁶(κ) has highest low-t heat zeta among all 9D products tested.

Full disorder discrimination requires v3 with matrix Laplacian + true Anderson localization.

---

*Evidence: [ANALYTIC-SPECTRUM] [ADDITIVE-DISORDER] [REPRODUCED] [PARTIAL]*
