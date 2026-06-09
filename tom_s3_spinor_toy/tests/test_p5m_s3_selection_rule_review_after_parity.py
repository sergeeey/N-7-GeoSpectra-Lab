"""Smoke tests for the S3 selection-rule review after parity formalization."""

from __future__ import annotations

from s3_selection_rule_review_after_parity import (
    build_s3_selection_rule_review_after_parity,
    s3_selection_rule_review_after_parity_summary,
)


def test_selection_rule_review_after_parity_preserves_smoke_only_fence() -> None:
    """The review layer must keep V-selection rules at smoke_only."""

    review = build_s3_selection_rule_review_after_parity()

    assert review.v_scaffold_hermitian is True
    assert review.v_scaffold_nonzero is True
    assert review.reduced_matrix_element_status == "ANALYTIC_DIRECT_HAAR_CONVENTION"
    assert review.reduced_matrix_element_claim_scope == "engineering smoke tests only; no quantitative physics claims"
    assert review.parity_formalization_status == "started"
    assert review.parity_candidate_p1_status == "inconclusive"
    assert review.parity_candidate_p2_status == "passed"
    assert review.selection_rule_status == "smoke_only"
    assert review.review_result == "smoke_only_preserved"
    assert "review after parity formalization" in review.scope


def test_selection_rule_review_after_parity_summary_records_fence() -> None:
    """The summary should expose the smoke-only fence and all review markers."""

    summary = s3_selection_rule_review_after_parity_summary()

    assert summary["status"] == "passed"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False
    assert summary["v_scaffold_hermitian"] is True
    assert summary["v_scaffold_nonzero"] is True
    assert summary["parity_formalization_status"] == "started"
    assert summary["parity_candidate_p1_status"] == "inconclusive"
    assert summary["parity_candidate_p2_status"] == "passed"
    assert summary["selection_rule_status"] == "smoke_only"
    assert summary["review_result"] == "smoke_only_preserved"

    forbidden_claims = set(summary["forbidden_claims"])
    assert "S6 spectrum claims" in forbidden_claims
    assert "SU4 gauge decomposition" in forbidden_claims
    assert "hypercharge" in forbidden_claims
    assert "physical V-operator claim" in forbidden_claims
