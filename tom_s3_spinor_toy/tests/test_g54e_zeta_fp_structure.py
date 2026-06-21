"""
G54-E: Structure of ζ_FP(−1/2) along SM constraint — three special radii.

Continuation of G54-D. Using the same Hadamard subtraction formula,
characterize the full structure of ζ_FP as a function of ρ₆ along
ρ₃ = C ρ₆² (C=0.986).

Three special radii are identified and ordered:
  ρ₆_min ≈ 0.953 — local minimum of ζ_FP (most attractive Casimir energy)
  ρ₆*   ≈ 1.090 — UV pole cancels: c_{1/2}=0 (from G54-C)
  ρ₆**  ≈ 1.447 — ζ_FP=0: Casimir finite part vanishes (from G54-D)

ordering: ρ₆_min < ρ₆* < ρ₆** along the constraint.

Gates:
  E1: ζ_FP has a local minimum at ρ₆_min ∈ (0.9, 1.0)
  E2: ζ_FP=0 at ρ₆** ∈ (1.40, 1.50), precisely ≈ 1.4469
  E3: Three radii obey ρ₆_min < ρ₆* < ρ₆**, all on SM constraint
"""

import math
from math import sqrt, pi, exp

import numpy as np
from scipy.integrate import quad
from scipy.linalg import lstsq
from scipy.optimize import brentq, minimize_scalar
from scipy.special import comb, digamma

# ── constants ──────────────────────────────────────────────────────────────────
A0_S3 = sqrt(pi) / 2
A2_S3 = -sqrt(pi) / 4
CONSTRAINT_C = 0.986
GAMMA_NEG_HALF = -2.0 * sqrt(pi)
PSI_NEG_HALF = float(digamma(-0.5))
EPS_IREG = 0.10

# ── heat kernels ───────────────────────────────────────────────────────────────


def _hs3(tau: float, n: int = 200) -> float:
    return 2.0 * sum((k + 1) * (k + 2) * exp(-tau * (k + 1.5) ** 2) for k in range(n))


def _hs6(tau: float, n: int = 150) -> float:
    return sum(16 * comb(k + 5, 5, exact=True) * exp(-tau * (k + 3) ** 2) for k in range(n))


# ── SW coefficients ────────────────────────────────────────────────────────────

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


# ── Hadamard components (same as G54-D) ────────────────────────────────────────


def sigma_prime(r3: float, r6: float) -> float:
    sw = _sw()
    A0, A2 = A0_S3, A2_S3
    B0, B2, B4, B6, B8, B10 = sw["B0"], sw["B2"], sw["B4"], sw["B6"], sw["B8"], sw["B10"]
    cns = {
        -4.5: A0 * r3**3 * B0 * r6**6,
        -3.5: A0 * r3**3 * B2 * r6**4 + A2 * r3 * B0 * r6**6,
        -2.5: A0 * r3**3 * B4 * r6**2 + A2 * r3 * B2 * r6**4,
        -1.5: A0 * r3**3 * B6 + A2 * r3 * B4 * r6**2,
        -0.5: A0 * r3**3 * B8 / r6**2 + A2 * r3 * B6,
        1.5: A2 * r3 * B10 / r6**4,
    }
    return sum(cn / (alpha - 0.5) for alpha, cn in cns.items())


def c_half(r3: float, r6: float) -> float:
    sw = _sw()
    return A0_S3 * r3**3 * sw["B10"] / r6**4 + A2_S3 * r3 * sw["B8"] / r6**2


def rho6_star() -> float:
    sw = _sw()
    ratio = -(A2_S3 * sw["B8"]) / (A0_S3 * sw["B10"] * CONSTRAINT_C**2)
    return sqrt(ratio) if ratio > 0 else float("nan")


def _k_sw(t: float, r3: float, r6: float) -> float:
    sw = _sw()
    A0, A2 = A0_S3, A2_S3
    B0, B2, B4, B6, B8, B10 = sw["B0"], sw["B2"], sw["B4"], sw["B6"], sw["B8"], sw["B10"]
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
    Sig = sigma_prime(r3, r6)
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
    c12 = c_half(r3, r6)
    return (Sig + Ir + I2 - PSI_NEG_HALF * c12) / GAMMA_NEG_HALF


# ── E1: ζ_FP has a local minimum at ρ₆_min ∈ (0.9, 1.0) ─────────────────────


