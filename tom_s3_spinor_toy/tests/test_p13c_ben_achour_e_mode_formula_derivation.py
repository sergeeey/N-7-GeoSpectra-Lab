"""Tests for the exact Ben Achour E-mode formula derivation."""

from __future__ import annotations

from p13b1_spinor_state_selection_rule_repair import P13B_PATTERN_STILL_VALID
from p13c_ben_achour_e_mode_formula_derivation import (
    BASIS_ORDERING_DEPENDENT,
    FAILED,
    NORMALIZATION_DEPENDENT,
    SOURCE_FIXED,
    build_p13c_ben_achour_e_mode_formula_derivation,
    p13c_ben_achour_e_mode_formula_derivation_summary,
)


def test_p13c_exact_formula_summary_reports_source_fixed_formula() -> None:
    summary = p13c_ben_achour_e_mode_formula_derivation_summary()

    assert summary["status"] == "passed"
    assert summary["p13a_status"] == "passed"
    assert summary["p13b1_status"] == "passed"
    assert summary["p13b1_verdict"] == P13B_PATTERN_STILL_VALID
    assert summary["p13c0_status"] == "passed"
    assert summary["p11_status"] == "passed"
    assert summary["p12_status"] == "passed"
    assert summary["source_geometry_status"] == "SOURCE_SUPPORTED_GEOMETRY"
    assert summary["source_formula_status"] == SOURCE_FIXED
    assert summary["coefficient_normalization_status"] == SOURCE_FIXED
    assert summary["reduced_matrix_element_normalization_status"] == NORMALIZATION_DEPENDENT
    assert summary["pattern_status"] == "MATCHES_FROZEN_SCAFFOLD"
    assert summary["toy_gradient_relation_status"] == NORMALIZATION_DEPENDENT
    assert summary["boundary_mode_status"] == "VANISHING_OR_EXCLUDED"
    assert summary["exact_formula_identity_status"] == SOURCE_FIXED
    assert summary["low_mode_nonzero_status"] == "SOURCE_SUPPORTED_GEOMETRY"
    assert summary["normalization_marker"] == "NORMALIZATION_DEPENDENT"
    assert summary["verdict"] == SOURCE_FIXED
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False
    assert "E_i = (L + 2) B_i + C_i" in summary["exact_formula_expression"]
    assert "E'_i = (L + 2) B'_i - C'_i" in summary["exact_formula_prime_expression"]


def test_p13c_exact_formula_build_contract_tracks_selection_pattern_and_dependency_layers() -> None:
    audit = build_p13c_ben_achour_e_mode_formula_derivation()

    assert audit.source_formula_status == SOURCE_FIXED
    assert audit.coefficient_normalization_status == SOURCE_FIXED
    assert audit.reduced_matrix_element_normalization_status == NORMALIZATION_DEPENDENT
    assert audit.pattern_status == "MATCHES_FROZEN_SCAFFOLD"
    assert audit.toy_gradient_relation_status in {NORMALIZATION_DEPENDENT, BASIS_ORDERING_DEPENDENT}
    assert audit.boundary_mode_status == "VANISHING_OR_EXCLUDED"
    assert audit.verdict == SOURCE_FIXED
    assert audit.p13b1_verdict == P13B_PATTERN_STILL_VALID
    assert audit.p13c0_status == "passed"


def test_p13c_exact_formula_rejects_failed_classification() -> None:
    summary = p13c_ben_achour_e_mode_formula_derivation_summary()

    assert summary["source_formula_status"] != FAILED
    assert summary["verdict"] != FAILED
