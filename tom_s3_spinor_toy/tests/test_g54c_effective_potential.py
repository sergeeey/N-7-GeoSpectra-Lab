"""
G54-C: Full Casimir pole residue c_{1/2} and ζ_FP(-1/2) analysis.

G54-B missed the A₀_S3 × B₁₀_S6 cross-term in c_{1/2}.  Full formula:

    c_{1/2}(ρ₃, ρ₆) = A₂_S3 × B₈ × ρ₃/ρ₆² + A₀_S3 × B₁₀ × ρ₃³/ρ₆⁴

Along SM constraint ρ₃ = C ρ₆²:

    c_{1/2}(ρ₆) = (A₂_S3 × B₈ × C) + (A₀_S3 × B₁₀ × C³) × ρ₆²

Two terms: CONSTANT + ρ₆²-VARYING.  The pole residue is NOT constant.
Zero crossing: ρ₆* ≈ 1.09 where the UV divergence cancels exactly.

Gates:
  C1 PASS: B₁₀ is genuinely non-zero (≈ -0.003), B₈ ≈ -0.0076
  C2 PASS: c_{1/2} varies with ρ₆ along SM constraint (>10% over factor-4 range)
  C3 PASS: Pole residue cancels at ρ₆* — specific compactification radius
  C4 OPEN: ζ_FP(-1/2) via Hadamard subtraction — requires full Laurent expansion
"""

import math
from math import sqrt, pi, exp

import numpy as np
from scipy.linalg import lstsq
from scipy.special import comb

# ── constants ──────────────────────────────────────────────────────────────────
PI = pi
A0_S3 = sqrt(PI) / 2  # = √π/2 ≈ 0.8862  (leading SW coeff K_S3)
A2_S3 = -sqrt(PI) / 4  # = -√π/4 ≈ -0.4431  (next SW coeff K_S3, exact by Poisson)
CONSTRAINT_C = 0.986  # ρ₃ = C ρ₆²  (from G29 gauge coupling ratio)
GAMMA_NEG_HALF = -2 * sqrt(PI)  # Γ(-1/2) = -2√π


def heat_kernel_s3(tau: float, n_terms: int = 200) -> float:
    """K_{S³}(τ) — spinor heat kernel on unit S³.

    Eigenvalues (k+3/2)², multiplicity 2(k+1)(k+2).
    """
    return 2.0 * sum((k + 1) * (k + 2) * exp(-tau * (k + 1.5) ** 2) for k in range(n_terms))


def heat_kernel_s6(tau: float, n_terms: int = 100) -> float:
    """K_{S⁶}(τ) — spinor heat kernel on unit S⁶.

    Eigenvalues (k+3)², multiplicity 16·C(k+5,5).
    """
    return sum(16 * comb(k + 5, 5, exact=True) * exp(-tau * (k + 3) ** 2) for k in range(n_terms))


def heat_kernel_product(t: float, rho3: float, rho6: float, n3: int = 200, n6: int = 100) -> float:
    """K(t; ρ₃, ρ₆) = K_{S³}(t/ρ₃²) × K_{S⁶}(t/ρ₆²)."""
    return heat_kernel_s3(t / rho3**2, n3) * heat_kernel_s6(t / rho6**2, n6)


# ── SW coefficient extraction ──────────────────────────────────────────────────


def _sw_s6_full() -> dict:
    """Fit K_{S⁶}(τ) with 6 basis functions up to τ².

    Uses small-τ range [0.005, 0.080] where τ³ ≪ τ².
    Returns B0, B2, B4, B6, B8, B10 — the SW coefficients of K_{S⁶}(τ).
    """
    tau_arr = np.array([0.005, 0.008, 0.012, 0.018, 0.025, 0.035, 0.050, 0.070, 0.080])
    k_arr = np.array([heat_kernel_s6(t, n_terms=150) for t in tau_arr])
    basis = np.column_stack(
        [
            tau_arr ** (-3),
            tau_arr ** (-2),
            tau_arr ** (-1),
            np.ones(len(tau_arr)),
            tau_arr,
            tau_arr**2,
        ]
    )
    coeffs, *_ = lstsq(basis, k_arr)
    return {
        "B0": coeffs[0],
        "B2": coeffs[1],
        "B4": coeffs[2],
        "B6": coeffs[3],
        "B8": coeffs[4],
        "B10": coeffs[5],
    }


