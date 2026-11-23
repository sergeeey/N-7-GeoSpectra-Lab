"""C249 shared geometry: unit S^3 in Hopf coordinates, Hopf frame, spin connection, Kosmann derivative.

x = (sin a cos t, sin a sin t, cos a sin T, cos a cos T); frame E = (d_a, d_t / sin a, d_T / cos a).
Sign choices S_CONN and S_KOS are fixed by the tests in kosmann_checks.py (both signs are tested there).
"""

import sympy as sp

a, t, T = sp.symbols("alpha theta thetat", real=True)
Q = [a, t, T]
I = sp.I
X4 = sp.Matrix(
    [
        sp.sin(a) * sp.cos(t),
        sp.sin(a) * sp.sin(t),
        sp.cos(a) * sp.sin(T),
        sp.cos(a) * sp.cos(T),
    ]
)
JAC = X4.jacobian(Q)
G = sp.simplify(JAC.T * JAC)
GINV = sp.simplify(G.inv())
GAM = [
    [
        [
            sp.simplify(
                sum(
                    GINV[i, m]
                    * (
                        sp.diff(G[m, j], Q[k])
                        + sp.diff(G[m, k], Q[j])
                        - sp.diff(G[j, k], Q[m])
                    )
                    for m in range(3)
                )
                / 2
            )
            for k in range(3)
        ]
        for j in range(3)
    ]
    for i in range(3)
]
SIG = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
E = [[1, 0, 0], [0, 1 / sp.sin(a), 0], [0, 0, 1 / sp.cos(a)]]


def gdot(X, Y):
    return sum(G[i, j] * X[i] * Y[j] for i in range(3) for j in range(3))


def nabla_vec(X, Y):
    return [
        sum(X[j] * sp.diff(Y[i], Q[j]) for j in range(3))
        + sum(GAM[i][j][k] * X[j] * Y[k] for j in range(3) for k in range(3))
        for i in range(3)
    ]


def bivector(coef):
    """(1/4) sum_{b,c} coef(b,c) sigma_b sigma_c."""
    return (
        sum(
            (coef(b, c) * SIG[b] * SIG[c] for b in range(3) for c in range(3)),
            sp.zeros(2, 2),
        )
        / 4
    )


def omega(X):
    return bivector(lambda b, c: gdot(nabla_vec(X, E[c]), E[b]))


def vf(X, psi):
    return sp.Matrix(
        [sum(X[j] * sp.diff(psi[r], Q[j]) for j in range(3)) for r in range(2)]
    )


def nabla_spin(X, psi, s_conn):
    return vf(X, psi) + s_conn * omega(X) * psi


def cliff(Y, psi):
    return sum((gdot(Y, E[k]) * SIG[k] for k in range(3)), sp.zeros(2, 2)) * psi


def dirac(psi, s_conn):
    return sum(
        (SIG[k] * nabla_spin(E[k], psi, s_conn) for k in range(3)), sp.zeros(2, 1)
    )


def kos_matrix(v):
    return bivector(lambda b, c: gdot(nabla_vec(E[b], v), E[c]))


def kosmann(v, psi, s_conn, s_kos):
    return nabla_spin(v, psi, s_conn) + s_kos * kos_matrix(v) * psi


def killing(i, j):
    """Ambient rotation K_ij = x_i d_j - x_j d_i (1-based), pulled back to coordinate components."""
    K = sp.zeros(4, 1)
    K[j - 1] += X4[i - 1]
    K[i - 1] -= X4[j - 1]
    return [sp.simplify(c) for c in (GINV * JAC.T * K)]


def add(*vs, w=None):
    w = w or [1] * len(vs)
    return [sp.simplify(sum(wk * v[i] for wk, v in zip(w, vs))) for i in range(3)]


def bracket(X, Y):
    return [
        sp.simplify(
            sum(
                X[j] * sp.diff(Y[i], Q[j]) - Y[j] * sp.diff(X[i], Q[j])
                for j in range(3)
            )
        )
        for i in range(3)
    ]


H = sp.Rational(1, 2)
# self-dual / anti-self-dual combinations; N3^+ = (d_t - d_T)/2, N3^- = (d_t + d_T)/2
NP = [
    add(killing(2, 3), killing(1, 4), w=[H, H]),
    add(killing(3, 1), killing(2, 4), w=[H, H]),
    add(killing(1, 2), killing(3, 4), w=[H, H]),
]
NM = [
    add(killing(2, 3), killing(1, 4), w=[H, -H]),
    add(killing(3, 1), killing(2, 4), w=[H, -H]),
    add(killing(1, 2), killing(3, 4), w=[H, -H]),
]
