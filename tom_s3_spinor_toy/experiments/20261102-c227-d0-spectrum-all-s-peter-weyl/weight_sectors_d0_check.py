"""Exact-structure check of the correspondent's D0 on C^2-valued polynomials on S^3 of degree <= N (C = -1).

Functions: polynomials on R^4 of degree <= N restricted to S^3 = SU(2).
Quotient by (|x|^2 - 1): reduce x3^2 -> 1 - x0^2 - x1^2 - x2^2, so the basis has x3-degree <= 1.
D0 = -i sum_a sigma_a X_a, J_a = X_a + T_a, T_a = -i sigma_a. J3 = X3 + T3.

Prediction (Peter-Weyl; degree-d harmonics = V_{d/2} x V_{d/2}, left multiplicity 2s+1, s = d/2):
  total spin k = s + 1/2 : D0 = -2s,     irrep dim 2s + 2
  total spin k = s - 1/2 : D0 = 2s + 2,  irrep dim 2s      (s >= 1/2)
Each weight m in {-k..k} of each irrep gives (2s+1) states; J3 eigenvalue = -2i m.

Output: full spectrum match, and per-weight spectrum match, plus [D0, J3] = 0 check.
"""

import itertools
import pathlib
from collections import Counter
from fractions import Fraction

import numpy as np
import sympy as sp

N = 3
TOL = 1e-7

x = sp.symbols("x0:4", real=True)
I = sp.I
A = [
    sp.eye(2),
    sp.Matrix([[0, I], [I, 0]]),
    sp.Matrix([[0, -1], [1, 0]]),
    sp.Matrix([[I, 0], [0, -I]]),
]
sig = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
g = x[0] * A[0] + x[1] * A[1] + x[2] * A[2] + x[3] * A[3]
C = -1


def XR(a, f):
    # WHY: d/dt x_j along g -> g e^{tT_a} equals tr(g T_a A_j^dag)/2, since {A_j} is orthonormal.
    M = g * (C * I * sig[a])
    m = [sp.expand((M * A[j].H).trace() / 2) for j in range(4)]
    return sp.expand(sum(m[j] * sp.diff(f, x[j]) for j in range(4)))


def D0(F):
    out = sp.zeros(2, 1)
    for a in range(3):
        XF = sp.Matrix([sp.expand(XR(a, F[0])), sp.expand(XR(a, F[1]))])
        out += -I * sig[a] * XF
    return out.applyfunc(sp.expand)


def J3(F):
    XF = sp.Matrix([sp.expand(XR(2, F[0])), sp.expand(XR(2, F[1]))])
    return (XF - I * sig[2] * F).applyfunc(sp.expand)


BASIS = [
    (c, e)
    for c in range(2)
    for e in itertools.product(range(N + 1), repeat=4)
    if sum(e) <= N and e[3] <= 1
]
IDX = {b: i for i, b in enumerate(BASIS)}


def reduce_x3(f):
    # WHY: the ideal (|x|^2 - 1) is invariant under X_a, so reducing modulo it commutes with D0 and J3.
    f = sp.expand(f)
    while f != 0 and sp.Poly(f, x[3]).degree() >= 2:
        P = sp.Poly(f, x[3])
        d = P.degree()
        c = P.coeff_monomial(x[3] ** d)
        f = sp.expand(
            f - c * x[3] ** d + c * x[3] ** (d - 2) * (1 - x[0] ** 2 - x[1] ** 2 - x[2] ** 2)
        )
    return f


def coords(F):
    vec = np.zeros(len(BASIS), dtype=complex)
    for c in range(2):
        f = reduce_x3(F[c])
        if f == 0:
            continue
        for mon, cf in sp.Poly(f, *x).as_dict().items():
            vec[IDX[(c, mon)]] = complex(sp.N(cf))
    return vec


def matrix_of(op):
    cols = []
    for c, e in BASIS:
        mono = sp.Integer(1)
        for j, p in enumerate(e):
            mono *= x[j] ** p
        F = sp.zeros(2, 1)
        F[c] = mono
        cols.append(coords(op(F)))
    return np.array(cols).T


def predicted():
    full = Counter()
    sector = {}
    for twos in range(N + 1):
        left = twos + 1
        for k, eig in ((Fraction(twos + 1, 2), -twos), (Fraction(twos - 1, 2), twos + 2)):
            if k < 0:
                continue
            dim_k = int(2 * k) + 1
            full[eig] += left * dim_k
            for j in range(dim_k):
                sector.setdefault(float(k - j), Counter())[eig] += left
    return full, sector


def rounded(values):
    return Counter(np.round(np.real(values), 6))


def main():
    D = matrix_of(D0)
    J = matrix_of(J3)
    n = D.shape[0]
    lines = [f"quotient basis dimension (C^2 x degree<={N} mod |x|^2-1) = {n}"]
    lines.append(f"||D0 J3 - J3 D0|| = {np.linalg.norm(D @ J - J @ D):.2e}")

    full_pred, sector_pred = predicted()
    full_num = rounded(np.linalg.eigvals(D))
    full_ok = full_num == Counter({float(k): v for k, v in full_pred.items()})
    lines.append(f"full spectrum numeric : {dict(sorted(full_num.items()))}")
    lines.append(
        f"full spectrum predicted: {dict(sorted((float(k), v) for k, v in full_pred.items()))}"
    )
    lines.append(f"FULL SPECTRUM MATCH: {full_ok}")

    m_vals = np.round(2 * ((1j * np.linalg.eigvals(J)) / 2).real) / 2
    sectors_num = {}
    for m in sorted(set(m_vals.tolist())):
        lam = -2j * m
        _, S, Vh = np.linalg.svd(J - lam * np.eye(n))
        V = Vh.conj().T[:, S < TOL]
        if V.shape[1] == 0:
            continue
        R = np.linalg.lstsq(V, D @ V, rcond=None)[0]
        resid = np.linalg.norm(V @ R - D @ V)
        sectors_num[m] = rounded(np.linalg.eigvals(R))
        lines.append(
            f"m={m:+.1f} dim={V.shape[1]} invariance-residual={resid:.1e} "
            f"D0 numeric={dict(sorted(sectors_num[m].items()))}"
        )

    sector_ok = True
    for m, cnt in sectors_num.items():
        pred = sector_pred.get(m, Counter())
        pred_c = Counter({float(k): v for k, v in pred.items()})
        if cnt != pred_c:
            sector_ok = False
        lines.append(f"  m={m:+.1f} predicted={dict(sorted(pred_c.items()))} match={cnt == pred_c}")
    missing = set(sector_pred) - set(sectors_num)
    if missing:
        sector_ok = False
        lines.append(f"predicted weights absent in numeric: {sorted(missing)}")
    lines.append(f"WEIGHT SECTORS MATCH: {sector_ok}")

    text = "\n".join(lines) + "\n"
    print(text, flush=True)
    out = pathlib.Path(__file__).with_name("results_weight_sectors_deg2.txt")
    out.write_text(text, encoding="utf-8")
    print("done", flush=True)


if __name__ == "__main__":
    main()
