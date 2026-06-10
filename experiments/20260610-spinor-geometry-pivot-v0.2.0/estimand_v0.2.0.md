# Estimand — Spinor-Geometry Pivot v0.2.0

**Date:** 2026-06-10
**Ladder tier:** Full (research, geometry-discrimination hypothesis)
**Question type:** Descriptive → Predictive (causal interpretation explicitly excluded — see §6)
**Status:** DESIGN LOCKED — pending skeptic gate before any Phase 3 code

---

## Provenance of this revision

The original pivot claim («Dirac-sector makes harness geometry-sensitive via Lichnerowicz
D²=∇*∇+R/4») was decomposed into atoms and the central channel was falsified by
math-code trace:

> On a homogeneous sphere R=const, so R/4 = c·I.  
> H and H+cI share identical eigenvectors.  
> IPR = mean(Σ|ψᵢ|⁴) depends only on eigenvectors.  
> **∴ R/4 alone cannot make IPR geometry-sensitive.** [VERIFIED-tool, 2026-06-10]
>
> Numerical confirmation: IPR(H+W) = IPR(H+W+1.5I) to 1e-18 at N=200, strong disorder.

**Old pivot claim verdict: PIVOT** — not KILL; spectral fingerprints ARE distinguishable
and provide a valid geometry-discrimination channel (see §3).

**Recomposed claim verdict: CONTINUE_WITH_REDESIGNED_ENDPOINTS**

---

## §1 — Population

Finite radial Dirac operator on S³ in Hopf coordinates, discretized on a uniform
α-grid of N_α points, with S¹-disorder strength W ≥ 0. Scalar quantum numbers
(n, l) drawn from Camporesi-Higuchi, n ∈ {1,2,3,4}, l ∈ {0,...,n}.

Comparator spheres (future phases only, not yet implemented):
- S² (d=2): λ_min = ±1.0, degeneracy pattern 2,4,6,8,...
- S³ (d=3): λ_min = ±1.5, degeneracy pattern 2,6,12,20,...
- S⁶ (d=6): λ_min = ±3.0

---

## §2 — Intervention

Replace the scalar Laplacian operator (used in Phases 0–1) with the Dirac operator
D as defined by Camporesi-Higuchi (gr-qc/9505009). Observables computed from
eigenpairs of D.

Comparator: scalar Laplacian baseline (Phases 0–1, v0.1.21 Gate 4B).

---

## §3 — Primary Endpoint: Spectral Fingerprint Separation

**Definition (four components, all required):**

| Observable | Formula | S² value | S³ value | S⁶ value |
|---|---|---|---|---|
| |λ_min| | |λ_min| = d/2 | 1.0 | 1.5 | 3.0 |
| λ-ladder gap | λ_{n+1} − λ_n | 1.0 | 1.0 | 1.0 |
| Degeneracy d_0 | first level | 2 | 2 | 2 |
| Degeneracy d_1 | second level | 4 | 6 | 14 |

**Why this channel is geometry-sensitive [VERIFIED-tool]:**
- Scalar S³ degeneracies: 1, 4, 9, 16, 25 (sequence (l+1)²)
- Dirac S³ degeneracies: 2, 6, 12, 20, 30 (sequence (n+1)(n+2)) 
- |λ_min|: S²→1.0, S³→1.5, S⁶→3.0 (= d/2 exactly)
- These are analytically distinct across all three target spheres.

**Summary measure:** spectral fingerprint match score — fraction of predicted
(λ, degeneracy) pairs recovered within 5% relative tolerance on discretized grid.
Spectral distance between geometries: mean absolute ladder difference,
analytic value = |d_a − d_b| / 2.

**MCID:** match ≥ 90% of top-5 Dirac eigenvalues within 5% tolerance at N_α ≥ 100.

**Degeneracy split (honest accounting):** sector membership (λ_n appears in
sectors l = 0..n) is the NUMERICAL content; angular factors 2(l+1) per sector
are ANALYTIC-INPUT. Full degeneracy (n+1)(n+2) is a reconstruction, not a
direct measurement.

**Implementation:** `tom_s3_spinor_toy/spectral_fingerprint_proxy.py` +
`tests/test_spectral_fingerprint_proxy.py` (17 tests).
**Result 2026-06-10:** gates C9a/C9b/C9c PASSED at radial-proxy level —
see `proxy_results_v0.2.0.md`. Errors 5–11 orders below MCID.

