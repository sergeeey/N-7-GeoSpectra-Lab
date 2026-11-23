"""Test of the closed form derived analytically for the weight-0 sector:

    T^{-1} (D0 - I) T  =  2 (1 + sigma . L)       with L = -i x cross grad (orbital, ambient, on S^2),
    equivalently  T^{-1} D0 T = 3 + 2 sigma . L   on the total-weight-0 sector.

T: psi -> F(g) = g^dag psi(pi(g)),  T^{-1}: F -> G(n) = g F(g) (n = pi(g)).
Here G is computed from (D0 - I)F symbolically; the right side is evaluated on the same fields.
Fields: C^2-valued polynomials in n of degree 0..3 (restricted to S^2; L is tangent, so the extension does not matter).
Negative control: 2 (1 - sigma . L) must FAIL.
"""

import pathlib

import numpy as np
import sympy as sp

x = sp.symbols("x0:4", real=True)
n = sp.symbols("n0:3", real=True)
I = sp.I
A = [
    sp.eye(2),
    sp.Matrix([[0, I], [I, 0]]),
    sp.Matrix([[0, -1], [1, 0]]),
    sp.Matrix([[I, 0], [0, -I]]),
]
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
g = x[0] * A[0] + x[1] * A[1] + x[2] * A[2] + x[3] * A[3]
C = -1
g_s3 = g * sig[2] * g.H
nvec = [sp.expand(sp.Rational(1, 2) * (sig[i] * g_s3).trace()) for i in range(3)]


def XR(a, f):
    M = g * (C * I * sig[a])
    m = [sp.expand((M * A[j].H).trace() / 2) for j in range(4)]
    return sp.expand(sum(m[j] * sp.diff(f, x[j]) for j in range(4)))


def D0minusI(F):
    out = sp.zeros(2, 1)
    for a in range(3):
        XF = sp.Matrix([XR(a, F[0]), XR(a, F[1])])
        out += -I * sig[a] * XF
    return (out - F).applyfunc(sp.expand)


def sigL(psi):
    """(sigma . L) psi with L = -i x cross grad acting on ambient functions of n (tangent, extension-independent)."""
    out = sp.zeros(2, 1)
    for k in range(3):
        Lk = sp.zeros(2, 1)
        for i in range(3):
            for j in range(3):
                eps = sp.LeviCivita(k, i, j)
                if eps != 0:
                    Lk += -I * eps * n[i] * psi.applyfunc(lambda e, j=j: sp.diff(e, n[j]))
        out += sig[k] * Lk
    return out.applyfunc(sp.expand)


fields = {
    "deg0 (1,0)": sp.Matrix([1, 0]),
    "deg1 (-n_z, -(n_x+i n_y))": sp.Matrix([-n[2], -(n[0] + I * n[1])]),
    "deg1 (n_x, n_y)": sp.Matrix([n[0], n[1]]),
    "deg2 (n_z^2, n_x n_z)": sp.Matrix([n[2] ** 2, n[0] * n[2]]),
    "deg2 (n_x^2-n_y^2, i n_x n_y)": sp.Matrix([n[0] ** 2 - n[1] ** 2, I * n[0] * n[1]]),
    "deg3 (n_z^3-n_z, n_x n_z^2 + i n_y)": sp.Matrix(
        [n[2] ** 3 - n[2], n[0] * n[2] ** 2 + I * n[1]]
    ),
}

rng = np.random.default_rng(77)
M_pts = 60
pts = rng.normal(size=(M_pts, 4))
pts /= np.linalg.norm(pts, axis=1, keepdims=True)
S = [np.array(s.tolist(), dtype=complex) for s in sig]
s3 = S[2]


def n_of(p):
    G = (
        p[0] * np.eye(2)
        + p[1] * np.array(A[1].tolist(), dtype=complex)
        + p[2] * np.array(A[2].tolist(), dtype=complex)
        + p[3] * np.array(A[3].tolist(), dtype=complex)
    )
    return np.array([0.5 * np.trace(S[i] @ G @ s3 @ G.conj().T).real for i in range(3)])


nv = np.array([n_of(p) for p in pts])

results = []
non_discriminating = []
for name, psi in fields.items():
    psi_x = psi.subs({n[i]: nvec[i] for i in range(3)}).applyfunc(sp.expand)
    F = (g.H * psi_x).applyfunc(sp.expand)
    G = (g * D0minusI(F)).applyfunc(sp.expand)
    rhs_plus = (2 * (psi + sigL(psi))).applyfunc(sp.expand)
    rhs_minus = (2 * (psi - sigL(psi))).applyfunc(sp.expand)
    Gf = [sp.lambdify(x, G[i], "numpy") for i in range(2)]
    Gv = np.stack(
        [np.broadcast_to(np.array(Gf[i](*pts.T), dtype=complex), (M_pts,)) for i in range(2)],
        axis=1,
    )
    # WHY: on fields with sigma.L psi = 0 (e.g. constants) the two right-hand sides coincide, so the
    # sign-flipped control cannot fail there; such fields are not discriminating and are excluded
    # from the NEG verdict (they still count for the MAIN identity).
    discriminating = (rhs_plus - rhs_minus).applyfunc(sp.simplify) != sp.zeros(2, 1)
    if not discriminating:
        non_discriminating.append(name)
    for label, rhs in [("2(1+sigma.L)", rhs_plus), ("2(1-sigma.L) [NEG]", rhs_minus)]:
        if "NEG" in label and not discriminating:
            label = "2(1-sigma.L) [NEG,n/a]"
        Rf = [sp.lambdify(n, rhs[i], "numpy") for i in range(2)]
        Rv = np.stack(
            [np.broadcast_to(np.array(Rf[i](*nv.T), dtype=complex), (M_pts,)) for i in range(2)],
            axis=1,
        )
        err = float(np.max(np.abs(Gv - Rv)))
        results.append((name, label, err))
        print(f"{name:40s} {label:20s}: max|G - rhs| = {err:.2e}", flush=True)

ok_main = all(e < 1e-10 for nme, lab, e in results if "NEG" not in lab)
ok_neg = all(e > 1e-3 for nme, lab, e in results if "NEG" in lab and "n/a" not in lab)
print("MAIN identity T^-1(D0-I)T = 2(1+sigma.L) holds on all fields:", ok_main, flush=True)
print(
    "NEG control 2(1-sigma.L) fails on all discriminating fields:",
    ok_neg,
    f"(excluded, sigma.L psi = 0: {non_discriminating})",
    flush=True,
)
out = pathlib.Path(__file__).with_name("results_bridge_sigmaL.txt")
out.write_text(
    "\n".join(f"{a} | {b} | err={e:.3e}" for a, b, e in results)
    + f"\nMAIN={ok_main} NEG_FAILS={ok_neg}\n",
    encoding="utf-8",
)
print("done", flush=True)
