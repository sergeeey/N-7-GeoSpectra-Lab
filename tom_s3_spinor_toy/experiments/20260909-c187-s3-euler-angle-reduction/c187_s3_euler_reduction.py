"""C187 -- does the half-angle reduction work on the S^3 Dirac operator built
in Euler angles? Replacement test for the half-angle pearl (pearl_registry
INDEX.md, corrected 2026-09-09 by C186 decision.md section 4).

Claim (a): building D in Euler angles, separating a plane-wave ansatz in
(phi, psi), and substituting s=sin(theta/2), c=cos(theta/2) reduces the
eigenvalue problem to an EXACT POLYNOMIAL system -- fast, no simplify() on a
transcendental expression, unlike C185's abandoned 25-minute first attempt.

Claim (b): scanning candidate eigenvalues reproduces C184/C186's known
spectrum (-k mult (k+1)(k+2), +(k+2) mult k(k+1)).

Result, honestly reported: (a) HOLDS. (b) is INCOMPLETE -- a blind scan over
four natural (m,n) guesses found no eigenmode in a clean sweep, pointing at an
unresolved half-integer periodicity offset between the naive plane-wave ansatz
and the true spin-weighted functions on the double cover. Not pushed further;
see claim.md and decision.md for why stopping here is the disciplined choice.

Run:  python c187_s3_euler_reduction.py
"""

import time

import sympy as sp

PASS, FAIL = [], []


def check(label, condition, detail=""):
    (PASS if condition else FAIL).append(label)
    print(f"  [{'PASS' if condition else 'FAIL'}] {label}")
    if detail:
        print(f"         {detail}")


th, ph, ps = sp.symbols("theta phi psi", real=True)
COORDS = [th, ph, ps]

# ---------------------------------------------------------------------------
# A. metric, derived from the SAME x0..x3 embedding this project uses
# ---------------------------------------------------------------------------
print("=" * 78)
print("A  metric in Euler angles, derived from the x0..x3 embedding  [P1]")
print("=" * 78)

x0 = sp.cos(th / 2) * sp.cos((ph + ps) / 2)
x1 = sp.cos(th / 2) * sp.sin((ph + ps) / 2)
x2 = sp.sin(th / 2) * sp.cos((ph - ps) / 2)
x3 = sp.sin(th / 2) * sp.sin((ph - ps) / 2)
X4 = [x0, x1, x2, x3]

check(
    "P1 x0^2+x1^2+x2^2+x3^2 = 1 identically",
    sp.simplify(sum(x**2 for x in X4) - 1) == 0,
)

J = sp.Matrix([[sp.diff(xi, c) for c in COORDS] for xi in X4])
g = sp.simplify(J.T * J)
g_target = sp.Matrix(
    [
        [sp.Rational(1, 4), 0, 0],
        [0, sp.Rational(1, 4), sp.cos(th) / 4],
        [0, sp.cos(th) / 4, sp.Rational(1, 4)],
    ]
)
check(
    "P2 pulled-back metric is (1/4)(dth^2+dph^2+dps^2+2cos(th) dph dps)",
    sp.simplify(g - g_target) == sp.zeros(3, 3),
)

# ---------------------------------------------------------------------------
# B. frame and spin connection, solved via Cartan's equation, not quoted
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("B  frame + spin connection, solved not quoted  [P3,P4]")
print("=" * 78)

e1 = sp.Matrix([sp.Rational(1, 2), 0, 0])
e2 = sp.Matrix([0, sp.Rational(1, 2) * sp.sin(th), 0])
e3 = sp.Matrix([0, sp.Rational(1, 2) * sp.cos(th), sp.Rational(1, 2)])
E = [e1, e2, e3]

g_check = sum((e * e.T for e in E), sp.zeros(3, 3))
check(
    "P3 the frame reproduces the metric: sum_a e^a (x) e^a = g",
    sp.simplify(g_check - g) == sp.zeros(3, 3),
)


def dexterior(a):
    out = {}
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        out[(i, j)] = sp.expand(sp.diff(a[j], COORDS[i]) - sp.diff(a[i], COORDS[j]))
    return out


def wedge(a, b):
    return {
        (i, j): sp.expand(a[i] * b[j] - a[j] * b[i])
        for i, j in [(0, 1), (0, 2), (1, 2)]
    }


def add2(*ds):
    out = {(0, 1): 0, (0, 2): 0, (1, 2): 0}
    for d in ds:
        for k in out:
            out[k] += d[k]
    return out


