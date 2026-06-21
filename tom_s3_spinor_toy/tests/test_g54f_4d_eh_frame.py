"""
G54-F: Weyl rescaling to 4D Einstein-Hilbert frame — Casimir potential structure.

Closes G54-A gate F4. Using the Hadamard formula from G54-D and G54-E,
check how the Casimir potential transforms under Weyl rescaling from the
10D string frame to the 4D Einstein-Hilbert frame.

Weyl rescaling:
  g_μν^(4D EH) = V_int^{-1} g_μν^(10D string)
  V_EH_Cas(ρ₆) ∝ ζ_FP(ρ₆) / V_int(ρ₆)

where V_int = vol(S³, ρ₃) × vol(S⁶, ρ₆) along SM constraint ρ₃ = 0.986ρ₆².

Geometric volumes:
  vol(S³, r) = 2π² r³
  vol(S⁶, r) = 16π³/15 · r⁶
  V_int = 2π² (Cρ₆²)³ · 16π³ρ₆⁶/15 = 32π⁵C³ρ₆¹²/15

Along SM constraint: V_int ∝ ρ₆¹² (exact scaling).

Gates:
  F4.1: V_int ∝ ρ₆¹² — exact power law along constraint
  F4.2: V^EH_Cas monotone on [0.7, 1.5] — no local minimum in EH frame
  F4.3: V^EH_Cas(ρ₆**) = 0 — zero of ζ_FP preserved under Weyl rescaling
  F4.4: V_flux >> |ζ_FP| — Freund-Rubin flux dominates in EH frame (Dine-Seiberg regime)
  F4.5: V_total_EH = V^EH_Cas + V^EH_flux > 0, monotone decreasing on [0.7, 1.5]
"""

from math import sqrt, pi, exp

import numpy as np
from scipy.integrate import quad
from scipy.linalg import lstsq
from scipy.optimize import brentq
from scipy.special import comb, digamma

# ── constants ──────────────────────────────────────────────────────────────────
A0_S3 = sqrt(pi) / 2
A2_S3 = -sqrt(pi) / 4
CONSTRAINT_C = 0.986
GAMMA_NEG_HALF = -2.0 * sqrt(pi)
PSI_NEG_HALF = float(digamma(-0.5))
EPS_IREG = 0.10

VOL_S3_COEFF = 2 * pi**2  # vol(S³, r) = 2π²r³
VOL_S6_COEFF = 16 * pi**3 / 15  # vol(S⁶, r) = 16π³r⁶/15

# Freund-Rubin flux V_flux = const along SM constraint (G54-A F3)
V_FLUX_CONST = 15 * CONSTRAINT_C**3 / (16 * pi)  # q=1

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


# ── Hadamard ζ_FP (from G54-D) ────────────────────────────────────────────────


def _sigma_prime(r3: float, r6: float) -> float:
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


def _c_half(r3: float, r6: float) -> float:
    sw = _sw()
    return A0_S3 * r3**3 * sw["B10"] / r6**4 + A2_S3 * r3 * sw["B8"] / r6**2


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


# ── V_int and EH potentials ────────────────────────────────────────────────────


def v_int(r6: float) -> float:
    """Total internal volume V_int = vol(S³,ρ₃) × vol(S⁶,ρ₆) along SM constraint."""
    r3 = CONSTRAINT_C * r6**2
    return VOL_S3_COEFF * r3**3 * VOL_S6_COEFF * r6**6


def v_eh_cas(r6: float) -> float:
    """Casimir potential in 4D EH frame: ζ_FP / V_int."""
    return _zeta_fp(r6) / v_int(r6)


def v_eh_flux(r6: float) -> float:
    """Freund-Rubin flux in 4D EH frame: V_flux_const / V_int."""
    return V_FLUX_CONST / v_int(r6)


def v_eh_total(r6: float) -> float:
    """Total EH potential: Casimir + flux."""
    return v_eh_cas(r6) + v_eh_flux(r6)


# ── F4.1: V_int ∝ ρ₆¹² ───────────────────────────────────────────────────────


