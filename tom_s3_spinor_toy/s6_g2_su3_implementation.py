"""S6 / G2 / SU(3) implementation contract.

This module is the first executable layer for the separate S6 track. It does
not compute a spectrum, does not claim an SU(4) gauge decomposition, and does
not mix with the validated S3 basis layer.

The implementation is deliberately conservative:

- it fixes the homogeneous-space identity `S6 ≅ G2 / SU(3)`;
- it records the reductive split `g2 = su(3) ⊕ m`;
- it chooses a canonical homogeneous metric normalization and connection;
- it fixes a canonical spinor-bundle convention for the reductive frame;
- it preserves the homogeneous Dirac/Casimir baseline as the operator target;
- it stores the current claim fence so later implementation work cannot drift
  into hypercharge/index/chirality claims by accident.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

from s6_g2_su3_formula_spec import s6_formula_spec


S6_IMPLEMENTATION_STATUS: Final[str] = "started"
S6_RUNTIME_STATUS: Final[str] = "research_only"
S6_V_SELECTION_STATUS: Final[str] = "smoke_only"
S6_SAFE_FOR_RUNTIME: Final[bool] = False


@dataclass(frozen=True)
class S6ImplementationContract:
    """Structured contract for the current S6 implementation layer."""

    identity: str
    reductive_split: str
    dirac_baseline: str
    scope: str
    metric_normalization: str
    connection_choice: str
    spinor_bundle_convention: str
    dirac_operator_convention: str
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


def build_s6_implementation_contract() -> S6ImplementationContract:
    """Return the current S6 implementation contract."""

    spec = s6_formula_spec()
    return S6ImplementationContract(
        identity=spec.identity,
        reductive_split=spec.reductive_split,
        dirac_baseline=spec.dirac_baseline,
        scope="S6 implementation contract only; no spectrum or gauge claim",
        metric_normalization="unit round S6 normalization",
        connection_choice="Levi-Civita connection on the canonical homogeneous metric",
        spinor_bundle_convention="canonical spin structure induced by the G2/SU(3) reductive frame",
        dirac_operator_convention="homogeneous Dirac operator with Casimir cross-check target",
    )


def s6_implementation_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and testing."""

    contract = build_s6_implementation_contract()
    return {
        "identity": contract.identity,
        "reductive_split": contract.reductive_split,
        "dirac_baseline": contract.dirac_baseline,
        "scope": contract.scope,
        "metric_normalization": contract.metric_normalization,
        "connection_choice": contract.connection_choice,
        "spinor_bundle_convention": contract.spinor_bundle_convention,
        "dirac_operator_convention": contract.dirac_operator_convention,
        "selection_rules_status": contract.selection_rules_status,
        "forbidden_claims": contract.forbidden_claims,
        "implementation_status": S6_IMPLEMENTATION_STATUS,
        "runtime_status": S6_RUNTIME_STATUS,
        "v_selection_status": S6_V_SELECTION_STATUS,
        "safe_for_runtime": S6_SAFE_FOR_RUNTIME,
    }
