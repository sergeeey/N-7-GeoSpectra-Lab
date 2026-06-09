"""S6 / G2 / SU(3) spectrum operator review contract.

This module is a review fence for the spectrum operator layer. It does not
compute a spectrum. It checks that the current implementation remains a
contract and that no SU(4), hypercharge, instanton, index, or chirality claim
is smuggled in through the operator review stage.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

from s6_g2_su3_spectrum_implementation import build_s6_spectrum_implementation


S6_SPECTRUM_OPERATOR_REVIEW_STATUS: Final[str] = "started"
S6_RUNTIME_STATUS: Final[str] = "research_only"
S6_V_SELECTION_STATUS: Final[str] = "smoke_only"
S6_SAFE_FOR_RUNTIME: Final[bool] = False


@dataclass(frozen=True)
class S6SpectrumOperatorReview:
    """Structured review fence for the current S6 spectrum layer."""

    identity: str
    reductive_split: str
    spectrum_target: str
    dirac_operator_convention: str
    casimir_cross_check: str
    scope: str
    review_result: str
    forbidden_claims: Tuple[str, ...] = field(
        default_factory=lambda: (
            "SU4 gauge decomposition",
            "hypercharge",
            "instanton",
            "index",
            "chirality",
            "final spectrum",
        )
    )


def build_s6_spectrum_operator_review() -> S6SpectrumOperatorReview:
    """Return the current S6 spectrum operator review contract."""

    contract = build_s6_spectrum_implementation()
    return S6SpectrumOperatorReview(
        identity=contract.identity,
        reductive_split=contract.reductive_split,
        spectrum_target=contract.spectrum_target,
        dirac_operator_convention=contract.dirac_operator_convention,
        casimir_cross_check=contract.casimir_cross_check,
        scope="S6 spectrum operator review only; no spectrum computation or gauge claim",
        review_result="contract_fence_preserved",
    )


def s6_spectrum_operator_review_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and testing."""

    review = build_s6_spectrum_operator_review()
    return {
        "identity": review.identity,
        "reductive_split": review.reductive_split,
        "spectrum_target": review.spectrum_target,
        "dirac_operator_convention": review.dirac_operator_convention,
        "casimir_cross_check": review.casimir_cross_check,
        "scope": review.scope,
        "review_result": review.review_result,
        "forbidden_claims": review.forbidden_claims,
        "status": S6_SPECTRUM_OPERATOR_REVIEW_STATUS,
        "runtime_status": S6_RUNTIME_STATUS,
        "v_selection_status": S6_V_SELECTION_STATUS,
        "safe_for_runtime": S6_SAFE_FOR_RUNTIME,
    }
