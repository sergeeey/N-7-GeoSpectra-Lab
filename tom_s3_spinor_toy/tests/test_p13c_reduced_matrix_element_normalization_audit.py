"""Tests for the P13C reduced matrix-element normalization audit."""

from __future__ import annotations

import numpy as np

from ben_achour_one_form_modes import (
    BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE,
    NORMALIZATION_DEPENDENT as BEN_ACHOUR_NORMALIZATION_DEPENDENT,
    build_low_mode_ben_achour_one_form_modes,
)
from convention_registry import (
    NORMALIZATION_DEPENDENT,
    PHASE_CONVENTION_DEPENDENT,
)
from p13c_reduced_matrix_element_normalization_audit import (
    RELATIVE_COEFFICIENTS_DERIVED,
    REQUIRES_PHYSICAL_COUPLING_INPUT,
    build_p13c_reduced_matrix_element_normalization_audit,
    p13c_reduced_matrix_element_normalization_audit_summary,
    _wrong_normalization_control,
    _wrong_phase_control,
)
from s3_reduced_matrix_elements import reduced_element_metadata, reduced_elements_for_kmax1


def test_p13c_summary_reports_normalization_dependency_without_promotion() -> None:
    summary = p13c_reduced_matrix_element_normalization_audit_summary()

    assert summary["status"] == "passed"
    assert summary["p13a_status"] == "passed"
    assert summary["p13a1_status"] == BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE
    assert summary["p13b_status"] == "passed"
    assert summary["p11_status"] == "passed"
    assert summary["p12_status"] == "passed"
    assert summary["pattern_level_status"] == "DERIVED"
    assert summary["relative_coefficient_status"] == RELATIVE_COEFFICIENTS_DERIVED
    assert summary["absolute_normalization_status"] == NORMALIZATION_DEPENDENT
    assert summary["lambda_status"] == REQUIRES_PHYSICAL_COUPLING_INPUT
    assert summary["phase_status"] == PHASE_CONVENTION_DEPENDENT
    assert summary["p9_p10_comparison_status"] == NORMALIZATION_DEPENDENT
    assert summary["normalization_control_status"] == NORMALIZATION_DEPENDENT
    assert summary["phase_control_status"] == PHASE_CONVENTION_DEPENDENT
    assert summary["exact_coefficients_status"] == NORMALIZATION_DEPENDENT
    assert summary["reduced_matrix_element_status"] == RELATIVE_COEFFICIENTS_DERIVED
    assert summary["verdict"] == NORMALIZATION_DEPENDENT
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False

    source_names = {record.source for record in summary["coefficient_sources"]}
    source_statuses = {record.source_classification for record in summary["coefficient_sources"]}
    assert {
        "Wigner/CG coefficient",
        "reduced matrix element",
        "Ben Achour E_i/E'_i normalization",
        "gamma/Clifford normalization",
        "SU4 generator normalization",
        "coupling lambda",
    } <= source_names
    assert RELATIVE_COEFFICIENTS_DERIVED in source_statuses
    assert NORMALIZATION_DEPENDENT in source_statuses
    assert REQUIRES_PHYSICAL_COUPLING_INPUT in source_statuses

    assert summary["reduced_element_sample_count"] > 0
    assert summary["reduced_element_sample_nonzero"] > 0
    assert isinstance(summary["reduced_element_sample_value"], complex)


def test_p13c_controls_preserve_pattern_but_change_coefficients() -> None:
    wrong_norm = _wrong_normalization_control()
    wrong_phase = _wrong_phase_control()
    reduced_elements = reduced_elements_for_kmax1()
    metadata = reduced_element_metadata()
    low_mode = build_low_mode_ben_achour_one_form_modes(L=2, m_plus=0, m_minus=0)

    assert wrong_norm["status"] == NORMALIZATION_DEPENDENT
    assert wrong_norm["pattern_preserved"] is True
    assert wrong_norm["coefficients_changed"] is True
    assert wrong_phase["status"] == PHASE_CONVENTION_DEPENDENT
    assert wrong_phase["pattern_preserved"] is True
    assert wrong_phase["coefficients_changed"] is True
    assert metadata["final_ben_achour_normalization"] == "unresolved"
    assert metadata["normalization_status"] == "ANALYTIC_DIRECT_HAAR_CONVENTION"
    assert low_mode.normalization_status == BEN_ACHOUR_NORMALIZATION_DEPENDENT
    assert low_mode.readiness_verdict == BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE
    assert reduced_elements
    assert all(np.isfinite(value) for value in reduced_elements.values())


def test_p13c_build_contract_exposes_normalization_dependent_verdict() -> None:
    build = build_p13c_reduced_matrix_element_normalization_audit()

    assert build.p13a_status == "passed"
    assert build.p13a1_status == BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE
    assert build.p13b_status == "passed"
    assert build.pattern_level_status == "DERIVED"
    assert build.relative_coefficient_status == RELATIVE_COEFFICIENTS_DERIVED
    assert build.absolute_normalization_status == NORMALIZATION_DEPENDENT
    assert build.lambda_status == REQUIRES_PHYSICAL_COUPLING_INPUT
    assert build.phase_status == PHASE_CONVENTION_DEPENDENT
    assert build.normalization_control_status == NORMALIZATION_DEPENDENT
    assert build.phase_control_status == PHASE_CONVENTION_DEPENDENT
    assert build.exact_coefficients_status == NORMALIZATION_DEPENDENT
    assert build.reduced_matrix_element_status == RELATIVE_COEFFICIENTS_DERIVED
    assert build.verdict == NORMALIZATION_DEPENDENT
    assert build.su4_status == "su4_algebra_audit_passed_with_normalization_dependent_yw"
