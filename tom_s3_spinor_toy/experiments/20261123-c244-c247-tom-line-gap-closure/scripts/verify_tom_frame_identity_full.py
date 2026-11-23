"""Operator identity (critic's condition 1), numeric, all test fields incl. the j=3/2 sector (degree 3).

Claim:  (D0 - I) applied to the lift F(g) = g^dag psi(pi(g)), mapped back by G(g) = g (D0 - I)F,
equals c * (D_W psi)(pi(g)) with  D_W psi = U W D_loc (W^{-1} U^dag psi),  W = diag(e^{i pi/4}, e^{-i pi/4}).
Expected: c = 2i for every field; residual at machine precision; with W = identity it must FAIL.

Speed: symbolic expressions are lambdified; no sympy subs in the point loop.
Point sampling: uniform on S^3 with no pole filter (the earlier dead `or True` condition is removed;
the poles of the S^2 frame are included on purpose and are reported by distance to the pole).
"""

import pathlib

import numpy as np
import sympy as sp

x = sp.symbols("x0:4", real=True)
n = sp.symbols("n0:3", real=True)
th, ph = sp.symbols("theta phi", real=True)
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

U = sp.diag(sp.exp(-I * ph / 2), sp.exp(I * ph / 2)) * (
    sp.cos(th / 2) * sp.eye(2) - I * sp.sin(th / 2) * sig[1]
)
Ud = U.H
sphere_sub = {n[0]: sp.sin(th) * sp.cos(ph), n[1]: sp.sin(th) * sp.sin(ph), n[2]: sp.cos(th)}
Wrot = sp.diag(sp.exp(I * sp.pi / 4), sp.exp(-I * sp.pi / 4))


def Dloc(c):
    return sig[0] * (c.diff(th) + sp.cos(th) / (2 * sp.sin(th)) * c) + sig[1] * (
        c.diff(ph) / sp.sin(th)
    )


def DW_expr(psi_n, W):
    psi = psi_n.subs(sphere_sub)
    chi = Ud * psi
    return U * W * Dloc(W.H * chi)


fields = {
    "deg0 (1,0)": sp.Matrix([1, 0]),
    "deg1 (-n_z, -(n_x+i n_y))": sp.Matrix([-n[2], -(n[0] + I * n[1])]),
    "deg1 (n_x, n_y)": sp.Matrix([n[0], n[1]]),
    "deg2 (n_z^2, n_x n_z)": sp.Matrix([n[2] ** 2, n[0] * n[2]]),
    "deg2 (n_x^2-n_y^2, i n_x n_y)": sp.Matrix([n[0] ** 2 - n[1] ** 2, I * n[0] * n[1]]),
    "deg3 (n_z^3-n_z, n_x n_z^2 + i n_y)": sp.Matrix(
        [n[2] ** 3 - n[2], n[0] * n[2] ** 2 + I * n[1]]
    ),
    "deg3 (n_x^3, i n_y^3)": sp.Matrix([n[0] ** 3, I * n[1] ** 3]),
}

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


rng = np.random.default_rng(21)
M_pts = 80
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
tn = np.arccos(np.clip(nv[:, 2], -1, 1))
pn = np.arctan2(nv[:, 1], nv[:, 0])
pole_dist = np.minimum(tn, np.pi - tn)

results = []
for name, psi_n in fields.items():
    psi_x = psi_n.subs({n[i]: nvec[i] for i in range(3)}).applyfunc(sp.expand)
    F = (g.H * psi_x).applyfunc(sp.expand)
    G = (g * D0minusI(F)).applyfunc(sp.expand)
    Gf = [sp.lambdify(x, G[i], "numpy") for i in range(2)]
    Gv = np.stack(
        [np.broadcast_to(np.array(Gf[i](*pts.T), dtype=complex), (M_pts,)) for i in range(2)],
        axis=1,
    )
    for label, W in [("W=rot(pi/2)", Wrot), ("W=id", sp.eye(2))]:
        Dexpr = DW_expr(psi_n, W)
        Df = [sp.lambdify((th, ph), Dexpr[i], "numpy") for i in range(2)]
        Dv = np.stack(
            [np.broadcast_to(np.array(Df[i](tn, pn), dtype=complex), (M_pts,)) for i in range(2)],
            axis=1,
        )
        Gm = Gv.reshape(-1)
        Dm = Dv.reshape(-1)
        c = np.vdot(Dm, Gm) / np.vdot(Dm, Dm) if np.vdot(Dm, Dm) != 0 else 0
        res = float(np.max(np.abs(Gm - c * Dm)))
        results.append((name, label, c, res, float(pole_dist.min())))
        print(
            f"{name:40s} {label:12s}: c = {np.round(c, 6)}, residual {res:.2e}  (min distance to pole {pole_dist.min():.3f})",
            flush=True,
        )

out = pathlib.Path(__file__).with_name("results_frame_identity_full.txt")
out.write_text(
    "\n".join(
        f"{a} | {b} | c={c} | residual={r:.3e} | min_pole_dist={p:.3f}" for a, b, c, r, p in results
    )
    + "\n",
    encoding="utf-8",
)
print("done", flush=True)
