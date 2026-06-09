"""P10 matrix-element selection-rule review contract.

This module is a terminal review fence for the frozen matrix-element scaffold.
It does not compute a new V operator and does not promote V-selection rules.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

from p9_matrix_element_selection_rules import p9_matrix_element_selection_rules_summary


P10_SELECTION_RULE_MATRIX_ELEMENT_REVIEW_STATUS: Final[str] = "passed"
RUNTIME_STATUS: Final[str] = "research_only"
V_SELECTION_STATUS: Final[str] = "smoke_only"
SAFE_FOR_RUNTIME: Final[bool] = False


@dataclass(frozen=True)
class P10SelectionRuleMatrixElementReview:
    """Terminal review fence for the frozen matrix-element selection-rule audit."""

    p9_status: str
    v_scaffold_shape: Tuple[int, int]
    v_scaffold_hermitian: bool
    v_scaffold_nonzero: bool
    reduced_matrix_element_status: str
    reduced_matrix_element_claim_scope: str
    selection_rule_status: str
    review_result: str
    rule_status_summary: Tuple[Tuple[str, str], ...]
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


def build_p10_selection_rule_matrix_element_review() -> P10SelectionRuleMatrixElementReview:
    """Return the current P10 review contract."""

    p9_summary = p9_matrix_element_selection_rules_summary()
    return P10SelectionRuleMatrixElementReview(
        p9_status=str(p9_summary["status"]),
        v_scaffold_shape=tuple(p9_summary["v_scaffold_shape"]),
        v_scaffold_hermitian=bool(p9_summary["v_scaffold_hermitian"]),
        v_scaffold_nonzero=bool(p9_summary["v_scaffold_nonzero"]),
        reduced_matrix_element_status=str(p9_summary["reduced_matrix_element_status"]),
        reduced_matrix_element_claim_scope=str(p9_summary["reduced_matrix_element_claim_scope"]),
        selection_rule_status=str(p9_summary["v_selection_status"]),
        review_result="selection_rule_matrix_element_review_closed",
        rule_status_summary=tuple(p9_summary["claim_classification"]),
        scope=(
            "P10 selection-rule matrix-element review only; no V promotion, no "
            "fermion-generation claim, no Standard Model claim"
        ),
    )


def p10_selection_rule_matrix_element_review_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and tests."""

    review = build_p10_selection_rule_matrix_element_review()
    return {
        "p9_status": review.p9_status,
        "v_scaffold_shape": review.v_scaffold_shape,
        "v_scaffold_hermitian": review.v_scaffold_hermitian,
        "v_scaffold_nonzero": review.v_scaffold_nonzero,
        "reduced_matrix_element_status": review.reduced_matrix_element_status,
        "reduced_matrix_element_claim_scope": review.reduced_matrix_element_claim_scope,
        "selection_rule_status": review.selection_rule_status,
        "review_result": review.review_result,
        "rule_status_summary": review.rule_status_summary,
        "scope": review.scope,
        "forbidden_claims": review.forbidden_claims,
        "status": P10_SELECTION_RULE_MATRIX_ELEMENT_REVIEW_STATUS,
        "runtime_status": RUNTIME_STATUS,
        "v_selection_status": V_SELECTION_STATUS,
        "safe_for_runtime": SAFE_FOR_RUNTIME,
    }
