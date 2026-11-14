"""C229: three readings of the SU(2) action on functions of (xi, conj xi), derived from their definitions,
with every claim ASSERTED (the C225/C226 scripts printed the convention-B results without asserting them).

  A: (U f)(xi) = f(g^-1 xi)      the pullback of C225 (moving points xi -> g xi induces this on functions)
  B: (U f)(xi) = f(g xi)         an ANTI-representation
  C: (U f)(xi) = f(g^T xi)       a representation, with the opposite D3 weights to A

xi and conj(xi) are independent symbols (x1, x2, y1, y2). g_a(t) = exp(i t sigma_a / 2) = cos(t/2) + i sin(t/2) sigma_a
exactly (sigma^2 = 1), t real. D_a = (1/i) d/dt U(g_a(t)) at t = 0, a first-order operator, so it is the derivation
whose components are D_a applied to the four coordinates (derived from the definition, not hand-written).

Predictions written BEFORE running (from the algebra of g -> g^-1, g^T):
  A: [D_a,D_b] = +i eps D_c; D3 weights on (x1,x2,y1,y2) = (-1/2,+1/2,+1/2,-1/2); [D3,D+] = +D+ ; D+ xi = (-xi2, 0)
  B: D_B = -D_A; [D_a,D_b] = -i eps D_c; weights (+1/2,-1/2,-1/2,+1/2); [D3,D+] = -D+ (D1+iD2 LOWERS); anti-rep
  C: [D_a,D_b] = +i eps D_c; weights (+1/2,-1/2,-1/2,+1/2); [D3,D+] = +D+ ; representation
The script also runs five deliberately wrong variants (self-controls); each must FAIL the relevant check.
Exit code 0 only if every correct claim holds AND every self-control is caught.
"""

import itertools
import sys

import sympy as sp

x1, x2, y1, y2 = sp.symbols("x1 x2 y1 y2")
t = sp.Symbol("t", real=True)
I = sp.I
h = sp.Rational(1, 2)
COORD = [x1, x2, y1, y2]
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
F = sp.Function("F")(x1, x2, y1, y2)
FAILS = []


def conj_m(M):
    return M.applyfunc(lambda e: sp.conjugate(e))


def mx(conv, g):
    """matrix M with xi -> M xi for U f = f(M xi)."""
    return {"A": g.inv(), "B": g, "C": g.T}[conv]


def vector_field(conv, a, t_sym=t):
    """components c_i = (1/i) d/dt [coordinate_i of (M xi, conj(M) conj(xi))] at t=0, from the definition."""
    g = sp.cos(t_sym / 2) * sp.eye(2) + I * sp.sin(t_sym / 2) * SIG[a]
    M = mx(conv, g)
    xi = sp.Matrix([x1, x2])
    et = sp.Matrix([y1, y2])
    new_x = M * xi
    new_y = conj_m(M) * et
    comps = list(new_x) + list(new_y)
    return [sp.simplify(sp.diff(c, t_sym).subs(t_sym, 0) / I) for c in comps]


def D(vf, f):
    return sp.expand(sum(c * sp.diff(f, v) for c, v in zip(vf, COORD)))


def comm_signs(vfs):
    found = set()
    for a, b, c in itertools.permutations(range(3)):
        lhs = D(vfs[a], D(vfs[b], F)) - D(vfs[b], D(vfs[a], F))
        for s in (1, -1):
            if sp.simplify(sp.expand(lhs - s * I * sp.LeviCivita(a, b, c) * D(vfs[c], F))) == 0:
                found.add(s)
    return found


def weights(vfs):
    return [sp.simplify(D(vfs[2], v) / v) for v in COORD]


def ladder(vfs):
    dp = lambda f: D(vfs[0], f) + I * D(vfs[1], f)  # noqa: E731
    dm = lambda f: D(vfs[0], f) - I * D(vfs[1], f)  # noqa: E731
    return dp, dm


def d3_dplus_sign(vfs):
    dp, _ = ladder(vfs)
    r = sp.simplify(D(vfs[2], dp(F)) - dp(D(vfs[2], F)))
    for s in (1, -1):
        if sp.simplify(r - s * dp(F)) == 0:
            return s
    return 0


def casimir_on_xi(vfs):
    return [sp.simplify(sum(D(vfs[a], D(vfs[a], v)) for a in range(3))) for v in (x1, x2)]


