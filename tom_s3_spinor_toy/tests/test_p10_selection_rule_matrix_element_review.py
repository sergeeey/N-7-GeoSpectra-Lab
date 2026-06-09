"""Smoke tests for the P10 selection-rule matrix-element review contract."""

from __future__ import annotations

from p10_selection_rule_matrix_element_review import (
    build_p10_selection_rule_matrix_element_review,
    p10_selection_rule_matrix_element_review_summary,
)


def test_p10_review_keeps_the_matrix_element_scaffold_frozen() -> None:
    review = build_p10_selection_rule_matrix_element_review()

    assert review.p9_status == "passed"
    assert review.v_scaffold_shape == (16, 16)
    assert review.v_scaffold_hermitian is True
    assert review.v_scaffold_nonzero is True
    assert review.reduced_matrix_element_status == "ANALYTIC_DIRECT_HAAR_CONVENTION"
    assert review.selection_rule_status == "smoke_only"
    assert review.review_result == "selection_rule_matrix_element_review_closed"
    assert "no V promotion" in review.scope


def test_p10_summary_preserves_the_fence_and_classification() -> None:
    summary = p10_selection_rule_matrix_element_review_summary()

    assert summary["status"] == "passed"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False
    assert summary["p9_status"] == "passed"
    assert summary["selection_rule_status"] == "smoke_only"

    mapping = dict(summary["rule_status_summary"])
    assert mapping["v_scaffold_shape"] == "tensor_product_derived"
    assert mapping["v_scaffold_hermiticity"] == "tensor_product_derived"
    assert mapping["working reduced matrix elements"] == "normalization_dependent"
    assert mapping["physical V-selection rule"] == "smoke_only"
    assert mapping["full fermion generation claim"] == "requires_physical_input"
    assert mapping["Standard Model reproduced claim"] == "requires_physical_input"
