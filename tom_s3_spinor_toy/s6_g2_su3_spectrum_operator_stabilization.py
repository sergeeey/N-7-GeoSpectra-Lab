"""S6 / G2 / SU(3) spectrum operator stabilization contract.

This module is the next executable fence after the operator review. It does
not compute a spectrum. It only stabilizes the operator contract so the S6
track cannot drift into premature spectrum, SU(4), or hypercharge claims.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

from s6_g2_su3_spectrum_operator_review import build_s6_spectrum_operator_review


S6_SPECTRUM_OPERATOR_STABILIZATION_STATUS: Final[str] = "started"
S6_RUNTIME_STATUS: Final[str] = "research_only"
S6_V_SELECTION_STATUS: Final[str] = "smoke_only"
S6_SAFE_FOR_RUNTIME: Final[bool] = False


@dataclass(frozen=True)
class S6SpectrumOperatorStabilization:
    """Structured stabilization fence for the current S6 spectrum operator."""

    identity: str
    reductive_split: str
    spectrum_target: str
    dirac_operator_convention: str
    casimir_cross_check: str
    review_result: str
    scope: str
    stabilization_result: str
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


def build_s6_spectrum_operator_stabilization() -> S6SpectrumOperatorStabilization:
    """Return the current S6 spectrum operator stabilization contract."""

    review = build_s6_spectrum_operator_review()
    return S6SpectrumOperatorStabilization(
        identity=review.identity,
        reductive_split=review.reductive_split,
        spectrum_target=review.spectrum_target,
        dirac_operator_convention=review.dirac_operator_convention,
        casimir_cross_check=review.casimir_cross_check,
        review_result=review.review_result,
        scope="S6 spectrum operator stabilization only; no spectrum computation or gauge claim",
        stabilization_result="contract_fence_preserved",
    )


def s6_spectrum_operator_stabilization_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and testing."""

    stabilization = build_s6_spectrum_operator_stabilization()
    return {
        "identity": stabilization.identity,
        "reductive_split": stabilization.reductive_split,
        "spectrum_target": stabilization.spectrum_target,
        "dirac_operator_convention": stabilization.dirac_operator_convention,
        "casimir_cross_check": stabilization.casimir_cross_check,
        "review_result": stabilization.review_result,
        "scope": stabilization.scope,
        "stabilization_result": stabilization.stabilization_result,
        "forbidden_claims": stabilization.forbidden_claims,
        "status": S6_SPECTRUM_OPERATOR_STABILIZATION_STATUS,
        "runtime_status": S6_RUNTIME_STATUS,
        "v_selection_status": S6_V_SELECTION_STATUS,
        "safe_for_runtime": S6_SAFE_FOR_RUNTIME,
    }
