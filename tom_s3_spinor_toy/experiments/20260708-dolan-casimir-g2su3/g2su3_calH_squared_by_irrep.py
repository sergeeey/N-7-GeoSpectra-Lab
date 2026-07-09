"""
Round 12 (2026-07-09): calH^2 = 4*D^2, decomposed per SU(3)-irreducible
piece within S+(x)S- (the physically relevant domain of D+, per
preprint.tex SS4.2's branching S+(x)S-|SU(3) = (1,1)+(0,1)+(1,0)+2x(0,0)).

Key fact this confirms: D_on_simple_tensor (calibrated, equivariance-
verified) computes EXACTLY (1/2)*calH, where calH is the CORRECT
asymmetric twisted analog of Kostant's cubic element H (Round 10 -- NOT
the wrong symmetric H(x)Id+Id(x)H guess from Round 9). D^0_twisted (the
true-derivative piece) is entirely absent from this computation -- see
decision.md Round 12 for why this doesn't invalidate L4B (rho=trivial
has D^0_twisted=0 anyway) but DOES mean these numbers are only the
algebraic part of D^2, not the full answer, for rho != trivial.
"""

import sympy as sp
from g2su3_equivariance_check import build_D_matrix64
from g2su3_explicit_clifford import IDX


def idx(a, b):
    return 8 * IDX[a] + IDX[b]


def main():
    D = build_D_matrix64()
    D2 = sp.simplify(D * D)

    print("=" * 70)
    print("'3' piece: {y1(x)1, y2(x)1, y3(x)1} (S+ 3-rep (x) S- singlet)")
    print("=" * 70)
    for a in [(1,), (2,), (3,)]:
        i = idx(a, ())
        print(f"  D2[y{a[0]}(x)1, same] = {D2[i, i]}")

    print("\n" + "=" * 70)
    print("'3bar' piece: {y123(x)y12, y123(x)y13, y123(x)y23}")
    print("=" * 70)
    for b in [(1, 2), (1, 3), (2, 3)]:
        i = idx((1, 2, 3), b)
        label = "y" + "".join(map(str, b))
        print(f"  D2[y123(x){label}, same] = {D2[i, i]}")

    print("\n" + "=" * 70)
    print("v_b = y123(x)1 (diagonal entry only -- full 2x2 trivial-mult")
    print("block also needs D2(v_b), not computed here)")
    print("=" * 70)
    i = idx((1, 2, 3), ())
    print(f"  D2[v_b,v_b] = {D2[i, i]}")

    print("\n" + "=" * 70)
    print("'8' piece: complement of v_a in the 9-dim {y1,y2,y3}(x){y12,y13,y23}")
    print("=" * 70)
    triple1 = [(1,), (2,), (3,)]
    triple2 = [(1, 2), (1, 3), (2, 3)]
    idxs9 = [idx(p, q) for p in triple1 for q in triple2]
    sub = sp.simplify(D2[idxs9, idxs9])
    print("9x9 submatrix of D^2 on this reducible (8+1) piece:")
    sp.pprint(sub)
    print("\nExpected structure: rank-1, nonzero ONLY on the v_a=(y1(x)y23-y2(x)y13")
    print("+y3(x)y12) direction (matching D2(v_a)=v_a+3*v_b projected back onto")
    print("this 9-dim slice, v_b being outside it) -- the 8-dim complement should")
    print("be annihilated identically by the algebraic (calH-only) part of D^2.")

    v_a_9 = sp.zeros(9, 1)
    v_a_9[2] = 1  # y1(x)y23
    v_a_9[4] = -1  # y2(x)y13
    v_a_9[6] = 1  # y3(x)y12
    result = sp.simplify(sub * v_a_9)
    print(f"\n  sub . v_a (9-dim, projected) = {list(result)}")
    print(f"  matches v_a itself (coefficient 1)? {sp.simplify(result - v_a_9) == sp.zeros(9, 1)}")

    rank = sub.rank()
    print(f"\n  rank(9x9 submatrix) = {rank} (expect 1)")


if __name__ == "__main__":
    main()
