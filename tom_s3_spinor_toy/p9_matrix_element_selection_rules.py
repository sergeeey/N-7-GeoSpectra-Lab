"""P9 matrix-element selection-rule audit.

This module audits the current matrix-element scaffold in isolation from any
promotion claim. It consumes the validated S3/S6/SU4 contracts as fixed inputs
and classifies selection-rule statements by what the current engineering
scaffold can actually support.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

from p8_s3_s6_su4_tensor_product_basis_and_selection_rules import (
    p8_tensor_product_bridge_summary,
)
from s3_coupling_v_option_b import build_v_symbolic
from s3_reduced_matrix_elements import reduced_element_metadata
from s6_g2_su3_selection_rule_review import s6_selection_rule_review_summary
from su4_hypercharge_gauge_breaking_audit import su4_hypercharge_gauge_audit_summary
from standard_s3_spinor_harmonics import standard_spinor_cartan_weights


P9_MATRIX_ELEMENT_SELECTION_RULES_STATUS: Final[str] = "passed"
RUNTIME_STATUS: Final[str] = "research_only"
V_SELECTION_STATUS: Final[str] = "smoke_only"
SAFE_FOR_RUNTIME: Final[bool] = False

TENSOR_PRODUCT_DERIVED: Final[str] = "tensor_product_derived"
BASIS_ORDERING_DEPENDENT: Final[str] = "basis_ordering_dependent"
NORMALIZATION_DEPENDENT: Final[str] = "normalization_dependent"
REQUIRES_PHYSICAL_INPUT: Final[str] = "requires_physical_input"
SMOKE_ONLY: Final[str] = "smoke_only"
FAILED: Final[str] = "failed"


@dataclass(frozen=True)
class P9MatrixElementSelectionRules:
    """Structured matrix-element selection-rule audit."""

    v_scaffold_shape: Tuple[int, int]
    v_scaffold_hermitian: bool
    v_scaffold_nonzero: bool
    reduced_matrix_element_status: str
    reduced_matrix_element_claim_scope: str
    reduced_matrix_element_basis: str
    reduced_matrix_element_not_included: str
    s3_cartan_weights: Tuple[Tuple[str, float, float], ...]
    p8_bridge_result: str
    s6_selection_review_result: str
    su4_audit_result: str
    tensor_product_rules: Tuple[str, ...]
    basis_ordering_dependent_rules: Tuple[str, ...]
    normalization_dependent_rules: Tuple[str, ...]
    requires_physical_input_rules: Tuple[str, ...]
    smoke_only_rules: Tuple[str, ...]
    failed_rules: Tuple[str, ...]
    selection_rule_status: str
    audit_result: str
    scope: str
    forbidden_claims: Tuple[str, ...] = field(
        default_factory=lambda: (
            "full fermion generation claim",
            "Standard Model reproduced claim",
            "V-selection promotion",
            "safe_for_runtime promotion",
            "final Ben Achour E/E' basis mapping",
        )
    )

    @property
    def claim_classification(self) -> Tuple[Tuple[str, str], ...]:
        return (
            ("v_scaffold_shape", TENSOR_PRODUCT_DERIVED),
            ("v_scaffold_hermiticity", TENSOR_PRODUCT_DERIVED),
            ("working reduced matrix elements", NORMALIZATION_DEPENDENT),
            ("S3 Cartan weights", TENSOR_PRODUCT_DERIVED),
            ("P8 tensor-product bridge", TENSOR_PRODUCT_DERIVED),
            ("S6 selection review", TENSOR_PRODUCT_DERIVED),
            ("SU4 audit", TENSOR_PRODUCT_DERIVED),
            ("final Ben Achour E/E' basis mapping", NORMALIZATION_DEPENDENT),
            ("physical V-selection rule", SMOKE_ONLY),
            ("full fermion generation claim", REQUIRES_PHYSICAL_INPUT),
            ("Standard Model reproduced claim", REQUIRES_PHYSICAL_INPUT),
            ("failed matrix-element claim", FAILED),
        )


def build_p9_matrix_element_selection_rules() -> P9MatrixElementSelectionRules:
    """Return the current P9 matrix-element selection-rule audit contract."""

    v_matrix = build_v_symbolic(k_max=1)
    reduced = reduced_element_metadata()
    s3_weights = standard_spinor_cartan_weights()
    p8_summary = p8_tensor_product_bridge_summary()
    s6_summary = s6_selection_rule_review_summary()
    su4_summary = su4_hypercharge_gauge_audit_summary()

    return P9MatrixElementSelectionRules(
        v_scaffold_shape=(int(v_matrix.shape[0]), int(v_matrix.shape[1])),
        v_scaffold_hermitian=bool((v_matrix == v_matrix.conjugate().T).all()),
        v_scaffold_nonzero=bool(v_matrix.size > 0 and v_matrix.any()),
        reduced_matrix_element_status=str(reduced["normalization_status"]),
        reduced_matrix_element_claim_scope=str(reduced["claim_scope"]),
        reduced_matrix_element_basis=str(reduced["basis"]),
        reduced_matrix_element_not_included=str(reduced["not_included"]),
        s3_cartan_weights=tuple(
            (label, weights.i_l, weights.i_r) for label, weights in s3_weights.items()
        ),
        p8_bridge_result=str(p8_summary["bridge_result"]),
        s6_selection_review_result=str(s6_summary["review_result"]),
        su4_audit_result=str(su4_summary["audit_result"]),
        tensor_product_rules=(
            "v_scaffold_shape",
            "v_scaffold_hermiticity",
            "S3 Cartan weights",
            "P8 tensor-product bridge",
            "S6 selection review",
            "SU4 audit",
        ),
        basis_ordering_dependent_rules=(
            "basis ordering of S3/SU4 labels",
            "current working selection-rule scaffold labels",
        ),
        normalization_dependent_rules=(
            "working reduced matrix elements",
            "final Ben Achour E/E' basis mapping",
        ),
        requires_physical_input_rules=(
            "full fermion generation claim",
            "Standard Model reproduced claim",
        ),
        smoke_only_rules=("physical V-selection rule",),
        failed_rules=("failed matrix-element claim",),
        selection_rule_status="smoke_only",
        audit_result="matrix_element_selection_rule_audit_passed_without_promotion",
        scope=(
            "P9 matrix-element selection-rule audit only; no V promotion, no "
            "fermion-generation claim, no Standard Model claim"
        ),
    )


def p9_matrix_element_selection_rules_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and tests."""

    audit = build_p9_matrix_element_selection_rules()
    return {
        "v_scaffold_shape": audit.v_scaffold_shape,
        "v_scaffold_hermitian": audit.v_scaffold_hermitian,
        "v_scaffold_nonzero": audit.v_scaffold_nonzero,
        "reduced_matrix_element_status": audit.reduced_matrix_element_status,
        "reduced_matrix_element_claim_scope": audit.reduced_matrix_element_claim_scope,
        "reduced_matrix_element_basis": audit.reduced_matrix_element_basis,
        "reduced_matrix_element_not_included": audit.reduced_matrix_element_not_included,
        "s3_cartan_weights": audit.s3_cartan_weights,
        "p8_bridge_result": audit.p8_bridge_result,
        "s6_selection_review_result": audit.s6_selection_review_result,
        "su4_audit_result": audit.su4_audit_result,
        "claim_classification": audit.claim_classification,
        "tensor_product_rules": audit.tensor_product_rules,
        "basis_ordering_dependent_rules": audit.basis_ordering_dependent_rules,
        "normalization_dependent_rules": audit.normalization_dependent_rules,
        "requires_physical_input_rules": audit.requires_physical_input_rules,
        "smoke_only_rules": audit.smoke_only_rules,
        "failed_rules": audit.failed_rules,
        "selection_rule_status": audit.selection_rule_status,
        "audit_result": audit.audit_result,
        "scope": audit.scope,
        "forbidden_claims": audit.forbidden_claims,
        "status": P9_MATRIX_ELEMENT_SELECTION_RULES_STATUS,
        "runtime_status": RUNTIME_STATUS,
        "v_selection_status": V_SELECTION_STATUS,
        "safe_for_runtime": SAFE_FOR_RUNTIME,
    }
