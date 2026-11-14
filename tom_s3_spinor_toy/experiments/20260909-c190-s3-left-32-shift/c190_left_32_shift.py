"""C190 -- derive the connection-correction shift for the LEFT-acting S^3
Dirac operator, mirroring C189's right-acting derivation.

The letter to Tom says, in passing: "using the right-acting generators
rather than the left-acting ones is a convention: the left-acting version
is an equally good operator, and it produces the mirror-image spectrum,
with the constant below coming out -3/2 instead of +3/2." That is: the
letter's own stated expectation is RIGHT-acting -> +3/2, LEFT-acting -> -3/2.

This round computes the LEFT-acting shift the same way C189 computed the
right-acting one -- Cartan's structure equation, zero residual, no
quoting -- and finds the OPPOSITE assignment from what the letter states,
confirmed by the SAME external cross-check C189 used (does the shifted
spectrum reproduce the known-correct +-(l+3/2), NEVER below |lambda|=3/2 in
magnitude). The letter's own aside on this point was never itself derived
(by its own admission, the 3/2 value was "matched, not derived," and no
connection was built for either handedness before this session) -- so this
finding corrects an unverified expectation, not a computed prior result.

Run:  python c190_left_32_shift.py
"""

import sympy as sp

PASS, FAIL = [], []


def check(label, condition, detail=""):
    (PASS if condition else FAIL).append(label)
    print(f"  [{'PASS' if condition else 'FAIL'}] {label}")
    if detail:
        print(f"         {detail}")


th, ph, ps = sp.symbols("theta phi psi", real=True)
COORDS = [th, ph, ps]

x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)
X4 = [x0, x1, x2, x3]
MUL = {
    (0, 0): (-1, 0), (0, 1): (1, 3), (0, 2): (-1, 2),
    (1, 0): (-1, 3), (1, 1): (-1, 0), (1, 2): (1, 1),
    (2, 0): (1, 2), (2, 1): (-1, 1), (2, 2): (-1, 0),
}  # fmt: skip


def left_mult_components(a):
    out = [sp.Integer(0)] * 4
    out[a + 1] += X4[0]
    for b in range(3):
        c, idx = MUL[(a, b)]
        out[idx] += c * X4[b + 1]
    return out


def as_operator_amb(components):
    def op(f):
        return sp.expand(sum(components[m] * sp.diff(f, X4[m]) for m in range(4)))

    return op


XL_amb_op = [as_operator_amb(left_mult_components(a)) for a in range(3)]

X4_euler = [
    sp.cos(th / 2) * sp.cos((ph + ps) / 2),
    sp.cos(th / 2) * sp.sin((ph + ps) / 2),
    sp.sin(th / 2) * sp.cos((ph - ps) / 2),
    sp.sin(th / 2) * sp.sin((ph - ps) / 2),
]
euler_subs = dict(zip(X4, X4_euler))

# ---------------------------------------------------------------------------
print("=" * 78)
print("A  X_a^L is orthonormal (same argument as C189, checked again for L)")
print("=" * 78)

XL_amb = [left_mult_components(a) for a in range(3)]
G_amb = sp.Matrix(
    [
        [
            sp.expand(sum(XL_amb[a][m] * XL_amb[b][m] for m in range(4)))
            for b in range(3)
        ]
        for a in range(3)
    ]
)
sphere = sp.expand(sum(v**2 for v in X4))
check(
    "P1 g(X_a^L, X_b^L) = delta_ab * (x0^2+..+x3^2) identically",
    all(
        sp.expand(G_amb[a, b] - (sphere if a == b else 0)) == 0
        for a in range(3)
        for b in range(3)
    ),
)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("B  X_a^L in Euler-angle coordinates, verified against the closed form")
print("=" * 78)

J4 = sp.Matrix([[sp.diff(xi, c) for c in COORDS] for xi in X4_euler])


def tangent_coeffs(a, n_pts=5):
    import random

    c_x = left_mult_components(a)
    c_expr = [sp.expand(ci.subs(euler_subs)) for ci in c_x]
    normal = sp.trigsimp(sp.expand(J4.T * J4))
    coeffs = sp.trigsimp(normal.inv() * J4.T * sp.Matrix(c_expr))
    random.seed(a + 500)
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


CLOSED_FORM_L = [
    sp.Matrix([0, 2, 0]),
    sp.Matrix(
        [2 * sp.cos(ph), -2 * sp.sin(ph) / sp.tan(th), 2 * sp.sin(ph) / sp.sin(th)]
    ),
    sp.Matrix(
        [2 * sp.sin(ph), 2 * sp.cos(ph) / sp.tan(th), -2 * sp.cos(ph) / sp.sin(th)]
    ),
]

