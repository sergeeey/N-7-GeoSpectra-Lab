"""G16 tests: T3R from S³ K-generators — completing Y = T3R + (B−L)/2."""

import os
import sys

import sympy as sp
from sympy import zeros

_exp_dir = os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g16-t3r-from-k3")
sys.path.insert(0, _exp_dir)

for _p in [
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g15-hypercharge"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g11-block-generators"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g10b-su3-in-so6"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260617-g10-s6-so6-gauge"),
]:
    sys.path.insert(0, _p)

from g16_t3r_k3 import (  # noqa: E402
    BmL_32,
    C32,
    J3_32,
    K3_32,
    L_DN,
    L_UP,
    R_DN,
    R_UP,
    SM_RH_ANTIFERMIONS,
    SM_RH_FERMIONS,
    Y_32,
)

half = sp.Rational(1, 2)


# ── K₃ diagonal structure ─────────────────────────────────────────────────────


def test_K3_32_diagonal():
    """K₃^{32} is diagonal."""
    assert K3_32.is_diagonal()


def test_K3_32_left_sector_zero():
    """L sector (rows 0–15) has T3R = 0."""
    for i in L_UP + L_DN:
        assert K3_32[i, i] == 0, f"row {i}: K₃={K3_32[i, i]}"


def test_K3_32_R_up_half():
    """R,↑ sector (rows 16–23) has T3R = +1/2."""
    for i in R_UP:
        assert K3_32[i, i] == half, f"row {i}: K₃={K3_32[i, i]}"


def test_K3_32_R_dn_minus_half():
    """R,↓ sector (rows 24–31) has T3R = −1/2."""
    for i in R_DN:
        assert K3_32[i, i] == -half, f"row {i}: K₃={K3_32[i, i]}"


def test_K3_32_eigenvalue_structure():
    """K₃^{32} has exactly 16×0 + 8×(+1/2) + 8×(−1/2)."""
    diag = [K3_32[i, i] for i in range(32)]
    assert sum(1 for v in diag if v == 0) == 16
    assert sum(1 for v in diag if v == half) == 8
    assert sum(1 for v in diag if v == -half) == 8


# ── Commutativity ─────────────────────────────────────────────────────────────


def test_K3_J3_commute():
    """[K₃^{32}, J₃^{32}] = 0: T3R and T3L are independent quantum numbers."""
    assert K3_32 * J3_32 - J3_32 * K3_32 == zeros(32, 32)


def test_K3_commutes_all_color_generators():
    """[K₃^{32}, C_i^{32}] = 0 for all 8 SU(3)_color generators."""
    for i, C in enumerate(C32):
        assert K3_32 * C - C * K3_32 == zeros(32, 32), f"K₃ fails to commute with C_{i}"


# ── Hypercharge Y = K₃ + B−L/2 ───────────────────────────────────────────────


def test_Y_32_diagonal():
    """Y_32 = K₃^{32} + BmL_32/2 is diagonal."""
    assert Y_32.is_diagonal()


def test_Y_32_hermitian():
    """Y_32 is Hermitian (physical observable)."""
    assert Y_32 - Y_32.H == zeros(32, 32)


def test_Y_commutes_color_generators():
    """[Y_32, C_i^{32}] = 0: hypercharge commutes with SU(3)_color."""
    for i, C in enumerate(C32):
        assert Y_32 * C - C * Y_32 == zeros(32, 32), f"Y fails to commute with C_{i}"


# ── SM right-handed fermions ──────────────────────────────────────────────────


def test_nu_R_row_and_Y():
    """ν_R is at row 16 with Y = 0."""
    row, Y_exp = SM_RH_FERMIONS["nu_R"]
    assert row == 16
    assert Y_32[row, row] == Y_exp


def test_e_R_row_and_Y():
    """e_R is at row 24 with Y = −1."""
    row, Y_exp = SM_RH_FERMIONS["e_R"]
    assert row == 24
    assert Y_32[row, row] == Y_exp


def test_u_R_color_triplet_Y():
    """All three u_R states (rows 19, 21, 22) have Y = +2/3."""
    for key in ["u_R_1", "u_R_2", "u_R_3"]:
        row, Y_exp = SM_RH_FERMIONS[key]
        assert Y_32[row, row] == Y_exp, f"{key} row {row}: Y={Y_32[row, row]} ≠ {Y_exp}"


def test_d_R_color_triplet_Y():
    """All three d_R states (rows 27, 29, 30) have Y = −1/3."""
    for key in ["d_R_1", "d_R_2", "d_R_3"]:
        row, Y_exp = SM_RH_FERMIONS[key]
        assert Y_32[row, row] == Y_exp, f"{key} row {row}: Y={Y_32[row, row]} ≠ {Y_exp}"


def test_SM_RH_fermions_all_Y():
    """All 8 SM right-handed fermion states have correct geometric Y."""
    for name, (row, Y_exp) in SM_RH_FERMIONS.items():
        assert Y_32[row, row] == Y_exp, f"{name} row {row}: Y={Y_32[row, row]} ≠ {Y_exp}"


# ── SM right-handed antifermions ─────────────────────────────────────────────


def test_SM_RH_antifermions_all_Y():
    """All 8 SM right-handed antifermion states have correct geometric Y."""
    for name, (row, Y_exp) in SM_RH_ANTIFERMIONS.items():
        assert Y_32[row, row] == Y_exp, f"{name} row {row}: Y={Y_32[row, row]} ≠ {Y_exp}"


def test_antifermion_Y_opposite_sign():
    """For each fermion/antifermion pair: Y_f + Y_af = 0 (CPT conjugate)."""
    pairs = {
        "nu_R": "nu_Rbar",
        "u_R_1": "u_Rbar_1",
        "u_R_2": "u_Rbar_2",
        "u_R_3": "u_Rbar_3",
        "e_R": "e_Rbar",
        "d_R_1": "d_Rbar_1",
        "d_R_2": "d_Rbar_2",
        "d_R_3": "d_Rbar_3",
    }
    for ferm, antiferm in pairs.items():
        _, Y_f = SM_RH_FERMIONS[ferm]
        _, Y_af = SM_RH_ANTIFERMIONS[antiferm]
        assert Y_f + Y_af == 0, f"{ferm}+{antiferm}: Y={Y_f}+{Y_af}≠0"


# ── Left-handed sector ────────────────────────────────────────────────────────


def test_L_sector_lepton_doublet_Y():
    """Left-handed lepton doublet rows have Y = −1/2 (T3R=0, B−L=−1 → Y=−1/2)."""
    assert Y_32[0, 0] == sp.Rational(-1, 2)  # |L↑⟩⊗|000⟩
    assert Y_32[8, 8] == sp.Rational(-1, 2)  # |L↓⟩⊗|000⟩


def test_L_sector_quark_doublet_Y():
    """Left-handed quark doublet rows have Y = +1/6 (T3R=0, B−L=+1/3 → Y=+1/6)."""
    assert Y_32[3, 3] == sp.Rational(1, 6)  # |L↑⟩⊗|011⟩
    assert Y_32[11, 11] == sp.Rational(1, 6)  # |L↓⟩⊗|011⟩


def test_Y_32_formula_all_rows():
    """Y_32[i,i] = K3_32[i,i] + BmL_32[i,i]/2 for all 32 rows."""
    for i in range(32):
        expected = K3_32[i, i] + BmL_32[i, i] * half
        assert Y_32[i, i] == expected, f"row {i}: Y={Y_32[i, i]} ≠ {expected}"
