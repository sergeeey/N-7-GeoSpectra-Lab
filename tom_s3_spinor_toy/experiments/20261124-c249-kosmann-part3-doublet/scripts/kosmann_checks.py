"""C249 P1, P2: fix signs by discriminating tests, then check that the Kosmann derivative commutes with D."""

import json
import random
import sys

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
    dirac,
    kos_matrix,
    kosmann,
    nabla_spin,
    nabla_vec,
    omega,
    t,
    vf,
)

random.seed(20261124)
PTS = [
    (random.uniform(0.2, 1.35), random.uniform(0, 6.28), random.uniform(0, 6.28))
    for _ in range(6)
]
PSI = sp.Matrix(
    [
        sp.sin(a) * sp.cos(t) + I * sp.cos(2 * a) * sp.sin(T) + a * t,
        sp.exp(I * t) * sp.cos(a) + T**2 * sp.sin(a),
    ]
)
Y = [sp.cos(t) * a, sp.sin(T), a * T]
out = {}


def maxres(expr):
    f = sp.lambdify(Q, expr, "mpmath")
    return (
        max(abs(complex(v)) for p in PTS for v in sp.Matrix(f(*p)))
        if expr.shape
        else 0.0
    )


def report(name, val, expect_zero):
    ok = (val < 1e-9) if expect_zero else (val > 1e-3)
    out[name] = {
        "max_residual": float(val),
        "expected": "zero" if expect_zero else "nonzero",
        "pass": ok,
    }
    print(("PASS " if ok else "FAIL ") + f"{name}: {val:.3e}")
    return ok


ok = True
# P0a: frame orthonormal
gram = sp.Matrix(
    3, 3, lambda i, j: sp.simplify(__import__("kosmann_geometry").gdot(E[i], E[j]))
)
ok &= report(
    "frame_orthonormal", float(max(abs(sp.N(v)) for v in (gram - sp.eye(3)))), True
)
# P0b: spin-connection sign by Clifford compatibility nabla(Y.psi) = (nabla Y).psi + Y.nabla psi
for s in (+1, -1):
    X = E[1]
    res = (
        nabla_spin(X, cliff(Y, PSI), s)
        - cliff(nabla_vec(X, Y), PSI)
        - cliff(Y, nabla_spin(X, PSI, s))
    )
    good = report(f"clifford_compat_s_conn={s:+d}", maxres(res), s == +1)
    ok &= good
S_CONN = +1
# P0c: Lie algebra of the six fields
for name, N in (("plus", NP), ("minus", NM)):
    c = (
        sp.simplify(bracket(N[0], N[1])[1] / N[2][1])
        if N[2][1] != 0
        else sp.simplify(bracket(N[0], N[1])[2] / N[2][2])
    )
    res = [
        sp.simplify(bracket(N[i], N[j])[k] - c * N[l][k])
        for i, j, l in ((0, 1, 2), (1, 2, 0), (2, 0, 1))
        for k in range(3)
    ]
    out[f"bracket_const_{name}"] = str(c)
    ok &= report(
        f"su2_closure_{name}",
        float(max(abs(sp.N(r.subs({a: 0.7, t: 1.1, T: 2.3}))) for r in res)),
        True,
    )
cross = [
    sp.simplify(bracket(NP[i], NM[j])[k])
    for i in range(3)
    for j in range(3)
    for k in range(3)
]
ok &= report(
    "plus_minus_commute",
    float(max(abs(sp.N(r.subs({a: 0.7, t: 1.1, T: 2.3}))) for r in cross)),
    True,
)
print("N3+ =", NP[2], " N3- =", NM[2])
print("N1+ =", NP[0])
print("N1- =", NM[0])
# P1: Kosmann sign and commutation with D, for all six fields; controls: opposite sign, plain component-wise action
# WHY: the sign of the frame-rotation term depends on the index order in kos_matrix; it is not
# assumed. The pre-run guess was -1; the first run (2026-11-24) showed +1 commutes and -1 does not.
# Exactly one sign must pass; that sign is then used everywhere below.
for s_kos in (+1, -1):
    worst = 0.0
    for N in NP + NM:
        res = kosmann(N, dirac(PSI, S_CONN), S_CONN, s_kos) - dirac(
            kosmann(N, PSI, S_CONN, s_kos), S_CONN
        )
        worst = max(worst, maxres(res))
    ok &= report(f"kosmann_commutes_with_D_s_kos={s_kos:+d}", worst, s_kos == +1)
S_KOS = +1
worst = 0.0
for N in NP + NM:
    worst = max(worst, maxres(vf(N, dirac(PSI, S_CONN)) - dirac(vf(N, PSI), S_CONN)))
ok &= report("control_componentwise_commutes_with_D", worst, False)
# P1b: Kosmann respects brackets: [L_X, L_Y] = L_[X,Y]
worst = 0.0
for X_, Y_ in ((NP[0], NP[1]), (NM[0], NM[1]), (NP[0], NM[2])):
    lhs = kosmann(X_, kosmann(Y_, PSI, S_CONN, S_KOS), S_CONN, S_KOS) - kosmann(
        Y_, kosmann(X_, PSI, S_CONN, S_KOS), S_CONN, S_KOS
    )
    worst = max(worst, maxres(lhs - kosmann(bracket(X_, Y_), PSI, S_CONN, S_KOS)))
ok &= report("kosmann_bracket_homomorphism", worst, True)
# P2: correction matrix for the torus fields d_t, d_T
for name, v in (("d_theta", [0, 1, 0]), ("d_thetat", [0, 0, 1])):
    corr = sp.simplify(S_CONN * omega(v) + S_KOS * kos_matrix(v))
    # WHY: exact test (review 2026-11-24): the simplified matrix must be identically zero
    exact_zero = corr == sp.zeros(2, 2)
    ok &= report(f"torus_correction_zero_{name}", 0.0 if exact_zero else 1.0, True)
# record the nonzero correction for N1+ (the frame-rotation term the scalar treatment drops)
corr1 = sp.simplify(S_CONN * omega(NP[0]) + S_KOS * kos_matrix(NP[0]))
out["correction_matrix_N1_plus"] = str(corr1)
print("correction for N1+ :", corr1)
out["S_CONN"], out["S_KOS"] = S_CONN, S_KOS
with open("results_checks.json", "w") as fh:
    json.dump(out, fh, indent=1)
print("ALL_PASS" if ok else "SOME_FAIL")
sys.exit(0 if ok else 1)
