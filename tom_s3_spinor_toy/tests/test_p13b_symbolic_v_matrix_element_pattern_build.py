"""Tests for the P13B symbolic V matrix-element pattern build."""

from __future__ import annotations

from ben_achour_one_form_modes import (
    BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE,
    NORMALIZATION_DEPENDENT,
    SOURCE_SUPPORTED_GEOMETRY,
    VANISHING_OR_EXCLUDED,
    build_low_mode_ben_achour_one_form_modes,
    mode_applicability_status,
)
from p13b_symbolic_v_matrix_element_pattern_build import (
    SYMBOLIC_PATTERN_MATCHES_P11_P12,
    build_p13b_symbolic_v_matrix_element_pattern_build,
    build_symbolic_v_selection_pattern,
    compare_symbolic_pattern_to_frozen_scaffold,
    p13b_symbolic_v_matrix_element_pattern_build_summary,
)


def test_p13b_summary_reports_symbolic_pattern_match_without_promotion() -> None:
    summary = p13b_symbolic_v_matrix_element_pattern_build_summary()

    assert summary["status"] == "passed"
    assert summary["p13a_status"] == "passed"
    assert summary["p13a1_status"] == BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE
    assert summary["p11_status"] == "passed"
    assert summary["p12_status"] == "passed"
    assert summary["low_mode_geometry_status"] == SOURCE_SUPPORTED_GEOMETRY
    assert summary["low_mode_normalization_status"] == NORMALIZATION_DEPENDENT
    assert summary["low_mode_verdict"] == BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE
    assert summary["exact_coefficients_status"] == NORMALIZATION_DEPENDENT
    assert summary["symbolic_pattern_status"] == SYMBOLIC_PATTERN_MATCHES_P11_P12
    assert summary["comparison_status"] == SYMBOLIC_PATTERN_MATCHES_P11_P12
    assert summary["hermiticity_status"] == SYMBOLIC_PATTERN_MATCHES_P11_P12
    assert summary["p11_p12_alignment_status"] == SYMBOLIC_PATTERN_MATCHES_P11_P12
    assert summary["selection_rule_status"] == "SMOKE_ONLY"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False

    for k_max, status, same_shape, hermitian_ok, symbolic_nonzero, oracle_nonzero in summary["comparison_by_k"]:
        assert k_max in {1, 2, 3}
        assert status == SYMBOLIC_PATTERN_MATCHES_P11_P12
        assert same_shape is True
        assert hermitian_ok is True
        assert symbolic_nonzero == oracle_nonzero


def test_p13b_symbolic_pattern_matches_frozen_oracle_and_uses_low_mode_geometry() -> None:
    pattern1, states1, mask1 = build_symbolic_v_selection_pattern(1)
    pattern2, states2, mask2 = build_symbolic_v_selection_pattern(2)
    comparison1 = compare_symbolic_pattern_to_frozen_scaffold(1)
    comparison2 = compare_symbolic_pattern_to_frozen_scaffold(2)
    comparison3 = compare_symbolic_pattern_to_frozen_scaffold(3)
    low_mode = build_low_mode_ben_achour_one_form_modes(L=2, m_plus=0, m_minus=0)

    assert pattern1.shape == (16, 16)
    assert pattern2.shape == (40, 40)
    assert len(states1) == 16
    assert len(states2) == 40
    assert mask1.shape == (16, 16)
    assert mask2.shape == (40, 40)
    assert any(bool(getattr(entry, "free_symbols", set())) for entry in pattern1)
    assert any(bool(getattr(entry, "free_symbols", set())) for entry in pattern2)

    assert comparison1["pattern_matches"] is True
    assert comparison2["pattern_matches"] is True
    assert comparison3["pattern_matches"] is True
    assert comparison1["hermitian_compatible"] is True
    assert comparison2["hermitian_compatible"] is True
    assert comparison3["hermitian_compatible"] is True

    assert low_mode.source_geometry_status == SOURCE_SUPPORTED_GEOMETRY
    assert low_mode.readiness_verdict == BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE
    assert low_mode.normalization_status == NORMALIZATION_DEPENDENT
    assert any(component != 0 for component in low_mode.E.as_matrix())
    assert any(component != 0 for component in low_mode.E_prime.as_matrix())
    assert mode_applicability_status(1) == VANISHING_OR_EXCLUDED


def test_p13b_build_contract_exposes_symbolic_pattern_status() -> None:
    build = build_p13b_symbolic_v_matrix_element_pattern_build()

    assert build.p13a_status == "passed"
    assert build.p13a1_status == BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE
    assert build.p11_status == "passed"
    assert build.p12_status == "passed"
    assert build.symbolic_pattern_status == SYMBOLIC_PATTERN_MATCHES_P11_P12
    assert build.comparison_status == SYMBOLIC_PATTERN_MATCHES_P11_P12
    assert build.exact_coefficients_status == NORMALIZATION_DEPENDENT
