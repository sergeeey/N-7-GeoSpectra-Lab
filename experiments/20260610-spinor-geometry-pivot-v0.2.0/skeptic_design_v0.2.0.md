# Skeptic Design — Spinor-Geometry Pivot v0.2.0

**Date:** 2026-06-10
**Protocol:** FL Context Asymmetry (FL-rules §"Skeptic for artifact")
**What skeptic receives:** ONLY the recomposed claim + raw numbers. No session history.
**What skeptic does NOT receive:** success narrative, reasoning chain, design rationale.

---

## Recomposed Claim (give this verbatim to skeptic)

> «On a discretized radial grid (N_α ≥ 100), the Dirac operator eigenvalue spectrum
> on S³ (Hopf coordinates, Camporesi-Higuchi) exhibits geometry-discriminating
> fingerprints: |λ_min| = 1.5, degeneracy pattern 2, 6, 12, 20, ...,
> distinguishable from scalar Laplacian (degeneracy 1, 4, 9, 16, ...)
> at disorder W=0, without invoking R/4 or IPR observables.»

---

## Raw Numbers to Provide to Skeptic (no framing)

```
Numerical verification (2026-06-10, N=200, random W diagonal):
IPR(H+W)      = 0.019652907624
IPR(H+W+1.5I) = 0.019652907624
max |diff|    = 6.939e-18

Analytic fingerprints:
scalar S³ degeneracies: [1, 4, 9, 16, 25]
dirac  S³ degeneracies: [2, 6, 12, 20, 30]
|λ_min|: S²=1.0, S³=1.5, S⁶=3.0 (= d/2)

Source: reference_spinor_harmonics.py (phi_nl_hopf, eigenvalue_s3)
        geometry_s3_hopf.py (volume_measure, weighted_inner_product)
        11 tests pass, 0.82s
```

---

## Skeptic Prompt Template

```
You are a falsification agent. Your job is NOT to confirm but to break.

Given claim:
  [paste RECOMPOSED CLAIM above]

Given raw numbers:
  [paste RAW NUMBERS above]

Given code (key functions):
  phi_nl_hopf(n, l, alpha): cosα^{l+1} · sinα^l · P^{(l+1/2,l+3/2)}_{n-l}(cos 2α)
  eigenvalue_s3(n): return float(n) + 1.5
  volume_measure(alpha): sin(alpha) * cos(alpha)

Task:
  Generate 3 test cases that would FALSIFY this claim.
  Then specify exact commands or calculations to run them.
  Report: CONFIRMED / FALSIFIED / NEEDS-REAL-DATA for each.

Do NOT consider how the design was derived or why. Only: does the claim hold?
```

---

## Pre-Registered Falsification Tests (for skeptic to attempt)

### FT-S1: Degeneracy collapse under coarse grid

**What would falsify:** On a coarse α-grid (N_α = 20), Jacobi polynomial evaluation
produces numerical aliasing that collapses the (n+1)(n+2) degeneracy pattern into
noise — making S³ Dirac spectrum indistinguishable from S² or random.

**Test:** Build radial matrix for φ_{n,l}(α_i) at N_α=20, compute overlaps, check
if degeneracy structure survives.

**Falsification threshold:** degeneracy error > 20% on level 1 (expected 2-fold).

---

### FT-S2: Jacobi polynomial ambiguity at boundary

**What would falsify:** Near α=0 (cosα→1) and α=π/2 (sinα→0), the factor
cosα^{l+1}·sinα^l diverges or underflows for large l, and the NaN-guard in
`unweighted_mode()` silently discards those points — effectively changing the
support of integration and distorting the fingerprint.

**Test:** Evaluate phi_nl_hopf(n=4, l=4, alpha) at alpha values in [0, 0.05]
and [π/2-0.05, π/2]. Check for NaN, inf, or values > 1e10.

**Falsification threshold:** >5% of grid points discarded by NaN-guard.

---

### FT-S3: Spectral ladder does not separate spheres numerically

**What would falsify:** Even though analytic λ_min = d/2 is distinct, the numerical
finite-difference eigenvalue problem on a radial grid gives overlapping spectra for
d=2 and d=3 due to discretization error at realistic N_α.

**Test:** Implement toy 1D radial Dirac operators for S² and S³ (using known
analytic spectra as ground truth), discretize at N_α=100, compare computed
|λ_min| separation vs analytic gap of 0.5 (1.5-1.0).

**Falsification threshold:** |λ_min(S³)_computed - 1.5| > 0.25 at N_α=100.

---

## Escape Hatch Conditions

FT-S1 FAIL → downgrade to N_α ≥ 200 requirement, update estimand MCID.
FT-S2 FAIL → fix NaN-guard in reference_spinor_harmonics.py before any Phase 3.
FT-S3 FAIL → redesign discretization (non-uniform grid, Gauss-Lobatto points).

In all cases: update estimand_v0.2.0.md §7 and record in null_results/ if gate fails.

---

## Execution Status Update — 2026-06-10 (radial proxy)

| Pre-registered test | Status | Outcome |
|---|---|---|
| FT-S1 (degeneracy collapse, coarse grid) | partially executed | FD errors decrease monotonically 1000→4000 (6.9e-6 → 4.3e-7, d=3/6); no collapse. d=2 NOT covered by FD — see new finding. |
| FT-S2 (boundary divergence) | superseded | New, sharper failure mode found instead: see FT-S4. |
| FT-S3 (spheres not separated numerically) | executed | FALSIFICATION FAILED — separation exact to 1.6e-6; kill condition (gap error > 0.25) missed by 5 orders. |

**NEW FALSIFICATION MATERIAL — FT-S4 (discovered, not pre-registered):**
For d=2, lowest sector κ=1/2, the endpoint coefficient κ(κ−1) = −1/4 is the
critical limit-circle value: uniform FD converges only at rate ~h^0.1
(5.7% at N=1000 → 4.1% at N=32000). A naive lattice implementation on even-d
spheres would produce ~5% systematic |λ_min| errors — comparable to the MCID —
potentially faking or masking fingerprints. Resolved at proxy level by shooting
solver (error 6.3e-11). **Skeptic for Phase 3 should attack any even-d lattice
scheme on exactly this point.**

## When to Run Skeptic

**Trigger:** before committing any Phase 3 experiment code (lattice phase —
the radial proxy above does not exhaust the claim).

**Minimum skeptic output required:**
- Verdict on each FT-S1, FT-S2, FT-S3: CONFIRMED / FALSIFIED / NEEDS-REAL-DATA
- If any FALSIFIED: claim = BLOCKED, record in null_results/
- If all CONFIRMED: claim = CLEARED, proceed to controls_v0.2.0.md

---

## What Skeptic Should NOT Receive

- The claim-decomposer session output from 2026-06-10
- The reasoning that led to PIVOT verdict
- The observation that this is a "revised" claim
- Any framing about "low-hanging fruit" or "promising pivot"

The skeptic's value = independent falsification. Agreeableness bias = destroyed if
the skeptic knows the claim has already been internally vetted.
