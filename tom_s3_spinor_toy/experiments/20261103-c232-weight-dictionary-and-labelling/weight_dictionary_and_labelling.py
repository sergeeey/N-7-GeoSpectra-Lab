"""C232: weight dictionary for xi, conj(xi) and g_ab, the Hopf-charge reading of Gamma_2(T_12) = (1/2) diag(1,-1), and the statement
that the ORDER of the weights (which component is negative) is a labelling convention.

Definitions (frozen with TOM-CERT-01 and C229): x1, x2 = xi^1, xi^2; y1, y2 = their conjugates (independent symbols);
g(xi) = [[x1, -y2], [x2, y1]]; (L_h f)(xi) = f(h^-1 xi); (R_k f)(xi) = f(xi.k), xi.k = k00 xi + k10 J xi, J xi = (-y2, y1);
T_a = -i sigma_a/2; J_a^L = i dL(T_a), J_a^R = i dR(T_a); Hopf charge Q = (#x) - (#y).

Predictions written BEFORE running:
  W1. (J3L, J3R) on (g00, g01, g10, g11) = ((-1/2,+1/2), (-1/2,-1/2), (+1/2,+1/2), (+1/2,-1/2))  [TOM-CERT-01].
  W2. On every g_ab, 2*J3R equals the Hopf charge Q (x-type functions Q = +1, y-type Q = -1), so J3R on the index b is
      (1/2) diag(1, -1): the same diagonal as Gamma_2(T_12) in the correspondent's equation (77), IF his index is b.
  W3. Relabelling the doublet by the swap sigma_x gives generators (sigma_1, -sigma_2, -sigma_3)/2: same algebra [T_a,T_b] = i eps T_c,
      D3 -> -D3. So 'the first component has a negative eigenvalue' holds for (xi^1, xi^2) and for eta = (y2, -y1), and is
      reversed for (y1, y2) or for the swapped labelling: it is a labelling choice, not a property of the representation.
  W4. The Casimir is unchanged by the swap (3/4).
"""

import sys

import sympy as sp

x1, x2, y1, y2 = sp.symbols("x1 x2 y1 y2")
I = sp.I
h = sp.Rational(1, 2)
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
T = [-I * s / 2 for s in SIG]
FAILS = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)


def expect_caught(name, cond):
    print(("CAUGHT " if not cond else "MISSED ") + name)
    if cond:
        FAILS.append("self-control not caught: " + name)


def conjm(M):
    return M.applyfunc(sp.conjugate)


def vf_apply(f, dx, dy):
    return sp.expand(
        sum(dx[i] * sp.diff(f, [x1, x2][i]) + dy[i] * sp.diff(f, [y1, y2][i]) for i in range(2))
    )


def dL_field(Ta):
    """d/dt f(exp(-tT) xi): delta xi = -T xi, delta conj = -conj(T) conj(xi)"""
    X = sp.Matrix([x1, x2])
    Y = sp.Matrix([y1, y2])
    return list(-Ta * X), list(-conjm(Ta) * Y)


def dR_field(Ta):
    """d/dt f(xi.exp(tT)): delta xi = T00 xi + T10 J xi"""
    X = sp.Matrix([x1, x2])
    Jx = sp.Matrix([-y2, y1])
    dx = list(Ta[0, 0] * X + Ta[1, 0] * Jx)
    Jy = sp.Matrix([-x2, x1])  # conj(J xi) = (-x2, x1)
    dy = list(sp.conjugate(Ta[0, 0]) * sp.Matrix([y1, y2]) + sp.conjugate(Ta[1, 0]) * Jy)
    return dx, dy


def J(kind, a, f):
    dx, dy = (dL_field if kind == "L" else dR_field)(T[a])
    return sp.expand(I * vf_apply(f, dx, dy))


g = {"g00": x1, "g01": -y2, "g10": x2, "g11": y1}
want = {"g00": (-h, h), "g01": (-h, -h), "g10": (h, h), "g11": (h, -h)}


def Q(f):
    p = sp.Poly(f, x1, x2, y1, y2)
    degs = {m[0] + m[1] - m[2] - m[3] for m in p.monoms()}
    return degs.pop() if len(degs) == 1 else None


for name, f in g.items():
    wl = sp.simplify(J("L", 2, f) / f)
    wr = sp.simplify(J("R", 2, f) / f)
    check(f"{name}: (J3L, J3R) = {want[name]}", (wl, wr) == want[name])
    check(f"{name}: 2*J3R = Hopf charge Q = {Q(f)}", 2 * wr == Q(f))
