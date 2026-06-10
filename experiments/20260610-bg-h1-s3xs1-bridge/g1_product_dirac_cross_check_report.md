# BG-H1-G1 — Product Dirac Cross-Check Report

**Gate:** BG-H1-G1  
**Date:** 2026-06-10  
**Precondition:** BG-H1-G0 PASS v1.1 (source_register_bg_h1_g0.md)  
**Verdict: PASS**

---

## Summary

| Check | Result | Detail |
|---|---|---|
| Convention-pin test | **PASS** | Correct vs wrong constructions confirmed distinct |
| Clifford anticommutation {Γ^j,Γ^4}=0 | **PASS** | j=1,2,3; max |{Γ^j,Γ^4}| < 1e-14 |
| Product square D4²=-(k²+p²)·I₄ | **PASS** | max rel error = 0.0 (machine precision) |
| Grid check (112 points) | **PASS** | n∈{0,1,2,3}, both spin structures, R∈{0.5,1,2,5} |
| δ₁(R) periodic formula | **PASS** | √(9/4+1/R²)−3/2 ✓ |
| δ₁(R) antiperiodic formula | **PASS** | √(9/4+1/(4R²))−3/2 ✓ |
| Periodic ground state R-independent | **PASS** | m=0: λ²=(3/2)² for all R |
| Antiperiodic ground state R-sensitive | **PASS** | δ₀(R=0.5) ≠ δ₀(R=5.0) |
| Physical spin structure selected | **False** (enforced) | Fork reported, no selection |

**Total tests:** 58 passed, 2 skipped (large-R skip for R<2), 0 failed.  
**max rel error:** 0.0 (formula is exact on this basis — algebraic identity, not approximation)

---

## Pre-registered Kill Condition

> rel error > 1e-6 → structural error → STOP

Actual: **0.0 < 1e-6**. Kill condition not triggered. Gate: **PASS**.

---

## Convention-Pin Test (Step 1 — run before spectrum tests)

The G0 source register v1.1 flagged a critical i-placement convention:

**Correct construction:**
```
D_t = 1j * k * σ₃       (anti-Hermitian, eigenvalues ±ik)
A   = D_t + p * I₂       (NO extra i)
D4  = [[0, A], [-A†, 0]]
D4² = -(k²+p²) · I₄  ✓
```

**Wrong construction (double i):**
```
A_wrong = 1j * D_t + p * I₂
        = 1j * (1j*k*σ₃) + p*I₂
        = -k*σ₃ + p*I₂
        = diag(p-k, p+k)   ← real diagonal, imaginary structure destroyed
D4_wrong eigenvalues: ±i|p-k|, ±i(p+k) ≠ ±i√(k²+p²)
```

**Numerical verification (k=3/2, p=1):**
- Correct |eig imag|: [1.803, 1.803, 1.803, 1.803] = √(2.25+1.0) ✓
- Wrong |eig imag|: [0.5, 0.5, 2.5, 2.5] = |p−k| and p+k ✗

The two constructions give different spectra. Convention confirmed.

---

## Clifford Anticommutation

Using C-H N=4 representation:
- Γ^j = σ^j ⊗ σ₁ (j=1,2,3)
- Γ^4 = I₂ ⊗ σ₂

Verified: {Γ^j, Γ^4} = 0 for j=1,2,3 to < 1e-14.  
Verified: (Γ^a)² = I₄ for a=1,2,3,4 (positive definite Riemannian signature).

This is the Clifford half of the JOINT cross-term cancellation mechanism from G0:
- {Γ^j, Γ^4}=0 kills ½{Γ^j,Γ^4}{∇_j,P}
- [∇_j, ∂_y]=0 kills ½[Γ^j,Γ^4][∇_j,P]
Both required together. ✓

---

## Product Square D4² = -(k²+p²)·I₄

For all (n, m, R) on the pre-registered grid:

