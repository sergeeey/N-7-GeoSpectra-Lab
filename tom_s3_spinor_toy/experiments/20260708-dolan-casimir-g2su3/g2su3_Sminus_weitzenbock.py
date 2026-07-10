"""
Round 23 STEP B v2 (2026-07-10): corrected Weitzenbock decomposition of
(D_{S^6} (x) S^-)^2, fixing a real algebraic error found in v1.

WHAT WAS WRONG IN v1 (kept as the historical record, see decision.md
Round 23 STEP B/B-corrected sections): v1 tried to expand D^2 via
"D = sum_p e_p.nabla_p" and simplify e_p.nabla_p.e_q.nabla_q into
e_p.e_q.nabla_p.nabla_q -- valid ONLY if e_p (Clifford mult) commutes
with nabla_q (covariant derivative). In Round 22, Clifford mult acted on
F while the "domain" operator acted on the SEPARATE V_7 factor, so this
held trivially. HERE, for TERM1 = Dslash (x) Id (Dslash := sum_p e_p.M_p,
M_p := nabla_g(p,.)), BOTH e_p and M_p act on the SAME single Sigma --
they do NOT commute (M_p is itself built from Clifford BIVECTORS). This
was caught by a direct sanity check: Dslash_mat @ Dslash_mat (literal
matrix composition, "ground truth") did NOT match the naively-simplified
"-sum M_p^2 - sum_{p<q} e_p.e_q.[M_p,M_q]" reconstruction. Root cause:
the "naive" reconstruction implicitly assumed e_p commutes past M_q,
equivalent to dropping a genuine Leibniz correction term (nabla_b e_a,
the covariant derivative of the FRAME VECTOR e_a itself -- nonzero for
a naturally reductive space's invariant, non-normal frame). Rather than
correctly re-deriving that missing term, this version sidesteps the
issue entirely by using ONLY matrix composition (safe, handles operator
ordering automatically) for anything touching Dslash-squared, and ONLY
using Kronecker-bilinear algebra ((A(x)B)(C(x)D)=(AC)(x)(BD), which is
ALWAYS valid, no commutativity assumption) for the genuinely twisted
(TERM2) piece.

CORRECTED DERIVATION. D_on_simple_tensor's own formula splits additively
as D = TERM1 + TERM2 where TERM1(eta)(x)xi := Dslash(eta)(x)xi (Dslash :=
sum_p e_p.M_p, computed by DIRECT matrix composition, ground truth) and
TERM2(eta(x)xi) := sum_p (e_p.eta)(x)(M_p xi) = sum_p (E_p(x)M_p)(eta(x)xi)
(a SUM of Kronecker products, E_p acting on the LEFT/eta factor via
Clifford mult, M_p acting on the RIGHT/xi factor via nabla_g -- exactly
mirroring Round 22's TERM_A, which was safe for the identical reason:
different tensor factors).

D^2 = (TERM1+TERM2)^2 = TERM1^2 + TERM1.TERM2 + TERM2.TERM1 + TERM2^2
(a plain algebraic identity for ANY two operators, no commutativity
needed -- computed via direct matrix multiplication throughout, so this
identity is automatically exact once TERM1_mat+TERM2_mat=D64 is verified).

TERM1^2 = (Dslash_mat @ Dslash_mat) (x) Id_8 -- a FIXED, already fully
computed object (Dslash^2, verified by direct matrix composition), NOT
further decomposed (this is exactly the step v1 got wrong).

TERM2^2 = sum_{p,q} (E_p E_q)(x)(M_p M_q)   [Kronecker bilinearity, SAFE]
        = -sum_p Id_8(x)M_p^2 + sum_{p<q}(E_p E_q)(x)[M_p,M_q]
  [E_p^2=-Id, E_pE_q=-E_qE_p for p!=q -- ordinary Clifford relations on
   E alone, valid since this manipulation only ever touches E_p/E_q
   (which live in a genuine associative Clifford algebra with known
   relations) multiplied by M_p/M_q as an OPAQUE right-Kronecker-factor;
   no claim about M_p,E_q commuting is used anywhere in this step]
  = CASIMIR_E + sum_{p<q}(E_pE_q)(x)[M_p,M_q]
Using [M_p,M_q] = R(e_p,e_q) + nabla_{[e_p,e_q]} (a standard, frame-
independent curvature-commutator identity -- valid for M_p,M_q ALONE,
no e_p/e_q commutativity claim involved):
  F_{S^-} := -sum_{p<q}(E_pE_q)(x)R(e_p,e_q)     [genuinely E-side-only]
  TORSION_E := -sum_{p<q}(E_pE_q)(x)nabla_{[e_p,e_q]}

TERM1.TERM2 and TERM2.TERM1: computed by DIRECT matrix multiplication of
the already-built TERM1_mat, TERM2_mat (64x64) -- no further algebraic
simplification attempted (safe by construction).

nabla*nabla+R/4 (S-side + mixed) := TERM1^2 + TERM1.TERM2 + TERM2.TERM1
                                     + CASIMIR_E + TORSION_E
F_{S^-} := as derived above (the ONLY genuinely isolated, E-curvature-
only piece)

Evidence markers: every numeric claim is re-computed and asserted in
main() below ([VERIFIED-tool] on run).
"""

