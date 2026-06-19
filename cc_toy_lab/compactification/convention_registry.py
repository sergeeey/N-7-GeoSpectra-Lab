"""Convention / gate classification registry (P13 chain). research_only."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Final

from cc_toy_lab.compactification.registry_loader import load_registry

# P13E/P13F frozen statuses — immutable from P13H unless separate gate
P13E_FROZEN_CLASSIFICATION: Final[str] = "NORMALIZATION_DEPENDENT_NO_GO"
P13G_FROZEN_LAMBDA: Final[str] = "FREE_COUPLING_PARAMETER"


class Classification(str, Enum):
    CONVENTION_FIXED_CANDIDATE = "CONVENTION_FIXED_CANDIDATE"
    NORMALIZATION_DEPENDENT_NO_GO = "NORMALIZATION_DEPENDENT_NO_GO"
    FREE_COUPLING_PARAMETER_CONFIRMED = "FREE_COUPLING_PARAMETER_CONFIRMED"
    BASIS_ORDERING_DEPENDENT = "BASIS_ORDERING_DEPENDENT"
    PHASE_DEPENDENT = "PHASE_DEPENDENT"
    FAILED = "FAILED"
    INCONCLUSIVE = "INCONCLUSIVE"


@dataclass(frozen=True)
class GateStatus:
    gate_id: str
    status: str
    classification: str | None = None
    lambda_role: str | None = None
    runtime: str = "research_only"
    safe_for_runtime: bool = False
    selection_rules: str = "smoke_only"
    promotion: str = "forbidden_without_separate_gate"


_GATE_CACHE: dict[str, GateStatus] = {}


def get_gate_status(gate_id: str) -> GateStatus:
    if gate_id in _GATE_CACHE:
        return _GATE_CACHE[gate_id]

    mapping = {
        "P13E": ("P13E_no_go.yaml", P13E_FROZEN_CLASSIFICATION, None),
        "P13F": ("P13F_no_go.yaml", P13E_FROZEN_CLASSIFICATION, P13G_FROZEN_LAMBDA),
        "P13G": ("P13G_handoff.yaml", None, P13G_FROZEN_LAMBDA),
        "P13H": (None, None, None),
    }
    if gate_id not in mapping:
        raise KeyError(f"Unknown gate_id: {gate_id}")

    file_name, classification, lambda_role = mapping[gate_id]
    if file_name is None:
        gs = GateStatus(gate_id=gate_id, status="pending")
    else:
        data = load_registry(file_name)
        gs = GateStatus(
            gate_id=gate_id,
            status=str(data.get("status", "fixed")),
            classification=classification or data.get("reduced_coefficient_scale"),
            lambda_role=lambda_role or data.get("lambda"),
            runtime=str(data.get("runtime", "research_only")),
            safe_for_runtime=bool(data.get("safe_for_runtime", False)),
            selection_rules=str(data.get("selection_rules", "smoke_only")),
            promotion=str(data.get("promotion", "forbidden_without_separate_gate")),
        )
    _GATE_CACHE[gate_id] = gs
    return gs


def register_gate_result(
    gate_id: str,
    classification: Classification,
    *,
    overwrite_frozen: bool = False,
) -> GateStatus:
    """Register P13H result. Cannot overwrite P13E/P13F without evidence flag."""
    if gate_id in {"P13E", "P13F"} and not overwrite_frozen:
        frozen = get_gate_status(gate_id)
        if frozen.classification and frozen.classification != classification.value:
            raise ValueError(
                f"Cannot overwrite frozen {gate_id} classification "
                f"{frozen.classification} -> {classification.value}"
            )
    gs = GateStatus(
        gate_id=gate_id,
        status="completed",
        classification=classification.value,
        lambda_role=P13G_FROZEN_LAMBDA,
    )
    _GATE_CACHE[gate_id] = gs
    return gs
