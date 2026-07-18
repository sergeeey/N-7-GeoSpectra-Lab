"""E27 (round101, A6): naive component-substitution check of whether the
spin connection Omega_i(t) (E9/round73) transforms consistently under the
iota-induced frame exchange (round80/E14 Section C's b_i^j(x)
coefficients), the way the TORSION TENSOR was shown to at the affine
level.

Reuses, unchanged:
 - Omega_i(t) formula: experiments/20260717-round73-e9-explicit-parallel-
   spinor/e9_explicit_parallel_spinor.py:171-178
 - b_i^j(x) coefficients: experiments/20260717-round80-z2-left-right-
   symmetry-search/e14_z2_left_right_symmetry.py:165-177
"""

import sympy as sp

I2 = sp.eye(2)
t, c = sp.symbols("t c")
x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)
XS = [x0, x1, x2, x3]
NORM2 = x0**2 + x1**2 + x2**2 + x3**2


def pauli_matrices():
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    return [sx, sy, sz]


def clifford_generators():
    return [sp.I * s for s in pauli_matrices()]


def eps(i, j, k):
    p = [i, j, k]
    if len(set(p)) < 3:
        return 0
    sign = 1
    perm = p[:]
    for xx in range(3):
        for yy in range(3 - 1 - xx):
            if perm[yy] > perm[yy + 1]:
                perm[yy], perm[yy + 1] = perm[yy + 1], perm[yy]
                sign = -sign
    return sign


def christoffel(i, j, k):
    """Gamma^k_{ij}(t) = t*c*eps(i,j,k), 0-indexed."""
    return t * c * eps(i + 1, j + 1, k + 1)


def spin_connection_Omega(i, Z):
    """Reused unchanged from E9 (round73)."""
    total = sp.zeros(2, 2)
    for j in range(3):
        for k in range(3):
            coeff = christoffel(i, j, k)
            if coeff != 0:
                total += coeff * (Z[j] * Z[k])
    return sp.simplify(total / 4)


def group_element(Z):
    return x0 * I2 + x1 * Z[0] + x2 * Z[1] + x3 * Z[2]


def group_conjugate(Z):
    return x0 * I2 - x1 * Z[0] - x2 * Z[1] - x3 * Z[2]


def basis_matrices(Z):
    return [I2, Z[0], Z[1], Z[2]]


def basis_inverse(Z):
    basis = basis_matrices(Z)
    cols = [[M[0, 0], M[0, 1], M[1, 0], M[1, 1]] for M in basis]
    Bmat = sp.Matrix(cols).T
    return sp.simplify(Bmat.inv())


def coords_in_basis(M, Binv):
    v = sp.Matrix([M[0, 0], M[0, 1], M[1, 0], M[1, 1]])
    coeffs = Binv * v
    return [sp.simplify(coeffs[i]) for i in range(4)]


def express_fk_in_Z_basis(Z, Binv, k):
    """Reused unchanged from round80 (E14) e14_z2_left_right_symmetry.py:165-177."""
    g = group_element(Z)
    gbar = group_conjugate(Z)
    conj_scaled = sp.expand(gbar * Z[k] * g)
    coeffs_scaled = coords_in_basis(conj_scaled, Binv)
    b = [sp.together(coeffs_scaled[j + 1] / NORM2) for j in range(3)]
    return b


print("=" * 92)
print("PART 0 -- Reused inputs (E9/round73 Omega_i(t), round80/E14 b_i^j(x))")
print("=" * 92)
Z = clifford_generators()
Binv = basis_inverse(Z)
Omega = [spin_connection_Omega(i, Z) for i in range(3)]
for i in range(3):
    print(f"  Omega_{i + 1}(t) =")
    sp.pprint(Omega[i])
print()

