"""Extension of verify_dirac_closed_form.py after a blind review (2026-11-23).

The original script tested the closed form  U D_loc U^-1 = sum_k sigma_k (grad n_k . grad) - Gamma
on ONE field and never asserted the link Omega = exp(i pi Gamma/4) = U W U^dagger with
W = exp(i pi sigma_3/4). This script (a) repeats the closed-form test on four further fields, with
the +Gamma control on each, and (b) asserts U sigma_3 U^dagger = Gamma and
U W U^dagger = (1 + i Gamma)/sqrt(2) = exp(i pi Gamma/4) exactly (sympy).
"""

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
n = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
Gam = n[0] * s1 + n[1] * s2 + n[2] * s3


def dloc(c):
    return s1 * (c.diff(th) + sp.cos(th) / (2 * sp.sin(th)) * c) + s2 * (c.diff(ph) / sp.sin(th))


def closed(psi, sign_gamma):
    out = sp.zeros(2, 1)
    for k, sk in enumerate([s1, s2, s3]):
        f = n[k]
        out += sk * (
            sp.diff(f, th) * psi.diff(th) + sp.diff(f, ph) * psi.diff(ph) / sp.sin(th) ** 2
        )
    return out - sign_gamma * Gam * psi


fields = {
    "hopf doublet (cos th, sin th e^{i phi})": sp.Matrix([sp.cos(th), sp.sin(th) * sp.exp(I * ph)]),
    "(e^{-i phi} sin^2 th, cos th sin th e^{2 i phi})": sp.Matrix(
        [sp.exp(-I * ph) * sp.sin(th) ** 2, sp.cos(th) * sp.sin(th) * sp.exp(2 * I * ph)]
    ),
    "(n_x + i n_y, n_z)": sp.Matrix([n[0] + I * n[1], n[2]]),
    "(1, i cos(2 th) e^{-i phi})": sp.Matrix([1, I * sp.cos(2 * th) * sp.exp(-I * ph)]),
}

rng = np.random.default_rng(7)
pts = [(rng.uniform(0.3, np.pi - 0.3), rng.uniform(0, 2 * np.pi)) for _ in range(20)]
all_ok = True
for name, psi in fields.items():
    amb = sp.lambdify((th, ph), U * dloc(Ud * psi), "numpy")
    good = sp.lambdify((th, ph), closed(psi, +1), "numpy")
    ctrl = sp.lambdify((th, ph), closed(psi, -1), "numpy")
    e_ok = e_ctrl = 0.0
    for t, p in pts:
        a = np.array(amb(t, p), dtype=complex).reshape(2)
        e_ok = max(e_ok, float(np.max(np.abs(a - np.array(good(t, p), dtype=complex).reshape(2)))))
        e_ctrl = max(
            e_ctrl, float(np.max(np.abs(a - np.array(ctrl(t, p), dtype=complex).reshape(2))))
        )
    ok = e_ok < 1e-12 and e_ctrl > 1e-3
    all_ok = all_ok and ok
    print(f"{name}: closed-form error {e_ok:.2e}, +Gamma control error {e_ctrl:.2e}, ok={ok}")

# Omega link: exact (half-angle substitution theta = 2 half, then expand_trig + simplify; plain
# simplify() does not close these trigonometric identities) and numeric (200 random points)
half = sp.symbols("half", real=True)


def exact_zero(expr_matrix):
    sub = expr_matrix.subs(th, 2 * half)
    red = sub.applyfunc(
        lambda e: sp.simplify(sp.expand(sp.expand_trig(sp.expand(e.rewrite(sp.exp)))))
    )
    return red == sp.zeros(2, 2)


W = sp.cos(sp.pi / 4) * one + I * sp.sin(sp.pi / 4) * s3  # exp(i pi sigma_3 / 4)
omega = sp.cos(sp.pi / 4) * one + I * sp.sin(sp.pi / 4) * Gam  # exp(i pi Gamma/4), Gamma^2 = 1
link_checks = {
    "U sigma_3 U^dagger = Gamma": U * s3 * Ud - Gam,
    "U W U^dagger = exp(i pi Gamma/4)": U * W * Ud - omega,
    "Gamma^2 = 1": Gam * Gam - one,
}
link_ok = True
for label, mat in link_checks.items():
    ex = exact_zero(mat)
    fn = sp.lambdify((th, ph), mat, "numpy")
    worst = max(
        float(np.max(np.abs(np.array(fn(a, b), dtype=complex))))
        for a, b in zip(rng.uniform(0, np.pi, 200), rng.uniform(0, 2 * np.pi, 200), strict=True)
    )
    link_ok = link_ok and ex and worst < 1e-12
    print(f"{label}: exact zero = {ex}, numeric worst over 200 points = {worst:.2e}")
print("RESULT:", all_ok and link_ok)
