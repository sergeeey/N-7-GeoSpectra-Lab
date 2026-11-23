"""C249 diagnostic: rank of the highest-weight system for each half-integer phase (p, q).

psi = e^{i(p theta + q thetat)} (A, B); conditions: J3 eigenvalues fixed by (p, q), plus the ladder
conditions of a highest weight (or singlet) for both SU(2)s. Unknowns (A, B, A', B') at fixed alpha.
Null-space dimension > 0 at generic alpha means a non-zero local solution of the first-order system.
"""

import sys

import sympy as sp

# WHY: python -I (used by tom_line_check --run) drops the script folder from sys.path
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from kosmann_geometry import NM, NP, I, Q, T, a, kos_matrix, omega, t

C = {id(N): sp.simplify(omega(N) + kos_matrix(N)) for N in NP + NM}
A, B, Ap, Bp = sp.symbols("A B Ap Bp")
fA, fB = sp.Function("fA")(a), sp.Function("fB")(a)


def J(N, psi, spinor=True):
    d = sp.Matrix(
        [sum(N[j] * sp.diff(psi[r], Q[j]) for j in range(3)) for r in range(2)]
    )
    return -I * (d + C[id(N)] * psi) if spinor else -I * d


def ladder(Ns, s, psi, spinor=True):
    return J(Ns[0], psi, spinor) + s * I * J(Ns[1], psi, spinor)


ANG = [
    (0, 0),
    (sp.pi / 2, 0),
    (0, sp.pi / 2),
    (sp.pi / 3, sp.pi / 7),
    (sp.pi / 5, 2 * sp.pi / 3),
]
H = sp.Rational(1, 2)
for spinor in (True, False):
    for p, q in ((H, -H), (H, H), (-H, H), (-H, -H), (0, 0)):
        ph = sp.exp(I * (p * t + q * T))
        psi = ph * sp.Matrix([fA, fB if spinor else 0])
        jl3, jr3 = (p + q) / 2, (p - q) / 2
        # highest weight in each factor: J_+ psi = 0; a singlet also needs J_- psi = 0
        conds = [(NP, +1), (NM, +1)]
        if jl3 == 0:
            conds.append((NM, -1))
        if jr3 == 0:
            conds.append((NP, -1))
        rows = []
        for Ns, s in conds:
            e = (
                (ladder(Ns, s, psi, spinor) / ph)
                .subs({sp.Derivative(fA, a): Ap, sp.Derivative(fB, a): Bp})
                .subs({fA: A, fB: B})
            )
            for th, tt in ANG:
                for comp in e:
                    c = sp.expand(comp.subs({t: th, T: tt, a: sp.Rational(7, 10)}))
                    rows.append([sp.N(c.coeff(v), 30) for v in (A, B, Ap, Bp)])
        M = sp.Matrix(rows)
        if not spinor:
            M = M[:, [0, 2]]
        import numpy as np

        sv = np.linalg.svd(np.array(M.tolist(), dtype=complex), compute_uv=False)
        print(
            f"spinor={spinor} (p,q)=({p},{q}) (jL3,jR3)=({jl3},{jr3})  singular values: "
            + " ".join(f"{x:.2e}" for x in sv)
        )
