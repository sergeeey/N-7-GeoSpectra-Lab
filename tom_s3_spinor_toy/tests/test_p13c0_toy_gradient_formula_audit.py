"""Tests for the P13C0 toy gradient formula audit."""

from __future__ import annotations

import sympy as sp

from p13b0_state_measure_selection_rule_audit import (
    INVALID_SPINOR_STATE,
    SCALAR_STATE,
    SPINOR_STATE,
    classify_state_tuple,
    states_up_to_kmax,
)
from p13b1_spinor_state_selection_rule_repair import P13B_PATTERN_STILL_VALID
from p13c0_toy_gradient_formula_audit import (
    ASSUMED_BY_MODEL,
    BEN_ACHOUR_E_MODE_FORMULA_PENDING,
    LOW_MODE_TABLE_REPAIRED,
    NORMALIZATION_DEPENDENT,
    TOY_GRADIENT_REDUCED_ELEMENT_DERIVED,
    build_p13c0_toy_gradient_formula_audit,
    full_matrix_element,
    p13c0_toy_gradient_formula_audit_summary,
)


def test_p13c0_summary_reports_toy_gradient_status_and_repaired_table() -> None:
    summary = p13c0_toy_gradient_formula_audit_summary()

    assert summary["status"] == "passed"
    assert summary["p13b1_status"] == "passed"
    assert summary["p13b1_verdict"] == P13B_PATTERN_STILL_VALID
    assert summary["state_count_kmax2"] == 40
    assert summary["state_count_kmax3"] == 80
    assert summary["zero_tuple_classification_spinor"] == INVALID_SPINOR_STATE
    assert summary["zero_tuple_classification_scalar"] == SCALAR_STATE
    assert summary["j_r_zero_state_valid"] is True
    assert summary["low_mode_table_status"] == LOW_MODE_TABLE_REPAIRED
    assert summary["toy_gradient_formula_status"] == TOY_GRADIENT_REDUCED_ELEMENT_DERIVED
    assert summary["ben_achour_mode_formula_status"] == BEN_ACHOUR_E_MODE_FORMULA_PENDING
    assert summary["selection_rule_j_right_status"] == ASSUMED_BY_MODEL
    assert summary["selection_rule_j_left_status"] == TOY_GRADIENT_REDUCED_ELEMENT_DERIVED
    assert summary["normalization_status"] == NORMALIZATION_DEPENDENT
    assert summary["verdict"] == NORMALIZATION_DEPENDENT
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False

    assert len(summary["low_mode_table_entries"]) == 2
    assert summary["low_mode_table_entries"][0].expected == -sp.Rational(4, 3)
    assert summary["low_mode_table_entries"][1].expected == -sp.Rational(2, 3)
    assert summary["low_mode_table_mismatches"] == ()


def test_p13c0_low_mode_table_matches_full_matrix_element_and_keeps_spinor_state_validity() -> None:
    summary = p13c0_toy_gradient_formula_audit_summary()

    for entry in summary["low_mode_table_entries"]:
        assert full_matrix_element(entry.source, entry.target) == entry.expected

    states = states_up_to_kmax(2)
    assert len(states) == 40
    assert states[0].j_right == 0.0
    assert classify_state_tuple((0.5, -0.5, 0.0, 0.0)) == SPINOR_STATE
    assert classify_state_tuple((0.0, 0.0, 0.0, 0.0)) == INVALID_SPINOR_STATE


def test_p13c0_build_contract_marks_ben_achour_formula_pending() -> None:
    build = build_p13c0_toy_gradient_formula_audit()

    assert build.p13b1_status == "passed"
    assert build.p13b1_verdict == P13B_PATTERN_STILL_VALID
    assert build.low_mode_table_status == LOW_MODE_TABLE_REPAIRED
    assert build.toy_gradient_formula_status == TOY_GRADIENT_REDUCED_ELEMENT_DERIVED
    assert build.ben_achour_mode_formula_status == BEN_ACHOUR_E_MODE_FORMULA_PENDING
    assert build.selection_rule_j_right_status == ASSUMED_BY_MODEL
    assert build.normalization_status == NORMALIZATION_DEPENDENT
    assert build.verdict == NORMALIZATION_DEPENDENT
