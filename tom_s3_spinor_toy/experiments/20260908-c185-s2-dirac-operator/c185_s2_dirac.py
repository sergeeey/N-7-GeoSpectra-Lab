r"""
C185 -- the S^2 Dirac operator, built rather than quoted, and its spectrum.

C182 recorded the gap in its own words: "The S^2 Dirac eigenvalues +-(l+1) are
NOT derived. Only multiplicities. The S^2 Dirac operator was not built."

  A  metric -> frame -> spin connection, the connection obtained by SOLVING
     Cartan's first structure equation and then verified to satisfy it
  B  assemble D; fix the factor that makes it self-adjoint rather than assuming
  C  D^2 against the Lichnerowicz form -- the curvature constant must come out
  D  the spectrum, by exact linear algebra in a finite space (see below)
  E  multiplicities, per sign, against C182's independently obtained numbers
  F  injected error: perturb the connection, the pattern must break

WHY THE SPECTRUM IS COMPUTED THE WAY IT IS. A first attempt routed the
eigenfunctions down from S^3 by the Hopf descent, to reuse C182/C184b's
machinery. That version ran for 25 minutes of CPU without producing a line:
every matrix entry needed `simplify` on an expression mixing exponentials and
half-angle trigonometry, inside a double loop. It was killed, not debugged --
the approach was wrong, not the code.

What replaces it is exact and finite. Write psi = (f(theta), g(theta)) e^{i m phi}
with m half-integer. Then D psi = lambda psi becomes two first-order ODEs, and in
terms of s = sin(theta/2), c = cos(theta/2) -- for which ds/dtheta = c/2 and
dc/dtheta = -s/2 -- multiplying through by 4sc turns them into POLYNOMIAL
identities. Taking f and g homogeneous of degree N in (s,c) makes both sides
homogeneous of degree N+2, so the eigenvalue problem is a linear system over
Q(i) with N+1 unknowns per component. No simplification of transcendental
expressions anywhere; the whole spectrum falls out of nullspace dimensions.

A degree-N solution reappears inside every higher N (multiply by s^2+c^2 = 1),
so a single N large enough captures every level below it -- which is why one
scan at N=5 suffices for the first three levels.

Exact symbolic arithmetic; no floating point in any verdict.
"""

import sympy as sp

th, ph = sp.symbols("theta phi", real=True)
s_, c_ = sp.symbols("s c", positive=True)  # sin(theta/2), cos(theta/2)
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
OK = []


def check(label, cond, detail=""):
    OK.append((label, bool(cond)))
    print(
        f"  [{'PASS' if cond else 'FAIL'}] {label}{('  ' + detail) if detail else ''}"
    )


def simp(e):
    return sp.simplify(sp.trigsimp(sp.expand_trig(sp.simplify(e))))


# ===========================================================================
print("=" * 78)
print("A  metric -> frame -> spin connection, the connection SOLVED for   [P1,P2]")
print("=" * 78)
g_metric = sp.Matrix([[1, 0], [0, sp.sin(th) ** 2]])
e1 = sp.Matrix([[1, 0]])  # coefficient rows over (dtheta, dphi)
e2 = sp.Matrix([[0, sp.sin(th)]])
recon = e1.T * e1 + e2.T * e2
check(
    "P1 the frame reproduces the metric: sum_a e^a (x) e^a = g",
    simp(recon - g_metric) == sp.zeros(2, 2),
)

A, B = sp.symbols("A B")


def d_of(form):
    """exterior derivative of a 1-form; returns the dtheta ^ dphi coefficient."""
    return sp.diff(form[0, 1], th) - sp.diff(form[0, 0], ph)


def wedge(a, b):
    return a[0, 0] * b[0, 1] - a[0, 1] * b[0, 0]


om12 = sp.Matrix([[A, B]])
sol = sp.solve(
    [sp.expand(d_of(e1) + wedge(om12, e2)), sp.expand(d_of(e2) + wedge(-om12, e1))],
    [A, B],
    dict=True,
)
check(
    "P2a Cartan's first structure equation has a unique solution",
    len(sol) == 1,
    f"{sol}",
)
sol = sol[0]
om12 = sp.Matrix([[sol[A], sol[B]]])
print(f"  omega^1_2 = {sol[A]} dtheta + {sol[B]} dphi")
r1 = simp(d_of(e1) + wedge(om12, e2))
r2 = simp(d_of(e2) + wedge(-om12, e1))
check(
    "P2b and it satisfies that equation IDENTICALLY (residuals exactly zero)",
    r1 == 0 and r2 == 0,
    f"residuals ({r1}, {r2})",
)

