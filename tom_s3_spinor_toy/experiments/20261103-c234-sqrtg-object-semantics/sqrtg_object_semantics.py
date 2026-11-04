"""C234: what can 'sqrt|g| expanded in S^3 harmonics' mean? Coordinate dependence of the density and the scalar volume ratio.

Objects, all on the unit S^3 in R^4 with embedding x = (x1,x2,x3,x4):
  Hopf coordinates (eta, a, b): x = (cos eta cos a, cos eta sin a, sin eta cos b, sin eta sin b),  0 < eta < pi/2
  stereographic coordinates (u1,u2,u3):  x = (2u, r^2 - 1)/(r^2 + 1),  r^2 = |u|^2   (projection from the pole x4 = +1)
sqrt(det g) is computed from the pull-back metric of the embedding at a point (J^T J with the exact Jacobian), not from a formula.
Everything is evaluated at REGULAR points of both coordinate systems (the Hopf coordinates are singular at eta = 0, pi/2).

Predictions written BEFORE running:
  O1. Round metric: sqrt(g) in Hopf coordinates is sin(eta)cos(eta); in stereographic coordinates it is (2/(1+r^2))^3.
      At the same point of S^3 the two values differ (P1 = (1/2,1/2,1/2,1/2): 1/2 versus 1/8; P2 = (1/2,1/2,1/2,-1/2): 1/2 versus 27/8;
      P3 = (1/3,2/3,2/3,0): 2 sqrt(5)/9 versus 1). So sqrt(g) as a function of the point depends on the coordinates: a scalar DENSITY.
  O2. The ratio rho = sqrt(det g_deformed) / sqrt(det g_round), both in the SAME coordinates, takes the same value at the same point in
      both coordinate systems: a scalar function on S^3. g = exp(2 e x4) g_round gives rho = exp(3 e x4);
      g = g_round + e dx4 (x) dx4 gives rho = sqrt(1 + e (1 - x4^2)).
  O3. To first order rho = 1 + (1/2) tr_{g_round} h; for h = 2 e x4 g_round this is 1 + 3 e x4: the first-order volume change sits in
      the degree-1 harmonic x4, a member of the (1/2,1/2) multiplet.
Self-controls: claiming that sqrt(g) alone agrees across the coordinate systems must be caught; wrong closed forms for rho must be caught.
"""

import sys

import sympy as sp

eta, a, b = sp.symbols("eta a b", real=True)
u1, u2, u3 = sp.symbols("u1 u2 u3", real=True)
e = sp.Symbol("e", positive=True)
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


X_hopf = sp.Matrix(
    [
        sp.cos(eta) * sp.cos(a),
        sp.cos(eta) * sp.sin(a),
        sp.sin(eta) * sp.cos(b),
        sp.sin(eta) * sp.sin(b),
    ]
)
r2 = u1**2 + u2**2 + u3**2
X_st = sp.Matrix([2 * u1, 2 * u2, 2 * u3, r2 - 1]) / (r2 + 1)
J_H = X_hopf.jacobian((eta, a, b))
J_S = X_st.jacobian((u1, u2, u3))

# (name, Hopf coordinates, stereographic coordinates, point in R^4)
POINTS = [
    (
        "P1 (1/2,1/2,1/2,1/2)",
        {eta: sp.pi / 4, a: sp.pi / 4, b: sp.pi / 4},
        {u1: 1, u2: 1, u3: 1},
        sp.Matrix([R(1, 2)] * 4),
    ),
    (
        "P2 (1/2,1/2,1/2,-1/2)",
        {eta: sp.pi / 4, a: sp.pi / 4, b: -sp.pi / 4},
        {u1: R(1, 3), u2: R(1, 3), u3: R(1, 3)},
        sp.Matrix([R(1, 2), R(1, 2), R(1, 2), -R(1, 2)]),
    ),
    (
        "P3 (1/3,2/3,2/3,0)",
        {eta: sp.asin(R(2, 3)), a: sp.atan2(R(2, 3), R(1, 3)), b: 0},
        {u1: R(1, 3), u2: R(2, 3), u3: R(2, 3)},
        sp.Matrix([R(1, 3), R(2, 3), R(2, 3), 0]),
    ),
]
CLOSED_H = sp.sin(eta) * sp.cos(eta)
CLOSED_S = (2 / (1 + r2)) ** 3


def zero(expr):
    if isinstance(expr, sp.MatrixBase):
        return all(zero(c) for c in expr)
    return sp.simplify(sp.expand(sp.sympify(expr))) == 0