print("=" * 92)
print("PART 1 -- b_i^j(x) coefficients (Z_i^R = sum_j b_i^j(x) Z_j^L), reused from round80")
print("=" * 92)
b = [express_fk_in_Z_basis(Z, Binv, k) for k in range(3)]
for i in range(3):
    print(f"  b_{i + 1}^j(x) for j=1,2,3: {b[i]}")
print()

print("=" * 92)
print("PART 2 -- Naive R-frame spin connection: Omega_i^R(t)(x) := sum_j b_i^j(x)*Omega_j(t)")
print("=" * 92)
OmegaR = []
for i in range(3):
    tot = sp.zeros(2, 2)
    for j in range(3):
        tot += b[i][j] * Omega[j]
    OmegaR.append(sp.simplify(tot))

x_independence_results = []
all_x_independent = True
for i in range(3):
    entries_have_x = any(
        (
            OmegaR[i][r, col].has(x0)
            or OmegaR[i][r, col].has(x1)
            or OmegaR[i][r, col].has(x2)
            or OmegaR[i][r, col].has(x3)
        )
        for r in range(2)
        for col in range(2)
    )
    x_independence_results.append({"i": i + 1, "is_x_independent": not entries_have_x})
    all_x_independent = all_x_independent and (not entries_have_x)
    print(f"  Omega_{i + 1}^R(t)(x) x-independent? {not entries_have_x}")
    print(f"    Omega_{i + 1}^R(t)(x) =")
    sp.pprint(OmegaR[i])
print()
print(f"  ALL Omega_i^R(t)(x) x-independent? {all_x_independent}")
print()

print("=" * 92)
print("PART 3 -- IF x-independent: compare against +-Omega_i(1-t)")
print("=" * 92)
if all_x_independent:
    comparison = []
    for i in range(3):
        Om_1mt = sp.simplify(Omega[i].subs(t, 1 - t))
        diff_plus = sp.simplify(OmegaR[i] - Om_1mt)
        diff_minus = sp.simplify(OmegaR[i] + Om_1mt)
        matches_plus = diff_plus == sp.zeros(2, 2)
        matches_minus = diff_minus == sp.zeros(2, 2)
        comparison.append(
            {
                "i": i + 1,
                "matches_plus_Omega_1mt": matches_plus,
                "matches_minus_Omega_1mt": matches_minus,
            }
        )
        print(
            f"  i={i + 1}: Omega_i^R(t) == +Omega_i(1-t)? {matches_plus}; "
            f"== -Omega_i(1-t)? {matches_minus}"
        )
    spin_level_confirmed = all(
        c["matches_plus_Omega_1mt"] or c["matches_minus_Omega_1mt"] for c in comparison
    )
else:
    comparison = None
    spin_level_confirmed = False
    print("  SKIPPED -- Omega_i^R(t)(x) is x-DEPENDENT, so no constant-matrix comparison")
    print("  against Omega_i(1-t) is meaningful. This is the expected mathematical")
    print("  reason: a connection 1-form is NOT a tensor -- under a non-constant frame")
    print("  change (b_i^j(x) depends on x, unlike the affine/torsion-tensor case where")
    print("  T^t is a genuine tensor and the b(x)-dependence canceled via the rotation-")
    print("  coefficient identity, round80 Section C step 3), the connection acquires an")
    print("  additional INHOMOGENEOUS (Maurer-Cartan-type) term this naive component")
    print("  substitution omits. The naive check correctly detects this.")
print()

verdict = {
    "all_x_independent": all_x_independent,
    "spin_level_naive_check_confirmed": bool(spin_level_confirmed),
}
label = (
    "SPIN_LEVEL_EQUIVARIANCE_CONFIRMED_NAIVE"
    if spin_level_confirmed
    else "NAIVE_APPROACH_BLOCKED__X_DEPENDENT__INHOMOGENEOUS_TERM_NEEDED"
)
print("=" * 92)
print("VERDICT")
print("=" * 92)
for k, v in verdict.items():
    print(f"  {k}: {v}")
print(f"  label = '{label}'")
