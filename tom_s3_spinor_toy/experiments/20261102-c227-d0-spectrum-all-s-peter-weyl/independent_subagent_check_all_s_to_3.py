"""Independent check of D0 = -i sum sigma_a X_a spectrum on harmonic homogeneous degree-k polys on S^3.
Own parametrisation: g = [[a, -conj b],[b, conj a]], a = x0 + i x3, b = x1 + i x2.
X_a f(g) = d/dt f(g exp(t T_a)), T_a = -i sigma_a. No prediction formula used to build anything.
"""

import itertools
from collections import Counter
import numpy as np
import sympy as sp

x = sp.symbols("x0:4", real=True)
I = sp.I
a = x[0] + I * x[3]
b = x[1] + I * x[2]
g = sp.Matrix([[a, -sp.conjugate(b)], [b, sp.conjugate(a)]])
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]


def coords_of_matrix(M):
    # inverse of parametrisation, linear: a = M[0,0], b = M[1,0]
    A_, B_ = sp.expand(M[0, 0]), sp.expand(M[1, 0])
    return [sp.re(A_), sp.re(B_), sp.im(B_), sp.im(A_)]


VEL = []
for s_ in sig:
    v = coords_of_matrix(g * (-I * s_))
    VEL.append([sp.expand(c) for c in v])
# sanity: g T_a must stay in the quaternion form (tangent to SU(2)); check consistency
for k_, s_ in enumerate(sig):
    M = sp.expand(g * (-I * s_))
    assert sp.simplify(M[0, 1] + sp.conjugate(M[1, 0])) == 0
    assert sp.simplify(M[1, 1] - sp.conjugate(M[0, 0])) == 0


def run(k):
    mons = [e for e in itertools.product(range(k + 1), repeat=4) if sum(e) == k]
    idx = {e: i for i, e in enumerate(mons)}
    n = len(mons)

    def vec(f):
        v = np.zeros(n, complex)
        f = sp.expand(f)
        if f == 0:
            return v
        for m, c in sp.Poly(f, *x).as_dict().items():
            v[idx[m]] = complex(c)
        return v

    monos = [sp.Mul(*[x[j] ** e[j] for j in range(4)]) for e in mons]
    X = []
    for aa in range(3):
        cols = [vec(sum(VEL[aa][j] * sp.diff(m, x[j]) for j in range(4))) for m in monos]
        X.append(np.array(cols).T)
    # Laplacian to degree k-2
    if k >= 2:
        mons2 = [e for e in itertools.product(range(k), repeat=4) if sum(e) == k - 2]
        idx2 = {e: i for i, e in enumerate(mons2)}
        L = np.zeros((len(mons2), n))
        for i, m in enumerate(monos):
            lap = sp.expand(sum(sp.diff(m, x[j], 2) for j in range(4)))
            if lap != 0:
                for mm, c in sp.Poly(lap, *x).as_dict().items():
                    L[idx2[mm], i] = float(c)
        _, S, Vh = np.linalg.svd(L)
        r = int((S > 1e-9).sum())
        H = Vh[r:].conj().T
    else:
        H = np.eye(n)
    # D0 on C^2 (x) poly: -i sum sigma_a (x) X_a
    sg = [np.array(s_, dtype=complex) for s_ in sig]
    D = sum(-1j * np.kron(sg[aa], X[aa]) for aa in range(3))
    HH = np.kron(np.eye(2), H)
    R = np.linalg.lstsq(HH, D @ HH, rcond=None)[0]
    res = np.linalg.norm(HH @ R - D @ HH)
    herm = np.linalg.norm(
        R - R.conj().T
    )  # H has orthonormal columns; monomial inner product not L2, so may be non-herm
    ev = np.linalg.eigvals(R)
    return HH.shape[1], res, Counter(np.round(ev.real, 6)), np.abs(ev.imag).max(), herm


for k in range(0, 7):
    dim, res, cnt, im, herm = run(k)
    s = k / 2
    pred = Counter({-2 * s: int((2 * s + 1) * (2 * s + 2))})
    if k >= 1:
        pred[2 * s + 2] = int((2 * s + 1) * (2 * s))
    print(
        f"k={k} s={s} dimH(C^2)={dim} invres={res:.1e} max|Im|={im:.1e} num={dict(sorted(cnt.items()))} pred={dict(pred)} match={cnt == Counter({float(a_): v for a_, v in pred.items()})}"
    )
    # CS check: Dirac on unit S^3: +-(n+3/2), mult (n+1)(n+2)
print("D0-3/2 per k listed; CS: -(2s+3/2) with n=2s, +(2s+1/2) with n=2s-1")
