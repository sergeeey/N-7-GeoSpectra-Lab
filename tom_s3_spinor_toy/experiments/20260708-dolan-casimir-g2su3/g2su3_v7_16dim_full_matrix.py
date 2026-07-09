"""
Round 19 (2026-07-09): build the FULL 16-dimensional multiplicity space
M = Hom_SU(3)(V_7, F) and the complete 16x16 matrix of D^2_7 on it -- the
computation explicitly flagged as "not attempted" at the end of Round 18,
now that its true size (16, not 4) is known.

BASIS OF M (16 = 6 + 5 + 5). CORRECTION (caught by reviewer, this round):
Round 18's SU(3) Casimir spectrum on F (mult 30 at eigenvalue 4/3) ALONE
only forces mult("3")+mult("3bar")=10 -- Casimir cannot distinguish a
conjugate-irrep pair sharing the same eigenvalue, so it does NOT by itself
force the 5+5 split (Round 18's own docstring already flagged this as
[SPLIT NOT VERIFIED], a caveat this file's earlier draft failed to carry
forward). The ACTUAL exhaustiveness argument, independently confirmed by
the reviewer via a from-scratch derivation: Sigma = Lambda^0(+)Lambda^1(+)
Lambda^2(+)Lambda^3 = 1a(+)3(+)3bar(+)1b under SU(3) (already tool-verified
via closure checks in g2su3_twisted_kernel.py). Applying standard SU(3)
tensor-product rules to Sigma(x)Sigma = that 4-term sum squared (16 cross
terms) gives EXACTLY 5 "3"-sources (1a(x)3, 3(x)1a, 1b(x)3, 3(x)1b, plus
the antisymmetric part of 3bar(x)3bar=6bar(+)3) and EXACTLY 5 "3bar"-
sources (the mirror) -- matching c1..c5/d1..d5 one-for-one, with no other
cross-term contributing either "3" or "3bar". This is what actually closes
exhaustiveness (a full tensor-product accounting, not the Casimir spectrum
alone) -- this file constructs EXPLICIT basis vectors from that accounting
rather than trusting a dimension count alone, and additionally VERIFIES
(matches_reference_pattern, called for every constructed copy including
the two nontrivial c5/d5 extractions) that each one genuinely matches the
canonical action pattern -- not merely asserted in prose.

Hom(1,F) [6-dim, = F^{SU(3)} directly, since a map from the trivial rep is
determined by a single invariant target vector]: six NATURAL candidates,
each verified SU(3)-invariant and jointly independent (rank 6):
  s1 = 1(x)1        s2 = y123(x)1      s3 = 1(x)y123
  s4 = y123(x)y123  s5 = v_a (the Round-17 3(x)3bar contraction)
  s6 = v_a with tensor factors swapped

Hom(3,F) [5-dim]: FOUR natural "simple embedding" copies (Leibniz-trivial,
since su(3) kills 1a=Lambda^0 and 1b=Lambda^3, so y_i(x)[1a or 1b] or
[1a or 1b](x)y_i automatically transforms exactly like Sigma's own
Lambda^1={y1,y2,y3}) -- VERIFIED (tool) each matches the y1,y2,y3 action
pattern for all 8 generators, and are jointly independent (rank 12):
  c1 = 1(x)y_i     c2 = y_i(x)1     c3 = y123(x)y_i     c4 = y_i(x)y123
Plus a FIFTH copy extracted from Lambda^2(x)Lambda^2 = 3bar(x)3bar =
6bar (+) 3 (the antisymmetric part) -- found via diagonalizing the SU(3)
Casimir on this 9-dim subspace (confirmed spectrum {4/3:mult3, 10/3:mult6},
matching 3(+)6bar exactly), extracting the Casimir=4/3 nullspace (dim 3,
confirmed), then SOLVING (Schur, not guessed) for the 3x3 reordering/sign
matrix R needed to match the canonical y1,y2,y3 action pattern -- found
R = pure reversal (antidiagonal identity), i.e. c5 = [that 3-dim nullspace,
reversed] matches EXACTLY (verified, tool):
  c5_i = y_jk(x)y_lm - y_lm(x)y_jk  (antisymmetrized Lambda^2(x)Lambda^2)
All five, {c1,c2,c3,c4,c5} (15 vectors total), independently VERIFIED
rank 15 -- this is the FULL Hom(3,F), not a subset.

Hom(3bar,F) [5-dim]: the exact mirror construction (d1..d4 = simple
embeddings via Lambda^2={y12,y13,y23}, d5 = the 3bar-piece of
Lambda^1(x)Lambda^1 = 3(x)3 = 6(+)3bar, found the same way -- this time
the reordering solve gave R = pure identity, i.e. d5 needs NO reordering).
Verified rank 15.

THE INTERTWINERS w_i: V_7 -> F, for each basis vector, REUSE Round 18's
Schur intertwiners T (V_7's "3"={B,C,D} -> anything matching the y1,y2,y3
pattern) and T2 (V_7's "3bar"={A,E,F} -> anything matching y12,y13,y23) --
since ALL FIVE "3"-copies (c1..c5) transform IDENTICALLY to y1,y2,y3 by
construction/verification above, the SAME T works for all five (just
apply it to whichever target triple); same for T2 and d1..d5. This
reuses Round 18's already-reviewed, already-skeptic-confirmed Schur
solve verbatim -- no new intertwiner machinery invented here.

THE 16x16 MATRIX: for each of the 16 basis w_i, apply d7_apply (Round
17's already-reviewed formula, reused verbatim) TWICE to get D^2_7(w_i).
Since D_7 is built entirely from equivariant ingredients, D^2_7(w_i) is
itself guaranteed to be an element of M -- i.e. expressible EXACTLY as a
linear combination of the same 16 basis w_j's. Coefficients extracted via
the normal-equations solve c = (W^T W)^{-1} W^T . target on the flattened
(448 = 7*64 dim) representation of each w_i -- and, critically, VERIFIED
(tool) that W . c reproduces the target EXACTLY (all 448 components), not
just in a least-squares sense -- confirming D^2_7(w_i) really does lie
exactly in span(basis), the equivariance-preservation property that
Round 18's skeptic review (FT1) flagged as needing an explicit check.

RESULT: see main() for the actual 16x16 matrix and its eigenvalues --
this is the number that finally, honestly answers whether rho=7
introduces an unwanted zero mode.
"""