# ===========================================================================
print()
print("=" * 78)
print("B  assemble D, and fix the factor that makes it self-adjoint     [P3]")
print("=" * 78)
spin_term = sp.Rational(1, 4) * (sol[B] * s1 * s2 - sol[B] * s2 * s1)
print(f"  spin-connection term in the phi direction: {sp.simplify(spin_term).tolist()}")


def D_raw(psi, spin=None):
    """sigma^a e_a^mu (partial_mu + connection), acting on a 2-component psi."""
    sp_t = spin_term if spin is None else spin
    dth = sp.Matrix([sp.diff(x, th) for x in psi])
    dph = sp.Matrix([sp.diff(x, ph) for x in psi])
    return sp.expand(s1 * dth + s2 * (dph + sp_t * psi) / sp.sin(th))


probe = sp.Matrix(
    [sp.cos(th / 2) * sp.exp(sp.I * ph / 2), sp.sin(th / 2) * sp.exp(-sp.I * ph / 2)]
)
standard = s1 * sp.Matrix(
    [sp.diff(x, th) + sp.Rational(1, 2) / sp.tan(th) * x for x in probe]
) + s2 * sp.Matrix([sp.diff(x, ph) for x in probe]) / sp.sin(th)
check(
    "B1 the assembled operator equals sigma^1(d_th + (1/2)cot th) + sigma^2 d_ph/sin th",
    all(simp(v) == 0 for v in (D_raw(probe) - standard)),
)

# Self-adjointness: <v, D u> - <D v, u> must be a total theta-derivative, so that
# it integrates to zero over the closed sphere. Checked on a generic pair with
# the radial parts left as unknown real functions.
fa, fb, ga, gb = sp.symbols("fa fb ga gb", cls=sp.Function)
# WHY both components carry the SAME phase: D swaps the two components, so
# D psi = lambda psi is only consistent when both carry one and the same
# e^{i m phi}. The first draft gave them opposite phases; the Euler test then
# returned residues proportional to e^{+-i phi}, which is the signature of a
# test pair that is not of the right shape rather than of a non-symmetric
# operator. Third failure in this round that was the check and not the result.
u = sp.Matrix([fa(th) * sp.exp(sp.I * ph / 2), fb(th) * sp.exp(sp.I * ph / 2)])
v = sp.Matrix([ga(th) * sp.exp(sp.I * ph / 2), gb(th) * sp.exp(sp.I * ph / 2)])


def D(psi, spin=None):
    """The self-adjoint Dirac operator. The -i is not decoration -- see P3."""
    return sp.expand(-sp.I * D_raw(psi, spin))


def cj(e):
    return e.subs({sp.I: -sp.I})


lhs = sum(cj(v[i]) * D(u)[i] for i in range(2)) * sp.sin(th)
rhs = sum(cj(D(v)[i]) * u[i] for i in range(2)) * sp.sin(th)
residue = sp.expand(lhs - rhs)

# Is the residue a total theta-derivative? Decide it without having to guess
# WHAT of: an expression in functions and their first derivatives is a total
# derivative exactly when the Euler operator annihilates it,
#     dL/dh - d/dtheta ( dL/dh' ) = 0   for every function h appearing.
# The first draft of this check guessed an antiderivative instead and failed --
# which cannot distinguish "not self-adjoint" from "guessed wrong".
FUNCS = [fa(th), fb(th), ga(th), gb(th)]
euler = [
    sp.simplify(
        sp.diff(residue, h) - sp.diff(sp.diff(residue, sp.Derivative(h, th)), th)
    )
    for h in FUNCS
]
check(
    "P3 D is formally self-adjoint: <v,Du> - <Dv,u> is a total theta-derivative",
    all(e == 0 for e in euler),
    f"Euler operator on each of the four radial functions: {euler}",
)

# ===========================================================================
print()
print("=" * 78)
print("C  D^2 against the Lichnerowicz form                              [P4]")
print("=" * 78)