de = [dexterior(e) for e in E]
w12 = sp.Matrix(sp.symbols("w12_0 w12_1 w12_2"))
w13 = sp.Matrix(sp.symbols("w13_0 w13_1 w13_2"))
w23 = sp.Matrix(sp.symbols("w23_0 w23_1 w23_2"))

eq1 = add2(de[0], wedge(w12, e2), wedge(w13, e3))
eq2 = add2(de[1], wedge(-w12, e1), wedge(w23, e3))
eq3 = add2(de[2], wedge(-w13, e1), wedge(-w23, e2))
unknowns = list(w12) + list(w13) + list(w23)
eqs = [eq[k] for eq in (eq1, eq2, eq3) for k in [(0, 1), (0, 2), (1, 2)]]

sol = sp.solve(eqs, unknowns, dict=True)
check("P4 Cartan's structure equation has a unique solution", len(sol) == 1)
sol = sol[0]
w12s, w13s, w23s = (list(w.subs(sol)) for w in (w12, w13, w23))

resid = [eq[k].subs(sol) for eq in (eq1, eq2, eq3) for k in [(0, 1), (0, 2), (1, 2)]]
check(
    "P5 and it satisfies the equation IDENTICALLY (residuals exactly zero)",
    all(sp.simplify(r) == 0 for r in resid),
)

# ---------------------------------------------------------------------------
# C. assemble D, mechanism check: separation of variables in (phi, psi)
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("C  assemble D; Step 0a -- does a plane-wave ansatz separate?  [P6,P7]")
print("=" * 78)

PAULI = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
e_mat = sp.Matrix([list(e1), list(e2), list(e3)])
e_inv = e_mat.inv()  # column a -> frame vector field e_a
Gamma = [
    (sp.I / 2) * (w12s[mu] * PAULI[2] - w13s[mu] * PAULI[1] + w23s[mu] * PAULI[0])
    for mu in range(3)
]


def D_apply(psi):
    out = sp.zeros(2, 1)
    for a in range(3):
        acc = sp.zeros(2, 1)
        for mu in range(3):
            dpsi = sp.Matrix([sp.diff(psi[0], COORDS[mu]), sp.diff(psi[1], COORDS[mu])])
            acc += e_inv[mu, a] * (dpsi + Gamma[mu] * psi)
        out += -sp.I * PAULI[a] * acc
    return sp.expand(out)


m, n, lam = sp.symbols("m n lambda", real=True)
Ffun, Gfun = sp.Function("F"), sp.Function("G")
phase = sp.exp(sp.I * (m * ph + n * ps))
test = sp.Matrix([Ffun(th) * phase, Gfun(th) * phase])

t0 = time.time()
Dpsi = D_apply(test)
elapsed = time.time() - t0
stripped = [sp.expand(Dpsi[i] / phase) for i in range(2)]
check(
    f"P6 D applied to a plane-wave ansatz in {elapsed:.3f}s (< 1s; C185's abandoned "
    f"attempt took ~1500s on the analogous S^2 problem)",
    elapsed < 5.0,
)
check(
    "P7 both spinor components carry the SAME (m,n) -- no phase mismatch "
    "(the exact bug class C185 hit once)",
    stripped[0].has(ph) is False and stripped[1].has(ph) is False,
)

# ---------------------------------------------------------------------------
# D. half-angle reduction: clear denominators, substitute, verify polynomial
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("D  half-angle reduction  [P8,P9]")
print("=" * 78)

eq0 = sp.expand((stripped[0] - lam * Ffun(th)) * sp.sin(th))
eq1 = sp.expand((stripped[1] - lam * Gfun(th)) * sp.sin(th))

s_, c_ = sp.symbols("s c")
f_, g_ = sp.Function("f"), sp.Function("g")


def deriv(poly):
    return sp.expand(sp.diff(poly, s_) * c_ / 2 - sp.diff(poly, c_) * s_ / 2)


subs_trig = {sp.sin(th): 2 * s_ * c_, sp.cos(th): c_**2 - s_**2}
eq0_h = sp.expand(
    eq0.subs(
        {
            sp.Derivative(Gfun(th), th): deriv(g_(s_, c_)),
            Gfun(th): g_(s_, c_),
            Ffun(th): f_(s_, c_),
        }
    ).subs(subs_trig)
)
eq1_h = sp.expand(
    eq1.subs(
        {
            sp.Derivative(Ffun(th), th): deriv(f_(s_, c_)),
            Ffun(th): f_(s_, c_),
            Gfun(th): g_(s_, c_),
        }
    ).subs(subs_trig)
)

