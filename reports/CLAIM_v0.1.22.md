# FL Claim — v0.1.22 Negative Controls
# FL Full-Ladder Step 0

**Date:** 2026-06-03
**Version:** v0.1.22
**FL Step:** 0 (Falsifiable Claim)
**Derived from:** ESTIMAND_v0.1.22.md
**Pre-registration reference:** S3_S1_NEGATIVE_CONTROLS_PREREGISTRATION_v0.1.22.md

---

## Primary Claim (Falsifiable)

> **C1 — Harness discrimination:**
> "Negative controls (random_hermitian, scrambled_geometry, broken_wilson)
> will NOT reproduce the ring/wilson_ring localization pattern:
> specifically, their IPR(W=20) will NOT form a plateau flat across
> s1_size=16→128, AND/OR their IPR contrast will fall below 7.15×."

**Criterion for confirmation (C1 CONFIRMED):**
≥2/3 controls show IPR(W=20) decreasing with N AND contrast < 7.15×

**Criterion for falsification (C1 FALSIFIED):**
ANY control shows IPR(W=20) plateau (flat ±20% across ≥3 sizes)
AND contrast ≥7.15× — gate 4B signal reproduced by broken control.

---

> **C2 — spectral_circle diagnosis:**
> "spectral_circle IPR(W=20) will show the SAME decreasing-with-N pattern
> on scrambled geometry as on S³×S¹ geometry (same operator dimension, no
> S³×S¹ structure), indicating the spectral_circle Gate 4B result is
> driven by matrix structure, not geometric coupling."

**Criterion for confirmation (C2 CONFIRMED — ARTIFACT):**
spectral_circle scrambled IPR(W=20) trajectory ≈ spectral_circle S³×S¹ trajectory
(both decreasing, within 30% at each size).

**Criterion for falsification (C2 FALSIFIED — GEOMETRIC SIGNAL):**
spectral_circle scrambled IPR(W=20) is ≥2× higher than S³×S¹ at s1_size=64 or 128.

---

## Consequences by Outcome

### If C1 CONFIRMED and C2 CONFIRMED:
- Gate 4B ring/wilson_ring signal is geometry-specific (not reproduced by broken controls)
- spectral_circle is a structural artifact — "3/3 PASS" should be qualified
- **Allowed updated claim:** "ring and wilson_ring independently support finite-lattice
  localization-like signal specific to S³×S¹ geometric coupling. spectral_circle
  result is structurally indeterminate (artifact hypothesis not rejected)."
- **New allowed claim:** "2/3 valid geometric families (ring, wilson_ring) pass
  negative control screening."

### If C1 CONFIRMED and C2 FALSIFIED:
- Gate 4B signal is geometry-specific
- spectral_circle does respond to geometry (weaker localization, not artifact)
- "3/3 PASS" remains valid with weaker-localization qualifier for spectral_circle
- **Updated spectral_circle caveat:** IPR(W=20) decreasing with N is geometric,
  not artifactual — spectral_circle shows weaker localization than ring/wilson_ring.

### If C1 FALSIFIED (ANY control reproduces signal):
- Gate 4B specificity claim is WEAKENED
- Cannot claim signal is S³×S¹-specific
- **Required action:** identify WHICH structural property of the falsifying control
  produces the plateau. Revise harness discrimination criteria.
- Gate 4B verdict unchanged (pre-registered). Specificity claim must be removed.

---

## What This Claim Does NOT Assert

- NOT: "Negative controls confirm compactification"
- NOT: "S³×S¹ is the only geometry showing localization"
- NOT: "W=20 is optimal for any geometry"
- NOT: "Gate 4B verdict changes based on v0.1.22 results"
- NOT: "spectral_circle artifact implies Gate 4B is invalid" (ring+wilson_ring
  alone are sufficient for "2/3 families PASS" — threshold still met)

---

## Pre-Run Integrity Check

Before batch execution, confirm:
- [x] Estimand written (ESTIMAND_v0.1.22.md)
- [x] Claims written BEFORE seeing batch results (this file, 2026-06-03)
- [x] Thresholds defined (7.15× reference, ±20% plateau criterion)
- [x] Consequences table written for all outcome combinations
- [ ] Controls implementation verified (code review of scrambled_geometry operator)
- [ ] Dry run ≥1 case per control type before full batch

---

**Status:** PRE-RUN — written before any v0.1.22 batch results
**FL Step:** 0 COMPLETE
**Next:** FL step 1 (experiment.yaml) + step 2 (minimal artifact build)
**Date:** 2026-06-03
