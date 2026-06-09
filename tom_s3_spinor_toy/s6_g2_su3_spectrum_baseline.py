"""S6 / G2 / SU(3) spectrum baseline contract.

This module is the next fenced layer after the Dirac/Casimir baseline. It does
not compute any spectrum. It only records the spectral target and the claims
that remain forbidden until a real implementation exists.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

from s6_g2_su3_dirac_casimir_baseline import build_s6_dirac_casimir_baseline


S6_SPECTRUM_BASELINE_STATUS: Final[str] = "started"
S6_RUNTIME_STATUS: Final[str] = "research_only"
S6_V_SELECTION_STATUS: Final[str] = "smoke_only"
S6_SAFE_FOR_RUNTIME: Final[bool] = False


@dataclass(frozen=True)
class S6SpectrumBaseline:
    """Structured spectrum fence for the current S6 track."""

    identity: str
    reductive_split: str
    metric_normalization: str
    connection_choice: str
    spinor_bundle_convention: str
    dirac_operator_convention: str
    casimir_cross_check: str
    spectrum_target: str
    scope: str
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


def build_s6_spectrum_baseline() -> S6SpectrumBaseline:
    """Return the current S6 spectrum baseline contract."""

    baseline = build_s6_dirac_casimir_baseline()
    return S6SpectrumBaseline(
        identity=baseline.identity,
        reductive_split=baseline.reductive_split,
        metric_normalization=baseline.metric_normalization,
        connection_choice=baseline.connection_choice,
        spinor_bundle_convention=baseline.spinor_bundle_convention,
        dirac_operator_convention=baseline.dirac_operator_convention,
        casimir_cross_check=baseline.casimir_cross_check,
        spectrum_target="homogeneous Dirac spectrum on S6, to be derived later",
        scope="S6 spectrum baseline only; no spectrum computed and no gauge claim",
    )


def s6_spectrum_baseline_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and testing."""

    baseline = build_s6_spectrum_baseline()
    return {
        "identity": baseline.identity,
        "reductive_split": baseline.reductive_split,
        "metric_normalization": baseline.metric_normalization,
        "connection_choice": baseline.connection_choice,
        "spinor_bundle_convention": baseline.spinor_bundle_convention,
        "dirac_operator_convention": baseline.dirac_operator_convention,
        "casimir_cross_check": baseline.casimir_cross_check,
        "spectrum_target": baseline.spectrum_target,
        "scope": baseline.scope,
        "forbidden_claims": baseline.forbidden_claims,
        "status": S6_SPECTRUM_BASELINE_STATUS,
        "runtime_status": S6_RUNTIME_STATUS,
        "v_selection_status": S6_V_SELECTION_STATUS,
        "safe_for_runtime": S6_SAFE_FOR_RUNTIME,
    }
