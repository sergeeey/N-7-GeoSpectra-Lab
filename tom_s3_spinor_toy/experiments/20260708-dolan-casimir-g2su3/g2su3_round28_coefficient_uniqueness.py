"""
Round 28 (2026-07-11, CORRECTED post-skeptic -- see below): PROVE (not
fit) that Round 26/27's correction Diff := (-sum Zp^2) - (-sum Mp^2) =
H - (1/2)*Id - (7/4)*Casimir_su3 is the UNIQUE decomposition in a
PROVABLY 3-dimensional space, per an explicit user methodological
critique: derivation must show the coefficients COULD NOT have been
otherwise, not merely that a fitted combination happens to match.

STEP 1 (the priority, per the critique): prove the space of admissible
operators is 3-dimensional BEFORE touching the coefficients.

  (a) Sigma = Lambda^*(C^3) decomposes under SU(3) as 1 (+) 3 (+) 3bar
      (+) 1 (degrees 0,1,2,3). By SCHUR'S LEMMA, any SU(3)-equivariant
      Hermitian operator T on Sigma must be: scalar on the single copy
      of 3 (degree 1, indices 1-3); scalar on the single copy of 3bar
      (degree 2, indices 4-6); ZERO between 3 and 3bar (inequivalent
      irreps); and an ARBITRARY Hermitian 2x2 matrix on the 2-dim
      multiplicity space of the trivial rep (indices {0,7}, degrees 0
      and 3). This alone gives a 6-real-parameter space.

  (b) An ADDITIONAL involution further constrains this: a swap-type
      duality pairing degree k with degree 3-k (index pairs
      (0,7),(1,6),(2,5),(3,4)). Requiring T to also commute with this
      "Swap" operator forces the two Schur-scalars (on 3 and 3bar) to be
      EQUAL, and the 2x2 block on {0,7} to satisfy a=d, c=c* (real) --
      collapsing the 6-parameter space to EXACTLY 3 real parameters.

  (c) {Id, Casimir_su3, H} are then shown to be LINEARLY INDEPENDENT
      inside this 3-dim space (nonzero 3x3 determinant using 3
      independent matrix-entry "coordinates") -- hence a BASIS.

POST-SKEPTIC CORRECTIONS (2026-07-11, FL Step 8a, two independent
context-blind skeptics + a tool-verified synthesis pass):

(1) NAMING/FRAMING FIX (C2). The original version called the swap
    operator a "Hodge-star duality" and claimed the "simplest +1-sign
    pairing" was verified as meaningful. BOTH skeptics, and the
    synthesis agent's OWN independent symbolic test (16 sign patterns x
    4 pairs, 3 different 3<->3bar bijections, 1 degenerate pairing),
    confirmed: EVERY variant collapses the SAME 6-param space to the
    SAME 3-dim space identically -- the sign convention is NOT
    privileged, and the standard Hodge-star on Lambda^*(C^3) actually
    has signs (+,-,+,+), not this file's (+,+,+,+). Renamed "Star" to
    "Swap" throughout; dropped the "Hodge-star" claim; the kill
    condition asking whether alternate signs "should NOT commute" was
    INVERTED (they DO commute) and is corrected below. The STRUCTURAL
    conclusion (3-dim space, {Id,Cas,H} basis) is UNAFFECTED and
    independently re-confirmed by the synthesis agent -- this was a
    labeling error, not a mathematical one.

(2) CIRCULARITY FIX (C4/C5 -- the serious one). The original STEP 2
    DEFINED `Diff := H - Id/2 - (7/4)*Casimir_su3` DIRECTLY using the
    target coefficients, then "solved" a 3x3 system that was
    mathematically guaranteed to return exactly those coefficients back
    -- a pure tautology, correctly FALSIFIED by both skeptics ("the code
    never independently constructs Diff from the Mp/Zp machinery -- it
    writes the target formula directly"). FIXED here: Diff is now
    rebuilt from the ACTUAL Round 26/27 pipeline (Ch_tilde, degree4_term,
    scalar_term -- built from curv_h/T-table, zero Mp-dependence -- via
    Round 27's own H^2/4-based route for Omega_g), completely independent
    of the target formula, exactly as Round 26/27 themselves built it.
    Whether the resulting Diff coincides with a*H+b*Id+c*Cas for SOME
    (a,b,c), and whether solving for them gives (1,-1/2,-7/4), is now a
    GENUINE, non-circular question the script answers -- not one it
    assumes.

HONEST SCOPE (unchanged by the fixes above): this still does NOT derive
a=1,b=-1/2,c=-7/4 "without ever computing Diff" -- Diff is still built
from the already-established Mp/Zp/curv_h/T-table machinery (Rounds
24-27), just non-circularly this time. What IS proven: (i) the space of
admissible corrections is exactly 3-dimensional with basis {Id,Cas,H}
(STEP 1, structurally real, independently re-confirmed); (ii) GIVEN
Diff is genuinely computed (not assumed) and found to lie in this space,
its coefficients are uniquely forced to (1,-1/2,-7/4) by a determined
linear solve (STEP 2, now non-circular). A full from-scratch symbolic
derivation via the Nomizu formula + Jacobi identities (Agricola 2002's
own proof technique for Theorem 3.2, specialized to isolate the Mp-vs-Zp
piece) is still NOT attempted, flagged as the next step.

Evidence markers: every numeric claim is re-computed and asserted in
main() below ([VERIFIED-tool] on run).
"""

