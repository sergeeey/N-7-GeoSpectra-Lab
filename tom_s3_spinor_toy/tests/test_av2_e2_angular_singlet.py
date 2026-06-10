"""Tests — AV-2 E2: Angular singlet check for phi_{0,0}*g_{0,0} bilinear.

Gate: AV2-E2 (precondition: E1 STRONG_PASS)
Pre-registration: experiments/.../claim_e2_angular_singlet.md

Key result: <0,0 | 1/2,+1/2; 1/2,-1/2> = sqrt(2)/2 != 0
=> phi_{0,0}*g_{0,0} has nonzero J=0 singlet projection
=> E2 PASS => item40 -> RADIAL+ANGULAR_BILINEAR_SUPPORTED

These regressions pin:
  1. The CG coefficient value (exact sympy + float)
  2. Antisymmetry under swap of m quantum numbers
  3. The triplet component is also nonzero (mixed state, not pure singlet)
  4. The verdict PASS and item40 upgrade
  5. Scope guards (no overclaiming)
"""

from __future__ import annotations

import math

import pytest
from sympy import Rational, sqrt

from tom_s3_spinor_toy.av2_e2_angular_singlet import (
    J_MODE,
    J_SINGLET,
    M_LOWER,
    M_SINGLET,
    M_UPPER,
    _compute_cg_exact,
    e2_angular_singlet_summary,
    run_e2_angular_singlet,
)


# --- Fixtures ---


@pytest.fixture(scope="module")
def e2_report():
    return run_e2_angular_singlet()


@pytest.fixture(scope="module")
def e2_summary():
    return e2_angular_singlet_summary()


# --- CG coefficient values (core algebraic result) ---


class TestCGCoefficients:
    """Pin the Clebsch-Gordan coefficients used in E2.

    Standard SU(2) result (Condon-Shortley convention):
      <0,0 | 1/2,+1/2; 1/2,-1/2> = +sqrt(2)/2
      <0,0 | 1/2,-1/2; 1/2,+1/2> = -sqrt(2)/2  (antisymmetry)
      <1,0 | 1/2,+1/2; 1/2,-1/2> = +sqrt(2)/2  (triplet component)
    """

    def test_singlet_cg_exact_value(self):
        """CG singlet = sqrt(2)/2 (exact sympy)."""
        cg = _compute_cg_exact(J_MODE, M_UPPER, J_MODE, M_LOWER, J_SINGLET, M_SINGLET)
        assert cg == sqrt(2) / 2, f"CG singlet = {cg}, expected sqrt(2)/2"

    def test_singlet_cg_float_value(self):
        """CG singlet float = 1/sqrt(2) to 12 decimal places."""
        cg = _compute_cg_exact(J_MODE, M_UPPER, J_MODE, M_LOWER, J_SINGLET, M_SINGLET)
        assert abs(float(cg) - 1.0 / math.sqrt(2)) < 1e-12

    def test_singlet_cg_squared(self, e2_report):
        """C^2 = 0.5 exactly (each of singlet and triplet gets half the weight)."""
        assert abs(e2_report.cg_squared - 0.5) < 1e-14

    def test_singlet_cg_nonzero(self, e2_report):
        """The singlet CG coefficient must be nonzero for PASS."""
        assert e2_report.cg_squared > 0

    def test_antisymmetry(self, e2_report):
        """<0,0|1/2,-1/2;1/2,+1/2> = -<0,0|1/2,+1/2;1/2,-1/2> (SU(2) antisymmetry)."""
        assert e2_report.antisymmetry_verified, (
            "Antisymmetry check failed: CG(m_lower,m_upper) != -CG(m_upper,m_lower)"
        )

    def test_triplet_cg_nonzero(self, e2_report):
        """Triplet CG coefficient <1,0|...> is also nonzero (phi*g is a mixed state)."""
        assert e2_report.triplet_nonzero, (
            "Triplet CG is zero — phi*g would be a pure singlet, "
            "which contradicts the mixed nature of the cross term"
        )

    def test_singlet_plus_triplet_weight_equals_one(self, e2_report):
        """C^2_singlet + C^2_triplet = 1 (completeness: all weight accounted for)."""
        cg_triplet = _compute_cg_exact(J_MODE, M_UPPER, J_MODE, M_LOWER, Rational(1), Rational(0))
        total = e2_report.cg_squared + float(cg_triplet**2)
        assert abs(total - 1.0) < 1e-12, f"C^2_singlet + C^2_triplet = {total:.6f}, expected 1.0"


