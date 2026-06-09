"""Tests for the P13F V-operator derivation status and no-go record."""

from __future__ import annotations

from p13f_v_operator_derivation_status_and_no_go_record import (
    CONVENTION_FIXED,
    FREE_COUPLING_PARAMETER,
    NO_GO_RECORD,
    NORMALIZATION_DEPENDENT_NO_GO,
    SOURCE_FIXED,
    build_p13f_v_operator_derivation_status_and_no_go_record,
    p13f_v_operator_derivation_status_and_no_go_record_summary,
)


def test_p13f_summary_reports_final_no_go_record() -> None:
    summary = p13f_v_operator_derivation_status_and_no_go_record_summary()

    assert summary["status"] == "passed"
    assert summary["p13a_status"] == "passed"
    assert summary["p13b1_status"] == "passed"
    assert summary["p13c_status"] == "passed"
    assert summary["p13d_status"] == "passed"
    assert summary["p13e_status"] == "passed"
    assert summary["p11_status"] == "passed"
    assert summary["p12_status"] == "passed"
    assert summary["p7_status"] == "su4_algebra_audit_passed_with_normalization_dependent_yw"
    assert summary["source_identity_status"] == SOURCE_FIXED
    assert summary["convention_stack_status"] == CONVENTION_FIXED
    assert summary["hermiticity_status"] == CONVENTION_FIXED
    assert summary["compatibility_status"] == CONVENTION_FIXED
    assert summary["scale_status"] == NORMALIZATION_DEPENDENT_NO_GO
    assert summary["coupling_status"] == FREE_COUPLING_PARAMETER
    assert summary["operator_status"] == "V_OPERATOR_DERIVATION_BLOCKED"
    assert summary["verdict"] == NO_GO_RECORD
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False


def test_p13f_build_contract_tracks_blocking_fields() -> None:
    record = build_p13f_v_operator_derivation_status_and_no_go_record()

    assert record.source_identity_status == SOURCE_FIXED
    assert record.convention_stack_status == CONVENTION_FIXED
    assert record.hermiticity_status == CONVENTION_FIXED
    assert record.compatibility_status == CONVENTION_FIXED
    assert record.scale_status == NORMALIZATION_DEPENDENT_NO_GO
    assert record.coupling_status == FREE_COUPLING_PARAMETER
    assert record.verdict == NO_GO_RECORD
    assert "free coupling lambda" in record.blocking_fields
    assert "physical V-operator density" in record.blocking_fields

