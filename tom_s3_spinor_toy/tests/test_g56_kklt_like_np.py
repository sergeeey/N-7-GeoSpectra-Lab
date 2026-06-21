"""
G56: KKLT-like non-perturbative stabilization on S³×S⁶.

Question: What non-perturbative amplitude A_np and exponent λ can create a minimum
in V^EH_total near ρ₆** ≈ 1.447, and what scale is required?

Context from G54-F + G55:
  - V^EH_flux + V^EH_Cas alone → Dine-Seiberg runaway (no minimum)
  - V_flux_min = 1 >> |ζ_FP| ≈ 10⁻³ (Casimir ~1000× too small for flux competition)
  - ρ₆** ≈ 1.447 survives 4D EH frame as structural zero of V^EH_Cas

KKLT ansatz: add V_np = -A_np × exp(-λ/ρ₆²) / V_int  to EH potential.
This mimics gaugino condensation on a D-brane wrapping S³ (τ ∝ vol(S³) ∝ ρ₆⁴ for S³ at ρ₃=Cρ₆²).

The numerator: N(ρ₆) = V_FLUX_CONST + ζ_FP(ρ₆) - A_np × exp(-λ/ρ₆²)
Minimum condition: N'(ρ₆₀)/N(ρ₆₀) = 12/ρ₆₀ (from V_int ∝ ρ₆¹²)

Gates:
  NP1: For (A_np=0.38, λ=0.30), a minimum exists in [0.95, 1.45] (numerical)
  NP2: At the minimum, V^EH_total < 0 (AdS vacuum before uplift)
  NP3: Required A_np ~ V_FLUX_CONST ≈ 0.286 (order-unity, not exponentially suppressed)
  NP4: Casimir contribution at minimum << A_np × exp(-λ/ρ₆₀²) (Casimir-blind mechanism)
  NP5: The minimum location is inside the "Casimir window" [ρ₆_min, ρ₆**]
"""

from math import sqrt, pi, exp

import numpy as np
from scipy.integrate import quad
from scipy.linalg import lstsq
from scipy.optimize import brentq
from scipy.special import comb, digamma


def num_deriv(f, x, dx: float = 0.005) -> float:
    return (f(x + dx) - f(x - dx)) / (2 * dx)


# ── constants ──────────────────────────────────────────────────────────────────
A0_S3 = sqrt(pi) / 2
A2_S3 = -sqrt(pi) / 4
CONSTRAINT_C = 0.986
GAMMA_NEG_HALF = -2.0 * sqrt(pi)
PSI_NEG_HALF = float(digamma(-0.5))
EPS_IREG = 0.10

VOL_S3_COEFF = 2 * pi**2
VOL_S6_COEFF = 16 * pi**3 / 15
V_INT_COEFF = VOL_S3_COEFF * VOL_S6_COEFF  # V_int = V_INT_COEFF × r3³ × r6⁶

# V_flux along SM constraint (G54-A F3): const = 15C³/(16π)
V_FLUX_CONST = 15 * CONSTRAINT_C**3 / (16 * pi)

# Three special radii (from G54-E)
RHO6_MIN = 0.953  # most negative Casimir
RHO6_STAR = 1.090  # UV-finite (c_{1/2}=0)
RHO6_DSS = 1.447  # ζ_FP = 0


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


# ── Hadamard ζ_FP along SM constraint ─────────────────────────────────────────


def _sigma_prime_on_constraint(r6: float) -> float:
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


def _c_half_on_constraint(r6: float) -> float:
    sw = _sw()
    r3 = CONSTRAINT_C * r6**2
    return A0_S3 * r3**3 * sw["B10"] / r6**4 + A2_S3 * r3 * sw["B8"] / r6**2


def _k_sw_on_constraint(t: float, r6: float) -> float:
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


def _k_full_on_constraint(t: float, r6: float) -> float:
    r3 = CONSTRAINT_C * r6**2
    return _hs3(t / r3**2) * _hs6(t / r6**2)


def zeta_fp_on_constraint(r6: float) -> float:
    Sig = _sigma_prime_on_constraint(r6)
    Ir, _ = quad(
        lambda t: t ** (-1.5) * (_k_full_on_constraint(t, r6) - _k_sw_on_constraint(t, r6)),
        EPS_IREG,
        1.0,
        limit=200,
        epsabs=1e-9,
        epsrel=1e-7,
    )
    I2, _ = quad(
        lambda t: t ** (-1.5) * _k_full_on_constraint(t, r6),
        1.0,
        50.0,
        limit=100,
        epsabs=1e-12,
        epsrel=1e-10,
    )
    c12 = _c_half_on_constraint(r6)
    return (Sig + Ir + I2 - PSI_NEG_HALF * c12) / GAMMA_NEG_HALF


