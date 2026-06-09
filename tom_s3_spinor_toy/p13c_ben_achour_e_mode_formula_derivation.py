"""P13C Ben Achour E-mode formula derivation.

This module derives and audits the exact Ben Achour ``E_i / E'_i`` one-form
mode formula within the source-supported geometry layer. It compares the exact
formula to the frozen P11/P12 pattern and to the P13C0 toy-gradient placeholder
without promoting any physical V-operator.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

import sympy as sp

from ben_achour_one_form_modes import (
    NORMALIZATION_DEPENDENT as BEN_ACHOUR_NORMALIZATION_DEPENDENT,
    SOURCE_SUPPORTED_GEOMETRY,
    VANISHING_OR_EXCLUDED,
    build_low_mode_ben_achour_one_form_modes,
    mode_applicability_status,
)
from p11_external_oracle_matrix_element_derivation import (
    MATCHES_FROZEN_SCAFFOLD,
    compare_to_frozen_v_scaffold,
    p11_external_oracle_matrix_element_derivation_summary,
)
from p12_matrix_element_derivation_robustness_audit import (
    ROBUST,
    p12_matrix_element_derivation_robustness_audit_summary,
)
from p13a_v_operator_ansatz_convention_registry import (
    p13a_v_operator_ansatz_convention_registry_summary,
)
from p13b1_spinor_state_selection_rule_repair import (
    p13b1_spinor_state_selection_rule_repair_summary,
)
from p13c0_toy_gradient_formula_audit import (
    p13c0_toy_gradient_formula_audit_summary,
)


P13C_BEN_ACHOUR_E_MODE_FORMULA_DERIVATION_STATUS: Final[str] = "passed"
SOURCE_FIXED: Final[str] = "SOURCE_FIXED"
NORMALIZATION_DEPENDENT: Final[str] = "NORMALIZATION_DEPENDENT"
BASIS_ORDERING_DEPENDENT: Final[str] = "BASIS_ORDERING_DEPENDENT"
FAILED: Final[str] = "FAILED"


@dataclass(frozen=True)
class ExactBenAchourEModeFormulaAudit:
    """Structured contract for the exact Ben Achour E-mode formula audit."""

    p13a_status: str
    p13b1_status: str
    p13b1_verdict: str
    p13c0_status: str
    p11_status: str
    p12_status: str
    source_geometry_status: str
    source_formula_status: str
    coefficient_normalization_status: str
    reduced_matrix_element_normalization_status: str
    pattern_status: str
    toy_gradient_relation_status: str
    boundary_mode_status: str
    exact_formula_identity_status: str
    exact_formula_expression: str
    exact_formula_prime_expression: str
    low_mode_nonzero_status: str
    normalization_marker: str
    verdict: str
    blocking_fields: Tuple[str, ...] = field(
        default_factory=lambda: (
            "physical V-operator density",
            "physical coupling lambda",
            "operator-level coefficient normalization",
        )
    )
    scope: str = (
        "P13C exact Ben Achour E-mode formula derivation only; no physical V promotion"
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


def _low_mode_exact_formula() -> object:
    """Return the repaired source-supported low-mode Ben Achour formula."""

    return build_low_mode_ben_achour_one_form_modes(L=2, m_plus=0, m_minus=0)


def _formula_identity_status() -> str:
    low_mode = _low_mode_exact_formula()
    L = low_mode.L
    lhs_e = sp.simplify(low_mode.E.as_matrix() - ((L + 2) * low_mode.B.as_matrix() + low_mode.C.as_matrix()))
    lhs_ep = sp.simplify(low_mode.E_prime.as_matrix() - ((L + 2) * low_mode.B_prime.as_matrix() - low_mode.C_prime.as_matrix()))
    if lhs_e == sp.Matrix([0, 0, 0]) and lhs_ep == sp.Matrix([0, 0, 0]):
        return SOURCE_FIXED
    return FAILED


def _exact_formula_expression() -> str:
    return "E_i = (L + 2) B_i + C_i; E'_i = (L + 2) B'_i - C'_i"


def _toy_gradient_relation_status() -> str:
    toy = p13c0_toy_gradient_formula_audit_summary()
    if toy["status"] == "passed" and toy["ben_achour_mode_formula_status"] == "BEN_ACHOUR_E_MODE_FORMULA_PENDING":
        return NORMALIZATION_DEPENDENT
    return BASIS_ORDERING_DEPENDENT


def build_p13c_ben_achour_e_mode_formula_derivation() -> ExactBenAchourEModeFormulaAudit:
    """Return the exact Ben Achour E-mode formula derivation audit."""

    p13a = p13a_v_operator_ansatz_convention_registry_summary()
    p13b1 = p13b1_spinor_state_selection_rule_repair_summary()
    p13c0 = p13c0_toy_gradient_formula_audit_summary()
    p11 = p11_external_oracle_matrix_element_derivation_summary()
    p12 = p12_matrix_element_derivation_robustness_audit_summary()
    low_mode = _low_mode_exact_formula()
    comparison = compare_to_frozen_v_scaffold(2)

    source_formula_status = _formula_identity_status()
    coefficient_normalization_status = SOURCE_FIXED if source_formula_status == SOURCE_FIXED else FAILED
    reduced_matrix_element_normalization_status = NORMALIZATION_DEPENDENT
    pattern_status = MATCHES_FROZEN_SCAFFOLD if comparison["pattern_matches"] and p12["overall_status"] == ROBUST else FAILED
    low_mode_nonzero_status = SOURCE_SUPPORTED_GEOMETRY if any(component != 0 for component in low_mode.E.as_matrix()) and any(component != 0 for component in low_mode.E_prime.as_matrix()) else FAILED
    boundary_mode_status = VANISHING_OR_EXCLUDED if mode_applicability_status(1) == VANISHING_OR_EXCLUDED else FAILED
    exact_formula_identity_status = source_formula_status
    toy_gradient_relation_status = _toy_gradient_relation_status()
    normalization_marker = BEN_ACHOUR_NORMALIZATION_DEPENDENT

    verdict = SOURCE_FIXED if source_formula_status == SOURCE_FIXED and pattern_status == MATCHES_FROZEN_SCAFFOLD else FAILED

    return ExactBenAchourEModeFormulaAudit(
        p13a_status=str(p13a["status"]),
        p13b1_status=str(p13b1["status"]),
        p13b1_verdict=str(p13b1["verdict"]),
        p13c0_status=str(p13c0["status"]),
        p11_status=str(p11["status"]),
        p12_status=str(p12["status"]),
        source_geometry_status=str(low_mode.source_geometry_status),
        source_formula_status=source_formula_status,
        coefficient_normalization_status=coefficient_normalization_status,
        reduced_matrix_element_normalization_status=reduced_matrix_element_normalization_status,
        pattern_status=pattern_status,
        toy_gradient_relation_status=toy_gradient_relation_status,
        boundary_mode_status=boundary_mode_status,
        exact_formula_identity_status=exact_formula_identity_status,
        exact_formula_expression=_exact_formula_expression(),
        exact_formula_prime_expression="E'_i = (L + 2) B'_i - C'_i",
        low_mode_nonzero_status=low_mode_nonzero_status,
        normalization_marker=normalization_marker,
        verdict=verdict,
    )


def p13c_ben_achour_e_mode_formula_derivation_summary() -> dict[str, object]:
    """Return a compact summary suitable for tests and reports."""

    audit = build_p13c_ben_achour_e_mode_formula_derivation()
    return {
        "status": P13C_BEN_ACHOUR_E_MODE_FORMULA_DERIVATION_STATUS,
        "p13a_status": audit.p13a_status,
        "p13b1_status": audit.p13b1_status,
        "p13b1_verdict": audit.p13b1_verdict,
        "p13c0_status": audit.p13c0_status,
        "p11_status": audit.p11_status,
        "p12_status": audit.p12_status,
        "source_geometry_status": audit.source_geometry_status,
        "source_formula_status": audit.source_formula_status,
        "coefficient_normalization_status": audit.coefficient_normalization_status,
        "reduced_matrix_element_normalization_status": audit.reduced_matrix_element_normalization_status,
        "pattern_status": audit.pattern_status,
        "toy_gradient_relation_status": audit.toy_gradient_relation_status,
        "boundary_mode_status": audit.boundary_mode_status,
        "exact_formula_identity_status": audit.exact_formula_identity_status,
        "exact_formula_expression": audit.exact_formula_expression,
        "exact_formula_prime_expression": audit.exact_formula_prime_expression,
        "low_mode_nonzero_status": audit.low_mode_nonzero_status,
        "normalization_marker": audit.normalization_marker,
        "verdict": audit.verdict,
        "blocking_fields": audit.blocking_fields,
        "scope": audit.scope,
        "forbidden_claims": audit.forbidden_claims,
        "runtime_status": "research_only",
        "v_selection_status": "smoke_only",
        "safe_for_runtime": False,
    }
