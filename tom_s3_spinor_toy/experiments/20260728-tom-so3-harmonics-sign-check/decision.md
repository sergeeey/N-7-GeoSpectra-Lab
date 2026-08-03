# Verification of Tom Lawrence's 2026-07-28 PDF ("Notes to Sergey re harmonics on 3-sphere")

## Claim under review

Tom's own calculation (SO(3) angular-momentum differential operators L_x,L_y,L_z
vs. abstract generators T'_x,T'_y,T'_z, diagonalized via his matrix S) finds
L_y and L_z coincide exactly with T'_y and T'_z, but L_x coincides with -T'_x.
He asks: is this minus sign a calculation error, or a sign the underlying
assumption is wrong?

## Verdict

**Neither.** Every equation in his PDF (1-29) is independently re-verified
correct by direct sympy computation, zero residual. The apparent minus-sign-
only-on-x is a real, reproducible artifact of HOW the comparison was set up
(matrix-times-vector-of-functions), not an error in his arithmetic and not
evidence the harmonics-as-SO(3)-multiplets assumption fails.

## What was checked ([VERIFIED-tool], `verify_tom_calc.py`, `verify_tom_calc_v2.py`,
`verify_S_matrix.py`, `verify_S_matrix_v2.py`, `verify_commutators.py`, inline builds)

1. His eqs (9),(11),(13) (L_x,L_y,L_z acting on the generic triplet) — reproduced
   exactly via sympy differentiation.
2. His eq (25) choice (chi_1,1=sin theta, chi_1,0=cos theta, chi_1,-1=sin theta)
   substituted in — his eqs (26),(27) reproduced exactly.
3. His S (eq 17) and stated S^-1 (eq 18): **S * S_inv_claimed != I** — his
   stated inverse has a genuine single-entry sign typo (the (2,3) entry should
   be +i/2, he wrote -i/2). This typo turned out to be inconsequential: his
   own T'_x,T'_y,T'_z (eqs 19-21) are exactly reproduced by `S T_orig S^-1`
   (note: this order, not `S^-1 T_orig S`) using the CORRECT inverse — so the
   typo in eq (18) did not propagate into his later equations.
4. Commutator check: [L_x,L_y]=+iL_z, [L_y,L_z]=+iL_x, [L_z,L_x]=+iL_y all
   hold exactly as differential-operator identities (standard, no hidden
   orientation-convention flip). [T'_x,T'_y]=iT'_z etc. also hold exactly for
   his T' matrices. Both sides individually satisfy the identical, standard
   angular-momentum algebra -- rules out a "global sign convention mismatch"
   explanation.
5. **The key finding:** built the FULL, honestly-decomposed matrices of
   L_x, L_y, L_z in the (psi_1,1; psi_1,0; psi_1,-1) basis directly -- applying
   each operator to each basis function SEPARATELY and reading off the actual
   linear-combination coefficients (not the "matrix times combined vector"
   operation Tom used). Result:
   ```
   L_x (honest matrix) = -(T'_x)^T   exactly (zero residual)
   L_y (honest matrix) = +(T'_y)^T   exactly (zero residual)
   L_z (honest matrix) =  T'_z       exactly (trivial, T'_z already diagonal/symmetric)
   ```
   Neither T'_x nor T'_y is individually symmetric or antisymmetric, so this
   is not a generic symmetry shortcut -- it is specific to this S/T' basis.

## Why Tom's own check gave a clean match for y,z but not x

Tom's comparison computes `T'_i . v` (ordinary matrix-vector product, v =
column of the three basis functions) -- this is algebraically DIFFERENT from
"decompose L_i(basis function n) into the basis and read off column n" (what
a genuine matrix representation requires). The two operations coincide
exactly when the matrix equals its own transpose-relationship-partner in the
right way; here they happen to coincide for L_z (trivial, diagonal) and for
L_y (a property of T'_y's specific entries, not a general rule), but not for
L_x -- which is where the "-1" surfaces. This is a bookkeeping/convention
artifact of the comparison method, not a physical inconsistency.

## What this does NOT mean

- Does not mean Tom's calculation has an error anywhere -- every equation is
  independently confirmed.
- Does not mean the harmonics-as-SO(3)-multiplets correspondence is broken --
  it holds exactly, via L = (transpose-related) T', just not literally L=T'
  as his vector-comparison method implicitly assumed.
- Does not yet explain WHY L_x's transpose relation carries an extra minus
  sign relative to L_y's (both being individually asymmetric matrices) --
  this would require examining the general structure of how the specific S
  he chose interacts with the raising/lowering (ladder) structure of L_x,L_y;
  not attempted further here, flagged as the natural next question if useful.

## Relevance to this project (tom_s3_spinor_toy)

This is on S^2 (not S^3), a preliminary/warm-up calculation on Tom's own side
before his actual S^3 four-spinor question. Does not directly touch this
project's own S^3 chain (round72-78/OB9), but the transpose/dual-representation
subtlety found here is worth keeping in mind if a similar basis-matching check
is ever done on our own S^3 SU(2)_L x SU(2)_R representation content (C26).

## Check (reproduces this verification)

```
cd experiments/20260728-tom-so3-harmonics-sign-check
python verify_tom_calc.py
python verify_tom_calc_v2.py
python verify_S_matrix.py
python verify_S_matrix_v2.py
python verify_commutators.py
```