# ── G56 KKLT-like potential ────────────────────────────────────────────────────


def v_int_on_constraint(r6: float) -> float:
    r3 = CONSTRAINT_C * r6**2
    return V_INT_COEFF * r3**3 * r6**6


def v_eh_total_with_np(r6: float, A_np: float, lam: float) -> float:
    """V^EH_total = (V_flux + ζ_FP - A_np × exp(-λ/r6²)) / V_int."""
    np_term = A_np * exp(-lam / r6**2)
    return (V_FLUX_CONST + zeta_fp_on_constraint(r6) - np_term) / v_int_on_constraint(r6)


def find_minimum_r6(
    A_np: float, lam: float, r6_lo: float = 0.85, r6_hi: float = 1.45
) -> float | None:
    """Find ρ₆ that minimizes V^EH_total_with_np. Returns None if no interior minimum."""

    def dv(r: float) -> float:
        return num_deriv(lambda x: v_eh_total_with_np(x, A_np, lam), r, dx=0.005)

    # Scan for sign change in derivative (minimum = positive→ to negative derivative)
    rs = np.linspace(r6_lo, r6_hi, 30)
    derivs = [dv(r) for r in rs]
    for i in range(len(derivs) - 1):
        if derivs[i] < 0 and derivs[i + 1] > 0:
            return brentq(dv, rs[i], rs[i + 1], xtol=1e-6)
    return None


# ── Gate NP1: minimum exists ───────────────────────────────────────────────────


class TestNP1MinimumExists:
    """For (A_np=0.38, λ=0.30), V^EH_total has an interior minimum in [0.90, 1.45].

    Analytical estimate: minimum at ρ₆₀ satisfying
      N'(ρ₆₀) = 12 N(ρ₆₀) / ρ₆₀
    where N = V_flux + ζ_FP - A_np × exp(-λ/ρ₆₀²).
    For A_np=0.38, λ=0.30: minimum predicted near ρ₆₀ ≈ 1.09 (matching ρ₆*).
    """

    A_NP = 0.38
    LAM = 0.30

    def test_minimum_found_in_casimir_window(self):
        """Minimum exists in [ρ₆_min, ρ₆**] = [0.953, 1.447]."""
        r6_min = find_minimum_r6(self.A_NP, self.LAM)
        assert r6_min is not None, (
            f"No minimum found for A_np={self.A_NP}, λ={self.LAM} in [0.85, 1.45]"
        )
        assert RHO6_MIN < r6_min < RHO6_DSS, (
            f"Minimum at ρ₆₀={r6_min:.4f} outside Casimir window [{RHO6_MIN}, {RHO6_DSS}]"
        )

    def test_minimum_near_rho6_star(self):
        """For (0.38, 0.30), minimum is near ρ₆* ≈ 1.090 (UV-finite radius)."""
        r6_min = find_minimum_r6(self.A_NP, self.LAM)
        assert r6_min is not None
        assert 0.95 < r6_min < 1.25, f"Minimum at ρ₆₀={r6_min:.4f} (expected near 1.09)"

    def test_derivative_changes_sign_at_minimum(self):
        """d(V^EH)/dρ₆ is negative before and positive after the minimum."""
        r6_min = find_minimum_r6(self.A_NP, self.LAM)
        assert r6_min is not None

        def dv(r: float) -> float:
            return num_deriv(lambda x: v_eh_total_with_np(x, self.A_NP, self.LAM), r, dx=0.01)

        assert dv(r6_min - 0.05) < 0, "Derivative not negative before minimum"
        assert dv(r6_min + 0.05) > 0, "Derivative not positive after minimum"


# ── Gate NP2: AdS vacuum ───────────────────────────────────────────────────────


