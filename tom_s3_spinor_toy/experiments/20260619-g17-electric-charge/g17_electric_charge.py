"""G17: Electric charge Q = T3L + Y on the 32-dim S³×S⁶ spinor.

Gell-Mann–Nishijima–Nakano: Q = T3L + Y = J3_32 + Y_32.

G11: T3L = J₃^{32} = kron(J_S3[2], I8), diagonal ±1/2 in L sector, 0 in R sector.
G16: Y_32 = K₃^{32} + BmL_32/2, fully geometric.

All 32 states of the S³×S⁶ spinor identified by Q:
  Q = 0:    ν_L(0), ν̄_L(15), ν_R(16), ν̄_R(31)             — 4 states
  Q = −1:   e_L(8), e_R(24)                                  — 2 states
  Q = +1:   ē_L(7), ē_R(23)                                  — 2 states
  Q = +2/3: u_L(3,5,6), u_R(19,21,22)                       — 6 states
  Q = −2/3: ū_L(9,10,12), ū_R(25,26,28)                    — 6 states
  Q = −1/3: d_L(11,13,14), d_R(27,29,30)                   — 6 states
  Q = +1/3: d̄_L(1,2,4), d̄_R(17,18,20)                    — 6 states

Global neutrality: Σ Q_i = 0 over all 32 states.

λ = FREE_COUPLING_PARAMETER throughout. sm_derivation_claimed = False.
"""

import os
import sys

import sympy as sp
from sympy import zeros

for _p in [
    os.path.join(os.path.dirname(__file__), "..", "20260619-g16-t3r-from-k3"),
    os.path.join(os.path.dirname(__file__), "..", "20260619-g15-hypercharge"),
    os.path.join(os.path.dirname(__file__), "..", "20260618-g11-block-generators"),
    os.path.join(os.path.dirname(__file__), "..", "20260618-g10b-su3-in-so6"),
    os.path.join(os.path.dirname(__file__), "..", "20260617-g10-s6-so6-gauge"),
]:
    sys.path.insert(0, _p)

from g16_t3r_k3 import (  # noqa: E402
    C32,
    J3_32,
    SM_RH_ANTIFERMIONS,
    SM_RH_FERMIONS,
    Y_32,
)

half = sp.Rational(1, 2)

# ── Q = T3L + Y ───────────────────────────────────────────────────────────────

Q_32: sp.Matrix = J3_32 + Y_32

# ── Left-handed up-type (T3L = +1/2, rows 0–7) ───────────────────────────────
# Row = 0*8 + S6_index.  SP_SINGLET=0, AQUARK=(1,2,4), QUARK=(3,5,6), SM_SINGLET=7.
# Q = +1/2 + Y_L;  Y_L = BmL[j,j]/2 since T3R=0 in L sector.

SM_LH_UP: dict[str, tuple[int, sp.Rational]] = {
    "nu_L": (0, sp.Integer(0)),
    "d_Lbar_1": (1, sp.Rational(1, 3)),
    "d_Lbar_2": (2, sp.Rational(1, 3)),
    "u_L_1": (3, sp.Rational(2, 3)),
    "d_Lbar_3": (4, sp.Rational(1, 3)),
    "u_L_2": (5, sp.Rational(2, 3)),
    "u_L_3": (6, sp.Rational(2, 3)),
    "e_Lbar": (7, sp.Integer(1)),
}

# ── Left-handed down-type (T3L = −1/2, rows 8–15) ────────────────────────────

SM_LH_DN: dict[str, tuple[int, sp.Rational]] = {
    "e_L": (8, sp.Integer(-1)),
    "u_Lbar_1": (9, sp.Rational(-2, 3)),
    "u_Lbar_2": (10, sp.Rational(-2, 3)),
    "d_L_1": (11, sp.Rational(-1, 3)),
    "u_Lbar_3": (12, sp.Rational(-2, 3)),
    "d_L_2": (13, sp.Rational(-1, 3)),
    "d_L_3": (14, sp.Rational(-1, 3)),
    "nu_Lbar": (15, sp.Integer(0)),
}


# ── Gate verification ──────────────────────────────────────────────────────────


def verify_gates() -> str:
    gates_pass = 0

    # T1: Q_32 diagonal
    assert Q_32.is_diagonal(), "T1 FAIL: Q_32 not diagonal"
    gates_pass += 1

    # T2: Q_32 Hermitian
    assert Q_32 - Q_32.H == zeros(32, 32), "T2 FAIL: Q_32 not Hermitian"
    gates_pass += 1

    # T3: [Q_32, C_i] = 0  (QED commutes with SU(3) color)
    for i, C in enumerate(C32):
        assert Q_32 * C - C * Q_32 == zeros(32, 32), f"T3 FAIL: [Q, C_{i}] ≠ 0"
    gates_pass += 1

    # T4: Right-handed fermion Q (= Y since T3L=0 in R sector)
    for name, (row, y_exp) in SM_RH_FERMIONS.items():
        assert Q_32[row, row] == y_exp, f"T4 FAIL: {name} Q={Q_32[row, row]} ≠ {y_exp}"
    gates_pass += 1

    # T5: Right-handed antifermion Q
    for name, (row, y_exp) in SM_RH_ANTIFERMIONS.items():
        assert Q_32[row, row] == y_exp, f"T5 FAIL: {name} Q={Q_32[row, row]} ≠ {y_exp}"
    gates_pass += 1

    # T6: Left-handed up-type Q
    for name, (row, q_exp) in SM_LH_UP.items():
        assert Q_32[row, row] == q_exp, f"T6 FAIL: {name} Q={Q_32[row, row]} ≠ {q_exp}"
    gates_pass += 1

    # T7: Left-handed down-type Q
    for name, (row, q_exp) in SM_LH_DN.items():
        assert Q_32[row, row] == q_exp, f"T7 FAIL: {name} Q={Q_32[row, row]} ≠ {q_exp}"
    gates_pass += 1

    # T8: All 32 Q values in {0, ±1/3, ±2/3, ±1}
    allowed = {
        sp.Integer(0),
        sp.Rational(1, 3),
        sp.Rational(-1, 3),
        sp.Rational(2, 3),
        sp.Rational(-2, 3),
        sp.Integer(1),
        sp.Integer(-1),
    }
    for i in range(32):
        assert Q_32[i, i] in allowed, f"T8 FAIL: row {i} Q={Q_32[i, i]} not in SM set"
    gates_pass += 1

    # T9: Distinct Q values = 7 (full SM charge quantization)
    distinct = set(Q_32[i, i] for i in range(32))
    assert distinct == allowed, f"T9 FAIL: distinct Q values = {sorted(distinct)}"
    gates_pass += 1

    # T10: Global charge neutrality Σ Q_i = 0
    total = sum(Q_32[i, i] for i in range(32))
    assert total == 0, f"T10 FAIL: Σ Q_i = {total} ≠ 0"
    gates_pass += 1

    return f"PASS_G17_ELECTRIC_CHARGE_GEOMETRIC ({gates_pass}/10)"


if __name__ == "__main__":
    print(verify_gates())
