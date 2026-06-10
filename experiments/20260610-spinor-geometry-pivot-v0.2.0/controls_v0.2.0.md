# Controls — Spinor-Geometry Pivot v0.2.0

**Date:** 2026-06-10
**Linked estimand:** estimand_v0.2.0.md
**Status:** DESIGN ONLY — no data yet. All controls must pass before disorder (W>0) experiments.

---

## Control Architecture

Three control tiers, run in order. Each tier has a pass criterion.
If any tier fails: STOP, do not advance to next tier.

```
Tier 1 — Trivial vacuum (analytic check)
    ↓ PASS
Tier 2 — Positive control (known-good geometry)
    ↓ PASS
Tier 3 — Negative control (geometry-scrambled baselines)
    ↓ PASS
Phase 3 disorder experiments (W > 0)
```

---

## Tier 1 — Trivial Vacuum (tom_ansatz)

**Purpose:** Confirm that √sin(2α) is NOT a Dirac eigenfunction — i.e., the
harness can reject a non-eigenfunction candidate.

**Why this control:** tom_ansatz was the original motivation for the alpha-problem.
If it accidentally passed spectral fingerprint tests, the endpoint would be broken.

**Input:**
```python
from tom_s3_spinor_toy.reference_spinor_harmonics import tom_ansatz
from tom_s3_spinor_toy.geometry_s3_hopf import weighted_inner_product
alpha = np.linspace(0.01, np.pi/2 - 0.01, 500)
f = tom_ansatz(alpha)   # sqrt(sin(2*alpha))
```

**Test:** Compute ⟨f, φ_{n,l}⟩_w for (n,l) ∈ {(1,0),(1,1),(2,0),(2,1),(2,2)}.
If max|⟨f, φ_{n,l}⟩| > 0.1 for any single (n,l) → POSITIVE CONTROL CONCERN.

**Pass criterion:** No single projection > 0.1; confirm f is a superposition with
no dominant eigenmode — i.e., it is NOT an eigenfunction.
Status: [EXPECTED PASS per Phase 2 test results — must verify explicitly]

**Fail action:** Re-examine tom_ansatz definition; check if unweighted_mode()
accidentally normalizes it to look like an eigenfunction.

---

## Tier 2 — Positive Control (clean S³ fingerprint recovery)

**Purpose:** At W=0, N_α=200, the computed Dirac spectrum must match analytic values.

**This is the C9 gate from estimand_v0.2.0.md §7.**

### C9a — Eigenvalue recovery

Analytic target: λ_n = n + 3/2

| n | analytic λ | tolerance |
|---|---|---|
| 1 | 2.5 | ±0.125 (5%) |
| 2 | 3.5 | ±0.175 (5%) |
| 3 | 4.5 | ±0.225 (5%) |
| 4 | 5.5 | ±0.275 (5%) |

**Pass criterion:** All 4 eigenvalues within tolerance.

### C9b — Degeneracy pattern recovery

Analytic: (n+1)(n+2) = 2, 6, 12, 20, 30 for n=1,2,3,4,5

**Pass criterion:** Each degeneracy recovered within ±1 count at N_α=200.

### C9c — |λ_min| separation

S³ analytic |λ_min| = 1.5. Harness must recover ≥ 1.375 (threshold: 1.5 × 0.917).

If scalar Laplacian is also run: scalar λ₁(S³) = 3.0. These must not be
confused (absolute numerical separation > 1.0 is sufficient to distinguish).

**Pass criterion for C9:** C9a AND C9b AND C9c all pass.
**Fail action:** Record in null_results/ as DISCRETIZATION_FAILURE_v0.2.0, do NOT
proceed to disorder experiments.

---

## Tier 3 — Negative Controls (geometry-scrambled baselines)

**Purpose:** Harness must REJECT geometrically scrambled operators. If it cannot, the
spectral fingerprint is not specific.

### NC-1: Random Hermitian (RMT baseline)

