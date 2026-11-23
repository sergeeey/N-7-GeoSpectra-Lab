import random
import sys

sys.path.insert(0, sys.argv[1])
import sympy as sp
from kosmann_geometry import (
    NM,
    NP,
    E,
    I,
    Q,
    T,
    a,
    bracket,
    cliff,
    kos_matrix,
    kosmann,
    nabla_spin,
    nabla_vec,
    omega,
    t,
)

C = {id(N): sp.simplify(omega(N) + kos_matrix(N)) for N in NP + NM}


def J(N, psi):
    d = sp.Matrix(
        [sum(N[j] * sp.diff(psi[r], Q[j]) for j in range(3)) for r in range(2)]
    )
    return -I * (d + C[id(N)] * psi)


def lad(Ns, s, psi):
    return J(Ns[0], psi) + s * I * J(Ns[1], psi)


ph = sp.exp(I * (t - T) / 2)
plus = ph * sp.Matrix([sp.cos(a / 2), -I * sp.sin(a / 2)])
minus_claim = sp.conjugate(ph) * sp.Matrix([-I * sp.sin(a / 2), sp.cos(a / 2)])
random.seed(99)
pts = [
    {a: random.uniform(0.05, 1.52), t: random.uniform(-7, 7), T: random.uniform(-7, 7)}
    for _ in range(40)
]


def mx(M):
    return max(abs(complex(sp.N(c.subs(p), 30))) for p in pts for c in M)


# A1: full-angle exact check via rewrite to exp and simplify
def exact(M):
    return [sp.simplify(sp.expand(sp.simplify(c.rewrite(sp.exp)))) for c in M]


mjm = lad(NP, -1, plus)
print("J-^R plus vs claimed minus (40 pts):", mx(mjm - minus_claim))
for nm, M in [
    ("JR+ plus", lad(NP, +1, plus)),
    ("JR3 plus-1/2", J(NP[2], plus) - plus / 2),
    ("JL plus", sp.Matrix.vstack(*[J(N, plus) for N in NM])),
    ("JL minus", sp.Matrix.vstack(*[J(N, minus_claim) for N in NM])),
    ("JR- minus", lad(NP, -1, minus_claim)),
    ("JR+ minus - plus", lad(NP, +1, minus_claim) - plus),
    ("JR3 minus+1/2", J(NP[2], minus_claim) + minus_claim / 2),
]:
    print(nm, "num40:", mx(M), " exact:", exact(M))
# A2: Clifford compat for all frame vectors + random vector, s=+1
PSI = sp.Matrix(
    [sp.sin(a) * sp.cos(t) + I * a * T, sp.exp(I * T) * sp.cos(a) + t * a**2]
)
Y = [sp.sin(a) * t, sp.cos(T) * a, T * t]
Xr = [sp.cos(T), a * t, sp.sin(t)]
for X in E + [Xr]:
    r = (
        nabla_spin(X, cliff(Y, PSI), 1)
        - cliff(nabla_vec(X, Y), PSI)
        - cliff(Y, nabla_spin(X, PSI, 1))
    )
    print("clifford compat", X, mx(r))
# A3: Kosmann compat with Clifford: L_v(Y.psi) = [v,Y].psi + Y.L_v psi, both Kosmann signs
for sk in (+1, -1):
    w = 0
    for N in NP + NM:
        r = (
            kosmann(N, cliff(Y, PSI), 1, sk)
            - cliff(bracket(N, Y), PSI)
            - cliff(Y, kosmann(N, PSI, 1, sk))
        )
        w = max(w, mx(r))
    print("kosmann clifford-compat s_kos", sk, w)
# A4: Killing spinor at full angles numerically
for nm, psi in (("plus", plus), ("minus", minus_claim)):
    w = max(mx(nabla_spin(E[j], psi, 1) + I / 2 * cliff(E[j], psi)) for j in range(3))
    print("Killing mu=-i/2", nm, w)