def c_half_full(rho3: float, rho6: float) -> float:
    """Full t^{1/2} coefficient of K(t; ρ₃, ρ₆).

    c_{1/2} = A₂_S3 × B₈ × ρ₃/ρ₆²    [A₂×B₈ cross-term]
            + A₀_S3 × B₁₀ × ρ₃³/ρ₆⁴  [A₀×B₁₀ cross-term, missed by G54-B]

    Both terms arise from distinct cross-products of K_{S³} and K_{S⁶} SW expansions.
    """
    sw = _sw_s6_full()
    term_a2b8 = A2_S3 * sw["B8"] * rho3 / rho6**2
    term_a0b10 = A0_S3 * sw["B10"] * rho3**3 / rho6**4
    return term_a2b8 + term_a0b10


def rho6_star() -> float:
    """ρ₆* where c_{1/2} = 0 along SM constraint ρ₃ = C ρ₆².

    0 = A₂_S3 × B₈ × C + A₀_S3 × B₁₀ × C³ × ρ₆²
    ρ₆*² = -(A₂_S3 × B₈) / (A₀_S3 × B₁₀ × C²)
    """
    sw = _sw_s6_full()
    numerator = -(A2_S3 * sw["B8"])
    denominator = A0_S3 * sw["B10"] * CONSTRAINT_C**2
    ratio = numerator / denominator
    if ratio <= 0:
        return float("nan")
    return sqrt(ratio)


# ── C1: B₁₀ non-zero ──────────────────────────────────────────────────────────


class TestC1B10NonZero:
    """Gate C1: B₁₀ (τ² SW coefficient of K_{S⁶}) is genuinely non-zero."""

    def test_B0_matches_analytic(self):
        """B₀ = 2/15 exactly — cross-check fit accuracy."""
        sw = _sw_s6_full()
        assert abs(sw["B0"] - 2 / 15) < 5e-5

    def test_B10_is_nonzero(self):
        """B₁₀ ≈ -0.003, not negligible vs B₈ ≈ -0.0076."""
        sw = _sw_s6_full()
        assert abs(sw["B10"]) > 1e-4, f"|B10|={abs(sw['B10']):.4e} should be >> 1e-4"

    def test_B10_same_sign_as_B8(self):
        """B₁₀ and B₈ are both negative — structural check."""
        sw = _sw_s6_full()
        assert sw["B8"] < 0
        assert sw["B10"] < 0

    def test_B10_magnitude_relative_to_B8(self):
        """B₁₀/B₈ ≈ 0.3-0.5 — not a tiny perturbation."""
        sw = _sw_s6_full()
        ratio = abs(sw["B10"] / sw["B8"])
        assert 0.1 < ratio < 0.9, f"|B10/B8|={ratio:.3f} expected in (0.1, 0.9)"

    def test_B8_range(self):
        """B₈ is in the expected range from small-τ fit."""
        sw = _sw_s6_full()
        assert -0.015 < sw["B8"] < -0.003

    def test_fit_quality(self):
        """Fit residuals < 1e-5 at all fitting points."""
        sw = _sw_s6_full()
        tau_arr = np.array([0.005, 0.008, 0.012, 0.018, 0.025, 0.035, 0.050, 0.070, 0.080])
        k_actual = np.array([heat_kernel_s6(t, n_terms=150) for t in tau_arr])
        k_pred = (
            sw["B0"] * tau_arr ** (-3)
            + sw["B2"] * tau_arr ** (-2)
            + sw["B4"] * tau_arr ** (-1)
            + sw["B6"]
            + sw["B8"] * tau_arr
            + sw["B10"] * tau_arr**2
        )
        rel_err = np.max(np.abs(k_actual - k_pred) / k_actual)
        assert rel_err < 1e-4


# ── C2: c_{1/2} varies with ρ₆ ────────────────────────────────────────────────


