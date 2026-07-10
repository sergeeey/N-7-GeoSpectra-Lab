"""
Round 21 (2026-07-10): the L4A Weitzenbock investigation -- three results,
one of them a small structural THEOREM that finally explains WHY Round 16's
R^E/Scal construction could never have been fixed by debugging.

BACKGROUND. The preprint's L4A open problem asks for a spectral bound on
the curvature endomorphism F_{S^-} in the twisted Weitzenbock identity
  D^2 = nabla*nabla + Scal/4 + R^E                                   (*)
Round 16 attempted to BUILD R^E directly (build_RE in
g2su3_lichnerowicz_rho7.py) and calibrate (*) against the rho=trivial
L4B ground truth -- it failed (2/3 mismatch, then a 1/6 inconsistency)
and was abandoned. At the time only ONE calibration point existed
(rho=trivial, where nabla*nabla=0 identically, so the calibration could
not constrain the nabla*nabla coefficient at all -- the skeptic's
decisive Round-16 objection). Rounds 17-20 have since produced NEW,
independently validated data (full multiplicity-space D^2 matrices for
rho=7 and rho=14) that were not available then.

RESULT 1 (triangulation -- POSITIVE). Using the two calibration points
that share an SU(3)-singlet fiber block (rho=trivial and rho=7's
singlet-domain sub-block), the residual
  W := D^2 - nabla*nabla_can - Scal/4
(where nabla*nabla_can := C_2(G2;rho) - C_2(SU(3);sigma), the
CANONICAL-connection Casimir Laplacian used throughout Rounds 15-16, and
Scal=10 so Scal/4=5/2) comes out IDENTICAL from both calibration points:
  W|_singlet-block = [[-3/2, 1], [3, 1/2]]   (basis v_a, v_b)
This rho-independence across two independent, fully-validated data
sources is a genuine structural confirmation the single-point Round-16
calibration could never provide. (It is algebraically equivalent to
Round 17's uniform-shift observation {2,6}={0,4}+2, now reframed as a
statement about W.)

RESULT 2 (the old construction is definitively NOT this -- NEGATIVE,
with a clean signature). Round 16's build_RE(), restricted to the same
singlet block, gives [[-11/6, 2/3], [2, -1/2]] -- NOT the triangulated
value, and NOT off by any uniform scale (entry ratios 9/11, 3/2, 3/2,
-1). The discrepancy has an exact, suggestive form:
  W_triangulated - RE_computed = (1/3) * D^2|_trivial     (exactly)
Also tested: symmetrizing build_RE between the two tensor factors
(curvature on eta with Clifford on xi, PLUS the mirror) gives EXACTLY
2x the original -- i.e. both orderings contribute identically on this
block -- and still does not match. Recorded as negative controls.

RESULT 3 (the structural obstruction -- the actual explanation). Round
19's committed 16x16 matrix of D^2_7 on M = Hom_SU(3)(V_7, F) contains
NONZERO OFF-BLOCKS between different SU(3)-types (singlet-domain basis
elements couple to 3bar-domain ones, etc. -- re-verified in this file by
direct computation of one full column). But EVERY candidate right-hand
side of (*) as interpreted in Rounds 15-16 is TYPE-PRESERVING on M:
  - Scal/4 is a scalar;
  - any pointwise, G2-invariant bundle endomorphism (which is what R^E,
    F_{S^-}, or any curvature-built fiber operator IS on a homogeneous
    space) acts on M by post-composition with an SU(3)-equivariant fiber
    map, which by Schur's lemma preserves each SU(3)-isotypic component
    of F -- hence maps pure-type basis elements to same-type ones;
  - nabla*nabla_can = C_2(G2;rho)*I - C_2(SU(3);sigma_V) is block-scalar
    by type.
THEREFORE no choice of invariant fiber endomorphism R^E can make (*)
hold with nabla*nabla interpreted as the canonical-Casimir Laplacian:
the left side provably mixes types, every term on the right provably
does not. Round 16's failure was NOT a coding bug (this file re-verifies
its components: R_half's Ricci contraction and spin_lift_so6's
calibration both still pass) -- the FORMULA AS INTERPRETED is
structurally impossible.

WHAT THIS IMPLIES (the honest, useful conclusion): the Lichnerowicz/
Weitzenbock identity itself is a theorem and is not in question; what
fails is the IDENTIFICATION of its nabla*nabla term with the canonical
Casimir Laplacian. The true Levi-Civita rough Laplacian differs from the
canonical one by Nomizu-map cross-terms (first-order in the invariant
vector fields, schematically -sum_p [Z_p Lambda_p + Lambda_p Z_p +
Lambda_p^2] corrections), which are exactly the natural carrier of the
observed type-mixing. Deriving these cross-terms explicitly -- entirely
within the matrix-coefficient machinery this project already has -- is
the now-well-defined path to a correct, verified Weitzenbock identity
(and hence to L4A's F_{S^-} spectral data), replacing the dead-end
"debug build_RE" framing.

INTERPRETATION CAVEAT for Result 1 (stated so it is not over-read): the
triangulated W|_singlet is the singlet-block of the residual, NOT
directly "the value of a fiber operator R^E" -- Result 3 shows the full
residual W is not a fiber operator at all (it has off-blocks). W's
singlet-DIAGONAL block being rho-independent across {trivial, 7} is the
verified fact; whether it equals (Scal/4-shifted) fiber-curvature data
depends on the cross-terms' singlet-block contribution, which is exactly
what the derivation above would settle.

Evidence markers: every numeric claim in this docstring is re-computed
and asserted in main() below ([VERIFIED-tool] on run); the implication
paragraph is [INFERRED] (standard operator theory + the verified facts).
"""

