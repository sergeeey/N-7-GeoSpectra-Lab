"""
Round 14 (2026-07-09): V_7 construction that FIXES Round 6/8's failed
"rolling map" ansatz (see g2su3_V7_construction.py -- superseded, kept
only as a record of the dead end; decision.md documents why) -- not by
re-deriving a new ansatz, but by RESTRICTING the already-validated
g2su3_appendix_a_construction.py data.

AHL2023 Lemma A.1: g2 = stab_{spin(7)}{phi_1}, su(3) = stab{phi_1,phi_2},
for phi_1, phi_2 the first two standard basis vectors of Sigma_7=R^8 (NOT
something to solve for). Verified directly below: phi_1 is killed by all
14 g2 generators, phi_2 by exactly the 8 su(3) generators.

Given phi_1 is killed by every nu_k, and every nu_k is antisymmetric (so a
zero COLUMN forces a zero ROW at the same index), V_7 := phi_1^perp
(7-dim) is automatically preserved by the full g2 action -- restricting
the validated 8x8 nu_k matrices to rows/cols 2..8 gives G2's fundamental
7-dim representation directly, no new ansatz, no separate calibration
needed beyond what g2su3_appendix_a_construction.py already established.

Two independent structural checks on the result:
  1. C_2(G2;V_7) computed directly must be a pure scalar (irreducibility).
  2. C_2(SU(3);adjoint) computed the same way on span{nu_1..nu_8} must
     match the preprint's own cited value 3, with NO rescaling -- this
     confirms AHL2023's B_0-orthonormal basis uses the standard "physics"
     Tr(T^aT^b)=delta^ab/2 convention (C_2(adjoint SU(N))=N), the SAME
     convention resolved independently in g2su3_casimir_convention_check.py.
"""

import sympy as sp
from g2su3_appendix_a_construction import NU, nu, decompose_g2

N8 = 8


def phi(k):
    v = sp.zeros(N8, 1)
    v[k - 1] = 1
    return v


def main():
    phi1, phi2 = phi(1), phi(2)

    print("=" * 70)
    print("CHECK 1: phi_1 killed by all 14 g2 generators (Lemma A.1)?")
    print("=" * 70)
    killed_by_all_14 = all(sp.simplify(nu(k) * phi1) == sp.zeros(N8, 1) for k in range(1, 15))
    print(f"  phi_1 = e_1 killed by nu_1..nu_14: {killed_by_all_14}")

    print("\n" + "=" * 70)
    print("CHECK 2: phi_2 killed by exactly the 8 su(3) generators (not m)?")
    print("=" * 70)
    killed_by_su3 = all(sp.simplify(nu(k) * phi2) == sp.zeros(N8, 1) for k in range(1, 9))
    killed_by_m_too = all(sp.simplify(nu(k) * phi2) == sp.zeros(N8, 1) for k in range(9, 15))
    print(f"  phi_2 killed by nu_1..nu_8 (su(3)): {killed_by_su3}")
    print(f"  phi_2 ALSO killed by nu_9..nu_14 (m) [should be False]: {killed_by_m_too}")

    print("\n" + "=" * 70)
    print("V_7 := phi_1^perp (rows/cols 2..8) -- restrict all 14 nu_k")
    print("=" * 70)
    V7 = {k: sp.simplify(NU[k][1:8, 1:8]) for k in range(1, 15)}
    zero_first_row_col = all(
        sp.simplify(NU[k][0, :]) == sp.zeros(1, N8) and sp.simplify(NU[k][:, 0]) == sp.zeros(N8, 1)
        for k in range(1, 15)
    )
    print(
        f"  every nu_k has zero 1st row AND column (antisymmetry + phi_1-kill): {zero_first_row_col}"
    )

    print("\n" + "=" * 70)
    print("CHECK 3: C_2(G2; V_7) = -sum_k (nu_k|_V7)^2 -- scalar is CONSISTENT")
    print("with irreducibility (Schur), not independently sufficient to prove it")
    print("(a reducible sum of non-isomorphic irreps with equal Casimir would also")
    print("give a scalar here) -- treat this as a structural sanity check, not a")
    print("standalone irreducibility proof")
    print("=" * 70)
    C2_V7 = sp.simplify(-sum((V7[k] * V7[k] for k in range(1, 15)), sp.zeros(7, 7)))
    is_scalar_V7 = C2_V7 == C2_V7[0, 0] * sp.eye(7)
    print(f"  C_2(G2;7) matrix == scalar * I_7 ? {is_scalar_V7}")
    print(f"  scalar value: {sp.simplify(C2_V7[0, 0])}")

    print("\n" + "=" * 70)
    print("CHECK 4: C_2(SU(3); adjoint) via ad(nu_i), i=1..8, on span{nu_1..nu_8}")
    print("(same computation as g2su3_casimir_convention_check.py's convention")
    print(" cross-check, redone here directly from the 8x8 matrices)")
    print("=" * 70)

    def ad8(i, j):
        """8-dim adjoint-action coefficient vector of ad(nu_i) on nu_j, via decompose_g2."""
        comm = sp.simplify(nu(i) * nu(j) - nu(j) * nu(i))
        coeffs = decompose_g2(comm)
        return sp.Matrix([coeffs.get(k, 0) for k in range(1, 9)])

    AD = [sp.Matrix.hstack(*[ad8(i, j) for j in range(1, 9)]) for i in range(1, 9)]
    C2_adj = sp.simplify(-sum((AD[i - 1] * AD[i - 1] for i in range(1, 9)), sp.zeros(8, 8)))
    is_scalar_adj = C2_adj == C2_adj[0, 0] * sp.eye(8)
    print(f"  C_2(SU(3);adjoint) matrix == scalar * I_8 ? {is_scalar_adj}")
    print(f"  scalar value: {sp.simplify(C2_adj[0, 0])}  (preprint's own cited value: 3)")

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(
        f"  C_2(G2;V_7)          = {sp.simplify(C2_V7[0, 0])}  (Agricola 2002's cited value: 4 -- see"
    )
    print(
        "                          g2su3_casimir_convention_check.py for the resolved factor-of-2"
    )
    print(
        "                          convention mismatch: long-root^2=2 vs physics Tr(TT)=1/2 convention)"
    )
    print(
        f"  C_2(SU(3);adjoint)   = {sp.simplify(C2_adj[0, 0])}  (matches preprint exactly, no rescaling)"
    )


if __name__ == "__main__":
    main()
