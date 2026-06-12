"""LAMBDA-B5-G3: Spinorial curvature [nabla_a, nabla_b] = (1/4)[gamma_a, gamma_b] on unit S3.

Curvature tensor: R_{abcd} = delta_{ac} delta_{bd} - delta_{ad} delta_{bc}  (K=+1, from G2)
Claim: spinorial curvature F_{ab} = (1/4) R_{abcd} gamma^c gamma^d = (1/4)[gamma_a, gamma_b]
       These operators generate su(2) with Casimir j=1/2.
"""

import json
import os
import sys

import sympy as sp

# ── Setup ───────────────────────────────────────────────────────────────────
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
I2 = sp.eye(2)
gamma = [s1, s2, s3]

results: list[dict] = []
_passed = 0


def chk(name: str, cond: object, desc: str) -> bool:
    global _passed
    if isinstance(cond, sp.MatrixBase):
        ok = cond == sp.zeros(*cond.shape)
    elif isinstance(cond, sp.Basic):
        ok = bool(sp.simplify(cond) == 0)
    else:
        ok = bool(cond)
    results.append({"check": name, "pass": ok, "desc": desc})
    print(f"{'PASS' if ok else 'FAIL'} {name}: {desc}")
    if ok:
        _passed += 1
    return ok


def eps(a: int, b: int, c: int) -> int:
    if (a, b, c) in {(0, 1, 2), (1, 2, 0), (2, 0, 1)}:
        return 1
    if (a, b, c) in {(1, 0, 2), (2, 1, 0), (0, 2, 1)}:
        return -1
    return 0


def R(a: int, b: int, c: int, d: int) -> int:
    return (1 if a == c else 0) * (1 if b == d else 0) - (1 if a == d else 0) * (1 if b == c else 0)


# ── T1: Clifford commutators [gamma^a, gamma^b] = 2i eps^{abc} gamma^c ─────
comm_ok = all(
    gamma[a] * gamma[b] - gamma[b] * gamma[a]
    == sum((2 * sp.I * eps(a, b, c) * gamma[c] for c in range(3)), sp.zeros(2))
    for a in range(3)
    for b in range(3)
)
chk("T1", comm_ok, "[gamma^a, gamma^b] = 2i eps^{abc} gamma^c  [9 entries]")

# ── T2: Unit S3 curvature tensor  R_{1212} = 1  (K=+1 from G2) ─────────────
chk("T2", R(0, 1, 0, 1) == 1, "R_{1212} = 1 — sectional curvature K=+1 consistent with G2")

# ── T3a: Spinorial curvature F_{12} = (i/2) gamma^3 ────────────────────────
F12 = sum(
    (sp.Rational(1, 4) * R(0, 1, c, d) * gamma[c] * gamma[d] for c in range(3) for d in range(3)),
    sp.zeros(2),
)
F12_expected = sp.I * sp.Rational(1, 2) * gamma[2]  # (i/2) gamma^3
chk("T3a", F12 - F12_expected, "F_{12} = (1/4) R_{12cd} gamma^c gamma^d = (i/2) gamma^3")


# ── T3b: F_{ab} = (1/4)[gamma^a, gamma^b] for all (a,b) ────────────────────
def F(a: int, b: int) -> sp.Matrix:
    return sum(
        (
            sp.Rational(1, 4) * R(a, b, c, d) * gamma[c] * gamma[d]
            for c in range(3)
            for d in range(3)
        ),
        sp.zeros(2),
    )


def comm(a: int, b: int) -> sp.Matrix:
    return sp.Rational(1, 4) * (gamma[a] * gamma[b] - gamma[b] * gamma[a])


all_F = all(F(a, b) - comm(a, b) == sp.zeros(2) for a in range(3) for b in range(3))
chk("T3b", all_F, "F_{ab} = (1/4)[gamma^a, gamma^b] for all a,b  [9 entries]")

# ── T4: Antisymmetry F_{ab} = -F_{ba} ───────────────────────────────────────
antisym_ok = all(F(a, b) + F(b, a) == sp.zeros(2) for a in range(3) for b in range(3))
chk("T4", antisym_ok, "F_{ab} = -F_{ba}  (antisymmetry in a,b)")

# ── T5: su(2) generators J_a = F_{bc} eps_{abc} / 2 ────────────────────────
# J_1 = F_{23}, J_2 = F_{31}, J_3 = F_{12}
J = [F(1, 2), F(2, 0), F(0, 1)]

su2_ok = all(
    J[a] * J[b] - J[b] * J[a] == sum((-eps(a, b, c) * J[c] for c in range(3)), sp.zeros(2))
    for a in range(3)
    for b in range(3)
)
chk(
    "T5",
    su2_ok,
    "[J_a, J_b] = -eps_{abc} J_c  — anti-Hermitian su(2) generators (J_a=(i/2)sigma_a)",
)

# ── T6: J_a are anti-Hermitian ───────────────────────────────────────────────
antiherm_ok = all(J[a] + J[a].conjugate().T == sp.zeros(2) for a in range(3))
chk("T6", antiherm_ok, "J_a^dag = -J_a  (anti-Hermitian generators of su(2)_L)")

# ── T7: Casimir Sigma J_a^2 = -(3/4) I = -j(j+1) I  for j=1/2 ─────────────
casimir = sum((J[a] * J[a] for a in range(3)), sp.zeros(2))
chk("T7", casimir + sp.Rational(3, 4) * I2, "Sigma J_a^2 = -(3/4) I  — Casimir j=1/2 spin-1/2 rep")

# ── T8: Explicit form [nabla_1, nabla_2] psi = (i/2) gamma^3 psi ───────────
chk(
    "T8",
    F(0, 1) - sp.I * sp.Rational(1, 2) * gamma[2],
    "[nabla_1, nabla_2] = (i/2) gamma^3  — explicit spinorial curvature",
)

# ── Results ─────────────────────────────────────────────────────────────────
total = len(results)
print(f"\n{_passed}/{total} checks passed")
verdict = "PASS_SU2_CURVATURE_CONFIRMED" if _passed == total else "PARTIAL"

out = {
    "gate": "LAMBDA-B5-G3",
    "verdict": verdict,
    "passed": _passed,
    "total": total,
    "curvature_formula": "[nabla_a, nabla_b] = (1/4)[gamma_a, gamma_b] = (i/2) eps_{abc} gamma^c",
    "curvature_generates": "su(2)_L with Casimir j=1/2",
    "unit_s3": "R_{abcd} = delta_{ac}delta_{bd} - delta_{ad}delta_{bc}  [K=+1 from G2]",
    "connection_to_g2": "K=+1 curvature confirmed by G2 T11-T13 (R^{ab}=e^a∧e^b)",
    "lambda_status": "FREE_COUPLING_PARAMETER",
    "GEOMETRY_AGNOSTIC": True,
    "safe_for_runtime": False,
    "checks": results,
}

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_g3.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2)
print(f"Verdict: {verdict}")
print(f"Saved: {out_path}")
sys.exit(0 if _passed == total else 1)
