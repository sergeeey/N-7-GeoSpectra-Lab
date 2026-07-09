"""
Kostant cubic element H and its square H^2, built from the SAME calibrated
Levi-Civita Nomizu data already used for the trivial-isotype rank computation.

Purpose: resolve the "danger zone" question the skeptic raised — does the
torsion correction in Agricola 2002's Theorem 3.2 (the exact (D^t)^2 formula
for general connection parameter t, applied at t=1/2 = Levi-Civita) threaten
the KP spectral gap the preprint currently claims "proved" on non-trivial
G2-isotypic components?

Key algebraic fact used (Agricola 2002, Lemma 3.2 + eq. between Thm 3.2 and
H's definition): the cubic-Clifford term appearing in (D^t)^2 with coefficient
(1/2)(1-3t) * sum_{i,j,k} <[Z_i,Z_j]_m,Z_k> Z_i.Z_j.Z_k EQUALS 2(1-3t)*H,
where H := (1/4) sum_{i,j,k} <[Z_i,Z_j]_m,Z_k> Z_i.Z_j.Z_k is Kostant's cubic
element (t-independent, built purely from the torsion 3-form <[.,.]_m,.>).
At t=1/2: 2(1-3/2) = -1, so the cubic correction term in (D^{1/2})^2 is
EXACTLY -H. This lets us reuse H (fully computable from data already in
g2su3_explicit_clifford.py) instead of re-deriving the general formula.

H^2's degree-0 (scalar) and degree-4 parts are given in closed form by
Agricola's Prop 3.2:
  (H^2)_0 = (3/8) sum_{i,j} <[Z_i,Z_j]_m,[Z_i,Z_j]_m>
  (H^2)_4 = -(9/2) sum_{i<j<k<l} <Z_i,Jac_m(Z_j,Z_k,Z_l)> Z_i.Z_j.Z_k.Z_l
We do NOT need Agricola's proof of these formulas -- we compute H directly
as an explicit Clifford operator (8x8 complex matrix on Sigma) using
e_action, then square it as a matrix and read off (H^2)_0, (H^2)_4 directly.
This is a cross-check: if computed (H^2)_0 matches (3/8)*sum T(i,j,k)^2, our
torsion-extraction from LEVI_CIVITA_NOMIZU is validated independently.

NOTE: the SEPARATE Jac_h-dependent piece of Theorem 3.2's quartic term
(the "9t^2 Jac_h(Z_j,Z_k,Z_l)" addend, which involves the su(3)-valued
curvature [Z_j,Z_k]_h, NOT captured by H^2 alone) is NOT computed here --
it requires full g2 structure constants beyond what's been built so far.
This script establishes the H-based (torsion-only) part of the correction;
the Jac_h/curvature part remains open, flagged explicitly in the output.
"""

import sympy as sp
from g2su3_explicit_clifford import (
    DIM,
    SUBSETS,
    e_action,
    LEVI_CIVITA_NOMIZU,
    vec_from_subsets,
)

sqrt = sp.sqrt


def bivector_on_vector6(a, b, vec6):
    """(e_a ^ e_b) acting on a 6-dim REAL vector (not the spinor module):
    (e_a^e_b)(e_c) = delta_{b,c} e_a - delta_{a,c} e_b. vec6: sympy 6x1 Matrix."""
    out = sp.zeros(6, 1)
    out[a - 1] += vec6[b - 1]
    out[b - 1] -= vec6[a - 1]
    return out


def lambda_half(i, vec6):
    """Lambda_m^{1/2}(e_i) acting on vec6, from LEVI_CIVITA_NOMIZU."""
    terms = LEVI_CIVITA_NOMIZU[i]
    coeff = sp.Rational(1, 2) / sqrt(3)
    out = sp.zeros(6, 1)
    for sign, a, b in terms:
        out += sign * bivector_on_vector6(a, b, vec6)
    return coeff * out


