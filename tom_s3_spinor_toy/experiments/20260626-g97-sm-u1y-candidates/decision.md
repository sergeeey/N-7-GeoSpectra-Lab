# G97 Decision — U(1)_Y candidates from SO(4) x SO(7)

**Verdict: PARTIAL — T3_R identified; B-L generator absent from Iso(S3xS6)**

## Claim

Hypercharge U(1)_Y can be identified from the Cartan subalgebra of SO(4) x SO(7).

## Result

Pati-Salam formula: Y = T3_R + (B-L)/2

| Field | Y_SM | T3_R | B-L | Y = T3_R + BL/2 | Match |
|---|---|---|---|---|---|
| u_L | +1/6 | 0 | +1/3 | +1/6 | ALGEBRAIC |
| d_L | +1/6 | 0 | +1/3 | +1/6 | ALGEBRAIC |
| u_R | +2/3 | +2/3 | +1/3 | +5/6 | FAIL (B-L mismatch) |
| e_L | -1/2 | 0 | -1 | -1/2 | ALGEBRAIC |
| nu_L | -1/2 | 0 | -1 | -1/2 | ALGEBRAIC |
| e_R | -1 | -1 | -1 | -3/2 | FAIL (B-L mismatch) |

The Pati-Salam formula works IF B-L is assigned correctly. The failure is NOT
in the formula itself — it's that the T3_R values in the B-L decomposition
for right-handed quarks require SU(4) ⊃ SU(3) which is NOT in SO(4) x SO(7).

## Coverage summary

COVERED (algebraically verified):
- SU(3)_color: SU(3) subset G2 subset SO(7) [G96 VERIFIED]
- SU(2)_L: J+ sector of SO(4) = Iso(S3) [G95 VERIFIED]
- SU(2)_R: J- sector of SO(4) = Iso(S3) [G95 VERIFIED]
- T3_R: Cartan of SU(2)_R [G95 VERIFIED]

OPEN (needs Tom's Part 4/5):
- B-L generator: NOT in Iso(S3xS6) = SO(4)xSO(7)
  - SO(4) rank = 2: only T3_L, T3_R
  - SO(7) via G2: only H3, H8 from SU(3) Cartan
  - No SU(4) = no natural B-L generator
- B-L route: Pati-Salam needs SU(2)_R x SU(4) ⊃ SM
  - SU(4) has rank 3; our algebra has no SU(4) anywhere
  - Possible source: field content of D=13 SUGRA (not just isometry group)
  - Tom's spinor ansatz may provide U(1)_BL from fermion zero mode charges

## Physical interpretation

The gauge group from isometries alone is SU(3) x SU(2)_L x SU(2)_R (rank 4, 14 generators).
This is the Pati-Salam gauge group WITHOUT the U(1)_BL factor.
Full Pati-Salam = SU(2)_L x SU(2)_R x SU(4) requires SU(4), not present in geometry.

Two routes to U(1)_Y:
1. SU(2)_R breaking: if SU(2)_R breaks to U(1)_R = U(1)_T3R, then
   Y = T3_R + (B-L)/2 requires B-L from somewhere else
2. Direct from field content: fermion zero mode charges under SO(7) generators
   may produce effective B-L (Tom's Part 4/5 needed to determine this)

## What this does NOT mean

1. Does NOT mean SM hypercharges are unattainable — they may come from field
   content (fermions, fluxes), not purely from isometry group
2. Does NOT invalidate G95/G96 — SU(3) x SU(2) is solid, only U(1)_Y is open
3. Does NOT require additional compactification dimensions beyond D=13