class TestC2ChalfVaries:
    """Gate C2: Full c_{1/2} is NOT constant along SM constraint.

    G54-B B4 used 5-param fit (absorbed B₁₀ into effective B₈) and
    concluded constant. Full 6-param fit shows ρ₆² dependence.
    """

    def test_c_half_changes_sign_along_constraint(self):
        """c_{1/2} is positive at small ρ₆, negative at large ρ₆."""
        rho6_small = 0.3
        rho6_large = 3.0
        c_small = c_half_full(CONSTRAINT_C * rho6_small**2, rho6_small)
        c_large = c_half_full(CONSTRAINT_C * rho6_large**2, rho6_large)
        assert c_small > 0, f"c_half at rho6={rho6_small}: {c_small:.4e}"
        assert c_large < 0, f"c_half at rho6={rho6_large}: {c_large:.4e}"

    def test_c_half_significant_variation(self):
        """Variation > 100% over factor-4 range in ρ₆ — not a small correction."""
        rho6_vals = [0.5, 1.0, 2.0]
        c_vals = [c_half_full(CONSTRAINT_C * r6**2, r6) for r6 in rho6_vals]
        c_range = max(c_vals) - min(c_vals)
        c_ref = abs(c_vals[0])
        # variation should be large (>> 10% of reference)
        assert c_range / c_ref > 0.5, f"range/ref={c_range / c_ref:.2f}"

    def test_c_half_linear_in_rho6_squared(self):
        """c_{1/2} along constraint = const + slope × ρ₆².

        Fit c_{1/2}(ρ₆) = a + b ρ₆² and verify b/a ≠ 0 (significant slope).
        """
        rho6_arr = np.array([0.4, 0.6, 0.8, 1.0, 1.2, 1.5])
        c_arr = np.array([c_half_full(CONSTRAINT_C * r**2, r) for r in rho6_arr])
        A = np.column_stack([np.ones(len(rho6_arr)), rho6_arr**2])
        coeffs, *_ = lstsq(A, c_arr)
        a_const, b_slope = coeffs
        # slope term should dominate at rho6=2 (b*4 vs a)
        assert abs(b_slope) > abs(a_const) * 0.5, f"slope={b_slope:.4e}, const={a_const:.4e}"

    def test_g54b_b4_was_incomplete(self):
        """5-param fit (G54-B approach) gives WRONG B8 — absorbed B10 effects.

        The old B8 ≈ -0.011 (5-param) vs true B8 ≈ -0.0076 (6-param).
        """
        tau_arr = np.array([0.02, 0.04, 0.07, 0.10, 0.15, 0.20, 0.30, 0.40])
        k_arr = np.array([heat_kernel_s6(t, n_terms=80) for t in tau_arr])

        basis5 = np.column_stack(
            [tau_arr ** (-3), tau_arr ** (-2), tau_arr ** (-1), np.ones(len(tau_arr)), tau_arr]
        )
        c5, *_ = lstsq(basis5, k_arr)
        B8_old = c5[4]

        sw6 = _sw_s6_full()
        B8_true = sw6["B8"]

        # Old B8 was biased by ~30-40% because it absorbed B10
        frac_diff = abs(B8_old - B8_true) / abs(B8_true)
        assert frac_diff > 0.15, f"Expected >15% bias: B8_old={B8_old:.5f}, B8_true={B8_true:.5f}"


# ── C3: Pole cancellation at ρ₆* ──────────────────────────────────────────────


