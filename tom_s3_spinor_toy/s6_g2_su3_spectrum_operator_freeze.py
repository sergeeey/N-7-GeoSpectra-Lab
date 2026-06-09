"""S6 / G2 / SU(3) spectrum operator freeze contract.

This module is the next executable fence after lockdown. It does not compute a
spectrum. It freezes the current operator contract so later work cannot drift
into claims that exceed the supported S6 baseline.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

from s6_g2_su3_spectrum_operator_lockdown import build_s6_spectrum_operator_lockdown


S6_SPECTRUM_OPERATOR_FREEZE_STATUS: Final[str] = "started"
S6_RUNTIME_STATUS: Final[str] = "research_only"
S6_V_SELECTION_STATUS: Final[str] = "smoke_only"
S6_SAFE_FOR_RUNTIME: Final[bool] = False


@dataclass(frozen=True)
class S6SpectrumOperatorFreeze:
    """Structured freeze fence for the current S6 spectrum operator."""

    identity: str
    reductive_split: str
    spectrum_target: str
    dirac_operator_convention: str
    casimir_cross_check: str
    review_result: str
    stabilization_result: str
    lockdown_result: str
    scope: str
    freeze_result: str
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


def build_s6_spectrum_operator_freeze() -> S6SpectrumOperatorFreeze:
    """Return the current S6 spectrum operator freeze contract."""

    lockdown = build_s6_spectrum_operator_lockdown()
    return S6SpectrumOperatorFreeze(
        identity=lockdown.identity,
        reductive_split=lockdown.reductive_split,
        spectrum_target=lockdown.spectrum_target,
        dirac_operator_convention=lockdown.dirac_operator_convention,
        casimir_cross_check=lockdown.casimir_cross_check,
        review_result=lockdown.review_result,
        stabilization_result=lockdown.stabilization_result,
        lockdown_result=lockdown.lockdown_result,
        scope="S6 spectrum operator freeze only; no spectrum computation or gauge claim",
        freeze_result="contract_fence_preserved",
    )


def s6_spectrum_operator_freeze_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and testing."""

    freeze = build_s6_spectrum_operator_freeze()
    return {
        "identity": freeze.identity,
        "reductive_split": freeze.reductive_split,
        "spectrum_target": freeze.spectrum_target,
        "dirac_operator_convention": freeze.dirac_operator_convention,
        "casimir_cross_check": freeze.casimir_cross_check,
        "review_result": freeze.review_result,
        "stabilization_result": freeze.stabilization_result,
        "lockdown_result": freeze.lockdown_result,
        "scope": freeze.scope,
        "freeze_result": freeze.freeze_result,
        "forbidden_claims": freeze.forbidden_claims,
        "status": S6_SPECTRUM_OPERATOR_FREEZE_STATUS,
        "runtime_status": S6_RUNTIME_STATUS,
        "v_selection_status": S6_V_SELECTION_STATUS,
        "safe_for_runtime": S6_SAFE_FOR_RUNTIME,
    }
