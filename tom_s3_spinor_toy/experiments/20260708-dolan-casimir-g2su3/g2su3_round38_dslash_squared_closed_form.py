"""
Round 38 (2026-07-12): investigate the long-flagged "8/45 vs exact-
ratio-1" L4A norm-bound tension (preprint.tex L560-607 vs Round 23's
explicit F_{S^-} spectral computation, decision.md ~L4105-4279).

INVESTIGATION FIRST (research agent, no code changes): Round 23's own
decision.md analysis (L4204-4213) already TESTED and REJECTED a pure
rho_6-normalization mismatch as sufficient explanation (curvature-type
quantities scale identically under uniform rescaling -- the ~5.6x gap
survives that check). The BETTER-evidenced root cause per Round 23's
own Kill Analysis: "remainder" (:=D64^2-F_{S^-} on the 2-dim SU(3)-
invariant subspace) is NOT scalar ([[17/6,5/3],[5,7/2]], trace 19/3),
so there is no clean, independently-isolated "R/4 + nabla*nabla" to
compare against -- Round 23 explicitly flagged nabla*nabla as "NOT YET
independently isolated/verified" on the TWISTED Gamma(S^+ x S^-)
bundle, with the SAME method (matrix-coefficient-section machinery)
flagged as the natural next step, NOT attempted there.

THIS ROUND: does NOT attempt the full twisted-bundle nabla*nabla
isolation (a separate, larger undertaking -- Round 23's own object
lives on a 16-dim bundle with genuine cross-terms between chirality
factors, and correctly isolating nabla*nabla there requires care this
round does not risk). INSTEAD: establishes a genuinely NEW, verified
closed-form synthesis of the UNTWISTED S^6-intrinsic Dirac operator
Dslash_mat (Rounds 4-26, used as "TERM1" in Round 23's own D64=TERM1+
TERM2 split) via THIS SESSION's own Casimir_su3 machinery (Rounds 29-
37) -- connecting Round 27 (Dslash_mat=-(1/2)*H, an operator identity)
and Round 29 (H^2=3*Id-3*X, a closed-form quartic decomposition) to
Casimir_su3=Id+X/3 (Round 29/33/37) for the FIRST TIME.

CORE FINDING:
  Dslash_mat^2 = 3*Id - (9/4)*Casimir_su3                    EXACTLY
  sum_p M_p^2  = -(1/2)*Id + (1/4)*Casimir_su3                EXACTLY
(the second re-expresses Round 26's own already-built CASIMIR_L_plane
:=-sum M_p^2 in closed form too: CASIMIR_L_plain = (1/2)*Id -
(1/4)*Casimir_su3).

SPECTRAL CONSEQUENCE (immediate, from Casimir_su3's own known spectrum
{0: mult 2 (the two SU(3) singlets 1, y123), 4/3: mult 6 (the 3+3bar)}):
Dslash_mat^2 has spectrum {3: mult 2, 0: mult 6} -- i.e. Dslash_mat
itself has a 6-DIMENSIONAL KERNEL exactly on the (3+3bar) SU(3)-content
of Sigma, and eigenvalues +-sqrt(3) on the 2 singlets (Dslash_mat^2=3
there, never zero) -- a clean, closed-form, fully verified spectral
fact about this project's own untwisted Dirac operator that was
previously only known via raw 8x8 matrix diagonalization, never
connected to the Casimir_su3 machinery this session built.

RELEVANCE TO L4A (honest scope, NOT a resolution): Round 23's own
TERM1 = Dslash_mat (x) Id_{S^-}, so TERM1^2 = Dslash_mat^2 (x) Id_{S^-}
is NOW fully closed-form via this round's synthesis -- a genuinely
USEFUL building block for any FUTURE attempt to isolate nabla*nabla on
the twisted 16-dim bundle (Round 23's own flagged next step). This
round does NOT attempt that isolation, does NOT reconcile the 8/45 vs
~1 ratio, and does NOT touch preprint.tex. It establishes ONE new,
verified, closed-form fact, directly upstream of the open problem, and
stops there -- matching this project's own Minimal Relaxation Rule
(one atomic closure per round, not overreach).
"""

import sympy as sp

from g2su3_explicit_clifford import DIM, e_action
from g2su3_H_element import build_H_matrix, build_T_table
from g2su3_round26_jach_derivation import build_Mp
from g2su3_twisted_kernel import su3_action