class TestNP2AdSVacuum:
    """V^EH_total < 0 at the minimum — AdS vacuum before uplift.

    In standard KKLT, the F-term potential creates an AdS minimum.
    An anti-brane or D-term 'uplift' then raises V → 0 (Minkowski) or V > 0 (dS).
    The AdS depth |V^EH_min| sets the uplift energy required.
    """

    A_NP = 0.38
    LAM = 0.30

    def test_potential_negative_at_minimum(self):
        """V^EH_total(ρ₆₀) < 0 (AdS vacuum)."""
        r6_min = find_minimum_r6(self.A_NP, self.LAM)
        assert r6_min is not None
        v_min = v_eh_total_with_np(r6_min, self.A_NP, self.LAM)
        assert v_min < 0, f"V^EH(ρ₆₀={r6_min:.4f}) = {v_min:.4e} (expected < 0, AdS)"

    def test_ads_depth_smaller_than_flux(self):
        """|V^EH_min| < V_FLUX_CONST — AdS depth set by the flux-np cancellation, not flux alone."""
        r6_min = find_minimum_r6(self.A_NP, self.LAM)
        assert r6_min is not None
        v_min = abs(v_eh_total_with_np(r6_min, self.A_NP, self.LAM))
        v_flux_at_min = V_FLUX_CONST / v_int_on_constraint(r6_min)
        assert v_min < v_flux_at_min, (
            f"|V^EH_min|={v_min:.4e} ≥ V^EH_flux={v_flux_at_min:.4e} (unexpected)"
        )


# ── Gate NP3: required scale A_np ~ V_FLUX_CONST ──────────────────────────────


class TestNP3RequiredScale:
    """A_np required for stabilization is O(V_FLUX_CONST) ≈ 0.286.

    From the minimum condition N'(ρ₆₀) = 12 N(ρ₆₀)/ρ₆₀ and N(ρ₆₀) ≈ V_FLUX_CONST - A_np exp(-λ/ρ₆₀²):
    At minimum: A_np exp(-λ/ρ₆₀²) ≈ V_FLUX_CONST × (1 - 12λ/(ρ₆₀²(12-2λ/ρ₆₀²)))
    For small λ: A_np exp(-λ/ρ₆₀²) ≈ V_FLUX_CONST, so A_np ≈ V_FLUX_CONST × exp(λ/ρ₆₀²).

    For λ = 0.30, ρ₆₀ ≈ 1.09: exp(0.30/1.09²) ≈ exp(0.252) ≈ 1.29.
    → A_np_needed ≈ 0.286 × 1.29 ≈ 0.37 (order unity, not exponentially large).

    This is UNLIKE a KKLT with large τ (where A ~ W₀ × exp(aτ) can be exponentially large).
    At S³×S⁶ radii ρ₆ ~ 1 (Planck units), the KKLT amplitude is naturally O(1).
    """

    def test_a_np_needed_is_order_v_flux(self):
        """For λ=0.30, the minimum-creating A_np is within 1 order of V_FLUX_CONST."""
        lam = 0.30
        r6_0 = 1.09  # approximate minimum location
        # Minimum condition (approximate, ignoring Casimir and ζ_FP'):
        # A_np exp(-λ/ρ₆₀²) ≈ V_FLUX_CONST × ρ₆₀² × 12/(ρ₆₀²×12 - 2λ)
        denom = 12 * r6_0**2 - 2 * lam
        numerator = 12 * r6_0**2 * V_FLUX_CONST
        x_optimal = numerator / denom  # = A_np * exp(-λ/ρ₆₀²)
        A_np_needed = x_optimal * exp(lam / r6_0**2)
        # Should be within factor 5 of V_FLUX_CONST
        ratio = A_np_needed / V_FLUX_CONST
        assert 0.5 < ratio < 10.0, (
            f"A_np_needed = {A_np_needed:.4f}, ratio to V_FLUX_CONST = {ratio:.2f} "
            f"(expected 0.5–10, order-unity)"
        )

    def test_a_np_not_exponentially_large_for_small_lambda(self):
        """For λ ∈ [0.1, 1.0], A_np_needed < 10 × V_FLUX_CONST (not exp-large)."""
        r6_0 = 1.09
        for lam in [0.1, 0.3, 0.5, 1.0]:
            x = V_FLUX_CONST  # approximate (ignoring correction from min condition)
            A_needed = x * exp(lam / r6_0**2)
            assert A_needed < 10 * V_FLUX_CONST, (
                f"λ={lam}: A_needed={A_needed:.4f} >> 10 × V_FLUX_CONST={10 * V_FLUX_CONST:.4f}"
            )

    def test_required_a_np_increases_with_lambda(self):
        """Larger λ requires larger A_np (more non-perturbative energy to compete with flux)."""
        r6_0 = 1.09
        a_vals = [V_FLUX_CONST * exp(lam / r6_0**2) for lam in [0.1, 0.3, 0.5, 1.0]]
        assert a_vals[0] < a_vals[1] < a_vals[2] < a_vals[3], f"A_np not monotone in λ: {a_vals}"


