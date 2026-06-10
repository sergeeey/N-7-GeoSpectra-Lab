# AV-2 E2 — Pre-registered Claim: Angular Singlet Check

**Gate:** AV2-E2
**Date pre-registered:** 2026-06-10 (written BEFORE av2_e2_angular_singlet.py)
**Question type:** [x] descriptive  [ ] predictive  [ ] causal
**Precondition:** AV-2 E1 STRONG_PASS (confirmed 2026-06-10)

---

## Natural Language Statement

We check whether the bilinear φ_{0,0}·g_{0,0} — the radial cross-term selected by E1
— has a nonzero projection onto the J=0 (SO(4) singlet) sector of the C-H eigenspinor
bilinear algebra on S³. A nonzero singlet projection is required for the reconstruction
to be interpretable as a scalar density (not merely a formal fit).

---

## Estimand

- **Population:** The n=l=0 Camporesi-Higuchi eigenspinor on S³ (Hopf coordinates).
- **Intervention:** None — this is a descriptive check.
- **Comparator:** The threshold ⟨0,0|1/2,+1/2;1/2,-1/2⟩ ≠ 0 vs. = 0.
- **Endpoint:** The SU(2) Clebsch-Gordan coefficient
    C = ⟨j=0, m=0 | j₁=1/2, m₁=+1/2; j₂=1/2, m₂=-1/2⟩
  and its squared magnitude C².
- **MCID:** C² > 0 (any nonzero projection suffices for singlet pairing to exist).

---

## Background

The n=l=0 C-H eigenspinor on S³ carries the SU(2)_L × SU(2)_R representation (1/2, 0):
  - j_L = 1/2: two states m_L = +1/2 (upper component, radial function φ_{0,0})
                             and m_L = −1/2 (lower component, radial function g_{0,0})
  - j_R = 0: singlet under SU(2)_R

The bilinear φ_{0,0}·g_{0,0} corresponds to the m_L=(+1/2, −1/2) cross term
in the tensor product (1/2)⊗(1/2) = (0)⊕(1).

By SU(2) Clebsch-Gordan theory, the m=(+1/2,−1/2) state is:
  |+1/2, −1/2⟩ = (1/√2)(|0,0⟩ + |1,0⟩)

So it contains BOTH the J=0 singlet (|0,0⟩) and the J=1 triplet (|1,0⟩) components.
The singlet component C = ⟨0,0|1/2,+1/2;1/2,-1/2⟩ should equal ±1/√2.

---

## Pre-registered Pass/Fail Criteria

| Verdict | Condition | item40 consequence |
|---|---|---|
| **PASS** | C² > 0 (sympy exact, AND numerical cross-check) | → RADIAL+ANGULAR_BILINEAR_SUPPORTED |
| **FAIL** | C = 0 (singlet projection exactly zero) | → FORMAL_FIT_ONLY (E1 fit is formal only) |

C = 0 is algebraically impossible for (1/2,+1/2;1/2,-1/2|0,0) by CG theory,
but the test exists to confirm the n=l=0 mode DOES carry j_L=1/2, not j_L=0.

---

## Kill Condition

If sympy returns C = 0 for ⟨0,0|1/2,+1/2;1/2,-1/2⟩:
→ The n=l=0 mode is in the j_L=0 sector, meaning φ and g are not SU(2) partners.
→ The cross bilinear has no singlet component.
→ FAIL: record in null_results/. item40 → FORMAL_FIT_ONLY.

---

## What This Does NOT Mean (pre-declared)

1. PASS ≠ "Tom's ansatz solved" — angular singlet exists but physical interpretation not proven.
2. PASS ≠ physical promotion — λ = FREE_COUPLING_PARAMETER remains.
3. PASS ≠ full S³×S¹ compatibility — that requires BG-H1 separately.
4. The singlet component C² = 1/2 (not 1) — the cross term is only 50% in the singlet;
   the other 50% is in the triplet. This is fine for scalar density purposes (singlet ≠ 0).
5. No claim about higher modes (n≥1): this check is for n=l=0 only.

---

## Sensitivity

1. Cross-check CG coefficient numerically (scipy.special or manual Racah formula).
2. Verify sign convention: ⟨0,0|1/2,-1/2;1/2,+1/2⟩ = −⟨0,0|1/2,+1/2;1/2,-1/2⟩ (antisymmetry).
3. Verify the TRIPLET component is also present (C²_triplet > 0) to confirm the check
   is nontrivial (not a trivially-all-singlet case).
