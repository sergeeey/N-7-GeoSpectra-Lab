"""
G58: Curvature in 4D EH frame — V_curv^EH vs V_Cas^EH on SM constraint.

G54-F omitted the curvature term from v_eh_total. After Weyl rescaling:

  V_curv^EH(ρ₆) = V_class_string / V_int
               = [-(R_S3 + R_S6) × V_int] / V_int
               = -(6/(C²ρ₆⁴) + 30/ρ₆²)    along ρ₃ = C ρ₆²

Hierarchy at ρ₆ = 1:
  |V_curv^EH| ≈ 36  >>  V_flux^EH ≈ 4.6×10⁻⁴  >>  |V_Cas^EH| ≈ 1.6×10⁻⁶

V_curv^EH (negative, decaying ∝ ρ₆⁻²) competes with V_flux^EH (positive, ∝ ρ₆⁻¹²),
creating an interior minimum — but at ρ₆_min_curv ≈ 0.337, far from SM region.

Gates:
  C1: V_curv^EH < 0, ρ₆-dependent, monotone on [0.5, 2.0]
  C2: |V_curv^EH(1)| / V_flux^EH(1) > 10⁴ — curvature dominates flux
  C3: d/dρ₆(V_curv + V_flux) changes sign on (0.25, 0.50) → interior minimum
  C4: ρ₆_min_curv < 0.50 << RHO6_MIN_CAS ≈ 0.953 (Casimir window start)
  C5: |V_Cas^EH| / |V_curv^EH| < 10⁻⁴ at SM-scale radii — Casimir irrelevant
  C6 NULL: minimum of V_curv+V_flux is deep AdS (~−500), NOT in SM region
"""

from math import exp, pi, sqrt

import numpy as np
from scipy.integrate import quad
from scipy.linalg import lstsq
from scipy.optimize import brentq
from scipy.special import comb, digamma

# ── constants (matching G54-F) ─────────────────────────────────────────────────
CONSTRAINT_C = 0.986
A0_S3 = sqrt(pi) / 2
A2_S3 = -sqrt(pi) / 4
GAMMA_NEG_HALF = -2.0 * sqrt(pi)
PSI_NEG_HALF = float(digamma(-0.5))
EPS_IREG = 0.10

VOL_S3_COEFF = 2 * pi**2
VOL_S6_COEFF = 16 * pi**3 / 15
V_FLUX_CONST = 15 * CONSTRAINT_C**3 / (16 * pi)
K_VOL = VOL_S3_COEFF * CONSTRAINT_C**3 * VOL_S6_COEFF  # = 32π⁵C³/15

RHO6_MIN_CAS = 0.953  # ζ_FP minimum (G54-E)
RHO6_DSS = 1.447  # ζ_FP = 0 (G54-E)

# ── heat kernels ───────────────────────────────────────────────────────────────


def _hs3(tau: float, n: int = 200) -> float:
    return 2.0 * sum((k + 1) * (k + 2) * exp(-tau * (k + 1.5) ** 2) for k in range(n))


def _hs6(tau: float, n: int = 150) -> float:
    return sum(16 * comb(k + 5, 5, exact=True) * exp(-tau * (k + 3) ** 2) for k in range(n))


# ── SW coefficients (S⁶ fit) ──────────────────────────────────────────────────

_SW_CACHE: dict | None = None


def _sw() -> dict:
    global _SW_CACHE
    if _SW_CACHE is None:
        tau = np.array([0.005, 0.008, 0.012, 0.018, 0.025, 0.035, 0.050, 0.070, 0.080])
        k = np.array([_hs6(t, n=150) for t in tau])
        basis = np.column_stack(
            [tau ** (-3), tau ** (-2), tau ** (-1), np.ones(len(tau)), tau, tau**2]
        )
        c, *_ = lstsq(basis, k)
        _SW_CACHE = {
            "B0": c[0],
            "B2": c[1],
            "B4": c[2],
            "B6": c[3],
            "B8": c[4],
            "B10": c[5],
        }
    return _SW_CACHE


