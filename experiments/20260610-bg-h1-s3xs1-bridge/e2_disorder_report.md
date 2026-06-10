# BG-H1-E2 — Disorder Robustness Gate Report

**Gate:** BG-H1-E2
**Date:** 2026-06-10
**Precondition:** BG-H1-G0 PASS v1.1 + BG-H1-G1 PASS + BG-H1-E1 PASS
**Verdict: PASS**

---

## Summary

| Check | Result | Detail |
|---|---|---|
| Periodic δ(R) monotone decreasing in R | **PASS** | Confirmed over all 30 seeds |
| Antiperiodic δ(R) monotone decreasing in R | **PASS** | Confirmed over all 30 seeds |
| Max mean rel error vs analytic (periodic) | **PASS** | 2.53e-04 ≪ kill 5e-02 |
| Max mean rel error vs analytic (antiperiodic) | **PASS** | 2.54e-04 ≪ kill 5e-02 |
| Max fragility ratio (periodic) | **PASS** | 0.996 ≪ kill 10.0 |
| Max fragility ratio (antiperiodic) | **PASS** | 0.998 ≪ kill 10.0 |
| No physical spin structure selected | **True** (enforced) | Fork reported, no selection |

**S³ ground state under disorder:** k₀_baseline = 1.4999992975 (N=1000), k₀_mean = 1.5003936, k₀_std = 4.32e-03, s3_max_rel_fragility = 6.55e-03
**Max product fragility ratio:** 0.998 (antiperiodic, R=8) — product gap NOT more fragile than S³

---

## Pre-registered Kill Condition

> "Fingerprint destroyed by disorder only on product (not on S³) → bridge is fragile, FLAG."
>
> Operationalized as:
> (a) max_R fragility_ratio > 10.0 (product more than 10× more fragile than S³)
> (b) mean_rel_error > 5% at any R
> (c) mean δ(R) not monotone decreasing

All three conditions **NOT triggered**. Gate: **PASS**.

---

## Method

**Disorder model (identical to KT-3):**
- S³ FD diagonal perturbed: `diag_d = diag + W × ξ`, `ξ ~ Uniform(−1, 1)`
- W = 0.5 (more aggressive than KT-3's W_KILL = 0.1)
- 30 seeds (3× more than KT-3's 10 seeds)
- S¹ modes: EXACT (Fourier basis, not disordered)

**Product gap under disorder:**
- For each seed s: k₀_s = S³ ground eigenvalue under disorder
- δ_s(R) = √(k₀_s² + (m₁/R)²) − k₀_s (same E1 formula, disordered k₀)

**Fragility ratio definition:**
```
fragility_ratio(R) = (mean|δ_s(R) − δ_clean(R)|/δ_clean(R)) / (mean|k₀_s − k₀_base|/k₀_base)
```
Ratio < 1: product gap less sensitive to disorder than S³ fingerprint
Ratio ≈ 1: comparable sensitivity (expected analytically for large R)
Ratio >> 1: product gap MORE fragile — kill condition

---

## δ₁(R) Tables Under Disorder W=0.5 (30 seeds)

### Periodic spin structure (m₁=1, m ∈ ℤ)

| R | mean δ | std δ | mean rel err vs analytic | fragility ratio |
|---|---|---|---|---|
| 0.5 | 0.9998450 | 1.73e-03 | 1.55e-04 | 0.600 |
| 1.0 | 0.3027111 | 7.26e-04 | 2.13e-04 | 0.832 |
| 2.0 | 0.0811192 | 2.22e-04 | 2.42e-04 | 0.948 |
| 4.0 | 0.0206854 | 5.88e-05 | 2.51e-04 | 0.986 |
| 6.0 | 0.0092285 | 2.64e-05 | 2.53e-04 | 0.993 |
| 8.0 | 0.0051980 | 1.49e-05 | 2.53e-04 | 0.996 |

### Antiperiodic spin structure (m₁=1/2, m ∈ ℤ+½, Neveu-Schwarz)

| R | mean δ | std δ | mean rel err vs analytic | fragility ratio |
|---|---|---|---|---|
| 0.5 | 0.3027111 | 7.26e-04 | 2.13e-04 | 0.832 |
| 1.0 | 0.0811192 | 2.22e-04 | 2.42e-04 | 0.948 |
| 2.0 | 0.0206854 | 5.88e-05 | 2.51e-04 | 0.986 |
| 4.0 | 0.0051980 | 1.49e-05 | 2.53e-04 | 0.996 |
| 6.0 | 0.0023124 | 6.65e-06 | 2.54e-04 | 0.998 |
| 8.0 | 0.0013012 | 3.75e-06 | 2.54e-04 | 0.998 |

**Spin Structure Fork:** Both branches computed. **No selection made.**

---

## Fragility Ratio Analysis

**Observed:** fragility ratio ∈ [0.60, 0.998] — product gap ≤ S³ fragility at all R values.

**Analytic explanation:** Since δ(R) = √(k₀² + (m₁/R)²) − k₀, the sensitivity is:
```
dδ/dk₀ = k₀/√(k₀² + (m₁/R)²) − 1 ∈ (−1, 0)
```
This is always negative and bounded: |dδ/dk₀| < 1. The relative fragility ratio
```
|dδ/dk₀| × k₀/δ → 1   (large R, δ → 0)
|dδ/dk₀| × k₀/δ < 1  (small R, δ large)
```
Therefore fragility_ratio ≤ 1 analytically, and the observed values (0.6–1.0) match this.
**Kill condition (ratio > 10) cannot be triggered by this mechanism** — the product structure
adds NO fragility beyond the S³ sector.

---

## S³ Robustness at W=0.5

At W=0.5 (2× more aggressive than KT-3's primary test):
- k₀ mean rel fragility: 2.31e-03 (~0.23%)
- k₀ max rel fragility: 6.55e-03 (~0.66%)

The S³ fingerprint remains well within the KT-3 threshold (0.25 shift = 16.7% relative).
Consistent with KT-3 result which showed robustness up to at least W=0.5 in its sweep.

---

## What This Does NOT Mean (pre-registered, claim_bg_h1.md)

1. PASS ≠ "the true geometry is S³×S¹" — bridge feasibility check; GEOMETRY_AGNOSTIC intact.
2. PASS ≠ R is the physical compactification radius (no stabilization mechanism studied).
3. Nothing about S⁶ / SU(4)/SU(3) sectors or Tom's full compactification.
4. No physical promotion: λ_coupling = FREE_COUPLING_PARAMETER, safe_for_runtime = False.
5. No spin-structure selection — both branches reported, none endorsed.

---

## Gate Status

| Gate | Verdict |
|---|---|
| BG-H1-G0 (source trace) | ✅ PASS v1.1 |
| BG-H1-G1 (analytic cross-check) | ✅ PASS (max_err=0.0) |
| BG-H1-E1 (discrete proxy) | ✅ PASS (max_err=2.93e-08) |
| **BG-H1-E2 (disorder W=0.5)** | **✅ PASS (max_frag_ratio=0.998, max_mean_err=2.54e-04)** |

**Combined G0+G1+E1+E2 verdict:** `S3XS1_KK_BRIDGE_SUPPORTED_ROBUST` (descriptive only, per claim_bg_h1.md).

All 4 gates complete. BG-H1 hypothesis fully evaluated.
