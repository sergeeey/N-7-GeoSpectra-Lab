# BG-H1 — Pre-registered Claim: S³×S¹ Kaluza-Klein Gap Bridge

**Experiment ID:** 20260610-bg-h1-s3xs1-bridge
**Date pre-registered:** 2026-06-10 (design only — implementation NOT started)
**Question type:** [x] descriptive  [ ] predictive  [ ] causal
**Status:** research_only — no physical promotion
**Track:** GEOMETRY bridge (separate from AV-2 angular track; AV-2 is COMPLETE)

---

## Central Estimand

*Does the spectral fingerprint E0 ≈ 3/2 of the Dirac operator on S³ extend to the
product geometry S³×S¹ according to the standard Kaluza-Klein quadrature formula,
and does the gap shift δ(R) follow the pre-registered closed form?*

- **Population:** Eigenvalues of the Dirac operator on S³(radius 1) × S¹(radius R),
  levels n ≤ 6, KK modes |m| ≤ 4, R ∈ [0.5, 8].
- **Intervention:** None — descriptive spectral measurement.
- **Comparator:** Pure S³ spectrum λ = ±(n + 3/2) (verified in v0.2.0, E0 gate).
- **Endpoint:** (a) eigenvalue quadrature residual; (b) gap shift δ(R) vs closed form.
- **Summary measure:** max relative error over the tested (n, m, R) grid.
- **MCID:** rel. error < 1e-3 counts as "formula holds"; > 1e-2 counts as "formula broken".

## Pre-registered Hypothesis H-BG1

On S³×S¹ the squared Dirac eigenvalues satisfy the KK quadrature:

```
lambda^2(S3 x S1) = (n + 3/2)^2 + (m / R)^2
```

with n = 0, 1, 2, … (S³ level) and m the S¹ momentum number, whose value set
depends on the spin structure on S¹:

| Spin structure | m values | Lowest |m| | δ(R) prediction |
|---|---|---|---|
| Periodic (Ramond) | m ∈ ℤ | 0 | δ(R) = 0 for all R (gap unshifted) |
| Antiperiodic (Neveu-Schwarz) | m ∈ ℤ + 1/2 | 1/2 | δ(R) = sqrt(9/4 + 1/(4R²)) − 3/2 |

**Primary endpoint (first excited KK level, both structures):**

```
delta_1(R) = sqrt(9/4 + (m_1/R)^2) - 3/2
```

where m_1 = lowest nonzero |m| (= 1 for periodic, = 1/2 for antiperiodic).
For m_1 = 1 this reduces to the headline form `delta(R) = sqrt(9/4 + 1/R^2) - 3/2`.

**Declared fork:** the spin structure on S¹ is NOT chosen by this experiment —
BOTH branches are computed and reported. Choosing one would require physical input
we do not have (and would violate the no-physical-promotion constraint).

## Known Risk — Highest Hallucination-Risk Step (BLOCKING)

The additivity `lambda² = lambda²_{S³} + lambda²_{S¹}` requires the Dirac operator
on the product to decompose as D = D_{S³} ⊗ 1 + Γ ⊗ D_{S¹} with the cross terms
**anticommuting** (so cross terms vanish in D²). For odd×odd-dimensional products
(3+1 = 4) the spinor bundle structure (2-dim S³ spinors → 4-dim S³×S¹ spinors via
chirality doubling) must be confirmed from a primary source, NOT assumed.

→ **BG-H1-G0 source-trace gate is BLOCKING** (same protocol as AV-2 G0).

## Gates (in order; each gates the next)

| Gate | Check | Kill condition |
|---|---|---|
| BG-H1-G0 | Source trace (FL Step -4): confirm from primary literature (i) the product-Dirac decomposition with anticommuting cross terms, (ii) the spinor doubling 2→4 components, (iii) the m-spectrum per spin structure on S¹ | additivity NOT confirmed by source → KILL: quadrature formula is a hallucination, record in null_results/ |
| BG-H1-G1 | Analytic cross-check: assemble D² from verified C-H S³ blocks + Fourier S¹ blocks symbolically/numerically on small basis; verify quadrature to near machine precision | rel. error > 1e-6 on exact basis → structure wrong, STOP |
| BG-H1-E1 (PRIMARY) | Discrete proxy: extend the v0.2.0 discrete Dirac to S³×S¹ grid; measure E0(R) for R ∈ [0.5, 8]; fit δ(R) against closed form for both spin structures | rel. error > 1e-2 after grid-convergence check → formula broken on lattice, record mechanism |
| BG-H1-E2 | Robustness: disorder W=0.5 (KT-3 analog) — does δ(R) shape survive? | fingerprint destroyed by disorder only on product (not on S³) → bridge is fragile, FLAG |

## Verdict Rules (pre-registered)

- G0+G1+E1 pass → status: `S3XS1_KK_BRIDGE_SUPPORTED` (descriptive only).
- E1 passes for one spin structure only → report the fork, NO choice made.
- G0 kill → `null_results/20260610-bg-h1-kk-quadrature.md`, formula declared
  not source-supported, no lattice work done.
- E1 fail after G1 pass → discrete-proxy artifact suspected; G1 analytic result
  stands, lattice limitation documented; status capped at `ANALYTIC_ONLY`.

## What This Will NOT Mean (pre-declared, regardless of outcome)

1. PASS ≠ "the true geometry is S³×S¹" — this is a bridge feasibility check,
   GEOMETRY_AGNOSTIC remains the stance.
2. Nothing about S⁶ / SU(4)/SU(3) sectors or Tom's full S³×S⁶ compactification.
3. No physical promotion: λ_coupling = FREE_COUPLING_PARAMETER, safe_for_runtime = False.
4. No spin-structure selection — both branches reported, none endorsed.
5. NOT a statement about Tom's eq. 49 (that is the AV-2 track, already closed).

## Sensitivity (≥2, pre-registered)

1. Both spin structures (periodic / antiperiodic) — full fork, primary sensitivity.
2. Grid refinement: N_alpha 2000 → 4000 → 8000; N_S1 32 → 64 → 128.
3. R-range edge behavior: R → ∞ must recover pure S³ (δ → 0 like m₁²/(3R²) + O(R⁻⁴));
   small R must show KK dominance (δ ~ m₁/R − 3/2 + …).

## Dependencies

- C-H S³ radial blocks: `tom_s3_spinor_toy/reference_spinor_harmonics.py`,
  `discrete_radial_dirac_proxy.py` (verified in AV-2 G0/G1).
- S¹ Fourier blocks: trivial (e^{imθ}), but spin structure m-set is the G0 item.
- NOT dependent on Tom's reply — this track uses only standard differential geometry.

## Scope Fence

- **Goal:** verify/falsify the KK quadrature + δ(R) closed form, descriptively.
- **Boundary:** S³×S¹ only; no S⁶, no gauge fields, no action functional.
- **Done when:** all 4 gates have verdicts, report written, tests pinned.
- **NOT NOW:** physical interpretation, R-stabilization mechanisms, comparison
  with observed scales — all forbidden without a separate gate.