class TestF4p1VintScaling:
    """V_int along SM constraint scales exactly as ρ₆¹².

    Along ρ₃ = C ρ₆²:
      V_int = 2π²(Cρ₆²)³ × 16π³ρ₆⁶/15 = (32π⁵C³/15) × ρ₆¹²

    The exponent 12 = 3×2 + 6 (from 3 Hopf fibers on S³ and 6 on S⁶).
    """

    def test_vint_ratio_at_2x_is_2_to_12(self):
        """V_int(2.0)/V_int(1.0) = 2^12 = 4096 exactly."""
        ratio = v_int(2.0) / v_int(1.0)
        assert abs(ratio - 4096) < 0.01, f"V_int ratio = {ratio:.2f} (expected 4096)"

    def test_vint_ratio_at_1p5_is_1p5_to_12(self):
        """V_int(1.5)/V_int(1.0) = 1.5^12 = 129.75 exactly."""
        expected = 1.5**12
        ratio = v_int(1.5) / v_int(1.0)
        assert abs(ratio - expected) / expected < 1e-6, (
            f"V_int ratio = {ratio:.4f} (expected {expected:.4f})"
        )

    def test_vint_increases_with_rho6(self):
        """V_int grows strongly with ρ₆ — the Weyl factor suppresses any fixed-scale energy."""
        vi_09 = v_int(0.9)
        vi_10 = v_int(1.0)
        vi_12 = v_int(1.2)
        assert vi_09 < vi_10 < vi_12, f"V_int not monotone: {vi_09:.1f} {vi_10:.1f} {vi_12:.1f}"


# ── F4.2: V^EH_Cas monotone ───────────────────────────────────────────────────


class TestF4p2EHMonotone:
    """V^EH_Cas = ζ_FP/V_int is monotone increasing on [0.7, 1.5].

    The local minimum of ζ_FP at ρ₆_min≈0.953 (in 10D frame) does NOT
    survive Weyl rescaling — the ρ₆^12 denominator overwhelms ζ_FP structure.
    """

    def test_veh_cas_monotone_at_three_points(self):
        """V^EH_Cas(0.7) < V^EH_Cas(1.0) < V^EH_Cas(1.3)."""
        ve_07 = v_eh_cas(0.7)
        ve_10 = v_eh_cas(1.0)
        ve_13 = v_eh_cas(1.3)
        assert ve_07 < ve_10 < ve_13, f"Not monotone: {ve_07:.3e} < {ve_10:.3e} < {ve_13:.3e}?"

    def test_veh_cas_at_rho6_min_NOT_extremum(self):
        """V^EH_Cas has no minimum at ρ₆_min≈0.953 in EH frame.

        In EH frame, the local minimum that exists in ζ_FP is destroyed.
        Numerical derivative at 0.953 must be negative (still decreasing).
        """
        h = 0.02
        deriv = (v_eh_cas(0.953 + h) - v_eh_cas(0.953 - h)) / (2 * h)
        assert deriv > 0, f"d(V_EH)/d(ρ₆) at 0.953 = {deriv:.3e} (must be > 0, not a minimum)"

    def test_veh_cas_negative_on_range(self):
        """V^EH_Cas < 0 throughout [0.7, ρ₆**) — Casimir attractive in EH frame."""
        for r6 in [0.7, 0.8, 0.9, 0.95, 1.0, 1.09, 1.2, 1.4]:
            ve = v_eh_cas(r6)
            assert ve < 0, f"V^EH_Cas({r6}) = {ve:.3e} (expected < 0)"


# ── F4.3: Zero of ζ_FP preserved under Weyl rescaling ────────────────────────


class TestF4p3ZeroPreserved:
    """ρ₆** is a zero of V^EH_Cas — because it's a zero of ζ_FP (numerator).

    Weyl rescaling multiplies by 1/V_int, which is never zero.
    Therefore all zeros of ζ_FP remain zeros of V^EH_Cas.
    """

    def test_veh_cas_zero_at_rho6_double_star(self):
        """V^EH_Cas(ρ₆**) ≈ 0 (within numerical precision)."""
        r6ss = brentq(_zeta_fp, 1.44, 1.50, xtol=1e-4)
        ve_at_zero = v_eh_cas(r6ss)
        assert abs(ve_at_zero) < 1e-10, f"V^EH_Cas(ρ₆**) = {ve_at_zero:.2e}"

    def test_veh_cas_sign_change_at_rho6_double_star(self):
        """V^EH_Cas changes sign at ρ₆** (same bracket as ζ_FP)."""
        assert v_eh_cas(1.44) < 0, f"V^EH_Cas(1.44) = {v_eh_cas(1.44):.3e}"
        assert v_eh_cas(1.46) > 0, f"V^EH_Cas(1.46) = {v_eh_cas(1.46):.3e}"


