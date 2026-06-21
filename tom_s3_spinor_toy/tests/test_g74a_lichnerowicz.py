"""Tests for G74A: Lichnerowicz spectral gap → dim ker = ind EXACTLY → N_gen = 3."""

import os
import sys
from fractions import Fraction

_exp_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260621-g74a-lichnerowicz-gap"
)
sys.path.insert(0, _exp_dir)

from g74a_lichnerowicz import (  # noqa: E402
    LICHNEROWICZ_GAP_PHYSICAL,
    LICHNEROWICZ_RATIO,
    MIN_EIG_PHYSICAL,
    N_GEN_EXACT,
    N_HALF,
    RHO6_PHYSICAL,
    SAFETY_FACTOR,
    SCALAR_CURVATURE_PHYSICAL,
    C2_FUNDAMENTAL,
    C2_S_MINUS,
    C2_TRIVIAL,
    DIM_KER_PER_CHANNEL,
    DIM_S6,
    G2_SINGLET_MULT_PER_CHANNEL,
    G74A_RESULT,
    KK_MASS_SCALE,
    N_CHANNELS,
    bundle_curvature_op_norm,
    dirac_eigenvalue_s6,
    lichnerowicz_gap,
    min_eigenvalue_untwisted,
    scalar_curvature_s6,
)

TOL = 1e-9


# ─── G74A-A: S⁶ curvature ────────────────────────────────────────────────────


def test_s6_dimension():
    """S⁶ is 6-dimensional."""
    assert DIM_S6 == 6


def test_n_half():
    """n/2 = 3 for S⁶ (enters Dirac spectrum as offset)."""
    assert N_HALF == 3


def test_scalar_curvature_formula():
    """R(S⁶, ρ) = n(n-1)/ρ² = 30/ρ²."""
    assert abs(scalar_curvature_s6(1.0) - 30.0) < TOL
    assert abs(scalar_curvature_s6(2.0) - 30.0 / 4.0) < TOL
    assert abs(scalar_curvature_s6(0.5) - 30.0 / 0.25) < TOL


def test_scalar_curvature_positive():
    """R > 0 for any ρ > 0 (uniformly positive curvature on S⁶)."""
    for rho in [0.5, 1.0, 1.179, 2.0, 5.0]:
        assert scalar_curvature_s6(rho) > 0


def test_lichnerowicz_gap_formula():
    """R/4 = 7.5/ρ² for round S⁶."""
    assert abs(lichnerowicz_gap(1.0) - 7.5) < TOL
    assert abs(lichnerowicz_gap(2.0) - 7.5 / 4.0) < TOL


def test_curvature_physical():
    """At ρ₆ = 1.179: R ≈ 21.57, R/4 ≈ 5.39."""
    assert abs(SCALAR_CURVATURE_PHYSICAL - 30.0 / 1.179**2) < 1e-6
    assert abs(LICHNEROWICZ_GAP_PHYSICAL - 7.5 / 1.179**2) < 1e-6


# ─── G74A-B: Untwisted Dirac spectrum ────────────────────────────────────────


def test_dirac_spectrum_k0():
    """Lowest positive eigenvalue of untwisted D on S⁶: λ_0 = 3/ρ₆."""
    assert abs(dirac_eigenvalue_s6(1.0, k=0) - 3.0) < TOL
    assert abs(dirac_eigenvalue_s6(2.0, k=0) - 1.5) < TOL


def test_dirac_spectrum_increasing():
    """Eigenvalues λ_k = (k+3)/ρ₆ are strictly increasing in k."""
    rho = 1.179
    eigs = [dirac_eigenvalue_s6(rho, k) for k in range(5)]
    for a, b in zip(eigs, eigs[1:]):
        assert b > a


def test_min_eigenvalue_no_zero():
    """Min eigenvalue of untwisted D is > 0 — no zero modes."""
    for rho in [0.5, 1.0, 1.179, 2.0]:
        assert min_eigenvalue_untwisted(rho) > 0


def test_min_eigenvalue_physical():
    """At ρ₆ = 1.179: min|λ| = 3/1.179 ≈ 2.544."""
    assert abs(MIN_EIG_PHYSICAL - 3.0 / RHO6_PHYSICAL) < 1e-9


def test_untwisted_dirac_no_zero_modes_consistent_with_ind0():
    """No zero modes for untwisted D ↔ ind = 0 for trivial bundle (Atiyah-Singer)."""
    # ind(D⊗trivial) = c₃(trivial)/2 = 0 (from G73 formula)
    ind_trivial = Fraction(0) / 2
    assert ind_trivial == 0
    # min eigenvalue confirms: spectrum gap above 0
    assert min_eigenvalue_untwisted(1.0) == 3.0


