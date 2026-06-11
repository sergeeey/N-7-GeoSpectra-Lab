# LAMBDA-B5-G1: Canonical Dirac in Left-Invariant Frame → Spectrum ±(n+3/2)

**Date pre-registered:** 2026-06-11 (design only — implementation NOT started)
**Tier:** FL Standard (mathematical/structural claim, sympy + E0 harness)
**Question type:** [x] descriptive (structural)  [ ] predictive  [ ] causal
**Status:** research_only — no physical promotion
**Parent gate:** LAMBDA-B5-G2 `PASS_FRAME_ARTIFACT_CONFIRMED`
  (experiments/20260611-lambda-b5-cot-frame-artifact/)

---

## Claim (pre-registered, written before code runs)

**The canonical S³ Dirac operator constructed in the left-invariant (Maurer-Cartan)
frame, using the Nomizu spin connection ω_ij = ε_{ijk} σ^k (constant integer
structure constants, confirmed in G2), has spectrum ±(n + 3/2) for n = 0, 1, 2, …
This is consistent with the Camporesi-Higuchi result (gr-qc/9505009, eq. 3.28
specialised to N=3, ρ=1).**

Specifically:

1. The squared Dirac operator satisfies:
   ```
   D² = −∇²_spinor + R/4
   ```
   where R = 6 is the scalar curvature of S³ with ρ=1 (R = n(n-1) for Sⁿ).
   This is the Lichnerowicz formula.

2. The spinor Laplacian eigenvalues on S³ are:
   ```
   −∇²_spinor ψ = (l + 1)(l + 2) ψ      l = 0, 1, 2, …
   ```
   so D² eigenvalues = (l+1)(l+2) + 3/2 = (l + 3/2)² ← the Dirac spectrum.

3. Therefore D has eigenvalues ±(l + 3/2), with degeneracy (l+1)(l+2) per sign,
   consistent with arXiv:1103.4097 formula (same degeneracy used in E0 harness).

4. The POSITIVE CONTROL is the existing E0 harness (`discrete_radial_dirac_proxy.py`,
   n_grid=4000) which already confirms λ₀ ≈ ±1.500 = ±3/2, λ₁ ≈ ±2.500 = ±5/2.

---

## Motivation

G2 proved that the cot(2α) spin connection in Hopf frame = tanα − cotα is a frame
artifact: in the invariant frame all connection coefficients are ε_{ijk} (integers).
G1 closes the loop: does the invariant-frame Dirac operator, with this clean connection,
reproduce the known S³ spectrum? If YES → the Hopf and invariant-frame representations
are spectral-equivalent (as expected from frame-independence of the Dirac spectrum).
If NO → there is a hidden obstruction in the invariant-frame construction.

This is the consistency test between G2 (frame artifact confirmed) and the physical spectrum.

---

## Estimand

*Population:* S³ of radius ρ = 1.

*Intervention:* Dirac operator D built with left-invariant spin connection
  ω_ij = ε_{ijk} σ^k (Nomizu formula, G2-verified).

*Comparator:* Hopf-frame Dirac operator (gives same spectrum by frame independence;
  numerically confirmed by E0 harness).

*Endpoint:* Spectrum of D, i.e., set of eigenvalues λ satisfying Dψ = λψ.

*Summary measure:* Whether eigenvalues match ±(n + 3/2) for n = 0, 1, 2, …

*MCID:* Any eigenvalue deviating from ±(n + 3/2) by more than symbolic zero
  (exact sympy check) or |Δ| > 1e-6 (numerical E0 control) counts as FAIL.

---

## Verification Plan (two independent checks)

### C1 — Lichnerowicz / Casimir algebra (sympy)

Verify the identity:
```
(l + 3/2)² = (l+1)(l+2) + 3/2
```
symbolically for general l. This is a one-line algebraic check; if it holds,
the Dirac spectrum ±√(eigenvalue of D²) = ±(l+3/2) follows.

Rationale: the spinor Laplacian eigenvalues (l+1)(l+2) are the Casimir values
for the spin-1/2 representation on S³ (arXiv:1103.4097, Section 2); R/4 = 6/4 = 3/2.

### C2 — Nomizu connection → no-trig Dirac (sympy)

Show that the invariant-frame Dirac operator:
```
D = i γ^a (∂_a + ½ ε_{abc} γ^b γ^c / 2)
```
has constant (non-trigonometric) coefficients when written in the σ-basis, and that
its square produces the Lichnerowicz term + 3/2 using the su(2) algebra
{γ^a, γ^b} = 2δ^{ab} and [γ^a, γ^b] = 2i ε^{abc} γ_c (Clifford on R³).

