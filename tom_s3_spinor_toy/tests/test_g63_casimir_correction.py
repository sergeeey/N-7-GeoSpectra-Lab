"""
G63 — Casimir correction to G62 potential: robustness check.

Question: does adding V_Cas = α·ζ_FP(ρ₆)/(K_VOL·ρ₆¹²) to V_total
          significantly shift ρ_min and m_mod/m_KK from G62 values?

Framework:
  V_total_full = (V_FLUX + V_NP + α·ζ_FP) / (K_VOL·ρ₆¹²)

α is the dimensional coefficient converting ζ_FP into potential units.
Its physical value is unknown without a full string reduction, so this
experiment is a SENSITIVITY ANALYSIS: for what range of α does G62 hold?

Key findings (numerical, see TestG63_SensitivityScan):
  α=0.001 → δρ_min = -0.0005%   (negligible)
  α=0.010 → δρ_min = -0.005%    (negligible)
  α=0.100 → δρ_min = -0.052%    (perturbative)
  α=1.000 → δρ_min = -0.522%    (worst case, still small)

G62 prediction m_mod/m_KK=2.02% is stable:
  α=0.1 → 2.03% (+0.3%)
  α=1.0 → 2.09% (+3.0%)

Verdict: G62 results are ROBUST to Casimir corrections for any physically
reasonable α. One-loop string suppression (α ~ g_s²/4π² ~ 10⁻²) gives
sub-0.01% shifts.
"""

import numpy as np
import pytest
from math import pi, exp, sqrt
from scipy.optimize import minimize_scalar

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from test_g54d_hadamard_fp import zeta_fp, CONSTRAINT_C

# ── Fixed G62 parameters ──────────────────────────────────────────────────────
C = CONSTRAINT_C  # 0.986
V_FLUX = 15 * C**3 / (16 * pi)  # ≈ 0.2861
RHO_STAR = 1.090
LAM = 1 / 3
K_VOL = 2 * pi**2 * 16 * pi**3 / 15
A_NP = V_FLUX * exp(LAM / RHO_STAR**2)

# G62 anchor values
RHO_MIN_G62 = 1.1791
M_RATIO_G62 = 0.02025

# ── Precomputed ζ_FP grid (slow function, cached here) ───────────────────────
_RHO6_GRID = np.linspace(1.09, 1.35, 12)
_ZFP_GRID = np.array([zeta_fp(C * r6**2, r6) for r6 in _RHO6_GRID])


def _zfp(rho6: float) -> float:
    """ζ_FP at ρ₆ — linear interpolation from precomputed grid."""
    return float(np.interp(rho6, _RHO6_GRID, _ZFP_GRID))


def v_total(rho: float, alpha: float = 0.0) -> float:
    v_np = -A_NP * exp(-LAM / rho**2)
    v_cas = alpha * _zfp(rho)
    return (V_FLUX + v_np + v_cas) / (K_VOL * rho**12)


def _second_deriv(rho: float, alpha: float, dr: float = 5e-4) -> float:
    return (v_total(rho + dr, alpha) - 2 * v_total(rho, alpha) + v_total(rho - dr, alpha)) / dr**2


def find_minimum(alpha: float = 0.0):
    res = minimize_scalar(lambda r: v_total(r, alpha), bounds=(1.09, 2.0), method="bounded")
    rho, v = res.x, res.fun
    v2 = _second_deriv(rho, alpha)
    ratio = sqrt(abs(v2) / (1.0 / rho**2))
    return rho, v, ratio


# ── C1: ζ_FP at ρ_min is negative (Casimir is attractive) ────────────────────


class TestG63_C1_CasimirSign:
    """ζ_FP < 0 at ρ_min=1.179: Casimir deepens the minimum, doesn't oppose it."""

    def test_zfp_negative_at_rho_min(self):
        zfp = _zfp(RHO_MIN_G62)
        assert zfp < 0, f"Expected ζ_FP < 0 at ρ_min, got {zfp:.4e}"

    def test_zfp_negative_across_rho_range(self):
        """ζ_FP < 0 for all ρ₆ ∈ [ρ*, ρ**) — Casimir is attractive in this region."""
        for r6 in np.linspace(1.09, 1.40, 8):
            zfp = _zfp(r6)
            assert zfp < 0, f"ζ_FP > 0 at ρ₆={r6:.3f}: {zfp:.4e}"

    def test_zfp_magnitude_small_vs_vflux(self):
        """ζ_FP(ρ_min) / V_FLUX < 0.5% — Casimir is sub-percent of flux energy."""
        zfp = _zfp(RHO_MIN_G62)
        ratio = abs(zfp) / V_FLUX
        assert ratio < 0.005, f"|ζ_FP|/V_FLUX = {ratio * 100:.4f}% exceeds 0.5%"


# ── C2: Perturbative shift for physical α values ──────────────────────────────