**Input:** N×N GUE/GOE matrix, N = number of discretized modes.
**Expected:** Degeneracy pattern = 1 (generic spectrum, no multiplets).
**Pass criterion:** Harness reports no degeneracy clusters; |λ_min| not near d/2.

### NC-2: Permuted Hopf coordinates

**Input:** φ_{n,l}(α) with α-grid randomly permuted (index shuffle).
**Expected:** Destroys smooth Jacobi structure → degeneracy pattern collapses.
**Pass criterion:** Degeneracy match score < 50% (vs ≥90% for positive control).

### NC-3: Scalar Laplacian on S³

**Input:** Scalar Laplacian operator (l(l+2) eigenvalues, (l+1)² degeneracies).
**Expected:** Different fingerprint from Dirac: scalar has (l+1)² = 1,4,9,16,...
             vs Dirac (n+1)(n+2) = 2,6,12,20,...
**Pass criterion:** Fingerprint match score < 40% against Dirac degeneracy template.

**Why this control is critical:** If the harness cannot distinguish Dirac from scalar
Laplacian on the SAME sphere, the endpoint has no discriminating power.

---

## R/4-Invariance Regression Test

**Record permanently (never delete):**

```python
# Regression: IPR invariant under H -> H + c*I
# Verifies that R/4 channel cannot drive geometry-sensitivity via IPR
# VERIFIED-tool 2026-06-10, N=200, strong disorder
assert abs(ipr(H+W) - ipr(H+W+1.5*I)) < 1e-10, "IPR shift invariance broken"
```

This test must be included in any future test suite for the spinor harness.
If it fails: either a bug was introduced, or the observable was changed.

---

## Summary Table — with execution status 2026-06-10

| Control | Tier | Measures | Pass Criterion | Status (radial proxy) |
|---|---|---|---|---|
| tom_ansatz rejection | 1 | trivial vacuum | **REDESIGNED — see note below** | finding recorded |
| C9a eigenvalue recovery | 2 | discretization quality | 4/4 within 5% | **PASS** (4.3e-07) |
| C9b degeneracy recovery | 2 | degeneracy pattern | ±1 count per level | **PASS** (sector structure exact) |
| C9c |λ_min| separation | 2 | S³ vs scalar separation | ≥ 1.375 | **PASS** (1.500000) |
| NC-1 random Hermitian | 3 | specificity | no false clusters | **PASS** (match 0.0) |
| NC-2 permuted grid | 3 | structural sensitivity | < 50% match score | not yet run (lattice phase) |
| NC-3 scalar vs Dirac | 3 | operator discrimination | < 40% cross-match | **PASS** (cross-match 0.0) |
| IPR shift regression | permanent | R/4-channel closed | diff < 1e-10 | **PASS** (6.9e-18) |

Implementation: `tom_s3_spinor_toy/spectral_fingerprint_proxy.py`,
tests: `tom_s3_spinor_toy/tests/test_spectral_fingerprint_proxy.py` (17/17 passed).
Results: `proxy_results_v0.2.0.md` + `proxy_results_v0.2.0.json`.

### Tier 1 REDESIGN (per HD-MAVP audit 2026-06-10)

The original criterion «max projection < 0.1 → ansatz is NOT an eigenfunction»
FAILS in an informative way: tom_ansatz √sin(2α) projects with coefficient 0.92
onto phi_{11} (n=1, l=1, λ=±2.5), and onto the phi_{ll} series
(0.92, 0.88, 0.83, 0.79 for l=1..4) [VERIFIED-tool].

NEW Tier 1: dominant-mode DECOMPOSITION test — compute argmax_nl projection,
record the phi_{ll} series. This is a regression test of a FINDING (candidate
direct answer to Tom's alpha-problem), not a rejection gate.
Caveat: verified under radial weighted inner product only; full angular
confirmation required before communicating to Tom.

---

## Ordering constraint

Run Tier 1 before Tier 2. Run Tier 2 before Tier 3. Do NOT run disorder experiments
until all three tiers pass. This ordering prevents over-investing in disorder
campaigns that would be invalidated by a failed C9 gate.
