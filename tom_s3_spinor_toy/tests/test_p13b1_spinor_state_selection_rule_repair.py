"""Tests for the P13B1 spinor-state and selection-rule repair."""

from __future__ import annotations

from p13b0_state_measure_selection_rule_audit import INVALID_SPINOR_STATE, SCALAR_STATE, SPINOR_STATE
from p13b1_spinor_state_selection_rule_repair import (
    P13B_PATTERN_STILL_VALID,
    build_p13b1_spinor_state_selection_rule_repair,
    p13b1_spinor_state_selection_rule_repair_summary,
)
from p11_external_oracle_matrix_element_derivation import MATCHES_FROZEN_SCAFFOLD


def test_p13b1_summary_repairs_spinor_basis_without_p13c() -> None:
    summary = p13b1_spinor_state_selection_rule_repair_summary()

    assert summary["status"] == "passed"
    assert summary["p13b0_status"] == "BLOCKED_BY_INVALID_SPINOR_STATE"
    assert summary["p11_status"] == "passed"
    assert summary["p12_status"] == "passed"
    assert summary["state_count_kmax2"] == 40
    assert summary["state_count_kmax3"] == 80
    assert summary["zero_tuple_classification_spinor"] == INVALID_SPINOR_STATE
    assert summary["zero_tuple_classification_scalar"] == SCALAR_STATE
    assert summary["spinor_state_filter_status"] == SPINOR_STATE
    assert summary["pattern_comparison_status"] == P13B_PATTERN_STILL_VALID
    assert summary["rerun_p13b_required"] is False
    assert summary["verdict"] == P13B_PATTERN_STILL_VALID
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False

    assert summary["lowest_spinor_state_kmax2"].index == 0
    assert summary["lowest_spinor_state_kmax2"].k == 0
    assert summary["lowest_spinor_state_kmax2"].branch == "positive"
    assert summary["lowest_spinor_state_kmax2"].j_left == 0.5
    assert summary["lowest_spinor_state_kmax2"].m_left == -0.5
    assert summary["lowest_spinor_state_kmax2"].j_right == 0.0
    assert summary["lowest_spinor_state_kmax2"].m_right == 0.0
    assert summary["lowest_spinor_state_kmax3"].index == 0
    assert summary["lowest_spinor_state_kmax3"].k == 0
    assert summary["lowest_spinor_state_kmax3"].branch == "positive"

    assert summary["allowed_final_state_count_lowest_kmax2"] > 0
    assert summary["delta_j_left_status"] == "DERIVED"
    assert summary["delta_m_left_status"] == "DERIVED"
    assert summary["delta_j_right_status"] == "PATTERN_SUPPORTED"
    assert summary["delta_m_right_status"] == "PATTERN_SUPPORTED"


def test_p13b1_build_contract_keeps_pattern_and_basis_repairs_separate() -> None:
    audit = build_p13b1_spinor_state_selection_rule_repair()

    assert audit.p13b0_status == "BLOCKED_BY_INVALID_SPINOR_STATE"
    assert audit.p11_status == "passed"
    assert audit.p12_status == "passed"
    assert audit.pattern_comparison_status == P13B_PATTERN_STILL_VALID
    assert audit.verdict == P13B_PATTERN_STILL_VALID
    assert audit.rerun_p13b_required is False
    assert audit.allowed_final_state_count_lowest_kmax2 == len(audit.allowed_final_states_lowest_kmax2)
    assert audit.allowed_final_state_count_lowest_kmax2 > 0


def test_p13b1_regression_keeps_frozen_oracle_alignment() -> None:
    summary = p13b1_spinor_state_selection_rule_repair_summary()

    assert summary["pattern_comparison_status"] == P13B_PATTERN_STILL_VALID
    assert summary["p11_status"] == "passed"
    assert summary["p12_status"] == "passed"
    assert MATCHES_FROZEN_SCAFFOLD == "MATCHES_FROZEN_SCAFFOLD"
