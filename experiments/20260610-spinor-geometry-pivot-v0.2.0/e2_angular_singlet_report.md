# AV-2 E2 — Angular Singlet Check Report

**Gate:** AV2-E2
**Date:** 2026-06-10
**Verdict:** ✅ PASS
**item40 upgraded to:** `RADIAL + ANGULAR_BILINEAR_SUPPORTED`
**Precondition:** AV-2 E1 STRONG_PASS (confirmed 2026-06-10)

---

## Result

| Quantity | Value |
|---|---|
| CG singlet (exact) | `sqrt(2)/2` |
| CG singlet (float) | `0.70711...` = 1/√2 |
| C² (singlet weight) | **0.5** |
| C² (triplet weight) | 0.5 |
| Singlet + triplet | 1.0 (completeness ✓) |
| Antisymmetry verified | ✅ |
| Verdict | **PASS** |

---

## What Was Checked

The n=l=0 C-H eigenspinor on S³ carries the SU(2)_L × SU(2)_R representation (1/2, 0):
- Upper component φ_{0,0}: m_L = +1/2
- Lower component g_{0,0}: m_L = −1/2
- Both in j_L = 1/2

The cross bilinear φ·g corresponds to the m=(+1/2, −1/2) state in the tensor product
(1/2) ⊗ (1/2) = (0) ⊕ (1).

By Clebsch-Gordan theory (Condon-Shortley convention):
```
<j=0, m=0 | j₁=1/2, m₁=+1/2; j₂=1/2, m₂=-1/2> = sqrt(2)/2 ≠ 0  ✓
```

The singlet CG coefficient is nonzero, confirming the cross bilinear φ·g
has a nonzero projection onto the J=0 sector.

---

## Interpretation

The result C² = 0.5 means:
- 50% of the bilinear φ·g is in the J=0 (singlet) sector → CAN form a scalar density
- 50% is in the J=1 (triplet, m=0) sector → also present, but does not prevent singlet pairing

The antisymmetry check verifies the Condon-Shortley sign convention:
```
<0,0 | 1/2,-1/2; 1/2,+1/2> = -sqrt(2)/2 = -C  ✓
```

---

## Item 40 Status Update

| Previous (after E1) | New (after E2) |
|---|---|
| `RADIAL + TWO_COMPONENT_RECONSTRUCTION_SUPPORTED` | `RADIAL + ANGULAR_BILINEAR_SUPPORTED` |

---

## What This Does NOT Mean

1. NOT "Tom's ansatz solved" — this only checks that a singlet pairing exists for the
   specific bilinear selected by E1. Full eq.49 structure is not verified.
2. NOT "full angular verification" — only the lowest mode n=l=0 is checked.
3. NOT physical promotion — λ = FREE_COUPLING_PARAMETER.
4. NOT safe_for_runtime.
5. C² = 0.5 (not 1): the bilinear is NOT a pure singlet. The triplet component is
   also present (C²_triplet = 0.5). This is a fundamental limitation.
6. Nothing about S³×S¹ / BG-H1 — that is a separate track.

---

## Gate Chain Completed (AV-2)

| Gate | Result | Key quantity |
|---|---|---|
| G0 | ✅ PASS | C-H source trace: 18 eqs VERIFIED_FROM_PDF |
| G1 | ✅ PASS | 2-component system: eq 3.28 ≤2.3e-15, eq 3.38 ≤6e-16 |
| G2 | ✅ PASS | g_l0 exponent=−0.096≈0, mixed_l0=0.928≈cos¹ |
| E1 | ✅ STRONG_PASS | 1 term: φ_{0,0}·g_{0,0}=cosα·sinα=sin(2α)/2 (exact) |
| E2 | ✅ PASS | CG singlet = √2/2, C²=0.5 > 0 |

**AV-2 full gate chain: PASS** [VERIFIED-pytest 2026-06-10, 218 tests total]

**item40 final:** `RADIAL + ANGULAR_BILINEAR_SUPPORTED`

---

**Code:** `tom_s3_spinor_toy/av2_e2_angular_singlet.py`
**Tests:** 21 tests, all passing [VERIFIED-pytest 2026-06-10]
