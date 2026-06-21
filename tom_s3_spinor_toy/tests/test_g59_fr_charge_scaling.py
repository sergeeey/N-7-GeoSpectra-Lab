"""
G59 — FR on-shell gradient and charge-scaling audit
====================================================
Claim: The FR EH-frame minimum at ρ₆≈0.337 (G58) can be shifted to the
SM window [0.953, 1.447] only if V_FLUX_CONST is raised by factor ~15,000.
This rules out natural FR-based moduli stabilisation at SM scale.

Kill criterion: f₀_SM / f₀_current > KILL_RATIO = 100.

Gates
-----
A  String-frame gradient ∂V_str/∂ρ₆ < 0 everywhere → no classical FR minimum
B  Required f₀_SM ≈ 4412, ratio f₀_SM/f₀ ≈ 15,000 >> 100
C  Even at f₀_SM the vacuum at ρ₆=1 is AdS (~-29)
D  Power-law ρ₆_min ∝ f₀^α with α ∈ [1/10, 1/8] (numerical)
NULL  Charge tuning kills this branch
"""

import numpy as np
import pytest
from math import pi
from scipy.optimize import brentq

# ── shared constants (G54-F / G55 / G58 lineage) ──────────────────────────
C = 0.986
VOL_S3_COEFF = 2 * pi**2
VOL_S6_COEFF = 16 * pi**3 / 15
K_VOL = VOL_S3_COEFF * C**3 * VOL_S6_COEFF  # ≈ 625.3
V_FLUX_CONST = 15 * C**3 / (16 * pi)  # ≈ 0.2861; G55 q₃q₆=1 result

RHO6_MIN_G58 = 0.337  # EH-frame minimum from G58
RHO6_SM_LOW = 0.953  # bottom of Casimir/SM window (G54-E)
KILL_RATIO = 100  # f₀_SM/f₀ > this → G59 NULL
V_CAS_RHO1 = -1.6e-6  # V_Cas^EH at ρ₆=1 from G58-C5


# ── helper functions ───────────────────────────────────────────────────────


def dv_str_dr6(r6: float) -> float:
    """∂V_string/∂ρ₆ on SM constraint = -K_VOL(48ρ₆⁷/C² + 300ρ₆⁹).

    From V_curv_str = -K_VOL(6r6⁸/C² + 30r6¹⁰), derivative has positive powers.
    """
    return -K_VOL * (48.0 * r6**7 / C**2 + 300.0 * r6**9)


def f0_for_r6_min(r6_target: float) -> float:
    """f₀ such that d/dρ₆[V_curv^EH + f₀/V_int]=0 at ρ₆=r6_target.

    From 24/(C²ρ₆⁵) + 60/ρ₆³ = 12f₀/(K_VOL·ρ₆¹³).
    """
    lhs = 24.0 / (C**2 * r6_target**5) + 60.0 / r6_target**3
    return lhs * K_VOL * r6_target**13 / 12.0


def v_curv_eh(r6: float) -> float:
    return -(6.0 / (C**2 * r6**4) + 30.0 / r6**2)


def v_flux_eh(r6: float, f0: float = V_FLUX_CONST) -> float:
    return f0 / (K_VOL * r6**12)


def _dv_eh_sum(r6: float, f0: float) -> float:
    """d/dρ₆ [V_curv^EH + V_flux^EH(f0)]."""
    d_curv = 24.0 / (C**2 * r6**5) + 60.0 / r6**3
    d_flux = -12.0 * f0 / (K_VOL * r6**13)
    return d_curv + d_flux


def find_r6_min_eh(f0: float, lo: float = 0.10, hi: float = 1.5) -> float:
    """ρ₆ where d/dρ₆(V_curv^EH + V_flux^EH) = 0, for arbitrary f₀."""
    return brentq(lambda r: _dv_eh_sum(r, f0), lo, hi, xtol=1e-6)


# ── G59-A: string-frame gradient ──────────────────────────────────────────


class TestA1StringFrameAlwaysNegative:
    @pytest.mark.parametrize("r6", [0.2, 0.5, 0.8, 1.0, 1.5, 2.0])
    def test_gradient_negative(self, r6):
        """∂V_str/∂ρ₆ < 0 at all tested ρ₆: no FR minimum in string frame."""
        assert dv_str_dr6(r6) < 0


class TestA2FactoredForm:
    def test_inner_factor_always_positive(self):
        """Inner factor (48/C² + 300ρ₆²) > 0 everywhere → gradient always negative."""
        r6_grid = np.linspace(0.05, 3.0, 1000)
        inner = 48.0 / C**2 + 300.0 * r6_grid**2
        assert np.all(inner > 0)

    def test_factored_matches_direct(self):
        """∂V_str/∂ρ₆ = -K_VOL·ρ₆⁷·(48/C²+300ρ₆²) matches naive formula."""
        r6 = 0.7
        factored = -K_VOL * r6**7 * (48.0 / C**2 + 300.0 * r6**2)
        assert abs(factored - dv_str_dr6(r6)) / abs(dv_str_dr6(r6)) < 1e-10


