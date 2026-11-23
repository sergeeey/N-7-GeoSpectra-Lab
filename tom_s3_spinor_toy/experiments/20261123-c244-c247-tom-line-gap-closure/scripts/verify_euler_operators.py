"""Is the extra term the Euler-angle d/d(psi) term of the space-fixed angular momentum operators?

The generators are derived from the group action on SU(2) (no textbook formula is assumed), then compared
with the ladder operators of the letter. All checks are symbolic or at random points.
"""

import random

import sympy as sp

th, ph, ps = sp.symbols("theta phi psi", real=True)
I = sp.I
random.seed(5)
pts = [
    (random.uniform(0.3, 2.8), random.uniform(0.1, 6.0), random.uniform(0.1, 6.0)) for _ in range(6)
]
ok_all = True


def ev(expr, p):
    return complex(sp.N(expr.subs({th: p[0], ph: p[1], ps: p[2]}), 20))


def report(name, good):
    global ok_all
    ok_all &= bool(good)
    print("PASS" if good else "FAIL", name)


def allpts(expr, tol=1e-10):
    return all(abs(ev(expr, p)) < tol for p in pts)


sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])


def rot(axis, angle):
    return sp.cos(angle / 2) * sp.eye(2) - I * sp.sin(angle / 2) * axis


R = rot(sz, ph) * rot(sy, th)
D = R * rot(sz, ps)  # Euler-angle SU(2) element
q = [ph, th, ps]

# 1. derive the vector field of left multiplication by exp(-i eps sigma_a/2) on (phi, theta, psi)
fields = {}
for name, sig in (("x", sx), ("y", sy), ("z", sz)):
    a = sp.symbols("a_ph a_th a_ps")
    lhs = -I * sig / 2 * D
    eqs = [
        sum(a[i] * sp.diff(D[r, c], q[i]) for i in range(3)) - lhs[r, c]
        for r in range(2)
        for c in range(2)
    ]
    sol = sp.solve(eqs, a, dict=True)
    assert sol, f"no solution for {name}"
    fields[name] = tuple(sp.simplify(sol[0][u]) for u in a)


def Lop(name, f):
    a_ph, a_th, a_ps = fields[name]
    return -I * (a_ph * sp.diff(f, ph) + a_th * sp.diff(f, th) + a_ps * sp.diff(f, ps))


def Jp(f):
    return Lop("x", f) + I * Lop("y", f)


def Jm(f):
    return Lop("x", f) - I * Lop("y", f)


test = sp.sin(th) ** 2 * sp.exp(I * (2 * ph + ps)) + sp.cos(th / 2) * sp.exp(-I * ps / 2)

report("L_z = -i d/d phi", allpts(Lop("z", test) + I * sp.diff(test, ph)))
report(
    "[L_x, L_y] = i L_z",
    allpts(Lop("x", Lop("y", test)) - Lop("y", Lop("x", test)) - I * Lop("z", test)),
)
report("[J+, J-] = 2 L_z", allpts(Jp(Jm(test)) - Jm(Jp(test)) - 2 * Lop("z", test)))

# 2. the operators in Euler angles: same d/d theta and d/d phi parts as McMurry, plus a d/d psi term
expect_p = sp.exp(I * ph) * (
    sp.diff(test, th) + I * sp.cot(th) * sp.diff(test, ph) - (I / sp.sin(th)) * sp.diff(test, ps)
)
expect_m = sp.exp(-I * ph) * (
    -sp.diff(test, th) + I * sp.cot(th) * sp.diff(test, ph) - (I / sp.sin(th)) * sp.diff(test, ps)
)
report("J+ = e^{i phi}(d_th + i cot th d_ph - (i/sin th) d_psi)", allpts(Jp(test) - expect_p))
report(
    "J- = e^{-i phi}(-d_th + i cot th d_ph - (i/sin th) d_psi)  (same sign of the d_psi term)",
    allpts(Jm(test) - expect_m),
)