# --- E2 gate verdict ---


class TestE2GateVerdict:
    """Pin the E2 gate result."""

    def test_verdict_pass(self, e2_report):
        """E2 verdict must be PASS (CG != 0 by SU(2) theory)."""
        assert e2_report.verdict == "PASS", (
            f"E2 verdict = {e2_report.verdict!r}, expected PASS. "
            f"cg_squared = {e2_report.cg_squared}"
        )

    def test_item40_upgraded(self, e2_report):
        """item40 must be upgraded to ANGULAR_BILINEAR_SUPPORTED on PASS."""
        assert e2_report.item40_max_status == "RADIAL + ANGULAR_BILINEAR_SUPPORTED", (
            f"item40 = {e2_report.item40_max_status!r}"
        )

    def test_summary_verdict_consistent(self, e2_summary):
        """Summary dict verdict matches report verdict."""
        assert e2_summary["verdict"] == "PASS"

    def test_summary_cg_squared_consistent(self, e2_summary):
        assert abs(e2_summary["cg_singlet_squared"] - 0.5) < 1e-14

    def test_summary_item40_consistent(self, e2_summary):
        assert e2_summary["item40_status"] == "RADIAL + ANGULAR_BILINEAR_SUPPORTED"


# --- item40 cap ---


class TestItem40Cap:
    """item40 must not exceed the E2-era maximum and must not enter forbidden states."""

    ALLOWED_E2_STATUSES = {
        "RADIAL + ANGULAR_BILINEAR_SUPPORTED",  # PASS
        "FORMAL_FIT_ONLY",  # FAIL (singlet projection = 0)
    }

    FORBIDDEN_SUBSTRINGS = [
        "TOM_ANSATZ_SOLVED",
        "H_T1_PROMOTED",
        "LAMBDA_FIXED",
        "SAFE_FOR_RUNTIME",
        "PHYSICAL_V",
    ]

    def test_item40_in_allowed_set(self, e2_report):
        assert e2_report.item40_max_status in self.ALLOWED_E2_STATUSES, (
            f"item40 = {e2_report.item40_max_status!r} not in allowed set"
        )

    def test_item40_no_forbidden_substrings(self, e2_report):
        status = e2_report.item40_max_status.upper().replace(" ", "_")
        for substr in self.FORBIDDEN_SUBSTRINGS:
            assert substr not in status, f"item40 contains forbidden substring {substr!r}"


# --- Scope guards ---


class TestScopeIntegrity:
    """Forbidden claims must not appear in the report."""

    def test_forbidden_claims_not_empty(self, e2_report):
        assert len(e2_report.forbidden_claims) >= 4

    def test_tom_ansatz_not_claimed(self, e2_report):
        fc = [c.lower() for c in e2_report.forbidden_claims]
        assert any("tom ansatz" in c for c in fc)

    def test_lambda_fixed_forbidden(self, e2_report):
        fc = [c.lower() for c in e2_report.forbidden_claims]
        assert any("lambda" in c for c in fc)

    def test_scope_says_no_full_angular(self, e2_report):
        assert "no full angular" in e2_report.scope.lower()

    def test_scope_says_no_h_t1(self, e2_report):
        assert "no h-t1" in e2_report.scope.lower()


# --- Physical interpretation (what this does NOT mean) ---


class TestPhysicalLimits:
    """Regression: E2 PASS means singlet pairing exists, not physical promotion."""

    def test_cg_squared_not_one(self, e2_report):
        """C^2 = 0.5, not 1: phi*g is NOT a pure singlet (has triplet component too).

        This prevents overclaiming: the bilinear CAN pair to singlet,
        but is not exclusively in the singlet sector.
        """
        assert e2_report.cg_squared < 1.0, (
            "cg_squared = 1.0 would mean pure singlet — overclaim territory"
        )

    def test_cg_squared_equals_half(self, e2_report):
        """Each of singlet and triplet gets exactly half the weight (equal split)."""
        assert abs(e2_report.cg_squared - 0.5) < 1e-12
