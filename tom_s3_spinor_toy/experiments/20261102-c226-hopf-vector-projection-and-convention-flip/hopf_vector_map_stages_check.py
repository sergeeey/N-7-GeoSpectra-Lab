"""the correspondent's stages (his message of 2 Nov 2026): F = xi xi^dagger, V^i = 1/2 tr(F sigma^i),
SU(2) -> SO(3), point-to-orbit map, normalisation, ladder operators on the normalised doublet.

Two conventions for how SU(2) acts on the doublet are computed side by side:
  A  (note of 29 Oct, our D_a): (U(g) f)(xi) = f(g^{-1} xi); generators from d/dt at t = 0.
  B  (the correspondent's suggestion, 2 Nov): the components xi themselves are moved, xi -> g xi (no inverse).
Exact checks use rational points on S^3; the random-sample check is numeric and labelled.
"""

import numpy as np
import sympy as sp

I = sp.I
x1, x2, y1, y2 = sp.symbols(
    "x1 x2 y1 y2"
)  # xi^1, xi^2, conj(xi^1), conj(xi^2) as independent symbols
xi = sp.Matrix([x1, x2])
xib = sp.Matrix([y1, y2])
sig = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
F = xi * xib.T  # F_ab = xi^a conj(xi^b)
X = [x1, x2]
Y = [y1, y2]

fails = []


def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        fails.append(name)


def zero(expr):
    return sp.expand(expr) == 0


def all_zero(mat):
    return all(zero(e) for e in list(mat))


# ---------------------------------------------------------------- Stage 1: F and V
V = [sp.expand(sp.Rational(1, 2) * (F * s).trace()) for s in sig]
check(
    "S1a V^i = 1/2 tr(F sigma^i) = 1/2 xi^dagger sigma^i xi",
    all(zero(V[i] - sp.Rational(1, 2) * (xib.T * sig[i] * xi)[0]) for i in range(3)),
)
recon = sp.Rational(1, 2) * F.trace() * sp.eye(2) + sum(
    (V[i] * sig[i] for i in range(3)), sp.zeros(2)
)
check(
    "S1b F = 1/2 tr(F) I + V^i sigma^i (full decomposition of a 2x2 complex matrix)",
    all_zero(F - recon),
)
xi_norm2 = sp.expand((xib.T * xi)[0])
check("S1c tr F = |xi|^2", zero(F.trace() - xi_norm2))
check(
    "S1d Fierz: sum_i V^i V^i = (|xi|^2)^2 / 4 (polynomial identity)",
    zero(sum(v * v for v in V) - xi_norm2**2 / 4),
)


# ---------------------------------------------------------------- Stage 2: SU(2) -> SO(3)
def Rmat(gm):
    """R_ij = 1/2 tr(sigma_j g^dag sigma_i g), so that V(g xi) = R V(xi)."""
    gd = gm.H
    return sp.Matrix(3, 3, lambda i, j: sp.Rational(1, 2) * (sig[j] * gd * sig[i] * gm).trace())


def g_of(a, b):
    """SU(2) element [[a, -conj b], [b, conj a]]; needs |a|^2 + |b|^2 = 1."""
    return sp.Matrix([[a, -sp.conjugate(b)], [b, sp.conjugate(a)]])


quats = [
    (sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2)),
    (sp.Rational(3, 5), sp.Rational(4, 5), 0, 0),
    (0, 0, 1, 0),
    (sp.Rational(2, 3), sp.Rational(1, 3), sp.Rational(2, 3), 0),
    (sp.Rational(12, 13), 0, sp.Rational(4, 13), sp.Rational(3, 13)),
]
for q in quats:
    assert sum(sp.Rational(v) ** 2 for v in q) == 1
    gm = g_of(q[0] + I * q[1], q[2] + I * q[3])
    Rg = Rmat(gm)
    check(
        f"S2a exact g(quat={tuple(str(v) for v in q)}): R R^T = I and det R = +1",
        sp.simplify(Rg * Rg.T - sp.eye(3)) == sp.zeros(3) and sp.simplify(Rg.det() - 1) == 0,
    )
    gxi = gm * xi
    gxib = gm.conjugate() * xib  # conj(g xi) = conj(g) conj(xi)
    Vg = [
        sp.expand(v.subs({x1: gxi[0], x2: gxi[1], y1: gxib[0], y2: gxib[1]}, simultaneous=True))
        for v in V
    ]
    check(
        f"S2b exact g(quat={tuple(str(v) for v in q)}): V(g xi) = R V(xi) for symbolic xi",
        all(zero(Vg[i] - sum(Rg[i, j] * V[j] for j in range(3))) for i in range(3)),
    )
    print("     R =", Rg.tolist())