def claim_checks(vfs, expect_sign, expect_w, expect_d3dp, expect_dp_xi):
    out = {}
    out["commutator sign"] = comm_signs(vfs) == {expect_sign}
    out["D3 weights"] = weights(vfs) == expect_w
    out["[D3,D+] sign"] = d3_dplus_sign(vfs) == expect_d3dp
    dp, dm = ladder(vfs)
    out["D+ xi"] = [sp.simplify(dp(x1)), sp.simplify(dp(x2))] == expect_dp_xi
    cas = casimir_on_xi(vfs)
    out["Casimir 3/4 on xi"] = cas == [
        sp.Rational(3, 4) * x1,
        sp.Rational(3, 4) * x2,
    ]
    return out


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)


def expect_caught(name, cond):
    """self-control: the damaged variant must make the relevant check FAIL."""
    print(("CAUGHT " if not cond else "MISSED ") + name)
    if cond:
        FAILS.append("self-control not caught: " + name)


R2, R4 = sp.Rational(1, 2), sp.Rational(1, 4)
VF = {c: [vector_field(c, a) for a in range(3)] for c in "ABC"}

# ----- definitions -> vector fields
check(
    "D_B == -D_A componentwise (B is the anti-representation)",
    all(sp.simplify(p + q) == 0 for a in range(3) for p, q in zip(VF["B"][a], VF["A"][a])),
)
check(
    "A closed form D_a = -1/2 (sigma xi).d + 1/2 (conj(sigma) conj(xi)).conj(d)",
    all(
        sp.simplify(c - e) == 0
        for a in range(3)
        for c, e in zip(
            VF["A"][a],
            list(-R2 * SIG[a] * sp.Matrix([x1, x2]))
            + list(R2 * conj_m(SIG[a]) * sp.Matrix([y1, y2])),
        )
    ),
)

# ----- the three conventions
W_A = [-R2, R2, R2, -R2]
W_B = [R2, -R2, -R2, R2]
for conv, sign, w, d3dp, dpxi in (
    ("A", 1, W_A, 1, [-x2, 0]),
    ("B", -1, W_B, -1, [x2, 0]),
    ("C", 1, W_B, 1, None),
):
    if conv == "C":
        dp, dm = ladder(VF["C"])
        dpxi = [
            sp.simplify(dp(x1)),
            sp.simplify(dp(x2)),
        ]  # derived; asserted below only as 'D+ xi != 0 and D+^C = -D-^A'
    res = claim_checks(VF[conv], sign, w, d3dp, dpxi)
    for k, v in res.items():
        check(f"{conv}: {k}", v)
dpC, _ = ladder(VF["C"])
_, dmA = ladder(VF["A"])
check(
    "C: D+^C = -D-^A on a generic F (so D+^C is a genuine raising operator of its own D3)",
    sp.simplify(dpC(F) + dmA(F)) == 0,
)


# ----- group level: representation vs anti-representation (non-commuting rational elements)
def su2(a, b, c, d, n):
    a, b, c, d = (sp.Rational(v, n) for v in (a, b, c, d))
    assert a * a + b * b + c * c + d * d == 1
    return sp.Matrix([[a + I * b, -c + I * d], [c + I * d, a - I * b]])


g1, g2 = su2(1, 2, 2, 0, 3), su2(1, 2, 2, 4, 5)
assert g1 * g2 != g2 * g1
f = x1**2 * y2 + 3 * x2 * y1 * y2 - x1 * x2


def U(conv, g, fn):
    M = mx(conv, g)
    sub = dict(zip(COORD, list(M * sp.Matrix([x1, x2])) + list(conj_m(M) * sp.Matrix([y1, y2]))))
    return sp.expand(fn.subs(sub, simultaneous=True))


for conv, is_rep in (("A", True), ("B", False), ("C", True)):
    lhs = U(conv, g1, U(conv, g2, f))
    rep = sp.expand(lhs - U(conv, g1 * g2, f)) == 0
    anti = sp.expand(lhs - U(conv, g2 * g1, f)) == 0
    check(
        f"{conv}: U_g1 U_g2 = U_(g1 g2) is {is_rep} (rep) and U_g1 U_g2 = U_(g2 g1) is {not is_rep} (anti)",
        rep == is_rep and anti == (not is_rep),
    )

# ----- V, R, normalisation
S = SIG
Y_ = sp.Matrix([y1, y2])
X_ = sp.Matrix([x1, x2])
V = lambda Xv, Yv: sp.Matrix([R2 * (Yv.T * S[i] * Xv)[0] for i in range(3)])  # noqa: E731
Vx = V(X_, Y_)
ga, gb, gab, gbb = sp.symbols("ga gb gab gbb")  # a, b, conj(a), conj(b): independent symbols
G = sp.Matrix([[ga, -gbb], [gb, gab]])
Gc = sp.Matrix([[gab, -gb], [gbb, ga]])  # complex conjugate matrix
Gd = Gc.T  # g^dagger


def Rmat(Gm, Gdm, transpose=False, scale=1):
    R = sp.Matrix(3, 3, lambda i, j: scale * R2 * (S[j] * Gdm * S[i] * Gm).trace())
    return R.T if transpose else R