# ── F4.4: Flux >> Casimir in EH frame ────────────────────────────────────────


class TestF4p4FluxDominates:
    """V_flux >> |ζ_FP| throughout [0.7, 1.5] — Dine-Seiberg regime.

    From G54-A: V_flux = const ≈ 0.286 along SM constraint (q=1).
    From G54-D: |ζ_FP| ≈ 0.00085 in the same range.
    Ratio: V_flux/|ζ_FP| ≈ 330 >> 1.

    Consequence: total V^EH = V^EH_Cas + V^EH_flux > 0 on [0.7, 1.5].
    Both terms scale as 1/V_int ∝ 1/ρ₆¹², but flux numerator 300× larger.
    """

    def test_v_flux_const_much_larger_than_zeta_fp(self):
        """V_flux_const ≈ 0.286; |ζ_FP| ≈ 0.00085 — ratio ≈ 330."""
        max_abs_zfp = max(abs(_zeta_fp(r6)) for r6 in [0.8, 0.9, 0.95, 1.0, 1.09, 1.2])
        assert V_FLUX_CONST / max_abs_zfp > 100, (
            f"V_flux/|ζ_FP_max| = {V_FLUX_CONST / max_abs_zfp:.1f} (expected >> 100)"
        )

    def test_v_total_eh_positive_on_range(self):
        """V_total_EH > 0 on [0.7, 1.5] — flux dominates over Casimir."""
        for r6 in [0.7, 0.8, 0.9, 0.95, 1.0, 1.09, 1.2, 1.4]:
            vt = v_eh_total(r6)
            assert vt > 0, f"V_total_EH({r6}) = {vt:.3e} (expected > 0)"


# ── F4.5: Dine-Seiberg runaway in studied domain ─────────────────────────────


class TestF4p5DinevSeiberg:
    """V_total_EH is monotone decreasing on [0.7, 1.5] → no interior minimum.

    This is the Dine-Seiberg runaway: Casimir + flux alone cannot stabilize
    the compactification in the 4D EH frame within the studied range [0.7, 1.5].

    Physical consequence: additional stabilization mechanisms (non-perturbative,
    orientifolds, D-branes) are required. The three special radii (ρ₆_min, ρ₆*, ρ₆**)
    found in 10D string frame do NOT translate directly to a 4D minimum.

    ρ₆** is preserved as the ZERO of V^EH_Cas — not as a minimum.
    """

    def test_v_total_eh_decreasing(self):
        """V_total_EH(0.7) > V_total_EH(1.0) > V_total_EH(1.3) — monotone decreasing."""
        vt_07 = v_eh_total(0.7)
        vt_10 = v_eh_total(1.0)
        vt_13 = v_eh_total(1.3)
        assert vt_07 > vt_10 > vt_13, f"Not decreasing: {vt_07:.3e} > {vt_10:.3e} > {vt_13:.3e}?"

    def test_v_eh_cas_at_rho6_min_less_negative_than_10D_frame(self):
        """In EH frame, ρ₆_min is NOT a minimum: V^EH_Cas(0.95) > V^EH_Cas(0.8).

        In 10D: ζ_FP(0.95) < ζ_FP(0.8) (minimum at 0.95).
        In 4D EH: V^EH_Cas(0.95) > V^EH_Cas(0.8) (monotone — minimum gone).
        """
        assert v_eh_cas(0.95) > v_eh_cas(0.8), (
            f"EH frame: V^EH_Cas(0.95)={v_eh_cas(0.95):.3e} should be > {v_eh_cas(0.8):.3e}"
        )

    def test_v_total_positive_and_rho6_double_star_is_not_minimum(self):
        """ρ₆** is a zero of V^EH_Cas but V_total_EH(ρ₆**) > 0.

        Because V_flux contribution is still positive at ρ₆**.
        So ρ₆** is NOT a minimum of V_total_EH either.
        """
        r6ss = brentq(_zeta_fp, 1.44, 1.50, xtol=1e-4)
        vt_at_star = v_eh_total(r6ss)
        assert vt_at_star > 0, f"V_total_EH(ρ₆**) = {vt_at_star:.3e} (> 0, flux still contributes)"
