"""
Explicit Clifford-module / Levi-Civita computation on S^6 = G2/SU(3).

Data source: Agricola-Hofmann-Lawn 2023 ("Invariant Spinors on Homogeneous
Spheres"), Section 5.1 and Section 2.1 (Lagrangian-subspace spin
representation).

STEP 4 OF THE VERIFICATION PLAN (calibration, done FIRST):
Reproduce Theorem 5.1's known result before trusting anything harder:
  psi_+- = 1 +- y1^y2^y3 are Riemannian Killing spinors,
  nabla^g_X psi_+- = +-(1/(2 sqrt3)) X . psi_+-

If this does not reproduce exactly, there is a convention/sign error in the
setup below that must be fixed before attempting the twisted (S+ tensor S-)
computation this experiment actually needs.
"""

import itertools
import sympy as sp

IMAG = sp.I
sqrt = sp.sqrt

# ---------------------------------------------------------------------------
# Sigma = Lambda^bullet(C y1 + C y2 + C y3), 8-dimensional.
# Basis element indexed by a sorted tuple subset of {1,2,3}: () -> 1,
# (1,) -> y1, (1,2) -> y1^y2, (1,2,3) -> y1^y2^y3, etc.
# ---------------------------------------------------------------------------

SUBSETS = [tuple(sorted(c)) for k in range(4) for c in itertools.combinations([1, 2, 3], k)]
DIM = len(SUBSETS)  # 8
IDX = {s: i for i, s in enumerate(SUBSETS)}


def wedge_sign_insert(subset, j):
    """Sign to insert j into sorted subset (j not in subset), and resulting sorted subset."""
    pos = sum(1 for x in subset if x < j)
    sign = (-1) ** pos
    new_subset = tuple(sorted(subset + (j,)))
    return sign, new_subset


def contract_sign_remove(subset, j):
    """Sign to remove j from sorted subset (j in subset), and resulting sorted subset."""
    pos = subset.index(j)
    sign = (-1) ** pos
    new_subset = tuple(x for x in subset if x != j)
    return sign, new_subset


def y_wedge(j, vec):
    """y_j ^ (vec), vec a DIM-vector (sympy Matrix column)."""
    out = sp.zeros(DIM, 1)
    for s in SUBSETS:
        c = vec[IDX[s]]
        if c == 0:
            continue
        if j in s:
            continue
        sign, new_s = wedge_sign_insert(s, j)
        out[IDX[new_s]] += sign * c
    return out


def x_contract(j, vec):
    """x_j contraction (interior product) on vec."""
    out = sp.zeros(DIM, 1)
    for s in SUBSETS:
        c = vec[IDX[s]]
        if c == 0:
            continue
        if j not in s:
            continue
        sign, new_s = contract_sign_remove(s, j)
        out[IDX[new_s]] += sign * c
    return out


def e_action(i, vec):
    """Real orthonormal basis e_1..e_6 acting on Sigma, per AHL2023 eq. (5).
    e_{2j-1} . eta = i (x_j _| eta + y_j ^ eta)
    e_{2j}   . eta = (y_j ^ eta - x_j _| eta)
    i = 1..6 -> j = 1,2,3 ; odd/even.
    """
    j = (i + 1) // 2  # 1->1, 2->1, 3->2, 4->2, 5->3, 6->3
    if i % 2 == 1:  # e_{2j-1}
        return IMAG * (x_contract(j, vec) + y_wedge(j, vec))
    else:  # e_{2j}
        return y_wedge(j, vec) - x_contract(j, vec)


def clifford_mult_bivector(a, b, vec):
    """Action of (1/2) e_a . e_b on vec (the standard so(6)->spin(6) lift of
    the bivector generator e_{a,b}), a != b, 1<=a,b<=6."""
    return sp.Rational(1, 2) * (e_action(a, e_action(b, vec)) - e_action(b, e_action(a, vec))) / 2
    # NOTE: e_a . e_b already anticommutes appropriately in Clifford algebra;
    # (1/2)(e_a e_b) directly IS the lift (no need for commutator/2 again).
    # Kept both forms available for calibration -- see main() sanity checks.


