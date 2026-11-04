"""C238: tool check of the checkable statements in T. Lawrence, 'Symmetries of Field Configurations and No-Go Theorems',
Preprints.org doi:10.20944/preprints202510.2222.v2 (posted 3 Sept 2026, not peer-reviewed; 21 pp). Equation numbers are those of v2.

Artifact identity (Gate 1): this is the preprint v2, NOT the 27-page book chapter shown in the call of 2026-11-03 (the chapter has a de Sitter
part that the preprint lacks; Tom: 'I hadn't even included the stuff about de Sitter space in there at the time').

Predictions written BEFORE running:
  A1. Eq (3) (rotation 'as a diffeomorphism') maps the polar angle theta -> theta - omega, but eq (5) says theta -> theta + omega: sign mismatch
      inside the paper. Eq (4) (the covariance, passive) and eq (6) are consistent with each other and with (3).
  A2. Worked examples (21)-(30): V(A) = (-4, 12); V_r = 13, V_theta = 13/2; after theta' = theta + pi/3, A = (sqrt13, pi/2) and V_theta unchanged.
  A3. Eq (14): d/dtheta = x d/dy - y d/dx. Eq (57) as printed, i L_z = x d_y - y d_z, has a typo (y d_z should be y d_x); with L_z = -i(x d_y - y d_x), i L_z = d_phi.
  A4. Eq (60) is the metric induced on S^2 by the embedding (59). Eqs (62)-(63) are the infinitesimal rotations -theta x r (rotation by -theta), preserve r, are Killing for (60),
      and their r -> infinity limits are (65)-(68).
  A5. For S^3 in sigma coordinates (the 'straightforward generalisation to S^N'): the six fields P_a = z d_a and M_ab = p_a d_b - p_b d_a close as so(4)
      ([P_a,P_b] = -M_ab), are Killing for the metric g_ab = delta_ab + p_a p_b/(r^2 - p^2), and P_a / r commute in the limit r -> infinity.
  A6. Section 5.5 counting claim: in so(N2+1) the commutant of the Cartan subalgebra of so(N2) has dimension rank(so(N2)) + 1 if N2 is odd, + 0 if N2 is even (N2 = 1..8).
  A7. For N2 = 3, so(4) = su(2)_L + su(2)_R; the stabiliser so(3) is the diagonal; the extra commuting generator is a broken one, J3L - J3R (a rotation in one plane of R^4),
      and on the degree-n harmonics the joint spectrum of (iX3, iY3) is {(m_L,m_R)}, each pair once.
Self-controls (must be CAUGHT): claim (5) is consistent with (3); claim extra commuting generator also for N2 = 2; claim [P_a,P_b] = +M_ab; claim a wrong metric (60) with plus-minus sign flipped is Killing.
"""

import itertools
import sys

import sympy as sp

FAILS = []
R = sp.Rational


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)


def expect_caught(name, cond):
    print(("CAUGHT " if not cond else "MISSED ") + name)
    if cond:
        FAILS.append("self-control not caught: " + name)


# ---------------------------------------------------------------- A1
r, th, om = sp.symbols("r theta omega", positive=True)
x, y = r * sp.cos(th), r * sp.sin(th)
x3 = x * sp.cos(om) + y * sp.sin(om)  # eq (3), first component
y3 = -x * sp.sin(om) + y * sp.cos(om)  # eq (3), second component
check(
    "A1: eq (3) maps (r,theta) to (r, theta - omega)",
    sp.simplify(x3 - r * sp.cos(th - om)) == 0 and sp.simplify(y3 - r * sp.sin(th - om)) == 0,
)
expect_caught(
    "A1 control: eq (3) maps theta to theta + omega (as eq (5) states)",
    sp.simplify(x3 - r * sp.cos(th + om)) == 0,
)
check(
    "A1: eq (5) (theta + omega) is the map x cos w - y sin w, -(...) NOT the map (3): they differ",
    sp.simplify(x * sp.cos(om) - y * sp.sin(om) - x3) != 0,
)
check(
    "A1: eq (3) as printed gives theta' = theta - omega (same formula as the covariance (4)/(6)), which differs from the map x cos w - y sin w, ... implied by (5)",
    sp.simplify(x3 - r * sp.cos(th - om)) == 0
    and sp.simplify(y3 - r * sp.sin(th - om)) == 0
    and sp.simplify(x3 - (x * sp.cos(om) - y * sp.sin(om))) != 0,
)

