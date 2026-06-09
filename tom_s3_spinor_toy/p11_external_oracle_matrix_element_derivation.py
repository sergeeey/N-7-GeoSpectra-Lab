"""P11 external-oracle matrix-element derivation.

This module builds an independent symbolic selection-pattern oracle from
classic Wigner-D / Clebsch-Gordan / Wigner-Eckart machinery and compares it to
the frozen P9/P10 matrix-element scaffold. It does not promote V-selection
rules and does not claim Standard Model or fermion-generation results.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import math
from typing import Final, Tuple

import numpy as np
from sympy import S
from sympy.physics.wigner import clebsch_gordan

from p10_selection_rule_matrix_element_review import (
    p10_selection_rule_matrix_element_review_summary,
)
from p9_matrix_element_selection_rules import p9_matrix_element_selection_rules_summary
from s3_coupling_v_option_b import build_v_symbolic, expand_spectral_basis_states


P11_EXTERNAL_ORACLE_MATRIX_ELEMENT_DERIVATION_STATUS: Final[str] = "passed"
RUNTIME_STATUS: Final[str] = "research_only"
V_SELECTION_STATUS: Final[str] = "smoke_only"
SAFE_FOR_RUNTIME: Final[bool] = False

EXTERNAL_ORACLE_DERIVED: Final[str] = "EXTERNAL_ORACLE_DERIVED"
MATCHES_FROZEN_SCAFFOLD: Final[str] = "MATCHES_FROZEN_SCAFFOLD"
MISMATCHES_FROZEN_SCAFFOLD: Final[str] = "MISMATCHES_FROZEN_SCAFFOLD"
BASIS_ORDERING_DEPENDENT: Final[str] = "BASIS_ORDERING_DEPENDENT"
NORMALIZATION_DEPENDENT: Final[str] = "NORMALIZATION_DEPENDENT"
REQUIRES_PHYSICAL_INPUT: Final[str] = "REQUIRES_PHYSICAL_INPUT"
SMOKE_ONLY: Final[str] = "SMOKE_ONLY"


def _as_rational_half(value: float) -> S:
    return S(int(round(2 * value))) / 2


def _selection_allowed_raw(source, target) -> bool:
    if abs(target.j_right - source.j_right) > 1e-12:
        return False
    if abs(target.m_right - source.m_right) > 1e-12:
        return False
    if source.j_left == 0.0 and target.j_left == 0.0:
        return False
    if abs(target.j_left - source.j_left) > 1.0 + 1e-12:
        return False
    q_left = target.m_left - source.m_left
    if q_left not in {-1.0, 0.0, 1.0}:
        return False
    coefficient = clebsch_gordan(
        _as_rational_half(source.j_left),
        S(1),
        _as_rational_half(target.j_left),
        _as_rational_half(source.m_left),
        _as_rational_half(q_left),
        _as_rational_half(target.m_left),
    )
    return bool(coefficient != 0)


def _external_oracle_oriented_coefficient(source, target) -> complex:
    """Return the oriented Wigner-Eckart coefficient for the external oracle.

    The goal is not to re-import the frozen Option-B scaffold, but to recover
    the same nonzero pattern and cancellation structure from standard
    Clebsch-Gordan selection rules plus the positive reduced factor implied by
    the Wigner-Eckart decomposition.
    """

    if abs(target.j_right - source.j_right) > 1e-12:
        return 0.0 + 0.0j
    if abs(target.m_right - source.m_right) > 1e-12:
        return 0.0 + 0.0j
    if source.j_left == 0.0 and target.j_left == 0.0:
        return 0.0 + 0.0j
    if abs(target.j_left - source.j_left) > 1.0 + 1e-12:
        return 0.0 + 0.0j

    q_left = target.m_left - source.m_left
    if q_left not in {-1.0, 0.0, 1.0}:
        return 0.0 + 0.0j

    coefficient = clebsch_gordan(
        _as_rational_half(source.j_left),
        S(1),
        _as_rational_half(target.j_left),
        _as_rational_half(source.m_left),
        _as_rational_half(q_left),
        _as_rational_half(target.m_left),
    )
    if coefficient == 0:
        return 0.0 + 0.0j

    left_factor = math.sqrt(
        (2.0 * source.j_left + 1.0) * 3.0 / (2.0 * target.j_left + 1.0)
    )
    right_factor = math.sqrt(
        (2.0 * source.j_right + 1.0) / (2.0 * target.j_right + 1.0)
    )
    return complex(float(left_factor * right_factor) * complex(coefficient.evalf()))


def build_external_oracle_raw_pattern(k_max: int) -> tuple[np.ndarray, list[object]]:
    """Build the oriented symbolic coefficient matrix from Wigner/CG rules."""

    states = expand_spectral_basis_states(k_max=k_max)
    n = len(states)
    raw = np.zeros((n, n), dtype=complex)
    for source in states:
        for target in states:
            coefficient = _external_oracle_oriented_coefficient(source, target)
            if coefficient != 0.0:
                raw[target.index, source.index] = coefficient
    return raw, states


def build_external_oracle_selection_pattern(k_max: int) -> tuple[np.ndarray, list[object]]:
    """Return the Hermitianized selection pattern from the external oracle."""

    raw, states = build_external_oracle_raw_pattern(k_max=k_max)
    hermitian = (raw + raw.conjugate().T) / 2.0
    return hermitian, states


def compare_to_frozen_v_scaffold(k_max: int) -> dict[str, object]:
    """Compare the external oracle selection pattern to the frozen scaffold."""

    oracle_pattern, states = build_external_oracle_selection_pattern(k_max=k_max)
    frozen = build_v_symbolic(k_max=k_max)
    oracle_mask = np.abs(oracle_pattern) > 0
    frozen_mask = np.abs(frozen) > 0
    same_shape = oracle_pattern.shape == frozen.shape
    same_pattern = bool(same_shape and np.array_equal(oracle_mask, frozen_mask))
    hermitian_compatible = bool(
        np.allclose(oracle_pattern, oracle_pattern.conjugate().T, atol=1e-12)
        and np.allclose(frozen, frozen.conjugate().T, atol=1e-12)
    )
    return {
        "k_max": k_max,
        "shape": oracle_pattern.shape,
        "same_shape": same_shape,
        "pattern_matches": same_pattern,
        "hermitian_compatible": hermitian_compatible,
        "oracle_nonzero": int(np.count_nonzero(oracle_mask)),
        "frozen_nonzero": int(np.count_nonzero(frozen_mask)),
        "states": states,
        "oracle_mask": oracle_mask,
        "frozen_mask": frozen_mask,
    }


@dataclass(frozen=True)
class P11ExternalOracleMatrixElementDerivation:
    """Structured derivation probe for matrix-element selection patterns."""

    p10_status: str
    p9_status: str
    k_max_results: Tuple[Tuple[int, str], ...]
    external_oracle_status: str
    comparison_status: str
    basis_ordering_status: str
    normalization_status: str
    physical_input_status: str
    smoke_only_status: str
    exact_coefficients_status: str
    comparison_by_k: Tuple[Tuple[int, bool, bool, int, int], ...]
    selection_rule_status: str
    audit_result: str
    scope: str
    forbidden_claims: Tuple[str, ...] = field(
        default_factory=lambda: (
            "full fermion generation claim",
            "Standard Model reproduced claim",
            "V-selection promotion",
            "safe_for_runtime promotion",
            "ad hoc basis permutation",
            "ad hoc phase patch",
            "ad hoc normalization patch",
        )
    )


def build_p11_external_oracle_matrix_element_derivation() -> P11ExternalOracleMatrixElementDerivation:
    """Return the current P11 external-oracle derivation contract."""

    p9_summary = p9_matrix_element_selection_rules_summary()
    p10_summary = p10_selection_rule_matrix_element_review_summary()
    comparisons = [compare_to_frozen_v_scaffold(k_max=k) for k in (1, 2)]
    comparison_by_k = tuple(
        (
            c["k_max"],
            bool(c["pattern_matches"]),
            bool(c["hermitian_compatible"]),
            int(c["oracle_nonzero"]),
            int(c["frozen_nonzero"]),
        )
        for c in comparisons
    )
    overall_match = all(c["pattern_matches"] for c in comparisons)
    comparison_status = MATCHES_FROZEN_SCAFFOLD if overall_match else MISMATCHES_FROZEN_SCAFFOLD
    audit_result = (
        "external_oracle_matches_frozen_scaffold_without_promotion"
        if overall_match
        else "external_oracle_mismatch_requires_basis_or_operator_review"
    )
    return P11ExternalOracleMatrixElementDerivation(
        p10_status=str(p10_summary["status"]),
        p9_status=str(p9_summary["status"]),
        k_max_results=tuple((c["k_max"], comparison_status) for c in comparisons),
        external_oracle_status=EXTERNAL_ORACLE_DERIVED,
        comparison_status=comparison_status,
        basis_ordering_status=BASIS_ORDERING_DEPENDENT,
        normalization_status=NORMALIZATION_DEPENDENT,
        physical_input_status=REQUIRES_PHYSICAL_INPUT,
        smoke_only_status=SMOKE_ONLY,
        exact_coefficients_status=NORMALIZATION_DEPENDENT,
        comparison_by_k=comparison_by_k,
        selection_rule_status="smoke_only",
        audit_result=audit_result,
        scope=(
            "P11 external-oracle matrix-element derivation only; no V promotion, "
            "no fermion-generation claim, no Standard Model claim"
        ),
    )


def p11_external_oracle_matrix_element_derivation_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and tests."""

    derivation = build_p11_external_oracle_matrix_element_derivation()
    return {
        "p10_status": derivation.p10_status,
        "p9_status": derivation.p9_status,
        "k_max_results": derivation.k_max_results,
        "external_oracle_status": derivation.external_oracle_status,
        "comparison_status": derivation.comparison_status,
        "basis_ordering_status": derivation.basis_ordering_status,
        "normalization_status": derivation.normalization_status,
        "physical_input_status": derivation.physical_input_status,
        "smoke_only_status": derivation.smoke_only_status,
        "exact_coefficients_status": derivation.exact_coefficients_status,
        "comparison_by_k": derivation.comparison_by_k,
        "selection_rule_status": derivation.selection_rule_status,
        "audit_result": derivation.audit_result,
        "scope": derivation.scope,
        "forbidden_claims": derivation.forbidden_claims,
        "status": P11_EXTERNAL_ORACLE_MATRIX_ELEMENT_DERIVATION_STATUS,
        "runtime_status": RUNTIME_STATUS,
        "v_selection_status": V_SELECTION_STATUS,
        "safe_for_runtime": SAFE_FOR_RUNTIME,
    }