def clifford_mult_bivector_direct(a, b, vec):
    """Direct (1/2) e_a . e_b . vec (apply e_b first, then e_a), the standard convention."""
    return sp.Rational(1, 2) * e_action(a, e_action(b, vec))


# ---------------------------------------------------------------------------
# AHL2023 page 42: Levi-Civita Nomizu map Lambda^g(e_i), i=1..6, as
# combinations of bivectors e_{a,b} with coefficient 1/(2 sqrt3).
# Lambda^g(e_1) = (1/2sqrt3)(e_36+e_45)
# Lambda^g(e_2) = (1/2sqrt3)(e_35-e_46)
# Lambda^g(e_3) = (1/2sqrt3)(-e_16-e_25)
# Lambda^g(e_4) = (1/2sqrt3)(-e_15+e_26)
# Lambda^g(e_5) = (1/2sqrt3)(e_14+e_23)
# Lambda^g(e_6) = (1/2sqrt3)(e_13-e_24)
# ---------------------------------------------------------------------------

LEVI_CIVITA_NOMIZU = {
    1: [(1, 3, 6), (1, 4, 5)],
    2: [(1, 3, 5), (-1, 4, 6)],
    3: [(-1, 1, 6), (-1, 2, 5)],
    4: [(-1, 1, 5), (1, 2, 6)],
    5: [(1, 1, 4), (1, 2, 3)],
    6: [(1, 1, 3), (-1, 2, 4)],
}


def nabla_g_action(i, vec, bivector_fn):
    """nabla^g_{e_i} acting on an invariant spinor `vec`, via spin-lift of
    Lambda^g(e_i) using the given bivector convention function."""
    terms = LEVI_CIVITA_NOMIZU[i]
    coeff = sp.Rational(1, 2) / sqrt(3)
    out = sp.zeros(DIM, 1)
    for sign, a, b in terms:
        out += sign * bivector_fn(a, b, vec)
    return coeff * out


def vec_from_subsets(coeffs):
    """coeffs: dict subset-tuple -> coefficient."""
    v = sp.zeros(DIM, 1)
    for s, c in coeffs.items():
        v[IDX[s]] = c
    return v


def print_vec(vec, label):
    parts = []
    for s in SUBSETS:
        c = sp.simplify(vec[IDX[s]])
        if c != 0:
            name = "1" if s == () else "y" + "".join(str(x) for x in s)
            parts.append(f"({c}){name}")
    print(f"{label} = " + " + ".join(parts) if parts else f"{label} = 0")


def main():
    print("=" * 70)
    print("CALIBRATION: reproduce AHL2023 Theorem 5.1 Killing spinor eigenvalue")
    print("=" * 70)

    psi_plus = vec_from_subsets({(): 1, (1, 2, 3): 1})  # 1 + y1^y2^y3

    expected_eigenvalue = sp.Rational(1, 2) / sqrt(3)

    print("\nExpected: nabla^g_{e_i} psi_+ = (1/(2 sqrt3)) e_i . psi_+  for all i=1..6")
    print(f"Expected eigenvalue: {sp.simplify(expected_eigenvalue)}\n")

    for bivector_name, bivector_fn in [
        ("direct (1/2)e_a.e_b", clifford_mult_bivector_direct),
    ]:
        print(f"--- Using bivector convention: {bivector_name} ---")
        all_match = True
        for i in range(1, 7):
            lhs = nabla_g_action(i, psi_plus, bivector_fn)
            rhs = expected_eigenvalue * e_action(i, psi_plus)
            diff = sp.simplify(lhs - rhs)
            match = all(sp.simplify(x) == 0 for x in diff)
            all_match = all_match and match
            print(f"  e_{i}: nabla match = {match}")
            if not match:
                print_vec(sp.simplify(lhs), f"    lhs (nabla_e{i} psi_+)")
                print_vec(sp.simplify(rhs), f"    rhs (lambda * e{i}.psi_+)")
        print(f"  ALL MATCH: {all_match}\n")


if __name__ == "__main__":
    main()
