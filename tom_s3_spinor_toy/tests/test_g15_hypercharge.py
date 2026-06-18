"""G15 tests: B-L quantum number from S⁶ spinor geometry."""

import os
import sys

import sympy as sp
from sympy import zeros

_exp_dir = os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g15-hypercharge")
sys.path.insert(0, _exp_dir)

for _p in [
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g11-block-generators"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g10b-su3-in-so6"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260617-g10-s6-so6-gauge"),
]:
    sys.path.insert(0, _p)

from g15_hypercharge import (  # noqa: E402
    AQUARK,
    BmL,
    BmL_AQ,
    BmL_ALEP,
    BmL_LEP,
    BmL_Q,
    Gamma7,
    Hamming,
    I8,
    QUARK,
    SM_SINGLET,
    SP_SINGLET,
    sigma3_1,
    sigma3_2,
    sigma3_3,
    su3_spin,
)
from g10_s6_so6_gauge import complex_structure  # noqa: E402
from g11_block_generators import lift_to_spinor  # noqa: E402


# ── B-L structure ─────────────────────────────────────────────────────────────


def test_BmL_diagonal():
    """B-L is a diagonal matrix."""
    assert BmL.is_diagonal()


def test_BmL_entries_formula():
    """Each entry BmL[k,k] = (2·popcount(k) - 3)/3."""
    for k in range(8):
        expected = sp.Rational(2 * bin(k).count("1") - 3, 3)
        assert BmL[k, k] == expected, f"BmL[{k},{k}] = {BmL[k, k]} ≠ {expected}"


def test_BmL_equals_Hamming_formula():
    """BmL = (2H - 3I)/3 where H is the Hamming weight operator."""
    BmL_from_H = (2 * Hamming - 3 * I8) * sp.Rational(1, 3)
    assert BmL - BmL_from_H == zeros(8, 8)


def test_Hamming_diagonal_entries():
    """H[k,k] = popcount(k) for k in {0..7}."""
    for k in range(8):
        assert Hamming[k, k] == bin(k).count("1")


def test_sigma3_sum_structure():
    """Sum of individual σ₃ operators has correct diagonal."""
    S = sigma3_1 + sigma3_2 + sigma3_3
    for k in range(8):
        expected = 3 - 2 * bin(k).count("1")  # = popcount-based formula
        assert S[k, k] == expected


def test_BmL_hermitian():
    """B-L is Hermitian: BmL† = BmL (physical observable)."""
    assert BmL - BmL.H == zeros(8, 8)


# ── Commutativity ─────────────────────────────────────────────────────────────


def test_BmL_commutes_Gamma7():
    """[B-L, Γ₇] = 0 (both diagonal, B-L compatible with chirality split)."""
    assert BmL * Gamma7 - Gamma7 * BmL == zeros(8, 8)


def test_BmL_commutes_all_SU3_generators():
    """[B-L, C^spin_i] = 0 for all 8 SU(3)_color generators."""
    for i, C in enumerate(su3_spin):
        assert BmL * C - C * BmL == zeros(8, 8), f"B-L fails to commute with C_{i}"


# ── Sector assignments ────────────────────────────────────────────────────────


def test_quark_sector_BmL():
    """All three quark states {|011⟩,|101⟩,|110⟩} have B-L = +1/3."""
    for j in QUARK:
        assert BmL[j, j] == BmL_Q, f"|{j}⟩ has B-L={BmL[j, j]} ≠ 1/3"


def test_antiquark_sector_BmL():
    """All three antiquark states {|001⟩,|010⟩,|100⟩} have B-L = -1/3."""
    for j in AQUARK:
        assert BmL[j, j] == BmL_AQ, f"|{j}⟩ has B-L={BmL[j, j]} ≠ -1/3"


def test_lepton_singlet_BmL():
    """|000⟩ (lepton singlet, S^+) has B-L = -1."""
    assert BmL[SP_SINGLET, SP_SINGLET] == BmL_LEP


def test_antilepton_singlet_BmL():
    """|111⟩ (G13 zero mode, S^-) has B-L = +1."""
    assert BmL[SM_SINGLET, SM_SINGLET] == BmL_ALEP


def test_sector_values_distinct():
    """The four sector B-L values are distinct (non-trivial charge assignment)."""
    vals = [BmL[0, 0], BmL[3, 3], BmL[1, 1], BmL[7, 7]]
    assert len(set(vals)) == 4


def test_BmL_constant_in_quark_sector():
    """B-L is constant within the quark triplet (Schur: irrep → scalar)."""
    assert BmL[3, 3] == BmL[5, 5] == BmL[6, 6]


def test_BmL_constant_in_antiquark_sector():
    """B-L is constant within the antiquark antitriplet."""
    assert BmL[1, 1] == BmL[2, 2] == BmL[4, 4]


# ── Proportionality to J (almost-complex structure) ──────────────────────────


def test_lift_J_proportional_to_BmL():
    """lift_to_spinor(J) = -(3i/2)·BmL: B-L is the spinor lift of the u(1) center."""
    J_geom = complex_structure()
    J_spin = lift_to_spinor(J_geom)
    expected = BmL * sp.Rational(-3, 2) * sp.I
    assert J_spin - expected == zeros(8, 8)


def test_lift_J_is_anti_hermitian():
    """lift_to_spinor(J) is anti-Hermitian (as expected for an so(6) generator)."""
    J_geom = complex_structure()
    J_spin = lift_to_spinor(J_geom)
    assert J_spin + J_spin.H == zeros(8, 8)


# ── Hypercharge formula ───────────────────────────────────────────────────────


def test_Y_T3R0_lepton_singlet():
    """Y = (B-L)/2 for T3R=0: |000⟩ (lepton) has Y = -1/2."""
    Y = BmL[0, 0] * sp.Rational(1, 2)
    assert Y == sp.Rational(-1, 2)


def test_Y_T3R0_antilepton_singlet():
    """Y = (B-L)/2 for T3R=0: |111⟩ (anti-lepton) has Y = +1/2."""
    Y = BmL[7, 7] * sp.Rational(1, 2)
    assert Y == sp.Rational(1, 2)


def test_Gell_Mann_Nishijima_nu_R():
    """Y = T3R + (B-L)/2: ν_R has B-L=-1, T3R=+1/2 → Y=0."""
    Y = sp.Rational(1, 2) + BmL_LEP * sp.Rational(1, 2)
    assert Y == sp.Integer(0)


def test_Gell_Mann_Nishijima_e_R():
    """Y = T3R + (B-L)/2: e_R has B-L=-1, T3R=-1/2 → Y=-1."""
    Y = sp.Rational(-1, 2) + BmL_LEP * sp.Rational(1, 2)
    assert Y == sp.Integer(-1)


def test_Gell_Mann_Nishijima_u_R():
    """Y = T3R + (B-L)/2: u_R has B-L=+1/3, T3R=+1/2 → Y=+2/3."""
    Y = sp.Rational(1, 2) + BmL_Q * sp.Rational(1, 2)
    assert Y == sp.Rational(2, 3)


def test_Gell_Mann_Nishijima_d_R():
    """Y = T3R + (B-L)/2: d_R has B-L=+1/3, T3R=-1/2 → Y=-1/3."""
    Y = sp.Rational(-1, 2) + BmL_Q * sp.Rational(1, 2)
    assert Y == sp.Rational(-1, 3)
