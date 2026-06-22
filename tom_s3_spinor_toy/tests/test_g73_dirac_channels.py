"""Tests for G73: Three-channel Dirac index on S³×S⁶ → N_gen = 3."""

import os
import sys
from fractions import Fraction

_exp_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260621-g73-three-channel-dirac"
)
sys.path.insert(0, _exp_dir)

from g73_dirac import (  # noqa: E402
    A_HAT_S6,
    C3_8C,
    C3_8S,
    C3_8V,
    C3_S_MINUS,
    C3_T10_S6,
    C3_TRIVIAL,
    CHANNELS,
    DIM_FULL_SPINOR_PER_CHANNEL,
    DIM_S3_SPINOR,
    DIM_S6_SPINOR,
    DIM_TOTAL_SPINOR,
    G73_RESULT,
    INDEX_PER_CHANNEL,
    INDICES,
    N_GEN,
    N_TRIALITY_CHANNELS,
    ONE_GEN_FULL,
    ONE_GEN_SU3,
    S_MINUS_SPLITS_AS,
    THREE_GEN_FULL,
    THREE_GEN_SU3,
    TOTAL_INDEX,
    c3_direct_sum,
    dirac_index_s6,
)


# ─── G73-A: Tensor product structure ─────────────────────────────────────────


def test_s3_spinor_dimension():
    """S³ Dirac spinor = 4 (Spin(3)=SU(2) Dirac rep)."""
    assert DIM_S3_SPINOR == 4


def test_s6_spinor_dimension():
    """S⁶ Dirac spinor = 8 (Spin(6)=SU(4) Dirac = S⁺ ⊕ S⁻ = 4+4)."""
    assert DIM_S6_SPINOR == 8


def test_tensor_product_spinor_per_channel():
    """S(S³×S⁶) = S(S³) ⊗ S(S⁶) = 4 ⊗ 8 = 32 per channel."""
    assert DIM_FULL_SPINOR_PER_CHANNEL == DIM_S3_SPINOR * DIM_S6_SPINOR
    assert DIM_FULL_SPINOR_PER_CHANNEL == 32


def test_three_channels_total_dimension():
    """Total spinor space = 3 channels × 32 = 96."""
    assert DIM_TOTAL_SPINOR == N_TRIALITY_CHANNELS * DIM_FULL_SPINOR_PER_CHANNEL
    assert DIM_TOTAL_SPINOR == 96


# ─── G73-B: S⁻ bundle splitting ──────────────────────────────────────────────


def test_s_minus_splits_into_triplet_plus_singlet():
    """S⁻ of Spin(6): 4 → 3+1 under SU(3) (T^{1,0}S⁶ ⊕ trivial)."""
    assert S_MINUS_SPLITS_AS["triplet"] == 3
    assert S_MINUS_SPLITS_AS["singlet"] == 1


def test_s_minus_total_dimension():
    """Dim(S⁻) = 3 + 1 = 4 (half the 8-dim Dirac spinor)."""
    assert sum(S_MINUS_SPLITS_AS.values()) == 4


def test_s_plus_and_s_minus_cover_full_spinor():
    """S⁺ (4) + S⁻ (4) = 8-dim S⁶ spinor."""
    dim_s_plus = 4  # 4̄→3̄+1 under SU(3)
    dim_s_minus = sum(S_MINUS_SPLITS_AS.values())  # 4→3+1
    assert dim_s_plus + dim_s_minus == DIM_S6_SPINOR


# ─── G73-C: Chern class computation ──────────────────────────────────────────


def test_c3_t10_s6_from_g33():
    """c₃(T^{1,0}S⁶) = χ(S⁶) = 2 (from G33: Chern-Gauss-Bonnet)."""
    assert C3_T10_S6 == 2


def test_c3_trivial_bundle():
    """c₃(trivial rank-1 bundle) = 0."""
    assert C3_TRIVIAL == 0


def test_c3_direct_sum_formula():
    """c₃(A⊕B) = c₃(A)+c₃(B) when c₁=c₂=0 (valid on S⁶)."""
    assert c3_direct_sum(2, 0) == 2
    assert c3_direct_sum(0, 0) == 0
    assert c3_direct_sum(2, 2) == 4
    assert c3_direct_sum(-2, 2) == 0


def test_c3_s_minus_equals_c3_t10():
    """c₃(S⁻) = c₃(T^{1,0}S⁶ ⊕ trivial) = 2 + 0 = 2."""
    assert C3_S_MINUS == c3_direct_sum(C3_T10_S6, C3_TRIVIAL)
    assert C3_S_MINUS == 2


# ─── G73-D: Atiyah-Singer index ──────────────────────────────────────────────


def test_a_hat_s6_equals_one():
    """Â(S⁶) = 1 exactly: p₁=0 since H⁴(S⁶)=0, so Â = 1-p₁/24+... = 1."""
    assert A_HAT_S6 == 1