---

## §4 — Secondary (Exploratory) Endpoint: IPR Spin-Connection Channel

**Status:** EXPLORATORY — results cannot confirm or refute primary endpoint.

IPR may capture geometry effects through the spin connection Γ in ∇*∇ (the non-scalar
part), not through R/4. This hypothesis is:
- **Not refuted** (spin-connection channel not yet tested)
- **Not confirmed** (no data; R/4-channel explicitly falsified)
- **Not a blocker** for Phase 3 design

**Operationalization:** true_ipr_mean = mean(Σ|ψᵢ|⁴) for bottom 10% eigenstates,
same formula as Gate 4B v0.1.21.

**If IPR shows geometry-sensitivity in Phase 3 data:** record as new finding, run
skeptic separately, do not conflate with primary endpoint verdict.

---

## §5 — Intercurrent Events

| ICE | Strategy |
|---|---|
| Discretization wipes out spectral fingerprint (C9) | Hypothetical — record as FALSIFIED, do not add disorder |
| λ degeneracies split under disorder before geometry is read | Composite — record as a finding, not a failure |
| Numerical instability near α=0 or α=π/2 | Composite — NaN-guard exists in reference_spinor_harmonics.py:77 |
| **Critical limit-circle endpoint for half-integer κ (d even, l=0)** | **Composite — OCCURRED for d=2: κ(κ−1)=−1/4, FD converges ~h^0.1; resolved by shooting solver with indicial asymptotics [VERIFIED-tool 2026-06-10]. Any even-d lattice scheme must be boundary-adapted.** |

---

## §6 — What This Estimand Does NOT Mean

1. Does NOT claim gauge group emergence from spectral fingerprints.
2. Does NOT claim Tom Lawrence's framework is correct or testable here.
3. Does NOT claim spectral separation on a continuous S³ implies separation after
   S³×S¹ lattice discretization (this is C9, tested separately).
4. Does NOT claim IPR is geometry-sensitive (falsified for R/4 channel; spin-connection
   channel is exploratory only).
5. Does NOT promote any observable to production status (runtime=research_only).

---

## §7 — Mandatory Gate C9: Discretization Survival

**Before any Phase 3 result is interpreted:**

Gate question: Do predicted Dirac eigenvalues {λ_n = n + 3/2} survive on a uniform
α-grid with N_α points?

Gate pass criterion: max|λ_computed − λ_analytic| / λ_analytic < 5% for n ∈ {1,2,3,4}
at N_α = 100.

Gate fail action: record in null_results/, redesign discretization, do NOT proceed
to disorder-phase experiments.

**Implementation:** ~50 lines using existing phi_nl_hopf() and geometry_s3_hopf.py —
no new physics required.

---

## §8 — Sensitivity Analyses (≥2 required for Full-Ladder)

SA-1: Alternative discretization (N_α = 50 vs 200) — does fingerprint quality
      degrade gracefully or collapse discontinuously?

SA-2: Alternative degeneracy observable — replace count-based match with
      spectral entropy H = -Σ p_i log p_i over level-spacing distribution.
      If entropy distinguishes d while count-match fails → refine primary observable.

---

## §9 — Natural Language Statement

*"We estimate the fraction of analytically-predicted Dirac eigenvalue-degeneracy pairs
(|λ_min|, λ-ladder, degeneracy pattern) that are numerically recovered on a discretized
S³ radial grid (N_α ≥ 100), at disorder W=0, comparing Dirac vs scalar Laplacian operators,
handling discretization artifacts by the hypothetical ICE strategy."*

Written before any Phase 3 computation. 2026-06-10.

---

## §10 — Revision History

| Version | Date | Change |
|---|---|---|
| v0.1 (original pivot) | 2026-06-03 | IPR as primary endpoint; Lichnerowicz R/4 as geometry channel |
| **v0.2.0 (this doc)** | **2026-06-10** | **Spectral fingerprint as primary; IPR → exploratory; C9 gate added; R/4 falsification recorded** |

**Next step before any code:** skeptic gate on RECOMPOSED_CLAIM (context-asymmetric).
See `skeptic_design_v0.2.0.md`.
