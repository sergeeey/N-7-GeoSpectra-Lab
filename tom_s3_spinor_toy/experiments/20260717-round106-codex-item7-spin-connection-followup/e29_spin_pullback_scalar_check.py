"""E29 (round106): Codex item-7 follow-up. Three checks:
(1) b(x) is exactly the matrix of Ad(g(x)^-1) in the {Z_i} basis.
(2) The "naive" Omega_i^R(t)(x) IS the correct value of omega^t(Z_i^R)
    by linearity of 1-forms -- not an incomplete shortcut.
(3) H = (3c/2)*omega is a scalar multiple of I2 (E2's own fact,
    re-verified here), so D^t on constant spinors is pure scalar
    multiplication -- checking what this implies for spin-lift
    conjugation relating the t and 1-t eigenvalues.
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
    return t * c * eps(i + 1, j + 1, k + 1)


def spin_connection_Omega(i, Z):
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
    g = group_element(Z)
    gbar = group_conjugate(Z)
    conj_scaled = sp.expand(gbar * Z[k] * g)
    coeffs_scaled = coords_in_basis(conj_scaled, Binv)
    b = [sp.together(coeffs_scaled[j + 1] / NORM2) for j in range(3)]
    return b


Z = clifford_generators()
Binv = basis_inverse(Z)
g = group_element(Z)
gbar = group_conjugate(Z)

print("=" * 92)
print("PART 1 -- Is b(x) exactly the matrix of Ad(g(x)^-1) in the {Z_i} basis?")
print("=" * 92)
b = [express_fk_in_Z_basis(Z, Binv, k) for k in range(3)]
# Check: sum_j b_i^j(x) * Z_j  ==  gbar(x) * Z_i * g(x) / NORM2   (= g^-1 Z_i g)
all_match = True
for i in range(3):
    lhs = sp.zeros(2, 2)
    for j in range(3):
        lhs += b[i][j] * Z[j]
    rhs = sp.expand(gbar * Z[i] * g) / NORM2
    diff = sp.simplify(sp.expand(lhs - rhs))
    matches = diff == sp.zeros(2, 2)
    all_match = all_match and matches
    print(f"  i={i + 1}: sum_j b_i^j*Z_j == g^-1 Z_i g (=Ad(g^-1)(Z_i))? {matches}")
print(f"  ALL confirmed: {all_match}  -- b(x) IS the Ad(g(x)^-1) matrix, tool-verified")
print()

print("=" * 92)
print("PART 2 -- Linearity check: is Omega_i^R(t)(x):=sum_j b_i^j(x)*Omega_j(t)")
print("EXACTLY omega^t(Z_i^R), by linearity of the 1-form omega^t?")
print("=" * 92)
Omega = [spin_connection_Omega(i, Z) for i in range(3)]
OmegaR = []
for i in range(3):
    tot = sp.zeros(2, 2)
    for j in range(3):
        tot += b[i][j] * Omega[j]
    OmegaR.append(sp.simplify(tot))
print("  By construction (Z_i^R = sum_j b_i^j(x) Z_j^L, round80) and linearity of")
print("  omega^t in its vector argument: omega^t(Z_i^R) = sum_j b_i^j(x)*omega^t(Z_j^L)")
print("  = sum_j b_i^j(x)*Omega_j(t) = Omega_i^R(t)(x), EXACTLY -- this is an algebraic")
print("  identity (linearity of 1-forms), not something requiring separate verification")
print("  beyond confirming Omega_j(t):=omega^t(Z_j^L) itself (E9's own definition).")
print("  CONCLUSION: round101's 'naive' computation is CORRECT as an evaluation of")
print("  omega^t(Z_i^R) -- it is NOT missing a term AT THIS STEP. The genuine gap is")
print("  a DIFFERENT step: pulling back a CONNECTION (not just evaluating a 1-form at")
print("  a different vector) additionally requires how iota acts on the SPINOR FIBER")
print("  itself (which constant spinors count as 'parallel' in which frame) -- a")
print("  question about iota's spin lift, not about omega^t's own linearity.")
print()

print("=" * 92)
print("PART 3 -- Is H=(3c/2)*omega a scalar multiple of I2? (E2's own fact, re-verified)")
print("=" * 92)
omega = sp.simplify(Z[0] * Z[1] * Z[2])
H = sp.simplify(sp.Rational(3, 2) * c * omega)
is_scalar = sp.simplify(H - H[0, 0] * I2) == sp.zeros(2, 2)
print(f"  omega = Z1*Z2*Z3 = {omega.tolist()}")
print(f"  H = (3c/2)*omega = {H.tolist()}")
print(f"  H is a scalar multiple of I2? {is_scalar}   (H = {H[0, 0]} * I2)")
print()
print("  CONSEQUENCE: for CONSTANT spinors (E9's ansatz, Z_i(psi)=0), D^t(psi) =")
print("  t*H*psi = t*(3c/2)*psi -- PURE SCALAR multiplication. Any spin-lift S(x)")
print("  acting by conjugation (S^-1 * (scalar) * S = scalar, for ANY invertible S)")
print("  CANNOT turn the scalar t*(3c/2) into the scalar (1-t)*(3c/2) unless t=1-t")
print("  (t=1/2) -- conjugation is powerless to relate two DIFFERENT scalar values.")
print("  This means: at the level of the constant-spinor eigenvalue specifically (the")
print("  object E9's own kernel computation actually uses), NO spin-lift conjugation")
print("  of ANY kind can supply the desired t<->1-t equivalence -- a stronger, cleaner")
print("  statement than round101's x-dependence finding, though about a DIFFERENT,")
print("  simpler object (the scalar eigenvalue, not the full connection 1-form).")
print()

verdict = {
    "b_is_Ad_ginv_matrix_confirmed": bool(all_match),
    "naive_OmegaR_is_correct_omega_t_at_ZiR_by_linearity": True,
    "H_is_scalar_multiple_of_I2": bool(is_scalar),
    "conjugation_cannot_relate_t_and_1mt_scalar_eigenvalues_except_at_t_half": True,
}
print("=" * 92)
print("VERDICT")
print("=" * 92)
for k, v in verdict.items():
    print(f"  {k}: {v}")
label = "PARTIAL__LINEARITY_AND_SCALAR_POINTS_ESTABLISHED__FULL_SPIN_LIFT_OF_IOTA_STILL_OPEN"
print(f"  label = '{label}'")
