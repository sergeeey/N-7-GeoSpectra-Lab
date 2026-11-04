# C235 Decision -- Sector classification of S^3 harmonics (Q2)

**Date:** 2026-11-03

## Result

Exact sympy (rank/nullity of joint Casimir systems), 13 asserted checks and 3 self-controls, exit 0 (`run_output_sector_classification.txt`).

Scalars (harmonic degree d, s = d/2): sectors (j_L, j_R) = (s, s), dimension (2s+1)^2: 1, 4, 9, 16 for d = 0..3 (total 30). The d = 1 sector is the (1/2,1/2) multiplet of TOM-CERT-01.

C^2-valued fields, left-invariant frame (spin index rotates with the right action): sectors (j_L, k) with total right spin k:

| j_L | k | dim | D0 |
|---|---|---|---|
| 0 | 1/2 | 2 | 0 |
| 1/2 | 1 | 6 | -1 |
| 1/2 | 0 | 2 | 3 |
| 1 | 3/2 | 12 | -2 |
| 1 | 1/2 | 6 | 4 |
| 3/2 | 2 | 20 | -3 |
| 3/2 | 1 | 12 | 5 |

In general (s, s+1/2): (2s+1)(2s+2) states, D0 = -2s; (s, s-1/2): (2s+1)(2s) states, D0 = 2s+2. Total 60 = 2 x (1+4+9+16). D0 commutes with the left SU(2) and with the total right SU(2) (exact). The left action does not touch the spin index; adding it (Y + T) gives a different table (self-control caught).

Other trivialisation: with the right-invariant frame (D0' = -i sum sigma_a Y_a) the roles are mirrored: sectors (j_L, j_R) = (k, s) with the same dimensions, and D0' = -D0 on the mirrored sector (inversion g -> g^-1 maps X_a to -Y_a). So WHICH SU(2) carries the spin is a choice of trivialisation, not a property of the manifold.

## Representation-level facts (exact, to degree 3; all degrees: Peter-Weyl, standard)

1. Scalar sectors are (s, s): j_L - j_R = 0.
2. Spinor sectors have j_L - k = -+1/2: half-integer.
3. D0 is a function of (s, k) only: -2s on k = s+1/2, 2s+2 on k = s-1/2.
4. The side that carries the spin index is fixed by the trivialisation (left- or right-invariant frame), with the mirror table above.

## Interpretation-level statements (NOT established here)

- "j_L - j_R half-integer = fermion, integer = boson": a spin-statistics reading of a representation label, the correspondent's own phrase is only "integer quantum numbers, effectively bosonic".
- "SU(2)_L gives the left-handed weak interaction": his statement; here j_L is simply the label of the left translation.
- which sector would be a quark, a neutrino, or a meson: nothing in this computation says.

## Caveat

Degree <= 3 by exact linear algebra on a 60-dimensional space; the pattern for larger degree is the Peter-Weyl theorem. The asymmetry between L and R is a consequence of the frame in C227's definition of D0.

Ledger: C235_S3_HARMONIC_SECTORS_SCALARS_S_S_C2_FIELDS_JL_K_D0_DEPENDS_ON_S_K_SPIN_SIDE_IS_A_TRIVIALISATION_CHOICE
Follow-ups: none