# ---------------------------------------------------------------- A2
xx, yy = sp.symbols("x y", real=True)
V1 = xx**2 + 3 * yy - 17
V2 = 3 * xx - yy**2 + 15
check(
    "A2: V(A) at (2,3) = (-4, 12)", (V1.subs({xx: 2, yy: 3}), V2.subs({xx: 2, yy: 3})) == (-4, 12)
)
xp = sp.Symbol("xp")
check(
    "A2: after x' = x + 3 the components at A are unchanged (eq 23-24)",
    ((xp - 3) ** 2 + 3 * 3 - 17).subs(xp, 5) == -4 and (3 * (xp - 3) - 9 + 15).subs(xp, 5) == 12,
)
rr, tt = sp.symbols("rr tt", positive=True)
Vr, Vth = rr**2, rr**2 * sp.sin(tt)
pt = {rr: sp.sqrt(13), tt: sp.pi / 6}
check(
    "A2: V_r = 13, V_theta = 13/2 at (sqrt13, pi/6)",
    (sp.simplify(Vr.subs(pt)), sp.simplify(Vth.subs(pt))) == (13, R(13, 2)),
)
check(
    "A2: A has theta' = pi/2 and V_theta = r'^2 sin(theta' - pi/3) = 13/2",
    sp.simplify((sp.pi / 6 + sp.pi / 3) - sp.pi / 2) == 0
    and sp.simplify((13 * sp.sin(sp.pi / 2 - sp.pi / 3)) - R(13, 2)) == 0,
)

# ---------------------------------------------------------------- A3
f = sp.Function("f")
rho, ph = sp.symbols("rho phi", positive=True)
X_, Y_ = sp.symbols("X Y", real=True)
g = f(X_, Y_)
dth = sp.diff(g.subs({X_: rho * sp.cos(ph), Y_: rho * sp.sin(ph)}), ph)
cart = (X_ * sp.diff(g, Y_) - Y_ * sp.diff(g, X_)).subs(
    {X_: rho * sp.cos(ph), Y_: rho * sp.sin(ph)}
)
check(
    "A3: eq (14) d/dtheta = x d_y - y d_x (chain rule)", sp.simplify(dth.doit() - cart.doit()) == 0
)
wrong = (X_ * sp.diff(g, Y_)).subs({X_: rho * sp.cos(ph), Y_: rho * sp.sin(ph)})
expect_caught(
    "A3 control: eq (57) as printed read literally (y d_z, no y d_x term in the plane) equals d_phi",
    sp.simplify(dth.doit() - wrong.doit()) == 0,
)
check(
    "A3: eq (54) lambda = i n from e^{lambda(theta+2pi)} = e^{lambda theta}",
    sp.simplify(sp.exp(sp.I * 3 * 2 * sp.pi) - 1) == 0,
)

