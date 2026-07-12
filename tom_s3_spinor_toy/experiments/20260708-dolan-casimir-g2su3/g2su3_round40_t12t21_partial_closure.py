"""
Round 40 (2026-07-12): compute Round 25's `T12+T21` piece (the
TERM1.TERM2+TERM2.TERM1 cross terms in D64^2's decomposition) in closed
form via an anticommutator identity, and determine its OWN contribution
to Delta's known non-scalarity -- continuing Round 39's technique on
the piece both FL Step 8a skeptics flagged as "the least-examined
piece" of Round 25's 5-piece decomposition.

SCOPE CHOICE (via AskUserQuestion, user chose the recommended option):
a quick scouting computation (not part of this script) found
{Dslash_mat,E_p} (the anticommutator) is SPARSE -- only 4/64 nonzero
entries per p, connecting the two SU(3) singlets (basis indices 0,7)
to a p-dependent pair of "3+3bar" indices. An attempt to identify this
anticommutator as a single named Clifford bivector operator (e.g.
E_2*E_3) did NOT match cleanly -- so THIS round does NOT claim an
elegant closed form for {Dslash_mat,E_p} itself. INSTEAD: T12+T21 is
built via TWO routes (direct TERM1_mat*TERM2_mat + TERM2_mat*
TERM1_mat, matching Round 23's ORIGINAL construction; and sum_p
kron({Dslash_mat,E_p}, M_p), an algebraic identity following from the
GENERAL Kronecker mixed-product rule (A⊗B)(C⊗D)=(AC)⊗(BD), specialized
here with B=Id: TERM1.TERM2 = kron(Dslash,Id)*sum_p kron(E_p,M_p) =
sum_p kron(Dslash*E_p, M_p), and TERM2.TERM1 = sum_p kron(E_p*Dslash,
M_p), summing to sum_p kron({Dslash,E_p}, M_p) -- both routes must
agree by pure linear algebra, so route agreement here is a
construction sanity check, not independent evidence -- see Kill
Conditions), and its COMPRESSED value on Round 23/24/25's own
span(w_a,w_b) is computed directly.

FINDING (compute-first, verified before writing this docstring):
T12+T21 compressed on span(w_a,w_b) = [[0,1],[3,0]] EXACTLY -- trace 0,
det -3, eigenvalues +-sqrt(3) (FL Step 8a flag, added post-review: a
hook worth carrying into a future round, given the sqrt(3) factors
already seen in the {Dslash_mat,E_p} scouting and elsewhere in this
project's SU(3)/G2 machinery -- not interpreted further this round).

CONTEXT for what this means for Delta: Round 24's Delta :=
D64^2-nabla*nabla-F_{S^-} has known value [[5/2,4/3],[4,5/2]] on
span(w_a,w_b) (Round 24, re-verified Round 25). Round 39 established
piece_H+piece_step2_rem (two of Round 25's five pieces) compress to
EXACTLY [[-1/6,0],[0,5/2]]. Subtracting: the REMAINING three pieces
(T12+T21, TORSION_E, cross-Casimir) must together supply
[[5/2,4/3],[4,5/2]] - [[-1/6,0],[0,5/2]] = [[8/3,4/3],[4,0]].
T12+T21 alone supplies [[0,1],[3,0]] of that -- a REAL but PARTIAL
contribution. TORSION_E + cross-Casimir together must still supply
[[8/3,1/3],[1,0]], NOT computed or attempted this round.

HONEST LIMIT: this round does NOT close Delta's non-scalarity, does
NOT resolve the 8/45-vs-~1 L4A tension, and does NOT touch
preprint.tex. It narrows Round 25's open 5-piece decomposition by one
more piece (T12+T21, now exactly known and verified via two routes),
leaving TORSION_E+cross-Casimir as the final unexplained pieces for a
future round.
"""

import sympy as sp

from g2su3_explicit_clifford import DIM, e_action
from g2su3_H_element import build_H_matrix, build_T_table
from g2su3_compute_crossterm import nabla_g
from g2su3_twisted_kernel import su3_action

N64 = DIM * DIM


def idx64(a, b):
    return DIM * a + b


def unit_vec(i):
    v = sp.zeros(DIM, 1)
    v[i] = 1
    return v


def kron(A, B):
    rA, cA = A.shape
    rB, cB = B.shape
    out = sp.zeros(rA * rB, cA * cB)
    for i in range(rA):
        for j in range(cA):
            if A[i, j] != 0:
                out[i * rB : (i + 1) * rB, j * cB : (j + 1) * cB] += A[i, j] * B
    return out


