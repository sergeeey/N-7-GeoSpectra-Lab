"""Tests — AV-2 G2: Boundary exponent measurement (H-AV2 mechanism).

Gate: AV2-G2 (from claim_av2_angular.md)
Report: experiments/20260610-spinor-geometry-pivot-v0.2.0/g2_boundary_exponent_report.md

Pre-registered hypotheses (from Camporesi-Higuchi eqs 3.25/3.27, written BEFORE fitting):
  |phi_nl|^2 near alpha->pi/2: ~ cos^{2*(l+1)}  (l=0 -> cos^2, VANISHES)
  |g_nl|^2   near alpha->pi/2: ~ cos^{2*l}       (l=0 -> cos^0, NONZERO)
  phi*g mixed near alpha->pi/2: ~ cos^{2*l+1}    (l=0 -> cos^1, MATCHES target)
  target sin(2alpha)           ~ cos^1 near alpha->pi/2

These regressions pin the key findings of the G2 gate:
  1. g_nl l=0 boundary exponent is ~0 (nonzero at south pole)
  2. mixed phi*g l=0 boundary exponent is ~1 (matches target)
  3. The overall gate verdict is PASS
  4. item40 is correctly set (max = RADIAL + TWO_COMPONENT_BOUNDARY_MECHANISM_SUPPORTED)

Forbidden claims (enforced by scope assertions below):
  - "full angular verification"
  - "Tom ansatz solved"
  - "H-T1 promoted"
  - "lambda fixed"
  - "safe_for_runtime"
"""

from __future__ import annotations

import numpy as np
import pytest

from tom_s3_spinor_toy.av2_g2_boundary_exponent import (
    EXPONENT_TOLERANCE,
    PREREGISTERED_G_SQ_EXPONENT,
    PREREGISTERED_MIXED_EXPONENT,
    PREREGISTERED_PHI_SQ_EXPONENT,
    TARGET_SIN2ALPHA_EXPONENT,
    _measure_boundary_exponent,
    g2_boundary_exponent_summary,
    run_g2_boundary_exponent_measurement,
)


# --- Fixtures ---


@pytest.fixture(scope="module")
def g2_report():
    """Run the full G2 gate once; reuse across tests in this module."""
    return run_g2_boundary_exponent_measurement()


@pytest.fixture(scope="module")
def g2_summary():
    """Compact summary dict."""
    return g2_boundary_exponent_summary()


# --- Sanity: pre-registered values match analytic formula ---


class TestPreregisteredValues:
    """Pre-registered exponents must match the closed-form formula from C-H.

    phi_sq: 2*(l+1),  g_sq: 2*l,  mixed: 2*l+1.
    """

    @pytest.mark.parametrize(
        "n_l,expected",
        [
            ((0, 0), 2.0),
            ((1, 0), 2.0),
            ((1, 1), 4.0),
            ((2, 0), 2.0),
            ((2, 1), 4.0),
            ((3, 2), 6.0),
        ],
    )
    def test_phi_sq_preregistered(self, n_l, expected):
        assert PREREGISTERED_PHI_SQ_EXPONENT[n_l] == pytest.approx(expected)

    @pytest.mark.parametrize(
        "n_l,expected",
        [
            ((0, 0), 0.0),  # KEY: nonzero at boundary
            ((1, 0), 0.0),
            ((1, 1), 2.0),
            ((2, 0), 0.0),
            ((2, 1), 2.0),
            ((3, 2), 4.0),
        ],
    )
    def test_g_sq_preregistered(self, n_l, expected):
        assert PREREGISTERED_G_SQ_EXPONENT[n_l] == pytest.approx(expected)

    @pytest.mark.parametrize(
        "n_l,expected",
        [
            ((0, 0), 1.0),  # KEY: matches target cos^1
            ((1, 0), 1.0),
            ((1, 1), 3.0),
            ((2, 0), 1.0),
            ((2, 1), 3.0),
        ],
    )
    def test_mixed_preregistered(self, n_l, expected):
        assert PREREGISTERED_MIXED_EXPONENT[n_l] == pytest.approx(expected)

    def test_target_exponent(self):
        assert TARGET_SIN2ALPHA_EXPONENT == pytest.approx(1.0)


# --- Unit test: _measure_boundary_exponent ---