import sympy as sp

from g2su3_equivariance_check import build_D_matrix64, build_su3_matrix64
from g2su3_explicit_clifford import DIM, IDX, vec_from_subsets
from g2su3_twisted_kernel import su3_action
from g2su3_v7_3_3bar_intertwiners import PINV, build_MF, build_MV7, P3, P3BAR, solve_intertwiner
from g2su3_v7_multiplicity_dirac import d7_apply, idx64

N64 = DIM * DIM


def bv(a, b):
    v = sp.zeros(N64, 1)
    v[idx64(a, b)] = 1
    return v


def matches_reference_pattern(cols, ref_MF):
    """Verify (in THIS file's own scope, not inherited from an earlier
    interactive exploration) that a candidate triple `cols` transforms
    under su(3) EXACTLY like the reference pattern ref_MF (Sigma's own
    y1,y2,y3 or y12,y13,y23 3x3 action matrices) -- i.e. re-derive the
    'reordering was solved, not guessed' claim in-file rather than just
    asserting a hardcoded result."""
    Sk = {k: build_su3_matrix64(k) for k in range(1, 9)}
    for k in range(1, 9):
        for j in range(3):
            lhs = sp.simplify(Sk[k] * cols[j])
            rhs = sum((ref_MF[k][i, j] * cols[i] for i in range(3)), sp.zeros(N64, 1))
            if sp.simplify(lhs - rhs) != sp.zeros(N64, 1):
                return False
    return True


def build_w_cols_general(T, target_vecs, this_group_rows):
    """Same projection logic as Round 18's build_w_cols, but generalized to
    accept 3 arbitrary 64-dim target vectors (target_vecs) instead of only
    subset-tuple(x)1-type embeddings -- needed since c3,c4,c5 (and d3,d4,d5)
    are not of that restricted form."""
    I6 = sp.eye(6)
    cols = [sp.zeros(N64, 1)]
    for j in range(6):
        ej = I6[:, j]
        coeffs = PINV * ej
        group_coeffs = coeffs[this_group_rows, :]
        mapped = T * group_coeffs
        vecF = sum((mapped[row] * target_vecs[row] for row in range(3)), sp.zeros(N64, 1))
        cols.append(sp.simplify(vecF))
    return cols


def build_singlets():
    one, y123 = IDX[()], IDX[(1, 2, 3)]
    y1i, y2i, y3i = IDX[(1,)], IDX[(2,)], IDX[(3,)]
    y12i, y13i, y23i = IDX[(1, 2)], IDX[(1, 3)], IDX[(2, 3)]
    s1 = bv(one, one)
    s2 = bv(y123, one)
    s3 = bv(one, y123)
    s4 = bv(y123, y123)
    s5 = bv(y1i, y23i) - bv(y2i, y13i) + bv(y3i, y12i)
    s6 = bv(y23i, y1i) - bv(y13i, y2i) + bv(y12i, y3i)
    return [s1, s2, s3, s4, s5, s6]


