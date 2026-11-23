# Decision C249

**Verdict:** PROMOTE (descriptive mathematical identity on the round unit S^3); context-blind skeptic: CONFIRMED-REAL within the stated conventions (section below).

Ledger: C249_KOSMANN_HOPF_FRAME_ZERO_HALF_DOUBLET_IS_KILLING_SPINOR_PAIR_SCALAR_ANSATZ_HAS_NONE

## Result

In the Hopf frame E = (d_alpha, d_theta / sin alpha, d_thetat / cos alpha), with J_a = -i L_{N_a} and L the Kosmann derivative,

    psi_+ = e^{ i(theta - thetat)/2} ( cos(alpha/2), -i sin(alpha/2) ),
    psi_- = e^{-i(theta - thetat)/2} ( -i sin(alpha/2),  cos(alpha/2) ),

is a doublet (i_L, i_R) = (0, 1/2): J^L_a psi_+- = 0, J^R_3 psi_+- = +-1/2 psi_+-, J^R_- psi_+ = psi_-, J^R_+ psi_- = psi_+, J^R_- psi_- = 0. Both states satisfy D psi = -(3i/2) psi and nabla_X psi = -(i/2) X.psi (Killing spinors; |psi|^2 = 1 pointwise). The phase e^{+-i(theta - thetat)/2} is the one in the correspondent's ansatz (as quoted in the external summary); the profile is spinor-valued with half-angle entries, not one scalar function.

The total spinor term for N_1^+ (spin connection plus Kosmann term together, i.e. what the plain vector-field action drops) is

    C = (i/4) [ cos(theta - thetat) sigma_1 - sin(theta - thetat)/cos(alpha) sigma_2 - sin(theta - thetat)/sin(alpha) sigma_3 ],

with 1/sin alpha and 1/cos alpha, not cot(2 alpha). The boxed operator in the external text of 2026-11-24 is therefore not this term.

## Predictions vs outcome (claim.md written before the run)

| | prediction | outcome |
|---|---|---|
| P1 | one sign of the Kosmann term commutes with D; other sign and component-wise action do not | confirmed; residual 1.6e-14 vs 35 and 44. The sign that works is +1 in this code's index order; my pre-run guess was -1 (first log kept: `logs/run_kosmann_checks_first_run_presign.txt`) |
| P2 | correction vanishes for d_theta, d_thetat | confirmed exactly (simplified matrix identically zero) |
| P3 | Hopf-frame components of a smooth spinor are antiperiodic | the doublet's components flip sign under theta -> theta + 2 pi; the SO(3) winding of the frame itself was not computed. My remark of 2026-11-24 ("half-angle phases are not on S^3") holds for scalars only and is withdrawn for spinor components |
| P4 | a (0, 1/2) doublet exists and closes | confirmed; the 30 conditions vanish exactly (Weierstrass substitution), closure checks numeric about 1e-15 at 5 points; later seven of the eight closure conditions exact with symbolic angles, the eighth (J^R_- psi_+ = psi_-) numeric at 40 points (see Skeptic) |
| P5 | scalar system has only zero | confirmed: only A = 0 for the phase (1/2, -1/2) (exact solve in kosmann_doublet.py), and no non-zero solution at the other half-integer phases (rank scan, numeric, one alpha = 7/10); the correspondent's own equation cot^2(2 alpha) = -1 was not reproduced (slides not opened) |

## Controls

- Spin-connection sign: Clifford compatibility passes for +1 (1.9e-15), fails for -1 (15.2).
- Kosmann sign: commutes with D for +1 (1.6e-14), not for -1 (35.0); plain component-wise action does not commute (43.5).
- Bracket homomorphism [L_X, L_Y] = L_[X,Y]: 4.9e-15.
- Lowest weights (-1/2) admit no highest-weight solution (rank scan, smallest singular value about 1.7); a wrong eigenvalue (lambda + 1) fails.
- The plain (scalar) action on psi_+ is not annihilated by J^R_+ (1.07).

## Scripts and logs

