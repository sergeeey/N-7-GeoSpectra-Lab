"""P13C0 toy gradient formula audit.

This module audits the toy gradient reduced-element model based on the
``Y_{2,0,0} \propto cos(2 alpha)`` gradient one-form placeholder. It does not
substitute the exact Ben Achour E_i / E'_i co-exact modes and does not
promote a physical V-operator.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache
from typing import Final, Tuple

import sympy as sp

from p13b1_spinor_state_selection_rule_repair import (
    p13b1_spinor_state_selection_rule_repair_summary,
)
from p13b0_state_measure_selection_rule_audit import (
    INVALID_SPINOR_STATE,
    SPINOR_STATE,
    classify_state_tuple,
    states_up_to_kmax,
)


P13C0_TOY_GRADIENT_FORMULA_AUDIT_STATUS: Final[str] = "passed"
TOY_GRADIENT_REDUCED_ELEMENT_DERIVED: Final[str] = "TOY_GRADIENT_REDUCED_ELEMENT_DERIVED"
BEN_ACHOUR_E_MODE_FORMULA_PENDING: Final[str] = "BEN_ACHOUR_E_MODE_FORMULA_PENDING"
LOW_MODE_TABLE_REPAIRED: Final[str] = "LOW_MODE_TABLE_REPAIRED"
NORMALIZATION_DEPENDENT: Final[str] = "NORMALIZATION_DEPENDENT"
ASSUMED_BY_MODEL: Final[str] = "ASSUMED_BY_MODEL"
INCONCLUSIVE: Final[str] = "INCONCLUSIVE"
REQUIRES_PHYSICAL_INPUT: Final[str] = "REQUIRES_PHYSICAL_INPUT"


@dataclass(frozen=True)
class SpinorStateKey:
    k: int
    branch: str
    j_left: float
    m_left: float
    j_right: float
    m_right: float


@dataclass(frozen=True)
class LowModeTableEntry:
    source: SpinorStateKey
    target: SpinorStateKey
    expected: sp.Expr
    note: str


@dataclass(frozen=True)
class P13C0ToyGradientFormulaAudit:
    p13b1_status: str
    p13b1_verdict: str
    state_count_kmax2: int
    state_count_kmax3: int
    lowest_spinor_state_kmax2: SpinorStateKey
    lowest_spinor_state_kmax3: SpinorStateKey
    zero_tuple_classification_spinor: str
    zero_tuple_classification_scalar: str
    j_r_zero_state_valid: bool
    low_mode_table_status: str
    toy_gradient_formula_status: str
    ben_achour_mode_formula_status: str
    selection_rule_j_right_status: str
    selection_rule_j_left_status: str
    normalization_status: str
    low_mode_table_entries: Tuple[LowModeTableEntry, ...]
    low_mode_table_mismatches: Tuple[str, ...]
    verdict: str
    blocking_fields: Tuple[str, ...] = field(
        default_factory=lambda: (
            "exact Ben Achour E_i / E'_i formula",
            "physical V-operator density",
            "physical coupling lambda",
        )
    )
    scope: str = (
        "P13C0 toy-gradient audit only; no physical V promotion, no V-selection promotion"
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


@lru_cache(maxsize=None)
def _states(k_max: int):
    return tuple(states_up_to_kmax(k_max))


def _key_from_state(state) -> SpinorStateKey:
    return SpinorStateKey(
        k=int(state.k),
        branch=str(state.branch),
        j_left=float(state.j_left),
        m_left=float(state.m_left),
        j_right=float(state.j_right),
        m_right=float(state.m_right),
    )


def _toy_gradient_reduced_element(source: SpinorStateKey, target: SpinorStateKey) -> sp.Expr:
    """Toy reduced coefficient for the gradient profile model.

    The model keeps the right-sector labels fixed as an explicit assumption and
    uses a low-mode scalar-profile normalization. It is deliberately not the
    exact Ben Achour E/E' coefficient.
    """

    if source.j_right != target.j_right or source.m_right != target.m_right:
        return sp.Integer(0)
    if source.k != target.k or source.branch != target.branch:
        return sp.Integer(0)
    if source.j_left != target.j_left or source.m_left != target.m_left:
        return sp.Integer(0)
    return -sp.Rational(4 - 2 * source.k, 3)


def _low_mode_table() -> tuple[LowModeTableEntry, ...]:
    states = _states(2)
    source0 = _key_from_state(next(state for state in states if state.k == 0 and state.branch == "positive"))
    source1 = _key_from_state(next(state for state in states if state.k == 1 and state.branch == "positive"))
    return (
        LowModeTableEntry(
            source=source0,
            target=source0,
            expected=-sp.Rational(4, 3),
            note="bug-fixed low-mode coefficient; replaces the broken integer-ratio form",
        ),
        LowModeTableEntry(
            source=source1,
            target=source1,
            expected=-sp.Rational(2, 3),
            note="next repaired low-mode coefficient in the toy gradient profile",
        ),
    )


def full_matrix_element(source: SpinorStateKey, target: SpinorStateKey) -> sp.Expr:
    """Return the toy full matrix element for the gradient model."""

    return _toy_gradient_reduced_element(source, target)


def _table_mismatches(entries: Tuple[LowModeTableEntry, ...]) -> Tuple[str, ...]:
    mismatches: list[str] = []
    for idx, entry in enumerate(entries):
        actual = full_matrix_element(entry.source, entry.target)
        if sp.simplify(actual - entry.expected) != 0:
            mismatches.append(f"entry_{idx}")
    return tuple(mismatches)


def _valid_lowest_spinor_state(k_max: int) -> SpinorStateKey:
    return _key_from_state(_states(k_max)[0])


def build_p13c0_toy_gradient_formula_audit() -> P13C0ToyGradientFormulaAudit:
    """Return the P13C0 toy gradient formula audit contract."""

    p13b1_summary = p13b1_spinor_state_selection_rule_repair_summary()
    states2 = _states(2)
    states3 = _states(3)
    zero_spinor = classify_state_tuple((0.0, 0.0, 0.0, 0.0))
    zero_scalar = classify_state_tuple((0.0, 0.0, 0.0, 0.0), context="scalar")

    low_mode_table = _low_mode_table()
    mismatches = _table_mismatches(low_mode_table)
    j_r_zero_state_valid = classify_state_tuple((0.5, -0.5, 0.0, 0.0)) == SPINOR_STATE

    toy_gradient_formula_status = TOY_GRADIENT_REDUCED_ELEMENT_DERIVED
    ben_achour_mode_formula_status = BEN_ACHOUR_E_MODE_FORMULA_PENDING
    low_mode_table_status = LOW_MODE_TABLE_REPAIRED if not mismatches else INCONCLUSIVE
    selection_rule_j_right_status = ASSUMED_BY_MODEL
    selection_rule_j_left_status = TOY_GRADIENT_REDUCED_ELEMENT_DERIVED
    normalization_status = NORMALIZATION_DEPENDENT

    verdict = NORMALIZATION_DEPENDENT
    if zero_spinor == INVALID_SPINOR_STATE and low_mode_table_status == LOW_MODE_TABLE_REPAIRED:
        verdict = NORMALIZATION_DEPENDENT
    elif mismatches:
        verdict = INCONCLUSIVE

    return P13C0ToyGradientFormulaAudit(
        p13b1_status=str(p13b1_summary["status"]),
        p13b1_verdict=str(p13b1_summary["verdict"]),
        state_count_kmax2=len(states2),
        state_count_kmax3=len(states3),
        lowest_spinor_state_kmax2=_valid_lowest_spinor_state(2),
        lowest_spinor_state_kmax3=_valid_lowest_spinor_state(3),
        zero_tuple_classification_spinor=zero_spinor,
        zero_tuple_classification_scalar=zero_scalar,
        j_r_zero_state_valid=j_r_zero_state_valid,
        low_mode_table_status=low_mode_table_status,
        toy_gradient_formula_status=toy_gradient_formula_status,
        ben_achour_mode_formula_status=ben_achour_mode_formula_status,
        selection_rule_j_right_status=selection_rule_j_right_status,
        selection_rule_j_left_status=selection_rule_j_left_status,
        normalization_status=normalization_status,
        low_mode_table_entries=low_mode_table,
        low_mode_table_mismatches=mismatches,
        verdict=verdict,
    )


def p13c0_toy_gradient_formula_audit_summary() -> dict[str, object]:
    """Return a compact summary suitable for reports and tests."""

    audit = build_p13c0_toy_gradient_formula_audit()
    return {
        "status": P13C0_TOY_GRADIENT_FORMULA_AUDIT_STATUS,
        "p13b1_status": audit.p13b1_status,
        "p13b1_verdict": audit.p13b1_verdict,
        "state_count_kmax2": audit.state_count_kmax2,
        "state_count_kmax3": audit.state_count_kmax3,
        "lowest_spinor_state_kmax2": audit.lowest_spinor_state_kmax2,
        "lowest_spinor_state_kmax3": audit.lowest_spinor_state_kmax3,
        "zero_tuple_classification_spinor": audit.zero_tuple_classification_spinor,
        "zero_tuple_classification_scalar": audit.zero_tuple_classification_scalar,
        "j_r_zero_state_valid": audit.j_r_zero_state_valid,
        "low_mode_table_status": audit.low_mode_table_status,
        "toy_gradient_formula_status": audit.toy_gradient_formula_status,
        "ben_achour_mode_formula_status": audit.ben_achour_mode_formula_status,
        "selection_rule_j_right_status": audit.selection_rule_j_right_status,
        "selection_rule_j_left_status": audit.selection_rule_j_left_status,
        "normalization_status": audit.normalization_status,
        "low_mode_table_entries": audit.low_mode_table_entries,
        "low_mode_table_mismatches": audit.low_mode_table_mismatches,
        "verdict": audit.verdict,
        "blocking_fields": audit.blocking_fields,
        "scope": audit.scope,
        "forbidden_claims": audit.forbidden_claims,
        "runtime_status": "research_only",
        "v_selection_status": "smoke_only",
        "safe_for_runtime": False,
    }