sqrt = sp.sqrt


def unit_vec(i):
    v = sp.zeros(DIM, 1)
    v[i] = 1
    return v


def main():
    print("=" * 70)
    print("SETUP: rebuild T, H, Dslash_mat, sum M_p^2, Casimir_su3 (all via")
    print("ALREADY-established Rounds 4-37 constructions)")
    print("=" * 70)
    T = build_T_table()
    H = build_H_matrix(T)
    Id8 = sp.eye(DIM)

    Ms = build_Mp()
    Es = {}
    for p in range(1, 7):
        cols = [e_action(p, unit_vec(i)) for i in range(DIM)]
        Es[p] = sp.Matrix.hstack(*cols)
    Dslash_mat = sp.zeros(DIM, DIM)
    for p in range(1, 7):
        Dslash_mat += Es[p] * Ms[p]

    sumMp2 = sp.simplify(sum((Ms[p] * Ms[p] for p in range(1, 7)), sp.zeros(DIM, DIM)))

    Ls = {}
    for k in range(1, 9):
        cols = [su3_action(k, unit_vec(i)) for i in range(DIM)]
        Ls[k] = sp.Matrix.hstack(*cols)
    Casimir_su3 = sp.simplify(sum((-(Ls[k] * Ls[k]) for k in range(1, 9)), sp.zeros(DIM, DIM)))

    print("\n" + "=" * 70)
    print("STEP A: re-verify Round 27's own Dslash_mat = -(1/2)*H (operator")
    print("identity, cited unchanged, load-bearing for this round's synthesis)")
    print("=" * 70)
    round27_ok = sp.simplify(Dslash_mat - (-sp.Rational(1, 2)) * H) == sp.zeros(DIM, DIM)
    print(f"  Dslash_mat == -(1/2)*H exactly? {round27_ok}")
    assert round27_ok, "Round 27's own Dslash_mat=-(1/2)*H did not reproduce"

    print("\n" + "=" * 70)
    print("STEP B (the core new finding): Dslash_mat^2 = 3*Id - (9/4)*")
    print("Casimir_su3 EXACTLY -- a NEW synthesis connecting Round 27")
    print("(Dslash=-(1/2)H) + Round 29 (H^2=3*Id-3*X) + this session's own")
    print("Casimir_su3=Id+X/3 (Rounds 29/33/37) for the FIRST TIME")
    print("=" * 70)
    Dslash2_direct = sp.simplify(Dslash_mat * Dslash_mat)
    Dslash2_closed = sp.simplify(3 * Id8 - sp.Rational(9, 4) * Casimir_su3)
    match_dslash2 = sp.simplify(Dslash2_direct - Dslash2_closed) == sp.zeros(DIM, DIM)
    print(f"  Dslash_mat^2 == 3*Id - 9/4*Casimir_su3 exactly? {match_dslash2}")
    assert match_dslash2, "Dslash_mat^2 does not match the new closed form"

    print("\n" + "=" * 70)
    print("STEP C (companion synthesis): sum_p M_p^2 = -(1/2)*Id +")
    print("(1/4)*Casimir_su3 EXACTLY -- re-expresses Round 26's own")
    print("CASIMIR_L_plain:=-sum M_p^2 in closed form for the first time")
    print("=" * 70)
    sumMp2_closed = sp.simplify(-sp.Rational(1, 2) * Id8 + sp.Rational(1, 4) * Casimir_su3)
    match_summp2 = sp.simplify(sumMp2 - sumMp2_closed) == sp.zeros(DIM, DIM)
    print(f"  sum_p M_p^2 == -1/2*Id + 1/4*Casimir_su3 exactly? {match_summp2}")
    assert match_summp2, "sum M_p^2 does not match the new closed form"

    print("\n" + "=" * 70)
    print("STEP D: spectral consequence of STEP B, cross-checked against")
    print("Dslash_mat^2's own direct matrix eigenvalues (not merely derived")
    print("from Casimir_su3's spectrum in the abstract)")
    print("=" * 70)
    direct_eigs = Dslash2_direct.eigenvals()
    closed_eigs = Dslash2_closed.eigenvals()
    cas_eigs = Casimir_su3.eigenvals()
    print(f"  Dslash_mat^2 eigenvalues (direct matrix diagonalization): {direct_eigs}")
    print(f"  Dslash_mat^2 eigenvalues (from the closed form): {closed_eigs}")
    print(f"  Casimir_su3 eigenvalues (for reference): {cas_eigs}")
    eigs_match = direct_eigs == closed_eigs
    print(f"  direct and closed-form spectra agree exactly? {eigs_match}")
    assert eigs_match, "direct and closed-form spectra disagree"
    expected_spectrum = {sp.Integer(3): 2, sp.Integer(0): 6}
    spectrum_as_expected = direct_eigs == expected_spectrum
    print(f"  spectrum == {{3: mult 2, 0: mult 6}} exactly? {spectrum_as_expected}")
    assert spectrum_as_expected, f"unexpected spectrum {direct_eigs}"
    print("  => Dslash_mat has a 6-dimensional KERNEL exactly on the SU(3)")
    print("  (3+3bar) content of Sigma, and eigenvalues +-sqrt(3) (never 0)")
    print("  on the 2 SU(3) singlets -- a clean, closed-form spectral fact,")
    print("  previously only accessible via raw 8x8 diagonalization.")

    print("\n" + "=" * 70)
    print("STEP E (post-skeptic addition): verify Dslash_mat is normal (real-")
    print("symmetric), which is what actually licenses the narrative jump from")
    print("'Dslash_mat^2 has a 6-dim 0-eigenspace' to 'Dslash_mat itself has a")
    print("6-dim kernel' (ker(A^2)=ker(A) requires A normal; FL Step 8a skeptic-2")
    print("flagged this as [WEAK]/unverified in the original script -- closing")
    print("it here with a direct, in-artifact check rather than a narrative claim)")
    print("=" * 70)
    is_symmetric = sp.simplify(Dslash_mat - Dslash_mat.T) == sp.zeros(DIM, DIM)
    print(f"  Dslash_mat symmetric (== Dslash_mat.T)? {is_symmetric}")
    assert is_symmetric, "Dslash_mat is not symmetric -- normality claim unverified"
    direct_dslash_eigs = Dslash_mat.eigenvals()
    print(f"  Dslash_mat eigenvalues (direct diagonalization): {direct_dslash_eigs}")
    expected_dslash_spectrum = {sqrt(3): 1, -sqrt(3): 1, sp.Integer(0): 6}
    dslash_spectrum_ok = direct_dslash_eigs == expected_dslash_spectrum
    print(f"  spectrum == {{sqrt(3): 1, -sqrt(3): 1, 0: 6}} exactly? {dslash_spectrum_ok}")
    assert dslash_spectrum_ok, f"unexpected Dslash_mat spectrum {direct_dslash_eigs}"
    print("  => Dslash_mat is real-symmetric (hence normal), so ker(Dslash_mat^2)")
    print("  = ker(Dslash_mat) legitimately; the 6-dim kernel + +-sqrt(3) claim in")
    print("  Core argument #5 is now a DIRECTLY VERIFIED fact, not an inference.")

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  NEW, VERIFIED closed-form synthesis: Dslash_mat^2 = 3*Id -")
    print("  (9/4)*Casimir_su3, and sum_p M_p^2 = -(1/2)*Id + (1/4)*")
    print("  Casimir_su3 -- connecting Round 27/29 (pre-existing facts) to")
    print("  this session's own Casimir_su3 machinery (Rounds 29-37) for")
    print("  the FIRST TIME. Round 23's own TERM1 = Dslash_mat (x) Id_{S^-}")
    print("  is now fully closed-form (TERM1^2 = [3*Id-(9/4)*Casimir_su3]")
    print("  (x) Id_{S^-}) -- a genuinely useful building block for a")
    print("  FUTURE attempt to isolate nabla*nabla on the twisted 16-dim")
    print("  Gamma(S^+ (x) S^-) bundle (Round 23's own flagged next step).")
    print()
    print("  HONEST LIMIT: this round does NOT isolate nabla*nabla on the")
    print("  twisted bundle, does NOT reconcile the 8/45-vs-~1 L4A norm-")
    print("  bound tension, and does NOT touch preprint.tex. The full")
    print("  twisted-bundle reconciliation (Round 23's own next step)")
    print("  remains a separate, larger undertaking for a future round.")


if __name__ == "__main__":
    main()