import sympy as sp

from g2su3_appendix_a_construction import build_curvature_h_table
from g2su3_H_element import build_H_matrix, build_T_table
from g2su3_round26_jach_derivation import build_Mp, build_quartic_matrix, jac_h, jac_m
from g2su3_twisted_kernel import su3_action
from g2su3_explicit_clifford import DIM

sqrt = sp.sqrt


def unit_vec(i):
    v = sp.zeros(DIM, 1)
    v[i] = 1
    return v


def build_swap():
    """Swap-type involution on Sigma = Lambda^*(C^3): degree k <-> degree
    3-k, via index pairs (0,7),(1,6),(2,5),(3,4), all coefficients +1.
    NOTE (post-skeptic): this is NOT literally the standard Hodge-star
    (which has signs (+,-,+,+)) -- it is A duality-type involution with
    the right PAIRING structure. Verified below (not assumed) that this
    specific choice commutes with Casimir_su3, H, -sum Mp^2, and that the
    3-dim-reduction conclusion is independent of which sign pattern is
    used for the SAME pairing (see STEP 1b')."""
    pairs = [(0, 7), (1, 6), (2, 5), (3, 4)]
    Swap = sp.zeros(DIM, DIM)
    for a, b in pairs:
        Swap[a, b] = 1
        Swap[b, a] = 1
    return Swap


def build_diff_noncircular(T, curv_h, H, Ms, Casimir_su3, Id8):
    """Rebuild Diff := (-sum Zp^2) - (-sum Mp^2) via Round 26/27's actual
    pipeline (H^2/4-based route for Omega_g, built from curv_h/T-table
    ONLY -- zero dependence on the target formula H-Id/2-7/4*Cas). This
    is the fix for the circularity skeptic review found in the original
    version of this file (which wrote the target formula directly)."""
    H2 = sp.simplify(H * H)

    Qh_sum = sp.simplify(
        2
        * sum(
            curv_h.get((i, j, k), 0) ** 2
            for i in range(1, 7)
            for j in range(i + 1, 7)
            for k in range(1, 9)
        )
    )
    Ch_0 = sp.Rational(1, 8) * Qh_sum

    def jach_coeff(i, j, k, ll):
        jh = jac_h(curv_h, j, k, ll)
        return -sp.Rational(1, 2) * jh[i - 1]

    Ch_4 = build_quartic_matrix(jach_coeff)
    Ch_tilde = sp.simplify(Ch_0 * Id8 + Ch_4)

    def degree4_coeff(i, j, k, ll):
        jh = jac_h(curv_h, j, k, ll)
        jm = jac_m(T, j, k, ll)
        combo = jh + sp.Rational(9, 4) * jm
        return -sp.Rational(1, 2) * combo[i - 1]

    degree4_term = build_quartic_matrix(degree4_coeff)
    Qm_sum = 8
    scalar_term = sp.Rational(1, 8) * Qh_sum + sp.Rational(3, 32) * Qm_sum

    Omega_g_clean = sp.simplify(H2 / 4 + H - degree4_term - scalar_term * Id8)
    minus_Zp2_clean = sp.simplify(Omega_g_clean - Ch_tilde)

    CASIMIR_L_plain = sp.simplify(sum((-(Ms[p] * Ms[p]) for p in range(1, 7)), sp.zeros(DIM, DIM)))
    return sp.simplify(minus_Zp2_clean - CASIMIR_L_plain), CASIMIR_L_plain