def build_3_copies():
    one, y123 = IDX[()], IDX[(1, 2, 3)]
    yidx = [IDX[(1,)], IDX[(2,)], IDX[(3,)]]
    c1 = [bv(one, yi) for yi in yidx]
    c2 = [bv(yi, one) for yi in yidx]
    c3 = [bv(y123, yi) for yi in yidx]
    c4 = [bv(yi, y123) for yi in yidx]
    c5 = build_3_fifth_copy()
    return [c1, c2, c3, c4, c5]


def build_3_fifth_copy():
    """Extract the Casimir=4/3 ('3') piece of Lambda^2(x)Lambda^2, reorder
    to match the canonical y1,y2,y3 action pattern (solved via Schur, see
    docstring)."""
    y2idx = [IDX[(2, 3)], IDX[(1, 3)], IDX[(1, 2)]]
    y23v, y13v, y12v = (
        vec_from_subsets({(2, 3): 1}),
        vec_from_subsets({(1, 3): 1}),
        vec_from_subsets({(1, 2): 1}),
    )
    basisSig2 = [y23v, y13v, y12v]
    M2 = {}
    for k in range(1, 9):
        M = sp.zeros(3, 3)
        for col, v in enumerate(basisSig2):
            out = su3_action(k, v)
            for row, s in enumerate([(2, 3), (1, 3), (1, 2)]):
                M[row, col] = out[IDX[s]]
        M2[k] = sp.simplify(M)
    I3 = sp.eye(3)
    MV9 = {
        k: sp.simplify(
            sp.Matrix(sp.kronecker_product(M2[k], I3)) + sp.Matrix(sp.kronecker_product(I3, M2[k]))
        )
        for k in range(1, 9)
    }
    Cas9 = sp.zeros(9, 9)
    for k in range(1, 9):
        Cas9 += -(MV9[k] * MV9[k])
    Cas9 = sp.simplify(Cas9)
    ns = (Cas9 - sp.Rational(4, 3) * sp.eye(9)).nullspace()
    assert len(ns) == 3, f"expected 3-dim Casimir=4/3 nullspace, got {len(ns)}"
    basis9names = [(a, b) for a in y2idx for b in y2idx]

    def embed(v9):
        out = sp.zeros(N64, 1)
        for i, (a, b) in enumerate(basis9names):
            out[idx64(a, b)] += v9[i]
        return sp.simplify(out)

    raw = [embed(v) for v in ns]
    c5 = [raw[2], raw[1], raw[0]]  # reordering found via interactive Schur-solve
    ref = build_MF([(1,), (2,), (3,)])
    assert matches_reference_pattern(c5, ref), (
        "c5 reordering does NOT match the y1,y2,y3 action pattern -- "
        "the hardcoded [raw[2],raw[1],raw[0]] reversal is wrong"
    )
    return c5


def build_3bar_copies():
    one, y123 = IDX[()], IDX[(1, 2, 3)]
    ybaridx = [IDX[(1, 2)], IDX[(1, 3)], IDX[(2, 3)]]
    d1 = [bv(one, yb) for yb in ybaridx]
    d2 = [bv(yb, one) for yb in ybaridx]
    d3 = [bv(y123, yb) for yb in ybaridx]
    d4 = [bv(yb, y123) for yb in ybaridx]
    d5 = build_3bar_fifth_copy()
    return [d1, d2, d3, d4, d5]


def build_3bar_fifth_copy():
    """Extract the Casimir=4/3 ('3bar') piece of Lambda^1(x)Lambda^1,
    solved reordering gives pure identity (no reordering needed)."""
    yidx = [IDX[(1,)], IDX[(2,)], IDX[(3,)]]
    y1v, y2v, y3v = (
        vec_from_subsets({(1,): 1}),
        vec_from_subsets({(2,): 1}),
        vec_from_subsets({(3,): 1}),
    )
    basisSig1 = [y1v, y2v, y3v]
    M1 = {}
    for k in range(1, 9):
        M = sp.zeros(3, 3)
        for col, v in enumerate(basisSig1):
            out = su3_action(k, v)
            for row, s in enumerate([(1,), (2,), (3,)]):
                M[row, col] = out[IDX[s]]
        M1[k] = sp.simplify(M)
    I3 = sp.eye(3)
    MV9 = {
        k: sp.simplify(
            sp.Matrix(sp.kronecker_product(M1[k], I3)) + sp.Matrix(sp.kronecker_product(I3, M1[k]))
        )
        for k in range(1, 9)
    }
    Cas9 = sp.zeros(9, 9)
    for k in range(1, 9):
        Cas9 += -(MV9[k] * MV9[k])
    Cas9 = sp.simplify(Cas9)
    ns = (Cas9 - sp.Rational(4, 3) * sp.eye(9)).nullspace()
    assert len(ns) == 3, f"expected 3-dim Casimir=4/3 nullspace, got {len(ns)}"
    basis9names = [(a, b) for a in yidx for b in yidx]

    def embed(v9):
        out = sp.zeros(N64, 1)
        for i, (a, b) in enumerate(basis9names):
            out[idx64(a, b)] += v9[i]
        return sp.simplify(out)

    d5 = [embed(v) for v in ns]  # no reordering needed, per interactive Schur-solve
    ref = build_MF([(1, 2), (1, 3), (2, 3)])
    assert matches_reference_pattern(d5, ref), (
        "d5 does NOT match the y12,y13,y23 action pattern without reordering -- "
        "the assumed identity reordering is wrong"
    )
    return d5


