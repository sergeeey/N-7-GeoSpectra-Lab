# AV-2 E1 — Sparse Reconstruction Report

**Gate:** AV2-E1
**Date:** 2026-06-10
**Verdict:** ✅ STRONG_PASS
**item40 upgraded to:** `RADIAL + TWO_COMPONENT_RECONSTRUCTION_SUPPORTED`
**Precondition:** AV-2 G2 PASS (confirmed 2026-06-10)

---

## Result

| Metric | Value |
|--------|-------|
| Terms used | **1** |
| Pre-registered threshold (STRONG_PASS) | ≤ 5 terms |
| Residual (unweighted L2) | **0.0000%** |
| Residual (sin²α-weighted) | **0.0000%** |
| Selected atom | `phi_g(0,0)` = φ_{0,0}·g_{0,0} |
| Dictionary size | 56 atoms |

---

## Analytical Explanation (why 0% residual is NOT validation theater)

The 0% residual follows analytically from Camporesi-Higuchi eqs 3.25/3.27
[VERIFIED_FROM_PDF in AV-2 G0; numerical residual ≤ 2.22e-16 = machine epsilon]:

**From eq 3.25** (n=l=0, Jacobi P_0 = 1 for any parameters):
```
φ_{0,0}(α) = cos^{l+1}α · sin^l α · P^{0.5, 1.5}_0(cos 2α)  |_{l=0}
           = cos¹α · sin⁰α · 1
           = cos(α)
```

**From eq 3.27** (n=l=0, Jacobi P_0 = 1):
```
g_{0,0}(α) = cos^l α · sin^{l+1} α · P^{1.5, 0.5}_0(cos 2α)  |_{l=0}
           = cos⁰α · sin¹α · 1
           = sin(α)
```

**Product:**
```
φ_{0,0}(α) · g_{0,0}(α) = cos(α) · sin(α) = sin(2α)/2
```

**Target:** `sin(2α) = 2 · [φ_{0,0}(α) · g_{0,0}(α)]`

The target is EXACTLY representable as a scalar multiple of one C-H bilinear atom.
This is a mathematical identity, not a fitting artifact.

**Verification** [VERIFIED-python 2026-06-10]:
```
max|phi_00 - cos(a)|   = 0.00e+00  (machine exact)
max|g_00 - sin(a)|     = 0.00e+00  (machine exact)
max|2*phi00*g00 - sin(2a)| = 2.22e-16  (= double machine epsilon)
```

---

## Skeptic Response (why this is not validation theater)

**Skeptic trigger fired:** F1=1.000, 0% residual, 1 term — all round numbers.

**Why not synthetic / circular:**

1. The dictionary was built from C-H eigenfunction formulas (G0 source-traced from PDF).
   The atom `phi_g(0,0)` = φ_{0,0}·g_{0,0} was included because G2 showed it has
   boundary exponent ≈ cos¹ — MATCHING the target before we knew it was exact.

2. The pre-registration specified the mode set and algorithm BEFORE running E1.
   We did not know a priori that a 1-term solution existed —
   the pre-registration allowed up to 5 terms (STRONG_PASS) or 8 terms (WEAK_PASS).

3. The 0% residual is provable analytically from C-H eqs 3.25/3.27 + Jacobi P_0 = 1.
   It is a mathematical identity, not a numerical coincidence.

4. The AV-1c' dictionary (phi-only) gave 12.38% residual — if E1 were validation
   theater we would have "fixed" AV-1c' to get 0%, not built a separate gate.

**Evidence level:** [VERIFIED-python + VERIFIED_FROM_PDF (C-H eq 3.25/3.27)]

---

## Scientific Meaning

The AV-1c′ obstruction (12.38% residual, dense series needed) was an artifact
of projecting out the partner component g_{nl}.

The full two-component Camporesi-Higuchi structure on S³ provides:
- The radial function pair (φ_{0,0}, g_{0,0}) = (cos α, sin α)
- Their bilinear product = cos α · sin α = sin(2α)/2
- This EXACTLY equals the target eq.49 radial layer (up to a scalar)

**Interpretation:**
Tom's eq. 49 expansion ∝ sin(2α) is the bilinear density
φ_{0,0}(α) · g_{0,0}(α) — the lowest two-component C-H spinor bilinear on S³.

---

## Item 40 Status Update

| Previous (after G2) | New (after E1) |
|---------------------|----------------|
| `RADIAL + TWO_COMPONENT_BOUNDARY_MECHANISM_SUPPORTED` | `RADIAL + TWO_COMPONENT_RECONSTRUCTION_SUPPORTED` |

**What this does NOT mean:**
1. NOT full angular verification — angular quantum numbers not checked (→ E2)
2. NOT "Tom's ansatz solved" — angular singlet structure not verified yet
3. NOT H-T1 promoted — H-T1 remains in null_results/
4. NOT physical λ fixed — λ = FREE_COUPLING_PARAMETER
5. NOT safe_for_runtime

---

## Next Gate: E2 — Angular Singlet Check

Pre-registered endpoint: verify the chosen bilinear φ_{0,0}·g_{0,0} can pair
to total-angular-momentum singlets (required for a scalar √||g||).

If E2 passes → item40 → `RADIAL+ANGULAR_BILINEAR_SUPPORTED`
If E2 fails → status = FORMAL_FIT_ONLY (reconstruction is formal, not eq-49-meaningful)

**Data:** `experiments/20260610-spinor-geometry-pivot-v0.2.0/`
**Code:** `tom_s3_spinor_toy/av2_e1_sparse_reconstruction.py`
