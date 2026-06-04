# Cross-Geometry S²×S¹ Pre-Registration — v0.1.25

**Date:** 2026-06-03
**Status:** PRE-REGISTERED (written before any S²×S¹ execution)
**Prerequisite:** Gate 4B v0.1.24 SIGNAL_PRESERVED on S³×S¹
**Question type:** Descriptive

---

## Purpose

Gate 4B result is S³×S¹ only — no generalization claim is allowed.
Cross-geometry pilot asks: does the ring-family lattice localization signal
transfer to S²×S¹ (lower-dimensional sphere)?

**This matters because:**
- Transfer → signal is a lattice product property, not S³-specific
- No transfer → S³ dimension is necessary, stronger specificity
- Either outcome is scientifically meaningful and narrows the claim

---

## Estimand

**Population:** S²×S¹ finite-lattice product geometry
- S²: spectral Laplacian on 2-sphere (l=0,1,...,j_max), dim = (j_max+1)²
- S¹: ring discretization (same as Gate 4B ring family)

**Intervention:** Anderson disorder W=20, diagonal U(r) ∈ [-W, W]

**Comparator:** Gate 4B ring IPR(W=20) on S³×S¹:
- s1=16: 0.326, s1=32: 0.322, s1=64: 0.320 (plateau)

**Endpoint:** true_IPR(W=20) by s1_size — plateau vs decay

**Summary measure:** FSS slope and IPR(W=20) trajectory

**MCID:**
- TRANSFER (≥50% of S³×S¹ contrast): signal present in S²×S¹
- PARTIAL (20–50% of S³×S¹ contrast): weaker signal, dimension matters
- NO_TRANSFER (<20%): S³ dimension necessary

---

## Grid (Pilot)

| Parameter | Values |
|-----------|--------|
| Geometry | S²×S¹ |
| S¹ family | ring |
| s1_size | 16, 32, 64 |
| W | 0, 20 |
| j_max | 3 (S² truncation) |
| seeds | 123, 456, 789 |
| alpha | 0.0 |
| **Total** | **3 × 2 × 1 × 3 = 18 cases** |

Runtime estimate: ~5s/case (smaller S² dim than S³) → ~2 min total.

---

## Decision Rules (Pre-Registered)

S²×S¹ ring contrast threshold:

| Contrast at s1=64 | vs S³×S¹ ref (~14.2×) | Verdict |
|-------------------|-----------------------|---------|
| ≥7.1× (50%) | ≥50% | TRANSFER |
| 2.8–7.1× (20–50%) | 20–50% | PARTIAL |
| <2.8× (<20%) | <20% | NO_TRANSFER |

Secondary: IPR(W=20) trajectory — plateau (flat) vs decay.

**Follow-up rule:** If TRANSFER → run full 216-case grid on S²×S¹ (Gate 4B scale).

---

## Claims Boundary (Pre-Registered)

**If TRANSFER:**
- Allowed: "S²×S¹ pilot shows localization-like signal at W=20 (contrast ≥50% of S³×S¹)"
- Forbidden: "FL×S¹ generalised" — only two geometries tested

**If NO_TRANSFER:**
- Allowed: "S²×S¹ pilot does not reproduce S³×S¹ contrast (ratio <20%)"
- Allowed: "S³ dimension may be necessary for the observed signal"
- Forbidden: "S³×S¹ uniquely validated" — negative pilot ≠ uniqueness proof

---

## What This Result Does NOT Mean

1. TRANSFER does NOT prove physics of Kaluza-Klein on S²×S¹.
2. NO_TRANSFER does NOT prove S³ uniqueness — only pilot-scale pilot.
3. Does NOT test S⁶ or higher-dimensional geometries.
4. Pilot only (18 cases) — insufficient for FSS characterization without follow-up.

---

**Status:** PRE-REGISTERED — awaiting server execution
**Next step:** `scripts/run_cross_geometry_s2s1_v0.1.25.py --dry-run`