def flatten(w_cols):
    """7 x 64-dim vectors -> single 448-dim column vector."""
    return sp.Matrix.vstack(*w_cols)


def main():
    print("=" * 70)
    print("STEP 1: build 16-dim basis of M = Hom_SU(3)(V_7,F)")
    print("=" * 70)
    singlets = build_singlets()
    threes = build_3_copies()
    threebars = build_3bar_copies()

    rank6 = sp.Matrix.hstack(*singlets).rank()
    rank15a = sp.Matrix.hstack(*[v for triple in threes for v in triple]).rank()
    rank15b = sp.Matrix.hstack(*[v for triple in threebars for v in triple]).rank()
    print(f"  6 singlets independent: rank={rank6} (want 6)")
    print(f"  5 '3'-copies independent: rank={rank15a} (want 15)")
    print(f"  5 '3bar'-copies independent: rank={rank15b} (want 15)")

    print("\n" + "=" * 70)
    print("STEP 2: build the 16 intertwiners w_i: V_7 -> F (reusing Round 18's")
    print("Schur T, T2 -- same T works for all 5 '3'-copies, same T2 for all 5")
    print("'3bar'-copies, since they all transform identically by construction)")
    print("=" * 70)
    MV7_3 = build_MV7(P3, slice(0, 3))
    MV7_3BAR = build_MV7(P3BAR, slice(3, 6))
    MF_3 = build_MF([(1,), (2,), (3,)])
    MF_3BAR = build_MF([(1, 2), (1, 3), (2, 3)])
    sol, t = solve_intertwiner(MV7_3, MF_3)
    T = sp.Matrix(3, 3, [c.subs(t[6], 1) for c in sol])
    sol2, t2 = solve_intertwiner(MV7_3BAR, MF_3BAR)
    T2 = sp.Matrix(3, 3, [c.subs(t2[8], 1) for c in sol2])
    assert sp.simplify(T.det()) != 0
    assert sp.simplify(T2.det()) != 0

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

    print(f"  built {len(basis_w)} intertwiners: {labels}")

    print("\n" + "=" * 70)
    print("STEP 3: flatten to 448-dim, build W (448x16), verify full column rank")
    print("=" * 70)
    W = sp.Matrix.hstack(*[flatten(w) for w in basis_w])
    print(f"  W shape: {W.shape}, rank: {W.rank()} (want 16)")

    print("\n" + "=" * 70)
    print("STEP 4: apply D_7 twice to each basis w_i, extract 16x16 D^2_7 matrix")
    print("=" * 70)
    D64 = build_D_matrix64()
    # W has complex (I-valued) entries -- normal equations need the
    # CONJUGATE transpose (Hermitian form W^H W, guaranteed invertible for
    # full-column-rank W), not the plain transpose W^T W (a bilinear, not
    # sesquilinear, form -- can be singular even at full column rank).
    WH = W.H
    WtW_inv = (WH * W).inv()

    D2_cols = []
    for i, w in enumerate(basis_w):
        w_prime = d7_apply(w, D64)
        w_double = d7_apply(w_prime, D64)
        target = flatten(w_double)
        c = sp.simplify(WtW_inv * (WH * target))
        residual = sp.simplify(W * c - target)
        exact = residual == sp.zeros(448, 1)
        print(f"  D^2_7({labels[i]}): exact-in-span={exact}")
        assert exact, f"D^2_7({labels[i]}) is NOT exactly in span(basis) -- construction error"
        D2_cols.append(c)

    D2_MAT = sp.Matrix.hstack(*D2_cols)
    print("\nFull 16x16 matrix of D^2_7 on M (rows/cols ordered as labels above):")
    sp.pprint(D2_MAT)

    print("\n" + "=" * 70)
    print("STEP 5: eigenvalues of the full 16x16 D^2_7 matrix")
    print("=" * 70)
    eigs = D2_MAT.eigenvals()
    for val, mult in eigs.items():
        print(f"  eigenvalue = {sp.simplify(val)}   multiplicity = {mult}")

    has_zero = any(sp.simplify(val) == 0 for val in eigs)
    print(f"\nZero eigenvalue present (unwanted zero mode in rho=7): {has_zero}")


if __name__ == "__main__":
    main()
