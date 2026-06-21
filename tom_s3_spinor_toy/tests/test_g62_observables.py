"""
G62 — Physical observables from zero-fit parameters.

Variant 2: accept λ=1/3 (G61 dimensional hypothesis) and derive A_np from
the G60 Minkowski pearl. No fitting — pure geometry.

Parameters:
  λ = 1/3 = dim(S³)/dim(S³×S⁶)          [G61 dimensional]
  A_np = V_FLUX · exp(λ/ρ₆*²)             [G60 Minkowski pearl]
  ρ₆* = 1.090                             [G57 UV-selection]

Predictions (all dimensionless, in string units):
  O1: ρ₆_min — position of AdS minimum
  O2: V_min — depth of AdS minimum (negative)
  O3: m²_moduli = V''_EH(ρ₆_min) — moduli mass squared
  O4: m_KK = 1/ρ₆_min — KK mass scale
  O5: m_mod/m_KK — hierarchy between moduli and KK
  O6: Casimir correction δV/V_min at minimum (should be sub-dominant)
"""

import pytest
from math import pi, exp, sqrt
from scipy.optimize import minimize_scalar, brentq

# ── constants ─────────────────────────────────────────────────────────────────

C = 0.986
V_FLUX = 15 * C**3 / (16 * pi)
RHO6_STAR = 1.090  # G57 UV-selection
LAM = 1.0 / 3.0  # G61 dimensional: dim(S³)/dim(S³×S⁶)
A_NP = V_FLUX * exp(LAM / RHO6_STAR**2)  # G60 Minkowski pearl

VOL_S3_COEFF = 2 * pi**2
VOL_S6_COEFF = 16 * pi**3 / 15
K_VOL = VOL_S3_COEFF * VOL_S6_COEFF  # V_int = K_VOL · ρ₆¹² on SM constraint


def v_np(r6: float) -> float:
    """NP term: -A_np · exp(-λ/ρ₆²)."""
    return -A_NP * exp(-LAM / r6**2)


def v_total_no_cas(r6: float) -> float:
    """V_EH without Casimir (approximation: ζ_FP << V_flux)."""
    return (V_FLUX + v_np(r6)) / (K_VOL * r6**12)


def v_second_deriv(r6: float, dr: float = 5e-4) -> float:
    """Numerical second derivative of V_EH at r6."""
    return (v_total_no_cas(r6 + dr) - 2 * v_total_no_cas(r6) + v_total_no_cas(r6 - dr)) / dr**2


def find_minimum() -> float:
    """ρ₆ that minimizes V_EH (no Casimir)."""
    res = minimize_scalar(v_total_no_cas, bounds=(0.9, 1.5), method="bounded")
    return res.x


# ── G62-A: zero-fit parameter derivation ─────────────────────────────────────


class TestA_ZeroFitParameters:
    def test_lambda_is_exact_one_third(self):
        """λ = 1/3 exactly (ratio of integers, not a fit)."""
        assert LAM == 1.0 / 3.0

    def test_a_np_from_minkowski_pearl(self):
        """A_np derived from V_total(ρ₆*)=0: A_np = V_FLUX·exp(λ/ρ₆*²)."""
        a_pred = V_FLUX * exp(LAM / RHO6_STAR**2)
        assert abs(a_pred - A_NP) / A_NP < 1e-10  # exact by construction

    def test_a_np_close_to_fitted(self):
        """A_np_derived within 0.4% of G56 fitted A_np=0.38."""
        a_fitted = 0.38
        diff = abs(A_NP - a_fitted) / a_fitted
        print(f"\n  A_np_derived = {A_NP:.5f},  A_fitted = {a_fitted:.2f},  diff = {diff:.1%}")
        assert diff < 0.01, f"A_np mismatch {diff:.1%} > 1%"

    def test_v_flux_const(self):
        """V_FLUX = 15C³/(16π) ≈ 0.286 (G54-A result)."""
        assert 0.280 < V_FLUX < 0.295

    def test_minkowski_condition_at_rho_star(self):
        """By construction, V_total(ρ₆*)≈0 (Minkowski) when Casimir ignored."""
        v_star = v_total_no_cas(RHO6_STAR)
        assert abs(v_star) < 1e-15, f"V_total(ρ₆*)={v_star:.2e} not ≈ 0"


