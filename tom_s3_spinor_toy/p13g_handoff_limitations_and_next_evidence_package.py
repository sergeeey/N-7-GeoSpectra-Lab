"""P13G handoff limitations and next evidence package.

This module records the post-P13F handoff state for the candidate V-like S3
stack. It does not introduce a new derivation. The purpose is to preserve the
validated scaffold, the remaining blocker, and the next evidence requirement.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache
from typing import Final, Tuple

from p13a_v_operator_ansatz_convention_registry import (
    p13a_v_operator_ansatz_convention_registry_summary,
)
from p13b1_spinor_state_selection_rule_repair import (
    p13b1_spinor_state_selection_rule_repair_summary,
)
from p13c_ben_achour_e_mode_formula_derivation import (
    p13c_ben_achour_e_mode_formula_derivation_summary,
)
from p13d_coefficient_normalization_and_hermiticity_audit import (
    p13d_coefficient_normalization_and_hermiticity_audit_summary,
)
from p13e_reduced_coefficient_scale_fixing_or_no_go import (
    p13e_reduced_coefficient_scale_audit_summary,
)
from p13f_v_operator_derivation_status_and_no_go_record import (
    p13f_v_operator_derivation_status_and_no_go_record_summary,
)
from p11_external_oracle_matrix_element_derivation import (
    p11_external_oracle_matrix_element_derivation_summary,
)
from p12_matrix_element_derivation_robustness_audit import (
    p12_matrix_element_derivation_robustness_audit_summary,
)
from su4_hypercharge_gauge_breaking_audit import su4_hypercharge_gauge_audit_summary


P13G_HANDOFF_LIMITATIONS_AND_NEXT_EVIDENCE_PACKAGE_STATUS: Final[str] = "passed"
HANDOFF_RECORDED: Final[str] = "HANDOFF_RECORDED"


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
def _p13f_summary() -> dict[str, object]:
    return p13f_v_operator_derivation_status_and_no_go_record_summary()


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
class P13GHandoffLimitationsAndNextEvidencePackage:
    """Structured handoff package after the no-go record."""

    p13a_status: str
    p13b1_status: str
    p13c_status: str
    p13d_status: str
    p13e_status: str
    p13f_status: str
    p11_status: str
    p12_status: str
    p7_status: str
    validated_stack_status: str
    blocker_status: str
    next_evidence_requirement: str
    handoff_status: str
    summary_status: str
    verified_claims: Tuple[str, ...]
    not_verified: Tuple[str, ...]
    scope: str = (
        "P13G handoff / limitations package only; no new derivation and no "
        "physical promotion"
    )
    fence: Tuple[str, ...] = field(
        default_factory=lambda: (
            "runtime = research_only",
            "safe_for_runtime = no",
            "selection_rules = smoke_only",
            "promotion = forbidden_without_separate_gate",
        )
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


def build_p13g_handoff_limitations_and_next_evidence_package() -> P13GHandoffLimitationsAndNextEvidencePackage:
    """Return the frozen handoff package."""

    p13a = _p13a_summary()
    p13b1 = _p13b1_summary()
    p13c = _p13c_summary()
    p13d = _p13d_summary()
    p13e = _p13e_summary()
    p13f = _p13f_summary()
    p11 = _p11_summary()
    p12 = _p12_summary()
    p7 = _p7_summary()

    validated_stack_status = "P13A-P13F frozen and consistent"
    blocker_status = "lambda remains a free coupling parameter"
    next_evidence_requirement = (
        "A new external physical principle or source-fixed coupling derivation "
        "that actually fixes lambda"
    )

    verified_claims = (
        "source identities are fixed",
        "convention stack is fixed",
        "Hermiticity is preserved",
        "compatibility with P11/P12 is preserved",
        "reduced coefficient scale is NORMALIZATION_DEPENDENT_NO_GO",
        "lambda remains FREE_COUPLING_PARAMETER",
    )
    not_verified = (
        "physical V-operator derivation",
        "physical V-selection rules",
        "Standard Model reproduction",
        "fermion generation claim",
        "runtime safety",
    )

    return P13GHandoffLimitationsAndNextEvidencePackage(
        p13a_status=str(p13a["status"]),
        p13b1_status=str(p13b1["status"]),
        p13c_status=str(p13c["status"]),
        p13d_status=str(p13d["status"]),
        p13e_status=str(p13e["status"]),
        p13f_status=str(p13f["status"]),
        p11_status=str(p11["status"]),
        p12_status=str(p12["status"]),
        p7_status=str(p7["audit_result"]),
        validated_stack_status=validated_stack_status,
        blocker_status=blocker_status,
        next_evidence_requirement=next_evidence_requirement,
        handoff_status=HANDOFF_RECORDED,
        summary_status=P13G_HANDOFF_LIMITATIONS_AND_NEXT_EVIDENCE_PACKAGE_STATUS,
        verified_claims=verified_claims,
        not_verified=not_verified,
    )


def p13g_handoff_limitations_and_next_evidence_package_summary() -> dict[str, object]:
    """Return a compact summary suitable for tests and reports."""

    package = build_p13g_handoff_limitations_and_next_evidence_package()
    return {
        "status": P13G_HANDOFF_LIMITATIONS_AND_NEXT_EVIDENCE_PACKAGE_STATUS,
        "p13a_status": package.p13a_status,
        "p13b1_status": package.p13b1_status,
        "p13c_status": package.p13c_status,
        "p13d_status": package.p13d_status,
        "p13e_status": package.p13e_status,
        "p13f_status": package.p13f_status,
        "p11_status": package.p11_status,
        "p12_status": package.p12_status,
        "p7_status": package.p7_status,
        "validated_stack_status": package.validated_stack_status,
        "blocker_status": package.blocker_status,
        "next_evidence_requirement": package.next_evidence_requirement,
        "handoff_status": package.handoff_status,
        "summary_status": package.summary_status,
        "verified_claims": package.verified_claims,
        "not_verified": package.not_verified,
        "scope": package.scope,
        "fence": package.fence,
        "forbidden_claims": package.forbidden_claims,
    }
