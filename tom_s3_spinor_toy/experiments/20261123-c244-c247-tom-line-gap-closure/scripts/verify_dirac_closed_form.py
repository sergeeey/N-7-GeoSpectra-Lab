"""Closed form of the unit-S^2 Dirac operator in the Hopf-section frame (used in the bridge theorem v2).

Claim:  U D_loc U^{-1} = sum_k sigma_k (grad n_k . grad) - Gamma,   Gamma = sigma . n,
with U(theta, phi) = Rz(-phi) Ry(-theta), D_loc = s1 (d_th + cot/2) + s2 d_ph / sin th (unit S^2, frame e_th, e_ph).
Test on explicit C^2-valued fields (20 random points) and a negative control (wrong sign of Gamma must fail).
"""

import pathlib

import numpy as np
import sympy as sp

th, ph = sp.symbols("theta phi", real=True)
I = sp.I
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -I], [I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
one = sp.eye(2)
U = sp.diag(sp.exp(-I * ph / 2), sp.exp(I * ph / 2)) * (
    sp.cos(th / 2) * one - I * sp.sin(th / 2) * s2
)
Ud = U.H
psi = sp.Matrix(
    [
        sp.sin(th) * sp.cos(2 * ph) + sp.cos(th) ** 2 * sp.exp(I * ph),
        sp.cos(3 * th) * sp.sin(ph) + I * sp.sin(th) ** 2 * sp.cos(ph),
    ]
)


def Dloc(c):
    return s1 * (c.diff(th) + sp.cos(th) / (2 * sp.sin(th)) * c) + s2 * (c.diff(ph) / sp.sin(th))


ambient = U * Dloc(Ud * psi)
n = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
Gam = n[0] * s1 + n[1] * s2 + n[2] * s3


def closed(sign_gamma):
    out = sp.zeros(2, 1)
    for k, sk in enumerate([s1, s2, s3]):
        f = n[k]
        out += sk * (
            sp.diff(f, th) * psi.diff(th) + sp.diff(f, ph) * psi.diff(ph) / sp.sin(th) ** 2
        )
    return out - sign_gamma * Gam * psi


rng = np.random.default_rng(1)
pts = []
while len(pts) < 20:
    t, p = rng.uniform(0.3, np.pi - 0.3), rng.uniform(0, 2 * np.pi)
    pts.append((t, p))

amb_f = sp.lambdify((th, ph), ambient, "numpy")
ok_f = sp.lambdify((th, ph), closed(+1), "numpy")
neg_f = sp.lambdify((th, ph), closed(-1), "numpy")
err = 0.0
err_neg = 0.0
for t, p in pts:
    a = np.array(amb_f(t, p), dtype=complex).reshape(2)
    b = np.array(ok_f(t, p), dtype=complex).reshape(2)
    c = np.array(neg_f(t, p), dtype=complex).reshape(2)
    err = max(err, float(np.max(np.abs(a - b))))
    err_neg = max(err_neg, float(np.max(np.abs(a - c))))

print(
    f"closed form U D_loc U^-1 = sum sigma_k grad n_k . grad - Gamma: max error {err:.2e} (20 points)",
    flush=True,
)
print(f"NEG control (+Gamma instead of -Gamma) max error {err_neg:.2e} (must be large)", flush=True)
ok = err < 1e-12 and err_neg > 1e-3
print("RESULT:", ok, flush=True)
out = pathlib.Path(__file__).with_name("results_dirac_closed_form.txt")
out.write_text(
    f"closed_form_error={err:.3e} neg_error={err_neg:.3e} RESULT={ok}\n", encoding="utf-8"
)
