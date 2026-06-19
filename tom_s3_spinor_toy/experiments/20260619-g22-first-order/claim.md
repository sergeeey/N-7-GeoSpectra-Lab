# G22 — Claim: NCG first-order condition — maximal compatible subalgebra

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:** The SM Yukawa D_F (from S³×S⁶ spinor geometry) satisfies the NCG first-order
condition [[D_F, a], J_F b J_F] = 0 for the color-B-L subalgebra SU(3) × U(1)_{B-L},
and FAILS for the electroweak subalgebra SU(2)_L × SU(2)_R.
The maximal subalgebra of the Pati-Salam gauge group compatible with D_F as an NCG
first-order operator is exactly SU(3) × U(1)_{B-L} — the unbroken symmetry of the SM vacuum.

## Method

For each generator G_k of a subalgebra, compute:
  max_{a,b} |[[D_F, G_a], J_F G_b J_F]|

where J_F is the charge conjugation permutation matrix (J_F² = I, from G18).
A subalgebra is "compatible" if the maximum is < 1e-8.

## Results (numerical, [VERIFIED-numpy, 2026-06-19])

| Subalgebra | Generators | max violation | Compatible? |
|---|---|---|---|
| SU(3) | 8 | 0.000 | YES (trivially: [D_F, C_k] = 0) |
| U(1)_{B-L} | 1 | 0.000 | YES (trivially: [D_F, BL] = 0) |
| SU(3) × U(1)_{B-L} | 9 | 0.000 | YES |
| SU(2)_L | 3 | 0.25000000 | NO |
| SU(2)_R | 3 | 0.25000000 | NO |
| Full Pati-Salam | 15 | 0.25000000 | NO |

**Exact violation value:** 0.25 = (1/2)² — a pure geometric factor.

### Why SU(3) × U(1)_{B-L} passes

D_F (SM Yukawa) connects states with the SAME S⁶ index but different S³ components.
Every YUKAWA_PAIR (i, j) has: same S⁶ mode, same SU(3) representation, same B-L charge.
Therefore [D_F, C_k] = 0 for all k, and [D_F, BL] = 0. Both first commutators vanish,
making [[D_F, a], J_F b J_F] = 0 trivially for all SU(3) × U(1)_{B-L} pairs.

### Why SU(2)_L and SU(2)_R fail

D_F maps ν_L → ν_R (with Y_ν) and e_L → e_R (with Y_e) separately.
The SU(2)_L generator J_1 mixes ν_L ↔ e_L, so [D_F, J_1] ≠ 0.
The violation propagates via the physical chain:

  ν_L (0) → [D_F, J_1] → e_R (24): value = −1/2 × Y_e = −0.5
  e_R (24) → J_F J_1 J_F → ν_R (16): value = +1/2

  [[D_F, J_1], J_F J_1 J_F]_{(0,16)} = (−0.5)(+0.5) = −0.25

This equals (generator norm)² = (1/2)² = 0.25. Linear in Y, exact for Y=1.

### Relation to CCM

CCM 2006 (Connes-Chamseddine-Marcolli) proves the first-order condition holds for
A_F = ℂ ⊕ ℍ ⊕ M₃(ℂ) — a SMALLER algebra than Pati-Salam, where ℍ acts as a full
quaternion only on left-handed fields, and as a scalar on right-handed fields.

We approach from the OPPOSITE direction: starting from the larger Pati-Salam algebra
and finding it FAILS. The failure localizes to SU(2)_L and SU(2)_R — exactly the
electroweak generators that are broken by the Yukawa/Higgs mechanism.

**Physical interpretation:** The NCG first-order condition selects the maximal subalgebra
compatible with D_F. That maximal subalgebra = SU(3) × U(1)_{B-L} = the unbroken symmetry
after electroweak spontaneous symmetry breaking. This is not an axiom imposed on D_F;
it emerges from the spinor geometry of S³×S⁶.

## Gates summary [VERIFIED-numpy, 2026-06-19]

| Gate | Assertion | Result |
|---|---|---|
| F1 | SU(3) FO violation < 1e-8 (color singlet) | PASS |
| F2 | U(1)_{B-L} FO violation < 1e-8 (B-L preserved) | PASS |
| F3 | SU(2)_L violation = 0.25 exactly | PASS |
| F4 | SU(2)_R violation = 0.25 exactly | PASS |
| F5 | J_F² = I (right-action formula valid) | PASS |

## What this does NOT mean

1. Does NOT prove SM derivation — this is a descriptive result about which subalgebra
   is compatible with the first-order condition, not a derivation of the SM gauge group.
2. Does NOT reproduce CCM exactly — CCM uses a different representation of ℍ on H_F.
   The maximal compatible subalgebra in our setup (color × B-L) matches the UNBROKEN
   vacuum symmetry, not the full SM gauge symmetry.
3. Does NOT explain why SU(2)_L is gauged in the SM — only that D_F breaks it.
4. Does NOT apply to 3 generations — H_F = ℂ^{32} covers one generation only.
5. sm_derivation_claimed = False throughout.

**Status:** PASS_G22_FIRST_ORDER (5/5)
[VERIFIED-numpy, 2026-06-19, 19/19 tests green]
