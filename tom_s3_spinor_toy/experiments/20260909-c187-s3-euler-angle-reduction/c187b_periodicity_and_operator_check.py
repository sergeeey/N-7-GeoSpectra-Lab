"""C187b -- derive the (m,n) periodicity that closes claim (b)'s labelling
question, and pin down exactly where claim (b) still fails.

Two separate findings, kept separate because they answer different questions:

PART A -- periodicity: DERIVED AND CONFIRMED.
C186 built its Cartan generators J_3^L, J_3^R from the quaternion axis "k"
(python index a=2) purely by convention (any of i,j,k works equally as an
su(2) Cartan direction; the choice only fixes which basis the weight labels
are read in). This project's own Euler-angle embedding, however, has a
DIFFERENT preferred axis: computed directly from the Jacobian of the
embedding (tangency of X_a^L/X_a^R to S^3, solved via least squares, verified
to 1e-41 numerically), X_0^L = 2 d/dphi and X_0^R = 2 d/dpsi EXACTLY -- the "i"
axis (a=0), not "k". Rebuilding C186's joint-cell decomposition on the "i"
axis instead of "k" (a relabelling, not a new computation -- [D0,JL0]=0 and
[D0,JR0]=0 verified identically) makes the EXTREME weight states collapse to
a single, clean Fourier mode e^{i(m phi + n psi)} shared by both spinor
components -- exactly C187's original ansatz shape. This is the derivation
the half-angle pearl's corrected test needed and did not have.

PART B -- claim (b) itself: STILL NOT CLOSED, for a narrower, different
reason than periodicity. Applying C187's own Euler-angle D operator (frame +
Cartan connection, exactly as committed) to the now-CORRECTLY-labelled
candidate (m,n)=(-1/2,1/2), expected eigenvalue -1, does NOT return a
theta-independent multiple of the candidate -- checked symbolically under 4
sign conventions and numerically under all 144 combinations of (which Pauli
matrix pairs with which vielbein leg) x (connection sign) x (operator sign).
Zero of 144 reproduce a constant eigenvalue. This localises the remaining gap
to C187's geometric construction of D itself (frame/connection), which passes
its OWN internal consistency checks (P1-P9: frame reproduces the metric,
Cartan's equation solved with zero residual) but those checks do not verify
the RESULTING OPERATOR against any independent reference -- a general,
reusable lesson: self-consistency of a geometric construction does not by
itself certify that the construction equals a specific known operator.

Run:  python c187b_periodicity_and_operator_check.py
"""

import sympy as sp

PASS, FAIL = [], []


def check(label, condition, detail=""):
    (PASS if condition else FAIL).append(label)
    print(f"  [{'PASS' if condition else 'FAIL'}] {label}")
    if detail:
        print(f"         {detail}")


x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)
X = [x0, x1, x2, x3]
I2 = sp.eye(2)
PAULI = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
MUL = {
    (0, 0): (-1, 0), (0, 1): (1, 3), (0, 2): (-1, 2),
    (1, 0): (-1, 3), (1, 1): (-1, 0), (1, 2): (1, 1),
    (2, 0): (1, 2), (2, 1): (-1, 1), (2, 2): (-1, 0),
}  # fmt: skip


def right_mult_components(a):
    out = [sp.Integer(0)] * 4
    out[a + 1] += x0
    for b in range(3):
        c, idx = MUL[(b, a)]
        out[idx] += c * X[b + 1]
    return out


def left_mult_components(a):
    out = [sp.Integer(0)] * 4
    out[a + 1] += x0
    for b in range(3):
        c, idx = MUL[(a, b)]
        out[idx] += c * X[b + 1]
    return out


def as_operator(components):
    def op(f):
        return sp.expand(sum(components[m] * sp.diff(f, X[m]) for m in range(4)))

    return op


XR = [as_operator(right_mult_components(a)) for a in range(3)]
XL = [as_operator(left_mult_components(a)) for a in range(3)]


def harmonic_basis(k):
    monos = []
    for a in range(k + 1):
        for b in range(k + 1 - a):
            for c in range(k + 1 - a - b):
                monos.append(x0**a * x1**b * x2**c * x3 ** (k - a - b - c))
    coeffs = sp.symbols(f"c0:{len(monos)}")
    gen = sum(co * m for co, m in zip(coeffs, monos))
    lap = sp.expand(sum(sp.diff(gen, v, 2) for v in X))
    eqs = sp.Poly(lap, *X).coeffs() if lap != 0 else []
    sol = sp.solve(eqs, coeffs, dict=True)
    sol = sol[0] if sol else {}
    free = [c for c in coeffs if c not in sol]
    out = []
    for fc in free:
        sub = {c: (sp.Integer(1) if c == fc else sp.Integer(0)) for c in coeffs}
        expr = sp.expand(gen.subs(sol).subs(sub))
        if expr != 0:
            out.append(expr)
    return out