diag_b = sp.diag(h, -h)
check(
    "(1/2) diag(1,-1) equals the weight matrix of J3R on the right index (asserted entrywise)",
    [sp.simplify(J("R", 2, g["g00"]) / g["g00"]), sp.simplify(J("R", 2, g["g01"]) / g["g01"])]
    == [diag_b[0, 0], diag_b[1, 1]],
)

# algebra of J^L, J^R on generic polynomials, so the table above is not an accident of one generator
f0 = x1**2 * y2 + 3 * x2 * y1 * y2 - x1 * x2
okL = all(
    sp.expand(
        J("L", a, J("L", b, f0))
        - J("L", b, J("L", a, f0))
        - I * sum(sp.LeviCivita(a, b, c) * J("L", c, f0) for c in range(3))
    )
    == 0
    for a in range(3)
    for b in range(3)
)
okR = all(
    sp.expand(
        J("R", a, J("R", b, f0))
        - J("R", b, J("R", a, f0))
        - I * sum(sp.LeviCivita(a, b, c) * J("R", c, f0) for c in range(3))
    )
    == 0
    for a in range(3)
    for b in range(3)
)
check(
    "[J^L_a, J^L_b] = i eps J^L_c and [J^R_a, J^R_b] = i eps J^R_c on a test polynomial (J = i dX is a standard su(2))",
    okL and okR,
)

# W3, W4: swap relabelling on the 2x2 doublet generators  tau_a = sigma_a / 2 ((D_a on (xi1, xi2) acts as -tau_a))
tau = [s / 2 for s in SIG]
S1 = SIG[0]
tau_sw = [S1 * t * S1 for t in tau]
check(
    "swap relabelling keeps the su(2) algebra: [tau'_a, tau'_b] = i eps tau'_c",
    all(
        sp.simplify(
            tau_sw[a] * tau_sw[b]
            - tau_sw[b] * tau_sw[a]
            - I * sum((sp.LeviCivita(a, b, c) * tau_sw[c] for c in range(3)), sp.zeros(2))
        )
        == sp.zeros(2)
        for a in range(3)
        for b in range(3)
    ),
)
check(
    "swap relabelling: tau'_3 = -tau_3, tau'_2 = -tau_2, tau'_1 = tau_1",
    tau_sw[2] == -tau[2] and tau_sw[1] == -tau[1] and tau_sw[0] == tau[0],
)
check(
    "Casimir unchanged (3/4)",
    sum((t * t for t in tau_sw), sp.zeros(2)) == sp.Rational(3, 4) * sp.eye(2),
)


# which doublet has which ordering of the D3 = -J3L... weights (convention A of C229: D3 on a function = (1/i) d/dt f(exp(-i t sigma3/2) xi))
def D3A(f):
    sx = SIG[2] * sp.Matrix([x1, x2])
    sy = SIG[2].conjugate() * sp.Matrix([y1, y2])
    return sp.expand(
        -h * (sx[0] * sp.diff(f, x1) + sx[1] * sp.diff(f, x2))
        + h * (sy[0] * sp.diff(f, y1) + sy[1] * sp.diff(f, y2))
    )


def weights(vec):
    return [sp.simplify(D3A(v) / v) for v in vec]


check("(xi1, xi2): weights (-1/2, +1/2)", weights([x1, x2]) == [-h, h])
check(
    "eta = (y2, -y1): weights (-1/2, +1/2): the conjugate doublet in epsilon-relabelled order looks the same",
    weights([y2, -y1]) == [-h, h],
)
check("(y1, y2): weights (+1/2, -1/2): reversed order", weights([y1, y2]) == [h, -h])
check("(xi2, xi1) (swapped labelling): weights (+1/2, -1/2)", weights([x2, x1]) == [h, -h])

# self-controls
expect_caught("the swapped generators keep tau_3 (no sign flip)", tau_sw[2] == tau[2])
expect_caught("(y1, y2) has the same weights as (xi1, xi2)", weights([y1, y2]) == [-h, h])
expect_caught(
    "2*J3R differs from the Hopf charge on g01",
    2 * sp.simplify(J("R", 2, g["g01"]) / g["g01"]) != Q(g["g01"]),
)

print("\nFAILS:", FAILS if FAILS else "none")
sys.exit(1 if FAILS else 0)
