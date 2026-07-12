"""
Round 41 (2026-07-12): close the FINAL two pieces of Round 25's
5-piece decomposition of Delta -- TORSION_E and cross-Casimir -- via
direct construction (matching Round 25's own exact code), completing
the full algebraic bookkeeping of Delta's non-scalarity.

SCOPE (via AskUserQuestion, user chose the recommended option): a
quick scouting computation (not part of this committed script) found
BOTH remaining pieces are clean, rational matrices when compressed on
Round 23/24/25's own span(w_a,w_b):
  TORSION_E compressed      = [[8/3, 2/3], [2, 0]]
  cross_casimir compressed  = [[0, -1/3], [-1, 0]]
  sum                       = [[8/3, 1/3], [1, 0]]  == Round 40's own
                              still_owed EXACTLY.

Following Round 40's own lesson (a scouting attempt to find an elegant
closed form for {Dslash_mat,E_p} in terms of a NAMED operator did not
succeed there, and direct construction was used instead, honestly):
this round does NOT attempt to express TORSION_E/cross_casimir in
terms of Casimir_su3 or any other already-named object. Both are built
via DIRECT construction (TORSION_E from the T-table/curv_h-table via
nabla_bracket, exactly matching Round 25's own code; cross_casimir =
2*sum_p kron(M_p,M_p), exactly matching Round 25's own algebraic
re-expression of Round 24's nabla*nabla).

FINDING: with these two pieces closed, ALL FIVE pieces of Round 25's
Delta decomposition are now known in EXACT closed form:
  piece_H + piece_step2_rem  = [[-1/6, 0], [0, 5/2]]   (Round 39)
  T12+T21                    = [[0, 1], [3, 0]]         (Round 40)
  TORSION_E                  = [[8/3, 2/3], [2, 0]]     (this round)
  cross_casimir               = [[0, -1/3], [-1, 0]]     (this round)
  SUM                         = [[5/2, 4/3], [4, 5/2]]  == Delta_2x2
                                (Round 24/25's own known value) EXACTLY.

HONEST LIMIT (stated upfront, not after the fact): this is a COMPLETE
ALGEBRAIC ACCOUNTING of Delta's 5-piece decomposition -- every piece
Round 25 set up is now a known, verified quantity, nothing "unbuilt" or
"unexamined" remains in that specific sense. This does NOT make Delta
itself scalar -- Delta = [[5/2,4/3],[4,5/2]] is NOT proportional to Id,
and remains so. It does NOT resolve the 8/45-vs-~1 L4A norm-bound
tension (that tension is about whether R/4 can be cleanly, separately
isolated from Delta at all -- Round 24's own concern, unaffected by
this round's bookkeeping closure). It does NOT touch preprint.tex.
"""

import sympy as sp

from g2su3_appendix_a_construction import build_curvature_h_table
from g2su3_compute_crossterm import nabla_g
from g2su3_explicit_clifford import DIM, e_action
from g2su3_H_element import build_H_matrix, build_T_table
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
    """LINEAR compression, matching Round 25's own compress_2x2 exactly."""
    Pmat = sp.Matrix.hstack(va, vb)
    G = (Pmat.T * Pmat).inv()
    opa, opb = op * va, op * vb
    sol_a = G * Pmat.T * opa
    sol_b = G * Pmat.T * opb
    return sp.simplify(sp.Matrix.hstack(sol_a, sol_b))