for a in range(3):
    derived, tang_err = tangent_coeffs(a)
    check(
        f"P{2 + a}a X_{a}^L is genuinely tangent to S^3", tang_err < sp.Float("1e-30")
    )
    import random

    random.seed(a + 600)
    max_diff = 0
    for _ in range(5):
        pt = {
            th: sp.Rational(random.randint(5, 300), 100),
            ph: sp.Rational(random.randint(5, 600), 100),
            ps: sp.Rational(random.randint(5, 900), 100),
        }
        d = (derived.subs(pt).evalf(30) - CLOSED_FORM_L[a].subs(pt).evalf(30)).norm()
        max_diff = max(max_diff, d)
    check(
        f"P{2 + a}b X_{a}^L matches its stated closed form",
        max_diff < sp.Float("1e-25"),
        f"max diff = {max_diff}",
    )

XL_coeffs = sp.Matrix(CLOSED_FORM_L).reshape(3, 3)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("C  dual coframe + Cartan's structure equation for the L-connection")
print("=" * 78)

M_inv = sp.simplify(XL_coeffs.inv())
E = [list(M_inv[:, a]) for a in range(3)]
check(
    "P5 the dual L-coframe satisfies e^a(X_b) = delta_ab exactly",
    all(
        sp.simplify(sum(E[a][mu] * XL_coeffs[b, mu] for mu in range(3)))
        == (1 if a == b else 0)
        for a in range(3)
        for b in range(3)
    ),
)


def dext(a_coeffs):
    return {
        (i, j): sp.expand(
            sp.diff(a_coeffs[j], COORDS[i]) - sp.diff(a_coeffs[i], COORDS[j])
        )
        for i, j in [(0, 1), (0, 2), (1, 2)]
    }


def wedge(a_coeffs, b_coeffs):
    return {
        (i, j): sp.expand(a_coeffs[i] * b_coeffs[j] - a_coeffs[j] * b_coeffs[i])
        for i, j in [(0, 1), (0, 2), (1, 2)]
    }


def add2(*ds):
    out = {(0, 1): 0, (0, 2): 0, (1, 2): 0}
    for d in ds:
        for k in out:
            out[k] += d[k]
    return out


dE = [dext(e) for e in E]
w01_sym = sp.Matrix(sp.symbols("w01_0 w01_1 w01_2"))
w02_sym = sp.Matrix(sp.symbols("w02_0 w02_1 w02_2"))
w12_sym = sp.Matrix(sp.symbols("w12_0 w12_1 w12_2"))
eqA = add2(dE[0], wedge(list(w01_sym), E[1]), wedge(list(w02_sym), E[2]))
eqB = add2(dE[1], wedge(list(-w01_sym), E[0]), wedge(list(w12_sym), E[2]))
eqC = add2(dE[2], wedge(list(-w02_sym), E[0]), wedge(list(-w12_sym), E[1]))
unknowns = list(w01_sym) + list(w02_sym) + list(w12_sym)
eqs = [eq[k] for eq in (eqA, eqB, eqC) for k in [(0, 1), (0, 2), (1, 2)]]
sol = sp.solve(eqs, unknowns, dict=True)
check("P6 Cartan's structure equation has a unique solution", len(sol) == 1)

w01 = [sp.sin(ph) / 2, sp.Integer(0), -sp.sin(th) * sp.cos(ph) / 2]
w02 = [-sp.cos(ph) / 2, sp.Integer(0), -sp.sin(ph) * sp.sin(th) / 2]
w12 = [sp.Integer(0), sp.Rational(1, 2), sp.cos(th) / 2]

eqA2 = add2(dE[0], wedge(w01, E[1]), wedge(w02, E[2]))
eqB2 = add2(dE[1], wedge([-c for c in w01], E[0]), wedge(w12, E[2]))
eqC2 = add2(dE[2], wedge([-c for c in w02], E[0]), wedge([-c for c in w12], E[1]))
resid = [
    sp.trigsimp(eq[k]) for eq in (eqA2, eqB2, eqC2) for k in [(0, 1), (0, 2), (1, 2)]
]
check(
    "P7 the closed-form L-connection satisfies Cartan's equation IDENTICALLY",
    all(r == 0 for r in resid),
    f"omega_01={w01}, omega_02={w02}, omega_12={w12}",
)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("D  D_full^L - D_0^L: compute the shift, do not assume its sign")
print("=" * 78)

PAULI = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
Gamma = [
    (sp.I / 2) * (w01[mu] * PAULI[2] - w02[mu] * PAULI[1] + w12[mu] * PAULI[0])
    for mu in range(3)
]
GammaX = [
    sum((Gamma[mu] * XL_coeffs[a, mu] for mu in range(3)), sp.zeros(2, 2))
    for a in range(3)
]
extra = sp.simplify(
    -sp.I * sum((PAULI[a] * GammaX[a] for a in range(3)), sp.zeros(2, 2))
)

check(
    "P8 D_full^L - D_0^L is a scalar matrix, position-independent",
    extra == extra[0, 0] * sp.eye(2) and extra[0, 1] == 0,
    f"D_full^L - D_0^L = {list(extra)}",
)
shift_L = sp.nsimplify(extra[0, 0])
check(
    "P9 the L-shift is exactly +3/2 (mirror of C189's -3/2 for R)",
    shift_L == sp.Rational(3, 2),
    f"computed L-shift = {shift_L}",
)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("E  D_0^L's own spectrum -- IS it really the mirror of D_0^R's?")
print("=" * 78)


