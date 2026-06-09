"""P13D coefficient normalization and Hermiticity audit.

This module audits whether the reduced coefficient normalization in the
Ben Achour E_i / E'_i derivation can be fixed by the existing source
identities, Haar/unit-coframe normalization, Clifford gamma convention,
and P7 SU4 trace convention.

It does not promote a physical V-operator and does not promote V-selection
rules.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache
from typing import Final, Tuple

from convention_registry import (
    CONVENTION_FIXED,
    NORMALIZATION_DEPENDENT,
)
from p11_external_oracle_matrix_element_derivation import (
    MATCHES_FROZEN_SCAFFOLD,
    p11_external_oracle_matrix_element_derivation_summary,
)
from p12_matrix_element_derivation_robustness_audit import (
    ROBUST,
    p12_matrix_element_derivation_robustness_audit_summary,
)
from p13a_v_operator_ansatz_convention_registry import (
    P13_READY_FOR_SYMBOLIC_DERIVATION,
    p13a_v_operator_ansatz_convention_registry_summary,
)
from p13b1_spinor_state_selection_rule_repair import (
    p13b1_spinor_state_selection_rule_repair_summary,
)
from p13c_ben_achour_e_mode_formula_derivation import (
    SOURCE_FIXED,
    p13c_ben_achour_e_mode_formula_derivation_summary,
)
from p13c0_toy_gradient_formula_audit import (
    p13c0_toy_gradient_formula_audit_summary,
)
from p13c_reduced_matrix_element_normalization_audit import (
    NORMALIZATION_DEPENDENT as P13C_REDUCED_NORMALIZATION_DEPENDENT,
    PHASE_CONVENTION_DEPENDENT,
    p13c_reduced_matrix_element_normalization_audit_summary,
)
from su4_hypercharge_gauge_breaking_audit import (
    su4_hypercharge_gauge_audit_summary,
)


P13D_COEFFICIENT_NORMALIZATION_AND_HERMITICITY_AUDIT_STATUS: Final[str] = "passed"
PHASE_DEPENDENT: Final[str] = "PHASE_DEPENDENT"
BASIS_ORDERING_DEPENDENT: Final[str] = "BASIS_ORDERING_DEPENDENT"
FAILED: Final[str] = "FAILED"


@lru_cache(maxsize=1)
def _p13a_summary() -> dict[str, object]:
    return p13a_v_operator_ansatz_convention_registry_summary()


@lru_cache(maxsize=1)
def _p13b1_summary() -> dict[str, object]:
    return p13b1_spinor_state_selection_rule_repair_summary()


@lru_cache(maxsize=1)
def _p13c0_summary() -> dict[str, object]:
    return p13c0_toy_gradient_formula_audit_summary()


@lru_cache(maxsize=1)
def _p13c_summary() -> dict[str, object]:
    return p13c_ben_achour_e_mode_formula_derivation_summary()


@lru_cache(maxsize=1)
def _p11_summary() -> dict[str, object]:
    return p11_external_oracle_matrix_element_derivation_summary()


@lru_cache(maxsize=1)
def _p12_summary() -> dict[str, object]:
    return p12_matrix_element_derivation_robustness_audit_summary()


@lru_cache(maxsize=1)
def _p7_summary() -> dict[str, object]:
    return su4_hypercharge_gauge_audit_summary()


@lru_cache(maxsize=1)
def _p13c_reduced_summary() -> dict[str, object]:
    return p13c_reduced_matrix_element_normalization_audit_summary()


@dataclass(frozen=True)
class P13DCoefficientNormalizationAndHermiticityAudit:
    """Structured contract for the P13D normalization/Hermiticity audit."""

    p13a_status: str
    p13b1_status: str
    p13c0_status: str
    p13c_status: str
    p11_status: str
    p12_status: str
    p7_status: str
    source_identity_status: str
    convention_stack_status: str
    hermiticity_status: str
    coefficient_scaling_status: str
    p11_p12_compatibility_status: str
    ad_hoc_normalization_status: str
    exact_coefficient_status: str
    exact_normalization_status: str
    phase_status: str
    lambda_status: str
    verdict: str
    blocking_fields: Tuple[str, ...] = field(
        default_factory=lambda: (
            "exact reduced-coefficient normalization",
            "physical coupling lambda",
            "physical V-operator density",
        )
    )
    scope: str = (
        "P13D coefficient normalization and Hermiticity audit only; "
        "no physical V promotion"
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
    exact = _p13c_summary()
    toy = _p13c0_summary()
    if exact["source_formula_status"] == SOURCE_FIXED and exact["exact_formula_identity_status"] == SOURCE_FIXED:
        if toy["status"] == "passed":
            return SOURCE_FIXED
    return FAILED


def _convention_stack_status() -> str:
    p13a = _p13a_summary()
    p7 = _p7_summary()
    exact = _p13c_summary()
    if (
        p13a["readiness_verdict"] == P13_READY_FOR_SYMBOLIC_DERIVATION
        and p7["audit_result"] == "su4_algebra_audit_passed_with_normalization_dependent_yw"
        and bool(p7["hermiticity_verified"])
        and bool(p7["trace_convention_verified"])
        and exact["source_formula_status"] == SOURCE_FIXED
    ):
        return CONVENTION_FIXED
    return FAILED


def _hermiticity_status() -> str:
    p12 = _p12_summary()
    p7 = _p7_summary()
    reduced = _p13c_reduced_summary()
    if (
        p12["hermiticity_status"] == ROBUST
        and bool(p7["hermiticity_verified"])
        and reduced["phase_control_status"] == PHASE_CONVENTION_DEPENDENT
    ):
        return CONVENTION_FIXED
    return FAILED


def _coefficient_scaling_status() -> str:
    reduced = _p13c_reduced_summary()
    if reduced["normalization_control_status"] == P13C_REDUCED_NORMALIZATION_DEPENDENT:
        return NORMALIZATION_DEPENDENT
    return FAILED


def _compatibility_status() -> str:
    p11 = _p11_summary()
    p12 = _p12_summary()
    exact = _p13c_summary()
    if (
        p11["comparison_status"] == MATCHES_FROZEN_SCAFFOLD
        and p12["overall_status"] == ROBUST
        and exact["pattern_status"] == MATCHES_FROZEN_SCAFFOLD
    ):
        return CONVENTION_FIXED
    return FAILED


def _ad_hoc_normalization_status() -> str:
    reduced = _p13c_reduced_summary()
    if (
        reduced["normalization_control_status"] == P13C_REDUCED_NORMALIZATION_DEPENDENT
        and reduced["phase_control_status"] == PHASE_CONVENTION_DEPENDENT
        and reduced["exact_coefficients_status"] == NORMALIZATION_DEPENDENT
    ):
        return CONVENTION_FIXED
    return FAILED


def _lambda_status() -> str:
    reduced = _p13c_reduced_summary()
    return reduced["lambda_status"]


def build_p13d_coefficient_normalization_and_hermiticity_audit() -> P13DCoefficientNormalizationAndHermiticityAudit:
    """Return the current P13D audit contract."""

    p13a = _p13a_summary()
    p13b1 = _p13b1_summary()
    p13c0 = _p13c0_summary()
    p13c = _p13c_summary()
    p11 = _p11_summary()
    p12 = _p12_summary()
    p7 = _p7_summary()
    reduced = _p13c_reduced_summary()

    source_identity_status = _source_identity_status()
    convention_stack_status = _convention_stack_status()
    hermiticity_status = _hermiticity_status()
    coefficient_scaling_status = _coefficient_scaling_status()
    compatibility_status = _compatibility_status()
    ad_hoc_status = _ad_hoc_normalization_status()
    exact_coefficient_status = str(reduced["exact_coefficients_status"])
    exact_normalization_status = str(reduced["absolute_normalization_status"])
    phase_status = PHASE_DEPENDENT if reduced["phase_control_status"] == PHASE_CONVENTION_DEPENDENT else FAILED
    lambda_status = _lambda_status()

    if (
        source_identity_status == SOURCE_FIXED
        and convention_stack_status == CONVENTION_FIXED
        and hermiticity_status == CONVENTION_FIXED
        and coefficient_scaling_status == NORMALIZATION_DEPENDENT
        and compatibility_status == CONVENTION_FIXED
        and ad_hoc_status == CONVENTION_FIXED
        and exact_coefficient_status == NORMALIZATION_DEPENDENT
        and exact_normalization_status == NORMALIZATION_DEPENDENT
    ):
        verdict = NORMALIZATION_DEPENDENT
    elif source_identity_status == FAILED or convention_stack_status == FAILED or hermiticity_status == FAILED:
        verdict = FAILED
    else:
        verdict = BASIS_ORDERING_DEPENDENT if p13c["pattern_status"] != MATCHES_FROZEN_SCAFFOLD else NORMALIZATION_DEPENDENT

    return P13DCoefficientNormalizationAndHermiticityAudit(
        p13a_status=str(p13a["status"]),
        p13b1_status=str(p13b1["status"]),
        p13c0_status=str(p13c0["status"]),
        p13c_status=str(p13c["status"]),
        p11_status=str(p11["status"]),
        p12_status=str(p12["status"]),
        p7_status=str(p7["audit_result"]),
        source_identity_status=source_identity_status,
        convention_stack_status=convention_stack_status,
        hermiticity_status=hermiticity_status,
        coefficient_scaling_status=coefficient_scaling_status,
        p11_p12_compatibility_status=compatibility_status,
        ad_hoc_normalization_status=ad_hoc_status,
        exact_coefficient_status=exact_coefficient_status,
        exact_normalization_status=exact_normalization_status,
        phase_status=phase_status,
        lambda_status=lambda_status,
        verdict=verdict,
    )


def p13d_coefficient_normalization_and_hermiticity_audit_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and tests."""

    audit = build_p13d_coefficient_normalization_and_hermiticity_audit()
    return {
        "status": P13D_COEFFICIENT_NORMALIZATION_AND_HERMITICITY_AUDIT_STATUS,
        "p13a_status": audit.p13a_status,
        "p13b1_status": audit.p13b1_status,
        "p13c0_status": audit.p13c0_status,
        "p13c_status": audit.p13c_status,
        "p11_status": audit.p11_status,
        "p12_status": audit.p12_status,
        "p7_status": audit.p7_status,
        "source_identity_status": audit.source_identity_status,
        "convention_stack_status": audit.convention_stack_status,
        "hermiticity_status": audit.hermiticity_status,
        "coefficient_scaling_status": audit.coefficient_scaling_status,
        "p11_p12_compatibility_status": audit.p11_p12_compatibility_status,
        "ad_hoc_normalization_status": audit.ad_hoc_normalization_status,
        "exact_coefficient_status": audit.exact_coefficient_status,
        "exact_normalization_status": audit.exact_normalization_status,
        "phase_status": audit.phase_status,
        "lambda_status": audit.lambda_status,
        "verdict": audit.verdict,
        "blocking_fields": audit.blocking_fields,
        "scope": audit.scope,
        "forbidden_claims": audit.forbidden_claims,
        "runtime_status": "research_only",
        "v_selection_status": "smoke_only",
        "safe_for_runtime": False,
    }
