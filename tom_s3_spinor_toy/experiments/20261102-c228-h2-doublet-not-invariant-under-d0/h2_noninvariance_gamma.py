"""Check of the analytic non-invariance argument for H2 = span{Psi, Phi} (S^2 side, C = -1).

Claims checked numerically at random points of S^2:
  (1) Gamma Psi = -Psi,  Gamma Phi = -Phi,  Phi = J_- Psi,  J_- = L_- + S_- (S_- = (sigma_x - i sigma_y)/2).
  (2) [J_-, Gamma] = 0 on a generic test field (so Gamma commutes with the total moment).
  (3) A = D0 - I = 2(1 + sigma.L) satisfies Gamma A psi = A psi for psi = Psi (anticommutation).
  (4) A Psi is NOT in span{Psi, Phi}  (least-squares residual of A Psi on span{Psi, Phi}).
Also sanity: [L_x, L_y] = i L_z on a test scalar (checks the ladder-operator conventions).
"""

import pathlib

import numpy as np
import sympy as sp

th, ph = sp.symbols("theta phi", real=True)
I = sp.I
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
Sm = sp.Matrix([[0, 0], [1, 0]])
n = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
Gam = n[0] * sx + n[1] * sy + n[2] * sz


def Lp(f):
    return sp.exp(I * ph) * (sp.diff(f, th) + I * sp.cos(th) / sp.sin(th) * sp.diff(f, ph))


def Lm(f):
    return sp.exp(-I * ph) * (-sp.diff(f, th) + I * sp.cos(th) / sp.sin(th) * sp.diff(f, ph))


def Lz(f):
    return -I * sp.diff(f, ph)


def Lx(f):
    return (Lp(f) + Lm(f)) / 2


def Ly(f):
    return (Lp(f) - Lm(f)) / (2 * I)


def comp(op, F):
    return sp.Matrix([op(F[0]), op(F[1])])


def Jm(F):
    return comp(Lm, F) + Sm * F


def sigL(F):
    return sx * comp(Lx, F) + sy * comp(Ly, F) + sz * comp(Lz, F)


def A(F):
    return 2 * (F + sigL(F))


Psi = sp.Matrix([-(1 - sp.cos(th)) / 2, sp.exp(I * ph) * sp.sin(th) / 2])
Phi = Jm(Psi)
F_test = sp.Matrix([sp.cos(th) * sp.exp(I * ph), sp.sin(th) * sp.cos(ph) + I * sp.sin(ph)])
s_test = sp.cos(th) * sp.sin(th) * sp.exp(I * ph)

rng = np.random.default_rng(2)
N = 40
pts_th = rng.uniform(0.2, np.pi - 0.2, N)
pts_ph = rng.uniform(0.0, 2 * np.pi, N)


def ev(vec):
    cols = []
    for i in range(2):
        f = sp.lambdify((th, ph), vec[i], "numpy")
        cols.append(np.broadcast_to(np.array(f(pts_th, pts_ph), dtype=complex), (N,)))
    return np.stack(cols, axis=1)


def ev_matrix(M):
    cols = []
    for i in range(2):
        f = sp.lambdify((th, ph), M[i, 0], "numpy")
        cols.append(np.broadcast_to(np.array(f(pts_th, pts_ph), dtype=complex), (N,)))
    return np.stack(cols, axis=1)


GamMat = sp.lambdify((th, ph), Gam, "numpy")


def gamma_apply(F_vals):
    out = np.zeros_like(F_vals)
    for k in range(N):
        G = np.array(GamMat(pts_th[k], pts_ph[k]), dtype=complex)
        out[k] = G @ F_vals[k]
    return out


Psi_v = ev(Psi)
Phi_v = ev(Phi)
APsi = A(Psi)
APsi_v = ev(APsi)

lines = []
e1 = np.max(np.abs(gamma_apply(Psi_v) + Psi_v))
e2 = np.max(np.abs(gamma_apply(Phi_v) + Phi_v))
lines.append(f"(1) |Gamma Psi + Psi| = {e1:.2e},  |Gamma Phi + Phi| = {e2:.2e}")

GF_test = sp.Matrix([sum(Gam[i, j] * F_test[j] for j in range(2)) for i in range(2)])
lhs = ev(Jm(GF_test))
rhs = gamma_apply(ev(Jm(F_test)))
e3 = np.max(np.abs(lhs - rhs))
lines.append(f"(2) |J_-(Gamma F) - Gamma(J_- F)| on generic F = {e3:.2e}")

e4 = np.max(np.abs(gamma_apply(APsi_v) - APsi_v))
lines.append(f"(3) |Gamma A Psi - A Psi| = {e4:.2e}")

M = np.stack([Psi_v.reshape(-1), Phi_v.reshape(-1)], axis=1)
rhs_vec = APsi_v.reshape(-1)
coef, *_ = np.linalg.lstsq(M, rhs_vec, rcond=None)
resid = np.linalg.norm(M @ coef - rhs_vec) / np.linalg.norm(rhs_vec)
lines.append(
    f"(4) relative residual of A Psi on span{{Psi,Phi}} = {resid:.3e} (coefficients {np.round(coef, 4)})"
)

Lcomm = Lx(Ly(s_test)) - Ly(Lx(s_test)) - I * Lz(s_test)
ec = float(np.max(np.abs(ev_matrix(sp.Matrix([[Lcomm, 0], [0, 0]])))))
lines.append(f"sanity [Lx,Ly] - i Lz on test scalar = {ec:.2e} (must be ~0)")

ok = e1 < 1e-10 and e2 < 1e-10 and e3 < 1e-10 and e4 < 1e-10 and resid > 0.1
lines.append(f"RESULT: {ok}")
text = "\n".join(lines) + "\n"
print(text, flush=True)
out = pathlib.Path(__file__).with_name("results_H2_noninvariance_gamma.txt")
out.write_text(text, encoding="utf-8")