def harmonic_basis(k):
    monos = []
    for a in range(k + 1):
        for b in range(k + 1 - a):
            for c in range(k + 1 - a - b):
                monos.append(x0**a * x1**b * x2**c * x3 ** (k - a - b - c))
    coeffs = sp.symbols(f"c0:{len(monos)}")
    gen = sum(co * m for co, m in zip(coeffs, monos))
    lap = sp.expand(sum(sp.diff(gen, v, 2) for v in X4))
    eqs_ = sp.Poly(lap, *X4).coeffs() if lap != 0 else []
    sol_ = sp.solve(eqs_, coeffs, dict=True)
    sol_ = sol_[0] if sol_ else {}
    free = [c for c in coeffs if c not in sol_]
    out = []
    for fc in free:
        sub = {c: (sp.Integer(1) if c == fc else sp.Integer(0)) for c in coeffs}
        expr = sp.expand(gen.subs(sol_).subs(sub))
        if expr != 0:
            out.append(expr)
    return out


def op_matrix(op, basis):
    lam_ = sp.symbols(f"L0:{len(basis)}")
    cols = []
    for b in basis:
        img = sp.expand(op(b))
        eq_ = sp.expand(img - sum(lc * bb for lc, bb in zip(lam_, basis)))
        sol_ = sp.solve(sp.Poly(eq_, *X4).coeffs(), lam_, dict=True)
        sol_ = sol_[0] if sol_ else {}
        cols.append([sp.nsimplify(sol_.get(lc, 0)) for lc in lam_])
    return sp.Matrix(cols).T


for k in range(3):
    B = harmonic_basis(k)
    n = len(B)
    XLm = [op_matrix(o, B) for o in XL_amb_op]
    D0L = sp.zeros(2 * n)
    for a in range(3):
        D0L += -sp.I * sp.Matrix(sp.kronecker_product(PAULI[a], XLm[a]))
    spec = dict(D0L.eigenvals())
    # D_0^R = {-k: (k+1)(k+2), k+2: k(k+1)}; D_0^L should be its NEGATION:
    # {+k: (k+1)(k+2), -(k+2): k(k+1)} -- collapsing to {0:2} at k=0 since
    # the k(k+1) branch has multiplicity 0 there.
    expected_mirror = {k: (k + 1) * (k + 2)}
    if k * (k + 1) > 0:
        expected_mirror[-(k + 2)] = k * (k + 1)
    check(
        f"P{10 + k} k={k}: D_0^L spectrum = {spec}, is exactly D_0^R's "
        f"spectrum NEGATED (mirror-image, per the letter's OWN correct "
        f"half of this claim)",
        spec == expected_mirror,
        f"expected -D_0^R pattern {expected_mirror}",
    )

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("F  the discrepancy with the letter's stated sign assignment")
print("=" * 78)

N = 20
d0_neg = {-k: (k + 1) * (k + 2) for k in range(N)}
d0_pos = {k + 2: k * (k + 1) for k in range(N) if k * (k + 1) > 0}
full = dict(d0_neg)
for v, m in d0_pos.items():
    full[v] = full.get(v, 0) + m


def score_shift(shift_val):
    shifted = {sp.Rational(v) + shift_val: m for v, m in full.items()}
    expected = {}
    for lvl in range(N - 2):
        expected[-(lvl + sp.Rational(3, 2))] = (lvl + 1) * (lvl + 2)
        expected[(lvl + sp.Rational(3, 2))] = (lvl + 1) * (lvl + 2)
    common = sorted(set(shifted) & set(expected), key=float)
    mism = [v for v in common if shifted[v] != expected[v]]
    sub_floor = [v for v in shifted if abs(float(v)) < 1.5]
    return len(common), len(mism), sub_floor


common_neg, mism_neg, sub_neg = score_shift(sp.Rational(-3, 2))
common_pos, mism_pos, sub_pos = score_shift(sp.Rational(3, 2))
print(
    f"  D_0^R shifted by -3/2 (this round's + C189's derived value): "
    f"{common_neg} checked, {mism_neg} mismatches, sub-floor values {sub_neg}"
)
print(
    f"  D_0^R shifted by +3/2 (the letter's stated expectation):     "
    f"{common_pos} checked, {mism_pos} mismatches, sub-floor values {sub_pos}"
)
check(
    "P13 the DERIVED shift (-3/2 for R, verified via Cartan) reproduces the "
    "physical spectrum with ZERO error; the letter's stated expectation "
    "(+3/2 for R) does NOT -- confirming the letter's aside on handedness "
    "vs sign was an unverified guess, and it had the assignment backwards",
    mism_neg == 0 and not sub_neg and (mism_pos > 0 or sub_pos),
)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print(f"C190: {len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    for f in FAIL:
        print(f"  FAILED: {f}")
print("=" * 78)
