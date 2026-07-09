"""
Rigorous calibration check for the rolling-map ansatz in
g2su3_V7_construction.py. For every pair i<j in 1..6, compute [M_i,M_j] as a
7x7 matrix commutator, then decompose its restriction to m (rows/cols 1..6)
as a combination of the 15 elementary bivectors e_a^e_b (a<b, 1<=a,b<=6) via
exact linear solve, and check whether the result lies ENTIRELY within the
8-dimensional span of the su(3) vector-action generators (su3_vector_action,
i=1..8) -- since h=su(3) is exactly the isotropy subalgebra (dim g2=14,
dim S^6=6, so dim(isotropy)=8=dim su(3), with NO extra u(1)), any residual
component orthogonal to su(3)'s image within so(6) signals an error in the
rolling-map ansatz (or a bug), not a legitimate extra term.
"""

import sympy as sp
from g2su3_V7_construction import (
    build_T_table,
    m_generator_matrix,
    su3_vector_action,
)

BIVECTORS = [(a, b) for a in range(1, 7) for b in range(a + 1, 7)]  # 15 of them


def bivector_vec6(a, b):
    """e_a ^ e_b as a 6-dim vector acting on... no, we need it as an
    ELEMENT of so(6) i.e. a 6x6 antisymmetric matrix, to compare against
    su3_vector_action's image as 6x6 matrices."""
    M = sp.zeros(6, 6)
    M[a - 1, b - 1] = 1
    M[b - 1, a - 1] = -1
    return M


def su3_gen_as_6x6(i):
    """su3_vector_action(i, .) as an explicit 6x6 matrix (acting on m only,
    ignoring the p-row/col which is always zero for su(3))."""
    M = sp.zeros(6, 6)
    for col in range(6):
        vec7 = sp.zeros(7, 1)
        vec7[col + 1] = 1
        out = su3_vector_action(i, vec7)
        for row in range(6):
            M[row, col] = out[row + 1]
    return M


def main():
    T = build_T_table()
    Ms = {i: sp.simplify(m_generator_matrix(i, T)) for i in range(1, 7)}
    S6x6 = [su3_gen_as_6x6(i) for i in range(1, 9)]

    # Build the 8 su(3) generators as vectors in the 15-dim bivector-coefficient
    # space (coefficient of e_a^e_b in each S_i, a<b).
    su3_coeff_matrix = sp.zeros(15, 8)
    for col, S in enumerate(S6x6):
        for row, (a, b) in enumerate(BIVECTORS):
            su3_coeff_matrix[row, col] = S[a - 1, b - 1]

    print(
        "su(3) generators expressed in the 15-dim bivector basis (rows=bivectors, cols=8 generators):"
    )
    sp.pprint(su3_coeff_matrix)

    print("\n" + "=" * 70)
    print("For each pair (i,j), decompose [M_i,M_j]|_m against su(3)'s image")
    print("=" * 70)
    for i, j in [(a, b) for a in range(1, 7) for b in range(a + 1, 7)]:
        comm = sp.simplify(Ms[i] * Ms[j] - Ms[j] * Ms[i])
        # restrict to m-block (rows/cols 1..6)
        comm_m = comm[1:7, 1:7]
        target = sp.zeros(15, 1)
        for row, (a, b) in enumerate(BIVECTORS):
            target[row] = comm_m[a - 1, b - 1]
        if all(sp.simplify(x) == 0 for x in target):
            continue  # trivial, skip printing
        # least-squares / exact solve: su3_coeff_matrix * x = target ?
        # use sympy's linsolve on the augmented system
        aug = su3_coeff_matrix.row_join(target)
        rank_A = su3_coeff_matrix.rank()
        rank_aug = aug.rank()
        consistent = rank_A == rank_aug
        print(
            f"\n[M_{i},M_{j}]|_m nonzero. rank(su3_basis)={rank_A}, rank(augmented)={rank_aug}, "
            f"consistent (residual-free)={consistent}"
        )
        if not consistent:
            print(f"  ** RESIDUAL DETECTED ** -- [M_{i},M_{j}] has a component")
            print("  outside su(3)'s image in so(6). Ansatz may be wrong.")
            print(f"  Target vector (bivector coeffs): {[sp.simplify(x) for x in target]}")


if __name__ == "__main__":
    main()