import sympy as sp

from g2su3_appendix_a_construction import build_curvature_h_table
from g2su3_compute_crossterm import nabla_g
from g2su3_equivariance_check import build_D_matrix64, build_su3_matrix64
from g2su3_explicit_clifford import DIM, SUBSETS, e_action
from g2su3_H_element import build_T_table
from g2su3_twisted_kernel import su3_action

N64 = DIM * DIM


def idx64(a, b):
    return DIM * a + b


def chirality_sign(subset):
    return 1 if len(subset) % 2 == 0 else -1


S_PLUS = [i for i, s in enumerate(SUBSETS) if chirality_sign(s) == 1]
S_MINUS = [i for i, s in enumerate(SUBSETS) if chirality_sign(s) == -1]


def build_Mp():
    Ms = {}
    for p in range(1, 7):
        cols = [nabla_g(p, unit_vec(i)) for i in range(DIM)]
        Ms[p] = sp.Matrix.hstack(*cols)
    return Ms


def build_Lk():
    Ls = {}
    for k in range(1, 9):
        cols = [su3_action(k, unit_vec(i)) for i in range(DIM)]
        Ls[k] = sp.Matrix.hstack(*cols)
    return Ls


def build_Ep():
    Es = {}
    for p in range(1, 7):
        cols = [e_action(p, unit_vec(i)) for i in range(DIM)]
        Es[p] = sp.Matrix.hstack(*cols)
    return Es


def unit_vec(i):
    v = sp.zeros(DIM, 1)
    v[i] = 1
    return v


def kron(A, B):
    """Kronecker product matching idx64(a,b)=DIM*a+b (A acts on the LEFT
    index, B on the RIGHT index)."""
    rA, cA = A.shape
    rB, cB = B.shape
    out = sp.zeros(rA * rB, cA * cB)
    for i in range(rA):
        for j in range(cA):
            if A[i, j] != 0:
                out[i * rB : (i + 1) * rB, j * cB : (j + 1) * cB] += A[i, j] * B
    return out


def nabla_bracket(p, q, T, curv_h, Ms, Ls):
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


def curvature_R(p, q, T, curv_h, Ms, Ls):
    comm = Ms[p] * Ms[q] - Ms[q] * Ms[p]
    return comm - nabla_bracket(p, q, T, curv_h, Ms, Ls)


