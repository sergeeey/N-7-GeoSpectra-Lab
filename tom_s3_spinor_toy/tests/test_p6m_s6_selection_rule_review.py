"""Smoke tests for the S6 selection-rule review contract."""

from __future__ import annotations

from s6_g2_su3_selection_rule_review import (
    build_s6_selection_rule_review,
    s6_selection_rule_review_summary,
)


def test_s6_selection_rule_review_classifies_rules_without_promotion() -> None:
    review = build_s6_selection_rule_review()

    assert review.identity == "S6 ≅ G2 / SU(3)"
    assert review.spectrum_result_status == "passed"
    assert review.spectrum_result_review_status == "passed"
    assert review.selection_rule_status == "smoke_only"
    assert review.review_result == "selection_rule_classes_reviewed_without_promotion"

    assert review.spectrum_derived_rules == (
        "round_s6_dirac_spacing_rule",
        "round_s6_multiplicity_rule",
    )
    assert review.casimir_derived_rules == ("casimir_cross_check_rule",)
    assert review.representation_candidate_rules == ("g2_su3_representation_labels",)
    assert review.requires_su4_hypercharge_rules == ("su4_hypercharge_mapping",)
    assert review.requires_tensor_product_s3xs6_rules == ("s3xs6_tensor_product_coupling",)
    assert review.smoke_only_rules == ("physical_v_selection_rule",)


def test_s6_selection_rule_review_summary_keeps_fences_intact() -> None:
    summary = s6_selection_rule_review_summary()

    assert summary["status"] == "passed"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False

    mapping = dict(summary["rule_classification"])
    assert mapping["round_s6_dirac_spacing_rule"] == "S6_SPECTRUM_DERIVED"
    assert mapping["round_s6_multiplicity_rule"] == "S6_SPECTRUM_DERIVED"
    assert mapping["casimir_cross_check_rule"] == "CASIMIR_DERIVED"
    assert mapping["g2_su3_representation_labels"] == "REPRESENTATION_CANDIDATE"
    assert mapping["su4_hypercharge_mapping"] == "REQUIRES_SU4_HYPERCHARGE"
    assert mapping["s3xs6_tensor_product_coupling"] == "REQUIRES_TENSOR_PRODUCT_S3xS6"
    assert mapping["physical_v_selection_rule"] == "SMOKE_ONLY"