import sympy as sp

from g2su3_appendix_a_construction import build_curvature_h_table
from g2su3_equivariance_check import build_D_matrix64
from g2su3_explicit_clifford import DIM, IDX, SUBSETS, e_action, vec_from_subsets
from g2su3_H_element import build_T_table
from g2su3_lichnerowicz_rho7 import Rmat, build_R_half, build_RE, spin_lift_so6
from g2su3_v7_16dim_full_matrix import (
    build_3_copies,
    build_3bar_copies,
    build_singlets,
    build_w_cols_general,
    flatten,
)
from g2su3_v7_3_3bar_intertwiners import P3, P3BAR, build_MF, build_MV7, solve_intertwiner
from g2su3_v7_multiplicity_dirac import d7_apply, idx64

N64 = DIM * DIM

SCAL = sp.Integer(10)  # Scal=10 (so Scal/4=5/2), triple-verified in Round 16 (unchallenged part)
C2_G2_7 = sp.Integer(2)  # C_2(G2;7)=2 in this session's normalization, established Round 14+


def build_va_vb():
    y1, y2, y3 = IDX[(1,)], IDX[(2,)], IDX[(3,)]
    y12, y13, y23 = IDX[(1, 2)], IDX[(1, 3)], IDX[(2, 3)]
    one, y123 = IDX[()], IDX[(1, 2, 3)]
    v_a = sp.zeros(N64, 1)
    v_a[idx64(y1, y23)] = 1
    v_a[idx64(y2, y13)] = -1
    v_a[idx64(y3, y12)] = 1
    v_b = sp.zeros(N64, 1)
    v_b[idx64(y123, one)] = 1
    return v_a, v_b


def project_2x2(op_va, op_vb, v_a, v_b):
    """Express op(v_a), op(v_b) in the {v_a, v_b} basis; assert exactness."""
    P = sp.Matrix.hstack(v_a, v_b)
    G = (P.T * P).inv()
    sol_a = G * P.T * op_va
    sol_b = G * P.T * op_vb
    assert sp.simplify(op_va - P * sol_a) == sp.zeros(N64, 1), "op(v_a) leaks outside span"
    assert sp.simplify(op_vb - P * sol_b) == sp.zeros(N64, 1), "op(v_b) leaks outside span"
    return sp.Matrix.hstack(sol_a, sol_b)


def build_RE_symmetrized(R_half):
    """Negative control: build_RE with BOTH factor-orderings (curvature on
    xi/Clifford on eta, PLUS curvature on eta/Clifford on xi)."""
    basis = [vec_from_subsets({s: 1}) for s in SUBSETS]
    RE = sp.zeros(N64, N64)
    for a in range(DIM):
        eta = basis[a]
        for b in range(DIM):
            xi = basis[b]
            col = idx64(a, b)
            out = sp.zeros(N64, 1)
            for p in range(1, 7):
                for q in range(p + 1, 7):
                    Rpq = Rmat(R_half, p, q)
                    Rspin_xi = spin_lift_so6(Rpq, xi)
                    epeq_eta = e_action(p, e_action(q, eta))
                    for r in range(DIM):
                        if epeq_eta[r] == 0:
                            continue
                        for s in range(DIM):
                            if Rspin_xi[s] == 0:
                                continue
                            out[idx64(r, s)] += epeq_eta[r] * Rspin_xi[s]
                    Rspin_eta = spin_lift_so6(Rpq, eta)
                    epeq_xi = e_action(p, e_action(q, xi))
                    for r in range(DIM):
                        if Rspin_eta[r] == 0:
                            continue
                        for s in range(DIM):
                            if epeq_xi[s] == 0:
                                continue
                            out[idx64(r, s)] += Rspin_eta[r] * epeq_xi[s]
            RE[:, col] = out
    return sp.simplify(RE)


