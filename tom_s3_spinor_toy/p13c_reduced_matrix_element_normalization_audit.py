"""P13C reduced matrix-element normalization audit.

This module audits the coefficient provenance for the candidate S3 V-like
operator. It separates pattern-level evidence, relative coefficient evidence,
and absolute normalization evidence. It does not promote a physical V-operator
and does not promote V-selection rules.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

import numpy as np

from ben_achour_one_form_modes import (
    NORMALIZATION_DEPENDENT as BEN_ACHOUR_NORMALIZATION_DEPENDENT,
    build_low_mode_ben_achour_one_form_modes,
)
from convention_registry import (
    CONVENTION_FIXED,
    NORMALIZATION_DEPENDENT,
    PHASE_CONVENTION_DEPENDENT,
)
from p11_external_oracle_matrix_element_derivation import (
    MATCHES_FROZEN_SCAFFOLD,
    build_external_oracle_raw_pattern,
    p11_external_oracle_matrix_element_derivation_summary,
)
from p12_matrix_element_derivation_robustness_audit import (
    ROBUST,
    p12_matrix_element_derivation_robustness_audit_summary,
)
from p13a_v_operator_ansatz_convention_registry import (
    p13a_v_operator_ansatz_convention_registry_summary,
)
from ben_achour_one_form_modes import p13a1_ben_achour_one_form_mode_implementation_summary
from p13b_symbolic_v_matrix_element_pattern_build import (
    P13B_SYMBOLIC_V_MATRIX_ELEMENT_PATTERN_BUILD_STATUS,
)
from s3_reduced_matrix_elements import (
    reduced_element_metadata,
    reduced_elements_for_kmax1,
)
from su4_hypercharge_gauge_breaking_audit import su4_hypercharge_gauge_audit_summary


P13C_REDUCED_MATRIX_ELEMENT_NORMALIZATION_AUDIT_STATUS: Final[str] = "passed"
RELATIVE_COEFFICIENTS_DERIVED: Final[str] = "RELATIVE_COEFFICIENTS_DERIVED"
ABSOLUTE_NORMALIZATION_DERIVED: Final[str] = "ABSOLUTE_NORMALIZATION_DERIVED"
REQUIRES_PHYSICAL_COUPLING_INPUT: Final[str] = "REQUIRES_PHYSICAL_COUPLING_INPUT"
INCONCLUSIVE: Final[str] = "INCONCLUSIVE"
DERIVED: Final[str] = "DERIVED"
COEFFICIENT_SAMPLE_K_MAX: Final[int] = 1


@dataclass(frozen=True)
class CoefficientSourceAuditRecord:
    """A single audited source of coefficient information."""

    source: str
    source_classification: str
    evidence: str
    notes: str


@dataclass(frozen=True)
class P13CReducedMatrixElementNormalizationAudit:
    """Structured contract for the P13C normalization audit."""

    p13a_status: str
    p13a1_status: str
    p13b_status: str
    p11_status: str
    p12_status: str
    su4_status: str
    coefficient_sources: Tuple[CoefficientSourceAuditRecord, ...]
    pattern_level_status: str
    relative_coefficient_status: str
    absolute_normalization_status: str
    lambda_status: str
    phase_status: str
    p9_p10_comparison_status: str
    normalization_control_status: str
    phase_control_status: str
    exact_coefficients_status: str
    reduced_matrix_element_status: str
    reduced_element_sample_count: int
    reduced_element_sample_nonzero: int
    reduced_element_sample_value: complex
    verdict: str
    blocking_fields: Tuple[str, ...] = field(
        default_factory=lambda: (
            "absolute normalization of reduced matrix elements",
            "physical coupling lambda",
            "phase convention dependence",
            "physical V-operator density",
        )
    )
    scope: str = (
        "P13C coefficient normalization audit only; no physical V promotion, "
        "no V-selection promotion, no Standard Model claim"
    )
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


def _coefficient_source_records() -> tuple[CoefficientSourceAuditRecord, ...]:
    """Return the audited coefficient source registry."""

    return (
        CoefficientSourceAuditRecord(
            source="Wigner/CG coefficient",
            source_classification=DERIVED,
            evidence=(
                "SymPy Clebsch-Gordan selection rules recover the frozen P11/P12 "
                "zero/nonzero scaffold and preserve Hermiticity under the tested pattern"
            ),
            notes="pattern-level and relative-coefficient factor; not the absolute normalization",
        ),
        CoefficientSourceAuditRecord(
            source="reduced matrix element",
            source_classification=RELATIVE_COEFFICIENTS_DERIVED,
            evidence=(
                "working direct-Haar reduced elements exist in s3_reduced_matrix_elements; "
                "finite nonzero samples appear through k_max=1"
            ),
            notes="relative coefficients are available; final Ben Achour scaling remains unresolved",
        ),
        CoefficientSourceAuditRecord(
            source="Ben Achour E_i/E'_i normalization",
            source_classification=BEN_ACHOUR_NORMALIZATION_DEPENDENT,
            evidence=(
                "build_low_mode_ben_achour_one_form_modes(L=2, m_plus=0, m_minus=0) "
                "reports normalization-dependent exact E/E' normalization"
            ),
            notes="geometry is executable at low mode, but exact coefficient scale is not fixed",
        ),
        CoefficientSourceAuditRecord(
            source="gamma/Clifford normalization",
            source_classification=CONVENTION_FIXED,
            evidence="Euclidean Pauli/Clifford scaffold is already frozen in the registry",
            notes="fixed matrix convention; not the unresolved physical scale",
        ),
        CoefficientSourceAuditRecord(
            source="SU4 generator normalization",
            source_classification=CONVENTION_FIXED,
            evidence="P7 fixed T_I = lambda_I / 2 and Tr(T_a T_b) = 1/2 delta_ab",
            notes="generator normalization is fixed; physical coupling is not",
        ),
        CoefficientSourceAuditRecord(
            source="coupling lambda",
            source_classification=REQUIRES_PHYSICAL_COUPLING_INPUT,
            evidence="no internal source fixes the physical coupling constant",
            notes="lambda must come from external physical input or a separate promotion gate",
        ),
    )


def _wrong_normalization_control() -> dict[str, object]:
    """Check that a wrong rescaling changes coefficients but preserves the pattern."""

    base = reduced_elements_for_kmax1()
    if not base:
        return {
            "status": INCONCLUSIVE,
            "pattern_preserved": False,
            "coefficients_changed": False,
            "scale_factor": 2.0,
        }
    scale_factor = 2.0
    scaled = {key: value * scale_factor for key, value in base.items()}
    pattern_preserved = set(base) == set(scaled)
    coefficients_changed = any(not np.isclose(base[key], scaled[key]) for key in base)
    status = NORMALIZATION_DEPENDENT if pattern_preserved and coefficients_changed else INCONCLUSIVE
    return {
        "status": status,
        "pattern_preserved": pattern_preserved,
        "coefficients_changed": coefficients_changed,
        "scale_factor": scale_factor,
    }


def _wrong_phase_control() -> dict[str, object]:
    """Check that a wrong phase changes coefficients but preserves the pattern."""

    raw, states = build_external_oracle_raw_pattern(COEFFICIENT_SAMPLE_K_MAX)
    phase_vector = np.array(
        [1.0 if idx % 2 == 0 else 1.0j for idx in range(len(states))],
        dtype=complex,
    )
    diag = np.diag(phase_vector)
    transformed = diag @ raw @ np.conjugate(diag).T
    pattern_preserved = bool(np.array_equal(np.abs(transformed) > 0, np.abs(raw) > 0))
    coefficients_changed = bool(np.any(np.abs(transformed - raw) > 1e-12))
    status = (
        PHASE_CONVENTION_DEPENDENT if pattern_preserved and coefficients_changed else INCONCLUSIVE
    )
    return {
        "status": status,
        "pattern_preserved": pattern_preserved,
        "coefficients_changed": coefficients_changed,
    }


def _sample_reduced_element() -> tuple[int, int, complex]:
    """Return a representative reduced coefficient sample for reporting."""

    elements = reduced_elements_for_kmax1()
    if not elements:
        return 0, 0, 0.0 + 0.0j
    key = sorted(elements)[0]
    return (
        int(len(elements)),
        int(np.count_nonzero(list(elements.values()))),
        complex(elements[key]),
    )


def _evaluate_reduced_normalization_from_ben_achour() -> dict[str, object]:
    """Audit whether the reduced coefficients can be fixed from Ben Achour norms."""

    metadata = reduced_element_metadata()
    low_mode = build_low_mode_ben_achour_one_form_modes(L=2, m_plus=0, m_minus=0)
    if (
        metadata["final_ben_achour_normalization"] == "unresolved"
        or low_mode.normalization_status == BEN_ACHOUR_NORMALIZATION_DEPENDENT
    ):
        return {
            "status": NORMALIZATION_DEPENDENT,
            "reason": "final Ben Achour normalization remains unresolved",
            "metadata": metadata,
            "low_mode_status": low_mode.normalization_status,
        }
    return {
        "status": ABSOLUTE_NORMALIZATION_DERIVED,
        "reason": "Ben Achour normalization would be sufficient to fix the reduced coefficients",
        "metadata": metadata,
        "low_mode_status": low_mode.normalization_status,
    }


def _evaluate_p9_p10_comparison_normalization_dependence() -> dict[str, object]:
    """Compare available coefficients to P9/P10 only as normalization-dependent evidence."""

    p11 = p11_external_oracle_matrix_element_derivation_summary()
    p12 = p12_matrix_element_derivation_robustness_audit_summary()
    sample_count, sample_nonzero, sample_value = _sample_reduced_element()
    if p11["comparison_status"] == MATCHES_FROZEN_SCAFFOLD and p12["overall_status"] == ROBUST:
        status = NORMALIZATION_DEPENDENT
    else:
        status = INCONCLUSIVE
    return {
        "status": status,
        "working_scaffold_finite": bool(sample_count > 0 and sample_nonzero > 0),
        "sample_count": sample_count,
        "sample_nonzero": sample_nonzero,
        "sample_value": sample_value,
        "reason": "P9/P10 agreement remains normalization-dependent, not physical truth",
    }


def _phase_status_from_controls() -> str:
    control = _wrong_phase_control()
    return control["status"] if control["status"] != INCONCLUSIVE else PHASE_CONVENTION_DEPENDENT


def _relative_status_from_sources() -> str:
    reduced = reduced_elements_for_kmax1()
    if reduced and all(np.isfinite(value) for value in reduced.values()):
        return RELATIVE_COEFFICIENTS_DERIVED
    return INCONCLUSIVE


def _absolute_status_from_sources() -> str:
    return _evaluate_reduced_normalization_from_ben_achour()["status"]


def _lambda_status_from_sources() -> str:
    return REQUIRES_PHYSICAL_COUPLING_INPUT


def _pattern_level_status_from_prior_art() -> str:
    p11 = p11_external_oracle_matrix_element_derivation_summary()
    p12 = p12_matrix_element_derivation_robustness_audit_summary()
    if p11["comparison_status"] == MATCHES_FROZEN_SCAFFOLD and p12["overall_status"] == ROBUST:
        return DERIVED
    return INCONCLUSIVE


def _exact_coefficients_status(relative_status: str, absolute_status: str) -> str:
    if absolute_status == ABSOLUTE_NORMALIZATION_DERIVED:
        return ABSOLUTE_NORMALIZATION_DERIVED
    if relative_status == RELATIVE_COEFFICIENTS_DERIVED:
        return NORMALIZATION_DEPENDENT
    return INCONCLUSIVE


def build_p13c_reduced_matrix_element_normalization_audit() -> (
    P13CReducedMatrixElementNormalizationAudit
):
    """Return the current P13C normalization audit contract."""

    p13a = p13a_v_operator_ansatz_convention_registry_summary()
    p13a1 = p13a1_ben_achour_one_form_mode_implementation_summary()
    p11 = p11_external_oracle_matrix_element_derivation_summary()
    p12 = p12_matrix_element_derivation_robustness_audit_summary()
    su4 = su4_hypercharge_gauge_audit_summary()

    coefficient_sources = _coefficient_source_records()
    pattern_level_status = _pattern_level_status_from_prior_art()
    relative_status = _relative_status_from_sources()
    absolute_status = _absolute_status_from_sources()
    lambda_status = _lambda_status_from_sources()
    phase_status = _phase_status_from_controls()
    p9_p10_status = _evaluate_p9_p10_comparison_normalization_dependence()["status"]
    normalization_control = _wrong_normalization_control()
    phase_control = _wrong_phase_control()
    exact_status = _exact_coefficients_status(relative_status, absolute_status)
    reduced_audit = _evaluate_reduced_normalization_from_ben_achour()  # noqa: F841
    sample_count, sample_nonzero, sample_value = _sample_reduced_element()

    if exact_status == ABSOLUTE_NORMALIZATION_DERIVED:
        verdict = ABSOLUTE_NORMALIZATION_DERIVED
    elif (
        absolute_status == NORMALIZATION_DEPENDENT
        or lambda_status == REQUIRES_PHYSICAL_COUPLING_INPUT
    ):
        verdict = NORMALIZATION_DEPENDENT
    elif phase_status == PHASE_CONVENTION_DEPENDENT:
        verdict = PHASE_CONVENTION_DEPENDENT
    else:
        verdict = INCONCLUSIVE

    return P13CReducedMatrixElementNormalizationAudit(
        p13a_status=str(p13a["status"]),
        p13a1_status=str(p13a1["status"]),
        p13b_status=P13B_SYMBOLIC_V_MATRIX_ELEMENT_PATTERN_BUILD_STATUS,
        p11_status=str(p11["status"]),
        p12_status=str(p12["status"]),
        su4_status=str(su4["audit_result"]),
        coefficient_sources=coefficient_sources,
        pattern_level_status=pattern_level_status,
        relative_coefficient_status=relative_status,
        absolute_normalization_status=absolute_status,
        lambda_status=lambda_status,
        phase_status=phase_status,
        p9_p10_comparison_status=p9_p10_status,
        normalization_control_status=str(normalization_control["status"]),
        phase_control_status=str(phase_control["status"]),
        exact_coefficients_status=exact_status,
        reduced_matrix_element_status=relative_status,
        reduced_element_sample_count=sample_count,
        reduced_element_sample_nonzero=sample_nonzero,
        reduced_element_sample_value=sample_value,
        verdict=verdict,
    )


def p13c_reduced_matrix_element_normalization_audit_summary() -> dict[str, object]:
    """Return a compact summary suitable for reports and tests."""

    audit = build_p13c_reduced_matrix_element_normalization_audit()
    return {
        "p13a_status": audit.p13a_status,
        "p13a1_status": audit.p13a1_status,
        "p13b_status": audit.p13b_status,
        "p11_status": audit.p11_status,
        "p12_status": audit.p12_status,
        "su4_status": audit.su4_status,
        "coefficient_sources": audit.coefficient_sources,
        "pattern_level_status": audit.pattern_level_status,
        "relative_coefficient_status": audit.relative_coefficient_status,
        "absolute_normalization_status": audit.absolute_normalization_status,
        "lambda_status": audit.lambda_status,
        "phase_status": audit.phase_status,
        "p9_p10_comparison_status": audit.p9_p10_comparison_status,
        "normalization_control_status": audit.normalization_control_status,
        "phase_control_status": audit.phase_control_status,
        "exact_coefficients_status": audit.exact_coefficients_status,
        "reduced_matrix_element_status": audit.reduced_matrix_element_status,
        "reduced_element_sample_count": audit.reduced_element_sample_count,
        "reduced_element_sample_nonzero": audit.reduced_element_sample_nonzero,
        "reduced_element_sample_value": audit.reduced_element_sample_value,
        "verdict": audit.verdict,
        "blocking_fields": audit.blocking_fields,
        "scope": audit.scope,
        "forbidden_claims": audit.forbidden_claims,
        "status": P13C_REDUCED_MATRIX_ELEMENT_NORMALIZATION_AUDIT_STATUS,
        "runtime_status": "research_only",
        "v_selection_status": "smoke_only",
        "safe_for_runtime": False,
    }