# ── ζ_FP via Hadamard regularisation (verbatim from G54-F) ────────────────────


def _sigma_prime(r3: float, r6: float) -> float:
    sw = _sw()
    A0, A2 = A0_S3, A2_S3
    B0, B2, B4, B6, B8, B10 = (
        sw["B0"],
        sw["B2"],
        sw["B4"],
        sw["B6"],
        sw["B8"],
        sw["B10"],
    )
    cns = {
        -4.5: A0 * r3**3 * B0 * r6**6,
        -3.5: A0 * r3**3 * B2 * r6**4 + A2 * r3 * B0 * r6**6,
        -2.5: A0 * r3**3 * B4 * r6**2 + A2 * r3 * B2 * r6**4,
        -1.5: A0 * r3**3 * B6 + A2 * r3 * B4 * r6**2,
        -0.5: A0 * r3**3 * B8 / r6**2 + A2 * r3 * B6,
        1.5: A2 * r3 * B10 / r6**4,
    }
    return sum(cn / (alpha - 0.5) for alpha, cn in cns.items())


def _c_half(r3: float, r6: float) -> float:
    sw = _sw()
    return A0_S3 * r3**3 * sw["B10"] / r6**4 + A2_S3 * r3 * sw["B8"] / r6**2


def _k_sw(t: float, r3: float, r6: float) -> float:
    sw = _sw()
    A0, A2 = A0_S3, A2_S3
    B0, B2, B4, B6, B8, B10 = (
        sw["B0"],
        sw["B2"],
        sw["B4"],
        sw["B6"],
        sw["B8"],
        sw["B10"],
    )
    ta = (
        A0
        * r3**3
        * (
            B0 * r6**6 * t ** (-4.5)
            + B2 * r6**4 * t ** (-3.5)
            + B4 * r6**2 * t ** (-2.5)
            + B6 * t ** (-1.5)
            + B8 / r6**2 * t ** (-0.5)
            + B10 / r6**4 * t**0.5
        )
    )
    t2 = (
        A2
        * r3
        * (
            B0 * r6**6 * t ** (-3.5)
            + B2 * r6**4 * t ** (-2.5)
            + B4 * r6**2 * t ** (-1.5)
            + B6 * t ** (-0.5)
            + B8 / r6**2 * t**0.5
            + B10 / r6**4 * t**1.5
        )
    )
    return ta + t2


def _k_full(t: float, r3: float, r6: float) -> float:
    return _hs3(t / r3**2) * _hs6(t / r6**2)


def _zeta_fp(r6: float) -> float:
    r3 = CONSTRAINT_C * r6**2
    Sig = _sigma_prime(r3, r6)
    Ir, _ = quad(
        lambda t: t ** (-1.5) * (_k_full(t, r3, r6) - _k_sw(t, r3, r6)),
        EPS_IREG,
        1.0,
        limit=200,
        epsabs=1e-9,
        epsrel=1e-7,
    )
    I2, _ = quad(
        lambda t: t ** (-1.5) * _k_full(t, r3, r6),
        1.0,
        50.0,
        limit=100,
        epsabs=1e-12,
        epsrel=1e-10,
    )
    c12 = _c_half(r3, r6)
    return (Sig + Ir + I2 - PSI_NEG_HALF * c12) / GAMMA_NEG_HALF


# ── G58 potentials ─────────────────────────────────────────────────────────────


def v_int(r6: float) -> float:
    """V_int = K_VOL × ρ₆¹² along SM constraint ρ₃ = C ρ₆²."""
    return K_VOL * r6**12


def v_curv_eh(r6: float) -> float:
    """EH-frame curvature: V_class_string / V_int = -(6/C²ρ₆⁴ + 30/ρ₆²)."""
    return -(6.0 / (CONSTRAINT_C**2 * r6**4) + 30.0 / r6**2)