# Lichnerowicz relates D^2 to the SPINOR connection Laplacian, not the scalar
# one -- the connection sits inside the phi derivative. The first draft of this
# check used the scalar Laplacian and failed, which was the check being wrong
# rather than the operator: the residue it reported,
# (sin^2 th - 2 cos th + 1)/(4 sin^2 th), is exactly the connection term it had
# left out. Built here from the same connection D itself uses.
def conn_laplacian(psi):
    """- g^{mu nu} nabla_mu nabla_nu, with nabla_phi = d_phi + spin_term."""
    d2th = sp.Matrix([sp.diff(x, th, 2) for x in psi])
    d1th = sp.Matrix([sp.diff(x, th) for x in psi])
    dphi = sp.Matrix([sp.diff(x, ph) for x in psi]) + spin_term * psi
    dphi2 = sp.Matrix([sp.diff(x, ph) for x in dphi]) + spin_term * dphi
    return sp.expand(-(d2th + sp.cos(th) / sp.sin(th) * d1th + dphi2 / sp.sin(th) ** 2))


FF, GG = sp.Function("FF"), sp.Function("GG")
test = sp.Matrix([FF(th) * sp.exp(sp.I * ph / 2), GG(th) * sp.exp(-sp.I * ph / 2)])
resid = [
    simp(x) for x in (D(D(test)) - conn_laplacian(test) - sp.Rational(1, 2) * test)
]
print(f"  D^2 - (nabla* nabla + R/4) with R = 2, componentwise: {resid}")
check(
    "P4 D^2 = nabla* nabla + R/4 with R = 2 for the unit sphere (Lichnerowicz)",
    all(r == 0 for r in resid),
)

# ===========================================================================
print()
print("=" * 78)
print("D  the spectrum, by exact linear algebra in a finite space")
print("=" * 78)
# Acting on psi = (f, g) e^{i m phi}, D psi = lambda psi is
#     -i[ g' + (1/2)cot(th) g + (m/sin th) g ] = lambda f
#     -i[ f' + (1/2)cot(th) f - (m/sin th) f ] = lambda g
# In s = sin(th/2), c = cos(th/2):  cot th = (c^2-s^2)/(2sc),  sin th = 2sc.
# Multiplying by 4sc, and homogenising the bare `2m` term with s^2+c^2 = 1:
#     -i[ 4sc g' + (c^2-s^2) g + 2m (s^2+c^2) g ] = 4sc lambda f
#     -i[ 4sc f' + (c^2-s^2) f - 2m (s^2+c^2) f ] = 4sc lambda g
# Both sides homogeneous of degree N+2 when f, g are homogeneous of degree N.


def deriv(poly):
    """d/dtheta on a polynomial in s=sin(th/2), c=cos(th/2)."""
    return sp.expand(sp.diff(poly, s_) * c_ / 2 - sp.diff(poly, c_) * s_ / 2)


def kernel_dim(m, lam, N):
    """Dimension of the space of degree-N (f,g) solving D psi = lam psi."""
    a = sp.symbols(f"a0:{N + 1}")
    b = sp.symbols(f"b0:{N + 1}")
    f = sum(a[j] * s_**j * c_ ** (N - j) for j in range(N + 1))
    g = sum(b[j] * s_**j * c_ ** (N - j) for j in range(N + 1))
    hom = s_**2 + c_**2
    eqA = sp.expand(
        -sp.I * (4 * s_ * c_ * deriv(g) + (c_**2 - s_**2) * g + 2 * m * hom * g)
        - 4 * s_ * c_ * lam * f
    )
    eqB = sp.expand(
        -sp.I * (4 * s_ * c_ * deriv(f) + (c_**2 - s_**2) * f - 2 * m * hom * f)
        - 4 * s_ * c_ * lam * g
    )
    eqs = []
    for e in (eqA, eqB):
        p = sp.Poly(e, s_, c_)
        eqs.extend(p.coeffs())
    M = sp.Matrix([[sp.expand(e).coeff(v) for v in a + b] for e in eqs])
    return len(a + b) - M.rank()