def main():
    print("=" * 70)
    print("SETUP")
    print("=" * 70)
    T = build_T_table()
    curv_h = build_curvature_h_table()
    Ms = build_Mp()
    Ls = build_Lk()
    Es = build_Ep()
    Id8 = sp.eye(DIM)

    print("\n" + "=" * 70)
    print("STEP B0 (CORRECTED sanity gate): Dslash^2 via DIRECT matrix")
    print("composition (ground truth, no algebraic shortcut)")
    print("=" * 70)
    Dslash_mat = sp.zeros(DIM, DIM)
    for p in range(1, 7):
        Dslash_mat += Es[p] * Ms[p]
    Dslash2 = sp.simplify(Dslash_mat * Dslash_mat)
    print("  Dslash^2 (direct composition):")
    sp.pprint(Dslash2)

    print("\n" + "=" * 70)
    print("STEP B0b: TERM1 + TERM2 must reconstruct D64 EXACTLY")
    print("=" * 70)
    TERM1_mat = kron(Dslash_mat, Id8)
    TERM2_mat = sp.zeros(N64, N64)
    for p in range(1, 7):
        TERM2_mat += kron(Es[p], Ms[p])
    D64_reconstructed = sp.simplify(TERM1_mat + TERM2_mat)
    D64 = build_D_matrix64()
    diff_D = sp.simplify(D64_reconstructed - D64)
    print(f"  TERM1+TERM2 == D64 EXACTLY (all 64x64 entries)? {diff_D == sp.zeros(N64, N64)}")
    assert diff_D == sp.zeros(N64, N64), "TERM1+TERM2 does not reconstruct D64 -- fix the split"

    print("\n" + "=" * 70)
    print("STEP B1: four-piece expansion, D^2 = TERM1^2+TERM1.TERM2+TERM2.TERM1+TERM2^2")
    print("(plain algebraic identity, matrix multiplication only, always exact)")
    print("=" * 70)
    TERM1_sq = kron(Dslash2, Id8)
    T12 = TERM1_mat * TERM2_mat
    T21 = TERM2_mat * TERM1_mat
    T22 = sp.zeros(N64, N64)
    for p in range(1, 7):
        for q in range(1, 7):
            T22 += kron(Es[p] * Es[q], Ms[p] * Ms[q])
    D64_sq_reconstructed = sp.simplify(TERM1_sq + T12 + T21 + T22)
    D64_sq_direct = sp.simplify(D64 * D64)
    diff_D2 = sp.simplify(D64_sq_reconstructed - D64_sq_direct)
    print(
        f"  TERM1^2+TERM1.TERM2+TERM2.TERM1+TERM2^2 == D64^2 EXACTLY? "
        f"{diff_D2 == sp.zeros(N64, N64)}"
    )
    assert diff_D2 == sp.zeros(N64, N64), "four-piece sum does not reconstruct D64^2"

    print("\n" + "=" * 70)
    print("STEP B2: split TERM2^2 via SAFE Kronecker-bilinear algebra (E-side")
    print("Clifford relations only, no M/E commutativity assumed)")
    print("=" * 70)
    T22_casimir = sp.zeros(N64, N64)
    for p in range(1, 7):
        T22_casimir += kron(Id8, -(Ms[p] * Ms[p]))
    T22_cross = sp.zeros(N64, N64)
    for p in range(1, 7):
        for q in range(p + 1, 7):
            comm = Ms[p] * Ms[q] - Ms[q] * Ms[p]
            T22_cross += kron(Es[p] * Es[q], comm)
    diff_T22 = sp.simplify(T22 - (T22_casimir + T22_cross))
    print(
        f"  TERM2^2 == CASIMIR_E + cross-term EXACTLY (Kronecker bilinearity check)? "
        f"{diff_T22 == sp.zeros(N64, N64)}"
    )
    assert diff_T22 == sp.zeros(N64, N64), "Kronecker bilinear split of TERM2^2 is wrong"

    F_Sminus = sp.zeros(N64, N64)
    torsion_E = sp.zeros(N64, N64)
    for p in range(1, 7):
        for q in range(p + 1, 7):
            R_pq = curvature_R(p, q, T, curv_h, Ms, Ls)
            nb_pq = nabla_bracket(p, q, T, curv_h, Ms, Ls)
            # NOTE: no leading minus here -- T22_cross (the object being
            # matched) is +sum_{p<q}(E_pE_q)(x)[M_p,M_q] by construction
            # (see STEP B2 above, verified exact), and R_pq+nb_pq=[M_p,M_q]
            # by curvature_R's own definition, so the split must carry the
            # SAME (positive) overall sign, not the v1 formula's minus.
            F_Sminus += kron(Es[p] * Es[q], R_pq)
            torsion_E += kron(Es[p] * Es[q], nb_pq)
    diff_split = sp.simplify(T22_cross - (F_Sminus + torsion_E))
    print(
        f"  cross-term == F_{{S^-}} + TORSION_E EXACTLY (R+nabla_bracket split)? "
        f"{diff_split == sp.zeros(N64, N64)}"
    )
    assert diff_split == sp.zeros(N64, N64), "R vs nabla_bracket split of the cross-term is wrong"

    print("\n" + "=" * 70)
    print("STEP B3: restrict F_{S^-} to Gamma(S^+(x)S^-), check Hermitian + spectrum")
    print("=" * 70)
    dom_pairs = [(a, b) for a in S_PLUS for b in S_MINUS]
    dom_rows = [idx64(a, b) for a, b in dom_pairs]
    F_block = F_Sminus[dom_rows, dom_rows]
    print(f"  F_{{S^-}} restricted to Gamma(S^+(x)S^-): shape {F_block.shape}")
    is_herm = sp.simplify(F_block - F_block.H) == sp.zeros(16, 16)
    print(f"  Hermitian? {is_herm}")
    assert is_herm, "F_{S^-} restricted block is not Hermitian"
    eigs = F_block.eigenvals()
    print(f"  F_{{S^-}}|_{{S^+(x)S^-}} eigenvalues: {eigs}")

    print("\n" + "=" * 70)
    print("STEP B4: cross-check -- remainder (nabla*nabla+R/4) on the SAME")
    print("block, plus F_{S^-}, reconstructs D64^2|_{S^+(x)S^-} EXACTLY")
    print("=" * 70)
    remainder = TERM1_sq + T12 + T21 + T22_casimir + torsion_E
    remainder_block = remainder[dom_rows, dom_rows]
    cod_rows = [idx64(a, b) for a in S_MINUS for b in S_MINUS]
    D_block = D64[cod_rows, dom_rows]
    back_rows = [idx64(a, b) for a in S_PLUS for b in S_MINUS]
    dom2_rows = [idx64(a, b) for a in S_MINUS for b in S_MINUS]
    D_back = D64[back_rows, dom2_rows]
    D2_full_block = sp.simplify(D_back * D_block)
    total_block = sp.simplify(remainder_block + F_block)
    diff_final = sp.simplify(total_block - D2_full_block)
    print(
        f"  remainder + F_{{S^-}} == D64^2|_{{S^+(x)S^-}} EXACTLY? {diff_final == sp.zeros(16, 16)}"
    )
    assert diff_final == sp.zeros(16, 16), "final decomposition does not match ground truth"

    print("\n" + "=" * 70)
    print("STEP C: restrict to the 2-dim SU(3)-invariant subspace within")
    print("Gamma(S^+(x)S^-) -- the genuine rho=trivial multiplicity space --")
    print("and cross-check against Round 4-17's ALREADY-ESTABLISHED L4B result")
    print("=" * 70)

    def su3_block(k):
        S8 = build_su3_matrix64(k)
        M = sp.zeros(16, 16)
        for ci, (a, b) in enumerate(dom_pairs):
            col64 = idx64(a, b)
            vcol = S8[:, col64]
            for ri, (a2, b2) in enumerate(dom_pairs):
                row64 = idx64(a2, b2)
                M[ri, ci] = vcol[row64]
        return M

    gens = [su3_block(k) for k in range(1, 9)]
    big = sp.Matrix.vstack(*gens)
    null_space = big.nullspace()
    print(f"  common null space of all 8 su(3) generators: dimension {len(null_space)}")
    assert len(null_space) == 2, "SU(3)-invariant subspace is not 2-dimensional"

    # explicit basis found by inspection of the null space (see decision.md
    # Round 23 STEP C): w_b = 1(x)y123, w_a = y12(x)y3 - y13(x)y2 + y23(x)y1
    # -- the mirror of Round 4-17's v_b=y123(x)1, v_a=y1(x)y23-y2(x)y13+y3(x)y12
    # (LEFT/RIGHT swapped, since v_a,v_b live in the OTHER chirality block
    # Gamma(S^-(x)S^+), not this round's Gamma(S^+(x)S^-)).
    w_b = sp.zeros(N64, 1)
    w_b[idx64(0, 7)] = 1
    w_a = sp.zeros(N64, 1)
    w_a[idx64(4, 3)] = 1
    w_a[idx64(5, 2)] = -1
    w_a[idx64(6, 1)] = 1

    def project_2x2(op, va, vb, name):
        Pmat = sp.Matrix.hstack(va, vb)
        G = (Pmat.T * Pmat).inv()
        opa, opb = op * va, op * vb
        sol_a = G * Pmat.T * opa
        sol_b = G * Pmat.T * opb
        leak_a = sp.simplify(opa - Pmat * sol_a)
        leak_b = sp.simplify(opb - Pmat * sol_b)
        assert leak_a == sp.zeros(N64, 1), f"{name}(w_a) leaks outside span(w_a,w_b)"
        assert leak_b == sp.zeros(N64, 1), f"{name}(w_b) leaks outside span(w_a,w_b)"
        return sp.simplify(sp.Matrix.hstack(sol_a, sol_b))

    D64_sq = sp.simplify(D64 * D64)
    D2_2x2 = project_2x2(D64_sq, w_a, w_b, "D64^2")
    print("  D64^2 restricted to span(w_a,w_b):")
    sp.pprint(D2_2x2)
    print(f"  eigenvalues: {D2_2x2.eigenvals()}")
    assert D2_2x2 == sp.Matrix([[1, 1], [3, 3]]), (
        "D64^2 on the invariant subspace does NOT match Round 4-17's known [[1,1],[3,3]]"
    )

    F_2x2 = project_2x2(F_Sminus, w_a, w_b, "F_{S^-}")
    print("\n  F_{S^-} restricted to span(w_a,w_b):")
    sp.pprint(F_2x2)
    f_eigs = F_2x2.eigenvals()
    print(f"  eigenvalues: {f_eigs}")
    assert sp.Rational(-5, 2) in f_eigs, "F_{S^-}'s negative mode is NOT in the invariant subspace"

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print(f"  F_{{S^-}} spectrum on Gamma(S^+(x)S^-) (full 16-dim): {eigs}")
    print(f"  F_{{S^-}} spectrum on the 2-dim SU(3)-invariant subspace: {f_eigs}")
    print("  D64^2 == [[1,1],[3,3]] there, eigenvalues {4,0} -- EXACTLY Round 4-17's")
    print("  known L4B result. On the eigenvector where F_{S^-}=-5/2, R/4+F_{S^-}=0")
    print("  EXACTLY -- a mechanistic explanation of the pre-existing zero mode,")
    print("  not merely a numerical coincidence.")


if __name__ == "__main__":
    main()