# 3. on functions with definite weight k under psi: f = e^{i k psi} Y(theta, phi), the extra term is k/sin(theta)
k = sp.Rational(-1, 2)
Yt3 = sp.sin(th) ** 3 * sp.exp(2 * I * ph) + sp.cos(th / 2) * sp.exp(-I * ph)  # concrete amplitude
f = sp.exp(I * k * ps) * Yt3
lhs = Jp(f) * sp.exp(-I * k * ps)
rhs = sp.exp(I * ph) * (sp.diff(Yt3, th) + I * sp.cot(th) * sp.diff(Yt3, ph) + k / sp.sin(th) * Yt3)
report(
    "weight k: J+ (e^{ik psi} Y) = e^{ik psi} e^{i phi}(d_th + i cot th d_ph + k/sin th) Y  (checked at random points)",
    allpts(lhs - rhs),
)
# the letter's operator, written literally (not derived from rhs): extra term c = -e^{i phi}/(2 sin theta)
letter = sp.exp(I * ph) * (
    sp.diff(Yt3, th) + I * sp.cot(th) * sp.diff(Yt3, ph) - Yt3 / (2 * sp.sin(th))
)
report(
    "k = -1/2 reproduces the letter's operator literally, c = -e^{i phi}/(2 sin theta)",
    allpts(lhs - letter),
)
# negative control: the wrong weight (k = +1/2) must NOT reproduce it
f_wrong = sp.exp(I * sp.Rational(1, 2) * ps) * Yt3
wrong = Jp(f_wrong) * sp.exp(-I * sp.Rational(1, 2) * ps)
report("control: k = +1/2 does NOT reproduce the letter's operator", not allpts(wrong - letter))

# 4. the two other Euler conventions: psi' = psi + phi and psi'' = psi - phi
chart_check = {}
for label, sgn, c_expected in (
    ("N (psi' = psi + phi)", 1, k * sp.exp(I * ph) * sp.tan(th / 2)),
    ("S (psi'' = psi - phi)", -1, k * sp.exp(I * ph) / sp.tan(th / 2)),
):
    # f(phi, theta, psi) = e^{i k psi} Y = e^{i k psi'} Y' with psi' = psi + sgn*phi, Y' = e^{-i k sgn phi} Y
    # test J+ on a concrete function of (phi, theta, psi) built both ways, expressed back in the original variables
    Yt = sp.sin(th) * sp.exp(I * ph) + sp.cos(th / 2) ** 2  # concrete amplitude
    f_orig = sp.exp(I * k * ps) * Yt
    Yprime = sp.exp(-I * k * sgn * ph) * Yt
    # J+ f computed in original variables, then divided by e^{i k psi'} to read off the new amplitude
    lhs_c = Jp(f_orig) * sp.exp(-I * k * (ps + sgn * ph))
    Lp_Yprime = sp.exp(I * ph) * (sp.diff(Yprime, th) + I * sp.cot(th) * sp.diff(Yprime, ph))
    rhs_c = Lp_Yprime + c_expected * Yprime
    chart_check[label] = allpts(lhs_c - rhs_c)
    report(
        f"chart {label}: J+ acts as (L+ + c) with c = k e^{{i phi}} {'tan' if sgn == 1 else 'cot'}(theta/2)",
        chart_check[label],
    )

# 5. our frames are the second column of the Euler matrix: D e_2 = e^{i psi/2} eta
eta = sp.Matrix([-sp.exp(-I * ph / 2) * sp.sin(th / 2), sp.exp(I * ph / 2) * sp.cos(th / 2)])
col2 = D * sp.Matrix([0, 1])
report(
    "D(phi,theta,psi) e_2 = e^{i psi/2} eta",
    all(allpts((col2 - sp.exp(I * ps / 2) * eta)[r]) for r in range(2)),
)
report(
    "psi = -phi gives eta_N = e^{-i phi/2} eta; psi = +phi gives eta_S = e^{i phi/2} eta",
    all(
        allpts((col2.subs(ps, -ph) - sp.exp(-I * ph / 2) * eta)[r])
        and allpts((col2.subs(ps, ph) - sp.exp(I * ph / 2) * eta)[r])
        for r in range(2)
    ),
)

print("ALL PASS" if ok_all else "SOME FAILED")