N = 5
HALVES = [sp.Rational(k, 2) for k in (-7, -5, -3, -1, 1, 3, 5, 7)]
LAMS = [sp.Integer(k) for k in (-3, -2, -1, 1, 2, 3)]
table = {}
for lam in LAMS:
    ms = [m for m in HALVES if kernel_dim(m, lam, N) > 0]
    table[lam] = ms
    print(
        f"  lambda = {int(lam):>2}:  solutions at m = {[str(x) for x in ms]}   "
        f"-> multiplicity {len(ms)}"
    )

check(
    "P5 lambda = +-1 occurs with multiplicity 2 (per sign)",
    len(table[sp.Integer(1)]) == 2 and len(table[sp.Integer(-1)]) == 2,
)
check(
    "P6a lambda = +-2 occurs with multiplicity 4 (per sign)",
    len(table[sp.Integer(2)]) == 4 and len(table[sp.Integer(-2)]) == 4,
)
check(
    "P6b lambda = +-3 occurs with multiplicity 6 (per sign)",
    len(table[sp.Integer(3)]) == 6 and len(table[sp.Integer(-3)]) == 6,
)
check(
    "P6c and the pattern is |lambda| = n+1 with multiplicity 2(n+1)",
    all(
        len(table[sp.Integer(sgn * (n + 1))]) == 2 * (n + 1)
        for n in range(3)
        for sgn in (1, -1)
    ),
)
check(
    "P6d zero is NOT an eigenvalue -- the sphere's curvature forbids it",
    kernel_dim(sp.Rational(1, 2), sp.Integer(0), N) == 0
    and kernel_dim(sp.Rational(3, 2), sp.Integer(0), N) == 0,
)

# ===========================================================================
print()
print("=" * 78)
print("E  the two routes meeting                                          [P7]")
print("=" * 78)
mine = [len(table[sp.Integer(n + 1)]) for n in range(3)]
print(f"  multiplicities from THIS route (operator eigenvalues) : {mine}")
print("  from C182 (Hopf weight-sector dimensions, k = 1, 3, 5) : [2, 4, 6]")
check(
    "P7 the operator's multiplicities equal C182's independently obtained sector sizes",
    mine == [2, 4, 6],
)

# ===========================================================================
print()
print("=" * 78)
print("F  injected error -- perturb the connection, the pattern must break")
print("=" * 78)


# Doubling the connection coefficient changes the (c^2-s^2) term to 2(c^2-s^2).
def kernel_dim_bad(m, lam, N):
    a = sp.symbols(f"p0:{N + 1}")
    b = sp.symbols(f"q0:{N + 1}")
    f = sum(a[j] * s_**j * c_ ** (N - j) for j in range(N + 1))
    g = sum(b[j] * s_**j * c_ ** (N - j) for j in range(N + 1))
    hom = s_**2 + c_**2
    eqA = sp.expand(
        -sp.I * (4 * s_ * c_ * deriv(g) + 2 * (c_**2 - s_**2) * g + 2 * m * hom * g)
        - 4 * s_ * c_ * lam * f
    )
    eqB = sp.expand(
        -sp.I * (4 * s_ * c_ * deriv(f) + 2 * (c_**2 - s_**2) * f - 2 * m * hom * f)
        - 4 * s_ * c_ * lam * g
    )
    eqs = []
    for e in (eqA, eqB):
        eqs.extend(sp.Poly(e, s_, c_).coeffs())
    M = sp.Matrix([[sp.expand(e).coeff(v) for v in a + b] for e in eqs])
    return len(a + b) - M.rank()


bad = [
    len([m for m in HALVES if kernel_dim_bad(m, sp.Integer(n + 1), N) > 0])
    for n in range(3)
]
print(f"  with the connection coefficient doubled: {bad}")
check(
    "F1 the wrong connection does NOT give 2, 4, 6 -- so the check can fail",
    bad != [2, 4, 6],
    f"got {bad}",
)

# ===========================================================================
print()
print("=" * 78)
print("SUMMARY")
print("=" * 78)
failed = [lab for lab, ok in OK if not ok]
for lab, ok in OK:
    print(f"  {'PASS' if ok else 'FAIL'}  {lab}")
print(f"\n{len(OK) - len(failed)} of {len(OK)} checks passed")
print(
    "FAILED: " + "; ".join(failed)
    if failed
    else "the S^2 Dirac operator is built from the metric, and its eigenvalues "
    "+-(n+1) with multiplicity 2(n+1) are derived here, not cited"
)
