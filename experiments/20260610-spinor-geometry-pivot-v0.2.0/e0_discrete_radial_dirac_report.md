# E0 — Discrete Radial Dirac Eigenvalue Recovery

**Experiment:** E0_DISCRETE_RADIAL_DIRAC_EIGENVALUE_RECOVERY
**Date:** 2026-06-10
**Code:** `tom_s3_spinor_toy/discrete_radial_dirac_proxy.py`
**Tests:** `tom_s3_spinor_toy/tests/test_discrete_radial_dirac_proxy.py` — **16/16 passed, 0.65s**
**Raw data:** `e0_discrete_radial_dirac_results.json`
**Status:** research_only — no physical promotion

---

## Verdict

```
KILL-TEST (pre-registered): max rel. error > 5% → REDESIGN_DISCRETIZATION
RESULT:                     max rel. error = 6.7e-07 → PASS
                            (margin: ~75 000× below threshold)
```

**E0 gate: PASSED.** The discrete radial Dirac² operator on the Hopf α-grid
recovers the analytic eigenvalue ladder λ_n = n + d/2 AND reproduces the
verified Phase 2 eigenfunctions to 10 decimal places. Per decision record:
E2 controls and the YELLOW path (E3/E4/E5) are now unblocked.

---

## Operator

Flat-measure radial Dirac² on the Hopf grid α ∈ (0, π/2), per angular sector
κ = l + (d−1)/2, two chirality blocks χ = ±1:

```
H_χ u = -(1/4) u'' + κ(κ + χ·cos 2α)/sin² 2α · u = λ² u
```

Discretization: tridiagonal finite differences, Dirichlet BCs, N = 4000
(`eigh_tridiagonal`). The operator (superpotential structure) and the targets
(Camporesi-Higuchi λ = n + d/2, VERIFIED_FROM_PDF) are independent inputs —
agreement is evidence, not construction.

---

## S³ Results (primary — run first)

### Eigenvalue ladder, sector l = 0, N = 4000

| n | computed | analytic n + 3/2 | rel. error |
|---|---|---|---|
| 0 | 1.500000 | 1.5 | < 1e-7 |
| 1 | 2.500000 | 2.5 | < 1e-7 |
| 2 | 3.499999 | 3.5 | ~2e-7 |
| 3 | 4.499998 | 4.5 | ~4e-7 |
| 4 | 5.499996 | 5.5 | ~7e-7 |

max rel. error = **6.65e-07** (threshold 5e-02). Sector l = 1 starts at 2.5
(n ≥ l structure) — verified.

### Eigenvector correspondence with verified Phase 2 reference [new in E0]

| Block | Analytic counterpart | cosine similarity (n = 0, 1, 2) |
|---|---|---|
| χ = −1 | sin(2α) · `phi_nl_hopf` (CH eq 3.25, VERIFIED_FROM_PDF) | 1.0000000000, 1.0000000000, 1.0000000000 |
| χ = +1 | sin(2α) · `g_nl_hopf` (partner, α-mirror of 3.25) | 1.0000000000, 1.0000000000, 1.0000000000 |

Both chirality blocks are isospectral (λ = n + 3/2), as required by the
spectral symmetry of the Dirac operator. The discrete operator therefore
recovers not just the spectrum but the actual verified radial spinor profiles —
a stronger statement than KT-1 demanded.

**Component identification note:** χ = −1 hosts the upper component
(= `phi_nl_hopf`), χ = +1 the lower (`g_nl_hopf` = sinα^{l+1} cosα^l
P^{(l+3/2, l+1/2)}_{n−l}). Identified numerically; the analytic ground-state
check (u₀ = sin²α cosα for χ = +1, κ = 1) confirms the assignment.

---

## Generalization (run only after S³ PASS)

### d = 6: PASS

| n | computed | analytic n + 3 |
|---|---|---|
| 0 | 3.000000 | 3.0 |
| 1 | 4.000000 | 4.0 |
| 2 | 4.999999 | 5.0 |
| 3 | 5.999997 | 6.0 |
| 4 | 6.999995 | 7.0 |

max rel. error = 6.71e-07 → PASS.

### d = 2: EXCLUDED from the FD path (recorded, not silently skipped)

κ = 1/2 endpoint coefficient κ(κ−1) = −1/4 is the critical limit-circle value;
uniform FD converges at ~h^0.1 (≈5% error even at N = 32000). Covered by the
shooting solver in `spectral_fingerprint_proxy.py` (error 6.3e-11). A dedicated
test (`test_d2_explicitly_excluded_from_fd`) asserts the exclusion is recorded
in the output, so it cannot disappear from documentation.

---

## Findings

### tom_ansatz → phi_{11}: RADIAL PROJECTION FINDING ONLY

Dominant weighted radial projection of √sin(2α): **0.9204 onto phi_{11}**
(n = 1, l = 1, λ = ±2.5), regression-tested.

**Explicit scope limitation (hard constraint honored):** this is a statement
about RADIAL PROFILES under the weighted radial inner product. The angular
sector of the ansatz is unverified — this is NOT a full spinor identification.
Full angular confirmation is required before any communication to Tom presents
it as a mode identification.

---

## Hard Constraints — Compliance Record

| Constraint | Status |
|---|---|
| IPR not used as primary endpoint | ✓ — IPR absent from this module entirely |
| No claim of resolving S³×S¹ | ✓ — HA-4 recorded OPEN in output + test |
| No physical promotion | ✓ — research_only in output + test |
| HA-4 open | ✓ — `scope["HA-4"] = "OPEN — ..."`, asserted by test |
| tom_ansatz = radial projection only | ✓ — status string asserted by test |

---

## What E0 Does NOT Establish

1. Nothing about the S³×S¹ lattice product (HA-4 OPEN) — this is a continuum
   radial ODE discretization.
2. Nothing about disorder (W > 0 untested; KT-3 pending).
3. Nothing about full angular degeneracies beyond the sector structure
   (angular factors remain analytic inputs).
4. Nothing about the λ coupling (FREE_COUPLING_PARAMETER, untouched) or
   gauge-group emergence.

## Next per decision_record_v0.2.0.md

E0 PASS unblocks: **E2** (Tier 2 controls — largely covered by
`spectral_fingerprint_proxy` results), then parallel **E3/E4/E5**
(cross-sphere already done; disorder KT-3 is the main open experiment),
plus the **E6/HA-4 design gate** before any Phase 3 paper claims.
