"""
Find the explicit SU(3)-invariant vector v_a in span{y1,y2,y3} (x) span{y12,y13,y23}
(9-dimensional tensor product space, decomposing as 8 (+) 1 under SU(3)).

Approach: solve directly for the 1-dimensional kernel of all 8 su(3) generators
acting via Leibniz rule on the tensor product -- no need to pre-classify 3 vs
3bar abstractly.
"""

import sympy as sp
from g2su3_twisted_kernel import su3_action
from g2su3_explicit_clifford import IDX, vec_from_subsets

TRIPLE1 = [(1,), (2,), (3,)]  # y1,y2,y3 basis
TRIPLE2 = [(1, 2), (1, 3), (2, 3)]  # y12,y13,y23 basis


def tensor_action_matrix(i):
    """9x9 matrix of su(3) generator nu_i acting on span(TRIPLE1) (x) span(TRIPLE2)
    via Leibniz rule, in the basis ordered (a,b) for a in TRIPLE1, b in TRIPLE2."""
    basis1 = [vec_from_subsets({s: 1}) for s in TRIPLE1]
    basis2 = [vec_from_subsets({s: 1}) for s in TRIPLE2]

    # action of nu_i on each basis1 element, expressed in TRIPLE1 coords
    act1 = []
    for v in basis1:
        out = su3_action(i, v)
        coords = [sp.simplify(out[IDX[s]]) for s in TRIPLE1]
        act1.append(coords)

    act2 = []
    for v in basis2:
        out = su3_action(i, v)
        coords = [sp.simplify(out[IDX[s]]) for s in TRIPLE2]
        act2.append(coords)

    # 9x9 matrix for Leibniz action on tensor product, basis order (a_p, b_q) p,q=0,1,2
    M = sp.zeros(9, 9)
    for p in range(3):
        for q in range(3):
            row = 3 * p + q
            # d/d(nu_i) (a_p (x) b_q) = (nu_i.a_p) (x) b_q + a_p (x) (nu_i.b_q)
            for p2 in range(3):
                c = act1[p][p2]
                if c != 0:
                    M[row, 3 * p2 + q] += c
            for q2 in range(3):
                c = act2[q][q2]
                if c != 0:
                    M[row, 3 * p + q2] += c
    return M


def main():
    print("=" * 70)
    print("Finding SU(3)-invariant in span{y1,y2,y3} (x) span{y12,y13,y23}")
    print("=" * 70)

    # Stack all 8 generator matrices and find common kernel
    big = sp.zeros(9 * 8, 9)
    for i in range(1, 9):
        M = tensor_action_matrix(i)
        big[9 * (i - 1) : 9 * i, :] = M

    ns = big.nullspace()
    print(f"\nDimension of common kernel (should be 1 for the invariant): {len(ns)}")
    for v in ns:
        v = sp.simplify(v)
        print("\nInvariant vector (coords in basis y_p (x) y_q, p in {1,2,3}, q in {12,13,23}):")
        for p in range(3):
            for q in range(3):
                c = v[3 * p + q]
                if c != 0:
                    print(f"  y{TRIPLE1[p][0]} (x) y{''.join(str(x) for x in TRIPLE2[q])} : {c}")


if __name__ == "__main__":
    main()