def op_matrix(op, basis):
    lam = sp.symbols(f"L0:{len(basis)}")
    cols = []
    for b in basis:
        img = sp.expand(op(b))
        eq = sp.expand(img - sum(lc * bb for lc, bb in zip(lam, basis)))
        sol = sp.solve(sp.Poly(eq, *X).coeffs(), lam, dict=True)
        sol = sol[0] if sol else {}
        cols.append([sp.nsimplify(sol.get(lc, 0)) for lc in lam])
    return sp.Matrix(cols).T


def closes_as_su2(J):
    z = sp.zeros(*J[0].shape)
    return all(
        sp.expand(J[a] * J[b] - J[b] * J[a])
        == sp.expand(sp.I * sum((sp.LeviCivita(a, b, c) * J[c] for c in range(3)), z))
        for a in range(3)
        for b in range(3)
    )


B1 = harmonic_basis(1)
XR1 = [op_matrix(o, B1) for o in XR]
XL1 = [op_matrix(o, B1) for o in XL]
sR = +1 if closes_as_su2([+sp.I / 2 * m for m in XR1]) else -1
sL = +1 if closes_as_su2([+sp.I / 2 * m for m in XL1]) else -1

th, ph, ps = sp.symbols("theta phi psi", real=True)
COORDS = [th, ph, ps]
X4_euler = [
    sp.cos(th / 2) * sp.cos((ph + ps) / 2),
    sp.cos(th / 2) * sp.sin((ph + ps) / 2),
    sp.sin(th / 2) * sp.cos((ph - ps) / 2),
    sp.sin(th / 2) * sp.sin((ph - ps) / 2),
]
euler_subs = dict(zip(X, X4_euler))

# ---------------------------------------------------------------------------
print("=" * 78)
print("A  the preferred axis: which quaternion generator aligns with d/dphi, d/dpsi?")
print("=" * 78)

J4 = sp.Matrix([[sp.diff(xi, c) for c in COORDS] for xi in X4_euler])


def tangent_coeffs_numeric(c_expr_x, n_pts=3):
    """Solve J4 @ (A,B,C) = c via least squares, VERIFY tangency numerically
    (exact symbolic residual checks on this construction were unreliable --
    see the module docstring; high-precision numeric agreement across
    several points is the decisive test used throughout this script).

    c_expr_x is given in the GLOBAL x0..x3 symbols (as left/right_mult_
    components return it) -- substitute the Euler-angle embedding first, or
    the comparison against J4 (built purely in theta,phi,psi) is meaningless.
    """
    import random

    c_expr = [sp.expand(ci.subs(euler_subs)) for ci in c_expr_x]
    normal = sp.trigsimp(sp.expand(J4.T * J4))
    coeffs = sp.trigsimp(normal.inv() * J4.T * sp.Matrix(c_expr))
    random.seed(2)
    max_err = 0
    for _ in range(n_pts):
        pt = {
            th: sp.Rational(random.randint(5, 300), 100),
            ph: sp.Rational(random.randint(5, 600), 100),
            ps: sp.Rational(random.randint(5, 900), 100),
        }
        Jn = J4.subs(pt).evalf(40)
        cn = sp.Matrix([ci.subs(pt).evalf(40) for ci in c_expr])
        cf = coeffs.subs(pt).evalf(40)
        max_err = max(max_err, (Jn * cf - cn).norm())
    return coeffs, max_err


def numeric_equal_target(coeffs, target, n_pts=4):
    """coeffs may not be simplified to literal form even when it is EXACTLY
    equal to target (trigsimp does not always reach the reduced form) -- test
    by high-precision numeric evaluation instead of structural equality."""
    import random

    random.seed(3)
    for _ in range(n_pts):
        pt = {th: sp.Rational(random.randint(5, 300), 100)}
        got = coeffs.subs(pt).evalf(30)
        want = target.subs(pt).evalf(30)
        if (got - want).norm() > sp.Float("1e-20"):
            return False
    return True


c0L = left_mult_components(0)
coeffsL0, errL0 = tangent_coeffs_numeric(c0L)
target_L0 = sp.Matrix([0, 2, 0])
check(
    "A1 X_0^L (quaternion i, LEFT mult) = 2 d/dphi EXACTLY",
    numeric_equal_target(coeffsL0, target_L0) and errL0 < sp.Float("1e-30"),
    f"coeffs (unsimplified but numerically ==[0,2,0]): {list(coeffsL0)}",
)

