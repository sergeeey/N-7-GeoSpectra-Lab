"""S6 / G2 / SU(3) selection-rule review contract.

This module is a review fence for the already-computed round-S6 spectrum.
It does not recompute the spectrum, does not widen scope to SU(4) or
hypercharge, and only classifies which selection-rule classes are derivable
from the current S6 contract stack.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

from s6_g2_su3_spectrum_result_review import s6_spectrum_result_review_summary


S6_SELECTION_RULE_REVIEW_STATUS: Final[str] = "passed"
S6_RUNTIME_STATUS: Final[str] = "research_only"
S6_V_SELECTION_STATUS: Final[str] = "smoke_only"
S6_SAFE_FOR_RUNTIME: Final[bool] = False

S6_SPECTRUM_DERIVED: Final[str] = "S6_SPECTRUM_DERIVED"
CASIMIR_DERIVED: Final[str] = "CASIMIR_DERIVED"
REPRESENTATION_CANDIDATE: Final[str] = "REPRESENTATION_CANDIDATE"
REQUIRES_SU4_HYPERCHARGE: Final[str] = "REQUIRES_SU4_HYPERCHARGE"
REQUIRES_TENSOR_PRODUCT_S3XS6: Final[str] = "REQUIRES_TENSOR_PRODUCT_S3xS6"
SMOKE_ONLY: Final[str] = "SMOKE_ONLY"


@dataclass(frozen=True)
class S6SelectionRuleReview:
    """Structured review fence for S6 selection-rule classification."""

    identity: str
    reductive_split: str
    metric_normalization: str
    connection_choice: str
    spinor_bundle_convention: str
    dirac_operator_convention: str
    casimir_cross_check: str
    spectrum_formula: str
    multiplicity_formula: str
    spectrum_result_status: str
    spectrum_result_review_status: str
    spectrum_derived_rules: Tuple[str, ...]
    casimir_derived_rules: Tuple[str, ...]
    representation_candidate_rules: Tuple[str, ...]
    requires_su4_hypercharge_rules: Tuple[str, ...]
    requires_tensor_product_s3xs6_rules: Tuple[str, ...]
    smoke_only_rules: Tuple[str, ...]
    selection_rule_status: str
    review_result: str
    scope: str
    forbidden_claims: Tuple[str, ...] = field(
        default_factory=lambda: (
            "SU4 gauge decomposition",
            "hypercharge",
            "instanton",
            "index",
            "chirality",
            "runtime safe promotion",
            "physical V-operator claim",
        )
    )

    @property
    def rule_classification(self) -> Tuple[Tuple[str, str], ...]:
        """Return the flat rule -> class mapping for reporting and tests."""

        return (
            ("round_s6_dirac_spacing_rule", S6_SPECTRUM_DERIVED),
            ("round_s6_multiplicity_rule", S6_SPECTRUM_DERIVED),
            ("casimir_cross_check_rule", CASIMIR_DERIVED),
            ("g2_su3_representation_labels", REPRESENTATION_CANDIDATE),
            ("su4_hypercharge_mapping", REQUIRES_SU4_HYPERCHARGE),
            ("s3xs6_tensor_product_coupling", REQUIRES_TENSOR_PRODUCT_S3XS6),
            ("physical_v_selection_rule", SMOKE_ONLY),
        )


def build_s6_selection_rule_review() -> S6SelectionRuleReview:
    """Return the current S6 selection-rule review contract."""

    spectrum_review = s6_spectrum_result_review_summary()
    return S6SelectionRuleReview(
        identity=str(spectrum_review["identity"]),
        reductive_split=str(spectrum_review["reductive_split"]),
        metric_normalization=str(spectrum_review["metric_normalization"]),
        connection_choice=str(spectrum_review["connection_choice"]),
        spinor_bundle_convention=str(spectrum_review["spinor_bundle_convention"]),
        dirac_operator_convention=str(spectrum_review["dirac_operator_convention"]),
        casimir_cross_check=str(spectrum_review["casimir_cross_check"]),
        spectrum_formula=str(spectrum_review["spectrum_formula"]),
        multiplicity_formula=str(spectrum_review["multiplicity_formula"]),
        spectrum_result_status=str(spectrum_review["status"]),
        spectrum_result_review_status="passed",
        spectrum_derived_rules=(
            "round_s6_dirac_spacing_rule",
            "round_s6_multiplicity_rule",
        ),
        casimir_derived_rules=("casimir_cross_check_rule",),
        representation_candidate_rules=("g2_su3_representation_labels",),
        requires_su4_hypercharge_rules=("su4_hypercharge_mapping",),
        requires_tensor_product_s3xs6_rules=("s3xs6_tensor_product_coupling",),
        smoke_only_rules=("physical_v_selection_rule",),
        selection_rule_status="smoke_only",
        review_result="selection_rule_classes_reviewed_without_promotion",
        scope="S6 selection-rule review only; no new spectrum computation or gauge claim",
    )


def s6_selection_rule_review_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and tests."""

    review = build_s6_selection_rule_review()
    return {
        "identity": review.identity,
        "reductive_split": review.reductive_split,
        "metric_normalization": review.metric_normalization,
        "connection_choice": review.connection_choice,
        "spinor_bundle_convention": review.spinor_bundle_convention,
        "dirac_operator_convention": review.dirac_operator_convention,
        "casimir_cross_check": review.casimir_cross_check,
        "spectrum_formula": review.spectrum_formula,
        "multiplicity_formula": review.multiplicity_formula,
        "spectrum_result_status": review.spectrum_result_status,
        "spectrum_result_review_status": review.spectrum_result_review_status,
        "rule_classification": review.rule_classification,
        "spectrum_derived_rules": review.spectrum_derived_rules,
        "casimir_derived_rules": review.casimir_derived_rules,
        "representation_candidate_rules": review.representation_candidate_rules,
        "requires_su4_hypercharge_rules": review.requires_su4_hypercharge_rules,
        "requires_tensor_product_s3xs6_rules": review.requires_tensor_product_s3xs6_rules,
        "smoke_only_rules": review.smoke_only_rules,
        "selection_rule_status": review.selection_rule_status,
        "review_result": review.review_result,
        "scope": review.scope,
        "forbidden_claims": review.forbidden_claims,
        "status": S6_SELECTION_RULE_REVIEW_STATUS,
        "runtime_status": S6_RUNTIME_STATUS,
        "v_selection_status": S6_V_SELECTION_STATUS,
        "safe_for_runtime": S6_SAFE_FOR_RUNTIME,
    }
