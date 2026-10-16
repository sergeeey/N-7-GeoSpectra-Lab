"""C218 -- explicit real structure J on round59's Sigma, and its su(3)-equivariance,
checked directly (pre-registered claims P1-P5 in claim.md).

Reuses round59_route_a_independent.py (build_clifford, spin_lift, NOMIZU/ADNU,
run_calibration, EVEN_IDX/ODD_IDX) via importlib -- same loading pattern as C149/C193,
not retyped.

Run:  python c218_real_structure_j.py
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
R59_PATH = (
    HERE.parent
    / "20260714-round59-trivial-rank-certification"
    / "round59_route_a_independent.py"
)

PASS, FAIL = [], []
RESULTS: dict[str, object] = {}


def check(label, condition, detail=""):
    (PASS if condition else FAIL).append(label)
    print(f"  [{'PASS' if condition else 'FAIL'}] {label}")
    if detail:
        print(f"         {detail}")


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def unvec(v: sp.Matrix, n: int) -> sp.Matrix:
    """Inverse of column-stacking vec(): v[j*n+i] -> M[i,j]."""
    return sp.Matrix(n, n, lambda i, j: v[j * n + i])


def is_zero(m: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in m)


print("=" * 78)
print("0  load round59's machinery (reused, not retyped)")
print("=" * 78)

R59 = load_module("round59_route_a_independent", R59_PATH)
E = R59.build_clifford(conj=False)
Ec = R59.build_clifford(conj=True)
calib_ok, _ = R59.run_calibration(E, R59.NOMIZU)
check("Q0 round59 calibration re-verified on import", calib_ok)

RHO = {a: R59.spin_lift(R59.ADNU[a], E) for a in range(1, 9)}
conj_matches = all(is_zero(E[k].conjugate() - Ec[k]) for k in range(1, 7))
print(
    f"  informational: build_clifford(conj=True) == entrywise conjugate of E: {conj_matches}"
)
RESULTS["conj_true_equals_entrywise_conjugate"] = conj_matches

GAMMA = sp.zeros(8, 8)
for k in R59.EVEN_IDX:
    GAMMA[k, k] = 1
for k in R59.ODD_IDX:
    GAMMA[k, k] = -1

print()
print("=" * 78)
print("1  P1: solve B * conj(E_k) = eps * E_k * B  (k=1..6) for eps = +1, -1")
print("=" * 78)

I8 = sp.eye(8)
Econj = {k: E[k].conjugate() for k in range(1, 7)}


def solve_B(eps: int) -> list[sp.Matrix]:
    blocks = []
    for k in range(1, 7):
        blocks.append(
            sp.Matrix(sp.kronecker_product(Econj[k].T, I8))
            - eps * sp.Matrix(sp.kronecker_product(I8, E[k]))
        )
    big = sp.Matrix.vstack(*blocks)
    sols = big.nullspace()
    return [unvec(v, 8) for v in sols]


B_by_eps: dict[int, sp.Matrix] = {}
for eps in (+1, -1):
    sols = solve_B(eps)
    check(
        f"P1[eps={eps:+d}] solution space of B*conj(E_k)=eps*E_k*B is exactly 1-dimensional",
        len(sols) == 1,
        f"nullity = {len(sols)}",
    )
    RESULTS[f"nullity_eps_{eps:+d}"] = len(sols)
    if len(sols) == 1:
        B = sols[0]
        BBd = sp.simplify(B * B.H)
        c = BBd[0, 0]
        proportional = is_zero(BBd - c * I8) and sp.simplify(c) != 0
        check(
            f"P1[eps={eps:+d}] B is proportional to a unitary (B B^dagger = c I, c != 0)",
            proportional,
            f"c = {c}",
        )
        if proportional:
            B_by_eps[eps] = sp.simplify(B / sp.sqrt(c))

print()
print("=" * 78)
print("2  P2: J^2 and (anti)commutation with the chirality grading gamma, both eps")
print("=" * 78)

ko6_found = False
for eps, B in B_by_eps.items():
    J2 = sp.simplify(B * B.conjugate())
    j2_val = J2[0, 0] if is_zero(J2 - J2[0, 0] * I8) else None
    sigma = None
    Bg = sp.simplify(B * GAMMA * B.inv())
    if is_zero(Bg - GAMMA):
        sigma = +1
    elif is_zero(Bg + GAMMA):
        sigma = -1
    print(f"  eps={eps:+d}:  J^2 = {j2_val}*I   J gamma J^-1 = {sigma}*gamma")
    RESULTS[f"J2_eps_{eps:+d}"] = str(j2_val)
    RESULTS[f"gamma_sign_eps_{eps:+d}"] = sigma
    if j2_val == 1 and sigma == -1:
        ko6_found = True
check(
    "P2 at least one solution has the KO-6 pattern J^2=+1, J gamma = -gamma J",
    ko6_found,
)

print()
print("=" * 78)
print(
    "3  P3: J RHO[a] J^-1 = RHO[a] for all a=1..8, both eps (predicted FORCED, not su(3)-specific)"
)
print("=" * 78)

for eps, B in B_by_eps.items():
    worst = 0
    for a in range(1, 9):
        lhs = sp.simplify(B * RHO[a].conjugate() * B.inv())
        res = sp.simplify(lhs - RHO[a])
        worst = max(worst, max((abs(complex(sp.N(x))) for x in res), default=0.0))
    check(
        f"P3[eps={eps:+d}] J RHO[a] J^-1 = RHO[a] exactly for all 8 generators",
        worst < 1e-12,
        f"max residual = {worst:.3e}",
    )
    RESULTS[f"P3_max_residual_eps_{eps:+d}"] = worst

print()
print("=" * 78)
print("4  P4: negative controls -- the check CAN fail")
print("=" * 78)

if B_by_eps:
    eps0, B0 = next(iter(B_by_eps.items()))
    T = sp.I * RHO[1]
    res_T = sp.simplify(B0 * T.conjugate() * B0.inv() - T)
    norm_T = float(sp.N(sp.sqrt(sum(abs(x) ** 2 for x in T))))
    norm_res = float(sp.N(sp.sqrt(sum(abs(x) ** 2 for x in res_T))))
    check(
        "P4a antilinearity identity: complex-coefficient T = i*RHO[1] gives J T J^-1 = -T "
        "(in the Hermitian-generator convention this IS equivariance of exp(i theta T); "
        "arithmetic consistency, not evidence)",
        abs(norm_res - 2 * norm_T) < 1e-9 and norm_res > 0.1,
        f"||J T J^-1 - T|| = {norm_res:.4f}, 2||T|| = {2 * norm_T:.4f}",
    )
    rng = np.random.default_rng(20261003)
    Q, _ = np.linalg.qr(rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8)))
    En = {k: np.array(E[k].evalf(), dtype=complex) for k in range(1, 7)}
    worst_rand = min(
        max(
            np.max(np.abs(Q @ En[k].conj() @ np.linalg.inv(Q) - eps * En[k]))
            for k in range(1, 7)
        )
        for eps in (+1, -1)
    )
    RESULTS["P4a_norm_res"] = norm_res
    RESULTS["P4a_two_norm_T"] = 2 * norm_T
    check(
        "P4b a random unitary B' does NOT satisfy B' conj(E_k) B'^-1 = +-E_k",
        worst_rand > 0.1,
        f"smaller-eps worst residual = {worst_rand:.3f}",
    )
    RESULTS["P4b_random_unitary_worst_residual"] = float(worst_rand)
    # P4c (added after skeptic): random anti-Hermitian generator K in u(8) -- does exp(tK)
    # commute with J in the antiunitary sense, J K J^-1 = B conj(K) B^-1 =? K ?  Must fail.
    Bn = np.array(B0.evalf(), dtype=complex)
    Kr = rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8))
    Kr = Kr - Kr.conj().T
    res_K = np.max(np.abs(Bn @ Kr.conj() @ np.linalg.inv(Bn) - Kr))
    check(
        "P4c a random anti-Hermitian 8x8 generator does NOT satisfy J K J^-1 = K",
        res_K > 0.1,
        f"residual = {res_K:.3f}",
    )
    RESULTS["P4c_random_antiherm_residual"] = float(res_K)

print()
print("=" * 78)
print("5  P5 (separate object): nearly-Kahler J as the commutant of ADNU on R^6")
print("=" * 78)


def terms_to_matrix(terms) -> sp.Matrix:
    M = sp.zeros(6, 6)
    for coeff, a, b in terms:
        M[a - 1, b - 1] += coeff
        M[b - 1, a - 1] -= coeff
    return M


def matrix_to_terms(X: sp.Matrix):
    out = []
    for a in range(1, 7):
        for b in range(a + 1, 7):
            c = X[a - 1, b - 1]
            if sp.simplify(c) != 0:
                out.append((c, a, b))
    return out


A = {a: terms_to_matrix(R59.ADNU[a]) for a in range(1, 9)}
A_scaled = {a: (2 * A[a] if a < 8 else 2 * sp.sqrt(3) * A[a]) for a in range(1, 9)}
rows = []
for a in range(1, 9):
    Aa = sp.Matrix(A_scaled[a].applyfunc(sp.nsimplify))
    rows.append(
        sp.Matrix(sp.kronecker_product(sp.eye(6), Aa))
        - sp.Matrix(sp.kronecker_product(Aa.T, sp.eye(6)))
    )
big = sp.Matrix.vstack(*rows)
comm_basis = [unvec(v, 6) for v in big.nullspace()]
check(
    "P5a commutant of ADNU on R^6 has dimension exactly 2",
    len(comm_basis) == 2,
    f"dim = {len(comm_basis)}",
)
RESULTS["commutant_dim_ADNU_R6"] = len(comm_basis)

J_NK = None
if len(comm_basis) == 2:
    anti = [sp.simplify((M - M.T) / 2) for M in comm_basis]
    anti = [M for M in anti if not is_zero(M)]
    if anti:
        J0 = anti[0]
        J0sq = sp.simplify(J0 * J0)
        c = -J0sq[0, 0]
        if is_zero(J0sq + c * sp.eye(6)) and sp.simplify(c) != 0:
            J_NK = sp.simplify(J0 / sp.sqrt(c))
    check(
        "P5b the commutant contains an antisymmetric J_NK with J_NK^2 = -1 (up to sign)",
        J_NK is not None and is_zero(sp.simplify(J_NK * J_NK + sp.eye(6))),
    )

if J_NK is not None:
    LJ = R59.spin_lift(matrix_to_terms(J_NK), E)
    worst = 0.0
    for a in range(1, 9):
        res = sp.simplify(LJ * RHO[a] - RHO[a] * LJ)
        worst = max(worst, max(abs(complex(sp.N(x))) for x in res))
    check(
        "P5c [spin_lift(J_NK), RHO[a]] = 0 for all a (direct computation, not via C193's identity)",
        worst < 1e-12,
        f"max residual = {worst:.3e}",
    )
    rng2 = np.random.default_rng(7)
    X = sp.zeros(6, 6)
    for i in range(6):
        for j in range(i + 1, 6):
            v = int(rng2.integers(-3, 4))
            X[i, j], X[j, i] = v, -v
    LX = R59.spin_lift(matrix_to_terms(X), E)
    worst_X = max(
        max(abs(complex(sp.N(x))) for x in sp.simplify(LX * RHO[a] - RHO[a] * LX))
        for a in range(1, 9)
    )
    check(
        "P5d negative control: a random so(6) element does NOT commute with RHO",
        worst_X > 0.1,
        f"max residual = {worst_X:.3f}",
    )
    RESULTS["P5c_max_residual"] = worst
    RESULTS["P5d_random_so6_residual"] = float(worst_X)

print()
print("=" * 78)
print(f"C218: {len(PASS)} passed, {len(FAIL)} failed")
for f in FAIL:
    print(f"  FAILED: {f}")
print("=" * 78)

(HERE / "results_c218.json").write_text(json.dumps(RESULTS, indent=2, default=str))
