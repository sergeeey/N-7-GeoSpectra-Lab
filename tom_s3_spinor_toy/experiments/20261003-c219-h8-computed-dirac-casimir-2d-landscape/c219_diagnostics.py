"""C219 post-hoc diagnostics (Amendment A2, written AFTER the first run failed P1a and P1b)."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "c219", HERE / "c219_computed_casimir_landscape.py"
)
c219 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c219)
g92s = importlib.util.spec_from_file_location(
    "g92", HERE.parent / "20260626-g92-s3-casimir-stabilization" / "g92_s3_casimir.py"
)
g92 = importlib.util.module_from_spec(g92s)
g92s.loader.exec_module(g92)

r3, r6 = 1.3, 1.1
print("D1  T-spread by T-range (cancellation hypothesis)")
for ts in ((0.03, 0.06), (0.06, 0.12, 0.2), (0.12, 0.2, 0.3)):
    zs = [c219.zeta_fp(r3, r6, T=t * min(r3, r6) ** 2)[0] for t in ts]
    print(
        f"  T-args {ts}: zeta={np.round(zs, 12).tolist()}  abs spread={max(zs) - min(zs):.2e}"
    )

print("D2  brute-sum convergence at s=6.3")
zm = c219.zeta_mellin_general_s(r3, r6, 6.3)
for N in (220, 400, 800):
    zb = c219.zeta_brute(r3, r6, 6.3, nmax=N, mmax=N)
    print(f"  N={N}: brute={zb:.12e}  rel diff to Mellin={abs(zm - zb) / zb:.2e}")

print(
    "D3  zeta_FP along rho3=0.986 rho6^2 at G54's quoted points (G54: 1.2 -> -6.5e-4, 1.5 -> +2.0e-4, 1.09 -> -7.98e-4, 0.953 -> -8.63e-4)"
)
for r in (0.7, 0.953, 1.09, 1.2, 1.35, 1.447, 1.5):
    z = c219.zeta_fp(0.986 * r**2, r)[0]
    print(f"  rho6={r:5.3f}: zeta_FP={z:+.4e}")

print(
    "D4  feed G54's FITTED B8,B10 into the same machinery (cause test; T-independence expected to break)"
)
saved = dict(c219.B6)
c219.B6[1], c219.B6[2] = -0.0076, -0.0033
for r in (0.953, 1.09, 1.2, 1.5):
    z = c219.zeta_fp(0.986 * r**2, r)[0]
    print(f"  rho6={r:5.3f}: zeta_FP(G54 fit B8,B10)={z:+.4e}")
rs = np.linspace(0.6, 2.0, 281)
zz = np.array([c219.zeta_fp(0.986 * r**2, r)[0] for r in rs])
sign = np.where(np.diff(np.sign(zz)) != 0)[0]
print(
    "  zero(s):",
    [
        round(float(rs[i] - zz[i] * (rs[i + 1] - rs[i]) / (zz[i + 1] - zz[i])), 4)
        for i in sign
    ],
    " min at",
    float(rs[int(np.argmin(zz))]),
)
c219.B6.clear()
c219.B6.update(saved)

print("D5  refine the landscape minima (L-BFGS, Hessian) for the computed Casimir")
vol = g92.VOL_S3_UNIT * g92.VOL_S6_UNIT


def vtot(x, kappa):
    a, b = x
    if a < 0.3 or b < 0.3 or a > 8 or b > 8:
        return 1e3
    return g92.v_main(a, b) + kappa * c219.zeta_fp(a, b)[0] / (vol * a**3 * b**6)


def hess(x, kappa, h=2e-3):
    f = lambda a, b: vtot((a, b), kappa)
    a, b = x
    return np.array(
        [
            [
                (f(a + h, b) - 2 * f(a, b) + f(a - h, b)) / h**2,
                (f(a + h, b + h) - f(a + h, b - h) - f(a - h, b + h) + f(a - h, b - h))
                / (4 * h**2),
            ],
            [0, (f(a, b + h) - 2 * f(a, b) + f(a, b - h)) / h**2],
        ]
    )


for kappa, x0 in (
    (-1.0, (0.62, 1.27)),
    (-0.25, (0.53, 1.27)),
    (-0.05, (0.45, 1.27)),
    (-42.6, (1.09, 1.57)),
):
    res = minimize(
        vtot,
        x0,
        args=(kappa,),
        method="Nelder-Mead",
        options={"xatol": 1e-6, "fatol": 1e-16, "maxiter": 4000},
    )
    H = hess(res.x, kappa)
    H[1, 0] = H[0, 1]
    ev = np.linalg.eigvalsh(H)
    print(
        f"  kappa={kappa:+.2f}: x={np.round(res.x, 4).tolist()}  V={res.fun:.3e}  Hessian eig={np.round(ev, 12).tolist()}  PD={bool(np.all(ev > 0))}"
    )
