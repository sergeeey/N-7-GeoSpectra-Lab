# E3 — Claim: does the KT-8 product-decoupling formula survive a torsion-deformed S3 factor?

## Stakes
Internal-only (a follow-up gate on the open KT-8 gap / E2 candidate mechanism). Not
promotable to `preprint.tex` from this experiment alone — see "What this does NOT mean" below.

## Question type
[x] descriptive  [ ] predictive  [ ] causal

Descriptive: for the product Dirac operator on S3xS6, once S3's factor operator is replaced
by the torsion-deformed D_S3(t) (E2) instead of the Levi-Civita D_S3^{LC} (KT-8's original),
does the Clifford-algebra decoupling identity `D_full^2 = D_S6^2(x)1 + 1(x)D_S3(t)^2` still
hold exactly, and what does that imply for `min|eig(D_full)|` at t=0 (E2's crossing)?

## Background (established, not re-derived here)
- KT-8 (`experiments/20260615-g8-chirality-obstruction/`,
  `reports/PROJECT_360_ROUND3_SYNTHESIS.md` section "KT-8"): for the Levi-Civita (torsion-free)
  connection on both factors, `D_full = D_S6,twisted (x) Id_S3 + chi6 (x) D_S3^{LC}` (Sire & Xu,
  arXiv:2005.01448, eq. 2.2-2.3), giving `D_full^2 = D_S6^2(x)1 + 1(x)(D_S3^{LC})^2` exactly
  (cross term vanishes because `{chi6, D_S6}=0` is a general chirality-operator fact, independent
  of D_S3), and S3's own Levi-Civita spectrum +-(n+3/2)/rho3 never reaches 0 -> `ker(D_full)=0`.
- E2 (`experiments/20260717-round67-e2-s3-torsion-deformation/`): replacing S3's connection with
  Agricola's torsion-deformed one-parameter family gives `D_S3(t) = D_S3^{LC} + (t-1/2)*h_H`
  (h_H=3, exact scalar shift), with exact zero eigenvalues at e.g. t=0, t=1 (n=0 level). E2
  explicitly flagged (claim.md item 1, decision.md item 1) that whether KT-8's decoupling
  formula survives this substitution was NOT checked there — Sire & Xu only cover
  Levi-Civita-on-both-factors.

## Claim (falsifiable)
1. The decoupling identity `D_full^2 = D_S6^2(x)Id_S3 + Id_S6(x)D_S3(t)^2` continues to hold
   to machine precision (residual < 1e-9) for t in {0, 0.5, 1, 0.25}, for two independent
   D_S6 test operators, AND for an arbitrary random Hermitian D_S3 unrelated to the torsion
   family — because the cross term in the Sire-Xu expansion is
   `{chi6, D_S6}(x)D_S3`, which vanishes iff `{chi6,D_S6}=0` alone; D_S3 never enters that
   condition, so the decoupling is structurally independent of what D_S3 is.
2. Consequently, at t=0 (where D_S3(0) has an exact zero eigenvalue per E2),
   `min|eig(D_full)|` collapses from the Levi-Civita floor (1.5, KT-8) down to
   `min|eig(D_S6)|` — the S3 floor is removed, and D_full's spectral gap is now set entirely
   by whatever D_S6's own spectrum does.
3. This does NOT by itself demonstrate `ker(D_full) != 0` with the REAL physical
   curvature-twisted D_S6 operator (not reconstructed in this script) — that requires
   combining this experiment's verified decoupling identity with two facts established
   elsewhere: D_S3(0) has an exact zero eigenvalue (E2) and D_S6,twisted has an exact zero
   eigenvalue (G73/G74A, ind=1 per channel). The logical combination is stated explicitly in
   the results, not re-derived from scratch.

## Method
1. Build Cl(3) (S3 generators, Pauli matrices sigma_x,sigma_y,sigma_z, Cl(3,0) convention)
   and Cl(6) (S6 generators, Jordan-Wigner on 3 qubits, 8-dim rep) independently from scratch
   — no script from KT-8's own from-scratch pass survives in the repo (confirmed by
   `grep -rl "Cl(9)\|Jordan-Wigner" experiments/` before starting: zero hits besides this
   experiment and E2's claim/decision text), so this is a fresh, not reused, construction.
2. Build chi6 = i*(Gamma6_1...Gamma6_6), verify Hermitian, chi6^2=Id, and chi6 anticommutes
   with each of the 6 generators (the only property the decoupling proof needs).
3. Assemble the 16-dim Cl(9) representation: Gamma_full_i = Gamma6_i(x)I2 (S6 directions),
   Gamma_full_{6+j} = chi6(x)Gamma3_j (S3 directions) — verify all 9x9=81 (45 unordered)
   pairwise Clifford relations exactly.
4. D_S3(t) substituted directly as a 2x2 matrix (not built from Gamma3_j, matching KT-8's own
   style): `D_S3(t) = 1.5*sigma_z + (t-0.5)*3*I2`, reusing E2's own calibrated closed form
   (1.5 = G8's n=0 eigenvalue, h_H=3 = E2's calibration) rather than re-deriving Kostant's
   torsion element.
5. Two independent D_S6 test operators, both anticommuting with chi6 by construction:
   (i) single-generator combination scaled to eigenvalues +-0.185 (matches KT-8's own reported
   near-zero stress test exactly); (ii) a projector construction `(M - chi6@M@chi6)/2` for a
   fixed-seed random Hermitian M, giving a richer, non-degenerate spectrum not tied to the
   single-generator special case (a single-generator combination always squares to a scalar
   multiple of the identity — algebraic fact, not itself evidence about the real operator).
6. Build D_full, compute the decoupling residual and full spectrum for t in
   {0.5 (regression check against KT-8's published 1.5113689), 0 and 1 (E2's crossings),
   0.25 (generic non-crossing, sanity check of the formula's prediction at an arbitrary point)},
   and repeat with an arbitrary random Hermitian D_S3 (not from the torsion family at all) to
   test the structural independence claim directly.

## Kill criterion
If the decoupling residual exceeded 1e-9 for ANY t or D_S6 variant, or for the arbitrary
random D_S3 check, the claim that decoupling is structurally independent of D_S3 would be
FALSIFIED — this would mean the cross-term cancellation secretly depended on D_S3 being the
specific Levi-Civita operator (or on some property of D_S3 beyond Hermiticity), and the whole
KT-8 result would need re-examination even for its ORIGINAL Levi-Civita case.
Kill signal: `verdict.decoupling_survives_torsion_deformation == False` in `results_e3.json`.
Also: if the reproduced t=0.5/single-generator `min_abs_eig_d_full` disagreed with KT-8's
published 1.5113689 by more than 1e-4, that would indicate this from-scratch construction is
NOT the same one KT-8 used (wrong convention, sign error, etc.) and the whole exercise would
need to be redone with the discrepancy resolved first.
Kill signal: `kt8_regression_check.matches_kt8_within_1e-4 == False`.

## Assumptions (status)
| Assumption | Status |
|---|---|
| Sire & Xu product-Dirac formula, `D=D_M1(x)Id+omega_C^M1(x)D_M2` | [VERIFIED-external-source] — already established and cited in KT-8, not re-read here |
| D_S3(t) = 1.5*sigma_z + (t-0.5)*3*I2 (E2's closed form) | [VERIFIED-sympy, reused from E2] — not re-derived here |
| D_S3(0), D_S3(1) have exact zero eigenvalues | [VERIFIED-sympy, reused from E2] |
| The real curvature-twisted D_S6,twisted has an exact zero eigenvalue (ind=1/channel) | [VERIFIED-sympy, cited from G73/G74A] — NOT reconstructed in this script; this script's D_S6 test operators are flat Clifford-algebra stand-ins, not the physical differential operator |
| Cl(3)/Cl(6)/chi6/Cl(9) construction, decoupling residual, spectra | [VERIFIED-tool] — this script, exact/machine-precision numeric linear algebra |
| Single-generator D_S6 forces D_S6^2=const*Id (cannot itself carry an exact non-trivial zero eigenvalue) | [VERIFIED-tool, derived and confirmed numerically] — a structural limitation of that specific test-operator choice, explicitly not claimed to be the real physical operator's behavior |

## What this does NOT mean
1. Does **not** independently reconstruct the real curvature-twisted S6 Dirac operator or
   re-verify its zero mode — that is G73/G74A's result, cited here, not re-derived. This
   script's D_S6 test operators are flat-Clifford-algebra stand-ins (same limitation KT-8's
   own second pass had), useful for testing the DECOUPLING STRUCTURE, not for computing the
   physical operator's actual kernel.
2. Does **not** supply any physical reason to select t=0 (or t=1, or any other E2 crossing)
   over t=1/2 (Levi-Civita, the physically default/round choice) — this is the SAME
   FITTED-vs-DERIVED gap E2 already flagged and it is entirely unaddressed here. Finding that
   the decoupling survives at t=0 does not make t=0 physically motivated.
3. Does **not** verify that a torsion connection on S3 is compatible with the rest of this
   project's construction (NCG spectral triple G18+, Freund-Rubin flux, etc.) — same caveat
   E2 already recorded, unexamined here too.
4. Does **not** by itself close KT-8. It closes exactly one specific open item E2 raised (does
   the decoupling formula generalize to a torsion-deformed S3 factor) — the answer is yes,
   structurally and unconditionally (independent of D_S3 entirely) — but the physical-selection
   gap (item 2 above) means KT-8 remains open as "REFUTED within the stated [Levi-Civita]
   product ansatz — blocking" per `preprint.tex`'s own current wording, now with one additional
   caveat: a torsion-deformed variant of the ansatz WOULD evade the block mathematically, IF a
   principled reason for t=0 existed. It currently does not.

## Check
`python e3_full_operator_torsion_deformed.py` ->
`verdict.label == "PASS_DECOUPLING_SURVIVES_TORSION_DEFORMATION"`,
`verdict.construction_verified == true`,
`verdict.kt8_regression_matches == true`,
`verdict.s3_floor_removed_at_t0 == true`.
