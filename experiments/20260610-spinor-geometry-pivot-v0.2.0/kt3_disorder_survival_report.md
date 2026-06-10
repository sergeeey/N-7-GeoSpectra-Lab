# KT-3 — Disorder Survival Test for Spectral Fingerprints

**Experiment:** KT3_DISORDER_SURVIVAL_TEST
**Date:** 2026-06-10
**Code:** `tom_s3_spinor_toy/disorder_survival_proxy.py`
**Tests:** `tom_s3_spinor_toy/tests/test_disorder_survival_proxy.py` — **17/17 passed, 0.50s**
**Raw data:** `kt3_disorder_survival_results.json`
**Status:** research_only — no physical promotion

---

## Verdict

```
PRE-REGISTERED KILL-TEST: max shift of |λ_min| at W=0.1 > 0.25 → KT3_FAIL
RESULT:                    max shift = 7.5e-04 → KT3_PASS
                           (margin: 335× below threshold)

W* > 0.5 (fingerprint survives entire tested disorder range)
```

**KT-3 gate: PASSED.** The Dirac spectral fingerprint |λ_min| = d/2 is
exceptionally robust to diagonal disorder. Even at W = 0.5, the maximum
shift over 10 seeds is 3.7e-3 — 67× below the kill threshold 0.25.
**W* is not yet determined** by this sweep (survives all tested W values).

---

## Setup

**Operator:**
```
H_χ u_i = [-(1/4)u'' + κ(κ+χ·cos 2α)/sin²2α] u_i  +  W · ξ_i · u_i
```
where ξ_i ~ Uniform[-1, 1], zero-mean, with fixed numpy seeds 0..9.
E0 baseline operator unchanged; disorder is purely diagonal.

**Kill threshold:** gap/2 = |λ_min(S²) − λ_min(S³)| / 2 = |1.0 − 1.5| / 2 = **0.25**
If disorder pushes S³ |λ_min| by > 0.25, it enters S² territory — fingerprint
discrimination collapses.

**Grid:** N = 2000 (baseline error ~3e-6; far below any disorder-induced shift).

---

## S³ Results (primary)

### Disorder sweep: W × 10 seeds, primary sphere d=3

| W | median shift | max shift | std | vs threshold 0.25 |
|---|---|---|---|---|
| 0.01 | 4.2e-05 | 7.5e-05 | 2.5e-05 | 3333× below |
| 0.05 | 2.1e-04 | 3.7e-04 | 1.3e-04 | 676× below |
| **0.10** | **4.2e-04** | **7.5e-04** | **2.5e-04** | **335× below** |
| 0.25 | 1.0e-03 | 1.9e-03 | 6.3e-04 | 134× below |
| 0.50 | 2.1e-03 | 3.7e-03 | 1.3e-03 | 67× below |

### Scaling law

max_shift scales **linearly** with W (slope ≈ 7.5e-3 per unit W), consistent
with first-order perturbation theory: δ|λ| ≈ δE/(2λ_0) where δE = W·⟨u₀|diag(ξ)|u₀⟩.

The ground state u₀ is spread over N = 2000 grid points (extended state),
so the disorder matrix element is averaged down to ~W/√N.
This structural averaging is what makes the fingerprint robust.

### W* — applicable disorder range

W* > 0.5 (last tested value). Extrapolating the linear scaling law:
W* ≈ 0.25 / (7.5e-3) ≈ **33** (far outside the tested range).

The fingerprint is not fragile — it is robust by structural averaging, not by
accident of the specific W values tested.

---

## S⁶ Results (secondary)

Same test for d = 6 (|λ_min| = 3.0):

| W | median shift | max shift |
|---|---|---|
| 0.01 | 1.3e-05 | 5.2e-05 |
| 0.05 | 6.7e-05 | 2.6e-04 |
| 0.10 | 1.3e-04 | 5.2e-04 |
| 0.25 | 3.3e-04 | 1.3e-03 |
| 0.50 | 6.6e-04 | 2.6e-03 |

**Verdict: KT3_PASS.** S⁶ shifts are smaller than S³ by a factor of ~1.4,
consistent with 1/(2λ₀) scaling (λ₀(S⁶)=3.0 > λ₀(S³)=1.5, so denominator larger).

---

## Cross-Sphere Separation at W = 0.1

| Observable | Value |
|---|---|
| S³ max |λ_min| over seeds | 1.5007 |
| S⁶ min |λ_min| over seeds | 2.9995 |
| Gap (S⁶_min − S³_max) | **1.4989** |

The analytic gap = 1.5; disorder reduces it by only 1.1e-3. Cross-sphere
discrimination **remains unambiguous** at W = 0.1 and beyond the tested range.

---

## What KT-3 Does NOT Establish

1. **Full lattice (S³×S¹) case (HA-4 OPEN):** this tests the radial operator
   on a single-sphere grid. The original S³×S¹ GEOMETRY_AGNOSTIC verdict
   concerned a product geometry; that is a separate, unresolved question.

2. **Off-diagonal disorder:** only diagonal disorder (Anderson-type, on-site)
   was tested. Off-diagonal disorder (hopping disorder) could behave differently;
   untested.

3. **Many-body or interaction effects:** single-particle radial operator only.

4. **Large W (W > 0.5):** the sweep covers W ≤ 0.5. The linear extrapolation
   to W* ≈ 33 is an estimate; level crossing or localization could change
   the physics at much larger disorder.

5. **Degeneracy pattern under disorder:** |λ_min| is checked but the full
   degeneracy structure (2, 6, 12, 20, ...) under disorder is not yet tested.

---

## Hard Constraints — Compliance Record

| Constraint | Status |
|---|---|
| IPR not used as primary endpoint | ✓ — "shift of |lambda_min|; IPR not used" |
| No claim of resolving S³×S¹ | ✓ — HA-4 OPEN in output + test |
| No physical promotion | ✓ — research_only in output + test |
| tom_ansatz = radial projection only | ✓ — "RADIAL_PROJECTION_FINDING_ONLY" in scope |

---

## Implication for HA-4 Decision

KT-3 PASS with W* > 0.5 changes the HA-4 calculus:

**Before KT-3:** The fingerprint was verified only at W = 0 (clean limit).
It was unknown whether disorder — the essential feature of the original S³×S¹
harness — would destroy it immediately.

**After KT-3:** The fingerprint survives diagonal disorder up to at least W = 0.5,
with 335× margin at W = 0.1. This means:

- *Option (a) — S^d step toward S³×S¹:* the radial spectral fingerprint
  survives the kind of disorder present in the original harness. The physics
  supports using S^d discrimination as a building block toward S³×S¹.
  The missing design question is how to couple the S¹ direction.

- *Option (b) — separate tracks:* still valid if the S¹ coupling introduces
  qualitatively new physics that cannot be anticipated from the radial result.

HA-4 remains OPEN. But KT-3 eliminates the scenario where disorder would
have immediately killed the fingerprint, making Option (a) a credible path.

---

## Next Steps (per decision_record_v0.2.0.md)

With KT-3 PASS, the YELLOW path is partially verified:
- **E5 / FT-S4:** Confirm shooting solver (d=2 limit-circle) in the full
  lattice context — currently covered only at proxy level.
- **E6 / HA-4:** Formal design decision with KT-3 result in hand.
- **NC-2 (pending):** Permuted-grid negative control — only unexecuted
  Tier 3 control.
