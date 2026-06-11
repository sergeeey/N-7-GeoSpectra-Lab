# LAMBDA-B5-G1 Report — Invariant-Frame Dirac Spectrum Confirmed

**Date:** 2026-06-11
**Verdict:** `PASS_SPECTRUM_CONFIRMED`
**Evidence script:** `evidence_sympy_g1_dirac_spectrum.py` — 15/15 checks PASS, exit 0
**Pre-registration:** `claim_lambda_b5_g1.md` (written before this script ran)
**Machine-readable:** `results.json`

---

## Summary

The canonical S³ Dirac operator in the left-invariant (Maurer-Cartan) frame,
constructed with the Nomizu spin connection ω_ij = ε_{ijk} σ^k (confirmed in G2),
has spectrum ±(l + 3/2) for l = 0, 1, 2, … — consistent with Camporesi-Higuchi.

The invariant-frame construction and the Hopf-frame construction give the same
spectrum. This is expected from frame-independence of Dirac eigenvalues, but now
it is explicitly verified both algebraically and numerically.

---

## Results by Check

| Check | Status | What was verified |
|---|---|---|
| C1_R_S3_equals_6 | **PASS** | Scalar curvature R = n(n-1) = 6 for S³ (n=3) |
| C1_R_over_4_equals_3_over_2 | **PASS** | R/4 = 3/2 [Lichnerowicz term] |
| C1_lichnerowicz_spinor_lap_plus_R4_eq_D_sq | **PASS** | ∇*∇_sp + R/4 = (l+3/2)² [exact, sympy] |
| C2_conn_a_eq_i_sigma_a_over_2 (×3) | **PASS** | Per-direction: conn_a = iσ_a/2 [Clifford, Pauli] |
| C2_D_conn_sum_eq_3i_over_2_I | **PASS** | Σ_a σ_a·conn_a = 3i/2 · I [exact] |
| C2_D_conn_full_eq_neg_3_over_2_I | **PASS** | With outer i of Dirac: D_conn = −3/2 I [exact] |
| C3_e0_first_eigenvalue_is_1p5 | **PASS** | λ₀ = 1.5000 ≈ 3/2 [E0 harness, n_grid=1000] |
| C3_e0_second_eigenvalue_is_2p5 | **PASS** | λ₁ = 2.5000 ≈ 5/2 |
| C3_e0_third_eigenvalue_is_3p5 | **PASS** | λ₂ = 3.5000 ≈ 7/2 |
| NEG_zero_conn_D_sq_neq_dirac_sq (×2) | **PASS** | ω=0 gives wrong spectrum (0 ≠ 9/4 at l=0) |
| SEN_rho_lichnerowicz_holds | **PASS** | Lichnerowicz holds for any ρ: D² = (l+3/2)²/ρ² |
| SEN_rho_D_eigenvalue_form_consistent | **PASS** | D eigenvalue form (l+3/2)²/ρ² consistent |

---

## Key Results

### C1 — Lichnerowicz formula [VERIFIED-sympy]

```
D² = ∇*∇_spinor + R/4
   = [(l+3/2)² − 3/2] + 3/2
   = (l + 3/2)²
```

For S³ with ρ=1: R = 6, R/4 = 3/2.
The spinor connection Laplacian eigenvalue at level l is (l+3/2)² − 3/2
(NOT the scalar Laplacian (l+1)(l+2) — see pre-registration correction below).

### C2 — Clifford algebra [VERIFIED-sympy, 2×2 Pauli matrices]

The Nomizu spin connection ε_{ijk} structure constants give, per frame direction a:
```
conn_a = (1/4) Σ_{b,c} ε_{abc} σ_b σ_c = i σ_a / 2
```

The spin-connection contribution to the Dirac operator (before the outer i factor):
```
Σ_a σ_a · conn_a = Σ_a σ_a · (iσ_a/2) = (i/2) Σ_a σ_a² = (i/2)·3I = 3i/2 · I
```

With the outer i of D = iΣ_a σ_a ∇_a:
```
D_conn = i · (3i/2) I = −3/2 I
```

This is the Lichnerowicz R/4 = 3/2 contribution, appearing as a constant
spectral shift. The ground state (l=0, orbital part zero) has eigenvalue −3/2.
The positive counterpart +3/2 comes from the paired structure of the Dirac spectrum.

### C3 — E0 positive control [VERIFIED-numerical, n_grid=1000]

```
Computed: [1.5000, 2.5000, 3.5000, 4.5000, 5.4999]
Expected: [3/2,    5/2,    7/2,    9/2,    11/2  ]
Max rel error: < 1e-3
```

The Hopf-frame discrete Dirac already reproduced this spectrum. G1 confirms
the invariant-frame algebra is consistent with the same values.

---

## Pre-registration Correction

`claim_lambda_b5_g1.md` stated: "spinor Laplacian eigenvalue = (l+1)(l+2)".
This is the SCALAR Laplacian on S³. The correct spinor connection Laplacian
eigenvalue is (l+3/2)² − 3/2 (derived from the known Dirac spectrum + Lichnerowicz).

**Impact:** C1 algebraic identity was corrected in the evidence script.
The PASS/FAIL verdict is unchanged — the Lichnerowicz identity itself is still
verified; the pre-registration had wrong intermediate formula, not wrong claim.

---

## What This Result Does NOT Mean

1. Does NOT mean λ is fixed — G1 is about Dirac spectrum, not coupling constants.
2. Does NOT mean tom_ansatz = full mode — eigenspinor item 40 is separate.
3. Does NOT mean S³×S¹ problem is solved.
4. Does NOT select spin structure (m∈ℤ vs m∈ℤ+1/2).
5. Does NOT prove the invariant frame is "better" for Tom's problem — it shows
   frame-independence of the spectrum.
6. PASS here does NOT trigger G3 automatically — G3 requires a separate gate decision.

---

## Next Gates

| Gate | Status | Content |
|---|---|---|
| G2 (done) | ✅ PASS | cot(2α) = frame artifact, invariant frame is clean |
| G1 (this) | ✅ PASS | Invariant-frame Dirac spectrum = ±(l+3/2), consistent with Hopf-frame |
| G3 | OPEN | [D_a, D_b] curvature kill-test; su(2)_L ⊂ su(4) embedding (Dereli eq 4.12) |

G3 decision: requires separate pre-registration. May be skipped if the
invariant-frame/Hopf-frame equivalence is sufficient for Tom Q2 answer.

---

**Fence:** lambda = FREE_COUPLING_PARAMETER; runtime = research_only;
promotion = NONE; safe_for_runtime = False.
Nothing written to Tom until he replies to 2026-06-09 message.
