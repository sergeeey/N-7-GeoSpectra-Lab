"""
Twisted Dirac operator cross-term computation on S^6=G2/SU(3).

Builds on g2su3_explicit_clifford.py (CALIBRATED against AHL2023 Theorem 5.1
-- all 6 e_i directions matched the known Killing spinor eigenvalue exactly).

Goal: determine whether v_b := y123 (x) 1  and  v_a := [SU(3)-invariant in
the 3bar (x) 3 piece of S+ (x) S-] have a nonzero Levi-Civita twisted-Dirac
matrix element, resolving rank(D+|_trivial) in {0,1}.

Step A (this file): determine explicitly, via the REAL su(3) action
(ad(nu_i)|_m, AHL2023 page 42, lifted to spin the same way the Levi-Civita
Nomizu map was lifted and calibrated), which of {y_1,y_2,y_3} and
{y_12,y_13,y_23} is the SU(3) "3" and which is the "3bar", and construct the
explicit SU(3)-invariant vector v_a.
"""

import sympy as sp
from g2su3_explicit_clifford import (
    DIM,
    SUBSETS,
    IDX,
    clifford_mult_bivector_direct,
    vec_from_subsets,
)

sqrt = sp.sqrt


def su3_lift(a, b, vec):
    return clifford_mult_bivector_direct(a, b, vec)


# AHL2023 page 42, Remark 5.2: ad(nu_i)|_m, i=1..8.
SU3_GENERATORS = {
    1: [(1, 1, 2), (-1, 3, 4)],
    2: [(1, 3, 5), (1, 4, 6)],
    3: [(-1, 3, 6), (1, 4, 5)],
    4: [(1, 1, 6), (-1, 2, 5)],
    5: [(-1, 1, 5), (-1, 2, 6)],
    6: [(-1, 1, 4), (1, 2, 3)],
    7: [(1, 1, 3), (1, 2, 4)],
    8: [(-1, 1, 2), (-1, 3, 4), (2, 5, 6)],  # coefficient 1/(2sqrt3), others 1/2
}


def su3_action(i, vec):
    terms = SU3_GENERATORS[i]
    coeff = sp.Rational(1, 2) if i != 8 else sp.Rational(1, 2) / sqrt(3)
    out = sp.zeros(DIM, 1)
    for sign, a, b in terms:
        out += sign * su3_lift(a, b, vec)
    return coeff * out


def su3_casimir_action_squared(vec):
    """Sum_i ad(nu_i)^2 acting on vec -- to check which irrep a vector sits in
    by comparing eigenvalues (scalar check, not a full irrep classification)."""
    out = sp.zeros(DIM, 1)
    for i in range(1, 9):
        out += su3_action(i, su3_action(i, vec))
    return out


def main():
    print("=" * 70)
    print("Step A: determine 3 vs 3bar assignment via explicit su(3) action")
    print("=" * 70)

    y1 = vec_from_subsets({(1,): 1})
    y2 = vec_from_subsets({(2,): 1})
    y3 = vec_from_subsets({(3,): 1})
    y12 = vec_from_subsets({(1, 2): 1})
    y13 = vec_from_subsets({(1, 3): 1})
    y23 = vec_from_subsets({(2, 3): 1})

    print("\n--- Check closure: does su(3) preserve span{y1,y2,y3}? ---")
    for i in range(1, 9):
        out = su3_action(i, y1)
        coeffs = {s: sp.simplify(out[IDX[s]]) for s in SUBSETS if sp.simplify(out[IDX[s]]) != 0}
        print(f"  nu_{i} . y1 = {coeffs}")

    print("\n--- Check closure: does su(3) preserve span{y12,y13,y23}? ---")
    for i in range(1, 9):
        out = su3_action(i, y12)
        coeffs = {s: sp.simplify(out[IDX[s]]) for s in SUBSETS if sp.simplify(out[IDX[s]]) != 0}
        print(f"  nu_{i} . y12 = {coeffs}")

    print("\n--- Cartan generator nu_8 eigenvalues (weight check) ---")
    for name, v in [("y1", y1), ("y2", y2), ("y3", y3), ("y12", y12), ("y13", y13), ("y23", y23)]:
        out = su3_action(8, v)
        # check if it's an eigenvector
        ratios = []
        for s in SUBSETS:
            if sp.simplify(v[IDX[s]]) != 0:
                ratios.append(sp.simplify(out[IDX[s]] / v[IDX[s]]))
        print(f"  nu_8 . {name}: eigenvalue-like ratio(s) = {ratios}")


if __name__ == "__main__":
    main()