class TestG63_C2_PerturbativeShift:
    """For physically motivated α (one-loop suppressed), δρ_min < 0.1%."""

    def test_alpha_001_rho_shift_tiny(self):
        """α=0.01 (one-loop suppression g_s²/4π²~10⁻²): δρ_min < 0.01%."""
        rho, _, _ = find_minimum(alpha=0.01)
        delta = abs(rho - RHO_MIN_G62) / RHO_MIN_G62
        assert delta < 0.0001, f"δρ_min = {delta * 100:.5f}% for α=0.01"

    def test_alpha_01_rho_shift_below_0p1_percent(self):
        """α=0.1 (generous suppression): δρ_min < 0.1%."""
        rho, _, _ = find_minimum(alpha=0.1)
        delta = abs(rho - RHO_MIN_G62) / RHO_MIN_G62
        assert delta < 0.001, f"δρ_min = {delta * 100:.4f}% for α=0.1"

    def test_alpha_01_mass_ratio_stable(self):
        """α=0.1: m_mod/m_KK shifts by < 1% relative."""
        _, _, ratio = find_minimum(alpha=0.1)
        rel_shift = abs(ratio / M_RATIO_G62 - 1.0)
        assert rel_shift < 0.01, f"m_ratio shift = {rel_shift * 100:.3f}% for α=0.1"


# ── C3: Conservative worst-case α=1 ──────────────────────────────────────────


class TestG63_C3_WorstCase:
    """α=1 (no loop suppression, maximally conservative): δρ_min < 1%."""

    def test_alpha_1_rho_shift_below_1_percent(self):
        """Even at α=1, ρ_min shifts by < 1%."""
        rho, _, _ = find_minimum(alpha=1.0)
        delta = abs(rho - RHO_MIN_G62) / RHO_MIN_G62
        assert delta < 0.01, f"δρ_min = {delta * 100:.4f}% for α=1.0"

    def test_alpha_1_minimum_still_adS(self):
        """V_min remains negative at α=1 (AdS pocket survives)."""
        _, v, _ = find_minimum(alpha=1.0)
        assert v < 0, f"V_min = {v:.4e} not negative for α=1.0"

    def test_alpha_1_eft_still_valid(self):
        """m_mod/m_KK < 5% even at α=1 (EFT remains valid)."""
        _, _, ratio = find_minimum(alpha=1.0)
        assert ratio < 0.05, f"m_mod/m_KK = {ratio:.4f} exceeds 5% for α=1.0"

    def test_alpha_1_mass_ratio_shifts_by_less_than_5pct(self):
        """Worst case: m_mod/m_KK shifts by < 5% relative."""
        _, _, ratio = find_minimum(alpha=1.0)
        rel_shift = abs(ratio / M_RATIO_G62 - 1.0)
        assert rel_shift < 0.05, f"m_ratio shift = {rel_shift * 100:.3f}% for α=1.0"


# ── C4: Monotone shift — Casimir deepens minimum proportionally ───────────────


class TestG63_C4_MonotoneShift:
    """As α increases, ρ_min decreases and V_min deepens monotonically."""

    def test_rho_min_decreases_with_alpha(self):
        alphas = [0.0, 0.1, 0.3, 0.5, 1.0]
        rho_mins = [find_minimum(alpha=a)[0] for a in alphas]
        diffs = [rho_mins[i + 1] - rho_mins[i] for i in range(len(rho_mins) - 1)]
        assert all(d < 0 for d in diffs), (
            f"ρ_min not monotonically decreasing: {[f'{r:.5f}' for r in rho_mins]}"
        )

    def test_v_min_deepens_with_alpha(self):
        """Casimir (negative) deepens the AdS minimum as α grows."""
        alphas = [0.0, 0.1, 0.3, 0.5, 1.0]
        v_mins = [find_minimum(alpha=a)[1] for a in alphas]
        # V_min is negative, deepening means more negative
        diffs = [v_mins[i + 1] - v_mins[i] for i in range(len(v_mins) - 1)]
        assert all(d < 0 for d in diffs), (
            f"V_min not monotonically deepening: {[f'{v:.4e}' for v in v_mins]}"
        )

    def test_print_sensitivity_table(self, capsys):
        """Print full sensitivity table — visible with pytest -s."""
        print("\n\nG63 — Casimir sensitivity scan:")
        print(f"{'α':>8} {'ρ_min':>10} {'δρ_min%':>10} {'V_min':>12} {'m/m_KK':>9} {'δ(m/m)%':>9}")
        print("-" * 65)
        rho0, v0, ratio0 = find_minimum(alpha=0.0)
        for alpha in [0.0, 0.001, 0.01, 0.05, 0.1, 0.3, 0.5, 1.0]:
            rho, v, ratio = find_minimum(alpha=alpha)
            drho = (rho - rho0) / rho0 * 100
            dm = (ratio / ratio0 - 1.0) * 100
            print(f"{alpha:>8.3f} {rho:>10.5f} {drho:>+10.4f} {v:>12.4e} {ratio:>9.5f} {dm:>+9.4f}")
        print()
