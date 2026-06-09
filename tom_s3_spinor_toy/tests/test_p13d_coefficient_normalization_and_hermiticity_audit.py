"""Tests for the P13D coefficient normalization and Hermiticity audit."""

from __future__ import annotations

from p13d_coefficient_normalization_and_hermiticity_audit import (
    CONVENTION_FIXED,
    NORMALIZATION_DEPENDENT,
    PHASE_DEPENDENT,
    SOURCE_FIXED,
    build_p13d_coefficient_normalization_and_hermiticity_audit,
    p13d_coefficient_normalization_and_hermiticity_audit_summary,
)
from p13c_reduced_matrix_element_normalization_audit import (
    NORMALIZATION_DEPENDENT as P13C_REDUCED_NORMALIZATION_DEPENDENT,
    PHASE_CONVENTION_DEPENDENT,
    _wrong_normalization_control,
    _wrong_phase_control,
)


def test_p13d_summary_reports_normalization_dependent_exact_coefficients() -> None:
    summary = p13d_coefficient_normalization_and_hermiticity_audit_summary()

    assert summary["status"] == "passed"
    assert summary["p13a_status"] == "passed"
    assert summary["p13b1_status"] == "passed"
    assert summary["p13c0_status"] == "passed"
    assert summary["p13c_status"] == "passed"
    assert summary["p11_status"] == "passed"
    assert summary["p12_status"] == "passed"
    assert summary["p7_status"] == "su4_algebra_audit_passed_with_normalization_dependent_yw"
    assert summary["source_identity_status"] == SOURCE_FIXED
    assert summary["convention_stack_status"] == CONVENTION_FIXED
    assert summary["hermiticity_status"] == CONVENTION_FIXED
    assert summary["coefficient_scaling_status"] == NORMALIZATION_DEPENDENT
    assert summary["p11_p12_compatibility_status"] == CONVENTION_FIXED
    assert summary["ad_hoc_normalization_status"] == CONVENTION_FIXED
    assert summary["exact_coefficient_status"] == NORMALIZATION_DEPENDENT
    assert summary["exact_normalization_status"] == NORMALIZATION_DEPENDENT
    assert summary["phase_status"] == PHASE_DEPENDENT
    assert summary["lambda_status"] == "REQUIRES_PHYSICAL_COUPLING_INPUT"
    assert summary["verdict"] == NORMALIZATION_DEPENDENT
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False


def test_p13d_controls_preserve_pattern_and_flag_phase_and_scaling() -> None:
    wrong_norm = _wrong_normalization_control()
    wrong_phase = _wrong_phase_control()

    assert wrong_norm["status"] == P13C_REDUCED_NORMALIZATION_DEPENDENT
    assert wrong_norm["pattern_preserved"] is True
    assert wrong_norm["coefficients_changed"] is True
    assert wrong_phase["status"] == PHASE_CONVENTION_DEPENDENT
    assert wrong_phase["pattern_preserved"] is True
    assert wrong_phase["coefficients_changed"] is True


def test_p13d_build_contract_tracks_hermiticity_and_nonpromotion() -> None:
    audit = build_p13d_coefficient_normalization_and_hermiticity_audit()

    assert audit.source_identity_status == SOURCE_FIXED
    assert audit.convention_stack_status == CONVENTION_FIXED
    assert audit.hermiticity_status == CONVENTION_FIXED
    assert audit.coefficient_scaling_status == NORMALIZATION_DEPENDENT
    assert audit.p11_p12_compatibility_status == CONVENTION_FIXED
    assert audit.ad_hoc_normalization_status == CONVENTION_FIXED
    assert audit.exact_coefficient_status == NORMALIZATION_DEPENDENT
    assert audit.exact_normalization_status == NORMALIZATION_DEPENDENT
    assert audit.phase_status == PHASE_DEPENDENT
    assert audit.verdict == NORMALIZATION_DEPENDENT
    assert audit.p13b1_status == "passed"
    assert audit.p13c_status == "passed"
    assert audit.p12_status == "passed"
    assert audit.p7_status == "su4_algebra_audit_passed_with_normalization_dependent_yw"
    assert "physical V-operator density" in audit.blocking_fields