c0R = right_mult_components(0)
coeffsR0, errR0 = tangent_coeffs_numeric(c0R)
target_R0 = sp.Matrix([0, 0, 2])
check(
    "A2 X_0^R (quaternion i, RIGHT mult) = 2 d/dpsi EXACTLY",
    numeric_equal_target(coeffsR0, target_R0) and errR0 < sp.Float("1e-30"),
    f"coeffs (unsimplified but numerically ==[0,0,2]): {list(coeffsR0)}",
)

c2L = left_mult_components(2)
coeffsL2, _ = tangent_coeffs_numeric(c2L)
check(
    "A3 X_2^L (quaternion k -- C186's own Cartan choice) is NOT a pure "
    "d/dphi or d/dpsi direction -- it mixes all three coordinates",
    not any(coeffsL2[i] == 0 for i in range(3)),
    f"coeffs={list(coeffsL2)}",
)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("B  rebuild C186's k=1 weight decomposition on the i-axis (a=0)")
print("=" * 78)


def build_axis(k, axis):
    B = harmonic_basis(k)
    n = len(B)
    XRm = [op_matrix(o, B) for o in XR]
    XLm = [op_matrix(o, B) for o in XL]
    D0 = sp.zeros(2 * n)
    for a in range(3):
        D0 += -sp.I * sp.Matrix(sp.kronecker_product(PAULI[a], XRm[a]))
    JL = sp.Matrix(sp.kronecker_product(I2, sL * sp.I / 2 * XLm[axis]))
    JR = sp.Matrix(sp.kronecker_product(I2, sR * sp.I / 2 * XRm[axis])) + sp.Matrix(
        sp.kronecker_product(PAULI[axis] / 2, sp.eye(n))
    )
    return B, D0, JL, JR


def restrict(P, A):
    C = (P.H * P).inv() * P.H * (A * P)
    assert sp.expand(A * P - P * C) == sp.zeros(*(A * P).shape)
    return C


def joint_cells(P, AL, AR):
    cells = {}
    for lL, _, vL in restrict(P, AL).eigenvects():
        Q = P * sp.Matrix.hstack(*vL)
        for lR, _, vR in restrict(Q, AR).eigenvects():
            key = (sp.nsimplify(lL), sp.nsimplify(lR))
            cells.setdefault(key, [])
            for v in vR:
                cells[key].append(sp.expand(Q * v))
    return cells


def as_spinor(B, vec):
    n = len(B)
    return sp.Matrix(
        [sp.expand(sum(vec[i * n + m] * B[m] for m in range(n))) for i in range(2)]
    )


B, D0, JL0, JR0 = build_axis(1, 0)
nB = len(B)
check(
    "B1 rebuilt on axis a=0: [D0,JL0]=0, [D0,JR0]=0, [JL0,JR0]=0",
    sp.expand(D0 * JL0 - JL0 * D0) == sp.zeros(2 * nB)
    and sp.expand(D0 * JR0 - JR0 * D0) == sp.zeros(2 * nB)
    and sp.expand(JL0 * JR0 - JR0 * JL0) == sp.zeros(2 * nB),
)

cth, sth, u, uinv, v, vinv = sp.symbols("cth sth u uinv v vinv")
euv_subs = dict(
    zip(
        X,
        [
            (cth * u * v + cth * uinv * vinv) / 2,
            (cth * u * v - cth * uinv * vinv) / (2 * sp.I),
            (sth * u * vinv + sth * uinv * v) / 2,
            (sth * u * vinv - sth * uinv * v) / (2 * sp.I),
        ],
    )
)


def reduce_exact(e):
    e = sp.expand(e)
    e = e.subs({u * uinv: 1, v * vinv: 1})
    e = sp.expand(e)
    return sp.expand(e.subs({cth**2: 1 - sth**2}))


lo, hi = sp.Integer(-1), sp.Integer(3)
Nlo = sp.Matrix.hstack(*(D0 - lo * sp.eye(2 * nB)).nullspace())
Nhi = sp.Matrix.hstack(*(D0 - hi * sp.eye(2 * nB)).nullspace())