class TestMeasureBoundaryExponent:
    """Test the log-log fitting function on known analytical inputs."""

    def test_cos_squared_exponent(self):
        """cos^2(alpha) -> exponent ~2.0."""
        alpha = np.linspace(0.01, np.pi / 2 - 0.001, 2000)
        vals = np.cos(alpha) ** 2
        exp, r2 = _measure_boundary_exponent(vals, alpha, (0.85, 0.98))
        assert abs(exp - 2.0) < EXPONENT_TOLERANCE
        assert r2 > 0.99

    def test_cos_one_exponent(self):
        """cos^1(alpha) -> exponent ~1.0. Same as sin(2alpha)."""
        alpha = np.linspace(0.01, np.pi / 2 - 0.001, 2000)
        vals = np.cos(alpha)
        exp, r2 = _measure_boundary_exponent(vals, alpha, (0.85, 0.98))
        assert abs(exp - 1.0) < EXPONENT_TOLERANCE
        assert r2 > 0.99

    def test_constant_exponent_zero(self):
        """f = 1 (constant) near boundary -> exponent ~0."""
        alpha = np.linspace(0.01, np.pi / 2 - 0.001, 2000)
        vals = np.ones_like(alpha)
        exp, r2 = _measure_boundary_exponent(vals, alpha, (0.85, 0.98))
        assert abs(exp) < EXPONENT_TOLERANCE

    def test_sin_2alpha_exponent(self):
        """sin(2alpha) = 2*sin*cos -> cos^1 near boundary."""
        alpha = np.linspace(0.01, np.pi / 2 - 0.001, 8001)
        vals = np.sin(2.0 * alpha)
        exp, r2 = _measure_boundary_exponent(vals, alpha, (0.90, 0.98))
        assert abs(exp - 1.0) < EXPONENT_TOLERANCE
        assert r2 > 0.99

    def test_all_zeros_returns_nan(self):
        """If all values are essentially zero, return nan."""
        alpha = np.linspace(0.01, np.pi / 2 - 0.001, 200)
        vals = np.zeros_like(alpha)
        exp, r2 = _measure_boundary_exponent(vals, alpha, (0.85, 0.98))
        assert np.isnan(exp)


# --- Key findings: the H-AV2 mechanism ---


class TestG2KeyFindings:
    """Pin the two key numerical results that constitute the G2 PASS verdict."""

    def test_g_l0_exponent_near_zero(self, g2_report):
        """g_nl l=0 boundary exponent must be < 0.4 (nonzero at south pole).

        Pre-registered: 0.0.  Kill threshold: 0.3.
        Measured: ~-0.096.
        This is the core of H-AV2 — the partner component g_nl does NOT vanish.
        """
        exp = g2_report.key_finding_g_l0_exponent
        assert abs(exp) < 0.40, (
            f"g_l0 exponent {exp:.4f} >= 0.40 — "
            "boundary mechanism absent (G2 kill condition triggered)"
        )

    def test_mixed_l0_exponent_near_one(self, g2_report):
        """mixed phi*g l=0 exponent must be within 0.4 of 1.0 (cos^1 structure).

        Pre-registered: 1.0.  Measured: ~0.928.
        This matches the target sin(2alpha) exponent.
        """
        exp = g2_report.key_finding_mixed_l0_exponent
        assert abs(exp - 1.0) < 0.40, (
            f"mixed_l0 exponent {exp:.4f} deviates from 1.0 by > 0.40 — no cos^1 pathway to target"
        )

    def test_mechanism_supported(self, g2_report):
        """mechanism_supported flag must be True."""
        assert g2_report.mechanism_supported is True

    def test_verdict_pass(self, g2_report):
        """G2 gate verdict must be PASS (not FAIL, not MIXED)."""
        assert g2_report.verdict == "PASS", (
            f"G2 verdict is {g2_report.verdict!r}, expected PASS. "
            f"g_l0={g2_report.key_finding_g_l0_exponent}, "
            f"mixed_l0={g2_report.key_finding_mixed_l0_exponent}"
        )


# --- item40 status cap (hard constraint) ---


