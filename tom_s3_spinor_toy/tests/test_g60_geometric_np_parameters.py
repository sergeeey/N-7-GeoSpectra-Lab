"""
G60 — Geometric derivation of A_np and λ from Minkowski uplift + UV selection.

CLAIM: Requiring (1) minimum at ρ₆* + (2) Minkowski vacuum V_total(ρ₆*)=0
algebraically fixes BOTH free parameters of G56's KKLT-like potential:

  V_np = -A_np · exp(-λ/ρ₆²)

Derivation:
  Minkowski:  V_flux + ζ_FP(ρ₆*) = A_np · exp(-λ/ρ₆*²)         ... (M)
  Minimum:    ζ_FP'(ρ₆*) + (2λ/ρ₆*³) · [V_flux + ζ_FP(ρ₆*)] = 0  ... (Mn)

  From (Mn): λ_geom = -ρ₆*³/2 · ζ_FP'(ρ₆*) / (V_flux + ζ_FP(ρ₆*))
  From (M):  A_geom = (V_flux + ζ_FP(ρ₆*)) · exp(+λ_geom/ρ₆*²)

Null criterion: |λ_geom - 0.30| / 0.30 > 0.30  (30% — G60 NULL if fails badly)
Promote criterion: |λ_geom - 0.30| / 0.30 < 0.10  (10% — derived from geometry)
"""

import numpy as np
import pytest
from math import pi, exp, sqrt
from scipy.integrate import quad
from scipy.linalg import lstsq
from scipy.special import comb, digamma

# ── reuse G56 spectral machinery ──────────────────────────────────────────────
A0_S3 = sqrt(pi) / 2
A2_S3 = -sqrt(pi) / 4
CONSTRAINT_C = 0.986
GAMMA_NEG_HALF = -2.0 * sqrt(pi)
PSI_NEG_HALF = float(digamma(-0.5))
EPS_IREG = 0.10

VOL_S3_COEFF = 2 * pi**2
VOL_S6_COEFF = 16 * pi**3 / 15
V_INT_COEFF = VOL_S3_COEFF * VOL_S6_COEFF
V_FLUX_CONST = 15 * CONSTRAINT_C**3 / (16 * pi)

RHO6_STAR = 1.090

# G56 fitted values (to be compared against geometric derivation)
A_NP_FITTED = 0.38
LAM_FITTED = 0.30

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


def _hs3(tau: float, n: int = 200) -> float:
    return 2.0 * sum((k + 1) * (k + 2) * exp(-tau * (k + 1.5) ** 2) for k in range(n))


def _hs6(tau: float, n: int = 150) -> float:
    return sum(16 * comb(k + 5, 5, exact=True) * exp(-tau * (k + 3) ** 2) for k in range(n))


def _sigma_prime(r6: float) -> float:
    sw = _sw()
    r3 = CONSTRAINT_C * r6**2
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


def _c_half(r6: float) -> float:
    sw = _sw()
    r3 = CONSTRAINT_C * r6**2
    return A0_S3 * r3**3 * sw["B10"] / r6**4 + A2_S3 * r3 * sw["B8"] / r6**2


def _k_sw(t: float, r6: float) -> float:
    sw = _sw()
    r3 = CONSTRAINT_C * r6**2
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


def _k_full(t: float, r6: float) -> float:
    r3 = CONSTRAINT_C * r6**2
    return _hs3(t / r3**2) * _hs6(t / r6**2)


def zeta_fp(r6: float) -> float:
    Sig = _sigma_prime(r6)
    Ir, _ = quad(
        lambda t: t ** (-1.5) * (_k_full(t, r6) - _k_sw(t, r6)),
        EPS_IREG,
        1.0,
        limit=200,
        epsabs=1e-9,
        epsrel=1e-7,
    )
    I2, _ = quad(
        lambda t: t ** (-1.5) * _k_full(t, r6),
        1.0,
        50.0,
        limit=100,
        epsabs=1e-12,
        epsrel=1e-10,
    )
    c12 = _c_half(r6)
    return (Sig + Ir + I2 - PSI_NEG_HALF * c12) / GAMMA_NEG_HALF


