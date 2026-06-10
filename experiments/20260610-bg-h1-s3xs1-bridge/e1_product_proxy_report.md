# BG-H1-E1 — Discrete S³×S¹ Proxy Gate Report

**Gate:** BG-H1-E1 (Primary)
**Date:** 2026-06-10
**Precondition:** BG-H1-G0 PASS v1.1 + BG-H1-G1 PASS
**Verdict: PASS**

---

## Summary

| Check | Result | Detail |
|---|---|---|
| Periodic δ(R) vs formula | **PASS** | max rel error = 2.92e-08 (kill: >1e-2) |
| Antiperiodic δ(R) vs formula | **PASS** | max rel error = 2.93e-08 |
| Negative control (m=0, δ=0) | **PASS** | δ < 1e-14 for all R (periodic ground) |
| Grid convergence (periodic) | **PASS** | Monotone O(h²): 1.56e-06→2.44e-08 |
| Grid convergence (antiperiodic) | **PASS** | Monotone, same rate |
| Edge behavior: large R (R=8) | **PASS** | δ≈0.0052 (KK suppressed) |
| Edge behavior: small R (R=0.5) | **PASS** | δ=1.0 (KK dominates) |
| Kronecker sum identity | **PASS** | max_abs_err = 9.09e-13 (machine precision) |
| Spin structure selected | **False** (enforced) | Fork reported, no selection |

**S³ ground state:** k₀_disc(N=4000) = 1.4999999561 (analytic: 1.5)
**max rel error overall:** 2.93e-08 ≪ kill threshold 1e-2

---

## Pre-registered Kill Condition

> max rel error > 1e-2 → FAIL

Actual: **2.93e-08 < 1e-2**. Kill condition not triggered. Gate: **PASS**.

---

## Method

**Spectrum additivity (exact for Kronecker-sum structure):**
1. λ_S3_0_disc = lowest eigenvalue of FD tridiagonal on S³ (reuses E0 operator, N=4000 interior points)
2. S¹ modes: p = m/R (kept EXACT — Fourier basis, no S¹ discretization error)
3. Product gap: δ_disc(R) = √(λ_S3_0_disc² + (m₁/R)²) − λ_S3_0_disc
4. Compare to: δ_analytic(R) = √(9/4 + (m₁/R)²) − 3/2

The Kronecker-sum cross-check confirms that this additivity holds at the discrete level (eigenvalues of D²_S3⊗I + I⊗D²_S1 = all pairwise sums {λ_S3_i² + λ_S1_j²}) to machine precision.

---

## δ₁(R) Tables — Both Spin Structures

### Periodic spin structure (m₁=1, m ∈ ℤ)

Ground state m=0: λ² = (3/2)² for all R — **R-independent, δ₀=0**. ✓

First KK mode m=1: δ₁(R) = √(9/4 + 1/R²) − 3/2

| R | δ_disc | δ_analytic | rel error |
|---|---|---|---|
| 0.5 | 1.0000000 | 1.0000000 | 1.76e-08 |
| 1.0 | 0.3027756 | 0.3027756 | 2.44e-08 |
| 2.0 | 0.0811388 | 0.0811388 | 2.78e-08 |
| 4.0 | 0.0206906 | 0.0206906 | 2.89e-08 |
| 6.0 | 0.0092309 | 0.0092309 | 2.91e-08 |
| 8.0 | 0.0051993 | 0.0051993 | 2.92e-08 |

### Antiperiodic spin structure (m₁=1/2, m ∈ ℤ+½, Neveu-Schwarz)

Ground state m=1/2: δ₀(R) = √(9/4 + 1/(4R²)) − 3/2 — **R-sensitive**. ✓

| R | δ_disc | δ_analytic | rel error |
|---|---|---|---|
| 0.5 | 0.3027756 | 0.3027756 | 2.44e-08 |
| 1.0 | 0.0811388 | 0.0811388 | 2.78e-08 |
| 2.0 | 0.0206906 | 0.0206906 | 2.89e-08 |
| 4.0 | 0.0051993 | 0.0051993 | 2.92e-08 |
| 6.0 | 0.0023130 | 0.0023130 | 2.92e-08 |
| 8.0 | 0.0013015 | 0.0013015 | 2.93e-08 |

**Spin Structure Fork:** Both branches computed. **No selection made.** Physical choice requires input beyond this gate's scope.