This is a 2×2 matrix computation in sympy (two-spinor representation).

### C3 — E0 positive control (numerical, already existing)

Run `discrete_radial_dirac_proxy.run_e0(n_grid=4000)` and confirm:
- First positive eigenvalue ≈ 1.5 (= 3/2, n=0)
- Second positive eigenvalue ≈ 2.5 (= 5/2, n=1)
- Third positive eigenvalue ≈ 3.5 (= 7/2, n=2)

This test already passes (E0 gate PASS in v0.2.0 pivot). Used here as control only,
not new evidence.

---

## Pre-registered Verdict Rules

```
PASS (invariant-frame Dirac consistent with known spectrum):
  C1: (l+3/2)² = (l+1)(l+2) + 3/2 [exact, expand + simplify = 0]
  AND C2: invariant-frame D² = Casimir + 3/2 [exact, no trig, constant coefficients]
  AND C3: E0 harness eigenvalues match ±(n+3/2) within 1e-6 [already PASS]
  → Finding: "invariant-frame Dirac is spectrally consistent; cot(2α) absence in
    invariant frame has no spectral consequence"

PARTIAL (C1+C3 pass, C2 ambiguous):
  Algebraic identity holds and E0 numerical check passes, but C2 matrix computation
  cannot be fully simplified → record as CONSISTENT_NUMERICALLY_UNVERIFIED_ALGEBRAICALLY

FAIL (spectrum mismatch):
  C1 fails → claim kills immediately (arithmetic error in pre-registration)
  OR C3 fails → E0 harness broken; investigate before G3
  → Record in null_results/; do NOT proceed to G3

BLOCKED:
  C2 requires su(2) Clifford computation that sympy cannot complete in reasonable time
  → Use numerical C3 only; mark C2 as NEEDS_MANUAL_DERIVATION
```

---

## Controls

**Positive control:** E0 harness (C3 above) — already PASS, spectrum confirmed
  numerically. This is independent of invariant-frame algebra.

**Negative control:** Set spin connection ω = 0 (free flat Dirac in S³ coordinates).
  Should give WRONG spectrum (shifted by R/4 = 3/2 term missing).
  If this negative control also "passes" → test is degenerate.

**Convention pin:** Same ρ=1, same gamma matrix convention as G2
  (`{γ^a, γ^b} = 2δ^{ab}`, Euclidean signature).

---

## Sensitivity Checks

1. **Radius ρ ≠ 1:** spectrum becomes ±(n + 3/2)/ρ. Verify Lichnerowicz identity
   holds with R = 6/ρ².
2. **Sign of ε_{ijk}:** flip orientation; spectrum unchanged (eigenvalues come in ±
   pairs regardless of orientation).

---

## What This Does NOT Mean (pre-declared)

1. Does NOT mean λ is fixed — G1 is about the Dirac spectrum, not coupling constants.
2. Does NOT mean tom_ansatz = full mode — eigenspinor geometry (item 40) is separate.
3. Does NOT mean S³×S¹ problem is solved.
4. Does NOT select spin structure (m∈ℤ vs m∈ℤ+1/2).
5. Does NOT prove the invariant frame is "correct" for Tom's problem — it shows
   frame-independence of the spectrum, which is expected.
6. PASS here does NOT trigger G3 automatically — G3 requires a separate decision.

---

## Source Grounding

- Camporesi-Higuchi gr-qc/9505009, eq. 3.28: S^N Dirac spectrum ±(l + N/2), l≥0.
- arXiv:1103.4097, Section 2: degeneracy formula and Casimir values on S³.
- Lichnerowicz formula: standard spinor geometry (Lawson-Michelsohn, Spin Geometry).
- G2 provenance: `experiments/20260611-lambda-b5-cot-frame-artifact/` — Nomizu
  connection ε_{ijk} confirmed VERIFIED-sympy 2026-06-11.

---

## Files to Create (implementation not started)

```
experiments/20260611-lambda-b5-g1-invariant-frame-dirac/
  claim_lambda_b5_g1.md              ← this file (pre-registration)
  evidence_sympy_g1_dirac_spectrum.py  ← sympy C1+C2; calls E0 for C3
  g1_invariant_frame_dirac_report.md   ← written AFTER code runs
  results.json                         ← written by evidence script
```

**Rule:** `g1_invariant_frame_dirac_report.md` and `results.json` do NOT exist
until the evidence script runs.

---

**Fence:** lambda = FREE_COUPLING_PARAMETER; runtime = research_only;
promotion = NONE; safe_for_runtime = False.
Nothing written to Tom until he replies to 2026-06-09 message.