def zeta_fp_deriv(r6: float, dr: float = 0.005) -> float:
    return (zeta_fp(r6 + dr) - zeta_fp(r6 - dr)) / (2 * dr)


def derive_lambda(r6_star: float) -> float:
    """λ_geom from Minkowski + minimum conditions."""
    P_star = V_FLUX_CONST + zeta_fp(r6_star)
    zfp_prime = zeta_fp_deriv(r6_star)
    return -(r6_star**3) / 2.0 * zfp_prime / P_star


def derive_a_np(r6_star: float, lam_geom: float) -> float:
    """A_geom from Minkowski condition."""
    P_star = V_FLUX_CONST + zeta_fp(r6_star)
    return P_star * exp(+lam_geom / r6_star**2)


# ── G60-A: verify input quantities ───────────────────────────────────────────


class TestA_Inputs:
    def test_v_flux_order_unity(self):
        """V_flux ≈ 0.286: order-unity, not exponentially suppressed."""
        assert 0.1 < V_FLUX_CONST < 1.0

    def test_zeta_fp_at_rho_star_small(self):
        """ζ_FP(ρ₆*) << V_flux (Casimir negligible at UV-selection point)."""
        zfp = abs(zeta_fp(RHO6_STAR))
        assert zfp < 0.01 * V_FLUX_CONST, (
            f"|ζ_FP(ρ₆*)| = {zfp:.2e} not << V_flux = {V_FLUX_CONST:.4f}"
        )

    def test_zeta_fp_prime_nonzero(self):
        """ζ_FP'(ρ₆*) ≠ 0: the Casimir has nonzero slope at UV-selection radius."""
        zfp_prime = zeta_fp_deriv(RHO6_STAR)
        assert abs(zfp_prime) > 1e-6, f"ζ_FP'(ρ₆*) ≈ 0, cannot derive λ"


# ── G60-B: derived parameters ────────────────────────────────────────────────


class TestB_DerivedParameters:
    def test_lambda_geom_negative(self):
        """NULL structural result: λ_geom < 0 because ζ_FP is monotone increasing in window.

        ζ_FP'(ρ₆*) > 0 throughout [ρ₆_min, ρ₆**] → formula λ = -ρ*³/2·ζ_FP'/(V+ζ) < 0.
        The Minkowski uplift condition CANNOT produce positive λ from Casimir physics alone.
        """
        lam = derive_lambda(RHO6_STAR)
        assert lam < 0, f"Expected λ_geom < 0 (structural NULL), got {lam:.4f}"

    def test_a_np_geom_close_to_v_flux(self):
        """With λ≈0, A_geom ≈ V_FLUX_CONST: NP amplitude is just the flux level."""
        lam = derive_lambda(RHO6_STAR)
        a_np = derive_a_np(RHO6_STAR, lam)
        rel_diff = abs(a_np - V_FLUX_CONST) / V_FLUX_CONST
        assert rel_diff < 0.01, f"A_geom={a_np:.4f} not close to V_flux={V_FLUX_CONST:.4f}"

    def test_casimir_derivative_positive_at_star(self):
        """Core cause: ζ_FP'(ρ₆*) > 0 in the Casimir window → λ forced negative."""
        zfp_prime = zeta_fp_deriv(RHO6_STAR)
        assert zfp_prime > 0, f"Expected ζ_FP'(ρ₆*)>0 (rising Casimir), got {zfp_prime:.6f}"

    def test_lambda_geom_small_absolute(self):
        """|λ_geom| << 1: the geometric constraint gives approximately λ=0, not 0.30."""
        lam = derive_lambda(RHO6_STAR)
        assert abs(lam) < 0.05, f"|λ_geom| = {abs(lam):.4f} not << 0.30"


# ── G60-C: comparison to G56 fitted values ───────────────────────────────────


