"""Independent THIRD verification method for the L_x = -(T'_x)^T finding:
instead of solving linear systems (verify_tom_calc.py) or column-decomposition
via exp(i*phi) coefficient extraction (build_full_matrices.py), use genuine
bra-ket inner-product projection: <psi_m | L_i | psi_m'> := integral over the
sphere of conj(psi_m) * (L_i psi_m') * sin(theta) dtheta dphi, normalized by
<psi_m|psi_m>. This is the standard quantum-mechanics way to extract matrix
elements and is structurally independent of both prior methods (integration,
not equation-solving or coefficient-matching).
"""
import sympy as sp

theta, phi = sp.symbols("theta phi", real=True)
I = sp.I  # noqa: E741


def Lx(f):
    return I * sp.sin(phi) * sp.diff(f, theta) + I * sp.cot(theta) * sp.cos(phi) * sp.diff(f, phi)


def Ly(f):
    return -I * sp.cos(phi) * sp.diff(f, theta) + I * sp.cot(theta) * sp.sin(phi) * sp.diff(f, phi)


def Lz(f):
    return -I * sp.diff(f, phi)


basis = {
    "p1": sp.sin(theta) * sp.exp(I * phi),
    "p0": sp.cos(theta),
    "pm1": sp.sin(theta) * sp.exp(-I * phi),
}
order = ["p1", "p0", "pm1"]


def inner_product(f, g):
    """<f|g> := integral f_conj * g * sin(theta) dtheta [0,pi] dphi [0,2pi]."""
    integrand = sp.conjugate(f) * g * sp.sin(theta)
    inner_theta = sp.integrate(integrand, (theta, 0, sp.pi))
    return sp.simplify(sp.integrate(inner_theta, (phi, 0, 2 * sp.pi)))


def matrix_element(bra_name, op, ket_name):
    bra = basis[bra_name]
    ket = basis[ket_name]
    norm_bra = inner_product(bra, bra)
    raw = inner_product(bra, op(ket))
    return sp.simplify(raw / norm_bra)


def build_matrix(op):
    M = sp.zeros(3, 3)
    for col, ket_name in enumerate(order):
        for row, bra_name in enumerate(order):
            M[row, col] = matrix_element(bra_name, op, ket_name)
    return M


Lx_bra = build_matrix(Lx)
Ly_bra = build_matrix(Ly)
Lz_bra = build_matrix(Lz)

print("=== Matrices via bra-ket inner-product projection (3rd independent method) ===")
print("Lx:")
sp.pprint(Lx_bra)
print("Ly:")
sp.pprint(Ly_bra)
print("Lz:")
sp.pprint(Lz_bra)

Tpx = sp.Matrix([[0, 1, 0], [sp.Rational(1, 2), 0, sp.Rational(-1, 2)], [0, -1, 0]])
Tpy = sp.Matrix([[0, -I, 0], [sp.Rational(1, 2) * I, 0, sp.Rational(1, 2) * I], [0, -I, 0]])
Tpz = sp.diag(1, 0, -1)

print()
print("Lx_bra vs -(T'x)^T:", sp.simplify(Lx_bra - (-Tpx.T)))
print("Ly_bra vs +(T'y)^T:", sp.simplify(Ly_bra - Tpy.T))
print("Lz_bra vs T'z:", sp.simplify(Lz_bra - Tpz))
