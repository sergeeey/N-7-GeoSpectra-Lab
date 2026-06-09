"""P13B1 spinor-state and selection-rule repair.

This module repairs the spinor-state basis assumptions before any coefficient
normalization audit. It inspects the current spinor state labels, removes the
scalar tuple from spinor tests, and audits the current gamma^a A_a selection
rules against the frozen P11/P12 symbolic scaffold.

It does not promote a physical V-operator and does not proceed to P13C.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

from p11_external_oracle_matrix_element_derivation import compare_to_frozen_v_scaffold, p11_external_oracle_matrix_element_derivation_summary
from p12_matrix_element_derivation_robustness_audit import p12_matrix_element_derivation_robustness_audit_summary
from p13b0_state_measure_selection_rule_audit import (
    INVALID_SPINOR_STATE,
    SPINOR_STATE,
    classify_state_tuple,
    states_up_to_kmax,
)


P13B1_SPINOR_STATE_AND_SELECTION_RULE_REPAIR_STATUS: Final[str] = "passed"
P13B_READY_FOR_RERUN: Final[str] = "P13B_READY_FOR_RERUN"
P13B_PATTERN_STILL_VALID: Final[str] = "P13B_PATTERN_STILL_VALID"
P13B_PATTERN_REQUIRES_REPAIR: Final[str] = "P13B_PATTERN_REQUIRES_REPAIR"
BLOCKED_BY_SPINOR_BASIS_CONVENTION: Final[str] = "BLOCKED_BY_SPINOR_BASIS_CONVENTION"
BLOCKED_BY_SELECTION_RULE_DERIVATION: Final[str] = "BLOCKED_BY_SELECTION_RULE_DERIVATION"
REQUIRES_PHYSICAL_INPUT: Final[str] = "REQUIRES_PHYSICAL_INPUT"
INCONCLUSIVE: Final[str] = "INCONCLUSIVE"


@dataclass(frozen=True)
class SpinorSelectionRuleAuditRecord:
    """State-space and selection-rule repair summary."""

    p13b0_status: str
    p11_status: str
    p12_status: str
    state_count_kmax2: int
    state_count_kmax3: int
    lowest_spinor_state_kmax2: object
    lowest_spinor_state_kmax3: object
    zero_tuple_classification_spinor: str
    zero_tuple_classification_scalar: str
    spinor_state_filter_status: str
    allowed_final_states_lowest_kmax2: Tuple[object, ...]
    allowed_final_state_count_lowest_kmax2: int
    delta_j_left_status: str
    delta_j_right_status: str
    delta_m_left_status: str
    delta_m_right_status: str
    pattern_comparison_status: str
    rerun_p13b_required: bool
    verdict: str
    blocking_fields: Tuple[str, ...] = field(
        default_factory=lambda: (
            "invalid spinor basis assumption",
            "selection-rule derivation for gamma^a A_a",
        )
    )
    scope: str = (
        "P13B1 repair audit only; no coefficient normalization, no physical V promotion"
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


def _spinor_states_by_kmax(k_max: int) -> tuple[object, ...]:
    return states_up_to_kmax(k_max)


def _lowest_state(states: tuple[object, ...]) -> object:
    if not states:
        raise RuntimeError("No spinor states available")
    return states[0]


def _allowed_final_states_lowest_kmax2() -> tuple[object, ...]:
    comparison = compare_to_frozen_v_scaffold(2)
    states = comparison["states"]
    oracle_mask = comparison["oracle_mask"]
    source_index = 0
    allowed: list[object] = []
    for target_index, state in enumerate(states):
        if oracle_mask[target_index, source_index]:
            allowed.append(state)
    return tuple(allowed)


def _classify_selection_rules(allowed_final_states: tuple[object, ...], source_state: object) -> tuple[str, str, str, str]:
    if not allowed_final_states:
        return (
            BLOCKED_BY_SELECTION_RULE_DERIVATION,
            BLOCKED_BY_SELECTION_RULE_DERIVATION,
            BLOCKED_BY_SELECTION_RULE_DERIVATION,
            BLOCKED_BY_SELECTION_RULE_DERIVATION,
        )

    delta_j_left = sorted({round(state.j_left - source_state.j_left, 12) for state in allowed_final_states})
    delta_j_right = sorted({round(state.j_right - source_state.j_right, 12) for state in allowed_final_states})
    delta_m_left = sorted({round(state.m_left - source_state.m_left, 12) for state in allowed_final_states})
    delta_m_right = sorted({round(state.m_right - source_state.m_right, 12) for state in allowed_final_states})

    left_status = "DERIVED" if all(delta in {-1.0, 0.0, 1.0} for delta in delta_j_left) else BLOCKED_BY_SELECTION_RULE_DERIVATION
    left_m_status = "DERIVED" if all(delta in {-1.0, 0.0, 1.0} for delta in delta_m_left) else BLOCKED_BY_SELECTION_RULE_DERIVATION
    right_status = "PATTERN_SUPPORTED" if all(delta == 0.0 for delta in delta_j_right) else INCONCLUSIVE
    right_m_status = "PATTERN_SUPPORTED" if all(delta == 0.0 for delta in delta_m_right) else INCONCLUSIVE

    return left_status, right_status, left_m_status, right_m_status


def build_p13b1_spinor_state_selection_rule_repair() -> SpinorSelectionRuleAuditRecord:
    """Return the P13B1 repair audit contract."""

    p13b0_status = "BLOCKED_BY_INVALID_SPINOR_STATE"
    p11_summary = p11_external_oracle_matrix_element_derivation_summary()
    p12_summary = p12_matrix_element_derivation_robustness_audit_summary()

    states2 = _spinor_states_by_kmax(2)
    states3 = _spinor_states_by_kmax(3)
    spinor_states2 = states2
    spinor_states3 = states3
    lowest2 = _lowest_state(states2)
    lowest3 = _lowest_state(states3)
    zero_spinor = classify_state_tuple((0.0, 0.0, 0.0, 0.0))
    zero_scalar = classify_state_tuple((0.0, 0.0, 0.0, 0.0), context="scalar")

    allowed_final_states = _allowed_final_states_lowest_kmax2()
    delta_j_left_status, delta_j_right_status, delta_m_left_status, delta_m_right_status = _classify_selection_rules(
        allowed_final_states, lowest2
    )

    p11_p12_pattern_status = (
        P13B_PATTERN_STILL_VALID
        if p11_summary["comparison_status"] == "MATCHES_FROZEN_SCAFFOLD" and p12_summary["overall_status"] == "ROBUST"
        else P13B_PATTERN_REQUIRES_REPAIR
    )

    if len(spinor_states2) != 40 or len(spinor_states3) != 80:
        verdict = BLOCKED_BY_SPINOR_BASIS_CONVENTION
    elif zero_spinor != INVALID_SPINOR_STATE:
        verdict = BLOCKED_BY_SPINOR_BASIS_CONVENTION
    elif p11_p12_pattern_status == P13B_PATTERN_STILL_VALID and delta_j_left_status == "DERIVED":
        verdict = P13B_PATTERN_STILL_VALID
    elif delta_j_left_status == BLOCKED_BY_SELECTION_RULE_DERIVATION:
        verdict = BLOCKED_BY_SELECTION_RULE_DERIVATION
    else:
        verdict = P13B_READY_FOR_RERUN

    return SpinorSelectionRuleAuditRecord(
        p13b0_status=p13b0_status,
        p11_status=str(p11_summary["status"]),
        p12_status=str(p12_summary["status"]),
        state_count_kmax2=len(states2),
        state_count_kmax3=len(states3),
        lowest_spinor_state_kmax2=lowest2,
        lowest_spinor_state_kmax3=lowest3,
        zero_tuple_classification_spinor=zero_spinor,
        zero_tuple_classification_scalar=zero_scalar,
        spinor_state_filter_status=SPINOR_STATE,
        allowed_final_states_lowest_kmax2=allowed_final_states,
        allowed_final_state_count_lowest_kmax2=len(allowed_final_states),
        delta_j_left_status=delta_j_left_status,
        delta_j_right_status=delta_j_right_status,
        delta_m_left_status=delta_m_left_status,
        delta_m_right_status=delta_m_right_status,
        pattern_comparison_status=p11_p12_pattern_status,
        rerun_p13b_required=verdict == P13B_READY_FOR_RERUN,
        verdict=verdict,
    )


def p13b1_spinor_state_selection_rule_repair_summary() -> dict[str, object]:
    """Return a compact summary for reports and tests."""

    audit = build_p13b1_spinor_state_selection_rule_repair()
    return {
        "status": P13B1_SPINOR_STATE_AND_SELECTION_RULE_REPAIR_STATUS,
        "p13b0_status": audit.p13b0_status,
        "p11_status": audit.p11_status,
        "p12_status": audit.p12_status,
        "state_count_kmax2": audit.state_count_kmax2,
        "state_count_kmax3": audit.state_count_kmax3,
        "lowest_spinor_state_kmax2": audit.lowest_spinor_state_kmax2,
        "lowest_spinor_state_kmax3": audit.lowest_spinor_state_kmax3,
        "zero_tuple_classification_spinor": audit.zero_tuple_classification_spinor,
        "zero_tuple_classification_scalar": audit.zero_tuple_classification_scalar,
        "spinor_state_filter_status": audit.spinor_state_filter_status,
        "allowed_final_states_lowest_kmax2": audit.allowed_final_states_lowest_kmax2,
        "allowed_final_state_count_lowest_kmax2": audit.allowed_final_state_count_lowest_kmax2,
        "delta_j_left_status": audit.delta_j_left_status,
        "delta_j_right_status": audit.delta_j_right_status,
        "delta_m_left_status": audit.delta_m_left_status,
        "delta_m_right_status": audit.delta_m_right_status,
        "pattern_comparison_status": audit.pattern_comparison_status,
        "rerun_p13b_required": audit.rerun_p13b_required,
        "verdict": audit.verdict,
        "blocking_fields": audit.blocking_fields,
        "scope": audit.scope,
        "forbidden_claims": audit.forbidden_claims,
        "runtime_status": "research_only",
        "v_selection_status": "smoke_only",
        "safe_for_runtime": False,
    }
