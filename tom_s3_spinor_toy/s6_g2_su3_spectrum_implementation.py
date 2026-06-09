"""S6 / G2 / SU(3) spectrum implementation contract.

This module is the next executable layer after the spectrum baseline. It does
not compute any spectrum. It only records the implementation fence and keeps
the separate S6 track from drifting into SU(4), hypercharge, or other claims
that are not yet supported.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

from s6_g2_su3_spectrum_baseline import build_s6_spectrum_baseline


S6_SPECTRUM_IMPLEMENTATION_STATUS: Final[str] = "started"
S6_RUNTIME_STATUS: Final[str] = "research_only"
S6_V_SELECTION_STATUS: Final[str] = "smoke_only"
S6_SAFE_FOR_RUNTIME: Final[bool] = False


@dataclass(frozen=True)
class S6SpectrumImplementation:
    """Structured implementation contract for the current S6 spectrum layer."""

    identity: str
    reductive_split: str
    metric_normalization: str
    connection_choice: str
    spinor_bundle_convention: str
    dirac_operator_convention: str
    casimir_cross_check: str
    spectrum_target: str
    scope: str
    selection_rules_status: str = "not started"
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


def build_s6_spectrum_implementation() -> S6SpectrumImplementation:
    """Return the current S6 spectrum implementation contract."""

    baseline = build_s6_spectrum_baseline()
    return S6SpectrumImplementation(
        identity=baseline.identity,
        reductive_split=baseline.reductive_split,
        metric_normalization=baseline.metric_normalization,
        connection_choice=baseline.connection_choice,
        spinor_bundle_convention=baseline.spinor_bundle_convention,
        dirac_operator_convention=baseline.dirac_operator_convention,
        casimir_cross_check=baseline.casimir_cross_check,
        spectrum_target=baseline.spectrum_target,
        scope="S6 spectrum implementation contract only; no spectrum or gauge claim",
    )


def s6_spectrum_implementation_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and testing."""

    contract = build_s6_spectrum_implementation()
    return {
        "identity": contract.identity,
        "reductive_split": contract.reductive_split,
        "metric_normalization": contract.metric_normalization,
        "connection_choice": contract.connection_choice,
        "spinor_bundle_convention": contract.spinor_bundle_convention,
        "dirac_operator_convention": contract.dirac_operator_convention,
        "casimir_cross_check": contract.casimir_cross_check,
        "spectrum_target": contract.spectrum_target,
        "scope": contract.scope,
        "selection_rules_status": contract.selection_rules_status,
        "forbidden_claims": contract.forbidden_claims,
        "status": S6_SPECTRUM_IMPLEMENTATION_STATUS,
        "runtime_status": S6_RUNTIME_STATUS,
        "v_selection_status": S6_V_SELECTION_STATUS,
        "safe_for_runtime": S6_SAFE_FOR_RUNTIME,
    }