def compress_2x2(op, va, vb):
    """LINEAR compression (Gram-corrected projection onto span(va,vb)'s
    coefficients), matching Round 25's own compress_2x2 exactly. Valid
    for summing per-piece contributions whose TOTAL preserves the
    subspace, even if individual pieces do not."""
    Pmat = sp.Matrix.hstack(va, vb)
    G = (Pmat.T * Pmat).inv()
    opa, opb = op * va, op * vb
    sol_a = G * Pmat.T * opa
    sol_b = G * Pmat.T * opb
    return sp.simplify(sp.Matrix.hstack(sol_a, sol_b))


def main():
    print("=" * 70)
    print("SETUP: rebuild Dslash_mat, M_p, E_p, H, Casimir_su3 (all via")
    print("ALREADY-established Rounds 4-39 constructions)")
    print("=" * 70)
    T = build_T_table()
    H = build_H_matrix(T)
    Id8 = sp.eye(DIM)

    Ms = {}
    for p in range(1, 7):
        cols = [nabla_g(p, unit_vec(i)) for i in range(DIM)]
        Ms[p] = sp.Matrix.hstack(*cols)
    Es = {}
    for p in range(1, 7):
        cols = [e_action(p, unit_vec(i)) for i in range(DIM)]
        Es[p] = sp.Matrix.hstack(*cols)
    Dslash_mat = sp.zeros(DIM, DIM)
    for p in range(1, 7):
        Dslash_mat += Es[p] * Ms[p]

    Ls = {}
    for k in range(1, 9):
        cols = [su3_action(k, unit_vec(i)) for i in range(DIM)]
        Ls[k] = sp.Matrix.hstack(*cols)
    Casimir_su3 = sp.simplify(sum((-(Ls[k] * Ls[k]) for k in range(1, 9)), sp.zeros(DIM, DIM)))

    print("\n" + "=" * 70)
    print("STEP A: build T12+T21 via Round 23's ORIGINAL construction --")
    print("direct matrix multiplication TERM1_mat*TERM2_mat + TERM2_mat*")
    print("TERM1_mat, no algebraic manipulation")
    print("=" * 70)
    TERM1_mat = kron(Dslash_mat, Id8)
    TERM2_mat = sp.zeros(N64, N64)
    for p in range(1, 7):
        TERM2_mat += kron(Es[p], Ms[p])
    T12 = TERM1_mat * TERM2_mat
    T21 = TERM2_mat * TERM1_mat
    T12T21_direct = sp.simplify(T12 + T21)
    print("  T12+T21 built via direct 64x64 matrix multiplication.")

    print("\n" + "=" * 70)
    print("STEP B: cross-check via the anticommutator identity T12+T21 =")
    print("sum_p kron({Dslash_mat,E_p}, M_p) -- a construction sanity check")
    print("(both routes are algebraically forced to agree; NOT independent")
    print("evidence, see Kill Conditions/claim.md)")
    print("=" * 70)
    T12T21_anticomm = sp.zeros(N64, N64)
    for p in range(1, 7):
        anti = sp.simplify(Dslash_mat * Es[p] + Es[p] * Dslash_mat)
        T12T21_anticomm += kron(anti, Ms[p])
    T12T21_anticomm = sp.simplify(T12T21_anticomm)
    routes_match = sp.simplify(T12T21_direct - T12T21_anticomm) == sp.zeros(N64, N64)
    print(f"  T12+T21 (direct) == sum_p kron({{Dslash,E_p}},M_p) exactly? {routes_match}")
    assert routes_match, "the two T12+T21 construction routes disagree"

    print("\n" + "=" * 70)
    print("STEP C: compress T12+T21 onto span(w_a,w_b) (Round 23/24/25's")
    print("own 2-dim SU(3)-invariant subspace, EXACT same w_a/w_b/compress")
    print("method)")
    print("=" * 70)
    w_b = sp.zeros(N64, 1)
    w_b[idx64(0, 7)] = 1
    w_a = sp.zeros(N64, 1)
    w_a[idx64(4, 3)] = 1
    w_a[idx64(5, 2)] = -1
    w_a[idx64(6, 1)] = 1

    T12T21_2x2 = compress_2x2(T12T21_direct, w_a, w_b)
    print(f"  T12+T21 compressed on span(w_a,w_b): {list(T12T21_2x2)}")
    expected_T12T21 = sp.Matrix([[0, 1], [3, 0]])
    matches_expected = T12T21_2x2 == expected_T12T21
    print(f"  T12+T21|_2dim == [[0,1],[3,0]] exactly? {matches_expected}")
    assert matches_expected, f"T12+T21|_2dim changed from the verified value: {T12T21_2x2}"

    print("\n" + "=" * 70)
    print("STEP C.1 (post-skeptic addition): surface the eigenvalue")
    print("structure of T12T21_2x2 -- flagged by both FL Step 8a skeptics")
    print("as a mild underclaim in the original version of this script")
    print("=" * 70)
    tr = T12T21_2x2.trace()
    det = T12T21_2x2.det()
    eigs = T12T21_2x2.eigenvals()
    print(f"  trace = {tr}, det = {det}, eigenvalues = {eigs}")
    expected_eigs = {sp.sqrt(3): 1, -sp.sqrt(3): 1}
    eigs_ok = eigs == expected_eigs
    print(f"  eigenvalues == {{sqrt(3):1, -sqrt(3):1}} exactly? {eigs_ok}")
    assert eigs_ok, f"unexpected eigenvalue structure: {eigs}"
    print("  Noted as a hook for a future round (not interpreted further")
    print("  here): sqrt(3) also appeared in the {Dslash_mat,E_p} scouting")
    print("  entries this round started from.")

    print("\n" + "=" * 70)
    print("STEP D: re-derive Round 39's own piece_H+piece_step2_rem")
    print("compressed value in-script (self-contained re-verification, not")
    print("just cited), then compute how much of Delta's remainder T12+T21")
    print("accounts for")
    print("=" * 70)
    CASIMIR_L_plain = sp.simplify(sum((-(Ms[p] * Ms[p]) for p in range(1, 7)), sp.zeros(DIM, DIM)))
    Dslash2 = sp.simplify(Dslash_mat * Dslash_mat)
    cubic_and_curvature_L = sp.simplify(Dslash2 - CASIMIR_L_plain)
    closed_form_ccL = sp.simplify(sp.Rational(5, 2) * Id8 - 2 * Casimir_su3)
    ccL_ok = sp.simplify(cubic_and_curvature_L - closed_form_ccL) == sp.zeros(DIM, DIM)
    print(f"  cubic_and_curvature_L == (5/2)*Id-2*Casimir_su3 (Round 38/39)? {ccL_ok}")
    assert ccL_ok, "Round 38/39's closed form did not reproduce"

    piece_H_and_step2 = kron(cubic_and_curvature_L, Id8)
    piece_H_and_step2_2x2 = compress_2x2(piece_H_and_step2, w_a, w_b)
    print(f"  piece_H+piece_step2_rem compressed: {list(piece_H_and_step2_2x2)}")
    expected_r39 = sp.Matrix([[sp.Rational(-1, 6), 0], [0, sp.Rational(5, 2)]])
    r39_ok = piece_H_and_step2_2x2 == expected_r39
    print(f"  matches Round 39's own asserted [[-1/6,0],[0,5/2]] exactly? {r39_ok}")
    assert r39_ok, "Round 39's own compressed value did not reproduce"

    Delta_2x2_known = sp.Matrix([[sp.Rational(5, 2), sp.Rational(4, 3)], [4, sp.Rational(5, 2)]])
    target_remaining = sp.simplify(Delta_2x2_known - piece_H_and_step2_2x2)
    print(f"\n  Delta_2x2 (Round 24/25's own known value) = {list(Delta_2x2_known)}")
    print(f"  target_remaining := Delta_2x2 - (piece_H+piece_step2_rem) = {list(target_remaining)}")

    still_owed = sp.simplify(target_remaining - T12T21_2x2)
    print(f"\n  still_owed := target_remaining - T12T21_2x2 = {list(still_owed)}")
    print("  (this is what TORSION_E + cross-Casimir must STILL supply --")
    print("  NOT computed this round)")
    fully_accounts = still_owed == sp.zeros(2, 2)
    print(f"  T12+T21 alone accounts for ALL of Delta's remaining non-scalarity? {fully_accounts}")

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  T12+T21 -- Round 25's own 'least-examined piece' -- now has a")
    print("  verified compressed value [[0,1],[3,0]], confirmed via TWO")
    print("  construction routes (direct multiplication, anticommutator")
    print("  identity). This is a REAL, VERIFIED, but PARTIAL contribution")
    print("  to Delta's non-scalarity -- it does NOT fully close the gap.")
    print(f"  TORSION_E + cross-Casimir must still supply {list(still_owed)}")
    print("  on span(w_a,w_b) -- NOT computed or attempted this round.")
    print()
    print("  HONEST LIMIT: this round does NOT close Delta's non-scalarity,")
    print("  does NOT resolve the 8/45-vs-~1 L4A tension, and does NOT")
    print("  touch preprint.tex. Round 25's 5-piece decomposition now has")
    print("  THREE pieces closed/known exactly (H, step2_remainder, T12+T21)")
    print("  and TWO still open (TORSION_E, cross-Casimir) for a future round.")


if __name__ == "__main__":
    main()