def test_index_formula_zero_bundle():
    """ind(D⊗trivial) = c₃(0)/2 = 0."""
    assert dirac_index_s6(0) == Fraction(0)


def test_index_formula_c3_equals_2():
    """ind(D⊗E) = 2/2 = 1 when c₃(E)=2."""
    assert dirac_index_s6(2) == Fraction(1)


def test_index_formula_c3_equals_6():
    """ind(D⊗E) = 6/2 = 3 when c₃(E)=6."""
    assert dirac_index_s6(6) == Fraction(3)


def test_index_per_channel_is_one():
    """ind(D_{S⁶} ⊗ S⁻) = c₃(S⁻)/2 = 2/2 = 1 per triality channel."""
    assert INDEX_PER_CHANNEL == Fraction(1)


# ─── G73-E: Triality invariance ──────────────────────────────────────────────


def test_all_channels_have_same_c3():
    """Z₃ triality preserves c₃: c₃(8_v) = c₃(8_s) = c₃(8_c) = 2."""
    assert C3_8V == C3_8S == C3_8C == 2


def test_all_channels_have_same_index():
    """All three channels give index 1 (by triality invariance)."""
    for idx in INDICES:
        assert idx == Fraction(1)


def test_three_channels_present():
    """CHANNELS dict has exactly 8_v, 8_s, 8_c."""
    assert set(CHANNELS.keys()) == {"8_v", "8_s", "8_c"}


# ─── G73-F: N_gen = 3 ────────────────────────────────────────────────────────


def test_total_index_equals_three():
    """Total index = sum over channels = 1+1+1 = 3."""
    assert TOTAL_INDEX == Fraction(3)


def test_n_gen_equals_three():
    """N_gen = int(total index) = 3."""
    assert N_GEN == 3


def test_n_gen_matches_triality_orbit():
    """N_gen = 3 = |Z₃ orbit| from G67 — two independent derivations agree."""
    assert N_GEN == N_TRIALITY_CHANNELS


# ─── G73-G: Fermion content ──────────────────────────────────────────────────


def test_one_generation_su3_content():
    """One generation = 3+3̄+2 under SU(3): triplet + antitriplet + 2 singlets."""
    assert ONE_GEN_SU3["triplet"] == 3
    assert ONE_GEN_SU3["antitriplet"] == 3
    assert ONE_GEN_SU3["singlet"] == 2


def test_one_generation_dimension_matches_s6_spinor():
    """Sum of SU(3) content = 8 = dim(S⁶ spinor)."""
    assert sum(ONE_GEN_SU3.values()) == DIM_S6_SPINOR


def test_three_generations_su3_content():
    """Three generations = 3×(3+3̄+2) = 9+9̄+6 under SU(3)."""
    assert THREE_GEN_SU3["triplet"] == 9
    assert THREE_GEN_SU3["antitriplet"] == 9
    assert THREE_GEN_SU3["singlet"] == 6


def test_one_generation_full_state_count():
    """One full generation = S(S³) ⊗ S(S⁶) = 4 × 8 = 32 states."""
    assert ONE_GEN_FULL == 32


def test_three_generations_full_state_count():
    """Three generations = 3 × 32 = 96 states total."""
    assert THREE_GEN_FULL == 96


# ─── G73 summary ─────────────────────────────────────────────────────────────


def test_g73_result_status():
    """G73 result is marked PROMOTE."""
    assert G73_RESULT["status"] == "PROMOTE"


def test_g73_result_summary():
    """G73 summary record is self-consistent."""
    assert G73_RESULT["N_gen"] == 3
    assert G73_RESULT["index_per_channel"] == Fraction(1)
    assert G73_RESULT["total_index"] == Fraction(3)
    assert G73_RESULT["c3_per_channel"] == 2
    assert G73_RESULT["A_hat_S6"] == 1
    assert G73_RESULT["states_per_gen"] == 32
    assert G73_RESULT["total_states"] == 96


# ─── Cross-gate integration ───────────────────────────────────────────────────


def test_n_triality_channels_matches_g67():
    """N_TRIALITY_CHANNELS in G73 matches G67's three SO(8) triality channels.

    G67 establishes the three independent Z₃-triality channels (8_v, 8_s, 8_c).
    G73 imports this count as N_TRIALITY_CHANNELS = 3.
    This test ensures the two modules stay consistent.
    """
    _g67_dir = os.path.join(
        os.path.dirname(__file__), "..", "experiments", "20260621-g67-octonion-triality"
    )
    sys.path.insert(0, _g67_dir)
    from g67_triality import N_CHANNELS as G67_N_CHANNELS  # noqa: PLC0415

    assert N_TRIALITY_CHANNELS == G67_N_CHANNELS, (
        f"G73 N_TRIALITY_CHANNELS={N_TRIALITY_CHANNELS} ≠ G67 N_CHANNELS={G67_N_CHANNELS}"
    )
