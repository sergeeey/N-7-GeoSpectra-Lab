"""Smoke tests for the P9 matrix-element selection-rule audit."""

from __future__ import annotations

from p9_matrix_element_selection_rules import (
    build_p9_matrix_element_selection_rules,
    p9_matrix_element_selection_rules_summary,
)


def test_p9_matrix_element_audit_keeps_v_scaffold_smoke_only() -> None:
    audit = build_p9_matrix_element_selection_rules()

    assert audit.v_scaffold_shape == (16, 16)
    assert audit.v_scaffold_hermitian is True
    assert audit.v_scaffold_nonzero is True
    assert audit.reduced_matrix_element_status == "ANALYTIC_DIRECT_HAAR_CONVENTION"
    assert audit.reduced_matrix_element_claim_scope == "engineering smoke tests only; no quantitative physics claims"
    assert "no V promotion" in audit.scope or "no V promotion" in audit.scope
    assert audit.selection_rule_status == "smoke_only"
    assert audit.audit_result == "matrix_element_selection_rule_audit_passed_without_promotion"

    assert audit.smoke_only_rules == ("physical V-selection rule",)
    assert audit.requires_physical_input_rules == (
        "full fermion generation claim",
        "Standard Model reproduced claim",
    )


def test_p9_summary_classifies_selection_rules_and_preserves_fence() -> None:
    summary = p9_matrix_element_selection_rules_summary()

    assert summary["status"] == "passed"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False
    assert summary["p8_bridge_result"] == "tensor_product_ordering_review_passed"
    assert summary["s6_selection_review_result"] == "selection_rule_classes_reviewed_without_promotion"
    assert summary["su4_audit_result"].startswith("su4_algebra_audit_passed")

    mapping = dict(summary["claim_classification"])
    assert mapping["v_scaffold_shape"] == "tensor_product_derived"
    assert mapping["v_scaffold_hermiticity"] == "tensor_product_derived"
    assert mapping["working reduced matrix elements"] == "normalization_dependent"
    assert mapping["S3 Cartan weights"] == "tensor_product_derived"
    assert mapping["P8 tensor-product bridge"] == "tensor_product_derived"
    assert mapping["S6 selection review"] == "tensor_product_derived"
    assert mapping["SU4 audit"] == "tensor_product_derived"
    assert mapping["final Ben Achour E/E' basis mapping"] == "normalization_dependent"
    assert mapping["physical V-selection rule"] == "smoke_only"
    assert mapping["full fermion generation claim"] == "requires_physical_input"
    assert mapping["Standard Model reproduced claim"] == "requires_physical_input"
    assert mapping["failed matrix-element claim"] == "failed"
