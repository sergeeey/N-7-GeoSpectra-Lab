import sys

sys.path.insert(0, sys.argv[1])
import sympy as sp
from kosmann_geometry import (
    JAC,
    NM,
    NP,
    SIG,
    X4,
    E,
    I,
    Q,
    T,
    a,
    dirac,
    kos_matrix,
    omega,
    t,
)

C = {id(N): sp.simplify(omega(N) + kos_matrix(N)) for N in NP + NM}
print("traces C_N:", [sp.simplify(C[id(N)].trace()) for N in NP + NM])
print("sig1 sig2 sig3 =", SIG[0] * SIG[1] * SIG[2])
cols = [X4] + [JAC * sp.Matrix(E[k]) for k in range(3)]
print("orientation det:", sp.simplify(sp.Matrix.hstack(*cols).det()))
A, B, Ap, Bp = sp.symbols("A B Ap Bp")


def J(N, psi):
    d = sp.Matrix(
        [sum(N[j] * sp.diff(psi[r], Q[j]) for j in range(3)) for r in range(2)]
    )
    return -I * (d + C[id(N)] * psi)


# guess (1/2,0) highest weight at p=q=1/2 by analogy; solve local null vector then test closed forms
ph = sp.exp(I * (t + T) / 2)
cands = {
    "(cos, i sin)": sp.Matrix([sp.cos(a / 2), I * sp.sin(a / 2)]),
    "(cos,-i sin)": sp.Matrix([sp.cos(a / 2), -I * sp.sin(a / 2)]),
    "(cos, sin)": sp.Matrix([sp.cos(a / 2), sp.sin(a / 2)]),
    "(cos,-sin)": sp.Matrix([sp.cos(a / 2), -sp.sin(a / 2)]),
    "(sin, i cos)": sp.Matrix([sp.sin(a / 2), I * sp.cos(a / 2)]),
    "(i sin, cos)": sp.Matrix([I * sp.sin(a / 2), sp.cos(a / 2)]),
    "(sin,cos)": sp.Matrix([sp.sin(a / 2), sp.cos(a / 2)]),
    "(-sin,cos)": sp.Matrix([-sp.sin(a / 2), sp.cos(a / 2)]),
}
p = {a: 0.63, t: 0.41, T: 1.77}
for nm, v in cands.items():
    psi = ph * v
    conds = sp.Matrix.vstack(
        J(NM[0], psi) + I * J(NM[1], psi),
        *[J(N, psi) for N in NP],
        J(NM[2], psi) - psi / 2,
    )
    r = max(abs(complex(sp.N(c.subs(p)))) for c in conds)
    if r < 1e-10:
        D = dirac(psi, 1)
        lam = complex(sp.N((D[0] / psi[0]).subs(p)))
        w = max(
            abs(complex(sp.N((D - lam * psi)[k].subs(pp))))
            for k in range(2)
            for pp in [p, {a: 1.1, t: -2.0, T: 0.3}]
        )
        print(
            "(1/2,0) highest weight", nm, "residual", r, "D eigen", lam, "eig check", w
        )