def v_flux_eh(r6: float) -> float:
    """EH-frame FR flux: V_FLUX_CONST / V_int (same as G54-F)."""
    return V_FLUX_CONST / v_int(r6)


def v_cas_eh(r6: float) -> float:
    """EH-frame Casimir: ζ_FP / V_int (same as G54-F)."""
    return _zeta_fp(r6) / v_int(r6)


def _dv_curv_flux(r6: float) -> float:
    """d/dρ₆ of (V_curv^EH + V_flux^EH)."""
    d_curv = 24.0 / (CONSTRAINT_C**2 * r6**5) + 60.0 / r6**3
    d_flux = -12.0 * V_FLUX_CONST / (v_int(r6) * r6)
    return d_curv + d_flux


def find_r6_min_curv() -> float:
    """ρ₆ where d/dρ₆(V_curv^EH + V_flux^EH) = 0, bracketed in (0.25, 0.50)."""
    return brentq(_dv_curv_flux, 0.25, 0.50, xtol=1e-6)


# ── C1: curvature negative and ρ₆-dependent ────────────────────────────────────


class TestC1CurvatureNegative:
    """V_curv^EH < 0 and strictly monotone increasing toward 0⁻ as ρ₆ increases."""

    def test_negative_at_four_radii(self):
        """V_curv^EH(ρ₆) < 0 for ρ₆ ∈ {0.5, 1.0, 1.5, 2.0}."""
        for r6 in [0.5, 1.0, 1.5, 2.0]:
            v = v_curv_eh(r6)
            assert v < 0.0, f"V_curv^EH({r6}) = {v:.3f} not < 0"

    def test_monotone_increasing_toward_zero(self):
        """V_curv^EH increases (less negative) as ρ₆ grows — unlike V_Cas."""
        vs = [v_curv_eh(r6) for r6 in [0.5, 1.0, 1.5, 2.0]]
        for i in range(len(vs) - 1):
            assert vs[i] < vs[i + 1] < 0.0, (
                f"Not monotone at index {i}: {vs[i]:.2f} vs {vs[i + 1]:.2f}"
            )


# ── C2: curvature dominates flux ──────────────────────────────────────────────


class TestC2CurvatureDominatesFlux:
    """V_curv^EH >> V_flux^EH by four or more orders of magnitude."""

    def test_ratio_exceeds_ten_thousand_at_unit_rho6(self):
        """|V_curv^EH(1.0)| / V_flux^EH(1.0) > 10⁴."""
        ratio = abs(v_curv_eh(1.0)) / v_flux_eh(1.0)
        assert ratio > 1e4, f"|V_curv/V_flux|(1.0) = {ratio:.2e} (expected > 1e4)"

    def test_curvature_dominates_flux_across_sm_range(self):
        """|V_curv^EH| > 100 × V_flux^EH at ρ₆ ∈ {0.7, 1.0, 1.2, 1.5}."""
        for r6 in [0.7, 1.0, 1.2, 1.5]:
            ratio = abs(v_curv_eh(r6)) / v_flux_eh(r6)
            assert ratio > 100.0, f"|V_curv/V_flux|({r6}) = {ratio:.1f} (< 100)"


# ── C3: interior minimum exists ───────────────────────────────────────────────


class TestC3InteriorMinimum:
    """d/dρ₆(V_curv + V_flux) changes sign → Bolzano guarantees a minimum."""

    def test_derivative_negative_at_0p25(self):
        """At ρ₆=0.25 flux term ∝ ρ₆⁻¹³ dominates → derivative negative."""
        assert _dv_curv_flux(0.25) < 0.0, f"d/dρ₆(0.25) = {_dv_curv_flux(0.25):.1e}"

    def test_derivative_positive_at_0p50(self):
        """At ρ₆=0.50 curvature slope ∝ ρ₆⁻³ dominates → derivative positive."""
        assert _dv_curv_flux(0.50) > 0.0, f"d/dρ₆(0.50) = {_dv_curv_flux(0.50):.1e}"

    def test_brentq_finds_root_with_near_zero_residual(self):
        """brentq locates ρ₆_min with |d/dρ₆| < 1 (well-converged root)."""
        r6_min = find_r6_min_curv()
        residual = abs(_dv_curv_flux(r6_min))
        assert residual < 1.0, f"|d/dρ₆|(ρ₆_min={r6_min:.4f}) = {residual:.3e}"
        assert 0.25 < r6_min < 0.50, f"ρ₆_min_curv={r6_min:.4f} not in (0.25, 0.50)"


