"""S6 / G2 / SU(3) spectrum operator final review contract.

This module is the terminal review fence for the current S6 operator chain.
It does not compute a spectrum and does not widen scope beyond the freeze.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

from s6_g2_su3_spectrum_operator_freeze import build_s6_spectrum_operator_freeze


S6_SPECTRUM_OPERATOR_FINAL_REVIEW_STATUS: Final[str] = "passed"
S6_RUNTIME_STATUS: Final[str] = "research_only"
S6_V_SELECTION_STATUS: Final[str] = "smoke_only"
S6_SAFE_FOR_RUNTIME: Final[bool] = False


@dataclass(frozen=True)
class S6SpectrumOperatorFinalReview:
    """Terminal review fence for the current S6 spectrum operator."""

    identity: str
    reductive_split: str
    spectrum_target: str
    dirac_operator_convention: str
    casimir_cross_check: str
    freeze_result: str
    review_result: str
    final_review_result: str
    scope: str
    forbidden_claims: Tuple[str, ...] = field(
        default_factory=lambda: (
            "SU4 gauge decomposition",
            "hypercharge",
            "instanton",
            "index",
            "chirality",
            "final spectrum",
            "runtime safe promotion",
        )
    )


def build_s6_spectrum_operator_final_review() -> S6SpectrumOperatorFinalReview:
    """Return the current S6 spectrum operator final review contract."""

    freeze = build_s6_spectrum_operator_freeze()
    return S6SpectrumOperatorFinalReview(
        identity=freeze.identity,
        reductive_split=freeze.reductive_split,
        spectrum_target=freeze.spectrum_target,
        dirac_operator_convention=freeze.dirac_operator_convention,
        casimir_cross_check=freeze.casimir_cross_check,
        freeze_result=freeze.freeze_result,
        review_result="contract_fence_reviewed",
        final_review_result="contract_fence_final_review_complete",
        scope="S6 spectrum operator final review only; no spectrum computation or gauge claim",
        forbidden_claims=(
            "SU4 gauge decomposition",
            "hypercharge",
            "instanton",
            "index",
            "chirality",
            "final spectrum",
            "runtime safe promotion",
        ),
    )


def s6_spectrum_operator_final_review_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and testing."""

    review = build_s6_spectrum_operator_final_review()
    return {
        "identity": review.identity,
        "reductive_split": review.reductive_split,
        "spectrum_target": review.spectrum_target,
        "dirac_operator_convention": review.dirac_operator_convention,
        "casimir_cross_check": review.casimir_cross_check,
        "freeze_result": review.freeze_result,
        "review_result": review.review_result,
        "final_review_result": review.final_review_result,
        "scope": review.scope,
        "forbidden_claims": review.forbidden_claims,
        "status": S6_SPECTRUM_OPERATOR_FINAL_REVIEW_STATUS,
        "runtime_status": S6_RUNTIME_STATUS,
        "v_selection_status": S6_V_SELECTION_STATUS,
        "safe_for_runtime": S6_SAFE_FOR_RUNTIME,
    }