def metric_at(J, sub):
    Jn = J.subs(sub)
    return sp.simplify(Jn.T * Jn), Jn


def rho_values(pt, kind):
    name, hs, ss, xp = pt
    gH, JH = metric_at(J_H, hs)
    gS, JS = metric_at(J_S, ss)
    out = {}
    for tag, g, Jn, X in (("H", gH, JH, X_hopf.subs(hs)), ("S", gS, JS, X_st.subs(ss))):
        x4 = sp.simplify(X[3])
        if kind == "round":
            gd = g
        elif kind == "conf":
            gd = g * sp.exp(2 * e * x4)
        else:  # g + e dx4 (x) dx4 : dx4 as the covector (d x4 / d coordinate) at the point
            grad = (
                sp.Matrix([sp.diff(X_hopf[3], v).subs(hs) for v in (eta, a, b)])
                if tag == "H"
                else sp.Matrix([sp.diff(X_st[3], v).subs(ss) for v in (u1, u2, u3)])
            )
            gd = g + e * grad * grad.T
        out[tag] = (sp.sqrt(sp.simplify(gd.det())), x4)
    return out


# ---- O1
for pt in POINTS:
    name, hs, ss, xp = pt
    check(
        f"{name}: both coordinate values describe the same point of R^4",
        zero(X_hopf.subs(hs) - xp) and zero(X_st.subs(ss) - xp),
    )
    v = rho_values(pt, "round")
    sh, ss_ = sp.simplify(v["H"][0]), sp.simplify(v["S"][0])
    check(
        f"{name}: sqrt(g) from J^T J equals sin(eta)cos(eta) in Hopf and (2/(1+r^2))^3 in stereographic",
        zero(sh - CLOSED_H.subs(hs)) and zero(ss_ - CLOSED_S.subs(ss)),
    )
    check(
        f"{name}: the two values of sqrt(g) at the same point are different numbers ({sp.nsimplify(sh)} versus {sp.nsimplify(ss_)})",
        not zero(sh - ss_),
    )

# ---- O2
for pt in POINTS:
    name, hs, ss, xp = pt
    base = rho_values(pt, "round")
    for kind, closed in (
        ("conf", lambda x4: sp.exp(3 * e * x4)),
        ("aniso", lambda x4: sp.sqrt(1 + e * (1 - x4**2))),
    ):
        dv = rho_values(pt, kind)
        rhoH = sp.simplify(dv["H"][0] / base["H"][0])
        rhoS = sp.simplify(dv["S"][0] / base["S"][0])
        x4 = sp.simplify(xp[3])
        check(f"{name}, {kind}: rho is the same in both coordinate systems", zero(rhoH - rhoS))
        check(f"{name}, {kind}: rho equals the closed form at x4 = {x4}", zero(rhoH - closed(x4)))

# ---- O3 (first order, pointwise)
for pt in POINTS:
    name, hs, ss, xp = pt
    x4 = xp[3]
    g, _ = metric_at(J_H, pt[1])
    h = 2 * e * x4 * g
    half_tr = sp.simplify((g.inv() * h).trace() / 2)
    rho1 = sp.series(sp.exp(3 * e * x4), e, 0, 2).removeO()
    check(
        f"{name}: (1/2) tr h = 3 e x4 and rho = 1 + 3 e x4 + O(e^2) for the conformal deformation",
        zero(half_tr - 3 * e * x4) and zero(rho1 - (1 + 3 * e * x4)),
    )

# ---- self-controls
P1 = POINTS[0]
v1 = rho_values(P1, "round")
expect_caught(
    "sqrt(g) alone agrees across Hopf and stereographic coordinates at P1",
    zero(v1["H"][0] - v1["S"][0]),
)
dv = rho_values(P1, "conf")
rho_wrong = sp.simplify(dv["H"][0] / v1["H"][0])
expect_caught(
    "wrong closed form rho = exp(2 e x4) for the conformal deformation at P1",
    zero(rho_wrong - sp.exp(2 * e * R(1, 2))),
)
dva = rho_values(P1, "aniso")
rho_a = sp.simplify(dva["H"][0] / v1["H"][0])
expect_caught(
    "wrong closed form rho = sqrt(1 + e x4^2) for g_round + e dx4 dx4 at P1",
    zero(rho_a - sp.sqrt(1 + e * R(1, 4))),
)

print("\nFAILS:", FAILS if FAILS else "none")
sys.exit(1 if FAILS else 0)