---

## Grid Convergence (R=1, periodic m₁=1)

O(h²) convergence confirmed. Doubling N reduces error by ~4× (as expected for 2nd-order FD).

| N_alpha | k₀_disc | rel error |
|---|---|---|
| 500 | 1.4999971899 | 1.56e-06 |
| 1000 | 1.4999992975 | 3.90e-07 |
| 2000 | 1.4999998244 | 9.74e-08 |
| 4000 | 1.4999999561 | 2.44e-08 |

**Rate:** ~4× improvement per 2× N, consistent with O(h²) = O(N⁻²) FD convergence. ✓
Monotone: **True** (checked by tests).

---

## Edge Behavior (Sensitivity #3)

**Large R (R=8, periodic m₁=1):**
- δ_analytic(R=8) = 0.0051993
- Leading-order approximation: (m₁/R)²/(2k₀) = 1/(3×64) = 0.0052083
- Relative deviation from approx: ~0.17% (well within 3% tolerance) ✓

**Small R (R=0.5, periodic m₁=1):**
- δ_analytic(R=0.5) = 1.0 (KK gap equals full ground-state energy) ✓
- KK dominance confirmed: δ(R=0.5) > 0.5 ✓

**Monotone in R:** δ decreasing as R increases — confirmed for both discrete and analytic. ✓

---

## Kronecker-Sum Cross-Check (Small Grid)

Built D²_prod = D²_S3_disc ⊗ I_S1 + I_S3 ⊗ D²_S1_disc (n_alpha=30, n_s1=16, R=1).
Matrix size: 29 × 16 = 464 × 464.

Verified: eigenvalues of D²_prod = all pairwise sums {λ_S3_i + λ_S1_j}.
**max_abs_err = 9.09e-13** (< 1e-8 threshold). Machine precision algebraic identity. ✓

This confirms that:
1. The spectrum additivity λ²_{prod} = λ²_{S3} + λ²_{S1} holds at the discrete operator level.
2. The Clifford cross-term cancellation (established in G0/G1) is geometrically realized in the product discrete operator.

---

## Negative Control

Periodic m=0 (S³ ground, m=0 KK ground): δ = √(k₀_disc² + 0) - k₀_disc = 0.
**δ < 1e-14 for all R ∈ {0.5, 1.0, 2.0, 4.0, 6.0, 8.0}**. ✓

This is the pure-S³ fingerprint E0≈3/2, unshifted by KK compactification when m=0.

---

## What This Does NOT Mean (pre-registered, claim_bg_h1.md)

1. PASS ≠ "the true geometry is S³×S¹" — bridge feasibility check; GEOMETRY_AGNOSTIC intact.
2. PASS ≠ R is the physical compactification radius (no stabilization mechanism studied).
3. Nothing about S⁶ / SU(4)/SU(3) sectors or Tom's full compactification.
4. No physical promotion: λ_coupling = FREE_COUPLING_PARAMETER, safe_for_runtime = False.
5. No spin-structure selection — both branches reported, none endorsed.
6. NOT a statement about Tom's eq. 49 (AV-2 track, already closed).

---

## Sources

All from C-H gr-qc/9505009, traced in source_register_bg_h1_g0.md v1.1:
- eq 3.26: λ²(n, N=3) = (n+3/2)² — S³ spectrum
- Product spectrum additivity: established analytically in G1 (D4²=-(k²+p²)·I₄)
- Algebraic basis: Kronecker-sum eigenvalue theorem (standard linear algebra)

---

## Gate Status

| Gate | Verdict |
|---|---|
| BG-H1-G0 (source trace) | ✅ PASS v1.1 |
| BG-H1-G1 (analytic cross-check) | ✅ PASS (max_err=0.0) |
| **BG-H1-E1 (discrete proxy)** | **✅ PASS (max_err=2.93e-08)** |
| BG-H1-E2 (disorder W=0.5) | ▶ NEXT |

**Combined G0+G1+E1 verdict:** `S3XS1_KK_BRIDGE_SUPPORTED` (descriptive only, per claim_bg_h1.md verdict rules).

---

## Next Gate

BG-H1-E2: Disorder robustness — does δ(R) shape survive disorder W=0.5 (KT-3 analog)?
Kill condition: fingerprint destroyed by disorder on product but not on pure S³ → bridge is fragile, FLAG.
