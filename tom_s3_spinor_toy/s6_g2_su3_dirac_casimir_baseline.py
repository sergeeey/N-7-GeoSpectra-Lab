"""S6 / G2 / SU(3) Dirac/Casimir baseline contract.

This module is the next executable layer for the separate S6 track after the
geometry convention has been fixed. It does not compute a spectrum, does not
claim an SU(4) gauge decomposition, and does not mix with the validated S3
basis layer.

The baseline is deliberately conservative:

- it keeps the homogeneous-space identity `S6 ≅ G2 / SU(3)`;
- it keeps the reductive split `g2 = su(3) ⊕ m`;
- it fixes the operator target as the homogeneous Dirac/Casimir cross-check;
- it records the current convention fence so future implementation work cannot
  drift into spectrum, hypercharge, index, or chirality claims by accident.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

from s6_g2_su3_implementation import build_s6_implementation_contract


S6_DIRAC_CASIMIR_STATUS: Final[str] = "started"
S6_RUNTIME_STATUS: Final[str] = "research_only"
S6_V_SELECTION_STATUS: Final[str] = "smoke_only"
S6_SAFE_FOR_RUNTIME: Final[bool] = False


@dataclass(frozen=True)
class S6DiracCasimirBaseline:
    """Structured baseline contract for the current S6 Dirac layer."""

    identity: str
    reductive_split: str
    metric_normalization: str
    connection_choice: str
    spinor_bundle_convention: str
    dirac_operator_convention: str
    casimir_cross_check: str
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


def build_s6_dirac_casimir_baseline() -> S6DiracCasimirBaseline:
    """Return the current S6 Dirac/Casimir baseline contract."""

    contract = build_s6_implementation_contract()
    return S6DiracCasimirBaseline(
        identity=contract.identity,
        reductive_split=contract.reductive_split,
        metric_normalization=contract.metric_normalization,
        connection_choice=contract.connection_choice,
        spinor_bundle_convention=contract.spinor_bundle_convention,
        dirac_operator_convention=contract.dirac_operator_convention,
        casimir_cross_check="D ~ C_G + (1/8) s",
        scope="S6 Dirac/Casimir baseline only; no spectrum or gauge claim",
    )


def s6_dirac_casimir_baseline_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and testing."""

    baseline = build_s6_dirac_casimir_baseline()
    return {
        "identity": baseline.identity,
        "reductive_split": baseline.reductive_split,
        "metric_normalization": baseline.metric_normalization,
        "connection_choice": baseline.connection_choice,
        "spinor_bundle_convention": baseline.spinor_bundle_convention,
        "dirac_operator_convention": baseline.dirac_operator_convention,
        "casimir_cross_check": baseline.casimir_cross_check,
        "scope": baseline.scope,
        "forbidden_claims": baseline.forbidden_claims,
        "status": S6_DIRAC_CASIMIR_STATUS,
        "runtime_status": S6_RUNTIME_STATUS,
        "v_selection_status": S6_V_SELECTION_STATUS,
        "safe_for_runtime": S6_SAFE_FOR_RUNTIME,
    }
