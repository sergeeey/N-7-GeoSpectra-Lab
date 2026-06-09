"""Tests for the P13E reduced coefficient scale fixing or no-go audit."""

from __future__ import annotations

from p13e_reduced_coefficient_scale_fixing_or_no_go import (
    CONVENTION_FIXED,
    FREE_COUPLING_PARAMETER,
    NORMALIZATION_DEPENDENT_NO_GO,
    SOURCE_FIXED,
    build_p13e_reduced_coefficient_scale_audit,
    p13e_reduced_coefficient_scale_audit_summary,
)


def test_p13e_summary_reports_no_go_for_unfixed_scale() -> None:
    summary = p13e_reduced_coefficient_scale_audit_summary()

    assert summary["status"] == "passed"
    assert summary["p13a_status"] == "passed"
    assert summary["p13b1_status"] == "passed"
    assert summary["p13c_status"] == "passed"
    assert summary["p13d_status"] == "passed"
    assert summary["p11_status"] == "passed"
    assert summary["p12_status"] == "passed"
    assert summary["p7_status"] == "su4_algebra_audit_passed_with_normalization_dependent_yw"
    assert summary["source_identity_status"] == SOURCE_FIXED
    assert summary["convention_stack_status"] == CONVENTION_FIXED
    assert summary["hermiticity_status"] == CONVENTION_FIXED
    assert summary["pattern_compatibility_status"] == CONVENTION_FIXED
    assert summary["scale_fix_status"] == NORMALIZATION_DEPENDENT_NO_GO
    assert summary["coupling_parameter_status"] == FREE_COUPLING_PARAMETER
    assert summary["normalization_status"] == "NORMALIZATION_DEPENDENT"
    assert summary["verdict"] == NORMALIZATION_DEPENDENT_NO_GO
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False


def test_p13e_build_contract_tracks_no_go_and_compatibility() -> None:
    audit = build_p13e_reduced_coefficient_scale_audit()

    assert audit.source_identity_status == SOURCE_FIXED
    assert audit.convention_stack_status == CONVENTION_FIXED
    assert audit.hermiticity_status == CONVENTION_FIXED
    assert audit.pattern_compatibility_status == CONVENTION_FIXED
    assert audit.scale_fix_status == NORMALIZATION_DEPENDENT_NO_GO
    assert audit.coupling_parameter_status == FREE_COUPLING_PARAMETER
    assert audit.verdict == NORMALIZATION_DEPENDENT_NO_GO
    assert "free coupling lambda" in audit.blocking_fields
    assert audit.p13d_status == "passed"
    assert audit.p12_status == "passed"
    assert audit.p11_status == "passed"