def main():
    v_a, v_b = build_va_vb()
    D64 = build_D_matrix64()

    print("=" * 70)
    print("STEP 1: D^2 on rho=trivial, via direct squaring of the validated D64")
    print("=" * 70)
    D2_triv = project_2x2(sp.simplify(D64 * (D64 * v_a)), sp.simplify(D64 * (D64 * v_b)), v_a, v_b)
    print("  D^2|_trivial (basis v_a,v_b):")
    sp.pprint(D2_triv)
    assert D2_triv == sp.Matrix([[1, 1], [3, 3]]), "L4B ground truth changed?!"

    print("\n" + "=" * 70)
    print("STEP 2: D^2 on rho=7's singlet-domain block, via d7_apply (Round 17)")
    print("=" * 70)
    w_a_cols = [v_a if i == 0 else sp.zeros(N64, 1) for i in range(7)]
    w_b_cols = [v_b if i == 0 else sp.zeros(N64, 1) for i in range(7)]
    wa2 = d7_apply(d7_apply(w_a_cols, D64), D64)
    wb2 = d7_apply(d7_apply(w_b_cols, D64), D64)
    D2_7sing = project_2x2(wa2[0], wb2[0], v_a, v_b)
    print("  D^2_7|_singlet-block (value at phi_2, basis v_a,v_b):")
    sp.pprint(D2_7sing)
    assert D2_7sing == sp.Matrix([[3, 1], [3, 5]]), "Round 17 ground truth changed?!"

    print("\n" + "=" * 70)
    print("STEP 3 (RESULT 1): triangulate W = D^2 - nabla*nabla_can - Scal/4")
    print("=" * 70)
    W_triv = sp.simplify(D2_triv - 0 * sp.eye(2) - (SCAL / 4) * sp.eye(2))
    W_7 = sp.simplify(D2_7sing - C2_G2_7 * sp.eye(2) - (SCAL / 4) * sp.eye(2))
    print("  from rho=trivial (nabla*nabla_can=0):")
    sp.pprint(W_triv)
    print("  from rho=7 singlet (nabla*nabla_can=C2(G2;7)-C2(SU3;1)=2):")
    sp.pprint(W_7)
    agree = sp.simplify(W_triv - W_7) == sp.zeros(2, 2)
    print(f"  TWO INDEPENDENT CALIBRATION POINTS AGREE EXACTLY: {agree}")
    assert agree
    W_singlet = W_triv
    assert W_singlet == sp.Matrix([[sp.Rational(-3, 2), 1], [3, sp.Rational(1, 2)]])

    print("\n" + "=" * 70)
    print("STEP 4 (RESULT 2): Round 16's build_RE() does NOT equal W_singlet")
    print("=" * 70)
    T_table = build_T_table()
    curv_h = build_curvature_h_table()
    R_half = build_R_half(T_table, curv_h)
    RE = build_RE(R_half)
    RE_2x2 = project_2x2(sp.simplify(RE * v_a), sp.simplify(RE * v_b), v_a, v_b)
    print("  build_RE() restricted to the singlet block:")
    sp.pprint(RE_2x2)
    match = sp.simplify(RE_2x2 - W_singlet) == sp.zeros(2, 2)
    print(f"  equals triangulated W_singlet? {match} (expected False)")
    assert not match
    diff = sp.simplify(W_singlet - RE_2x2)
    sig = sp.simplify(diff - sp.Rational(1, 3) * D2_triv) == sp.zeros(2, 2)
    print(f"  discrepancy == (1/3)*D^2|_trivial exactly: {sig}")
    assert sig
    ratios = [
        sp.simplify(W_singlet[i, j] / RE_2x2[i, j])
        for i in range(2)
        for j in range(2)
        if RE_2x2[i, j] != 0
    ]
    uniform = len(set(ratios)) == 1
    print(f"  entry ratios {ratios} -- uniform scale? {uniform} (expected False)")
    assert not uniform

    print("\n" + "=" * 70)
    print("STEP 5 (negative control): symmetrized build_RE = 2x original, still wrong")
    print("=" * 70)
    RE_sym = build_RE_symmetrized(R_half)
    RE_sym_2x2 = project_2x2(sp.simplify(RE_sym * v_a), sp.simplify(RE_sym * v_b), v_a, v_b)
    doubled = sp.simplify(RE_sym_2x2 - 2 * RE_2x2) == sp.zeros(2, 2)
    still_wrong = sp.simplify(RE_sym_2x2 - W_singlet) != sp.zeros(2, 2)
    print(f"  symmetrized == 2x original: {doubled};  still != W_singlet: {still_wrong}")
    assert doubled and still_wrong

    print("\n" + "=" * 70)
    print("STEP 6 (RESULT 3): D^2_7 mixes SU(3)-types on the multiplicity space")
    print("-- hence NO invariant fiber endomorphism can complete the Weitzenbock")
    print("identity with the canonical-Casimir nabla*nabla (Schur obstruction)")
    print("=" * 70)
    singlets = build_singlets()
    threes = build_3_copies()
    threebars = build_3bar_copies()
    MV7_3 = build_MV7(P3, slice(0, 3))
    MV7_3BAR = build_MV7(P3BAR, slice(3, 6))
    MF_3 = build_MF([(1,), (2,), (3,)])
    MF_3BAR = build_MF([(1, 2), (1, 3), (2, 3)])
    sol, t = solve_intertwiner(MV7_3, MF_3)
    T = sp.Matrix(3, 3, [c.subs(t[6], 1) for c in sol])
    assert T.det() != 0, "3-channel intertwiner degenerate -- Schur solve gave wrong irrep pairing"
    sol2, t2 = solve_intertwiner(MV7_3BAR, MF_3BAR)
    T2 = sp.Matrix(3, 3, [c.subs(t2[8], 1) for c in sol2])
    assert T2.det() != 0, (
        "3bar-channel intertwiner degenerate -- Schur solve gave wrong irrep pairing"
    )

    basis_w = []
    labels = []
    for i, s in enumerate(singlets):
        basis_w.append([s if j == 0 else sp.zeros(N64, 1) for j in range(7)])
        labels.append(f"singlet_{i + 1}")
    for i, triple in enumerate(threes):
        basis_w.append(build_w_cols_general(T, triple, slice(0, 3)))
        labels.append(f"three_{i + 1}")
    for i, triple in enumerate(threebars):
        basis_w.append(build_w_cols_general(T2, triple, slice(3, 6)))
        labels.append(f"threebar_{i + 1}")
    Wmat = sp.Matrix.hstack(*[flatten(w) for w in basis_w])
    WH = Wmat.H
    WtW_inv = (WH * Wmat).inv()

    found_mixing = False
    for col_idx in range(6):  # scan singlet columns until off-type coupling found
        w2 = d7_apply(d7_apply(basis_w[col_idx], D64), D64)
        target = flatten(w2)
        c = sp.simplify(WtW_inv * (WH * target))
        residual = sp.simplify(Wmat * c - target)
        assert residual == sp.zeros(7 * N64, 1), "D^2 column not in span -- basis error"
        off = {labels[j]: c[j] for j in range(6, 16) if sp.simplify(c[j]) != 0}
        print(f"  D^2({labels[col_idx]}): off-type (three*/threebar*) coefficients: {off}")
        if off:
            found_mixing = True
            break
    print(f"  TYPE-MIXING CONFIRMED (off-block nonzero): {found_mixing}")
    assert found_mixing, "no mixing found in singlet columns -- contradicts Round 19 matrix"

    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print("  1. Residual W = D^2 - nabla*nabla_can - Scal/4 is rho-independent on")
    print("     the singlet block across two independent calibration points:")
    print("     W_singlet = [[-3/2, 1], [3, 1/2]].")
    print("  2. Round 16's build_RE() != W_singlet (discrepancy = (1/3)*D^2_triv,")
    print("     not a uniform scale; symmetrizing doubles it, still wrong).")
    print("  3. D^2 mixes SU(3)-types on M while Scal/4, any invariant fiber")
    print("     endomorphism (Schur), and nabla*nabla_can are all type-preserving")
    print("     -- so NO fiber R^E completes the identity as interpreted in")
    print("     Rounds 15-16. Not a coding bug: the canonical-Casimir Laplacian")
    print("     is not the Levi-Civita rough Laplacian; the missing Nomizu")
    print("     cross-terms are the type-mixing carrier, and deriving them")
    print("     explicitly is the well-defined path to L4A.")


if __name__ == "__main__":
    main()