# ---------------------------------------------------------------- A4: S^2 sigma coordinates
p1, p2, rad = sp.symbols("p1 p2 rad", positive=True)
zz = sp.sqrt(rad**2 - p1**2 - p2**2)
emb = sp.Matrix([p1, p2, zz])
J = emb.jacobian([p1, p2])
gind = sp.simplify(J.T * J)
g60 = sp.Matrix(
    2, 2, lambda a, b: (1 if a == b else 0) + [p1, p2][a] * [p1, p2][b] / (rad**2 - p1**2 - p2**2)
)
check("A4: eq (60) = metric induced by the embedding (59)", sp.simplify(gind - g60) == sp.zeros(2))
t1, t2, t3 = sp.symbols("t1 t2 t3")
d1 = -t2 * zz + t3 * p2  # eq (62) first-order change of pi^1
d2 = t1 * zz - t3 * p1  # eq (63)
check(
    "A4: eqs (62)-(63) keep the point on the sphere: delta z of the full rotation equals -(p . delta p)/z",
    sp.simplify(
        (-sp.Matrix([t1, t2, t3]).cross(sp.Matrix([p1, p2, zz])))[2] + (p1 * d1 + p2 * d2) / zz
    )
    == 0,
)
# rotation by -theta about axis theta: delta x = -theta x x
xv = sp.Matrix([p1, p2, zz])
th_v = sp.Matrix([t1, t2, t3])
dx = -th_v.cross(xv)
check(
    "A4: eqs (62)-(63) = delta x = -(theta x x) projected on (p1,p2) (rotation by -theta)",
    sp.simplify(dx[0] - d1) == 0 and sp.simplify(dx[1] - d2) == 0,
)
# Killing check for the fields in (62)-(63)
K = [sp.Matrix([0, zz]), sp.Matrix([-zz, 0]), sp.Matrix([p2, -p1])]  # coefficients of t1, t2, t3
vars2 = [p1, p2]


def lie_metric(Xv, G, vs):
    n = len(vs)
    out = sp.zeros(n)
    for a_ in range(n):
        for b_ in range(n):
            out[a_, b_] = sum(
                Xv[c] * sp.diff(G[a_, b_], vs[c])
                + G[c, b_] * sp.diff(Xv[c], vs[a_])
                + G[a_, c] * sp.diff(Xv[c], vs[b_])
                for c in range(n)
            )
    return sp.simplify(out)


check(
    "A4: the three fields of (62)-(63) are Killing for the metric (60)",
    all(lie_metric(Kv, g60, vars2) == sp.zeros(2) for Kv in K),
)
# decompactification limit: K / rad terms
lim_ok = sp.limit(zz / rad, rad, sp.oo) == 1
check(
    "A4: z/r -> 1 as r -> infinity, so (62)-(63) -> (65)-(68) (arc-length translations l = theta r plus the rotation t3)",
    lim_ok,
)
check(
    "A4: g_ab -> delta_ab as r -> infinity (eq 64)",
    sp.limit(g60[0, 1], rad, sp.oo) == 0 and sp.limit(g60[0, 0], rad, sp.oo) == 1,
)

# ---------------------------------------------------------------- A5: S^3 sigma model, so(4) closure
q = sp.symbols("q1 q2 q3", real=True)
rr3 = sp.Symbol("rr3", positive=True)
z3 = sp.sqrt(rr3**2 - sum(v**2 for v in q))
P = [sp.Matrix([z3 if i == a else 0 for i in range(3)]) for a in range(3)]


def Mab(a, b):
    return sp.Matrix([q[a] if i == b else (-q[b] if i == a else 0) for i in range(3)])


Ms = {(a, b): Mab(a, b) for a, b in [(0, 1), (0, 2), (1, 2)]}


def bracket(U_, V_):
    return sp.simplify(
        sp.Matrix(
            [
                sum(U_[c] * sp.diff(V_[i], q[c]) - V_[c] * sp.diff(U_[i], q[c]) for c in range(3))
                for i in range(3)
            ]
        )
    )


g3 = sp.Matrix(
    3, 3, lambda a, b: (1 if a == b else 0) + q[a] * q[b] / (rr3**2 - sum(v**2 for v in q))
)
J3 = sp.Matrix([list(q) + [z3]]).T.jacobian(q)
check(
    "A5: S^3 sigma metric = induced metric of the embedding (q, z) in R^4",
    sp.simplify(J3.T * J3 - g3) == sp.zeros(3),
)
allf = list(P) + list(Ms.values())
check(
    "A5: all six fields P_a, M_ab are Killing for the S^3 sigma metric",
    all(lie_metric(F, g3, q) == sp.zeros(3) for F in allf),
)
ok_pp = all(
    sp.simplify(bracket(P[a], P[b]) + Mab(a, b)) == sp.zeros(3, 1)
    for a, b in [(0, 1), (0, 2), (1, 2)]
)
check("A5: [P_a, P_b] = -M_ab (so(4) structure, broken-broken -> unbroken)", ok_pp)
expect_caught(
    "A5 control: [P_a, P_b] = +M_ab",
    all(
        sp.simplify(bracket(P[a], P[b]) - Mab(a, b)) == sp.zeros(3, 1)
        for a, b in [(0, 1), (0, 2), (1, 2)]
    ),
)
# closure of [M, P] into P
ok_mp = True
for (a, b), Mv in Ms.items():
    for c in range(3):
        br = bracket(Mv, P[c])
        cand = sp.zeros(3, 1)
        for d_ in range(3):
            coef = (1 if (b == c and d_ == a) else 0) - (1 if (a == c and d_ == b) else 0)
            cand += coef * P[d_]
        ok_mp = ok_mp and sp.simplify(br - cand) == sp.zeros(3, 1)
