"""Q3 point corrections, checked numerically.
  C1. Within one CP^1 subspace (fixed [a:b]): <Psi_v,Psi_w> = 4 pi(|a|^2+|b|^2)<v,w>  (orthogonal basis of one multiplet).
      Between two subspaces [a:b] and [a':b']: <Psi^{ab}_v,Psi^{a'b'}_w> = 4 pi (conj(a) a' + conj(b) b') <v,w>.
      So two subspaces are orthogonal iff conj(a)a' + conj(b)b' = 0 (not automatic).
  C2. (1,1) and (1,-1) (Bloch +n and -n) are orthogonal subspaces; (1,0) and (0,1) too.
"""
import numpy as np

rng = np.random.default_rng(5)
xg, wg = np.polynomial.legendre.leggauss(60)
phg = np.linspace(0, 2 * np.pi, 60, endpoint=False)
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]


def M(a, b, n):
    return a * np.eye(2) + b * (n[0] * sig[0] + n[1] * sig[1] + n[2] * sig[2])


def inner(a1, b1, a2, b2, v, w):
    tot = 0j
    for x, wi in zip(xg, wg):
        th = np.arccos(x)
        for p in phg:
            n = np.array([np.sin(th) * np.cos(p), np.sin(th) * np.sin(p), np.cos(th)])
            tot += wi * (2 * np.pi / 60) * np.vdot(M(a1, b1, n) @ v, M(a2, b2, n) @ w)
    return tot


fails = []
for trial in range(3):
    a1, b1, a2, b2 = rng.normal(size=4) + 1j * rng.normal(size=4)
    v, w = rng.normal(size=2) + 1j * rng.normal(size=2), rng.normal(size=2) + 1j * rng.normal(size=2)
    got = inner(a1, b1, a2, b2, v, w)
    pred = 4 * np.pi * (np.conj(a1) * a2 + np.conj(b1) * b2) * np.vdot(v, w)
    ok = abs(got - pred) / (abs(pred) + 1e-30) < 1e-10
    print(("PASS " if ok else "FAIL ") + "C1 cross-subspace inner product = 4pi(conj(a)a'+conj(b)b')<v,w> (trial %d)" % trial)
    if not ok:
        fails.append(trial)
    same = inner(a1, b1, a1, b1, v, w)
    ok2 = abs(same - 4 * np.pi * (abs(a1) ** 2 + abs(b1) ** 2) * np.vdot(v, w)) < 1e-9
    print(("PASS " if ok2 else "FAIL ") + "C1 within one subspace: 4pi(|a|^2+|b|^2)<v,w> (trial %d)" % trial)
    if not ok2:
        fails.append(("within", trial))

# C2 Bloch +n (a=b=1) and -n (a=1,b=-1): orthogonal subspaces
v, w = np.array([1, 0.3j]), np.array([0.2, 1])
o = inner(1, 1, 1, -1, v, w)
print(("PASS " if abs(o) < 1e-10 else "FAIL ") + "C2 Bloch +n and -n subspaces are orthogonal (|<.,.>| = %.1e)" % abs(o))
if abs(o) >= 1e-10:
    fails.append("C2")
print("\nFAILS:", fails if fails else "none")