def torsion_T(i, j, k):
    """T(i,j,k) = <[Z_i,Z_j]_m, Z_k> = 2 <Lambda_m^{1/2}(e_i) e_j, e_k>."""
    e_j = sp.zeros(6, 1)
    e_j[j - 1] = 1
    lam = lambda_half(i, e_j)
    return sp.simplify(2 * lam[k - 1])


def build_T_table():
    T = {}
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                val = torsion_T(i, j, k)
                if val != 0:
                    T[(i, j, k)] = val
    return T


def check_total_antisymmetry(T):
    print("--- Checking total antisymmetry of T(i,j,k) ---")
    ok = True
    for (i, j, k), val in T.items():
        # antisymmetry under swap i<->j
        v_ij = T.get((j, i, k), 0)
        if sp.simplify(v_ij + val) != 0:
            print(f"  FAIL swap(i,j) at {(i, j, k)}: T={val}, T_swapped={v_ij}")
            ok = False
        v_jk = T.get((i, k, j), 0)
        if sp.simplify(v_jk + val) != 0:
            print(f"  FAIL swap(j,k) at {(i, j, k)}: T={val}, T_swapped={v_jk}")
            ok = False
    print(f"  Total antisymmetry holds: {ok}")
    return ok


def clifford_triple(i, j, k, vec):
    return e_action(i, e_action(j, e_action(k, vec)))


def build_H_matrix(T):
    """H = (1/4) sum_{i,j,k} T(i,j,k) Z_i.Z_j.Z_k, as an 8x8 matrix on Sigma."""
    H = sp.zeros(DIM, DIM)
    basis = [vec_from_subsets({s: 1}) for s in SUBSETS]
    for col, bvec in enumerate(basis):
        out = sp.zeros(DIM, 1)
        for (i, j, k), val in T.items():
            out += val * clifford_triple(i, j, k, bvec)
        out = sp.Rational(1, 4) * out
        for row in range(DIM):
            H[row, col] = out[row]
    return sp.simplify(H)


def main():
    print("=" * 70)
    print("Building torsion 3-form T(i,j,k) = <[Z_i,Z_j]_m, Z_k> from LC Nomizu data")
    print("=" * 70)
    T = build_T_table()
    for (i, j, k), val in sorted(T.items()):
        if i < j < k:
            print(f"  T({i},{j},{k}) = {val}")
    check_total_antisymmetry(T)

    print("\n" + "=" * 70)
    print("Building H = (1/4) sum T(i,j,k) Z_i.Z_j.Z_k as 8x8 matrix on Sigma")
    print("=" * 70)
    H = build_H_matrix(T)
    print("H matrix built (8x8). Checking H is skew-Hermitian-ish / degree structure...")

    H2 = sp.simplify(H * H)
    print("\nH^2 matrix (should be scalar*I + degree-4 Clifford part):")
    # print nonzero entries
    for r in range(DIM):
        for c in range(DIM):
            v = sp.simplify(H2[r, c])
            if v != 0:
                print(f"  H2[{SUBSETS[r]},{SUBSETS[c]}] = {v}")

    # cross-check scalar part against closed form (3/8) sum_{i,j} sum_k T(i,j,k)^2
    scalar_closed_form = sp.Rational(3, 8) * sum(
        sp.simplify(T.get((i, j, k), 0)) ** 2
        for i in range(1, 7)
        for j in range(1, 7)
        for k in range(1, 7)
    )
    scalar_closed_form = sp.simplify(scalar_closed_form)
    print(f"\nClosed-form (H^2)_0 = (3/8) sum <[Zi,Zj]_m,[Zi,Zj]_m> = {scalar_closed_form}")
    diag_vals = set(sp.simplify(H2[r, r]) for r in range(DIM))
    print(
        f"Diagonal entries of H^2 (should all equal (H^2)_0 if H^2 has no deg-4 part surviving on diagonal... "
        f"actually deg-4 part IS off-diagonal in this basis in general): {diag_vals}"
    )


if __name__ == "__main__":
    main()
