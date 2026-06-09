"""P13F V-operator derivation status and no-go record.

This module records the current state of the candidate V-like S3 operator
stack after P13A-P13E. It does not introduce a new physical derivation.

The record is intentionally conservative: it summarizes the fixed source
identities, the preserved Hermiticity, the compatibility with the frozen
P11/P12 scaffold, and the remaining no-go on the exact reduced coefficient
scale / free coupling.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache
from typing import Final, Tuple

from p11_external_oracle_matrix_element_derivation import (
    p11_external_oracle_matrix_element_derivation_summary,
)
from p12_matrix_element_derivation_robustness_audit import (
    p12_matrix_element_derivation_robustness_audit_summary,
)
from p13a_v_operator_ansatz_convention_registry import (
    P13_READY_FOR_SYMBOLIC_DERIVATION,
    p13a_v_operator_ansatz_convention_registry_summary,
)
from p13b1_spinor_state_selection_rule_repair import (
    P13B_PATTERN_STILL_VALID,
    p13b1_spinor_state_selection_rule_repair_summary,
)
from p13c_ben_achour_e_mode_formula_derivation import (
    SOURCE_FIXED,
    p13c_ben_achour_e_mode_formula_derivation_summary,
)
from p13d_coefficient_normalization_and_hermiticity_audit import (
    CONVENTION_FIXED,
    p13d_coefficient_normalization_and_hermiticity_audit_summary,
)
from p13e_reduced_coefficient_scale_fixing_or_no_go import (
    FREE_COUPLING_PARAMETER,
    NORMALIZATION_DEPENDENT_NO_GO,
    p13e_reduced_coefficient_scale_audit_summary,
)
from su4_hypercharge_gauge_breaking_audit import su4_hypercharge_gauge_audit_summary


P13F_V_OPERATOR_DERIVATION_STATUS_AND_NO_GO_RECORD_STATUS: Final[str] = "passed"
NO_GO_RECORD: Final[str] = "NO_GO_RECORD"
V_OPERATOR_DERIVATION_BLOCKED: Final[str] = "V_OPERATOR_DERIVATION_BLOCKED"


@lru_cache(maxsize=1)
def _p13a_summary() -> dict[str, object]:
    return p13a_v_operator_ansatz_convention_registry_summary()


@lru_cache(maxsize=1)
def _p13b1_summary() -> dict[str, object]:
    return p13b1_spinor_state_selection_rule_repair_summary()


@lru_cache(maxsize=1)
def _p13c_summary() -> dict[str, object]:
    return p13c_ben_achour_e_mode_formula_derivation_summary()


@lru_cache(maxsize=1)
def _p13d_summary() -> dict[str, object]:
    return p13d_coefficient_normalization_and_hermiticity_audit_summary()


@lru_cache(maxsize=1)
def _p13e_summary() -> dict[str, object]:
    return p13e_reduced_coefficient_scale_audit_summary()


@lru_cache(maxsize=1)
def _p11_summary() -> dict[str, object]:
    return p11_external_oracle_matrix_element_derivation_summary()


@lru_cache(maxsize=1)
def _p12_summary() -> dict[str, object]:
    return p12_matrix_element_derivation_robustness_audit_summary()


@lru_cache(maxsize=1)
def _p7_summary() -> dict[str, object]:
    return su4_hypercharge_gauge_audit_summary()


@dataclass(frozen=True)
class P13FVOperatorDerivationStatusAndNoGoRecord:
    """Structured final status record for the current V-derivation state."""

    p13a_status: str
    p13b1_status: str
    p13c_status: str
    p13d_status: str
    p13e_status: str
    p11_status: str
    p12_status: str
    p7_status: str
    source_identity_status: str
    convention_stack_status: str
    hermiticity_status: str
    compatibility_status: str
    scale_status: str
    coupling_status: str
    operator_status: str
    verdict: str
    blocking_fields: Tuple[str, ...] = field(
        default_factory=lambda: (
            "free coupling lambda",
            "exact reduced coefficient scale",
            "physical V-operator density",
        )
    )
    scope: str = (
        "P13F status and no-go record only; no new derivation and no physical V promotion"
    )
    forbidden_claims: Tuple[str, ...] = field(
        default_factory=lambda: (
            "physical V-operator derivation",
            "V-selection promotion",
            "Standard Model reproduced claim",
            "fermion generation claim",
            "safe_for_runtime promotion",
        )
    )


def _source_identity_status() -> str:
    p13c = _p13c_summary()
    p13d = _p13d_summary()
    p13e = _p13e_summary()
    if (
        p13c["source_formula_status"] == SOURCE_FIXED
        and p13d["source_identity_status"] == SOURCE_FIXED
        and p13e["source_identity_status"] == SOURCE_FIXED
    ):
        return SOURCE_FIXED
    return V_OPERATOR_DERIVATION_BLOCKED


def _convention_stack_status() -> str:
    p13a = _p13a_summary()
    p7 = _p7_summary()
    p13d = _p13d_summary()
    if (
        p13a["readiness_verdict"] == P13_READY_FOR_SYMBOLIC_DERIVATION
        and p13d["convention_stack_status"] == CONVENTION_FIXED
        and p7["audit_result"] == "su4_algebra_audit_passed_with_normalization_dependent_yw"
    ):
        return CONVENTION_FIXED
    return V_OPERATOR_DERIVATION_BLOCKED


def _hermiticity_status() -> str:
    p12 = _p12_summary()
    p13d = _p13d_summary()
    p7 = _p7_summary()
    if (
        p12["hermiticity_status"] == "ROBUST"
        and p13d["hermiticity_status"] == CONVENTION_FIXED
        and bool(p7["hermiticity_verified"])
    ):
        return CONVENTION_FIXED
    return V_OPERATOR_DERIVATION_BLOCKED


def _compatibility_status() -> str:
    p11 = _p11_summary()
    p12 = _p12_summary()
    p13b1 = _p13b1_summary()
    p13e = _p13e_summary()
    if (
        p11["comparison_status"] == "MATCHES_FROZEN_SCAFFOLD"
        and p12["overall_status"] == "ROBUST"
        and p13b1["verdict"] == P13B_PATTERN_STILL_VALID
        and p13e["scale_fix_status"] == NORMALIZATION_DEPENDENT_NO_GO
    ):
        return CONVENTION_FIXED
    return V_OPERATOR_DERIVATION_BLOCKED


def _scale_status() -> str:
    p13e = _p13e_summary()
    if p13e["scale_fix_status"] == NORMALIZATION_DEPENDENT_NO_GO:
        return NORMALIZATION_DEPENDENT_NO_GO
    return V_OPERATOR_DERIVATION_BLOCKED


def _coupling_status() -> str:
    p13e = _p13e_summary()
    if p13e["coupling_parameter_status"] == FREE_COUPLING_PARAMETER:
        return FREE_COUPLING_PARAMETER
    return V_OPERATOR_DERIVATION_BLOCKED


def build_p13f_v_operator_derivation_status_and_no_go_record() -> P13FVOperatorDerivationStatusAndNoGoRecord:
    """Return the final status/no-go record for the current V-derivation stack."""

    p13a = _p13a_summary()
    p13b1 = _p13b1_summary()
    p13c = _p13c_summary()
    p13d = _p13d_summary()
    p13e = _p13e_summary()
    p11 = _p11_summary()
    p12 = _p12_summary()
    p7 = _p7_summary()

    source_identity_status = _source_identity_status()
    convention_stack_status = _convention_stack_status()
    hermiticity_status = _hermiticity_status()
    compatibility_status = _compatibility_status()
    scale_status = _scale_status()
    coupling_status = _coupling_status()

    if (
        source_identity_status == SOURCE_FIXED
        and convention_stack_status == CONVENTION_FIXED
        and hermiticity_status == CONVENTION_FIXED
        and compatibility_status == CONVENTION_FIXED
        and scale_status == NORMALIZATION_DEPENDENT_NO_GO
        and coupling_status == FREE_COUPLING_PARAMETER
    ):
        verdict = NO_GO_RECORD
        operator_status = V_OPERATOR_DERIVATION_BLOCKED
    else:
        verdict = V_OPERATOR_DERIVATION_BLOCKED
        operator_status = V_OPERATOR_DERIVATION_BLOCKED

    return P13FVOperatorDerivationStatusAndNoGoRecord(
        p13a_status=str(p13a["status"]),
        p13b1_status=str(p13b1["status"]),
        p13c_status=str(p13c["status"]),
        p13d_status=str(p13d["status"]),
        p13e_status=str(p13e["status"]),
        p11_status=str(p11["status"]),
        p12_status=str(p12["status"]),
        p7_status=str(p7["audit_result"]),
        source_identity_status=source_identity_status,
        convention_stack_status=convention_stack_status,
        hermiticity_status=hermiticity_status,
        compatibility_status=compatibility_status,
        scale_status=scale_status,
        coupling_status=coupling_status,
        operator_status=operator_status,
        verdict=verdict,
    )


def p13f_v_operator_derivation_status_and_no_go_record_summary() -> dict[str, object]:
    """Return a compact summary suitable for tests and reports."""

    record = build_p13f_v_operator_derivation_status_and_no_go_record()
    return {
        "status": P13F_V_OPERATOR_DERIVATION_STATUS_AND_NO_GO_RECORD_STATUS,
        "p13a_status": record.p13a_status,
        "p13b1_status": record.p13b1_status,
        "p13c_status": record.p13c_status,
        "p13d_status": record.p13d_status,
        "p13e_status": record.p13e_status,
        "p11_status": record.p11_status,
        "p12_status": record.p12_status,
        "p7_status": record.p7_status,
        "source_identity_status": record.source_identity_status,
        "convention_stack_status": record.convention_stack_status,
        "hermiticity_status": record.hermiticity_status,
        "compatibility_status": record.compatibility_status,
        "scale_status": record.scale_status,
        "coupling_status": record.coupling_status,
        "operator_status": record.operator_status,
        "verdict": record.verdict,
        "blocking_fields": record.blocking_fields,
        "scope": record.scope,
        "forbidden_claims": record.forbidden_claims,
        "runtime_status": "research_only",
        "v_selection_status": "smoke_only",
        "safe_for_runtime": False,
    }
