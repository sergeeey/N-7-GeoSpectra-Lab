# Spectral-Fingerprint Proxy — Results v0.2.0

**Date:** 2026-06-10
**Code:** `tom_s3_spinor_toy/spectral_fingerprint_proxy.py`
**Tests:** `tom_s3_spinor_toy/tests/test_spectral_fingerprint_proxy.py` — **17/17 passed, 17.8s**
**Raw data:** `proxy_results_v0.2.0.json`
**Status:** research_only — no physical promotion, no gauge-group claim

---

## Verdict

**KT-1 (eigenvalue recovery): PASSED.**
**KT-2 (cross-sphere discrimination): PASSED at radial-proxy level.**
**Gates C9a / C9b / C9c (radial-proxy versions): PASSED.**

The Dirac/spinor radial sector numerically distinguishes S², S³, S⁶ through
spectral fingerprints, with errors 5–11 orders of magnitude below the 5% MCID.
IPR was not used as a primary observable anywhere; NC-A confirms the R/4→IPR
channel is closed (gap 6.9e-18).

---

## Method (one paragraph)

The squared Dirac operator on S^d reduces, in geodesic polar angle θ and flat
measure, to H = −d²/dθ² + κ(κ+cosθ)/sin²θ with κ = l + (d−1)/2 per angular
sector. The operator construction (superpotential W = κ/sinθ) and the analytic
targets λ = n + d/2 (Camporesi-Higuchi, VERIFIED_FROM_PDF) are independent
inputs: a match across three dimensions and 4–5 levels with zero fitted
parameters cannot be coincidental. Discretization: tridiagonal finite
differences (`eigh_tridiagonal`); for the critical case d=2 (κ=1/2), a
two-sided shooting solver with indicial asymptotics.

---

## Primary Endpoint Results

### |λ_min| = d/2 fingerprint [VERIFIED-REAL: computed from discretized operator]

| Sphere | computed | analytic | rel. error | solver |
|---|---|---|---|---|
| S² | 1.000000 | 1.0 | 6.3e-11 | shooting |
| S³ | 1.500000 | 1.5 | 4.3e-07 | FD N=4000 |
| S⁶ | 3.000000 | 3.0 | 4.3e-07 | FD N=4000 |

### Eigenvalue ladder (max rel. error over 4 levels)

| Sphere | ladder (computed) | max rel. err |
|---|---|---|
| S² | 1, 2, 3, 4 | 6.3e-11 |
| S³ | 1.5, 2.5, 3.5, 4.5 | 4.3e-07 |
| S⁶ | 3, 4, 5, 6 | 4.3e-07 |

### Spectral distance (analytic = |d_a − d_b|/2)

| Pair | computed | analytic | rel. err |
|---|---|---|---|
| S²–S³ | 0.499999 | 0.5 | 1.6e-06 |
| S²–S⁶ | 1.999999 | 2.0 | 5.3e-07 |
| S³–S⁶ | 1.500000 | 1.5 | 1.9e-07 |

All pairwise |λ_min| separations > 0.4 ≫ numerical error → three spheres
mutually distinguishable. KT-2 kill condition (gap error > 0.25) — not triggered
by 5 orders of magnitude.

### Degeneracy pattern — honest split

Numerically verified: λ_n = n + 3/2 appears in **exactly** sectors l = 0..n
(sector membership, FD per sector). With analytic angular factors 2(l+1)
[ANALYTIC-INPUT, S² Dirac degeneracy] this reconstructs:

| n | sectors found | D₃ reconstructed | D₃ analytic (CH 3.58) |
|---|---|---|---|
| 0 | {0} | 2 | 2 |
| 1 | {0,1} | 6 | 6 |
| 2 | {0,1,2} | 12 | 12 |

Dirac [2,6,12,...] ≠ scalar [(l+1)² = 1,4,9,...] at every level.

---

## Negative Controls

| Control | Result | Pass criterion | Verdict |
|---|---|---|---|
| NC-A: IPR(H+W) vs IPR(H+W+1.5I) | gap = 6.9e-18 | < 1e-12 | **PASS** — R/4→IPR channel closed |
| NC-B: GOE random Hermitian vs Dirac ladder | match = 0.0 | ≤ 0.25 | **PASS** — no false fingerprint |
| NC-C: scalar vs Dirac on same S³ | cross-match = 0.0 | ≤ 0.34 | **PASS** — operator structure detected |

**Honest framing of NC-C:** the scalar SPECTRUM is itself geometry-sensitive
(λ₁ = d); what was geometry-agnostic in v0.1.22 was the vector/IPR channel on
lattice products. NC-C shows the fingerprint distinguishes OPERATORS on a fixed
sphere — it does not retroactively explain the v0.1.22 verdict.

---

## Discretization Survival (gate C9 / SA-1)

FD error vs grid (d=3 and d=6 identical to 3 digits):

| N_grid | max rel. err |
|---|---|
| 1000 | 6.9e-06 |
| 2000 | 1.7e-06 |
| 4000 | 4.3e-07 |

Clean ~h² convergence; MCID (5%) beaten by 5 orders of magnitude.

**EXCEPTION — d=2 critical case [VERIFIED-tool]:** the lowest sector κ = 1/2
has endpoint coefficient κ(κ−1) = −1/4 — the limit-circle value. Uniform FD
converges only logarithmically: 5.7% error at N=1000 → 4.1% at N=32000
(rate ≈ h^0.1). The shooting solver with correct indicial exponents
(u ~ θ^{κ+1} at 0, u ~ (π−θ)^κ at π) resolves it to 6.3e-11. A regression test
(`test_d2_fd_limitation_is_real`) pins this failure so it cannot silently
disappear from documentation.

**Implication for Phase 3:** any lattice Dirac implementation on even-d spheres
must handle half-integer-κ sectors with boundary-adapted methods; naive uniform
grids will produce ~5% systematic errors that could mask or fake fingerprints
near the MCID threshold.

---

## What These Results Do NOT Mean

1. NOT a lattice result: this is a continuum radial ODE discretization, not the
   S³×S¹ product-lattice harness. HA-4 scope gap remains open.
2. NOT a disorder result: W > 0 untested (KT-3 pending). The fingerprint is
   established only in the clean limit.
3. NOT a full-degeneracy measurement: angular factors are analytic inputs.
4. NOT a resolution of the v0.1.22 GEOMETRY_AGNOSTIC verdict — different question.
5. NOT a statement about λ coupling (FREE_COUPLING_PARAMETER, untouched) or
   gauge-group emergence.

---

## Next Steps (per decision_record_v0.2.0.md)

- **E4 / KT-3:** add weak disorder W=0.1 to the radial operator, test fingerprint
  survival (|λ_min| shift < gap/2 = 0.25).
- **E6 / HA-4:** design decision — relationship between pure-sphere
  discrimination and the original S³×S¹ question.
- d=2 boundary-adapted lattice scheme — required before any even-d lattice work.