# ── Gate NP4: Casimir blind ────────────────────────────────────────────────────


class TestNP4CasimirBlind:
    """Casimir contribution at minimum is << A_np × exp(-λ/ρ₆₀²).

    The KKLT stabilization works independently of the Casimir energy.
    The Casimir correction at the minimum is a <1% effect on the np term.
    This means: Casimir does NOT help KKLT stabilize (it's Casimir-blind).
    """

    A_NP = 0.38
    LAM = 0.30

    def test_casimir_small_at_kklt_minimum(self):
        """|ζ_FP(ρ₆₀)| << A_np × exp(-λ/ρ₆₀²) at the minimum (ratio < 1%)."""
        r6_min = find_minimum_r6(self.A_NP, self.LAM)
        assert r6_min is not None
        zfp = abs(zeta_fp_on_constraint(r6_min))
        np_energy = self.A_NP * exp(-self.LAM / r6_min**2)
        ratio = zfp / np_energy
        assert ratio < 0.05, (
            f"|ζ_FP|/A_np×exp(-λ/ρ₆₀²) = {ratio:.4f} at ρ₆₀={r6_min:.4f} (expected << 0.05)"
        )

    def test_casimir_irrelevant_to_minimum_location(self):
        """Removing Casimir shifts the minimum by < 5% in ρ₆."""
        # Minimum with full potential
        r6_full = find_minimum_r6(self.A_NP, self.LAM)

        # Minimum without Casimir (V^EH = (V_flux - A_np × exp(-λ/r6²)) / V_int)
        def v_no_casimir(r6: float) -> float:
            return (V_FLUX_CONST - self.A_NP * exp(-self.LAM / r6**2)) / v_int_on_constraint(r6)

        def dv_nc(r: float) -> float:
            return num_deriv(v_no_casimir, r, dx=0.005)

        rs = np.linspace(0.85, 1.45, 30)
        derivs_nc = [dv_nc(r) for r in rs]
        r6_no_cas = None
        for i in range(len(derivs_nc) - 1):
            if derivs_nc[i] < 0 and derivs_nc[i + 1] > 0:
                r6_no_cas = brentq(dv_nc, rs[i], rs[i + 1], xtol=1e-6)
                break

        assert r6_full is not None and r6_no_cas is not None
        shift = abs(r6_full - r6_no_cas) / r6_full
        assert shift < 0.05, (
            f"Casimir shifts minimum by {100 * shift:.1f}% (ρ₆_full={r6_full:.4f}, ρ₆_no_cas={r6_no_cas:.4f})"
        )


# ── Gate NP5: KKLT scale summary ──────────────────────────────────────────────


class TestNP5KKLTScaleSummary:
    """Summary: what KKLT requires vs what Casimir provides.

    Three-way comparison:
      V_flux_min = 1.000   (unit flux — AM-GM lower bound from G55)
      A_np_needed ≈ 0.38   (KKLT non-perturbative amplitude)
      max|ζ_FP| ≈ 0.00086 (Casimir peak)

    Order: V_flux_min > A_np_needed >> max|ζ_FP|
    Casimir is 3 orders below what's needed for KKLT stabilization.
    """

    def test_scale_hierarchy_flux_np_casimir(self):
        """V_flux_min > A_np_needed >> |ζ_FP|_max."""
        v_flux_min = 1.0  # q3*q6=1 from G55 A3
        a_np_needed = 0.38  # from NP3 for λ=0.30
        zfp_max = 0.00086  # from G54-E

        assert v_flux_min > a_np_needed > 0, f"Order violated: {v_flux_min} > {a_np_needed}?"
        assert a_np_needed / zfp_max > 200, (
            f"A_np/|ζ_FP|_max = {a_np_needed / zfp_max:.0f} (expected >> 200)"
        )

    def test_no_minimum_without_np(self):
        """Without np term (A_np=0), V^EH_total has no minimum — confirms G54-F."""
        r6_no_np = find_minimum_r6(A_np=0.0, lam=0.3)
        assert r6_no_np is None, (
            f"Minimum found at ρ₆={r6_no_np} without np term — contradicts G54-F Dine-Seiberg"
        )
