"""P13B0 state / measure / selection-rule audit.

This module repairs the validation setup before any matrix-element pattern
claim. It validates state labels, the S3 volume measure, complex-valued toy
matrix elements, and the current selection-rule assumptions for the candidate
``gamma^a A_a`` coupling. It does not claim a physical V-operator.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Iterable, Tuple

import numpy as np
import sympy as sp
from scipy import integrate

from ben_achour_one_form_modes import (
    BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE,
    NORMALIZATION_DEPENDENT,
    build_low_mode_ben_achour_one_form_modes,
    hopf_coordinate_symbols,
    p13a1_ben_achour_one_form_mode_implementation_summary,
)
from geometry_s3_hopf import s3_volume_analytical, volume_measure
from p11_external_oracle_matrix_element_derivation import (
    compare_to_frozen_v_scaffold,
    p11_external_oracle_matrix_element_derivation_summary,
)
from p12_matrix_element_derivation_robustness_audit import (
    p12_matrix_element_derivation_robustness_audit_summary,
)
from s3_coupling_v_option_b import expand_spectral_basis_states
from standard_s3_spinor_harmonics import standard_spinor_frame


P13B0_STATE_MEASURE_AND_SELECTION_RULE_AUDIT_STATUS: Final[str] = "passed"
P13B0_READY_AFTER_REPAIR: Final[str] = "P13B0_READY_AFTER_REPAIR"
BLOCKED_BY_INVALID_SPINOR_STATE: Final[str] = "BLOCKED_BY_INVALID_SPINOR_STATE"
BLOCKED_BY_MEASURE_ERROR: Final[str] = "BLOCKED_BY_MEASURE_ERROR"
BLOCKED_BY_SELECTION_RULE_DERIVATION: Final[str] = "BLOCKED_BY_SELECTION_RULE_DERIVATION"
BLOCKED_BY_SPINOR_HARMONIC_BLACK_BOX: Final[str] = "BLOCKED_BY_SPINOR_HARMONIC_BLACK_BOX"
BLOCKED_BY_E_MODE_BLACK_BOX: Final[str] = "BLOCKED_BY_E_MODE_BLACK_BOX"
BLOCKED_BY_NUMERICAL_CONVERGENCE: Final[str] = "BLOCKED_BY_NUMERICAL_CONVERGENCE"
INCONCLUSIVE: Final[str] = "INCONCLUSIVE"
BLACK_BOX_DEPENDENCY: Final[str] = "BLACK_BOX_DEPENDENCY"
DERIVED: Final[str] = "DERIVED"
REFUTED: Final[str] = "REFUTED"
MEASURE_APPLIED_ONCE: Final[str] = "MEASURE_APPLIED_ONCE"
COMPLEX_PRESERVED: Final[str] = "COMPLEX_PRESERVED"
CONVENTION_DEPENDENT: Final[str] = "CONVENTION_DEPENDENT"
SPINOR_STATE: Final[str] = "SPINOR_STATE"
INVALID_SPINOR_STATE: Final[str] = "INVALID_SPINOR_STATE"
SCALAR_STATE: Final[str] = "SCALAR_STATE"


@dataclass(frozen=True)
class SpinorStateAuditRecord:
    index: int
    k: int
    branch: str
    j_left: float
    m_left: float
    j_right: float
    m_right: float
    classification: str
    note: str


@dataclass(frozen=True)
class P13B0StateMeasureSelectionRuleAudit:
    p13a1_status: str
    p11_status: str
    p12_status: str
    state_count_kmax2: int
    state_records_kmax2: Tuple[SpinorStateAuditRecord, ...]
    lowest_spinor_state: SpinorStateAuditRecord
    zero_tuple_classification: str
    measure_status: str
    measure_once_status: str
    measure_double_count_status: str
    complex_matrix_status: str
    spinor_normalization_status: str
    e_mode_status: str
    e_mode_normalization_status: str
    selection_rule_status: str
    selection_rule_assumption_status: str
    numerical_convergence_status: str
    convergence_by_grid: Tuple[Tuple[int, complex], ...]
    verdict: str
    blocking_fields: Tuple[str, ...] = field(
        default_factory=lambda: (
            "invalid spinor state assumption",
            "selection-rule derivation",
            "spinor-harmonic normalization black-box dependency",
            "exact coefficient normalization",
        )
    )


def states_up_to_kmax(k_max: int) -> tuple[SpinorStateAuditRecord, ...]:
    """Return the expanded spectral spinor states through ``k_max``."""

    states = expand_spectral_basis_states(k_max=k_max)
    records: list[SpinorStateAuditRecord] = []
    for state in states:
        records.append(
            SpinorStateAuditRecord(
                index=state.index,
                k=state.k,
                branch=state.branch,
                j_left=state.j_left,
                m_left=state.m_left,
                j_right=state.j_right,
                m_right=state.m_right,
                classification=SPINOR_STATE,
                note="frozen spectral/Wigner scaffold state",
            )
        )
    return tuple(records)


def classify_state_tuple(
    state: tuple[float, float, float, float],
    *,
    context: str = "spinor",
) -> str:
    """Classify a raw state tuple under the current audit convention."""

    j_left, m_left, j_right, m_right = state
    if all(abs(value) < 1e-12 for value in state):
        if context == "scalar":
            return SCALAR_STATE
        return INVALID_SPINOR_STATE
    if context == "scalar":
        return CONVENTION_DEPENDENT
    valid_states = {
        (record.j_left, record.m_left, record.j_right, record.m_right)
        for record in states_up_to_kmax(2)
    }
    if state in valid_states:
        return SPINOR_STATE
    if j_left == 0.0 and j_right == 0.0:
        return INVALID_SPINOR_STATE
    return CONVENTION_DEPENDENT


def lowest_spinor_state() -> SpinorStateAuditRecord:
    """Return the lowest state in the current spectral scaffold ordering."""

    records = states_up_to_kmax(2)
    if not records:
        raise RuntimeError("No spectral states available")
    return records[0]


def _measure_audit(n_points: int = 4001) -> dict[str, object]:
    alpha = np.linspace(0.0, np.pi / 2.0, n_points)
    radial_numeric = np.trapezoid(volume_measure(alpha), alpha)
    radial_exact, _ = integrate.quad(lambda a: float(volume_measure(np.array([a]))[0]), 0.0, np.pi / 2.0)
    full_once = radial_exact * (2.0 * np.pi) ** 2
    double_counted = radial_exact * (2.0 * np.pi) ** 4
    exact = s3_volume_analytical()
    once_ok = bool(np.isclose(full_once, exact, rtol=1e-10, atol=1e-10))
    double_ok = bool(np.isclose(double_counted, exact, rtol=1e-10, atol=1e-10))
    return {
        "status": MEASURE_APPLIED_ONCE if once_ok and not double_ok else BLOCKED_BY_MEASURE_ERROR,
        "measure_once_value": full_once,
        "measure_double_count_value": double_counted,
        "exact_volume": exact,
        "radial_measure": radial_exact,
        "radial_measure_numeric": radial_numeric,
    }


def _candidate_complex_matrix_element(grid_n: int) -> complex:
    """Return a toy complex matrix element with the full complex value preserved."""

    eps = 1e-6
    alpha = np.linspace(eps, np.pi / 2.0 - eps, grid_n)
    theta = 0.37
    phi = 1.11
    sigma1 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sigma2 = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
    sigma3 = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)

    low_mode = build_low_mode_ben_achour_one_form_modes(L=2, m_plus=0, m_minus=0)
    alpha_sym, theta_sym, phi_sym = hopf_coordinate_symbols()
    components = [
        sp.lambdify((alpha_sym, theta_sym, phi_sym), low_mode.E.dalpha, "numpy"),
        sp.lambdify((alpha_sym, theta_sym, phi_sym), low_mode.E.dtheta, "numpy"),
        sp.lambdify((alpha_sym, theta_sym, phi_sym), low_mode.E.dphi, "numpy"),
    ]

    integrand = np.zeros_like(alpha, dtype=complex)
    for idx, a in enumerate(alpha):
        frame = standard_spinor_frame(a, theta, phi)
        a_vec = np.array([component(a, theta, phi) for component in components], dtype=complex)
        gamma_a_a = a_vec[0] * sigma1 + a_vec[1] * sigma2 + a_vec[2] * sigma3
        matrix = frame.conj().T @ gamma_a_a @ frame
        integrand[idx] = complex(matrix[0, 0])

    return np.trapezoid(integrand * volume_measure(alpha), alpha) * (2.0 * np.pi) ** 2


def _convergence_audit(grid_sizes: Iterable[int] = (20, 40, 80)) -> tuple[str, tuple[tuple[int, complex], ...]]:
    values: list[tuple[int, complex]] = []
    for grid_n in grid_sizes:
        values.append((int(grid_n), _candidate_complex_matrix_element(int(grid_n))))
    diffs = [abs(values[i + 1][1] - values[i][1]) for i in range(len(values) - 1)]
    converged = len(diffs) >= 2 and diffs[-1] < diffs[0] and diffs[-1] < 1e-6
    return ("CONVERGED" if converged else "NOT_CONVERGED", tuple(values))


def _selection_rule_audit() -> tuple[str, str]:
    """Audit the selection-rule assumptions for the candidate gamma^a A_a."""

    # The current scaffold validates the left CG selection pattern, but there is
    # still no explicit operator density derivation that proves the right-sector
    # behavior for gamma^a A_a. Therefore we refuse to assume Δj_R = 0.
    oracle = compare_to_frozen_v_scaffold(1)
    if oracle["pattern_matches"] and oracle["hermitian_compatible"]:
        return INCONCLUSIVE, "current evidence supports the frozen scaffold, not the full gamma^a A_a derivation"
    return REFUTED, "frozen scaffold mismatch would refute the current working pattern"


def build_p13b0_state_measure_selection_rule_audit() -> P13B0StateMeasureSelectionRuleAudit:
    """Return the current P13B0 repair-audit contract."""

    p13a1_summary = p13a1_ben_achour_one_form_mode_implementation_summary()
    p11_summary = p11_external_oracle_matrix_element_derivation_summary()
    p12_summary = p12_matrix_element_derivation_robustness_audit_summary()

    records = states_up_to_kmax(2)
    lowest = lowest_spinor_state()
    zero_tuple_classification = classify_state_tuple((0.0, 0.0, 0.0, 0.0))
    measure = _measure_audit()
    convergence_status, convergence_by_grid = _convergence_audit()
    selection_rule_status, selection_rule_assumption_status = _selection_rule_audit()

    spinor_normalization_status = BLACK_BOX_DEPENDENCY
    e_mode_status = BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE
    e_mode_normalization_status = NORMALIZATION_DEPENDENT
    complex_matrix_status = COMPLEX_PRESERVED

    if zero_tuple_classification == INVALID_SPINOR_STATE:
        verdict = BLOCKED_BY_INVALID_SPINOR_STATE
    elif measure["status"] == BLOCKED_BY_MEASURE_ERROR:
        verdict = BLOCKED_BY_MEASURE_ERROR
    elif selection_rule_status == INCONCLUSIVE:
        verdict = BLOCKED_BY_SELECTION_RULE_DERIVATION
    elif spinor_normalization_status == BLACK_BOX_DEPENDENCY:
        verdict = BLOCKED_BY_SPINOR_HARMONIC_BLACK_BOX
    elif e_mode_status != BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE:
        verdict = BLOCKED_BY_E_MODE_BLACK_BOX
    elif convergence_status != "CONVERGED":
        verdict = BLOCKED_BY_NUMERICAL_CONVERGENCE
    else:
        verdict = P13B0_READY_AFTER_REPAIR

    return P13B0StateMeasureSelectionRuleAudit(
        p13a1_status=str(p13a1_summary["status"]),
        p11_status=str(p11_summary["status"]),
        p12_status=str(p12_summary["status"]),
        state_count_kmax2=len(records),
        state_records_kmax2=records,
        lowest_spinor_state=lowest,
        zero_tuple_classification=zero_tuple_classification,
        measure_status=str(measure["status"]),
        measure_once_status=MEASURE_APPLIED_ONCE if measure["status"] == MEASURE_APPLIED_ONCE else BLOCKED_BY_MEASURE_ERROR,
        measure_double_count_status=BLOCKED_BY_MEASURE_ERROR if measure["status"] == MEASURE_APPLIED_ONCE else MEASURE_APPLIED_ONCE,
        complex_matrix_status=complex_matrix_status,
        spinor_normalization_status=spinor_normalization_status,
        e_mode_status=e_mode_status,
        e_mode_normalization_status=e_mode_normalization_status,
        selection_rule_status=selection_rule_status,
        selection_rule_assumption_status=selection_rule_assumption_status,
        numerical_convergence_status=convergence_status,
        convergence_by_grid=convergence_by_grid,
        verdict=verdict,
    )


def p13b0_state_measure_selection_rule_audit_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and tests."""

    audit = build_p13b0_state_measure_selection_rule_audit()
    return {
        "p13a1_status": audit.p13a1_status,
        "p11_status": audit.p11_status,
        "p12_status": audit.p12_status,
        "state_count_kmax2": audit.state_count_kmax2,
        "lowest_spinor_state": audit.lowest_spinor_state,
        "zero_tuple_classification": audit.zero_tuple_classification,
        "measure_status": audit.measure_status,
        "measure_once_status": audit.measure_once_status,
        "measure_double_count_status": audit.measure_double_count_status,
        "complex_matrix_status": audit.complex_matrix_status,
        "spinor_normalization_status": audit.spinor_normalization_status,
        "e_mode_status": audit.e_mode_status,
        "e_mode_normalization_status": audit.e_mode_normalization_status,
        "selection_rule_status": audit.selection_rule_status,
        "selection_rule_assumption_status": audit.selection_rule_assumption_status,
        "numerical_convergence_status": audit.numerical_convergence_status,
        "convergence_by_grid": audit.convergence_by_grid,
        "verdict": audit.verdict,
        "blocking_fields": audit.blocking_fields,
        "status": P13B0_STATE_MEASURE_AND_SELECTION_RULE_AUDIT_STATUS,
        "runtime_status": "research_only",
        "v_selection_status": "smoke_only",
        "safe_for_runtime": False,
    }
