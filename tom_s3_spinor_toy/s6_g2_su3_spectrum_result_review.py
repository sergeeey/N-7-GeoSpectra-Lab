"""S6 / G2 / SU(3) spectrum result review contract.

This is the terminal review fence after the analytic spectrum computation
layer. It does not compute anything new; it only records the resulting round-S6
baseline and keeps the remaining claims fenced off.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

from s6_g2_su3_spectrum_computation import s6_spectrum_computation_summary


S6_SPECTRUM_RESULT_REVIEW_STATUS: Final[str] = "passed"
S6_RUNTIME_STATUS: Final[str] = "research_only"
S6_V_SELECTION_STATUS: Final[str] = "smoke_only"
S6_SAFE_FOR_RUNTIME: Final[bool] = False


@dataclass(frozen=True)
class S6SpectrumResultReview:
    """Terminal review fence for the analytic S6 spectrum result."""

    identity: str
    reductive_split: str
    metric_normalization: str
    connection_choice: str
    spinor_bundle_convention: str
    dirac_operator_convention: str
    casimir_cross_check: str
    spectrum_target: str
    spectrum_formula: str
    multiplicity_formula: str
    computation_status: str
    scope: str
    forbidden_claims: Tuple[str, ...] = field(
        default_factory=lambda: (
            "SU4 gauge decomposition",
            "hypercharge",
            "instanton",
            "index",
            "chirality",
            "runtime safe promotion",
        )
    )


def build_s6_spectrum_result_review() -> S6SpectrumResultReview:
    """Return the current S6 spectrum result review contract."""

    summary = s6_spectrum_computation_summary()
    return S6SpectrumResultReview(
        identity=summary["identity"],
        reductive_split=summary["reductive_split"],
        metric_normalization=summary["metric_normalization"],
        connection_choice=summary["connection_choice"],
        spinor_bundle_convention=summary["spinor_bundle_convention"],
        dirac_operator_convention=summary["dirac_operator_convention"],
        casimir_cross_check=summary["casimir_cross_check"],
        spectrum_target=summary["spectrum_target"],
        spectrum_formula="lambda_{k,+/-} = +/- (k + 3) / R",
        multiplicity_formula="mu_k = 8 * binomial(k + 5, k)",
        computation_status=summary["status"],
        scope="S6 spectrum result review only; no new spectrum computation or gauge claim",
    )


def s6_spectrum_result_review_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and testing."""

    review = build_s6_spectrum_result_review()
    return {
        "identity": review.identity,
        "reductive_split": review.reductive_split,
        "metric_normalization": review.metric_normalization,
        "connection_choice": review.connection_choice,
        "spinor_bundle_convention": review.spinor_bundle_convention,
        "dirac_operator_convention": review.dirac_operator_convention,
        "casimir_cross_check": review.casimir_cross_check,
        "spectrum_target": review.spectrum_target,
        "spectrum_formula": review.spectrum_formula,
        "multiplicity_formula": review.multiplicity_formula,
        "computation_status": review.computation_status,
        "scope": review.scope,
        "forbidden_claims": review.forbidden_claims,
        "status": S6_SPECTRUM_RESULT_REVIEW_STATUS,
        "runtime_status": S6_RUNTIME_STATUS,
        "v_selection_status": S6_V_SELECTION_STATUS,
        "safe_for_runtime": S6_SAFE_FOR_RUNTIME,
    }