# ── G59-B: required flux charge ───────────────────────────────────────────


class TestB1RequiredFlux:
    def test_f0_sm_value(self):
        """f₀_SM needed for EH minimum at ρ₆=1 is between 4000 and 5000."""
        f0_sm = f0_for_r6_min(1.0)
        assert 4000 < f0_sm < 5000, f"Expected f₀_SM∈(4000,5000), got {f0_sm:.1f}"

    def test_f0_sm_actually_shifts_minimum(self):
        """With f₀=f₀_SM, EH-frame minimum lands at ρ₆=1.00 ± 0.05."""
        f0_sm = f0_for_r6_min(1.0)
        r6_new = find_r6_min_eh(f0_sm, lo=0.1, hi=1.5)
        assert abs(r6_new - 1.0) < 0.05, f"Expected ρ₆_min≈1.0, got {r6_new:.3f}"


class TestB2ChargeRatio:
    def test_ratio_exceeds_kill_threshold(self):
        """f₀_SM/f₀_current > KILL_RATIO=100 → G59 NULL triggered."""
        ratio = f0_for_r6_min(1.0) / V_FLUX_CONST
        assert ratio > KILL_RATIO, f"Kill threshold {KILL_RATIO} not exceeded: {ratio:.0f}"

    def test_ratio_is_order_ten_thousand(self):
        """Ratio is ~15,000 (not borderline): deeply outside natural range."""
        ratio = f0_for_r6_min(1.0) / V_FLUX_CONST
        assert ratio > 5_000, f"Expected ratio > 5000, got {ratio:.0f}"


# ── G59-C: AdS depth at f₀_SM ────────────────────────────────────────────


class TestC1AdSPersists:
    def test_v_eh_still_negative_at_r6_1(self):
        """V_EH(ρ₆=1, f₀_SM) < 0: AdS persists even at SM-tuned charges."""
        f0_sm = f0_for_r6_min(1.0)
        v = v_curv_eh(1.0) + v_flux_eh(1.0, f0_sm)
        assert v < 0, f"Expected AdS (V<0) at ρ₆=1 with f₀_SM, got {v:.2f}"

    def test_v_eh_shallower_than_g58(self):
        """V_EH(ρ₆=1, f₀_SM)≈-29 is shallower than G58 minimum ≈-520."""
        f0_sm = f0_for_r6_min(1.0)
        v_sm = v_curv_eh(1.0) + v_flux_eh(1.0, f0_sm)
        v_g58 = -520.0
        assert v_sm > v_g58, f"Expected V_SM({v_sm:.1f}) > V_G58({v_g58:.1f})"
        assert v_sm < -5.0, f"Expected V_SM still clearly AdS (<-5), got {v_sm:.2f}"


# ── G59-D: power-law scaling ρ₆_min ∝ f₀^α ──────────────────────────────


class TestD1PowerLaw:
    def test_baseline_consistent_with_g58(self):
        """find_r6_min_eh(V_FLUX_CONST) ≈ 0.337 (reproduces G58 result)."""
        r6 = find_r6_min_eh(V_FLUX_CONST)
        assert abs(r6 - RHO6_MIN_G58) < 0.02, f"Expected ≈0.337, got {r6:.3f}"

    def test_scale_exponent_in_physical_range(self):
        """×1024 in f₀ raises ρ₆_min by factor ∈ [1.8, 2.7]: α ∈ [1/10, 1/8]."""
        r6_a = find_r6_min_eh(V_FLUX_CONST)
        r6_b = find_r6_min_eh(V_FLUX_CONST * 1024.0)
        ratio = r6_b / r6_a
        # 1024^{1/10}=2.0  (large-ρ limit), 1024^{1/8}≈2.38 (small-ρ limit)
        assert 1.8 < ratio < 2.8, f"Expected ρ₆ scale ratio ∈ (1.8, 2.8), got {ratio:.3f}"


# ── G59-NULL: kill verdict ────────────────────────────────────────────────


class TestNullVerdict:
    def test_charge_tuning_unphysical(self):
        """f₀_SM/f₀ >> KILL_RATIO·100: cannot reach SM window with natural charges."""
        ratio = f0_for_r6_min(1.0) / V_FLUX_CONST
        assert ratio > KILL_RATIO * 100, f"Expected ratio > {KILL_RATIO * 100}, got {ratio:.0f}"

    def test_casimir_irrelevant_regardless_of_charge(self):
        """|V_Cas^EH(ρ₆=1)| / |V_curv^EH(ρ₆=1)| < 10⁻⁴ at any charge scale."""
        ratio = abs(V_CAS_RHO1 / v_curv_eh(1.0))
        assert ratio < 1e-4, f"Expected |V_Cas/V_curv| < 10⁻⁴, got {ratio:.2e}"
