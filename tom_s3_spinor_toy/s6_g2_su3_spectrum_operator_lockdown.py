"""S6 / G2 / SU(3) spectrum operator lockdown contract.

This module is the next executable lock after stabilization. It does not
compute a spectrum. It exists only to make the fence explicit, stable, and
hard to misread as an implementation claim.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

from s6_g2_su3_spectrum_operator_stabilization import (
    build_s6_spectrum_operator_stabilization,
)


S6_SPECTRUM_OPERATOR_LOCKDOWN_STATUS: Final[str] = "started"
S6_RUNTIME_STATUS: Final[str] = "research_only"
S6_V_SELECTION_STATUS: Final[str] = "smoke_only"
S6_SAFE_FOR_RUNTIME: Final[bool] = False


@dataclass(frozen=True)
class S6SpectrumOperatorLockdown:
    """Structured lockdown fence for the current S6 spectrum operator."""

    identity: str
    reductive_split: str
    spectrum_target: str
    dirac_operator_convention: str
    casimir_cross_check: str
    review_result: str
    stabilization_result: str
    scope: str
    lockdown_result: str
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


def build_s6_spectrum_operator_lockdown() -> S6SpectrumOperatorLockdown:
    """Return the current S6 spectrum operator lockdown contract."""

    stabilization = build_s6_spectrum_operator_stabilization()
    return S6SpectrumOperatorLockdown(
        identity=stabilization.identity,
        reductive_split=stabilization.reductive_split,
        spectrum_target=stabilization.spectrum_target,
        dirac_operator_convention=stabilization.dirac_operator_convention,
        casimir_cross_check=stabilization.casimir_cross_check,
        review_result=stabilization.review_result,
        stabilization_result=stabilization.stabilization_result,
        scope="S6 spectrum operator lockdown only; no spectrum computation or gauge claim",
        lockdown_result="contract_fence_preserved",
    )


def s6_spectrum_operator_lockdown_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and testing."""

    lockdown = build_s6_spectrum_operator_lockdown()
    return {
        "identity": lockdown.identity,
        "reductive_split": lockdown.reductive_split,
        "spectrum_target": lockdown.spectrum_target,
        "dirac_operator_convention": lockdown.dirac_operator_convention,
        "casimir_cross_check": lockdown.casimir_cross_check,
        "review_result": lockdown.review_result,
        "stabilization_result": lockdown.stabilization_result,
        "scope": lockdown.scope,
        "lockdown_result": lockdown.lockdown_result,
        "forbidden_claims": lockdown.forbidden_claims,
        "status": S6_SPECTRUM_OPERATOR_LOCKDOWN_STATUS,
        "runtime_status": S6_RUNTIME_STATUS,
        "v_selection_status": S6_V_SELECTION_STATUS,
        "safe_for_runtime": S6_SAFE_FOR_RUNTIME,
    }