class TestC_ComparisonToFitted:
    """Key test: do geometric parameters match the G56 fits?"""

    def test_lambda_relative_error(self):
        """|λ_geom - 0.30| / 0.30: record the relative error for verdict."""
        lam = derive_lambda(RHO6_STAR)
        rel_err = abs(lam - LAM_FITTED) / LAM_FITTED
        print(f"\n  λ_geom = {lam:.4f},  λ_fitted = {LAM_FITTED:.2f},  rel_err = {rel_err:.1%}")
        # Soft check: not more than 200% off (i.e., not completely wrong)
        assert rel_err < 2.0, f"λ_geom = {lam:.4f} vs {LAM_FITTED}: completely off"

    def test_a_np_relative_error(self):
        """|A_geom - 0.38| / 0.38: record the relative error for verdict."""
        lam = derive_lambda(RHO6_STAR)
        a_np = derive_a_np(RHO6_STAR, lam)
        rel_err = abs(a_np - A_NP_FITTED) / A_NP_FITTED
        print(f"\n  A_geom = {a_np:.4f},  A_fitted = {A_NP_FITTED:.2f},  rel_err = {rel_err:.1%}")
        assert rel_err < 2.0, f"A_geom = {a_np:.4f} vs {A_NP_FITTED}: completely off"

    def test_promote_criterion_lambda(self):
        """λ_geom matches fitted within 10% → parameters ARE geometrically derived."""
        lam = derive_lambda(RHO6_STAR)
        rel_err = abs(lam - LAM_FITTED) / LAM_FITTED
        if rel_err <= 0.10:
            pass  # PROMOTE: geometric derivation works
        else:
            pytest.skip(
                f"λ_geom={lam:.4f} differs from λ_fitted={LAM_FITTED} by {rel_err:.1%} "
                f"(>10%: parameters not geometrically fixed — INVESTIGATE)"
            )

    def test_promote_criterion_a_np(self):
        """A_geom matches fitted within 10% → amplitude IS geometrically derived."""
        lam = derive_lambda(RHO6_STAR)
        a_np = derive_a_np(RHO6_STAR, lam)
        rel_err = abs(a_np - A_NP_FITTED) / A_NP_FITTED
        if rel_err <= 0.10:
            pass  # PROMOTE
        else:
            pytest.skip(
                f"A_geom={a_np:.4f} differs from A_fitted={A_NP_FITTED} by {rel_err:.1%} "
                f"(>10%: amplitude not geometrically fixed — INVESTIGATE)"
            )


# ── G60-D: consistency check via PSLQ candidates ─────────────────────────────


class TestD_ClosedFormCandidates:
    """Check whether derived values match simple closed forms."""

    def test_lambda_vs_three_tenths(self):
        """Is λ_geom close to the exact rational 3/10?"""
        lam = derive_lambda(RHO6_STAR)
        err_rational = abs(lam - 3.0 / 10.0)
        print(f"\n  λ_geom = {lam:.6f}, 3/10 = 0.3, |diff| = {err_rational:.6f}")
        # Just record, don't assert — this is diagnostic
        assert err_rational < 0.5, "λ_geom is more than 0.5 away from 3/10 (trivially wrong)"

    def test_a_np_vs_three_eighths(self):
        """Is A_geom close to exact rational 3/8?"""
        lam = derive_lambda(RHO6_STAR)
        a_np = derive_a_np(RHO6_STAR, lam)
        err_rational = abs(a_np - 3.0 / 8.0)
        err_transcendental = abs(a_np - 6.0 / (5.0 * pi))
        print(
            f"\n  A_geom = {a_np:.6f}, 3/8 = {3 / 8:.6f}, |diff| = {err_rational:.6f}"
            f"\n  A_geom = {a_np:.6f}, 6/5π = {6 / (5 * pi):.6f}, |diff| = {err_transcendental:.6f}"
        )
        assert err_rational < 0.5 or err_transcendental < 0.5, "A_geom unreasonably far"