# Float check on many random SU(2) elements (numeric, not exact)
rng = np.random.default_rng(0)
sig_np = [np.array(s.tolist(), dtype=complex) for s in sig]
max_dev = 0.0
min_det = 1.0
for _ in range(2000):
    q = rng.normal(size=4)
    q /= np.linalg.norm(q)
    a = q[0] + 1j * q[1]
    b = q[2] + 1j * q[3]
    gn = np.array([[a, -np.conj(b)], [b, np.conj(a)]])
    Rn = np.array(
        [
            [0.5 * np.trace(sig_np[j] @ gn.conj().T @ sig_np[i] @ gn).real for j in range(3)]
            for i in range(3)
        ]
    )
    max_dev = max(max_dev, np.max(np.abs(Rn @ Rn.T - np.eye(3))))
    min_det = min(min_det, np.linalg.det(Rn))
check(f"S2c [NUMERIC, 2000 random g] max |R R^T - I| = {max_dev:.2e} < 1e-12", max_dev < 1e-12)
check(f"S2d [NUMERIC, 2000 random g] min det R = {min_det:.6f} > 1 - 1e-12", min_det > 1 - 1e-12)

# ---------------------------------------------------------------- Stage 3: complex point <-> real point
# For |xi| = 1, the matrix g(xi) = [[xi1, -conj xi2], [xi2, conj xi1]] has first column xi,
# so xi = g(xi) e_1: every point on S^3 is an SU(2) image of (1, 0).
e1 = sp.Matrix([1, 0])
xi0 = (1, 0)
V0 = [sp.simplify(v.subs({x1: 1, x2: 0, y1: 1, y2: 0})) for v in V]
check("S3a V(1,0) = (0, 0, 1/2)", V0 == [0, 0, sp.Rational(1, 2)])
rng2 = np.random.default_rng(1)
dev3 = 0.0
for _ in range(500):
    z = rng2.normal(size=4)
    z /= np.linalg.norm(z)
    xv = np.array([z[0] + 1j * z[1], z[2] + 1j * z[3]])
    gn = np.array([[xv[0], -np.conj(xv[1])], [xv[1], np.conj(xv[0])]])
    Vn = np.array([0.5 * np.vdot(xv, s @ xv).real for s in sig_np])
    Rn = np.array(
        [
            [0.5 * np.trace(sig_np[j] @ gn.conj().T @ sig_np[i] @ gn).real for j in range(3)]
            for i in range(3)
        ]
    )
    V_from_orbit = Rn @ np.array([0, 0, 0.5])
    dev3 = max(dev3, np.max(np.abs(Vn - V_from_orbit)))
check(f"S3b [NUMERIC, 500 unit xi] V(xi) = R(g(xi)) (0,0,1/2): max dev = {dev3:.2e}", dev3 < 1e-12)

# Radius and fibre: |V| = |xi|^2 / 2, and V is invariant under xi -> e^{i phi} xi (fibres are circles).
phi = sp.symbols("phi", real=True)
ph = sp.exp(I * phi)
Vphase = [
    sp.simplify(
        v.subs(
            {x1: ph * x1, x2: ph * x2, y1: sp.conjugate(ph) * y1, y2: sp.conjugate(ph) * y2},
            simultaneous=True,
        )
    )
    for v in V
]
check(
    "S3c phase invariance: V(e^{i phi} xi) = V(xi)",
    all(sp.simplify(Vphase[i] - V[i]) == 0 for i in range(3)),
)

# ---------------------------------------------------------------- Stage 4: normalisation
# Points where V is a coordinate direction (unit xi):
pts = {
    "x1": (1 / sp.sqrt(2), 1 / sp.sqrt(2)),
    "x2": (1 / sp.sqrt(2), I / sp.sqrt(2)),
    "x3": (1, 0),
}
for name, (u1, u2) in pts.items():
    cj = {y1: sp.conjugate(u1), y2: sp.conjugate(u2)}
    vals = [sp.nsimplify(sp.simplify(v.subs({x1: u1, x2: u2}).subs(cj))) for v in V]
    print(f"     point for {name}: xi = ({sp.simplify(u1)}, {sp.simplify(u2)}), V = {vals}")