`scripts/kosmann_geometry.py`, `kosmann_checks.py` (ALL_PASS, exit 0), `kosmann_rank_scan.py` (diagnostic, numeric, print-only: its evidence is the printed singular values, not the exit code); `scripts/skeptic/attack.py`, `attack2.py` (print-only as well; evidence is the log content), `kosmann_doublet.py` (ALL_PASS, exit 0), `kosmann_dirac_eigen.py` (ALL_PASS, exit 0); logs in `logs/`, results in `scripts/results_*.json`.

## History of this run (stated, not hidden)

1. First doublet script timed out (15 min of symbolic simplification), rewritten.
2. `sp.solve` on the 30 conditions returned []; the numeric null space was one-dimensional; the closed form was read off numeric null vectors at four alphas and then checked exactly. So the closed form was found numerically and verified symbolically, not derived symbolically.
3. Two exactness checks failed for algebra reasons (half angles, pi/21 angles) before the Weierstrass form passed; samples were changed to five (d, s) pairs with an invertible design.
4. Dirac eigenvalue extraction first took the real part (0); with Hermitian sigma the eigenvalue is imaginary.

## What this does NOT mean

- It is not the correspondent's operator, field equation or convention; the generators come from the embedding, and the Clifford convention (sigma, Hermitian) is ours.
- It does not say which SU(2) is spin or which multiplet is physical; a (1/2, 0) highest weight also exists (rank scan, numeric only), as expected from the two Killing-spinor families.
- It does not show the correspondent made an error. It shows only that the phase as quoted in the external summary is compatible with a spinor field, and that a scalar profile with the plain vector-field action has no non-zero solution.
- Global smoothness across alpha = 0 and pi/2 (where the Hopf frame degenerates) was not checked directly; it is inferred from the Killing equation [INFERRED, textbook fact, not re-derived].
- No novelty: Kosmann derivative and Killing spinors on S^3 are standard.

## Pre-commit review (2026-11-24)

The reviewer agent was blocked by its cycle cap (counter from earlier cycles); per the Independent Review Fallback Policy a fresh skeptic substituted. Verdict NEEDS_WORK, no blocking issue. Fixed: closure count (seven exact plus one numeric), residual quoted from the log, print-only scripts not cited as exit-code evidence, exact torus check, rank-scan scope, softer wording about the correspondent's phase, name of the total spinor term; C248: four negative controls, assert replaced by exit(1). Not changed: the claim.md title and folder name (pre-registration kept; the amendment states the limits).

## Skeptic (context-blind, claim.md and scripts only, 2026-11-24)

Verdict: CONFIRMED-REAL, scoped to the stated conventions. Its own scripts: session scratchpad `c249/attack.py`, `attack2.py`.

- Concern: the Kosmann formula in claim.md carries the wrong sign (- instead of +), so a reader reproducing from claim.md gets the wrong operator -> **Mitigated** (amendment in claim.md; prereg text kept).
- Concern: the five-sample argument rests on a first-harmonic assumption -> **Mitigated by the skeptic itself**: seven closure conditions vanish exactly with symbolic angles; the eighth, J^R_- psi_+ = psi_-, and the Killing equation hold numerically at 40 random points (about 5e-16). [VERIFIED-tool: the skeptic's scripts copied to `scripts/skeptic/` and re-run by me; they only print, so the evidence is the content of `logs/run_skeptic_attack*.txt`, not the exit code]
- Concern: sign compensation between connection and Kosmann term -> **Dismissed**: connection sign fixed by Clifford compatibility on all frame vectors, Kosmann sign also by Kosmann-Clifford compatibility (+1: 1e-13, -1: 102), tr C_N = 0. [skeptic, tool]
- Concern: L/R labels and the sign of the eigenvalue are conventions (orientation det = -1); a (1/2, 0) doublet with D = +3i/2 exists -> **Accepted limitation**, written into claim.md and the ledger; logged in `logs/run_skeptic_attack2.txt`: combined residual of its highest-weight conditions 5.5e-17, D eigenvalue 1.5i; an unlogged inline check by me gave the same (D psi / psi = 1.5i, J^L_3 = 1/2, J^R residual 1.6e-17).
- Most dangerous premise: the link to Part 3 (cot^2(2 alpha) = -1) is known only from an external summary and is not reproduced; the transfer to his labels is not established -> **Accepted limitation**: the result may not be quoted as "explains his obstruction".
