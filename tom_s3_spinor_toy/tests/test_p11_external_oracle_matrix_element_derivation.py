"""Smoke tests for the P11 external-oracle matrix-element derivation."""

from __future__ import annotations

from p11_external_oracle_matrix_element_derivation import (
    build_external_oracle_selection_pattern,
    build_p11_external_oracle_matrix_element_derivation,
    compare_to_frozen_v_scaffold,
    p11_external_oracle_matrix_element_derivation_summary,
)


def test_p11_oracle_matches_frozen_scaffold_for_k1_and_k2() -> None:
    derivation = build_p11_external_oracle_matrix_element_derivation()

    assert derivation.external_oracle_status == "EXTERNAL_ORACLE_DERIVED"
    assert derivation.comparison_status == "MATCHES_FROZEN_SCAFFOLD"
    assert derivation.selection_rule_status == "smoke_only"
    assert derivation.audit_result == "external_oracle_matches_frozen_scaffold_without_promotion"
    assert derivation.p9_status == "passed"
    assert derivation.p10_status == "passed"

    for k_max, matched, hermitian_ok, oracle_nonzero, frozen_nonzero in derivation.comparison_by_k:
        assert k_max in {1, 2}
        assert matched is True
        assert hermitian_ok is True
        assert oracle_nonzero == frozen_nonzero


def test_p11_oracle_pattern_is_symbolic_and_frozen_fence_remains() -> None:
    pattern1, states1 = build_external_oracle_selection_pattern(1)
    pattern2, states2 = build_external_oracle_selection_pattern(2)
    comparison1 = compare_to_frozen_v_scaffold(1)
    summary = p11_external_oracle_matrix_element_derivation_summary()

    assert pattern1.shape == (16, 16)
    assert pattern2.shape == (40, 40)
    assert len(states1) == 16
    assert len(states2) == 40
    assert comparison1["pattern_matches"] is True
    assert comparison1["hermitian_compatible"] is True

    assert summary["status"] == "passed"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False

    mapping = {k_max: matched for k_max, matched, *_ in summary["comparison_by_k"]}
    assert mapping[1] is True
    assert mapping[2] is True
    assert summary["comparison_status"] == "MATCHES_FROZEN_SCAFFOLD"
