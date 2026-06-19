# G25 Claim: Yukawa Texture — S³×S⁶ Predicts 4 Parameters

**Date:** 2026-06-19
**Experiment:** 20260619-g25-yukawa-texture

## Question type
[x] descriptive — "How many independent Yukawa parameters does S³×S⁶ geometry allow?"
[ ] predictive
[ ] causal

## Claim

The product geometry S³×S⁶ constrains the Dirac operator D_F to have exactly
**4 independent Yukawa parameters** {Y_ν, Y_e, Y_u, Y_d} via a two-step cascade:

  **Naive bound:** L→R chirality block = 16×16 = **256 entries**

  **Step 1 — S⁶-diagonal (product geometry):**
  D_F connects same S⁶ mode k%8 across S³ components.
  Yukawa pairs (i,j) with i%8 ≠ j%8 are geometrically forbidden.
  → Reduces to **8 modes × 2 S³ pairings = 16 entries**

  **Step 2 — |Q|-uniqueness (CPT symmetry):**
  [D_F, Q_32] = 0 (T4 in G18) fixes Q[i] = Q[j] per Yukawa pair.
  [D_F, J_F]  = 0 (T7 in G18) forces CPT conjugates to share coupling.
  CPT maps Q → −Q, so coupling is a function of |Q| alone.
  4 distinct |Q| values: {0, 1, 2/3, 1/3} → **4 free parameters**

  The 4 parameters are in bijection with the 4 SM fermion species:

  | |Q| | Parameter | Fermion         |
  |----|-----------|-----------------|
  |  0 | Y_ν       | neutrino + ν̄   |
  |  1 | Y_e       | electron + e⁺  |
  | 2/3| Y_u       | up quark + ū   |
  | 1/3| Y_d       | down quark + d̄ |

## Structure confirmed

**S³ Hopf pairings:** {(0,2), (1,3)} — the two L↔R connections from SU(2)_L×SU(2)_R.
**S⁶ singlet modes:** {0, 7} (C₂=0 from Spin(7)→G₂→SU(3) branching).
**S⁶ triplet modes:** {1,2,3,4,5,6} (C₂>0, 3+3̄ of SU(3)).
Each S⁶ mode appears in exactly **2 Yukawa pairs** (one per S³ Hopf pairing).

## Verification (numerical — all [VERIFIED-pytest])

| Gate | Check | Result |
|------|-------|--------|
| P1 | All 16 Yukawa pairs have i%8 = j%8 (S⁶-diagonal) | PASS |
| P2 | All S³ pairings ∈ {(0,2), (1,3)} (Hopf adjacency) | PASS |
| P3 | Every S⁶ mode appears in exactly 2 Yukawa pairs | PASS |
| P4 | Coupling uniquely determined by |Q|, 4 distinct |Q| values | PASS |
| P5 | Exactly 4 Yukawa symbols = {Y_ν, Y_e, Y_u, Y_d} | PASS |
| P6 | Cascade 256 → 16 → 4 confirmed numerically | PASS |

## What this does NOT mean

1. Does NOT fix the numerical values of Y_ν, Y_e, Y_u, Y_d — they remain free parameters
2. Does NOT explain the hierarchy m_e ≪ m_u ≪ m_t — only the parameter count
3. Does NOT claim S³×S⁶ is unique — other geometries with 4-species structure may exist
4. Does NOT address mixing angles (CKM, PMNS) — those require multi-generation extension
5. Does NOT derive the SM Lagrangian — only the Yukawa sector DOF count

## Decision

**PROMOTE** — G25 passes all 6 gates.

Physical significance: the S³×S⁶ product geometry predicts the correct number of
independent Yukawa coupling constants for one SM generation from first principles.
The 256-entry freedom of an unconstrained L→R operator is reduced 64-fold to 4
by geometry (S⁶-diagonal) and CPT symmetry (|Q|-uniqueness). The 4 parameters
correspond exactly to the 4 SM fermion species (ν, e, u, d).

This closes **Угол 5 "Предсказание"** of the CSDR 5-angle plan.

sm_derivation_claimed = False.
λ = FREE_COUPLING_PARAMETER.

24 tests, 6/6 gates PASS.
