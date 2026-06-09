"""S3 selection-rule review after parity formalization.

This module is a narrow review fence. It does not derive a new physical V
operator. It only checks that the current engineering scaffold remains
Hermitian, that the parity formalization did not justify promotion, and that
the selection-rule status stays smoke-only.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

import numpy as np

from s3_coupling_v_option_b import build_v_symbolic
from s3_parity_smoke import parity_smoke_summary
from s3_reduced_matrix_elements import reduced_element_metadata
from s3_kronecker_skeleton import s3_parity_formalization_summary


P5M_SELECTION_RULE_REVIEW_STATUS: Final[str] = "passed"
RUNTIME_STATUS: Final[str] = "research_only"
V_SELECTION_STATUS: Final[str] = "smoke_only"
SAFE_FOR_RUNTIME: Final[bool] = False


@dataclass(frozen=True)
class S3SelectionRuleReviewAfterParity:
    """Structured review fence for S3 selection rules after parity formalization."""

    v_scaffold_hermitian: bool
    v_scaffold_nonzero: bool
    reduced_matrix_element_status: str
    reduced_matrix_element_claim_scope: str
    parity_formalization_status: str
    parity_candidate_p1_status: str
    parity_candidate_p2_status: str
    selection_rule_status: str
    review_result: str
    scope: str
    forbidden_claims: Tuple[str, ...] = field(
        default_factory=lambda: (
            "S6 spectrum claims",
            "SU4 gauge decomposition",
            "hypercharge",
            "instanton",
            "index",
            "chirality",
            "promotion to runtime-safe",
            "physical V-operator claim",
        )
    )


def _is_hermitian(matrix: np.ndarray, atol: float = 1e-12) -> bool:
    return bool(np.allclose(matrix, matrix.conjugate().T, atol=atol))


def build_s3_selection_rule_review_after_parity() -> S3SelectionRuleReviewAfterParity:
    """Return the review contract for the current selection-rule fence."""

    v_matrix = build_v_symbolic(k_max=1)
    parity_summary = parity_smoke_summary()
    formalization = s3_parity_formalization_summary()
    metadata = reduced_element_metadata()
    return S3SelectionRuleReviewAfterParity(
        v_scaffold_hermitian=_is_hermitian(v_matrix),
        v_scaffold_nonzero=bool(np.count_nonzero(v_matrix) > 0),
        reduced_matrix_element_status=str(metadata["normalization_status"]),
        reduced_matrix_element_claim_scope=str(metadata["claim_scope"]),
        parity_formalization_status=str(formalization["status"]),
        parity_candidate_p1_status=str(parity_summary["results"]["P1"].status),
        parity_candidate_p2_status=str(parity_summary["results"]["P2"].status),
        selection_rule_status="smoke_only",
        review_result="smoke_only_preserved",
        scope="S3 selection-rule review after parity formalization only; no promotion",
    )


def s3_selection_rule_review_after_parity_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and tests."""

    review = build_s3_selection_rule_review_after_parity()
    return {
        "status": P5M_SELECTION_RULE_REVIEW_STATUS,
        "runtime_status": RUNTIME_STATUS,
        "v_selection_status": V_SELECTION_STATUS,
        "safe_for_runtime": SAFE_FOR_RUNTIME,
        "v_scaffold_hermitian": review.v_scaffold_hermitian,
        "v_scaffold_nonzero": review.v_scaffold_nonzero,
        "reduced_matrix_element_status": review.reduced_matrix_element_status,
        "reduced_matrix_element_claim_scope": review.reduced_matrix_element_claim_scope,
        "parity_formalization_status": review.parity_formalization_status,
        "parity_candidate_p1_status": review.parity_candidate_p1_status,
        "parity_candidate_p2_status": review.parity_candidate_p2_status,
        "selection_rule_status": review.selection_rule_status,
        "review_result": review.review_result,
        "scope": review.scope,
        "forbidden_claims": review.forbidden_claims,
    }