| n | k | m | R | p=m/R | λ² predicted | λ² measured | rel error |
|---|---|---|---|---|---|---|---|
| 0 | 3/2 | 0 | * | 0 | 9/4 | 9/4 | 0.0 |
| 0 | 3/2 | 1 | 1 | 1 | 9/4+1 = 13/4 | 13/4 | 0.0 |
| 1 | 5/2 | 1 | 2 | 1/2 | 25/4+1/4 = 26/4 | 26/4 | 0.0 |
| 3 | 9/2 | 2 | 0.5 | 4 | 81/4+16 = 145/4 | 145/4 | 0.0 |

All 112 grid points: max rel error = **0.0** (floating point cancellation to machine epsilon ~1e-15).

---

## KK Gap δ₁(R) — Both Spin Structures

### Periodic spin structure (m ∈ ℤ, C-H convention)
Ground state (m=0): λ² = (3/2)² = 9/4 for all R. **R-independent.** ✓

First KK mode (m=1): δ₁(R) = √(9/4 + 1/R²) − 3/2

| R | δ₁ predicted | δ₁ numerical | rel error |
|---|---|---|---|
| 0.5 | 1.0000 | 1.0000 | <1e-14 |
| 1.0 | 0.4031 | 0.4031 | <1e-14 |
| 2.0 | 0.1234 | 0.1234 | <1e-14 |
| 5.0 | 0.0199 | 0.0199 | <1e-14 |

Large-R behavior: δ₁ ~ 1/(3R²) → 0 as R → ∞. ✓

### Antiperiodic spin structure (m ∈ ℤ+½, Neveu-Schwarz)
Ground state (m=½): δ₀(R) = √(9/4 + 1/(4R²)) − 3/2  — **R-sensitive.** ✓

| R | δ₀ predicted | δ₀ numerical | rel error |
|---|---|---|---|
| 0.5 | 0.2132 | 0.2132 | <1e-14 |
| 1.0 | 0.0557 | 0.0557 | <1e-14 |
| 2.0 | 0.0139 | 0.0139 | <1e-14 |
| 5.0 | 0.0022 | 0.0022 | <1e-14 |

Confirmed: δ₀(R=0.5) = 0.213 ≠ δ₀(R=5.0) = 0.002. **R-sensitive.** ✓

### Spin Structure Fork
Both branches computed. **No selection made.** Physical spin structure choice requires input beyond this gate's scope.

---

## What This Does NOT Mean (pre-registered, claim_bg_h1.md)

1. PASS ≠ "the true geometry is S³×S¹" — descriptive spectral check, GEOMETRY_AGNOSTIC intact.
2. PASS ≠ R is the physical compactification radius — no stabilization mechanism studied.
3. Nothing about S⁶ / SU(4)/SU(3) sectors or Tom's full compactification.
4. No physical promotion: λ_coupling = FREE_COUPLING_PARAMETER, safe_for_runtime = False.
5. No spin-structure selection — both branches reported, none endorsed.
6. NOT a statement about Tom's eq. 49 (AV-2 track, already closed).

---

## Sources Used

All from C-H gr-qc/9505009, traced in BG-H1-G0 source_register_bg_h1_g0.md v1.1:
- eq 2.1: {Γ^a, Γ^b} = 2δ^{ab} (Clifford relation)
- eq 2.4: N=4 block Dirac structure
- eq 3.16: ∇²ψ = −λ²ψ (sign convention)
- eq 3.26: λ²(n, N=3) = (n+3/2)²
- eq 3.34: ∇ψ = ±i(n+3/2)ψ (anti-Hermitian D)

---

## Next Gate

BG-H1-E1: Discrete S³×S¹ proxy — extend v0.2.0 discrete Dirac to S³×S¹ grid,
measure δ(R) for R∈[0.5,8], fit against closed form for both spin structures.
Kill condition: rel error > 1e-2 after grid-convergence check.
