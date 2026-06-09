"""P13E reduced coefficient scale fixing or no-go audit.

This module determines whether the unresolved reduced coefficient scale in the
Ben Achour E_i / E'_i V-like derivation can be fixed from the existing source
identities and conventions, or whether the scale remains a no-go / free
coupling parameter.

It does not promote physical V-selection rules.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache
from typing import Final, Tuple

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
from p13d_coefficient_normalization_and_hermiticity_audit import (
    CONVENTION_FIXED,
    NORMALIZATION_DEPENDENT,
    p13d_coefficient_normalization_and_hermiticity_audit_summary,
)
from su4_hypercharge_gauge_breaking_audit import su4_hypercharge_gauge_audit_summary


P13E_REDUCED_COEFFICIENT_SCALE_FIXING_OR_NO_GO_STATUS: Final[str] = "passed"
FREE_COUPLING_PARAMETER: Final[str] = "FREE_COUPLING_PARAMETER"
NORMALIZATION_DEPENDENT_NO_GO: Final[str] = "NORMALIZATION_DEPENDENT_NO_GO"
FAILED: Final[str] = "FAILED"


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
def _p11_summary() -> dict[str, object]:
    return p11_external_oracle_matrix_element_derivation_summary()


@lru_cache(maxsize=1)
def _p12_summary() -> dict[str, object]:
    return p12_matrix_element_derivation_robustness_audit_summary()


@lru_cache(maxsize=1)
def _p7_summary() -> dict[str, object]:
    return su4_hypercharge_gauge_audit_summary()


@dataclass(frozen=True)
class P13EReducedCoefficientScaleAudit:
    """Structured contract for the P13E scale-fixing / no-go audit."""

    p13a_status: str
    p13b1_status: str
    p13c_status: str
    p13d_status: str
    p11_status: str
    p12_status: str
    p7_status: str
    source_identity_status: str
    convention_stack_status: str
    hermiticity_status: str
    pattern_compatibility_status: str
    scale_fix_status: str
    coupling_parameter_status: str
    normalization_status: str
    verdict: str
    blocking_fields: Tuple[str, ...] = field(
        default_factory=lambda: (
            "free coupling lambda",
            "exact reduced coefficient normalization",
            "physical V-operator density",
        )
    )
    scope: str = (
        "P13E reduced coefficient scale fixing or no-go audit only; "
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
    p13c = _p13c_summary()
    p13d = _p13d_summary()
    if (
        p13c["source_formula_status"] == SOURCE_FIXED
        and p13c["exact_formula_identity_status"] == SOURCE_FIXED
        and p13d["source_identity_status"] == SOURCE_FIXED
    ):
        return SOURCE_FIXED
    return FAILED


def _convention_stack_status() -> str:
    p13a = _p13a_summary()
    p13d = _p13d_summary()
    p7 = _p7_summary()
    if (
        p13a["readiness_verdict"] == P13_READY_FOR_SYMBOLIC_DERIVATION
        and p13d["convention_stack_status"] == CONVENTION_FIXED
        and p7["audit_result"] == "su4_algebra_audit_passed_with_normalization_dependent_yw"
    ):
        return CONVENTION_FIXED
    return FAILED


def _hermiticity_status() -> str:
    p12 = _p12_summary()
    p13d = _p13d_summary()
    p7 = _p7_summary()
    if (
        p12["hermiticity_status"] == ROBUST
        and p13d["hermiticity_status"] == CONVENTION_FIXED
        and bool(p7["hermiticity_verified"])
    ):
        return CONVENTION_FIXED
    return FAILED


def _pattern_compatibility_status() -> str:
    p11 = _p11_summary()
    p12 = _p12_summary()
    p13d = _p13d_summary()
    if (
        p11["comparison_status"] == MATCHES_FROZEN_SCAFFOLD
        and p12["overall_status"] == ROBUST
        and p13d["p11_p12_compatibility_status"] == CONVENTION_FIXED
    ):
        return CONVENTION_FIXED
    return FAILED


def _coupling_parameter_status() -> str:
    p13d = _p13d_summary()
    if p13d["lambda_status"] == "REQUIRES_PHYSICAL_COUPLING_INPUT":
        return FREE_COUPLING_PARAMETER
    return FAILED


def _scale_fix_status() -> str:
    p13d = _p13d_summary()
    if (
        p13d["exact_coefficient_status"] == NORMALIZATION_DEPENDENT
        and p13d["exact_normalization_status"] == NORMALIZATION_DEPENDENT
        and p13d["coefficient_scaling_status"] == NORMALIZATION_DEPENDENT
    ):
        return NORMALIZATION_DEPENDENT_NO_GO
    return SOURCE_FIXED


def build_p13e_reduced_coefficient_scale_audit() -> P13EReducedCoefficientScaleAudit:
    """Return the current P13E scale audit contract."""

    p13a = _p13a_summary()
    p13b1 = _p13b1_summary()
    p13c = _p13c_summary()
    p13d = _p13d_summary()
    p11 = _p11_summary()
    p12 = _p12_summary()
    p7 = _p7_summary()

    source_identity_status = _source_identity_status()
    convention_stack_status = _convention_stack_status()
    hermiticity_status = _hermiticity_status()
    pattern_compatibility_status = _pattern_compatibility_status()
    coupling_parameter_status = _coupling_parameter_status()
    scale_fix_status = _scale_fix_status()
    normalization_status = p13d["coefficient_scaling_status"]

    if scale_fix_status == SOURCE_FIXED:
        verdict = SOURCE_FIXED
    elif scale_fix_status == CONVENTION_FIXED:
        verdict = CONVENTION_FIXED
    elif scale_fix_status == NORMALIZATION_DEPENDENT_NO_GO:
        verdict = NORMALIZATION_DEPENDENT_NO_GO
    else:
        verdict = FAILED

    return P13EReducedCoefficientScaleAudit(
        p13a_status=str(p13a["status"]),
        p13b1_status=str(p13b1["status"]),
        p13c_status=str(p13c["status"]),
        p13d_status=str(p13d["status"]),
        p11_status=str(p11["status"]),
        p12_status=str(p12["status"]),
        p7_status=str(p7["audit_result"]),
        source_identity_status=source_identity_status,
        convention_stack_status=convention_stack_status,
        hermiticity_status=hermiticity_status,
        pattern_compatibility_status=pattern_compatibility_status,
        scale_fix_status=scale_fix_status,
        coupling_parameter_status=coupling_parameter_status,
        normalization_status=normalization_status,
        verdict=verdict,
    )


def p13e_reduced_coefficient_scale_audit_summary() -> dict[str, object]:
    """Return a compact summary suitable for tests and reports."""

    audit = build_p13e_reduced_coefficient_scale_audit()
    return {
        "status": P13E_REDUCED_COEFFICIENT_SCALE_FIXING_OR_NO_GO_STATUS,
        "p13a_status": audit.p13a_status,
        "p13b1_status": audit.p13b1_status,
        "p13c_status": audit.p13c_status,
        "p13d_status": audit.p13d_status,
        "p11_status": audit.p11_status,
        "p12_status": audit.p12_status,
        "p7_status": audit.p7_status,
        "source_identity_status": audit.source_identity_status,
        "convention_stack_status": audit.convention_stack_status,
        "hermiticity_status": audit.hermiticity_status,
        "pattern_compatibility_status": audit.pattern_compatibility_status,
        "scale_fix_status": audit.scale_fix_status,
        "coupling_parameter_status": audit.coupling_parameter_status,
        "normalization_status": audit.normalization_status,
        "verdict": audit.verdict,
        "blocking_fields": audit.blocking_fields,
        "scope": audit.scope,
        "forbidden_claims": audit.forbidden_claims,
        "runtime_status": "research_only",
        "v_selection_status": "smoke_only",
        "safe_for_runtime": False,
    }