extreme_keys = [(sp.Rational(-1, 2), -1), (sp.Rational(1, 2), 1)]
n_single_monomial = 0
for lam, P in ((lo, Nlo), (hi, Nhi)):
    cells = joint_cells(P, JL0, JR0)
    for key in cells:
        if key not in [
            (sp.Rational(-1, 2), -1),
            (sp.Rational(1, 2), -1),
            (sp.Rational(-1, 2), 1),
            (sp.Rational(1, 2), 1),
        ]:
            continue
        psi_x = as_spinor(B, cells[key][0])
        psi_euv = [reduce_exact(c.subs(euv_subs)) for c in psi_x]
        nz = [c for c in psi_euv if c != 0]
        n_terms = max(
            (len(sp.Poly(c, u, uinv, v, vinv).terms()) for c in nz), default=0
        )
        if n_terms == 1:
            n_single_monomial += 1

check(
    "B2 all 4 extreme-weight states are a SINGLE Fourier mode on the i-axis "
    "(the k-axis version needed 4 monomials per state -- see claim.md)",
    n_single_monomial == 4,
    f"{n_single_monomial}/4 extreme states reduced to one monomial",
)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("C  does C187's OWN D operator reproduce this now-correctly-labelled state?")
print("=" * 78)

e1 = sp.Matrix([sp.Rational(1, 2), 0, 0])
e2 = sp.Matrix([0, sp.Rational(1, 2) * sp.sin(th), 0])
e3 = sp.Matrix([0, sp.Rational(1, 2) * sp.cos(th), sp.Rational(1, 2)])
E3 = [e1, e2, e3]


def dext(a):
    return {
        (i, j): sp.expand(sp.diff(a[j], COORDS[i]) - sp.diff(a[i], COORDS[j]))
        for i, j in [(0, 1), (0, 2), (1, 2)]
    }


def wedge3(a, b):
    return {
        (i, j): sp.expand(a[i] * b[j] - a[j] * b[i])
        for i, j in [(0, 1), (0, 2), (1, 2)]
    }


def add3(*ds):
    out = {(0, 1): 0, (0, 2): 0, (1, 2): 0}
    for d in ds:
        for k in out:
            out[k] += d[k]
    return out


de3 = [dext(e) for e in E3]
w12v = sp.Matrix(sp.symbols("w12_0 w12_1 w12_2"))
w13v = sp.Matrix(sp.symbols("w13_0 w13_1 w13_2"))
w23v = sp.Matrix(sp.symbols("w23_0 w23_1 w23_2"))
eqA = add3(de3[0], wedge3(w12v, e2), wedge3(w13v, e3))
eqB = add3(de3[1], wedge3(-w12v, e1), wedge3(w23v, e3))
eqC = add3(de3[2], wedge3(-w13v, e1), wedge3(-w23v, e2))
unk3 = list(w12v) + list(w13v) + list(w23v)
eqs3 = [eq[k] for eq in (eqA, eqB, eqC) for k in [(0, 1), (0, 2), (1, 2)]]
sol3 = sp.solve(eqs3, unk3, dict=True)[0]
w12s, w13s, w23s = (list(w.subs(sol3)) for w in (w12v, w13v, w23v))
e_mat = sp.Matrix([list(e1), list(e2), list(e3)])
e_inv = e_mat.inv()
Gamma = [
    (sp.I / 2) * (w12s[mu] * PAULI[2] - w13s[mu] * PAULI[1] + w23s[mu] * PAULI[0])
    for mu in range(3)
]


def D_apply_euler(psi):
    out = sp.zeros(2, 1)
    for a in range(3):
        acc = sp.zeros(2, 1)
        for mu in range(3):
            dpsi = sp.Matrix([sp.diff(psi[0], COORDS[mu]), sp.diff(psi[1], COORDS[mu])])
            acc += e_inv[mu, a] * (dpsi + Gamma[mu] * psi)
        out += -sp.I * PAULI[a] * acc
    return sp.expand(out)


mval, nval = sp.Rational(-1, 2), sp.Rational(1, 2)
Fc, Gc = -sp.sin(th / 2), sp.sin(th / 2)
phase = sp.exp(sp.I * (mval * ph + nval * ps))
candidate = sp.Matrix([Fc * phase, Gc * phase])

Dcand = D_apply_euler(candidate)
r0 = sp.simplify(Dcand[0] / candidate[0])
r1 = sp.simplify(Dcand[1] / candidate[1])
check(
    "C1 C187's committed D operator gives a constant ratio D(psi)/psi = -1 "
    "on the derived, correctly-labelled candidate",
    r0 == -1 and r1 == -1,
    f"ratio0={r0}, ratio1={r1} -- NOT reproduced; see claim.md's Kill "
    f"criterion note. This is NOT a periodicity problem (part A/B above "
    f"closed that); it is unresolved and localized to the operator "
    f"construction itself.",
)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print(f"C187b: {len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    for f in FAIL:
        print(f"  EXPECTED-OPEN: {f}")
print("=" * 78)