check("A5: [M_ab, P_c] = delta_bc P_a - delta_ac P_b (P_a transform as a vector of so(3))", ok_mp)
# contraction
cont = True
for a, b in [(0, 1), (0, 2), (1, 2)]:
    br = sp.simplify(bracket(P[a] / rr3, P[b] / rr3) + Mab(a, b) / rr3**2)
    cont = cont and br == sp.zeros(3, 1) and sp.limit(Mab(a, b)[0] / rr3**2, rr3, sp.oo) == 0
check(
    "A5: [P_a/r, P_b/r] = -M_ab/r^2 -> 0 as r -> infinity: the translations commute in the decompactification limit",
    cont,
)
metric_wrong = sp.Matrix(
    3, 3, lambda a, b: (1 if a == b else 0) - q[a] * q[b] / (rr3**2 - sum(v**2 for v in q))
)
expect_caught(
    "A5 control: sign-flipped metric is Killing",
    all(lie_metric(F, metric_wrong, q) == sp.zeros(3) for F in P),
)


# ---------------------------------------------------------------- A6: counting rule
def so_basis(n):
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            Mx = sp.zeros(n)
            Mx[i, j], Mx[j, i] = 1, -1
            out.append(Mx)
    return out


def extra_commuting(N2):
    dim = N2 + 1
    basis = so_basis(dim)
    cartan = []
    for k in range(N2 // 2):
        Mx = sp.zeros(dim)
        Mx[2 * k, 2 * k + 1], Mx[2 * k + 1, 2 * k] = 1, -1
        cartan.append(Mx)
    if not cartan:
        return len(basis) if dim == 2 else None, 0
    rows = []
    for C in cartan:
        cols = [(B * C - C * B).reshape(dim * dim, 1) for B in basis]
        rows.append(sp.Matrix.hstack(*cols))
    ns = sp.Matrix.vstack(*rows).nullspace()
    return len(ns), N2 // 2


res = {}
for N2 in range(1, 9):
    if N2 == 1:
        cdim, rk = 1, 0  # so(2) is abelian of dim 1, Cartan of so(1) is empty
    else:
        cdim, rk = extra_commuting(N2)
    res[N2] = cdim - rk
check(
    f"A6: extra commuting generators for N2 = 1..8: {res} = [1,0,1,0,1,0,1,0]",
    [res[n] for n in range(1, 9)] == [1, 0, 1, 0, 1, 0, 1, 0],
)
expect_caught("A6 control: claim an extra commuting generator at N2 = 2", res[2] == 1)

# ---------------------------------------------------------------- A7: N2 = 3
a_, b_, c_, d_ = sp.symbols("a b c d", real=True)
U4 = [a_, b_, c_, d_]
I2 = sp.eye(2)
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
SIG = [s1, s2, s3]
T = [-sp.I * s / 2 for s in SIG]


def gmat(u):
    return u[0] * I2 + sp.I * (u[3] * s1 - u[2] * s2 + u[1] * s3)


def coords(M):
    return sp.Matrix(
        [
            sp.simplify(M.trace() / 2),
            sp.simplify((M * s3).trace() / (2 * sp.I)),
            sp.simplify(-(M * s2).trace() / (2 * sp.I)),
            sp.simplify((M * s1).trace() / (2 * sp.I)),
        ]
    )


E4 = [sp.Matrix([1 if i == j else 0 for i in range(4)]) for j in range(4)]
AL = [sp.Matrix.hstack(*[coords(T[k] * gmat(E4[j])) for j in range(4)]) for k in range(3)]
AR = [sp.Matrix.hstack(*[coords(gmat(E4[j]) * T[k]) for j in range(4)]) for k in range(3)]
U4v = sp.Matrix(U4)
for nm, Mx in (("L3 - R3", AL[2] - AR[2]), ("L3 + R3", AL[2] + AR[2])):
    print("   ", nm, "=", Mx.tolist(), " rank", Mx.rank())
check(
    "A7: A_L3 - A_R3 and A_L3 + A_R3 are antisymmetric rank-2 (each a rotation in ONE plane of R^4)",
    all(Mx.T == -Mx and Mx.rank() == 2 for Mx in (AL[2] - AR[2], AL[2] + AR[2])),
)
check(
    "A7: so(4) = su(2)_L + su(2)_R: L and R commute, relations close",
    all(
        sp.simplify(AL[i] * AR[j] - AR[j] * AL[i]) == sp.zeros(4)
        for i in range(3)
        for j in range(3)
    ),
)


def Xop(k, f_):
    w = AL[k] * U4v
    return sp.expand(-sum(w[i] * sp.diff(f_, U4[i]) for i in range(4)))


def Yop(k, f_):
    w = AR[k] * U4v
    return sp.expand(sum(w[i] * sp.diff(f_, U4[i]) for i in range(4)))


def monomials(n):
    out = []
    for i in range(n + 1):
        for j in range(n + 1 - i):
            for k in range(n + 1 - i - j):
                out.append(a_**i * b_**j * c_**k * d_ ** (n - i - j - k))
    return out


def vec(f_, mons):
    Pp = sp.Poly(f_, *U4)
    return sp.Matrix([Pp.coeff_monomial(m) for m in mons])


def harmonic_basis(n):
    mons = monomials(n)
    if n < 2:
        return mons, sp.eye(len(mons))
    lm = monomials(n - 2)
    Lm = sp.Matrix.hstack(*[vec(sum(sp.diff(m, v, 2) for v in U4), lm) for m in mons])
    return mons, sp.Matrix.hstack(*Lm.nullspace())


for n in (1, 2, 3):
    mons, H = harmonic_basis(n)
    x3m = sp.Matrix.hstack(*[vec(Xop(2, m), mons) for m in mons])
    y3m = sp.Matrix.hstack(*[vec(Yop(2, m), mons) for m in mons])
    HtH = (H.T * H).inv()
    X3 = sp.simplify(HtH * H.T * x3m * H)
    Y3 = sp.simplify(HtH * H.T * y3m * H)
    comm = sp.simplify(X3 * Y3 - Y3 * X3) == sp.zeros(H.cols)
    # joint eigenvalues of (i X3, i Y3): use X3 + 3 Y3-like generic combination to separate, then read both
    gen = sp.I * X3 + sp.pi * sp.I * Y3
    ev = gen.eigenvals()
    s = R(n, 2)
    expected = {}
    for mL in [R(2 * k - n, 2) for k in range(n + 1)]:
        for mR in [R(2 * k - n, 2) for k in range(n + 1)]:
            val = sp.nsimplify(mL + sp.pi * mR)
            expected[val] = expected.get(val, 0) + 1
    got = {sp.simplify(k): v for k, v in ev.items()}
    exp_s = {sp.simplify(k): v for k, v in expected.items()}
    # eigenvalue signs may be mirrored (-m); compare as multisets symmetric under overall sign
    neg = {sp.simplify(-k): v for k, v in exp_s.items()}
    check(
        f"A7: degree {n}: iX3, iY3 commute and their joint spectrum is all pairs (m_L, m_R) in {{-s..s}}^2, s = {s}, each once ({(n + 1) ** 2} states)",
        comm and (got == exp_s or got == neg) and H.cols == (n + 1) ** 2,
    )

print("\nFAILS:", FAILS if FAILS else "none")
sys.exit(1 if FAILS else 0)
