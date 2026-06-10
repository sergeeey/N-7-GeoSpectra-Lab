# NC-2 — Permuted Grid Negative Control

**Experiment:** NC2_PERMUTED_GRID_NEGATIVE_CONTROL  
**Tier:** 3 (Tier-3 negative control — last in the Tier sequence)  
**Date:** 2026-06-10  
**Code:** `tom_s3_spinor_toy/nc2_permuted_grid.py`  
**Tests:** `tom_s3_spinor_toy/tests/test_nc2_permuted_grid.py` — **14/14 passed, 0.39s**  
**Raw data:** `nc2_permuted_grid_results.json`  
**Status:** research_only — no physical promotion

---

## Verdict

```
NC-2 GATE: PASS
Overall: NC2_PASS  (S³ PASS, S⁶ PASS)

S³: min deviation = 270%, max deviation = 458%  (threshold: > 50%)
S⁶: min deviation = 320%, max deviation = 410%

Fingerprint completely destroyed in ALL seeds.
Margin above threshold: ~5× (270% vs 50%).
```

**Interpretation:** The spectral fingerprint |λ_min| = d/2 is a GENUINE GEOMETRIC
property of the smooth Hopf coordinate structure. It is not an artifact of the
tridiagonal matrix topology. When the geometric ordering of the potential is
destroyed, the fingerprint collapses by 270-460%, not by a small perturbation.

---

## Setup

**Permutation:** Keep kinetic (off-diagonal = −1/(4h²)) fixed; permute only the
potential values V(α_i) → V(α_{perm(i)}).  This destroys the smooth SUSY
quantum-well while preserving the graph (tridiagonal) structure.

**Why this matters:** If |λ_min| = d/2 survived permutation, the fingerprint
would be a property of the tridiagonal graph (any N-point chain), not of S^d.
The test confirms that geometric ordering is essential.

---

## Results

### S³ (primary, d=3, analytic |λ_min| = 1.5)

| Seed | |λ_min|_perm | deviation |
|---|---|---|
| 0 | 8.36 | 458% |
| 1 | 5.54 | 270% |
| 2 | 6.93 | 362% |
| 3 | 8.08 | 438% |
| 4 | 5.94 | 296% |

min deviation = 270%, max = 458%, threshold = 50%.  **ALL SEEDS: fingerprint destroyed.**

### S⁶ (secondary, d=6, analytic |λ_min| = 3.0)

| Seed | |λ_min|_perm | deviation |
|---|---|---|
| 0 | 15.30 | 410% |
| 1 | 12.67 | 322% |
| 2 | 12.60 | 320% |
| 3 | 13.99 | 366% |
| 4 | 14.98 | 399% |

min deviation = 320%, max = 410%. **ALL SEEDS: fingerprint destroyed.**

---

## Physical Mechanism

The Dirac² operator V(α) = κ(κ + χ·cos 2α)/sin² 2α is a **SUSY quantum-well
potential** whose smooth ordering is essential to produce the eigenvalue ladder
λ_n = n + d/2.  The smooth Jacobi polynomial eigenfunctions u_n(α) are adapted
to this ordered potential landscape.

After random permutation:
1. The quantum well (minimum of V at α = π/4) is displaced to a random position
2. The wavefunction can no longer follow the smooth analytic profile
3. The kinetic energy cost increases dramatically (wavefunction confined to the
   minimum-V site cannot spread smoothly)
4. Result: |λ_min|_perm ≈ 4–8× the analytic value, not 1.5

This ~300% increase quantifies the geometric sensitivity:
**the fingerprint requires ordered geometry, not just tridiagonal connectivity.**

---

## Tier-3 Complete

NC-2 is the last pending Tier-3 control. Status of all Tier-3 controls:

| Control | Status |
|---|---|
| NC-1: Random Hermitian (RMT baseline) | **PASS** (spectral_fingerprint_proxy.py) |
| NC-2: Permuted Hopf coordinates | **PASS** (this report, 2026-06-10) |
| NC-3: Scalar Laplacian vs Dirac | **PASS** (spectral_fingerprint_proxy.py) |

**All Tier-1, Tier-2, Tier-3 controls complete.  Phase 3 entry condition (NC-2)
is now satisfied.**

---

## What NC-2 Does NOT Establish

1. **Nothing about the S³×S¹ product geometry** (HA-4 OPEN, see ha4_design_decision.md)
2. **Nothing about off-diagonal permutations** — only diagonal (potential) was permuted;
   off-diagonal permutation (hopping topology) is a different experiment
3. **Nothing about small perturbations** — this tests a global random permutation,
   not a local geometric deformation

---

## Next Steps

With NC-2 complete, the Phase 3 entry condition is now fully met:

```
Phase 3 entry checklist:
  ✓  E0 gate PASS          (discrete eigenvalue + eigenvector recovery)
  ✓  KT-3 gate PASS        (fingerprint survives W = 0.1 disorder, margin 335×)
  ✓  HA-4 gate DECIDED     (ONE_TRACK_WITH_EXPLICIT_BRIDGE_GATE)
  ✓  NC-2 PASS             (fingerprint is geometric, not matrix artifact)
  
Phase 3 first task (from ha4_design_decision.md):
  BG-1: Build S³×S¹ Dirac lattice (product geometry, Hopf × circle)
  BG-2: Verify KK tower structure under BCs
  BG-3: Test S¹-direction disorder (hopping disorder)
```
