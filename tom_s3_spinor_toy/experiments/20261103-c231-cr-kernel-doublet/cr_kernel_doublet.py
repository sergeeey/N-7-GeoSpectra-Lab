"""C231: the tangential Cauchy-Riemann operator on S^3 as a candidate selector of the doublet.

Objects: x1, x2 = xi^1, xi^2 and y1, y2 = conj(xi^1), conj(xi^2) as independent symbols; functions on S^3 are polynomials
modulo the relation x1 y1 + x2 y2 = 1 (reduced by the one-element Groebner basis, leading term x1*y1 in lex x1>y1>x2>y2).
Lbar = x1 d/dy2 - x2 d/dy1 is tangent to S^3 (Lbar(x1 y1 + x2 y2) = 0) and kills holomorphic functions.
Charge n of the Hopf U(1): f(t xi) = t^n f(xi), i.e. (#x) - (#y) = n.
SU(2) acts by the pull-back convention A of C229: D_a = -1/2 (sigma_a xi).d + 1/2 (conj(sigma_a) conj(xi)).dbar.

Predictions written BEFORE running:
  P1. For every n = 0..4 the kernel of Lbar on charge-n functions of degree <= n + 3 has dimension n + 1 and is the span of the
      holomorphic monomials x1^i x2^(n-i); for n < 0 it is zero.  (dimension n+1 = Riemann-Roch for O(n) on CP^1.)
  P2. The kernel is SU(2)-invariant (D_a maps it into itself); the Casimir sum D_a D_a equals (n/2)(n/2 + 1).
  P3. D3 weights on (x1, x2) are (-1/2, +1/2) (convention A); the anti-holomorphic doublet (y1, y2) has the opposite weights, and
      eta = (y2, -y1) transforms exactly like (x1, x2).
  P4. H2 of C228 (Psi, Phi, in the gauge xi^1 real) equals {f(xi) * J xi : f in span(x1, x2)}, J xi = (-conj xi^2, conj xi^1):
      Psi = xi^2 * J xi, and Phi proportional to xi^1 * J xi.  J xi is the pointwise Gamma = -1 eigenvector.
Self-controls: a wrong operator (Lbar with a sign error, which is not tangent) must give a different kernel dimension; the kernel of
the CONJUGATE operator L = y1 d/dx2 - y2 d/dx1 at charge n < 0 must have dimension |n| + 1.
"""

import itertools
import sys

import sympy as sp

x1, x2, y1, y2 = sp.symbols("x1 x2 y1 y2")
VARS = (x1, y1, x2, y2)
REL = x1 * y1 + x2 * y2 - 1
I = sp.I
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
SIGC = [m.conjugate() for m in SIG]
FAILS = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)


def expect_caught(name, cond):
    print(("CAUGHT " if not cond else "MISSED ") + name)
    if cond:
        FAILS.append("self-control not caught: " + name)


def nf(f):
    """normal form of f modulo the sphere relation"""
    f = sp.expand(f)
    if f == 0:
        return sp.Integer(0)
    _, r = sp.reduced(f, [REL], *VARS, order="lex")
    return sp.expand(r)


def monomials(n, N):
    """normal-form monomials x^a y^b with charge n and total degree <= N (not both x1 and y1 present)"""
    out = []
    for a1, a2, b1, b2 in itertools.product(range(N + 1), repeat=4):
        if a1 + a2 + b1 + b2 > N or (a1 + a2) - (b1 + b2) != n:
            continue
        if a1 > 0 and b1 > 0:
            continue
        out.append(x1**a1 * x2**a2 * y1**b1 * y2**b2)
    return out


def Lbar(f, sign=1):
    return sp.diff(f, y2) * x1 - sign * sp.diff(f, y1) * x2


def Lconj(f):
    return sp.diff(f, x2) * y1 - sp.diff(f, x1) * y2


def coeff_matrix(images, basis):
    """rows: images expressed in the monomial basis (images already normal-formed)"""
    monos = sorted({m for im in images for m in sp.Poly(im, *VARS).monoms()} | set(), key=str)
    idx = {m: i for i, m in enumerate(monos)}
    M = sp.zeros(len(images), len(monos))
    for r, im in enumerate(images):
        if im == 0:
            continue
        for mon, c in sp.Poly(im, *VARS).terms():
            M[r, idx[mon]] = c
    return M


def kernel(op, n, N):
    basis = monomials(n, N)
    imgs = [nf(op(b)) for b in basis]
    B = sp.Matrix(len(basis), len(basis), lambda i, j: 0)
    # kernel of the linear map basis -> images: solve sum c_i image_i = 0
    M = coeff_matrix(imgs, basis)
    ns = M.T.nullspace() if M.shape[1] else [sp.eye(len(basis))[:, i] for i in range(len(basis))]
    vecs = []
    for v in ns:
        vecs.append(nf(sum(v[i] * basis[i] for i in range(len(basis)))))
    return vecs


def D(a, f):
    sx = SIG[a] * sp.Matrix([x1, x2])
    sy = SIGC[a] * sp.Matrix([y1, y2])
    return sp.expand(
        -sp.Rational(1, 2) * (sx[0] * sp.diff(f, x1) + sx[1] * sp.diff(f, x2))
        + sp.Rational(1, 2) * (sy[0] * sp.diff(f, y1) + sy[1] * sp.diff(f, y2))
    )