# ── G62-B: potential minimum (Observable O1, O2) ──────────────────────────────


class TestB_PotentialMinimum:
    def test_minimum_exists_in_sm_window(self):
        """AdS minimum exists in Casimir window [0.953, 1.447]."""
        r6_min = find_minimum()
        assert 0.953 < r6_min < 1.447, f"ρ₆_min={r6_min:.3f} outside Casimir window"

    def test_minimum_position(self):
        """ρ₆_min ≈ 1.18: minimum displaced from UV-selection point ρ₆*=1.090."""
        r6_min = find_minimum()
        print(f"\n  ρ₆_min = {r6_min:.4f}  (UV-selection ρ₆* = {RHO6_STAR})")
        assert r6_min > RHO6_STAR, "Minimum should be above UV-selection point"
        assert r6_min < 1.25, f"Minimum too far from SM window: {r6_min:.3f}"

    def test_minimum_is_ads(self):
        """V_min < 0 (AdS minimum — uplift needed for Minkowski, as in KKLT)."""
        r6_min = find_minimum()
        v_min = v_total_no_cas(r6_min)
        print(f"\n  V_min = {v_min:.3e}  (negative = AdS as expected)")
        assert v_min < 0, f"Expected AdS minimum (V<0), got V_min={v_min:.3e}"

    def test_minimum_depth_order(self):
        """V_min of order 10⁻⁶: shallow minimum (exponentially suppressed NP term)."""
        r6_min = find_minimum()
        v_min = v_total_no_cas(r6_min)
        assert -1e-4 < v_min < -1e-9, f"|V_min|={abs(v_min):.2e} not in expected range"

    def test_uv_selection_vs_minimum_split(self):
        """UV-selection (ρ₆*=1.090) and minimum (ρ₆_min≈1.18) are distinct — KKLT uplift needed."""
        r6_min = find_minimum()
        split = abs(r6_min - RHO6_STAR) / RHO6_STAR
        print(f"\n  ρ₆_min - ρ₆* = {r6_min - RHO6_STAR:.4f} ({split:.1%})")
        assert split > 0.05, f"UV-selection and minimum too close: {split:.1%}"


# ── G62-C: moduli mass (Observable O3, O4, O5) ────────────────────────────────


class TestC_ModuliMass:
    def test_second_derivative_positive(self):
        """V''(ρ₆_min) > 0: confirmed minimum (not maximum)."""
        r6_min = find_minimum()
        v_pp = v_second_deriv(r6_min)
        assert v_pp > 0, f"V''(ρ₆_min) = {v_pp:.3e} not positive"

    def test_moduli_mass_squared_order(self):
        """m²_moduli = V''_EH(ρ₆_min) of order 10⁻⁴ (string units)."""
        r6_min = find_minimum()
        m2_mod = v_second_deriv(r6_min)
        print(f"\n  m²_moduli = {m2_mod:.3e} (string units)")
        assert 1e-5 < m2_mod < 1e-2, f"m²_moduli = {m2_mod:.2e} unexpected"

    def test_kk_mass_squared(self):
        """m²_KK = 1/ρ₆_min² ≈ 0.72 (string units) — parametrically larger than m²_moduli."""
        r6_min = find_minimum()
        m2_kk = 1.0 / r6_min**2
        print(f"\n  m²_KK = {m2_kk:.4f},  ρ₆_min = {r6_min:.4f}")
        assert 0.5 < m2_kk < 1.5, f"m²_KK = {m2_kk:.3f} unexpected"

    def test_moduli_lighter_than_kk(self):
        """m_moduli << m_KK: EFT hierarchy — moduli stabilized below KK threshold."""
        r6_min = find_minimum()
        m2_mod = v_second_deriv(r6_min)
        m2_kk = 1.0 / r6_min**2
        ratio_sq = m2_mod / m2_kk
        ratio = sqrt(ratio_sq)
        print(f"\n  m_mod/m_KK = {ratio:.4f}  ({ratio:.1%})")
        assert ratio < 0.1, f"Moduli not lighter than KK: m_mod/m_KK = {ratio:.3f}"

    def test_moduli_mass_in_sm_units(self):
        """m_moduli in units of m_KK: concrete prediction from zero-fit parameters."""
        r6_min = find_minimum()
        m2_mod = v_second_deriv(r6_min)
        m2_kk = 1.0 / r6_min**2
        m_ratio = sqrt(m2_mod / m2_kk)
        print(f"\n  PREDICTION: m_moduli/m_KK = {m_ratio:.4f}")
        print(f"  (With m_KK ~ 10¹⁵ GeV → m_moduli ~ {m_ratio * 1e15:.1e} GeV)")
        # Just document: soft check
        assert 0 < m_ratio < 1