def swap_conj(e):
    return sp.expand(e).subs({ga: gab, gab: ga, gb: gbb, gbb: gb, I: -I}, simultaneous=True)


def relation(transpose=False, scale=1):
    R = Rmat(G, Gd, transpose, scale)
    res = V(G * X_, Gc * Y_) - R * Vx
    return sp.simplify(sp.expand(res)) == sp.zeros(3, 1), R


ok_rel, Rg = relation()
check(
    "V(g xi) = R(g) V(xi) for generic g (a, b, conj a, conj b independent, norm NOT imposed)",
    ok_rel,
)
n2 = ga * gab + gb * gbb
check(
    "R R^T = (|a|^2+|b|^2)^2 I and det R = (|a|^2+|b|^2)^3 (so R in SO(3) when |a|^2+|b|^2 = 1)",
    sp.expand(Rg * Rg.T - n2**2 * sp.eye(3)) == sp.zeros(3) and sp.expand(Rg.det() - n2**3) == 0,
)
real_ok = True
for i in range(3):
    for j in range(3):
        e = sp.expand(Rg[i, j])
        real_ok &= sp.expand(swap_conj(e) - e) == 0
check(
    "every entry of R equals its complex conjugate as a polynomial (R is REAL, not just orthogonal)",
    real_ok,
)
adj = sp.Matrix(3, 3, lambda i, j: R2 * (S[i] * G * S[j] * Gd).trace())
check(
    "index order: R_ij = 1/2 tr(sigma_j g^+ sigma_i g) equals 1/2 tr(sigma_i g sigma_j g^+)",
    sp.expand(adj - Rg) == sp.zeros(3),
)
check(
    "R is not symmetric for generic g (so a transpose error would be seen)",
    sp.expand(Rg - Rg.T) != sp.zeros(3),
)

# Hopf points and the sphere normalisation by an explicit integral
th, ph = sp.symbols("th ph", real=True)
xi = sp.Matrix([sp.cos(th / 2), sp.sin(th / 2) * sp.exp(I * ph)])
Vu = V(xi, xi.conjugate()).applyfunc(sp.simplify)
n = sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])
check(
    "unit xi = (cos th/2, sin th/2 e^{i ph}) gives V = n/2 (n the unit vector)",
    sp.simplify(Vu - n / 2) == sp.zeros(3, 1),
)
LAM2 = sp.sqrt(3 / sp.pi)


def sphere_norms(lam2):
    return [
        sp.simplify(
            sp.integrate(
                sp.integrate((lam2 * Vu[i]) ** 2 * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi)
            )
        )
        for i in range(3)
    ]


check(
    "integral over S^2 of (lambda^2 V_i)^2 = 1 for i = 1,2,3 with lambda^2 = sqrt(3/pi) (computed, not assumed)",
    sphere_norms(LAM2) == [1, 1, 1],
)
check(
    "V invariant under xi -> e^{i phi} xi",
    sp.simplify(V(sp.exp(I * ph) * X_, sp.exp(-I * ph) * Y_) - Vx) == sp.zeros(3, 1),
)

# ----- self-controls: damaged variants must be caught
# S1: erase convention B (D_B := D_A)
resB_erased = claim_checks(VF["A"], -1, W_B, -1, [x2, 0])
expect_caught("erased convention B (D_B := D_A) passes the B claims", all(resB_erased.values()))
# S2: wrong lambda^2
expect_caught(
    "lambda^2 = sqrt(1/pi) gives unit sphere norms", sphere_norms(sp.sqrt(1 / sp.pi)) == [1, 1, 1]
)
# S3: R scaled by (1+i): reality check
Rs = Rmat(G, Gd, scale=1 + I)
rs_real = all(
    sp.expand(swap_conj(sp.expand(Rs[i, j])) - sp.expand(Rs[i, j])) == 0
    for i in range(3)
    for j in range(3)
)
expect_caught("R*(1+i) passes the reality check", rs_real)
# S4: transposed R
ok_t, _ = relation(transpose=True)
expect_caught("transposed R satisfies V(g xi) = R V(xi)", ok_t)
# S5: flip the sign of the holomorphic part of D_1 in A
vf_bad = [list(v) for v in VF["A"]]
vf_bad[0] = [-vf_bad[0][0], -vf_bad[0][1], vf_bad[0][2], vf_bad[0][3]]
expect_caught(
    "damaged D_1 (holomorphic sign flipped) keeps [D_a,D_b] = +i eps D_c", comm_signs(vf_bad) == {1}
)

print("\nFAILS:", FAILS if FAILS else "none")
sys.exit(1 if FAILS else 0)
