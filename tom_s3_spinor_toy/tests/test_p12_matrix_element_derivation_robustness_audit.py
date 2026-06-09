"""Smoke tests for the P12 matrix-element derivation robustness audit."""

from __future__ import annotations

from p12_matrix_element_derivation_robustness_audit import (
    evaluate_basis_ordering_robustness,
    evaluate_k_max_extension,
    evaluate_normalization_robustness,
    evaluate_phase_convention_robustness,
    p12_matrix_element_derivation_robustness_audit_summary,
)


def test_p12_robustness_audit_reports_robust_selection_patterns() -> None:
    summary = p12_matrix_element_derivation_robustness_audit_summary()

    assert summary["p11_status"] == "passed"
    assert summary["p10_status"] == "passed"
    assert summary["basis_ordering_status"] == "PERMUTED_EQUIVALENT"
    assert summary["phase_status"] == "PHASE_DEPENDENT"
    assert summary["normalization_status"] == "NORMALIZATION_DEPENDENT"
    assert summary["k_max_status"] == "ROBUST"
    assert summary["hermiticity_status"] == "ROBUST"
    assert summary["overall_status"] == "ROBUST"
    assert summary["selection_rule_status"] == "smoke_only"
    assert summary["status"] == "passed"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False

    for k_max, status, matched, hermitian_ok, oracle_nonzero, frozen_nonzero in summary["k_max_results"]:
        assert k_max in {1, 2, 3}
        assert status == "ROBUST"
        assert matched is True
        assert hermitian_ok is True
        assert oracle_nonzero == frozen_nonzero


def test_p12_axis_audits_preserve_pattern_and_hermiticity() -> None:
    basis = evaluate_basis_ordering_robustness(2)
    phase = evaluate_phase_convention_robustness(2)
    normalization = evaluate_normalization_robustness(2)
    extension = evaluate_k_max_extension((1, 2, 3))

    assert basis["status"] == "PERMUTED_EQUIVALENT"
    assert phase["status"] == "PHASE_DEPENDENT"
    assert normalization["status"] == "NORMALIZATION_DEPENDENT"
    assert extension["status"] == "ROBUST"

    assert all(match and herm_ok and frozen_herm_ok for _, match, herm_ok, frozen_herm_ok in basis["checks"])
    assert all(match and herm_ok for _, match, herm_ok in phase["checks"])
    assert all(match and herm_ok for _, match, herm_ok in normalization["checks"])
    assert all(status == "ROBUST" for _, status, *_ in extension["results"])

