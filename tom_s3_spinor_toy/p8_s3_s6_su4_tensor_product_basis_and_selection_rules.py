"""P8 tensor-product basis and selection-rule bridge.

This module is a strict bridge layer between the validated S3 spinor scaffold,
the frozen S6 spectrum labels, and the audited SU(4) / SU(3)c gauge metadata.
It does not derive physical fermion generations, does not claim Standard Model
reproduction, and does not promote V-selection rules.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

from standard_s3_spinor_harmonics import standard_spinor_cartan_weights
from s6_g2_su3_spectrum_result_review import s6_spectrum_result_review_summary
from su4_hypercharge_gauge_breaking_audit import su4_hypercharge_gauge_audit_summary


P8_TENSOR_PRODUCT_BASIS_AND_SELECTION_RULES_STATUS: Final[str] = "passed"
RUNTIME_STATUS: Final[str] = "research_only"
V_SELECTION_STATUS: Final[str] = "smoke_only"
SAFE_FOR_RUNTIME: Final[bool] = False


@dataclass(frozen=True)
class P8TensorProductBridge:
    """Structured bridge between S3 basis, S6 labels, and SU4 metadata."""

    s3_basis_order: str
    s3_cartan_weights: Tuple[Tuple[str, float, float], ...]
    s6_spectrum_order: str
    s6_spectrum_formula: str
    s6_multiplicity_formula: str
    su4_basis_order: str
    su4_lambda_15_normalization: str
    su4_candidate_yw: str
    bridge_order: str
    tensor_product_derived_rules: Tuple[str, ...]
    basis_ordering_dependent_rules: Tuple[str, ...]
    normalization_dependent_rules: Tuple[str, ...]
    requires_physical_input_rules: Tuple[str, ...]
    smoke_only_rules: Tuple[str, ...]
    failed_rules: Tuple[str, ...]
    selection_rule_status: str
    bridge_result: str
    scope: str
    forbidden_claims: Tuple[str, ...] = field(
        default_factory=lambda: (
            "full fermion generation claim",
            "Standard Model reproduced claim",
            "V-selection promotion",
            "safe_for_runtime promotion",
            "S3xS6 tensor-product coupling physical claim",
        )
    )

    @property
    def claim_classification(self) -> Tuple[Tuple[str, str], ...]:
        return (
            ("s3_spinor_basis_order", "tensor_product_derived"),
            ("s6_spectrum_level_order", "tensor_product_derived"),
            ("tensor_product_label_order", "tensor_product_derived"),
            ("su4_generator_order", "basis_ordering_dependent"),
            ("su3c_embedding_labels", "basis_ordering_dependent"),
            ("lambda_15_normalization", "normalization_dependent"),
            ("candidate_Y_W", "normalization_dependent"),
            ("full fermion generation claim", "requires_physical_input"),
            ("Standard Model reproduced claim", "requires_physical_input"),
            ("physical V-selection rule", "smoke_only"),
            ("failed bridge claim", "failed"),
        )


def build_p8_tensor_product_bridge() -> P8TensorProductBridge:
    """Return the current P8 tensor-product bridge contract."""

    s3_weights = standard_spinor_cartan_weights()
    s6_summary = s6_spectrum_result_review_summary()
    su4_summary = su4_hypercharge_gauge_audit_summary()
    return P8TensorProductBridge(
        s3_basis_order="plus_plus, plus_minus, minus_plus, minus_minus",
        s3_cartan_weights=tuple(
            (label, weights.i_l, weights.i_r)
            for label, weights in s3_weights.items()
        ),
        s6_spectrum_order="k ascending; sign (+,-); multiplicity per signed level",
        s6_spectrum_formula=str(s6_summary["spectrum_formula"]),
        s6_multiplicity_formula=str(s6_summary["multiplicity_formula"]),
        su4_basis_order=str(su4_summary["basis_ordering"]),
        su4_lambda_15_normalization=str(su4_summary["lambda_15_normalization"]),
        su4_candidate_yw=str(su4_summary["candidate_yw"]),
        bridge_order="S3 basis × S6 labels × SU4 labels, lexicographic tensor order",
        tensor_product_derived_rules=(
            "s3_spinor_basis_order",
            "s6_spectrum_level_order",
            "tensor_product_label_order",
        ),
        basis_ordering_dependent_rules=(
            "su4_generator_order",
            "su3c_embedding_labels",
        ),
        normalization_dependent_rules=(
            "lambda_15_normalization",
            "candidate_Y_W",
        ),
        requires_physical_input_rules=(
            "full fermion generation claim",
            "Standard Model reproduced claim",
        ),
        smoke_only_rules=("physical V-selection rule",),
        failed_rules=("failed bridge claim",),
        selection_rule_status="smoke_only",
        bridge_result="tensor_product_ordering_review_passed",
        scope=(
            "P8 tensor-product basis/order bridge only; no fermion-generation or "
            "Standard Model claim; no V promotion"
        ),
    )


def p8_tensor_product_bridge_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and tests."""

    bridge = build_p8_tensor_product_bridge()
    return {
        "s3_basis_order": bridge.s3_basis_order,
        "s3_cartan_weights": bridge.s3_cartan_weights,
        "s6_spectrum_order": bridge.s6_spectrum_order,
        "s6_spectrum_formula": bridge.s6_spectrum_formula,
        "s6_multiplicity_formula": bridge.s6_multiplicity_formula,
        "su4_basis_order": bridge.su4_basis_order,
        "su4_lambda_15_normalization": bridge.su4_lambda_15_normalization,
        "su4_candidate_yw": bridge.su4_candidate_yw,
        "bridge_order": bridge.bridge_order,
        "claim_classification": bridge.claim_classification,
        "tensor_product_derived_rules": bridge.tensor_product_derived_rules,
        "basis_ordering_dependent_rules": bridge.basis_ordering_dependent_rules,
        "normalization_dependent_rules": bridge.normalization_dependent_rules,
        "requires_physical_input_rules": bridge.requires_physical_input_rules,
        "smoke_only_rules": bridge.smoke_only_rules,
        "failed_rules": bridge.failed_rules,
        "selection_rule_status": bridge.selection_rule_status,
        "bridge_result": bridge.bridge_result,
        "scope": bridge.scope,
        "forbidden_claims": bridge.forbidden_claims,
        "status": P8_TENSOR_PRODUCT_BASIS_AND_SELECTION_RULES_STATUS,
        "runtime_status": RUNTIME_STATUS,
        "v_selection_status": V_SELECTION_STATUS,
        "safe_for_runtime": SAFE_FOR_RUNTIME,
    }
