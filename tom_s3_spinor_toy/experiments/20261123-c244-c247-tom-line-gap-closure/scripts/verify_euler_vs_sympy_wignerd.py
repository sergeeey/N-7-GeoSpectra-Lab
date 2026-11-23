"""Positive control against an independent implementation: do the Euler-angle J+/J- (verify_euler_operators.py)
act on sympy's Wigner D-functions with the standard su(2) coefficients?

sympy.physics.quantum.spin.Rotation.D(j, m', k', phi, theta, psi) = <j m'| exp(-i phi Jz) exp(-i theta Jy) exp(-i psi Jz) |j k'>
= e^{-i m' phi} d^j_{m'k'}(theta) e^{-i k' psi}. Our functions are e^{i m phi} e^{i k psi} f(theta), so m = -m', k = -k'.

Prediction (before the run): J+ D(j,-m,-k) = a * D(j,-(m+1),-k) with |a| = sqrt(j(j+1) - m(m+1)), the same number at every
point (a is a constant, possibly with a convention-dependent phase), and J_z = -i d/d phi gives eigenvalue m.
Negative control: the same test with the WRONG extra-term sign (+i/sin(theta) d_psi) must fail for k != 0.
"""

import random

import sympy as sp
from sympy.physics.quantum.spin import Rotation

th, ph, ps = sp.symbols("theta phi psi", real=True)
I = sp.I
random.seed(9)
pts = [
    (random.uniform(0.4, 2.7), random.uniform(0.1, 6.0), random.uniform(0.1, 6.0)) for _ in range(5)
]
R = sp.Rational


def Jp(f, sign=-1):
    return sp.exp(I * ph) * (
        sp.diff(f, th) + I * sp.cot(th) * sp.diff(f, ph) + sign * (I / sp.sin(th)) * sp.diff(f, ps)
    )


def Jm(f, sign=-1):
    return sp.exp(-I * ph) * (
        -sp.diff(f, th) + I * sp.cot(th) * sp.diff(f, ph) + sign * (I / sp.sin(th)) * sp.diff(f, ps)
    )


def D(j, mp, kp):
    return Rotation.D(j, mp, kp, ph, th, ps).doit()


def ev(e, p):
    return complex(sp.N(e.subs({ph: p[1], th: p[0], ps: p[2]}), 25))


def ratio_const(op, j, m, k, target_m, sign):
    """op D(j,-m,-k) vs D(j,-target_m,-k): returns (constant?, value)."""
    src = D(j, -m, -k)
    tgt = D(j, -target_m, -k)
    out = op(src, sign)
    rs = []
    for p in pts:
        t = ev(tgt, p)
        if abs(t) < 1e-8:
            continue
        rs.append(ev(out, p) / t)
    if len(rs) < 3:
        return None, None
    spread = max(abs(r - rs[0]) for r in rs) / max(abs(rs[0]), 1e-30)
    return spread < 1e-8, rs[0]


ok = True
n_checked = 0
for j in (R(1, 2), R(1), R(3, 2)):
    ms = [j - i for i in range(int(2 * j) + 1)]
    for k in ms:
        for m in ms:
            # J_z eigenvalue
            fz = D(j, -m, -k)
            jz = max(abs(ev(-I * sp.diff(fz, ph), p) - m * ev(fz, p)) for p in pts)
            ok &= jz < 1e-9
            n_checked += 1
            if m < j:
                const, a = ratio_const(Jp, j, m, k, m + 1, -1)
                want = sp.sqrt(j * (j + 1) - m * (m + 1))
                good = bool(const) and abs(abs(a) - float(want)) < 1e-8
                ok &= good
                n_checked += 1
                if not good:
                    print(
                        f"FAIL J+ j={j} m={m} k={k}: const={const} |a|={abs(a) if a is not None else None} want={want}"
                    )
            if m > -j:
                const, a = ratio_const(Jm, j, m, k, m - 1, -1)
                want = sp.sqrt(j * (j + 1) - m * (m - 1))
                good = bool(const) and abs(abs(a) - float(want)) < 1e-8
                ok &= good
                n_checked += 1
                if not good:
                    print(
                        f"FAIL J- j={j} m={m} k={k}: const={const} |a|={abs(a) if a is not None else None} want={want}"
                    )
print(f"standard su(2) action on sympy Wigner D: {n_checked} checks, all pass: {ok}")

# negative control: the wrong sign of the d_psi term must fail for some k != 0
fails = 0
tot = 0
for j in (R(1, 2), R(1), R(3, 2)):
    ms = [j - i for i in range(int(2 * j) + 1)]
    for k in ms:
        if k == 0:
            continue
        for m in ms:
            if m < j:
                const, a = ratio_const(Jp, j, m, k, m + 1, +1)
                want = float(sp.sqrt(j * (j + 1) - m * (m + 1)))
                tot += 1
                if not (bool(const) and abs(abs(a) - want) < 1e-8):
                    fails += 1
print(
    f"negative control (wrong sign of d_psi term): fails in {fails} of {tot} cases with k != 0 (must be > 0)"
)
ok &= fails > 0
print("ALL PASS" if ok else "SOME FAILED")
