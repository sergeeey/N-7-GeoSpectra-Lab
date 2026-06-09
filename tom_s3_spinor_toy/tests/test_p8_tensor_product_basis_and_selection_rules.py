"""Smoke tests for the P8 tensor-product bridge contract."""

from __future__ import annotations

from p8_s3_s6_su4_tensor_product_basis_and_selection_rules import (
    build_p8_tensor_product_bridge,
    p8_tensor_product_bridge_summary,
)


def test_p8_bridge_classifies_tensor_product_and_fences() -> None:
    bridge = build_p8_tensor_product_bridge()

    assert bridge.s3_basis_order == "plus_plus, plus_minus, minus_plus, minus_minus"
    assert bridge.s6_spectrum_order.startswith("k ascending; sign (+,-)")
    assert bridge.bridge_result == "tensor_product_ordering_review_passed"
    assert bridge.selection_rule_status == "smoke_only"
    assert "no fermion-generation" in bridge.scope
    assert "no V promotion" in bridge.scope

    assert bridge.tensor_product_derived_rules == (
        "s3_spinor_basis_order",
        "s6_spectrum_level_order",
        "tensor_product_label_order",
    )
    assert bridge.basis_ordering_dependent_rules == (
        "su4_generator_order",
        "su3c_embedding_labels",
    )
    assert bridge.normalization_dependent_rules == (
        "lambda_15_normalization",
        "candidate_Y_W",
    )
    assert bridge.requires_physical_input_rules == (
        "full fermion generation claim",
        "Standard Model reproduced claim",
    )
    assert bridge.smoke_only_rules == ("physical V-selection rule",)


def test_p8_bridge_summary_preserves_research_only_and_smoke_only() -> None:
    summary = p8_tensor_product_bridge_summary()

    assert summary["status"] == "passed"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False
    assert summary["bridge_order"].startswith("S3 basis × S6 labels × SU4 labels")

    mapping = dict(summary["claim_classification"])
    assert mapping["s3_spinor_basis_order"] == "tensor_product_derived"
    assert mapping["s6_spectrum_level_order"] == "tensor_product_derived"
    assert mapping["tensor_product_label_order"] == "tensor_product_derived"
    assert mapping["su4_generator_order"] == "basis_ordering_dependent"
    assert mapping["su3c_embedding_labels"] == "basis_ordering_dependent"
    assert mapping["lambda_15_normalization"] == "normalization_dependent"
    assert mapping["candidate_Y_W"] == "normalization_dependent"
    assert mapping["full fermion generation claim"] == "requires_physical_input"
    assert mapping["Standard Model reproduced claim"] == "requires_physical_input"
    assert mapping["physical V-selection rule"] == "smoke_only"
    assert mapping["failed bridge claim"] == "failed"