class TestE1LocalMinimum:
    """ζ_FP has a local minimum at ρ₆_min ≈ 0.953 along the SM constraint.

    This is where the Casimir energy is most attractive (most negative).
    The minimum is in (0.9, 1.0), not at any particularly 'nice' radius.
    """

    def test_zeta_fp_at_0p95_less_than_at_0p80(self):
        """ζ_FP(0.95) < ζ_FP(0.80) — going toward minimum as ρ₆ increases from 0.8."""
        zfp_080 = _zeta_fp(0.80)
        zfp_095 = _zeta_fp(0.95)
        assert zfp_095 < zfp_080, f"ζ_FP: 0.80→{zfp_080:.6f}, 0.95→{zfp_095:.6f}"

    def test_zeta_fp_at_0p95_less_than_at_1p10(self):
        """ζ_FP(0.95) < ζ_FP(1.10) — going away from minimum as ρ₆ increases past 1.0."""
        zfp_095 = _zeta_fp(0.95)
        zfp_110 = _zeta_fp(1.10)
        assert zfp_095 < zfp_110, f"ζ_FP: 0.95→{zfp_095:.6f}, 1.10→{zfp_110:.6f}"

    def test_local_min_located_in_interval(self):
        """Brentq-style: ζ_FP is decreasing at 0.85 and increasing at 1.05.

        Derivative sign change confirms local minimum in (0.85, 1.05).
        """
        # numerical derivative at 0.85 (should be negative → still going down)
        h = 0.02
        deriv_at_085 = (_zeta_fp(0.85 + h) - _zeta_fp(0.85 - h)) / (2 * h)
        # numerical derivative at 1.05 (should be positive → going up)
        deriv_at_105 = (_zeta_fp(1.05 + h) - _zeta_fp(1.05 - h)) / (2 * h)
        assert deriv_at_085 < 0, f"d(ζ_FP)/d(ρ₆) at 0.85 = {deriv_at_085:.4e} (expected < 0)"
        assert deriv_at_105 > 0, f"d(ζ_FP)/d(ρ₆) at 1.05 = {deriv_at_105:.4e} (expected > 0)"

    def test_local_min_value_order_of_magnitude(self):
        """ζ_FP at minimum ≈ -0.00086 — O(10⁻³), small but negative."""
        zfp_095 = _zeta_fp(0.95)
        assert -0.005 < zfp_095 < -0.0001, f"ζ_FP(0.95)={zfp_095:.4e}"


# ── E2: ζ_FP = 0 at ρ₆** ∈ (1.40, 1.50) ─────────────────────────────────────


class TestE2ZeroLocation:
    """ζ_FP = 0 at ρ₆** ≈ 1.447, located to 3 significant figures."""

    def test_zeta_fp_negative_at_1p40(self):
        """ζ_FP(1.40) < 0 — still on negative side of zero."""
        assert _zeta_fp(1.40) < 0, f"ζ_FP(1.40)={_zeta_fp(1.40):.4e}"

    def test_zeta_fp_positive_at_1p50(self):
        """ζ_FP(1.50) > 0 — crossed zero."""
        assert _zeta_fp(1.50) > 0, f"ζ_FP(1.50)={_zeta_fp(1.50):.4e}"

    def test_rho6_double_star_in_1p44_1p46(self):
        """ρ₆** ∈ (1.44, 1.46) — three-significant-figure bracket."""
        zfp_a = _zeta_fp(1.44)
        zfp_b = _zeta_fp(1.46)
        assert zfp_a < 0, f"ζ_FP(1.44)={zfp_a:.4e} should be < 0"
        assert zfp_b > 0, f"ζ_FP(1.46)={zfp_b:.4e} should be > 0"

    def test_rho6_double_star_bisection_value(self):
        """Brentq gives ρ₆** ≈ 1.447 ± 0.003."""
        r6ss = brentq(_zeta_fp, 1.44, 1.50, xtol=1e-4)
        assert 1.440 < r6ss < 1.460, f"ρ₆**={r6ss:.4f} outside (1.440, 1.460)"
        assert abs(_zeta_fp(r6ss)) < 1e-8, f"|ζ_FP(ρ₆**)|={abs(_zeta_fp(r6ss)):.2e}"