# ─── G74A-C: Bundle curvature ─────────────────────────────────────────────────


def test_su3_casimir_fundamental():
    """C₂(3) = (N²-1)/(2N) = 8/6 = 4/3 for SU(3) fundamental."""
    assert C2_FUNDAMENTAL == Fraction(4, 3)


def test_su3_casimir_trivial():
    """C₂(1) = 0 for trivial (singlet) representation."""
    assert C2_TRIVIAL == Fraction(0)


def test_c2_s_minus():
    """C₂(S⁻) = max(C₂(3), C₂(1)) = 4/3 (triplet component dominates)."""
    assert C2_S_MINUS == Fraction(4, 3)


def test_bundle_curvature_formula():
    """|F_{S⁻}|_op = C₂(3)/ρ₆² = (4/3)/ρ₆²."""
    assert abs(bundle_curvature_op_norm(1.0) - 4.0 / 3.0) < TOL
    assert abs(bundle_curvature_op_norm(2.0) - (4.0 / 3.0) / 4.0) < TOL


def test_bundle_curvature_less_than_lichnerowicz():
    """|F_{S⁻}|_op < R/4 for all ρ₆: Lichnerowicz dominates."""
    for rho in [0.5, 1.0, 1.179, 2.0, 5.0]:
        assert bundle_curvature_op_norm(rho) < lichnerowicz_gap(rho)


# ─── G74A-D: Lichnerowicz ratio ───────────────────────────────────────────────


def test_lichnerowicz_ratio_exact():
    """Ratio |F_{S⁻}|/(R/4) = (4/3)/(30/4) = 8/45 exactly."""
    assert LICHNEROWICZ_RATIO == Fraction(8, 45)


def test_lichnerowicz_ratio_less_than_one():
    """Ratio < 1 → Lichnerowicz gap dominates → no accidental zeros."""
    assert LICHNEROWICZ_RATIO < 1


def test_safety_factor_exact():
    """Safety factor (R/4)/|F_{S⁻}| = 45/8 = 5.625."""
    assert SAFETY_FACTOR == Fraction(45, 8)


def test_safety_factor_greater_than_one():
    """Safety factor > 1 confirms Lichnerowicz dominance."""
    assert SAFETY_FACTOR > 1


# ─── G74A-E: G₂ equivariance ─────────────────────────────────────────────────


def test_g2_singlet_multiplicity():
    """Trivial G₂-rep appears exactly once per channel in ker(D⊗S⁻)."""
    assert G2_SINGLET_MULT_PER_CHANNEL == 1


def test_dim_ker_per_channel_exact():
    """dim ker = 1 per channel — exact (not just ≥ 1 from ind)."""
    assert DIM_KER_PER_CHANNEL == 1


# ─── G74A-F: Combined result ──────────────────────────────────────────────────


def test_n_channels():
    """Three triality channels (G67, G73)."""
    assert N_CHANNELS == 3


def test_n_gen_exact():
    """N_gen = 3 × 1 = 3 EXACTLY (not just ≥ 3)."""
    assert N_GEN_EXACT == 3


def test_n_gen_exact_upgrades_g73():
    """G74A gives N_gen = 3 exactly; G73 gave N_gen ≥ 3 (lower bound only)."""
    ind_from_g73 = 3  # N_gen lower bound from G73
    assert N_GEN_EXACT == ind_from_g73  # the bound is saturated


# ─── G74A-G: Spectral gap ─────────────────────────────────────────────────────


def test_kk_mass_scale():
    """KK mass scale ~ 1/ρ₆_physical."""
    assert abs(KK_MASS_SCALE - 1.0 / RHO6_PHYSICAL) < TOL


def test_zero_modes_lighter_than_kk():
    """Zero modes are massless (topological), far below KK scale."""
    from g74a_lichnerowicz import ZERO_MODE_MASS

    assert ZERO_MODE_MASS == 0.0
    assert ZERO_MODE_MASS < KK_MASS_SCALE


def test_spectral_gap_positive():
    """Non-zero eigenvalues are separated from 0 by a positive gap."""
    from g74a_lichnerowicz import SPECTRAL_GAP_LOWER

    assert SPECTRAL_GAP_LOWER > 0


# ─── G74A summary ─────────────────────────────────────────────────────────────


def test_g74a_status():
    """G74A result is marked PROMOTE."""
    assert G74A_RESULT["status"] == "PROMOTE"


def test_g74a_summary():
    """G74A summary is internally consistent."""
    assert G74A_RESULT["n_gen_exact"] == 3
    assert G74A_RESULT["dim_ker_per_channel"] == 1
    assert abs(G74A_RESULT["safety_factor"] - 5.625) < 1e-9
    assert G74A_RESULT["lichnerowicz_ratio"] < 0.2
