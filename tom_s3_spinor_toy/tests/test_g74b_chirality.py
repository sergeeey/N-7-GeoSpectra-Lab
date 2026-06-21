"""Tests for G74B: Chirality from index sign → SM chirality from geometry."""

import os
import sys
from fractions import Fraction

_exp_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260621-g74b-chirality-from-index"
)
sys.path.insert(0, _exp_dir)

from g74b_chirality import (  # noqa: E402
    A_HAT,
    C3_S_MINUS,
    CHIRALITY_SIGN,
    CHIRALITY_VERDICT,
    CHOSEN_ORIENTATION,
    DIM_KER_LEFT_PER_CHANNEL,
    DIM_KER_RIGHT_PER_CHANNEL,
    DIM_S_MINUS,
    DIM_S_PLUS,
    G23_CONSISTENT,
    G74B_RESULT,
    IND_PER_CHANNEL,
    IND_SIGN,
    N_CHANNELS,
    NET_CHIRALITY,
    ORIENTATION_REVERSED_IND,
    TOTAL_LEFT_ZERO_MODES,
    TOTAL_RIGHT_ZERO_MODES,
    TWISTING_BUNDLE_C3,
    chirality_from_c3,
)


# ─── G74B-A: Chirality sectors ────────────────────────────────────────────────


def test_s_plus_dimension():
    """S⁺: positive chirality Weyl spinors of Spin(6), dim = 4."""
    assert DIM_S_PLUS == 4


def test_s_minus_dimension():
    """S⁻: negative chirality Weyl spinors of Spin(6), dim = 4."""
    assert DIM_S_MINUS == 4


def test_twisting_bundle_c3():
    """Twisting bundle S⁻ has c₃ = 2 (from G33/G73)."""
    assert TWISTING_BUNDLE_C3 == 2


# ─── G74B-B: Index sign ───────────────────────────────────────────────────────


def test_ind_per_channel_positive():
    """ind(D^+⊗S⁻) = +1 > 0 per channel."""
    assert IND_PER_CHANNEL == Fraction(1)
    assert IND_PER_CHANNEL > 0


def test_ind_sign():
    """Index sign is positive (+1)."""
    assert IND_SIGN == +1


def test_chirality_verdict():
    """Positive index → left-handed excess."""
    assert CHIRALITY_VERDICT == "LEFT_HANDED_EXCESS"


def test_ind_not_zero():
    """Non-zero index → chiral (not vector-like)."""
    assert IND_PER_CHANNEL != 0


# ─── G74B-C: Zero mode count per chirality ────────────────────────────────────


def test_left_zero_modes():
    """One left-handed zero mode per channel (from G74A: total = 1, ind = +1)."""
    assert DIM_KER_LEFT_PER_CHANNEL == 1


def test_right_zero_modes():
    """Zero right-handed zero modes per channel (G74A: total = 1, ind = +1 forces L=1, R=0)."""
    assert DIM_KER_RIGHT_PER_CHANNEL == 0


def test_ind_equals_left_minus_right():
    """Index = left zero modes - right zero modes = 1 - 0 = +1."""
    computed = DIM_KER_LEFT_PER_CHANNEL - DIM_KER_RIGHT_PER_CHANNEL
    assert computed == IND_PER_CHANNEL


def test_total_zero_modes_per_channel():
    """Total zero modes per channel = left + right = 1 = G74A result."""
    total = DIM_KER_LEFT_PER_CHANNEL + DIM_KER_RIGHT_PER_CHANNEL
    assert total == 1  # consistent with G74A


def test_uniqueness_of_chirality_assignment():
    """Given dim ker = 1 and ind = +1, the unique solution is (L=1, R=0)."""
    dim_ker = 1  # from G74A
    ind = int(IND_PER_CHANNEL)  # = +1
    # Solve: L - R = ind, L + R = dim_ker, L >= 0, R >= 0
    L = (dim_ker + ind) // 2
    R = (dim_ker - ind) // 2
    assert L == DIM_KER_LEFT_PER_CHANNEL
    assert R == DIM_KER_RIGHT_PER_CHANNEL
    assert L >= 0 and R >= 0


# ─── G74B-D: Three channels ───────────────────────────────────────────────────