class TestItem40StatusCap:
    """item40 must not exceed the allowed maximum for G2.

    G2 is NOT full angular verification.
    Maximum allowed: RADIAL + TWO_COMPONENT_BOUNDARY_MECHANISM_SUPPORTED.
    Forbidden: any claim about angular singlet, H-T1 promotion, lambda fixed.
    """

    ALLOWED_STATUSES = {
        "RADIAL + TWO_COMPONENT_BOUNDARY_MECHANISM_SUPPORTED",
        "RADIAL + TWO_COMPONENT_BOUNDARY_MECHANISM_PARTIAL",
        "RADIAL + DICTIONARY_ROBUST",  # fallback on G2 FAIL
    }

    FORBIDDEN_SUBSTRINGS = [
        "ANGULAR_SINGLET",
        "H_T1_PROMOTED",
        "H-T1",
        "LAMBDA_FIXED",
        "SAFE_FOR_RUNTIME",
        "PHYSICAL_V",
    ]

    def test_item40_within_allowed_set(self, g2_report):
        assert g2_report.item40_max_status in self.ALLOWED_STATUSES, (
            f"item40 = {g2_report.item40_max_status!r} is outside the allowed set"
        )

    def test_item40_no_forbidden_substrings(self, g2_report):
        status = g2_report.item40_max_status.upper()
        for substr in self.FORBIDDEN_SUBSTRINGS:
            assert substr not in status, (
                f"item40 = {g2_report.item40_max_status!r} contains forbidden substring {substr!r}"
            )

    def test_summary_item40_consistent(self, g2_summary):
        """Summary dict item40 must match full report."""
        assert g2_summary["item40_status"] in self.ALLOWED_STATUSES


# --- Scope integrity: forbidden claims not present ---


class TestScopeIntegrity:
    """The scope and forbidden_claims fields must be set correctly."""

    SCOPE_KEYWORDS_REQUIRED = [
        "no full angular verification",
        "no physical promotion",
        "no h-t1 promotion",
    ]

    def test_scope_field_present(self, g2_report):
        assert g2_report.scope, "scope field is empty"

    def test_scope_contains_key_restrictions(self, g2_report):
        scope_lower = g2_report.scope.lower()
        for kw in self.SCOPE_KEYWORDS_REQUIRED:
            assert kw in scope_lower, f"scope missing required restriction: {kw!r}"

    def test_forbidden_claims_not_empty(self, g2_report):
        assert len(g2_report.forbidden_claims) >= 4

    def test_forbidden_claims_include_angular_full(self, g2_report):
        fc = [c.lower() for c in g2_report.forbidden_claims]
        assert any("full angular" in c for c in fc), (
            "forbidden_claims does not include 'full angular verification'"
        )

    def test_forbidden_claims_include_lambda_fixed(self, g2_report):
        fc = [c.lower() for c in g2_report.forbidden_claims]
        assert any("lambda" in c for c in fc), "forbidden_claims does not include lambda constraint"


# --- Per-bilinear PASS/FAIL regression ---


class TestPerBilinearFits:
    """Regression: confirm specific (n,l,bilinear) fits are PASS.

    These are the critical modes for H-AV2.
    """

    @pytest.mark.parametrize(
        "n,ang_l,btype,expected_exp,tol",
        [
            (0, 0, "phi_sq", 2.0, 0.25),
            (0, 0, "g_sq", 0.0, 0.25),  # KEY: nonzero at boundary
            (0, 0, "mixed_phi_g", 1.0, 0.25),  # KEY: cos^1
            (1, 0, "phi_sq", 2.0, 0.25),
            (1, 0, "g_sq", 0.0, 0.25),
            (1, 0, "mixed_phi_g", 1.0, 0.30),  # slightly wider due to higher mode
            (1, 1, "phi_sq", 4.0, 0.25),
            (1, 1, "g_sq", 2.0, 0.25),
            (1, 1, "mixed_phi_g", 3.0, 0.25),
        ],
    )
    def test_fit_within_tolerance(self, g2_report, n, ang_l, btype, expected_exp, tol):
        """Check median fitted exponent across 3 windows is within tolerance."""
        fits = [
            f
            for f in g2_report.fits
            if f.n == n
            and f.ang_l == ang_l
            and f.bilinear_type == btype
            and f.fitted_exponent != -999.0
        ]
        assert fits, f"No fits found for (n={n}, l={ang_l}, {btype})"
        median_exp = float(np.median([f.fitted_exponent for f in fits]))
        assert abs(median_exp - expected_exp) < tol, (
            f"(n={n}, l={ang_l}, {btype}): fitted={median_exp:.4f}, "
            f"expected={expected_exp:.1f}, tol={tol}"
        )

    def test_target_sin2alpha_exponent(self, g2_report):
        """Target sin(2alpha) sanity measurement must give exponent ~1."""
        fits = [
            f
            for f in g2_report.fits
            if f.bilinear_type == "target_sin2alpha" and f.fitted_exponent != -999.0
        ]
        assert fits, "No target_sin2alpha fits found"
        median_exp = float(np.median([f.fitted_exponent for f in fits]))
        assert abs(median_exp - 1.0) < 0.1, (
            f"target sin(2alpha) exponent = {median_exp:.4f}, expected ~1.0"
        )