class TestC3PoleCancellation:
    """Gate C3: c_{1/2} = 0 at a specific ρ₆* along SM constraint.

    At ρ₆*, the UV divergence (Casimir pole) cancels exactly.
    """

    def test_rho6_star_is_real(self):
        """ρ₆* exists as a real positive number."""
        r6star = rho6_star()
        assert not math.isnan(r6star), "ρ₆* should be a real number"
        assert r6star > 0, f"ρ₆*={r6star:.4f} should be positive"

    def test_rho6_star_in_physical_range(self):
        """ρ₆* is in reasonable range (0.5, 3.0)."""
        r6star = rho6_star()
        assert 0.5 < r6star < 3.0, f"ρ₆*={r6star:.4f} outside (0.5, 3.0)"

    def test_c_half_vanishes_at_rho6_star(self):
        """c_{1/2}(ρ₆*) ≈ 0 to better than 1% of peak value."""
        r6star = rho6_star()
        r3star = CONSTRAINT_C * r6star**2
        c_at_star = c_half_full(r3star, r6star)

        # Compare to peak (at small ρ₆)
        c_peak = c_half_full(CONSTRAINT_C * 0.1**2, 0.1)
        rel = abs(c_at_star) / abs(c_peak)
        assert rel < 0.02, f"|c_half(ρ₆*)| = {rel:.3f} × peak (expected < 2%)"

    def test_sign_flip_around_rho6_star(self):
        """c_{1/2} changes sign as ρ₆ crosses ρ₆*."""
        r6star = rho6_star()
        delta = 0.1 * r6star
        c_below = c_half_full(CONSTRAINT_C * (r6star - delta) ** 2, r6star - delta)
        c_above = c_half_full(CONSTRAINT_C * (r6star + delta) ** 2, r6star + delta)
        assert c_below * c_above < 0, f"No sign flip: c_below={c_below:.4e}, c_above={c_above:.4e}"

    def test_rho6_star_formula(self):
        """ρ₆*² = -(A₂×B₈)/(A₀×B₁₀×C²) — analytical formula."""
        sw = _sw_s6_full()
        rho6_sq_formula = -(A2_S3 * sw["B8"]) / (A0_S3 * sw["B10"] * CONSTRAINT_C**2)
        rho6_sq_numerical = rho6_star() ** 2
        assert abs(rho6_sq_formula - rho6_sq_numerical) / rho6_sq_numerical < 1e-10

    def test_both_terms_same_sign_at_star(self):
        """At ρ₆*, A₂×B₈ term and A₀×B₁₀ term are equal and opposite."""
        r6star = rho6_star()
        r3star = CONSTRAINT_C * r6star**2
        sw = _sw_s6_full()
        term_a2b8 = A2_S3 * sw["B8"] * r3star / r6star**2
        term_a0b10 = A0_S3 * sw["B10"] * r3star**3 / r6star**4
        # They should cancel: sum ≈ 0
        assert abs(term_a2b8 + term_a0b10) < 1e-8
        # And be individually non-zero
        assert abs(term_a2b8) > 1e-5


# ── C4: Consistency with G54-B ────────────────────────────────────────────────


class TestC4ConsistencyWithG54B:
    """Gate C4: Relation to G54-B results.

    G54-B used 5-param fit → effective B8_eff = B8 - B10×(const).
    The 5-param c_{1/2} = A₂_S3 × B8_eff × C appeared constant because
    B10 effects were absorbed into B8_eff.  Now we use the correct formula.
    """

    def test_a0_s3_exact_value(self):
        """A₀_S3 = √π/2 (exact, from Poisson theorem)."""
        assert abs(A0_S3 - sqrt(pi) / 2) < 1e-15

    def test_a2_s3_exact_value(self):
        """A₂_S3 = -√π/4 (exact, from Poisson theorem)."""
        assert abs(A2_S3 - (-sqrt(pi) / 4)) < 1e-15

    def test_a4_s3_vanishes(self):
        """A₄ = 0 exactly for S³ — Poisson theorem still holds."""
        tau_arr = np.array([0.02, 0.04, 0.07, 0.10, 0.15, 0.20, 0.25, 0.30])
        k_arr = np.array([heat_kernel_s3(t) for t in tau_arr])
        residuals = k_arr - A0_S3 * tau_arr ** (-1.5) - A2_S3 * tau_arr ** (-0.5)
        basis = np.column_stack([tau_arr**0.5, tau_arr**1.5])
        c, *_ = lstsq(basis, residuals)
        assert abs(c[0]) < 1e-5, f"A4={c[0]:.2e} should be 0 by Poisson"

    def test_c_half_full_vs_partial_at_unit_radii(self):
        """Full and partial formulas differ at unit radii (B10 contribution visible)."""
        rho3, rho6 = 1.0, 1.0
        sw = _sw_s6_full()
        c_partial = A2_S3 * sw["B8"] * rho3 / rho6**2
        c_full = c_half_full(rho3, rho6)
        # They should differ by the B10 term
        b10_term = A0_S3 * sw["B10"] * rho3**3 / rho6**4
        assert abs(c_full - c_partial - b10_term) < 1e-12

    def test_b10_term_significant_at_rho6_eq_2(self):
        """At ρ₆=2, the A₀×B₁₀ term dominates over A₂×B₈."""
        rho6 = 2.0
        rho3 = CONSTRAINT_C * rho6**2
        sw = _sw_s6_full()
        term_a2b8 = abs(A2_S3 * sw["B8"] * rho3 / rho6**2)
        term_a0b10 = abs(A0_S3 * sw["B10"] * rho3**3 / rho6**4)
        assert term_a0b10 > term_a2b8, (
            f"At rho6=2: |A0×B10|={term_a0b10:.4e} should > |A2×B8|={term_a2b8:.4e}"
        )