# ── C4: minimum outside Casimir window ────────────────────────────────────────


class TestC4MinimumOutsideCasimirWindow:
    """ρ₆_min_curv << RHO6_MIN_CAS=0.953 — far below the Casimir window."""

    def test_minimum_below_0p5(self):
        """ρ₆_min_curv < 0.50 < 0.953 (Casimir window start)."""
        r6_min = find_r6_min_curv()
        assert r6_min < 0.50, f"ρ₆_min_curv = {r6_min:.4f} not < 0.50"

    def test_minimum_well_below_sm_region(self):
        """ρ₆_min_curv < 0.70 — outside SM-relevant range [0.70, 1.50]."""
        r6_min = find_r6_min_curv()
        assert r6_min < 0.70, f"ρ₆_min_curv = {r6_min:.4f} inside SM region"


# ── C5: Casimir negligible vs curvature ───────────────────────────────────────


class TestC5CasimirNegligible:
    """At SM-scale ρ₆, |V_Cas^EH| / |V_curv^EH| < 10⁻⁴ — Casimir is irrelevant."""

    def test_cas_to_curv_ratio_at_rho6_1p0(self):
        """|V_Cas^EH(1.0)| / |V_curv^EH(1.0)| < 10⁻⁴."""
        ratio = abs(v_cas_eh(1.0)) / abs(v_curv_eh(1.0))
        assert ratio < 1e-4, f"|V_Cas/V_curv|(1.0) = {ratio:.2e} (expected < 1e-4)"

    def test_cas_to_curv_ratio_at_casimir_peak(self):
        """|V_Cas^EH(0.953)| / |V_curv^EH(0.953)| < 10⁻⁴ even at Casimir minimum."""
        ratio = abs(v_cas_eh(RHO6_MIN_CAS)) / abs(v_curv_eh(RHO6_MIN_CAS))
        assert ratio < 1e-4, f"|V_Cas/V_curv|(0.953) = {ratio:.2e} (expected < 1e-4)"


# ── C6: NULL verdict ──────────────────────────────────────────────────────────


class TestC6NullVerdict:
    """G58 NULL — V_curv^EH stabilizes at ρ₆≈0.34 (deep AdS), not SM region.

    G54-F's Dine-Seiberg analysis was for V_flux+V_Cas only (curvature absent).
    Including V_curv creates a minimum but at the wrong scale:
      ρ₆_min ≈ 0.34 << 0.953 (Casimir window) << 1.09 (SM ρ₆*)
    """

    def test_minimum_value_deep_ads(self):
        """V_curv+V_flux at minimum << −100 (deep AdS, not a gentle de Sitter)."""
        r6_min = find_r6_min_curv()
        v_min = v_curv_eh(r6_min) + v_flux_eh(r6_min)
        assert v_min < -100.0, f"V_total(ρ₆_min={r6_min:.3f}) = {v_min:.1f} (expected << −100)"

    def test_curvature_negative_flux_positive_at_rho6_1(self):
        """V_curv^EH(1)<0 while V_flux^EH(1)>0: sign flip when curvature included.

        G54-F total was positive (Dine-Seiberg regime); adding V_curv gives a
        net negative potential at ρ₆=1, confirming curvature dominates.
        """
        v_curv = v_curv_eh(1.0)
        v_flux = v_flux_eh(1.0)
        assert v_curv < 0.0 < v_flux, f"Expected V_curv({v_curv:.2f}) < 0 < V_flux({v_flux:.6f})"
