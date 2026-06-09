"""Tests for the P13B0 state / measure / selection-rule audit."""

from __future__ import annotations

from p13b0_state_measure_selection_rule_audit import (
    BLACK_BOX_DEPENDENCY,
    BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE,
    BLOCKED_BY_INVALID_SPINOR_STATE,
    COMPLEX_PRESERVED,
    INCONCLUSIVE,
    INVALID_SPINOR_STATE,
    MEASURE_APPLIED_ONCE,
    SPINOR_STATE,
    build_p13b0_state_measure_selection_rule_audit,
    classify_state_tuple,
    p13b0_state_measure_selection_rule_audit_summary,
    states_up_to_kmax,
)


def test_p13b0_summary_reports_repair_gate_blocker_and_measure_once() -> None:
    summary = p13b0_state_measure_selection_rule_audit_summary()

    assert summary["status"] == "passed"
    assert summary["p13a1_status"] == BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE
    assert summary["p11_status"] == "passed"
    assert summary["p12_status"] == "passed"
    assert summary["state_count_kmax2"] == 40
    assert summary["zero_tuple_classification"] == INVALID_SPINOR_STATE
    assert summary["measure_status"] == MEASURE_APPLIED_ONCE
    assert summary["measure_once_status"] == MEASURE_APPLIED_ONCE
    assert summary["complex_matrix_status"] == COMPLEX_PRESERVED
    assert summary["spinor_normalization_status"] == BLACK_BOX_DEPENDENCY
    assert summary["e_mode_status"] == BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE
    assert summary["selection_rule_status"] == INCONCLUSIVE
    assert summary["verdict"] == BLOCKED_BY_INVALID_SPINOR_STATE
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False

    assert summary["lowest_spinor_state"].index == 0
    assert summary["lowest_spinor_state"].k == 0
    assert summary["lowest_spinor_state"].branch == "positive"
    assert summary["lowest_spinor_state"].j_left == 0.5
    assert summary["lowest_spinor_state"].m_left == -0.5
    assert summary["lowest_spinor_state"].j_right == 0.0
    assert summary["lowest_spinor_state"].m_right == 0.0

    for grid_n, value in summary["convergence_by_grid"]:
        assert grid_n in {20, 40, 80}
        assert isinstance(value, complex)


def test_p13b0_states_up_to_kmax2_are_classified_spinor_states() -> None:
    states = states_up_to_kmax(2)

    assert len(states) == 40
    assert all(state.classification == SPINOR_STATE for state in states)
    assert states[0].index == 0
    assert states[0].k == 0
    assert states[0].branch == "positive"
    assert states[0].j_left == 0.5
    assert states[0].m_left == -0.5
    assert states[0].j_right == 0.0
    assert states[0].m_right == 0.0


def test_p13b0_tuple_classification_distinguishes_scalar_and_spinor_contexts() -> None:
    assert classify_state_tuple((0.0, 0.0, 0.0, 0.0)) == INVALID_SPINOR_STATE
    assert classify_state_tuple((0.0, 0.0, 0.0, 0.0), context="scalar") == "SCALAR_STATE"
    assert classify_state_tuple((0.5, -0.5, 0.0, 0.0)) == SPINOR_STATE


def test_p13b0_build_contract_exposes_selection_rule_inconclusive_status() -> None:
    build = build_p13b0_state_measure_selection_rule_audit()

    assert build.selection_rule_status == INCONCLUSIVE
    assert build.selection_rule_assumption_status
    assert build.complex_matrix_status == COMPLEX_PRESERVED
    assert build.measure_status == MEASURE_APPLIED_ONCE
    assert build.verdict == BLOCKED_BY_INVALID_SPINOR_STATE
    assert build.spinor_normalization_status == BLACK_BOX_DEPENDENCY
