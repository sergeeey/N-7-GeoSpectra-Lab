"""P13B symbolic V matrix-element pattern build.

This module builds a symbolic zero/nonzero matrix-element pattern for the
candidate S3 V-like ansatz using the frozen P13A/P13A1 geometry and compares
it against the frozen P11/P12 scaffold/oracle pattern. It does not claim a
physical V-operator, does not promote V-selection rules, and does not compare
exact coefficients as physical values.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

import numpy as np
import sympy as sp
from sympy.physics.wigner import clebsch_gordan

from ben_achour_one_form_modes import (
    build_low_mode_ben_achour_one_form_modes,
)
from p11_external_oracle_matrix_element_derivation import (
    compare_to_frozen_v_scaffold,
    p11_external_oracle_matrix_element_derivation_summary,
)
from p12_matrix_element_derivation_robustness_audit import (
    p12_matrix_element_derivation_robustness_audit_summary,
)
from p13a_v_operator_ansatz_convention_registry import (
    p13a_v_operator_ansatz_convention_registry_summary,
)
from s3_coupling_v_option_b import expand_spectral_basis_states


P13B_SYMBOLIC_V_MATRIX_ELEMENT_PATTERN_BUILD_STATUS: Final[str] = "passed"
SYMBOLIC_PATTERN_MATCHES_P11_P12: Final[str] = "SYMBOLIC_PATTERN_MATCHES_P11_P12"
SYMBOLIC_PATTERN_PARTIAL_MATCH: Final[str] = "SYMBOLIC_PATTERN_PARTIAL_MATCH"
SYMBOLIC_PATTERN_MISMATCH: Final[str] = "SYMBOLIC_PATTERN_MISMATCH"
NORMALIZATION_DEPENDENT: Final[str] = "NORMALIZATION_DEPENDENT"
REQUIRES_PHYSICAL_INPUT: Final[str] = "REQUIRES_PHYSICAL_INPUT"
INCONCLUSIVE: Final[str] = "INCONCLUSIVE"
SMOKE_ONLY: Final[str] = "SMOKE_ONLY"


def _as_rational_half(value: float) -> sp.Rational:
    return sp.Rational(int(round(2 * value)), 2)


def _selection_allowed(source, target) -> bool:
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
        sp.Integer(1),
        _as_rational_half(target.j_left),
        _as_rational_half(source.m_left),
        _as_rational_half(q_left),
        _as_rational_half(target.m_left),
    )
    return bool(coefficient != 0)


def _symbolic_oriented_coefficient(source, target) -> sp.Expr:
    """Return a symbolic oriented matrix element for the candidate ansatz."""

    if not _selection_allowed(source, target):
        return sp.Integer(0)

    coefficient = clebsch_gordan(
        _as_rational_half(source.j_left),
        sp.Integer(1),
        _as_rational_half(target.j_left),
        _as_rational_half(source.m_left),
        _as_rational_half(target.m_left - source.m_left),
        _as_rational_half(target.m_left),
    )
    if coefficient == 0:
        return sp.Integer(0)

    reduced_key = tuple(sorted((source.index, target.index)))
    reduced = sp.Symbol(f"vred_{reduced_key[0]}_{reduced_key[1]}", real=True)
    left_factor = sp.sqrt(
        sp.Rational(int(round(2 * source.j_left)) + 1, 1)
        * sp.Integer(3)
        / sp.Rational(int(round(2 * target.j_left)) + 1, 1)
    )
    right_factor = sp.sqrt(
        sp.Rational(int(round(2 * source.j_right)) + 1, 1)
        / sp.Rational(int(round(2 * target.j_right)) + 1, 1)
    )
    return sp.simplify(reduced * left_factor * right_factor * coefficient)


def build_symbolic_v_raw_pattern(k_max: int) -> tuple[sp.Matrix, list[object], np.ndarray]:
    """Build the oriented symbolic coefficient matrix before Hermitianization."""

    states = expand_spectral_basis_states(k_max=k_max)
    size = len(states)
    raw = sp.MutableDenseMatrix.zeros(size, size)
    mask = np.zeros((size, size), dtype=bool)
    for source in states:
        for target in states:
            entry = _symbolic_oriented_coefficient(source, target)
            if entry != 0:
                raw[target.index, source.index] = entry
                mask[target.index, source.index] = True
    return sp.Matrix(raw), states, mask


def build_symbolic_v_selection_pattern(k_max: int) -> tuple[sp.Matrix, list[object], np.ndarray]:
    """Return the Hermitianized symbolic selection pattern and its mask."""

    raw, states, raw_mask = build_symbolic_v_raw_pattern(k_max=k_max)
    hermitian = sp.Matrix((raw + raw.conjugate().T) / 2)
    hermitian_mask = np.zeros(raw_mask.shape, dtype=bool)
    for i in range(hermitian.rows):
        for j in range(hermitian.cols):
            hermitian_mask[i, j] = sp.simplify(hermitian[i, j]) != 0
    return hermitian, states, hermitian_mask


def compare_symbolic_pattern_to_frozen_scaffold(k_max: int) -> dict[str, object]:
    """Compare the symbolic ansatz pattern to the frozen P11/P12 scaffold."""

    symbolic_pattern, states, symbolic_mask = build_symbolic_v_selection_pattern(k_max=k_max)
    oracle_comparison = compare_to_frozen_v_scaffold(k_max=k_max)
    oracle_mask = oracle_comparison["oracle_mask"]
    frozen_mask = oracle_comparison["frozen_mask"]

    same_shape = bool(
        symbolic_pattern.shape == oracle_mask.shape == frozen_mask.shape
    )
    matches_oracle = bool(same_shape and np.array_equal(symbolic_mask, oracle_mask))
    matches_frozen = bool(same_shape and np.array_equal(symbolic_mask, frozen_mask))
    hermitian_compatible = bool(
        all(
            sp.simplify(symbolic_pattern[i, j] - symbolic_pattern.conjugate().T[i, j]) == 0
            for i in range(symbolic_pattern.rows)
            for j in range(symbolic_pattern.cols)
        )
        and oracle_comparison["hermitian_compatible"]
    )

    return {
        "k_max": k_max,
        "shape": symbolic_pattern.shape,
        "same_shape": same_shape,
        "pattern_matches_oracle": matches_oracle,
        "pattern_matches_frozen": matches_frozen,
        "pattern_matches": bool(matches_oracle and matches_frozen),
        "hermitian_compatible": hermitian_compatible,
        "symbolic_nonzero": int(np.count_nonzero(symbolic_mask)),
        "oracle_nonzero": int(oracle_comparison["oracle_nonzero"]),
        "frozen_nonzero": int(oracle_comparison["frozen_nonzero"]),
        "states": states,
        "symbolic_mask": symbolic_mask,
        "oracle_mask": oracle_mask,
        "frozen_mask": frozen_mask,
        "symbolic_pattern": symbolic_pattern,
    }


def _low_mode_geometry_probe() -> dict[str, object]:
    """Return the low-mode Ben Achour geometry probe used by this gate."""

    low_mode = build_low_mode_ben_achour_one_form_modes(L=2, m_plus=0, m_minus=0)
    return {
        "status": low_mode.readiness_verdict,
        "source_geometry_status": low_mode.source_geometry_status,
        "normalization_status": low_mode.normalization_status,
        "mode_applicability_status": low_mode.mode_applicability_status,
        "E_nonzero": any(component != 0 for component in low_mode.E.as_matrix()),
        "E_prime_nonzero": any(component != 0 for component in low_mode.E_prime.as_matrix()),
        "blocking_fields": low_mode.blocking_fields,
    }


@dataclass(frozen=True)
class P13BSymbolicVMatrixElementPatternBuild:
    """Structured contract for the P13B symbolic pattern build."""

    p13a_status: str
    p13a1_status: str
    p11_status: str
    p12_status: str
    low_mode_geometry_status: str
    low_mode_normalization_status: str
    low_mode_verdict: str
    exact_coefficients_status: str
    symbolic_pattern_status: str
    comparison_status: str
    hermiticity_status: str
    p11_p12_alignment_status: str
    comparison_by_k: Tuple[Tuple[int, str, bool, bool, int, int], ...]
    selection_rule_status: str
    audit_result: str
    scope: str
    forbidden_claims: Tuple[str, ...] = field(
        default_factory=lambda: (
            "physical V-operator derivation",
            "V-selection promotion",
            "Standard Model reproduced claim",
            "fermion generation claim",
            "safe_for_runtime promotion",
            "exact coefficient physical value claim",
        )
    )


def build_p13b_symbolic_v_matrix_element_pattern_build() -> P13BSymbolicVMatrixElementPatternBuild:
    """Return the current P13B symbolic pattern build contract."""

    p11_summary = p11_external_oracle_matrix_element_derivation_summary()
    p12_summary = p12_matrix_element_derivation_robustness_audit_summary()
    p13a_summary = p13a_v_operator_ansatz_convention_registry_summary()
    low_mode_probe = _low_mode_geometry_probe()

    comparisons = [compare_symbolic_pattern_to_frozen_scaffold(k_max=k) for k in (1, 2, 3)]
    comparison_by_k = tuple(
        (
            c["k_max"],
            SYMBOLIC_PATTERN_MATCHES_P11_P12 if c["pattern_matches"] else SYMBOLIC_PATTERN_MISMATCH,
            bool(c["same_shape"]),
            bool(c["hermitian_compatible"]),
            int(c["symbolic_nonzero"]),
            int(c["oracle_nonzero"]),
        )
        for c in comparisons
    )

    all_match = all(c["pattern_matches"] for c in comparisons)
    any_match = any(c["pattern_matches"] for c in comparisons)
    all_hermitian = all(c["hermitian_compatible"] for c in comparisons)

    if all_match and all_hermitian:
        symbolic_status = SYMBOLIC_PATTERN_MATCHES_P11_P12
    elif any_match:
        symbolic_status = SYMBOLIC_PATTERN_PARTIAL_MATCH
    else:
        symbolic_status = SYMBOLIC_PATTERN_MISMATCH

    p11_p12_alignment_status = (
        SYMBOLIC_PATTERN_MATCHES_P11_P12
        if p11_summary["comparison_status"] == "MATCHES_FROZEN_SCAFFOLD"
        and p12_summary["overall_status"] == "ROBUST"
        else SYMBOLIC_PATTERN_PARTIAL_MATCH
    )

    return P13BSymbolicVMatrixElementPatternBuild(
        p13a_status=str(p13a_summary["status"]),
        p13a1_status=str(low_mode_probe["status"]),
        p11_status=str(p11_summary["status"]),
        p12_status=str(p12_summary["status"]),
        low_mode_geometry_status=str(low_mode_probe["source_geometry_status"]),
        low_mode_normalization_status=str(low_mode_probe["normalization_status"]),
        low_mode_verdict=str(low_mode_probe["status"]),
        exact_coefficients_status=NORMALIZATION_DEPENDENT,
        symbolic_pattern_status=symbolic_status,
        comparison_status=symbolic_status,
        hermiticity_status=SYMBOLIC_PATTERN_MATCHES_P11_P12 if all_hermitian else SYMBOLIC_PATTERN_MISMATCH,
        p11_p12_alignment_status=p11_p12_alignment_status,
        comparison_by_k=comparison_by_k,
        selection_rule_status=SMOKE_ONLY,
        audit_result=(
            "symbolic_pattern_matches_p11_p12_without_promotion"
            if symbolic_status == SYMBOLIC_PATTERN_MATCHES_P11_P12
            else "symbolic_pattern_partial_match_requires_review"
            if symbolic_status == SYMBOLIC_PATTERN_PARTIAL_MATCH
            else "symbolic_pattern_mismatch_requires_repair"
        ),
        scope=(
            "P13B symbolic pattern build only; no physical V promotion, no exact "
            "physical coefficient claims, no Standard Model claim"
        ),
    )


def p13b_symbolic_v_matrix_element_pattern_build_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and tests."""

    build = build_p13b_symbolic_v_matrix_element_pattern_build()
    return {
        "p13a_status": build.p13a_status,
        "p13a1_status": build.p13a1_status,
        "p11_status": build.p11_status,
        "p12_status": build.p12_status,
        "low_mode_geometry_status": build.low_mode_geometry_status,
        "low_mode_normalization_status": build.low_mode_normalization_status,
        "low_mode_verdict": build.low_mode_verdict,
        "exact_coefficients_status": build.exact_coefficients_status,
        "symbolic_pattern_status": build.symbolic_pattern_status,
        "comparison_status": build.comparison_status,
        "hermiticity_status": build.hermiticity_status,
        "p11_p12_alignment_status": build.p11_p12_alignment_status,
        "comparison_by_k": build.comparison_by_k,
        "selection_rule_status": build.selection_rule_status,
        "audit_result": build.audit_result,
        "scope": build.scope,
        "forbidden_claims": build.forbidden_claims,
        "status": P13B_SYMBOLIC_V_MATRIX_ELEMENT_PATTERN_BUILD_STATUS,
        "runtime_status": "research_only",
        "v_selection_status": "smoke_only",
        "safe_for_runtime": False,
    }
