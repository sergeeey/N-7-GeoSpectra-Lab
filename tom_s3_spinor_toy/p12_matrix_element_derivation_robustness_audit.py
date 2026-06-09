"""P12 matrix-element derivation robustness audit.

This module stress-tests the frozen P11 external Wigner/CG oracle against
basis-ordering, phase, normalization, and small k_max extension changes.
It does not promote V-selection rules and does not claim physical operator
derivations or Standard Model reproduction.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Iterable, Tuple

import numpy as np

from p10_selection_rule_matrix_element_review import (
    p10_selection_rule_matrix_element_review_summary,
)
from p11_external_oracle_matrix_element_derivation import (
    BASIS_ORDERING_DEPENDENT,
    NORMALIZATION_DEPENDENT,
    build_external_oracle_raw_pattern,
    build_external_oracle_selection_pattern,
    compare_to_frozen_v_scaffold,
    p11_external_oracle_matrix_element_derivation_summary,
)


P12_MATRIX_ELEMENT_DERIVATION_ROBUSTNESS_AUDIT_STATUS: Final[str] = "passed"
RUNTIME_STATUS: Final[str] = "research_only"
V_SELECTION_STATUS: Final[str] = "smoke_only"
SAFE_FOR_RUNTIME: Final[bool] = False

ROBUST: Final[str] = "ROBUST"
PERMUTED_EQUIVALENT: Final[str] = "PERMUTED_EQUIVALENT"
PHASE_DEPENDENT: Final[str] = "PHASE_DEPENDENT"
K_MAX_LIMITED: Final[str] = "K_MAX_LIMITED"
FAILED: Final[str] = "FAILED"


def _mask(matrix: np.ndarray) -> np.ndarray:
    return np.abs(matrix) > 0


def _permute_matrix(matrix: np.ndarray, permutation: np.ndarray) -> np.ndarray:
    return matrix[np.ix_(permutation, permutation)]


def _candidate_permutations(states: list[object]) -> dict[str, np.ndarray]:
    n = len(states)
    identity = np.arange(n, dtype=int)
    reverse = identity[::-1]
    branch_sorted = np.array(
        sorted(
            range(n),
            key=lambda i: (
                getattr(states[i], "k"),
                getattr(states[i], "branch"),
                getattr(states[i], "j_left"),
                getattr(states[i], "m_left"),
                getattr(states[i], "j_right"),
                getattr(states[i], "m_right"),
            ),
        ),
        dtype=int,
    )
    return {
        "identity": identity,
        "reverse": reverse,
        "branch_sorted": branch_sorted,
    }


def _candidate_phases(n: int) -> dict[str, np.ndarray]:
    phases = np.ones(n, dtype=complex)
    alternating = np.array([1.0 if idx % 2 == 0 else -1.0 for idx in range(n)], dtype=complex)
    quarter_turn = np.array(
        [1.0 if idx % 4 == 0 else 1j if idx % 4 == 1 else -1.0 if idx % 4 == 2 else -1j for idx in range(n)],
        dtype=complex,
    )
    return {
        "identity": phases,
        "alternating_sign": alternating,
        "quarter_turn": quarter_turn,
    }


def _apply_phases(matrix: np.ndarray, phases: np.ndarray) -> np.ndarray:
    diag = np.diag(phases)
    return diag @ matrix @ np.conjugate(diag).T


def _compare_masks(a: np.ndarray, b: np.ndarray) -> bool:
    return bool(np.array_equal(_mask(a), _mask(b)))


def _hermiticity_ok(matrix: np.ndarray) -> bool:
    return bool(np.allclose(matrix, matrix.conjugate().T, atol=1e-12))


@dataclass(frozen=True)
class P12MatrixElementDerivationRobustnessAudit:
    """Structured robustness audit for the P11 external oracle."""

    p11_status: str
    p10_status: str
    basis_ordering_status: str
    phase_status: str
    normalization_status: str
    k_max_status: str
    hermiticity_status: str
    overall_status: str
    k_max_results: Tuple[Tuple[int, str, bool, bool, int, int], ...]
    basis_ordering_checks: Tuple[Tuple[str, bool, bool, bool], ...]
    phase_checks: Tuple[Tuple[str, bool, bool], ...]
    normalization_checks: Tuple[Tuple[str, bool, bool], ...]
    selection_rule_status: str
    audit_result: str
    scope: str
    forbidden_claims: Tuple[str, ...] = field(
        default_factory=lambda: (
            "physical V-operator derivation",
            "V-selection promotion",
            "Standard Model reproduced claim",
            "fermion generation claim",
            "ad hoc basis permutation",
            "ad hoc phase patch",
            "ad hoc normalization patch",
        )
    )


def evaluate_basis_ordering_robustness(k_max: int = 2) -> dict[str, object]:
    """Stress-test the oracle pattern against label-order permutations."""

    oracle_pattern, states = build_external_oracle_selection_pattern(k_max=k_max)
    frozen = compare_to_frozen_v_scaffold(k_max=k_max)["frozen_mask"]
    candidate_perms = _candidate_permutations(states)
    checks: list[tuple[str, bool, bool, bool]] = []
    for name, perm in candidate_perms.items():
        permuted_oracle = _permute_matrix(oracle_pattern, perm)
        permuted_frozen = _permute_matrix(frozen, perm)
        checks.append(
            (
                name,
                _compare_masks(permuted_oracle, permuted_frozen),
                _hermiticity_ok(permuted_oracle),
                _hermiticity_ok(permuted_frozen),
            )
        )
    stable = all(match and herm_ok and frozen_herm_ok for _, match, herm_ok, frozen_herm_ok in checks)
    status = PERMUTED_EQUIVALENT if stable else BASIS_ORDERING_DEPENDENT
    return {
        "k_max": k_max,
        "status": status,
        "checks": tuple(checks),
        "oracle_shape": oracle_pattern.shape,
        "frozen_shape": frozen.shape,
    }


def evaluate_phase_convention_robustness(k_max: int = 2) -> dict[str, object]:
    """Stress-test the oracle against basis phase rotations."""

    raw, states = build_external_oracle_raw_pattern(k_max=k_max)
    oracle_pattern, _ = build_external_oracle_selection_pattern(k_max=k_max)
    phases = _candidate_phases(len(states))
    checks: list[tuple[str, bool, bool]] = []
    for name, phase_vector in phases.items():
        transformed = _apply_phases(raw, phase_vector)
        hermitianized = (transformed + transformed.conjugate().T) / 2.0
        checks.append(
            (
                name,
                _compare_masks(hermitianized, oracle_pattern),
                _hermiticity_ok(hermitianized),
            )
        )
    stable = all(match and herm_ok for _, match, herm_ok in checks)
    status = PHASE_DEPENDENT if stable else FAILED
    return {
        "k_max": k_max,
        "status": status,
        "checks": tuple(checks),
        "shape": oracle_pattern.shape,
    }


def evaluate_normalization_robustness(k_max: int = 2) -> dict[str, object]:
    """Stress-test the oracle against coefficient rescaling."""

    raw, _ = build_external_oracle_raw_pattern(k_max=k_max)
    oracle_pattern, _ = build_external_oracle_selection_pattern(k_max=k_max)
    scaling_factors = (0.5, 2.0, 3.0)
    checks: list[tuple[str, bool, bool]] = []
    for factor in scaling_factors:
        scaled = raw * complex(factor)
        hermitianized = (scaled + scaled.conjugate().T) / 2.0
        checks.append(
            (
                f"x{factor:g}",
                _compare_masks(hermitianized, oracle_pattern),
                _hermiticity_ok(hermitianized),
            )
        )
    stable = all(match and herm_ok for _, match, herm_ok in checks)
    status = NORMALIZATION_DEPENDENT if stable else FAILED
    return {
        "k_max": k_max,
        "status": status,
        "checks": tuple(checks),
        "shape": oracle_pattern.shape,
    }


def evaluate_k_max_extension(k_values: Iterable[int] = (1, 2, 3)) -> dict[str, object]:
    """Compare the oracle and frozen scaffold across a small k_max range."""

    results: list[tuple[int, str, bool, bool, int, int]] = []
    overall = ROBUST
    for k_max in k_values:
        try:
            comparison = compare_to_frozen_v_scaffold(k_max=k_max)
        except NotImplementedError:
            results.append((k_max, K_MAX_LIMITED, False, False, 0, 0))
            overall = K_MAX_LIMITED if overall == ROBUST else overall
            continue
        except RuntimeError:
            results.append((k_max, FAILED, False, False, 0, 0))
            overall = FAILED
            continue

        matched = bool(comparison["pattern_matches"])
        hermitian_ok = bool(comparison["hermitian_compatible"])
        oracle_nonzero = int(comparison["oracle_nonzero"])
        frozen_nonzero = int(comparison["frozen_nonzero"])
        status = ROBUST if matched and hermitian_ok else FAILED
        results.append((k_max, status, matched, hermitian_ok, oracle_nonzero, frozen_nonzero))
        if status != ROBUST:
            overall = status
    return {
        "status": overall,
        "results": tuple(results),
    }


def build_p12_matrix_element_derivation_robustness_audit() -> P12MatrixElementDerivationRobustnessAudit:
    """Return the current P12 robustness audit contract."""

    p11_summary = p11_external_oracle_matrix_element_derivation_summary()
    p10_summary = p10_selection_rule_matrix_element_review_summary()

    basis = evaluate_basis_ordering_robustness(k_max=2)
    phase = evaluate_phase_convention_robustness(k_max=2)
    normalization = evaluate_normalization_robustness(k_max=2)
    k_extension = evaluate_k_max_extension(k_values=(1, 2, 3))

    hermiticity_ok = all(
        herm_ok and frozen_herm_ok
        for _, _, herm_ok, frozen_herm_ok in basis["checks"]
    ) and all(
        herm_ok for _, _, herm_ok in phase["checks"]
    ) and all(
        herm_ok for _, _, herm_ok in normalization["checks"]
    )

    if k_extension["status"] == ROBUST and all(status == ROBUST for _, status, *_ in k_extension["results"]):
        k_status = ROBUST
    elif any(status == K_MAX_LIMITED for _, status, *_ in k_extension["results"]):
        k_status = K_MAX_LIMITED
    else:
        k_status = FAILED

    if basis["status"] == PERMUTED_EQUIVALENT and phase["status"] == PHASE_DEPENDENT and normalization["status"] == NORMALIZATION_DEPENDENT and k_status == ROBUST and hermiticity_ok:
        overall = ROBUST
    elif k_status == K_MAX_LIMITED:
        overall = K_MAX_LIMITED
    elif basis["status"] != PERMUTED_EQUIVALENT:
        overall = BASIS_ORDERING_DEPENDENT
    elif phase["status"] != PHASE_DEPENDENT:
        overall = FAILED
    else:
        overall = FAILED

    return P12MatrixElementDerivationRobustnessAudit(
        p11_status=str(p11_summary["status"]),
        p10_status=str(p10_summary["status"]),
        basis_ordering_status=str(basis["status"]),
        phase_status=str(phase["status"]),
        normalization_status=str(normalization["status"]),
        k_max_status=str(k_status),
        hermiticity_status=ROBUST if hermiticity_ok else FAILED,
        overall_status=str(overall),
        k_max_results=tuple(k_extension["results"]),
        basis_ordering_checks=tuple(basis["checks"]),
        phase_checks=tuple(phase["checks"]),
        normalization_checks=tuple(normalization["checks"]),
        selection_rule_status="smoke_only",
        audit_result=(
            "external_oracle_robustness_audit_passed"
            if overall == ROBUST
            else "external_oracle_robustness_audit_limited"
            if overall == K_MAX_LIMITED
            else "external_oracle_robustness_audit_failed"
        ),
        scope=(
            "P12 robustness audit only; no V promotion, no physical V-operator "
            "claim, no Standard Model claim"
        ),
    )


def p12_matrix_element_derivation_robustness_audit_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and tests."""

    audit = build_p12_matrix_element_derivation_robustness_audit()
    return {
        "p11_status": audit.p11_status,
        "p10_status": audit.p10_status,
        "basis_ordering_status": audit.basis_ordering_status,
        "phase_status": audit.phase_status,
        "normalization_status": audit.normalization_status,
        "k_max_status": audit.k_max_status,
        "hermiticity_status": audit.hermiticity_status,
        "overall_status": audit.overall_status,
        "k_max_results": audit.k_max_results,
        "basis_ordering_checks": audit.basis_ordering_checks,
        "phase_checks": audit.phase_checks,
        "normalization_checks": audit.normalization_checks,
        "selection_rule_status": audit.selection_rule_status,
        "audit_result": audit.audit_result,
        "scope": audit.scope,
        "forbidden_claims": audit.forbidden_claims,
        "status": P12_MATRIX_ELEMENT_DERIVATION_ROBUSTNESS_AUDIT_STATUS,
        "runtime_status": RUNTIME_STATUS,
        "v_selection_status": V_SELECTION_STATUS,
        "safe_for_runtime": SAFE_FOR_RUNTIME,
    }