check(
    "S4a x1-point gives V = (1/2, 0, 0)",
    [
        sp.simplify(
            v.subs({x1: 1 / sp.sqrt(2), x2: 1 / sp.sqrt(2), y1: 1 / sp.sqrt(2), y2: 1 / sp.sqrt(2)})
        )
        for v in V
    ]
    == [sp.Rational(1, 2), 0, 0],
)
check(
    "S4b x2-point gives V = (0, 1/2, 0)",
    [
        sp.simplify(
            v.subs(
                {x1: 1 / sp.sqrt(2), x2: I / sp.sqrt(2), y1: 1 / sp.sqrt(2), y2: -I / sp.sqrt(2)}
            )
        )
        for v in V
    ]
    == [0, sp.Rational(1, 2), 0],
)
# Normalised harmonic fields (project's Q1 convention): Y^i = sqrt((n+1)/S) x^i/r with n = 2, S = 4 pi
lam_sq = sp.sqrt(3 / sp.pi)  # lambda^2, with psi = lambda * xi
check(
    "S4c lambda^2 * (1/2) = sqrt(3/(4 pi)) = sqrt((n+1)/S), n=2, S=4 pi",
    sp.simplify(lam_sq / 2 - sp.sqrt(sp.Integer(3) / (4 * sp.pi))) == 0,
)
print(
    "     normalised doublet psi = lambda * xi, lambda = (3/pi)^(1/4) on |xi| = 1 (lambda^2 =",
    lam_sq,
    ")",
)


# ---------------------------------------------------------------- Stage 5: ladder operators
def D_A(a, f):
    """Convention A (note of 29 Oct): D_a = -1/2 (sigma_a xi).d + 1/2 (sigma_a* xibar).dbar."""
    s = sig[a]
    part1 = sum((s * xi)[k] * sp.diff(f, X[k]) for k in range(2))
    part2 = sum((s.conjugate() * xib)[k] * sp.diff(f, Y[k]) for k in range(2))
    return -sp.Rational(1, 2) * part1 + sp.Rational(1, 2) * part2


def D_B(a, f):
    """Convention B (the correspondent): xi -> g xi, so the generator is +1/2 (sigma_a xi).d - 1/2 (sigma_a* xibar).dbar."""
    s = sig[a]
    part1 = sum((s * xi)[k] * sp.diff(f, X[k]) for k in range(2))
    part2 = sum((s.conjugate() * xib)[k] * sp.diff(f, Y[k]) for k in range(2))
    return sp.Rational(1, 2) * part1 - sp.Rational(1, 2) * part2


ff = sp.Function("f")(x1, x2, y1, y2)
levi = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (1, 0, 2): -1, (0, 2, 1): -1, (2, 1, 0): -1}
for label, D in (("A", D_A), ("B", D_B)):
    # tangency to S^3: generators preserve |xi|^2
    for a in range(3):
        check(f"S5a[{label}] D{a + 1}(|xi|^2) = 0 (tangent to S^3)", zero(D(a, xi_norm2)))
    # commutators: [D_a, D_b] = s * i * eps_abc D_c; find s
    signs = set()
    for (a, b, c), e in levi.items():
        comm = sp.expand(D(a, D(b, ff)) - D(b, D(a, ff)))
        resid_plus = sp.simplify(comm - I * e * D(c, ff))
        resid_minus = sp.simplify(comm + I * e * D(c, ff))
        if resid_plus == 0:
            signs.add(+1)
        elif resid_minus == 0:
            signs.add(-1)
        else:
            signs.add(0)
    check(
        f"S5b[{label}] commutators [D_a,D_b] = s i eps D_c with a single sign s; signs found = {signs}",
        len(signs) == 1 and 0 not in signs,
    )
    print(f"     convention {label}: [D_a,D_b] = {list(signs)[0]:+d} i eps_abc D_c")
    # D3 weights on the coordinates
    w = [
        sp.simplify(D(2, X[0]) / X[0]),
        sp.simplify(D(2, X[1]) / X[1]),
        sp.simplify(D(2, Y[0]) / Y[0]),
        sp.simplify(D(2, Y[1]) / Y[1]),
    ]
    print(f"     convention {label}: D3 weights on (xi1, xi2, conj xi1, conj xi2) = {w}")

# Ladder operators on the normalised doublet psi = lambda * xi
lam = sp.symbols("lambda", positive=True)
psi = [lam * x1, lam * x2]
for label, D in (("A", D_A), ("B", D_B)):
    Lp = [sp.expand(D(0, p) + I * D(1, p)) for p in psi]
    Lm = [sp.expand(D(0, p) - I * D(1, p)) for p in psi]
    print(f"     convention {label}: (D1 + i D2) psi = {[sp.simplify(e) for e in Lp]}")
    print(f"     convention {label}: (D1 - i D2) psi = {[sp.simplify(e) for e in Lm]}")

print()
print("FAILS:", fails if fails else "none")