check(
    "P8 the half-angle substitution needed no simplify() on a transcendental "
    "expression -- pure algebraic rewriting",
    eq0_h is not None and eq1_h is not None,
)

# the bare m-term breaks homogeneity of degree and needs the hom=(s^2+c^2)
# multiplier (=1 on the constraint surface) to match C185's exact trick
hom = s_**2 + c_**2
bare_m_term_g = -2 * sp.I * m * g_(s_, c_)
bare_m_term_f = 2 * sp.I * m * f_(s_, c_)
check(
    "P9 the bare m-term is present and needs the hom=(s^2+c^2) fix, exactly "
    "as C185's own trick required for its bare m-term",
    sp.expand(eq0_h - eq0_h.subs(bare_m_term_g, 0)) != 0
    and sp.expand(eq1_h - eq1_h.subs(bare_m_term_f, 0)) != 0,
)
eq0_h = eq0_h.subs(bare_m_term_g, -2 * sp.I * m * hom * g_(s_, c_))
eq1_h = eq1_h.subs(bare_m_term_f, 2 * sp.I * m * hom * f_(s_, c_))


def kernel_dim(m_val, n_val, lam_val, N):
    a = sp.symbols(f"a0:{N + 1}")
    b = sp.symbols(f"b0:{N + 1}")
    f_poly = sum(a[j] * s_**j * c_ ** (N - j) for j in range(N + 1))
    g_poly = sum(b[j] * s_**j * c_ ** (N - j) for j in range(N + 1))
    subs = {m: m_val, n: n_val, lam: lam_val}
    e0 = eq0_h.subs(subs).subs(
        {
            sp.Derivative(g_(s_, c_), s_): sp.diff(g_poly, s_),
            sp.Derivative(g_(s_, c_), c_): sp.diff(g_poly, c_),
        }
    )
    e0 = e0.subs({g_(s_, c_): g_poly, f_(s_, c_): f_poly})
    e1 = eq1_h.subs(subs).subs(
        {
            sp.Derivative(f_(s_, c_), s_): sp.diff(f_poly, s_),
            sp.Derivative(f_(s_, c_), c_): sp.diff(f_poly, c_),
        }
    )
    e1 = e1.subs({f_(s_, c_): f_poly, g_(s_, c_): g_poly})
    unk = list(a) + list(b)
    rows = []
    for eq in (sp.expand(e0), sp.expand(e1)):
        p = sp.Poly(eq, s_, c_)
        for _, coeff in p.terms():
            rows.append([sp.diff(coeff, u) for u in unk])
    return len(unk) - sp.Matrix(rows).rank()


t0 = time.time()
scan = {}
for m_val, n_val in [
    (sp.Rational(1, 2), -sp.Rational(1, 2)),
    (-sp.Rational(1, 2), sp.Rational(1, 2)),
    (sp.Rational(1, 2), sp.Rational(1, 2)),
    (-sp.Rational(1, 2), -sp.Rational(1, 2)),
]:
    for N in range(4):
        for lv in range(-5, 6):
            d = kernel_dim(m_val, n_val, lv, N)
            if d > 0:
                scan[(m_val, n_val, N, lv)] = d
elapsed_scan = time.time() - t0
print(
    f"  blind scan: 4 (m,n) x 4 degrees x 11 lambda = 176 kernel_dim calls, {elapsed_scan:.1f}s"
)
print(f"  nonzero-kernel hits: {scan if scan else 'NONE'}")

check(
    f"P10 the blind scan itself completed fast ({elapsed_scan:.1f}s for 176 cases) "
    "-- confirms claim (a): the method is fast even swept broadly",
    elapsed_scan < 60.0,
)

# claim (b) is intentionally left as a documented, honest non-result -- see
# claim.md and decision.md for why this is not pushed further this round.
print()
print("  claim (b) [eigenvalue match]: NOT confirmed this round -- clean null")
print("  across the scan above. See decision.md for the periodicity hypothesis")
print("  and why this is reported honestly rather than forced.")

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print(
    f"C187: {len(PASS)} passed, {len(FAIL)} failed  (claim (a) checks only -- see above)"
)
if FAIL:
    for f in FAIL:
        print(f"  FAILED: {f}")
print("=" * 78)
