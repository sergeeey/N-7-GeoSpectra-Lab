"""Exact-norm check of the leak from H2 = span{Psi, Phi} under A = T^-1 (D0 - I) T = 2(1 + sigma.L) (C = -1).

Claims checked:
  (a) H2 lies in the j = 1/2 block (l = 0 and l = 1), where A^2 = 4, so A^2 Psi = 4 Psi and A^2 Phi = 4 Phi.
  (b) L^2 norms (measure dn on unit S^2): ||A Psi|| = 2 ||Psi||, ||A Phi|| = 2 ||Phi||.
  (c) A(H2) is orthogonal to H2 in L^2: <A Psi, Psi> = <A Psi, Phi> = <A Phi, Psi> = <A Phi, Phi> = 0.
  (d) A is symmetric in L^2: <A Psi, Phi> = <Psi, A Phi>.
L^2 integrals use Gauss-Legendre in u = cos(theta) and a uniform grid in phi (exact for these fields).
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


def A(F):
    return 2 * (F + sx * comp(Lx, F) + sy * comp(Ly, F) + sz * comp(Lz, F))


Psi = sp.Matrix([-(1 - sp.cos(th)) / 2, sp.exp(I * ph) * sp.sin(th) / 2])
Phi = Jm(Psi)
APsi = A(Psi)
APhi = A(Phi)
A2Psi = A(APsi)
A2Phi = A(APhi)

M_u = 48
M_p = 64
u_nodes, u_w = np.polynomial.legendre.leggauss(M_u)
phi_nodes = np.linspace(0.0, 2 * np.pi, M_p, endpoint=False)
phi_w = 2 * np.pi / M_p
U, P = np.meshgrid(u_nodes, phi_nodes, indexing="ij")
W = np.outer(u_w, np.full(M_p, phi_w))
TH = np.arccos(U)
PH = P


def grid(vec):
    out = []
    for i in range(2):
        f = sp.lambdify((th, ph), vec[i], "numpy")
        out.append(np.broadcast_to(np.array(f(TH, PH), dtype=complex), TH.shape))
    return np.stack(out, axis=-1)


def inner(a, b):
    return np.sum(W[..., None] * np.conj(a) * b)


Psi_g = grid(Psi)
Phi_g = grid(Phi)
APsi_g = grid(APsi)
APhi_g = grid(APhi)
A2Psi_g = grid(A2Psi)
A2Phi_g = grid(A2Phi)

lines = []
lines.append(
    f"(a) max|A^2 Psi - 4 Psi| = {np.max(np.abs(A2Psi_g - 4 * Psi_g)):.2e}, "
    f"max|A^2 Phi - 4 Phi| = {np.max(np.abs(A2Phi_g - 4 * Phi_g)):.2e}"
)

nPsi = np.sqrt(inner(Psi_g, Psi_g).real)
nPhi = np.sqrt(inner(Phi_g, Phi_g).real)
nAPsi = np.sqrt(inner(APsi_g, APsi_g).real)
nAPhi = np.sqrt(inner(APhi_g, APhi_g).real)
lines.append(
    f"(b) ||A Psi||/||Psi|| = {nAPsi / nPsi:.12f}, ||A Phi||/||Phi|| = {nAPhi / nPhi:.12f}"
)

cross = {
    "<A Psi, Psi>": inner(APsi_g, Psi_g),
    "<A Psi, Phi>": inner(APsi_g, Phi_g),
    "<A Phi, Psi>": inner(APhi_g, Psi_g),
    "<A Phi, Phi>": inner(APhi_g, Phi_g),
}
lines.append("(c) " + ", ".join(f"{k} = {abs(v):.2e}" for k, v in cross.items()))

sym1 = inner(APsi_g, Phi_g)
sym2 = inner(Psi_g, APhi_g)
lines.append(
    f"(d) <A Psi, Phi> = {sym1:.6f}, <Psi, A Phi> = {sym2:.6f}, difference = {abs(sym1 - sym2):.2e}"
)

ok = (
    np.max(np.abs(A2Psi_g - 4 * Psi_g)) < 1e-10
    and np.max(np.abs(A2Phi_g - 4 * Phi_g)) < 1e-10
    and abs(nAPsi / nPsi - 2) < 1e-10
    and abs(nAPhi / nPhi - 2) < 1e-10
    and max(abs(v) for v in cross.values()) < 1e-10
    and abs(sym1 - sym2) < 1e-10
)
lines.append(f"RESULT: {ok}")
text = "\n".join(lines) + "\n"
print(text, flush=True)
out = pathlib.Path(__file__).with_name("results_H2_j12_block.txt")
out.write_text(text, encoding="utf-8")