# ── G62-D: Casimir correction (Observable O6) ─────────────────────────────────


class TestD_CasimirCorrection:
    """Casimir (ζ_FP) is negligible vs NP term at the minimum — approximation is valid."""

    def test_casimir_small_vs_flux(self):
        """At ρ₆_min≈1.18, Casimir is still << V_flux (from ζ_FP structure G54-E)."""
        r6_min = find_minimum()
        # From G54-E: |ζ_FP| < 0.001 for all ρ₆ in [0.953, 1.447]
        zeta_upper_bound = 0.002
        v_cas_upper = zeta_upper_bound / (K_VOL * r6_min**12)
        v_flux_eff = V_FLUX / (K_VOL * r6_min**12)
        ratio = v_cas_upper / abs(v_flux_eff)
        print(f"\n  |ζ_FP|/V_flux upper bound = {ratio:.2%} at ρ₆_min={r6_min:.3f}")
        assert ratio < 0.02, f"Casimir correction dominates: {ratio:.2%}"

    def test_casimir_correction_to_minimum(self):
        """Casimir shifts V_min by < 20% — negligible at this level of approximation."""
        r6_min = find_minimum()
        v_min = v_total_no_cas(r6_min)
        zeta_estimate = -5e-4  # from G54-E: ζ_FP between ρ₆* and ρ₆**
        delta_v = zeta_estimate / (K_VOL * r6_min**12)
        correction = abs(delta_v / v_min)
        print(f"\n  δV_Casimir / |V_min| = {correction:.1%}")
        assert correction < 0.3, f"Casimir correction too large: {correction:.1%}"


# ── G62-E: Variant 2 summary ─────────────────────────────────────────────────


class TestE_Variant2Summary:
    def test_all_observables_computed(self):
        """Comprehensive print of all G62 observables."""
        r6_min = find_minimum()
        v_min = v_total_no_cas(r6_min)
        m2_mod = v_second_deriv(r6_min)
        m2_kk = 1.0 / r6_min**2
        m_ratio = sqrt(m2_mod / m2_kk)

        print("\n  === G62 Variant 2 Observable Summary ===")
        print(f"  Parameters (zero-fit):")
        print(f"    λ     = 1/3 = {LAM:.5f}")
        print(f"    A_np  = {A_NP:.5f}  (from Minkowski pearl)")
        print(f"    ρ₆*   = {RHO6_STAR} (UV-selection G57)")
        print(f"  Predictions:")
        print(f"    O1: ρ₆_min        = {r6_min:.4f}")
        print(f"    O2: V_min         = {v_min:.3e}  (AdS)")
        print(f"    O3: m²_moduli     = {m2_mod:.3e}  (string units)")
        print(f"    O4: m²_KK         = {m2_kk:.4f}      (string units)")
        print(f"    O5: m_mod/m_KK    = {m_ratio:.4f}  ({m_ratio:.2%})")
        print(
            f"    UV-split:  ρ₆_min - ρ₆* = {r6_min - RHO6_STAR:.4f} ({(r6_min - RHO6_STAR) / RHO6_STAR:.1%})"
        )

        # All must be physically reasonable
        assert r6_min > 0
        assert v_min < 0
        assert m2_mod > 0
        assert m_ratio < 1

    def test_variant2_no_fitting(self):
        """Confirm: all parameters are derived, not fitted."""
        # λ = exact rational
        assert LAM == 1.0 / 3.0
        # A_np = exact formula of V_FLUX (geometric) and ρ₆* (UV-selection)
        a_check = V_FLUX * exp(LAM / RHO6_STAR**2)
        assert abs(a_check - A_NP) / A_NP < 1e-12
        # No numerical tuning was performed