def in_span(f, vecs):
    f = nf(f)
    if f == 0:
        return True
    cs = sp.symbols(f"k0:{len(vecs)}")
    expr = sp.expand(f - sum(c * v for c, v in zip(cs, vecs)))
    expr = nf(expr)
    eqs = sp.Poly(expr, *VARS).coeffs() if expr != 0 else []
    return bool(sp.solve(eqs, cs, dict=True)) if cs else False


# ---- P1, P2: kernel dimension, holomorphic monomials, invariance, Casimir
for n in range(0, 5):
    N = n + 3
    ker = kernel(Lbar, n, N)
    check(f"n = {n}: dim ker Lbar (charge n, degree <= {N}) = {n + 1}", len(ker) == n + 1)
    hol = [nf(x1**i * x2 ** (n - i)) for i in range(n + 1)]
    check(
        f"n = {n}: kernel = span of the holomorphic monomials x1^i x2^(n-i)",
        all(in_span(h, ker) for h in hol) and all(in_span(k, hol) for k in ker),
    )
    inv = all(in_span(D(a, k), ker) for a in range(3) for k in ker)
    cas = all(
        nf(sum(D(a, D(a, k)) for a in range(3)) - sp.Rational(n, 2) * (sp.Rational(n, 2) + 1) * k)
        == 0
        for k in ker
    )
    check(f"n = {n}: kernel is SU(2)-invariant and Casimir = (n/2)(n/2+1)", inv and cas)
for n in (-1, -2):
    check(f"n = {n}: kernel of Lbar is zero (degree <= 4)", len(kernel(Lbar, n, 4)) == 0)

# ---- P3: weights, conjugate doublet, epsilon-image
w = [sp.simplify(D(2, v) / v) for v in (x1, x2, y1, y2)]
check(
    "D3 weights on (x1, x2, y1, y2) = (-1/2, +1/2, +1/2, -1/2): anti-holomorphic doublet has the opposite weights",
    w == [-sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2), -sp.Rational(1, 2)],
)
eta = [y2, -y1]
ok = all(
    sp.expand(D(a, eta[i]) + sp.Rational(1, 2) * (SIG[a] * sp.Matrix(eta))[i]) == 0
    for a in range(3)
    for i in range(2)
)
check("eta = (y2, -y1) transforms exactly like (x1, x2): D_a eta_i = -1/2 (sigma_a eta)_i", ok)
kc = kernel(Lconj, -1, 3)
check(
    "charge -1: kernel of the conjugate operator L has dimension 2 and is span{y1, y2}",
    len(kc) == 2 and all(in_span(v, kc) for v in (y1, y2)),
)
check(
    "charge -n: kernel of L has dimension n + 1 for n = 2, 3",
    all(len(kernel(Lconj, -n, n + 3)) == n + 1 for n in (2, 3)),
)

# ---- P4: H2 of C228 as {f(xi) J xi}
th, ph = sp.symbols("theta phi", real=True)
Sm = sp.Matrix([[0, 0], [1, 0]])


def Lm(f):
    return sp.exp(-I * ph) * (-sp.diff(f, th) + I * sp.cos(th) / sp.sin(th) * sp.diff(f, ph))


Psi = sp.Matrix([-(1 - sp.cos(th)) / 2, sp.exp(I * ph) * sp.sin(th) / 2])
Phi = sp.Matrix([Lm(Psi[0]), Lm(Psi[1])]) + Sm * Psi
xi_pt = {
    x1: sp.cos(th / 2),
    x2: sp.sin(th / 2) * sp.exp(I * ph),
    y1: sp.cos(th / 2),
    y2: sp.sin(th / 2) * sp.exp(-I * ph),
}
Jxi = sp.Matrix([-y2, y1]).subs(xi_pt, simultaneous=True)
check(
    "Psi = xi^2 * J xi on the section xi = (cos th/2, sin th/2 e^{i ph})",
    sp.simplify(Psi - xi_pt[x2] * Jxi) == sp.zeros(2, 1),
)
ratio = sp.simplify((Phi[0] / (xi_pt[x1] * Jxi[0])))
check(
    "Phi = k * xi^1 * J xi with a constant k (here k = %s)" % ratio,
    ratio.free_symbols == set() and sp.simplify(Phi - ratio * xi_pt[x1] * Jxi) == sp.zeros(2, 1),
)
n_vec = sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])
Gam = sum((n_vec[k] * SIG[k] for k in range(3)), sp.zeros(2))
check(
    "J xi is the pointwise Gamma = -1 eigenvector (sigma.n J xi = - J xi)",
    all(sp.simplify(sp.expand(sp.expand_trig(e).rewrite(sp.exp))) == 0 for e in (Gam * Jxi + Jxi)),
)

# ---- self-controls
expect_caught(
    "the sign-flipped operator x1 d/dy2 + x2 d/dy1 is tangent to S^3 (kills x1 y1 + x2 y2)",
    nf(Lbar(x1 * y1 + x2 * y2, sign=-1)) == 0,
)
expect_caught("conjugate operator L has a nonzero kernel at charge +1", len(kernel(Lconj, 1, 4)) > 0)
expect_caught("kernel of Lbar at n = -1 is NOT empty", len(kernel(Lbar, -1, 4)) > 0)

print("\nFAILS:", FAILS if FAILS else "none")
sys.exit(1 if FAILS else 0)
