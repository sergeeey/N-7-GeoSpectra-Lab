# C236 decision: PROMOTE as exact computation (scope: degrees 0..3)

Script: fourth_harmonic_diagonal_singlet.py, log run_output_c236.txt (exit 0, all checks PASS, 4 self-controls CAUGHT).

Result [VERIFIED-tool, exact sympy]:
- Degree 1: Casimir of SU(2)_diag has eigenvalues 0 (once) and 2 (three times). Singlet = a = ½ tr g = Re x0; triplet = (b, c, d).
- Scalar sectors (s,s): exactly one diagonal singlet for degrees 0..3; it is proportional to r^n U_n(a/r): 1, 2a, 3a² − b² − c² − d², 4a³ − 4a(b²+c²+d²) (the SU(2) characters, i.e. class functions).
- C²-valued fields, degrees 0..3: Dtot (left + total right) singlets = 0; Dorb (orbital only, spin untouched) singlets = 2.
- D0 (C227 form, factor 2 on Y because C227 uses T = −iσ): spectra {0:2}, {−1:6, 3:2}, {−2:12, 4:6}, {−3:20, 5:12} as in C235; commutes with X_k and K_k.

Representation-level facts: the "extra" harmonic besides a triplet is the class function (character); a spinor-valued field has no Dtot singlet because j_L and the total right spin k differ by ½. The zero holds for EVERY degree, not only 0..3 (skeptic, tool-checked): -1 in SU(2) acts trivially by conjugation and as -1 on C^2, so no Dtot-invariant exists; likewise "Dorb = 2" is just the scalar singlet tensor C^2.

Interpretation-level, NOT established: "fourth harmonic = background = right-handed neutrino"; this would need Tom's definition. What the computation does show: if the background must be a diagonal singlet of this Dtot, it cannot sit in a C²-valued sector, so a spinor background would need a different invariance than Dtot. Conditional on the choice of diagonal.

Error caught on the way: first D0 run gave all eigenvalues halved; cause was the normalisation of T (½ in my script, none in C227); fixed in the script and documented in its docstring. Not a physics discrepancy.

Skeptic concerns: none run yet (same-session computation; second reader not applied).

## Skeptic review (2026-11-04, context-blind, independent rerun reproduces the log byte for byte)
- (1) 1 + 3 with singlet a = (1/2) tr g, (2) one diagonal singlet per (s,s) equal to r^n U_n(a/r), (4) D0 spectrum with the factor-2 normalisation (grep of C227 confirms T_a = -i sigma_a, no 1/2): CONFIRMED-REAL.
- (3) no Dtot singlet: CONFIRMED but trivial and conditional on the choice of diagonal. Skeptic probe: at degree 1, K = Y + S gives 2 singlets and X + S gives 2 singlets; X + Y + S and X + Y + conj(S) give 0. K is the symmetry D0 actually commutes with, so a spinor background needs K-invariance, not Dtot-invariance: Accepted. The reading "if the background must be a diagonal singlet of this Dtot" must not be taken as a statement about Tom's background.
- Self-controls are negations of positive checks: no independent evidence. Accepted.

Ledger: C236_FOURTH_HARMONIC_IS_THE_DIAGONAL_SINGLET_A_CHARACTER_NO_FULL_DIAGONAL_SINGLET_ON_C2_FIELDS
