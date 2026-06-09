"""Tests for the P13H absolute normalization integral audit."""

from __future__ import annotations

import sympy as sp

from p13b1_spinor_state_selection_rule_repair import SPINOR_STATE
from p13e_reduced_coefficient_scale_fixing_or_no_go import (
    FREE_COUPLING_PARAMETER,
    NORMALIZATION_DEPENDENT_NO_GO,
)
from p13h_s3_absolute_normalization_integral_test import (
    CONVENTION_FIXED,
    EXACT_INTEGRAL_DERIVED,
    MEASURE_APPLIED_ONCE,
    P13H_S3_ABSOLUTE_NORMALIZATION_INTEGRAL_TEST_STATUS,
    LAMBDA,
    RHO,
    build_p13h_s3_absolute_normalization_integral_test,
    p13h_s3_absolute_normalization_integral_test_summary,
)


def test_p13h_summary_reports_exact_integral_and_no_go() -> None:
    summary = p13h_s3_absolute_normalization_integral_test_summary()

    assert summary["status"] == P13H_S3_ABSOLUTE_NORMALIZATION_INTEGRAL_TEST_STATUS
    assert summary["p13a_status"] == "passed"
    assert summary["p13b1_status"] == "passed"
    assert summary["p13c_status"] == "passed"
    assert summary["p13d_status"] == "passed"
    assert summary["p13e_status"] == "passed"
    assert summary["p13f_status"] == "passed"
    assert summary["p13g_status"] == "passed"
    assert summary["measure_status"] == MEASURE_APPLIED_ONCE
    assert summary["exact_integral_status"] == EXACT_INTEGRAL_DERIVED
    assert summary["lowest_repaired_spinor_state_classification"] == SPINOR_STATE
    assert summary["selected_state_pair_status"] == "LOWEST_REPAIRED_SPINOR_PAIR"
    assert summary["phase_invariance_status"] == CONVENTION_FIXED
    assert summary["normalization_status"] == NORMALIZATION_DEPENDENT_NO_GO
    assert summary["lambda_status"] == FREE_COUPLING_PARAMETER
    assert summary["verdict"] == NORMALIZATION_DEPENDENT_NO_GO
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False

    expected_coefficient = 16 * sp.pi**2 * RHO**3 / 15
    assert sp.simplify(summary["coefficient_symbolic"] - expected_coefficient) == 0
    assert sp.simplify(summary["matrix_element_symbolic"] - expected_coefficient * LAMBDA) == 0
    assert sp.simplify(summary["measure_once_value"] - 2 * sp.pi**2 * RHO**3) == 0
    assert sp.simplify(summary["measure_double_count_value"] - 8 * sp.pi**4 * RHO**3) == 0


def test_p13h_build_contract_preserves_phase_invariance_and_lowest_state() -> None:
    audit = build_p13h_s3_absolute_normalization_integral_test()

    assert audit.lowest_repaired_spinor_state_classification == SPINOR_STATE
    assert audit.measure_status == MEASURE_APPLIED_ONCE
    assert audit.phase_invariance_status == CONVENTION_FIXED
    assert audit.normalization_status == NORMALIZATION_DEPENDENT_NO_GO
    assert audit.lambda_status == FREE_COUPLING_PARAMETER
    assert audit.exact_integral_status == EXACT_INTEGRAL_DERIVED
    assert audit.verdict == NORMALIZATION_DEPENDENT_NO_GO
    assert audit.pattern_status == "MATCHES_FROZEN_SCAFFOLD"
    assert "physical V-operator derivation" in audit.forbidden_claims


def test_p13h_coefficient_is_exact_and_phase_twist_is_invariant() -> None:
    summary = p13h_s3_absolute_normalization_integral_test_summary()

    assert sp.simplify(summary["matrix_element_symbolic"] / LAMBDA - summary["coefficient_symbolic"]) == 0
    assert sp.simplify(summary["coefficient_symbolic"] - 16 * sp.pi**2 * RHO**3 / 15) == 0