def main():
    print("=" * 70)
    print("SETUP: rebuild Dslash_mat, M_p, E_p, H, Casimir_su3, T-table,")
    print("curv_h-table (all via ALREADY-established Rounds 4-40")
    print("constructions)")
    print("=" * 70)
    T = build_T_table()
    H = build_H_matrix(T)
    curv_h = build_curvature_h_table()
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

    def nabla_bracket(p, q):
        out = sp.zeros(DIM, DIM)
        for r in range(1, 7):
            coeff = T.get((p, q, r), 0)
            if coeff != 0:
                out += coeff * Ms[r]
        for k in range(1, 9):
            coeff = curv_h.get((p, q, k), 0)
            if coeff != 0:
                out -= coeff * Ls[k]
        return out

    w_b = sp.zeros(N64, 1)
    w_b[idx64(0, 7)] = 1
    w_a = sp.zeros(N64, 1)
    w_a[idx64(4, 3)] = 1
    w_a[idx64(5, 2)] = -1
    w_a[idx64(6, 1)] = 1

    print("\n" + "=" * 70)
    print("STEP A: build TORSION_E via direct construction (exactly Round")
    print("25's own code: sum_{p<q} kron(E_p*E_q, nabla_bracket(p,q)))")
    print("=" * 70)
    torsion_E = sp.zeros(N64, N64)
    for p in range(1, 7):
        for q in range(p + 1, 7):
            nb_pq = nabla_bracket(p, q)
            torsion_E += kron(Es[p] * Es[q], nb_pq)
    torsion_E = sp.simplify(torsion_E)
    torsion_2x2 = compress_2x2(torsion_E, w_a, w_b)
    print(f"  TORSION_E compressed on span(w_a,w_b): {list(torsion_2x2)}")
    expected_torsion = sp.Matrix([[sp.Rational(8, 3), sp.Rational(2, 3)], [2, 0]])
    torsion_ok = torsion_2x2 == expected_torsion
    print(f"  TORSION_E|_2dim == [[8/3,2/3],[2,0]] exactly? {torsion_ok}")
    assert torsion_ok, f"TORSION_E|_2dim changed from the verified value: {torsion_2x2}"

    print("\n" + "=" * 70)
    print("STEP B: build cross_casimir via direct construction (exactly")
    print("Round 25's own algebraic re-expression: 2*sum_p kron(M_p,M_p))")
    print("=" * 70)
    cross_casimir = sp.simplify(
        2 * sum((kron(Ms[p], Ms[p]) for p in range(1, 7)), sp.zeros(N64, N64))
    )
    cc_2x2 = compress_2x2(cross_casimir, w_a, w_b)
    print(f"  cross_casimir compressed on span(w_a,w_b): {list(cc_2x2)}")
    expected_cc = sp.Matrix([[0, sp.Rational(-1, 3)], [-1, 0]])
    cc_ok = cc_2x2 == expected_cc
    print(f"  cross_casimir|_2dim == [[0,-1/3],[-1,0]] exactly? {cc_ok}")
    assert cc_ok, f"cross_casimir|_2dim changed from the verified value: {cc_2x2}"

    print("\n" + "=" * 70)
    print("STEP C: re-derive Round 40's own still_owed in-script")
    print("(self-contained re-verification): TORSION_E + cross_casimir")
    print("=" * 70)
    still_owed_reconstructed = sp.simplify(torsion_2x2 + cc_2x2)
    print(f"  TORSION_E + cross_casimir = {list(still_owed_reconstructed)}")
    expected_still_owed = sp.Matrix([[sp.Rational(8, 3), sp.Rational(1, 3)], [1, 0]])
    still_owed_ok = still_owed_reconstructed == expected_still_owed
    print(f"  matches Round 40's own asserted [[8/3,1/3],[1,0]] exactly? {still_owed_ok}")
    assert still_owed_ok, "Round 40's own still_owed value did not reproduce"

    print("\n" + "=" * 70)
    print("STEP D (self-contained): re-derive the other three pieces")
    print("(piece_H+piece_step2_rem via Round 38/39's closed form;")
    print("T12+T21 via direct construction, matching Round 40) to")
    print("assemble the GRAND TOTAL of all five pieces")
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

    TERM1_mat = kron(Dslash_mat, Id8)
    TERM2_mat = sp.zeros(N64, N64)
    for p in range(1, 7):
        TERM2_mat += kron(Es[p], Ms[p])
    T12T21_direct = sp.simplify(TERM1_mat * TERM2_mat + TERM2_mat * TERM1_mat)
    T12T21_2x2 = compress_2x2(T12T21_direct, w_a, w_b)

    grand_total = sp.simplify(piece_H_and_step2_2x2 + T12T21_2x2 + torsion_2x2 + cc_2x2)
    print(f"\n  GRAND TOTAL (all 5 pieces summed) = {list(grand_total)}")
    Delta_2x2_known = sp.Matrix([[sp.Rational(5, 2), sp.Rational(4, 3)], [4, sp.Rational(5, 2)]])
    print(f"  Delta_2x2 (Round 24/25's own known value) = {list(Delta_2x2_known)}")
    full_closure = grand_total == Delta_2x2_known
    print(f"  ALL 5 pieces reconstruct Delta_2x2 EXACTLY? {full_closure}")
    assert full_closure, "the 5-piece grand total does not match Delta_2x2"

    print("\n" + "=" * 70)
    print("STEP E (honest scoping, asserted not just claimed): Delta_2x2")
    print("itself remains NON-scalar -- this round closes the BOOKKEEPING,")
    print("not Delta's non-scalarity")
    print("=" * 70)
    is_scalar = Delta_2x2_known == Delta_2x2_known[0, 0] * sp.eye(2)
    print(f"  Delta_2x2 proportional to Id (i.e. IS Delta scalar)? {is_scalar}")
    assert not is_scalar, "Delta_2x2 unexpectedly turned out scalar"

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  All FIVE pieces of Round 25's Delta decomposition are now")
    print("  known in EXACT closed form:")
    print(f"    piece_H+piece_step2_rem = {list(piece_H_and_step2_2x2)}  (Round 39)")
    print(f"    T12+T21                 = {list(T12T21_2x2)}  (Round 40)")
    print(f"    TORSION_E               = {list(torsion_2x2)}  (this round)")
    print(f"    cross_casimir           = {list(cc_2x2)}  (this round)")
    print(f"    SUM                     = {list(grand_total)} == Delta_2x2")
    print()
    print("  POST-SKEPTIC REWORD: individual per-piece values are now")
    print("  ASSERTED (previously only printed by Round 25 itself) -- a")
    print("  milestone for closing ROUND 25's OWN decomposition bookkeeping")
    print("  specifically, not for 'the L4A investigation' broadly (both FL")
    print("  Step 8a skeptics + synthesis independently flagged the original")
    print("  wording here as rhetorically inflated relative to content).")
    print()
    print("  HONEST LIMIT: Delta itself remains NON-scalar (asserted above,")
    print("  not just stated) -- this closure explains WHERE each piece of")
    print("  Delta's value comes from, it does NOT make Delta scalar, does")
    print("  NOT resolve the 8/45-vs-~1 L4A norm-bound tension (Round 24's")
    print("  own concern about whether R/4 can be cleanly isolated from")
    print("  Delta AT ALL is untouched by this bookkeeping), and does NOT")
    print("  touch preprint.tex.")


if __name__ == "__main__":
    main()