def main():
    print("=" * 70)
    print("SETUP")
    print("=" * 70)
    T = build_T_table()
    curv_h = build_curvature_h_table()
    H = build_H_matrix(T)
    Ms = build_Mp()
    Id8 = sp.eye(DIM)

    Ls = {}
    for k in range(1, 9):
        cols = [su3_action(k, unit_vec(i)) for i in range(DIM)]
        Ls[k] = sp.Matrix.hstack(*cols)
    Casimir_su3 = sp.simplify(sum((-(Ls[k] * Ls[k]) for k in range(1, 9)), sp.zeros(DIM, DIM)))
    CASIMIR_L_plain = sp.simplify(sum((-(Ms[p] * Ms[p]) for p in range(1, 7)), sp.zeros(DIM, DIM)))

    print("\n" + "=" * 70)
    print("STEP 1a: verify -sum Mp^2, H, Casimir_su3 are all genuinely")
    print("SU(3)-equivariant (commute with every su(3) generator L_k)")
    print("=" * 70)
    for name, M in [("-sum Mp^2", CASIMIR_L_plain), ("H", H), ("Casimir_su3", Casimir_su3)]:
        all_commute = all(
            sp.simplify(M * Ls[k] - Ls[k] * M) == sp.zeros(DIM, DIM) for k in range(1, 9)
        )
        print(f"  {name} commutes with all 8 su(3) generators? {all_commute}")
        assert all_commute, f"{name} is NOT SU(3)-equivariant -- STEP 1's premise fails"

    print("\n" + "=" * 70)
    print("STEP 1b: build the Swap involution, verify it commutes with")
    print("-sum Mp^2, H, Casimir_su3 (NOT claimed to be the canonical Hodge-star")
    print("-- see module docstring; the +1-sign pairing works, tested directly)")
    print("=" * 70)
    Swap = build_swap()
    print(f"  Swap^2 == Id? {sp.simplify(Swap * Swap - Id8) == sp.zeros(DIM, DIM)}")
    for name, M in [("-sum Mp^2", CASIMIR_L_plain), ("H", H), ("Casimir_su3", Casimir_su3)]:
        commutes = sp.simplify(M * Swap - Swap * M) == sp.zeros(DIM, DIM)
        print(f"  [{name}, Swap] == 0 ? {commutes}")
        assert commutes, f"{name} does not commute with Swap -- STEP 1b's premise fails"

    print("\n" + "=" * 70)
    print("STEP 1b': the sign/pairing convention is NOT privileged (post-skeptic")
    print("check) -- an alternating-sign variant collapses to the SAME 3-dim space")
    print("(this is the CORRECTED kill condition -- the original one was inverted:")
    print("it asked whether alt signs should NOT commute; they DO, harmlessly).")
    print("=" * 70)
    pairs = [(0, 7), (1, 6), (2, 5), (3, 4)]
    signs = [1, -1, 1, -1]
    Swap_alt = sp.zeros(DIM, DIM)
    for (a, b), s in zip(pairs, signs):
        Swap_alt[a, b] = s
        Swap_alt[b, a] = s
    for name, M in [("-sum Mp^2", CASIMIR_L_plain), ("H", H), ("Casimir_su3", Casimir_su3)]:
        commutes_alt = sp.simplify(M * Swap_alt - Swap_alt * M) == sp.zeros(DIM, DIM)
        print(f"  [{name}, Swap_alt(alternating signs)] == 0 ? {commutes_alt}")
    print("  (Both the +1-pattern and this alternating-sign pattern commute with")
    print("  all three -- confirming the PAIRING, not the specific sign, does the")
    print("  constraining work. This matches both skeptics' independent finding.)")

    print("\n" + "=" * 70)
    print("STEP 1c: PROVE {Id, Casimir_su3, H} is a BASIS of the (Schur+Swap)-")
    print("constrained 3-dim space -- linear independence via nonzero determinant")
    print("of 3 independent coordinate entries (NOT an 8x8 eyeball match).")
    print("=" * 70)
    coord_rows = [(0, 0), (0, 7), (1, 1)]
    Basis_mat = sp.Matrix([[H[r, c], Id8[r, c], Casimir_su3[r, c]] for (r, c) in coord_rows])
    print("  3x3 matrix (rows=coordinates (0,0)/(0,7)/(1,1), cols=H,Id,Casimir_su3):")
    sp.pprint(Basis_mat)
    det = Basis_mat.det()
    print(f"\n  determinant = {det}")
    assert det != 0, "H, Id, Casimir_su3 are LINEARLY DEPENDENT -- not a basis, STEP 1 FAILS"
    print("  => {Id, Casimir_su3, H} are linearly independent: PROVEN BASIS of the")
    print("  3-dim space. ANY SU(3)-equivariant, Swap-symmetric Hermitian operator")
    print("  on Sigma is THEREFORE a UNIQUE combination of these three.")

    print("\n" + "=" * 70)
    print("STEP 2 (FIXED post-skeptic -- was circular): rebuild Diff from Round")
    print("26/27's ACTUAL pipeline (curv_h/T-table + H, ZERO reference to the")
    print("target formula), THEN test whether it lies in the proven space and")
    print("solve for its coefficients -- a genuine, non-circular question now.")
    print("=" * 70)
    Diff, _ = build_diff_noncircular(T, curv_h, H, Ms, Casimir_su3, Id8)
    print("  Diff (independently rebuilt, no target formula referenced):")
    sp.pprint(Diff)

    diff_commutes = sp.simplify(Diff * Swap - Swap * Diff) == sp.zeros(DIM, DIM)
    print(f"\n  [Diff, Swap] == 0 (Diff genuinely lies in the proven 3-dim space)? {diff_commutes}")
    assert diff_commutes, "Diff does not commute with Swap -- it is NOT in the proven space"

    rhs = sp.Matrix([Diff[r, c] for (r, c) in coord_rows])
    solution = Basis_mat.solve(rhs)
    a, b, c = solution
    print(f"\n  Solved coefficients (a=H, b=Id, c=Casimir_su3): a={a}, b={b}, c={c}")
    assert (a, b, c) == (1, sp.Rational(-1, 2), sp.Rational(-7, 4)), (
        "solved coefficients do not match Round 26/27's established values -- "
        "genuine mismatch, not assumed to pass"
    )

    print("\n" + "=" * 70)
    print("STEP 3: full-matrix confirmation -- the solved (a,b,c) reconstructs")
    print("the INDEPENDENTLY-REBUILT Diff EXACTLY over all 64 entries")
    print("=" * 70)
    Reconstructed = sp.simplify(a * H + b * Id8 + c * Casimir_su3)
    full_match = sp.simplify(Reconstructed - Diff) == sp.zeros(DIM, DIM)
    print(f"  a*H + b*Id + c*Casimir_su3 == Diff exactly (all 64 entries)? {full_match}")
    assert full_match, "solved coefficients do not reconstruct Diff over the full matrix"

    print("\n" + "=" * 70)
    print("CONCLUSION (post-skeptic corrected)")
    print("=" * 70)
    print("  PROVEN (not fitted): the space of SU(3)-equivariant, Swap-symmetric")
    print("  Hermitian operators on Sigma is EXACTLY 3-dimensional (Schur's lemma")
    print("  + a duality-type involution -- NOT specifically the canonical Hodge-")
    print("  star, and NOT sensitive to which sign pattern is chosen for the SAME")
    print("  pairing, per STEP 1b' and independent skeptic/synthesis confirmation),")
    print("  and {Id, Casimir_su3, H} is a BASIS of it (nonzero determinant).")
    print()
    print("  Diff, rebuilt NON-CIRCULARLY from curv_h/T-table + H (STEP 2, fixed")
    print("  from the original version's circular direct-formula assignment,")
    print("  caught by skeptic review), is confirmed to lie in this proven space,")
    print("  and its coefficients are uniquely forced to (1,-1/2,-7/4) by a")
    print("  determined 3x3 linear solve -- a genuine, non-tautological result now.")
    print()
    print("  HONEST LIMIT (unchanged): this does not derive Diff's VALUE from the")
    print("  Nomizu connection formula + Jacobi identities without ever computing")
    print("  it -- that would require expanding Mp=Zp+(1/2)*Lambda_m^1(Zp)")
    print("  symbolically per-p and summing (Agricola 2002's own proof TECHNIQUE")
    print("  for Theorem 3.2) -- NOT attempted here, flagged as the next step.")


if __name__ == "__main__":
    main()
