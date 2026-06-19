"""G17 tests: Q = T3L + Y — electric charge on the 32-dim S³×S⁶ spinor."""

import os
import sys

import sympy as sp
from sympy import zeros

_exp_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260619-g17-electric-charge"
)
sys.path.insert(0, _exp_dir)

for _p in [
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g16-t3r-from-k3"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g15-hypercharge"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g11-block-generators"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g10b-su3-in-so6"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260617-g10-s6-so6-gauge"),
]:
    sys.path.insert(0, _p)

from g17_electric_charge import (  # noqa: E402
    Q_32,
    SM_LH_DN,
    SM_LH_UP,
)
from g16_t3r_k3 import (  # noqa: E402
    C32,
    J3_32,
    SM_RH_ANTIFERMIONS,
    SM_RH_FERMIONS,
    Y_32,
)

half = sp.Rational(1, 2)


# ── Algebraic properties ───────────────────────────────────────────────────────


def test_Q_32_diagonal():
    """Q = T3L + Y is diagonal (both summands are diagonal)."""
    assert Q_32.is_diagonal()


def test_Q_32_hermitian():
    """Q_32 is Hermitian — it is a physical observable."""
    assert Q_32 - Q_32.H == zeros(32, 32)


def test_Q_equals_J3_plus_Y_all_rows():
    """Q_32[i,i] = J3_32[i,i] + Y_32[i,i] for all 32 rows."""
    for i in range(32):
        assert Q_32[i, i] == J3_32[i, i] + Y_32[i, i], f"row {i}: mismatch"


# ── Commutativity with color ───────────────────────────────────────────────────


def test_Q_commutes_all_color_generators():
    """[Q_32, C_i] = 0 for all 8 SU(3) generators — QED commutes with color."""
    for i, C in enumerate(C32):
        assert Q_32 * C - C * Q_32 == zeros(32, 32), f"[Q, C_{i}] ≠ 0"


# ── Right-handed fermion Q ─────────────────────────────────────────────────────


def test_nu_R_Q_zero():
    """ν_R has Q = 0 (row 16, T3L=0, Y=0)."""
    row, y_exp = SM_RH_FERMIONS["nu_R"]
    assert row == 16
    assert Q_32[row, row] == 0
    assert Q_32[row, row] == y_exp


def test_e_R_Q_minus_one():
    """e_R has Q = −1 (row 24, T3L=0, Y=−1)."""
    row, y_exp = SM_RH_FERMIONS["e_R"]
    assert row == 24
    assert Q_32[row, row] == sp.Integer(-1)


def test_u_R_triplet_Q():
    """u_R color triplet (rows 19, 21, 22) has Q = +2/3."""
    for key in ["u_R_1", "u_R_2", "u_R_3"]:
        row, y_exp = SM_RH_FERMIONS[key]
        assert Q_32[row, row] == sp.Rational(2, 3), f"{key}: Q={Q_32[row, row]}"


def test_d_R_triplet_Q():
    """d_R color triplet (rows 27, 29, 30) has Q = −1/3."""
    for key in ["d_R_1", "d_R_2", "d_R_3"]:
        row, y_exp = SM_RH_FERMIONS[key]
        assert Q_32[row, row] == sp.Rational(-1, 3), f"{key}: Q={Q_32[row, row]}"


def test_SM_RH_fermions_all_Q():
    """All 8 SM right-handed fermion Q values match expectation."""
    for name, (row, q_exp) in SM_RH_FERMIONS.items():
        assert Q_32[row, row] == q_exp, f"{name} row {row}: Q={Q_32[row, row]} ≠ {q_exp}"


def test_SM_RH_antifermions_all_Q():
    """All 8 SM right-handed antifermion Q values match expectation."""
    for name, (row, q_exp) in SM_RH_ANTIFERMIONS.items():
        assert Q_32[row, row] == q_exp, f"{name} row {row}: Q={Q_32[row, row]} ≠ {q_exp}"


# ── Left-handed sector Q ──────────────────────────────────────────────────────


def test_nu_L_Q_zero():
    """ν_L has Q = 0 (row 0, T3L=+1/2, Y=−1/2)."""
    assert Q_32[0, 0] == sp.Integer(0)


def test_e_L_Q_minus_one():
    """e_L has Q = −1 (row 8, T3L=−1/2, Y=−1/2)."""
    assert Q_32[8, 8] == sp.Integer(-1)


def test_u_L_triplet_Q():
    """u_L color triplet (rows 3, 5, 6) has Q = +2/3."""
    for row in [3, 5, 6]:
        assert Q_32[row, row] == sp.Rational(2, 3), f"row {row}: Q={Q_32[row, row]}"


def test_d_L_triplet_Q():
    """d_L color triplet (rows 11, 13, 14) has Q = −1/3."""
    for row in [11, 13, 14]:
        assert Q_32[row, row] == sp.Rational(-1, 3), f"row {row}: Q={Q_32[row, row]}"


def test_SM_LH_up_all_Q():
    """All 8 left-handed up-type (T3L=+1/2) Q values match."""
    for name, (row, q_exp) in SM_LH_UP.items():
        assert Q_32[row, row] == q_exp, f"{name} row {row}: Q={Q_32[row, row]} ≠ {q_exp}"


def test_SM_LH_dn_all_Q():
    """All 8 left-handed down-type (T3L=−1/2) Q values match."""
    for name, (row, q_exp) in SM_LH_DN.items():
        assert Q_32[row, row] == q_exp, f"{name} row {row}: Q={Q_32[row, row]} ≠ {q_exp}"


# ── Neutrino rows ──────────────────────────────────────────────────────────────


def test_all_neutrino_rows_Q_zero():
    """All four neutrino states (ν_L, ν̄_L, ν_R, ν̄_R) have Q = 0."""
    neutrino_rows = [0, 15, 16, 31]
    for row in neutrino_rows:
        assert Q_32[row, row] == sp.Integer(0), f"row {row}: Q={Q_32[row, row]}"


# ── Q spectrum ─────────────────────────────────────────────────────────────────


def test_Q_charge_quantization():
    """All 32 Q eigenvalues are in {0, ±1/3, ±2/3, ±1}."""
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
        assert Q_32[i, i] in allowed, f"row {i}: Q={Q_32[i, i]} not quantized"


def test_Q_distinct_values():
    """Exactly 7 distinct Q values: {0, ±1/3, ±2/3, ±1}."""
    distinct = set(Q_32[i, i] for i in range(32))
    expected = {
        sp.Integer(0),
        sp.Rational(1, 3),
        sp.Rational(-1, 3),
        sp.Rational(2, 3),
        sp.Rational(-2, 3),
        sp.Integer(1),
        sp.Integer(-1),
    }
    assert distinct == expected


def test_Q_global_neutrality():
    """Global charge neutrality: Σ Q_i = 0 over all 32 states."""
    total = sum(Q_32[i, i] for i in range(32))
    assert total == sp.Integer(0)
