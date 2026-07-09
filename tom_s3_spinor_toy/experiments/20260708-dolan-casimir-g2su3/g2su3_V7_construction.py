"""
Step 1-4 of the rho=7 plan (decision.md, 2026-07-09): construct the action
of g2 = su(3) (+) m on the 7-dim fundamental representation V_7 = R p (+) m,
via the standard "rolling map" ansatz for the isotropy representation of a
naturally reductive space embedded in its ambient orthogonal group:

  e_i . p     = e_i                                  (i in m, moves p)
  e_i . e_j   = -delta_ij * p + [e_i,e_j]_m           (i,j in m)
  su3_gen . p = 0                                     (isotropy fixes p)
  su3_gen . e_j = (vector-rep action, already known)

where [e_i,e_j]_m = sum_k T(i,j,k) e_k, T already computed and independently
cross-checked against AHL2023 Prop 5.4's Ambrose-Singer torsion this session
(g2su3_H_element.py).

THIS ANSATZ IS [INFERRED], not lifted verbatim from a cited theorem -- it is
the standard formula for how a tangent-space Lie algebra element acts on the
ambient rep of a naturally reductive space (the isotropy-complement direction
X, viewed as an ambient rotation generator, satisfies X.p=X by definition of
"tangent to the orbit at p", and X.Y for Y in m decomposes into a "-<X,Y>p"
curvature-normal term forced by X.Y and X.p both being derivatives of the
SAME orbit map, plus the torsion term already known).

MANDATORY CALIBRATION (per this session's established discipline: never
trust a newly-derived ansatz before checking it against something already
verified): the resulting 6 operators M_1..M_6 (for e_1..e_6) together with
the 8 su(3) operators must satisfy the g2 Lie algebra structure -- in
particular [M_i, M_j] must be expressible as (su(3)-part, giving the
previously-missing curvature Jac_h data) + (m-part, which by the Jacobi
identity of the full bracket must be compatible with T). We check this
DIRECTLY by computing [M_i,M_j] as a matrix commutator and inspecting its
structure, rather than assuming the ansatz is correct.

If this calibration fails (extra terms neither in su(3)'s image nor
consistent with T), THIS ANSATZ IS WRONG and must not be used for the rho=7
kernel computation -- stop and report, do not force a fit.
"""

import sympy as sp
from g2su3_H_element import bivector_on_vector6, torsion_T
from g2su3_twisted_kernel import SU3_GENERATORS

sqrt = sp.sqrt

# V_7 basis: index 0 = p, indices 1..6 = e_1..e_6 (m directions)
V7_DIM = 7


def su3_vector_action(i, vec7):
    """su(3) generator i (1..8) acting on V_7 = R p (+) m: fixes p (isotropy
    definition), acts on the m-part via the SAME bivector data used for the
    spinor su3_action, but now lifted as a VECTOR (so(6)) action instead of
    a spin(6) action -- i.e. bivector_on_vector6 instead of the Clifford
    spin lift."""
    terms = SU3_GENERATORS[i]
    coeff = sp.Rational(1, 2) if i != 8 else sp.Rational(1, 2) / sqrt(3)
    m_in = vec7[1:7, :]  # 6-dim m part
    out_m = sp.zeros(6, 1)
    for sign, a, b in terms:
        out_m += sign * bivector_on_vector6(a, b, m_in)
    out_m = coeff * out_m
    out = sp.zeros(V7_DIM, 1)
    out[1:7, :] = out_m  # p-component stays 0
    return out


def build_T_table():
    T = {}
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                val = torsion_T(i, j, k)
                if val != 0:
                    T[(i, j, k)] = val
    return T


def m_generator_matrix(i, T):
    """M_i: 7x7 matrix for e_i (i in 1..6) acting on V_7, basis (p,e1..e6)."""
    M = sp.zeros(V7_DIM, V7_DIM)
    # e_i . p = e_i  => column 0 (input p) gets 1 at row i
    M[i, 0] = 1
    # e_i . e_j = -delta_ij p + sum_k T(i,j,k) e_k
    for j in range(1, 7):
        M[0, j] += -1 if i == j else 0
        for k in range(1, 7):
            val = T.get((i, j, k), 0)
            if val != 0:
                M[k, j] += val
    return M


def su3_matrix(i):
    """8 su(3) generator matrices as 7x7 operators on V_7 (columns = action
    on each basis vector e_0=p, e_1..e_6)."""
    M = sp.zeros(V7_DIM, V7_DIM)
    basis = [sp.zeros(V7_DIM, 1) for _ in range(V7_DIM)]
    for idx in range(V7_DIM):
        basis[idx][idx] = 1
    for col in range(V7_DIM):
        out = su3_vector_action(i, basis[col])
        for row in range(V7_DIM):
            M[row, col] = out[row]
    return M


def main():
    print("=" * 70)
    print("Building m-generator matrices M_1..M_6 on V_7 (rolling-map ansatz)")
    print("=" * 70)
    T = build_T_table()
    Ms = {i: sp.simplify(m_generator_matrix(i, T)) for i in range(1, 7)}
    for i in range(1, 7):
        print(f"\nM_{i} =")
        sp.pprint(Ms[i])

    print("\n" + "=" * 70)
    print("Building su(3) generator matrices (8 generators) on V_7")
    print("=" * 70)
    S = {i: sp.simplify(su3_matrix(i)) for i in range(1, 9)}

    print("\n" + "=" * 70)
    print("CALIBRATION 1: su(3) closure -- [S_i,S_j] should be a real linear")
    print("combination of S_1..S_8 with su(3) structure constants (spot check)")
    print("=" * 70)
    # spot check [S_1, S_2] against known su(3) structure (just report, since
    # we don't have independently-verified su(3) structure constants handy;
    # main point is it should act as ZERO on p and stay within span(S_i))
    comm12 = sp.simplify(S[1] * S[2] - S[2] * S[1])
    print("[S_1,S_2] acting on p (row0,col0 block) -- should be all zero (isotropy closes):")
    sp.pprint(comm12[:, 0])

    print("\n" + "=" * 70)
    print("CALIBRATION 2 (the critical one): [M_i,M_j] structure")
    print("=" * 70)
    print("Computing [M_1,M_2] and inspecting its action on p and on m...")
    comm = sp.simplify(Ms[1] * Ms[2] - Ms[2] * Ms[1])
    print("\n[M_1,M_2] full matrix:")
    sp.pprint(comm)
    print("\n[M_1,M_2] acting on p (column 0) -- MUST be 0 (m-part of bracket of")
    print("two m-elements must fix... wait, must check: [e1,e2] as a g2 element")
    print("decomposes into h-part (which fixes p, since h=su(3) is the isotropy)")
    print("plus m-part (which does NOT fix p in general, since m-elements move p).")
    print("So [M1,M2] acting on p should give exactly the M-part's action on p,")
    print("i.e. should equal sum_k T(1,2,k) * (M_k acting on p) = sum_k T(1,2,k)*e_k:")
    col0 = comm[:, 0]
    sp.pprint(col0)
    predicted = sp.zeros(V7_DIM, 1)
    for k in range(1, 7):
        val = T.get((1, 2, k), 0)
        if val != 0:
            predicted[k] = val
    print("\nPredicted (sum_k T(1,2,k) e_k, i.e. rho([e1,e2]_m) acting on p):")
    sp.pprint(predicted)
    match = sp.simplify(col0 - predicted) == sp.zeros(V7_DIM, 1)
    print(f"\nMatch (col0 of [M1,M2] vs predicted m-part-only prediction): {match}")


if __name__ == "__main__":
    main()