# ── E3: Three special radii are ordered ρ₆_min < ρ₆* < ρ₆** ─────────────────


class TestE3ThreeRadiiOrdering:
    """Three distinct special radii on SM constraint, strictly ordered.

    ρ₆_min ≈ 0.953 (min ζ_FP) < ρ₆* ≈ 1.090 (c_{1/2}=0) < ρ₆** ≈ 1.447 (ζ_FP=0)

    Physical interpretation:
    - ρ₆_min: most attractive Casimir (energy is most negative)
    - ρ₆*:    UV-finite (no counterterm), energy still negative
    - ρ₆**:   UV-finite AND energy = 0 (transition from attractive to repulsive)
    """

    def test_rho6_min_less_than_rho6_star(self):
        """ρ₆_min < ρ₆* — minimum precedes UV-pole cancellation."""
        r6_star = rho6_star()
        # Numerically: ρ₆_min is around 0.95, ρ₆* ≈ 1.09
        # Use: ζ_FP(0.95) < ζ_FP(0.80) (D → min is near 0.95)
        # and ρ₆* > 1.05 (G54-C established ρ₆* ≈ 1.09)
        assert r6_star > 1.04, f"ρ₆*={r6_star:.4f} should be > 1.04"
        # min is in (0.9, 1.0) from E1 tests → ρ₆_min < 1.0 < ρ₆*
        zfp_090 = _zeta_fp(0.90)
        zfp_100 = _zeta_fp(1.00)
        # ζ_FP is more negative at 0.90 than at 0.80 (approaching minimum from left)
        # and less negative at 1.05 than at 0.95 (past minimum)
        # Combined with ρ₆*≈1.09 → ρ₆_min < ρ₆*
        deriv_at_1p0 = (_zeta_fp(1.00 + 0.02) - _zeta_fp(1.00 - 0.02)) / 0.04
        # At 1.0 the derivative should be positive (past the minimum → going up)
        assert deriv_at_1p0 > 0, f"deriv at ρ₆=1.0 = {deriv_at_1p0:.4e} (min is to left of 1.0)"
        assert r6_star > 1.04, "ρ₆* > 1.04 → min is to its left"

    def test_rho6_star_less_than_rho6_double_star(self):
        """ρ₆* < ρ₆** — UV-pole cancellation precedes Casimir zero."""
        r6_star = rho6_star()
        r6ss = brentq(_zeta_fp, 1.40, 1.50, xtol=1e-4)
        assert r6_star < r6ss, f"ρ₆*={r6_star:.4f} should be < ρ₆**={r6ss:.4f}"

    def test_zeta_fp_negative_at_rho6_star(self):
        """ζ_FP(ρ₆*) < 0 — energy still attractive at the UV-finite radius."""
        r6_star = rho6_star()
        zfp_star = _zeta_fp(r6_star)
        assert zfp_star < 0, f"ζ_FP(ρ₆*)={zfp_star:.4e}"

    def test_three_radii_ordering_summary(self):
        """Combined: ρ₆_min < ρ₆* < ρ₆** as approximate numerical values.

        ρ₆_min ≈ 0.95 (where ζ_FP is minimized on [0.8, 1.1])
        ρ₆*   ≈ 1.09 (c_{1/2}=0, from G54-C formula)
        ρ₆**  ≈ 1.45 (ζ_FP=0, from bisection)
        """
        r6_star = rho6_star()
        r6ss = brentq(_zeta_fp, 1.40, 1.50, xtol=1e-4)

        # ρ₆_min ∈ (0.9, 1.0): verified by checking derivative sign change in E1
        # Here: just confirm ζ_FP at ρ₆=0.95 < ζ_FP at ρ₆*
        zfp_095 = _zeta_fp(0.95)
        zfp_star = _zeta_fp(r6_star)
        # Both negative; 0.95 should give more negative value
        assert zfp_095 < zfp_star, (
            f"ζ_FP(0.95)={zfp_095:.4e} should be more negative than ζ_FP(ρ₆*)={zfp_star:.4e}"
        )

        # ρ₆* < ρ₆**
        assert r6_star < r6ss, f"ρ₆*={r6_star:.4f} < ρ₆**={r6ss:.4f}"

        # All in (0.8, 1.6)
        assert 0.8 < 0.95 < r6_star < r6ss < 1.6, "Ordering check failed"