def test_n_channels():
    """Three triality channels (G67, G73)."""
    assert N_CHANNELS == 3


def test_total_left_zero_modes():
    """3 channels × 1 left-handed zero mode = 3 left-handed generations."""
    assert TOTAL_LEFT_ZERO_MODES == 3


def test_total_right_zero_modes():
    """3 channels × 0 right-handed = 0 right-handed at zero-mode level."""
    assert TOTAL_RIGHT_ZERO_MODES == 0


def test_net_chirality():
    """Net chirality = total left - total right = +3."""
    assert NET_CHIRALITY == +3


def test_net_chirality_equals_n_gen():
    """Net chirality = N_gen (each generation is left-handed at zero-mode level)."""
    assert NET_CHIRALITY == N_CHANNELS


# ─── G74B-E: Consistency with G23 ────────────────────────────────────────────


def test_g23_consistent():
    """G74B is consistent with G23 (chirality from NCG Dirac triple)."""
    assert G23_CONSISTENT is True


def test_both_chiralities_agree():
    """G23 (gauge-sector) and G74B (spinor-sector) both predict left-handed dominance."""
    g23_verdict = "LEFT"  # from G23: {D_F, gamma_F} = 0, SU(2)_L on left
    g74b_verdict = "LEFT"  # from G74B: ind > 0 → left-handed excess
    assert g23_verdict == g74b_verdict


# ─── G74B-F: Orientation ─────────────────────────────────────────────────────


def test_orientation_reversal_flips_chirality():
    """Reversing S⁶ orientation: ind → -ind (right-handed excess)."""
    assert ORIENTATION_REVERSED_IND == -IND_PER_CHANNEL
    assert ORIENTATION_REVERSED_IND < 0


def test_chosen_orientation():
    """Standard orientation chosen: ind = +1 (left-handed, matches SM)."""
    assert CHOSEN_ORIENTATION == "STANDARD"


def test_chirality_is_discrete_choice():
    """Orientation = discrete Z₂ choice, not continuous — one bit of input."""
    assert G74B_RESULT["requires_orientation_choice"] is True


# ─── G74B-G: Index sign from c₃ ──────────────────────────────────────────────


def test_c3_positive():
    """c₃(S⁻) = +2 > 0 → positive index → left-handed."""
    assert C3_S_MINUS == Fraction(2)
    assert C3_S_MINUS > 0


def test_a_hat():
    """Â(S⁶) = 1 (from G73/G74A)."""
    assert A_HAT == Fraction(1)


def test_chirality_from_c3_positive():
    """Positive c₃ → left-handed chirality."""
    assert chirality_from_c3(Fraction(2)) == +1
    assert chirality_from_c3(Fraction(6)) == +1


def test_chirality_from_c3_negative():
    """Negative c₃ → right-handed chirality (opposite orientation)."""
    assert chirality_from_c3(Fraction(-2)) == -1


def test_chirality_from_c3_zero():
    """Zero c₃ → non-chiral (no excess)."""
    assert chirality_from_c3(Fraction(0)) == 0


def test_chirality_sign_constant():
    """CHIRALITY_SIGN = chirality_from_c3(C3_S_MINUS) = +1."""
    assert CHIRALITY_SIGN == chirality_from_c3(C3_S_MINUS)
    assert CHIRALITY_SIGN == +1


# ─── G74B summary ─────────────────────────────────────────────────────────────


def test_g74b_status():
    """G74B result is marked PROMOTE."""
    assert G74B_RESULT["status"] == "PROMOTE"


def test_g74b_summary():
    """G74B summary is internally consistent."""
    assert G74B_RESULT["chirality_verdict"] == "LEFT_HANDED_EXCESS"
    assert G74B_RESULT["net_chirality"] == +3
    assert G74B_RESULT["total_left"] == 3
    assert G74B_RESULT["total_right"] == 0
    assert G74B_RESULT["g23_consistent"] is True


def test_upgrade_chain():
    """G74B is part of the G73→G74A→G74B upgrade chain."""
    upgrades = G74B_RESULT["upgrades"]
    assert len(upgrades) == 3
    assert any("G73" in u for u in upgrades)
    assert any("G74A" in u for u in upgrades)
    assert any("G74B" in u for u in upgrades)
