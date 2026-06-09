"""P13A V-operator ansatz and convention registry.

This module freezes the candidate symbolic V ansatz and the conventions needed
for a later symbolic derivation. It does not derive a physical V operator and
does not promote V-selection rules.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Tuple

import ben_achour_one_form_modes as ben_achour_one_form_modes
from ben_achour_scalar_modes import scalar_mode_metadata
from convention_registry import convention_record_by_gate
from convention_registry import BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE
from p11_external_oracle_matrix_element_derivation import p11_external_oracle_matrix_element_derivation_summary
from p12_matrix_element_derivation_robustness_audit import p12_matrix_element_derivation_robustness_audit_summary
from su4_hypercharge_gauge_breaking_audit import su4_hypercharge_gauge_audit_summary


P13A_V_OPERATOR_ANSATZ_AND_CONVENTION_REGISTRY_STATUS: Final[str] = "passed"
P13_READY_FOR_SYMBOLIC_DERIVATION: Final[str] = "P13_READY_FOR_SYMBOLIC_DERIVATION"
REQUIRES_PHYSICAL_INPUT: Final[str] = "REQUIRES_PHYSICAL_INPUT"
SOURCE_SUPPORTED_GEOMETRY: Final[str] = "SOURCE_SUPPORTED_GEOMETRY"


@dataclass(frozen=True)
class P13AVOperatorAnsatzConventionRegistry:
    """Frozen registry of the candidate V-like ansatz and conventions."""

    p11_status: str
    p12_status: str
    source_geometry_status: str
    source_geometry_source: str
    ben_achour_e_modes_status: str
    ben_achour_e_modes_blocker: str
    ben_achour_status: str
    su4_status: str
    coordinate_system: str
    metric_convention: str
    coframe_convention: str
    scalar_mode_convention: str
    killing_vector_convention: str
    one_form_basis_convention: str
    ansatz_expression: str
    field_mapping: str
    basis_ordering: str
    factor_order: str
    gamma_convention: str
    su4_generator_convention: str
    phase_convention: str
    normalization_status: str
    readiness_verdict: str
    physical_promotion_status: str
    blocking_fields: Tuple[str, ...]
    scope: str
    forbidden_claims: Tuple[str, ...] = field(
        default_factory=lambda: (
            "physical V-operator derivation",
            "V-selection promotion",
            "Standard Model reproduced claim",
            "fermion generation claim",
            "safe_for_runtime promotion",
        )
    )


def build_p13a_v_operator_ansatz_convention_registry() -> P13AVOperatorAnsatzConventionRegistry:
    """Return the candidate ansatz and its frozen conventions."""

    p11_summary = p11_external_oracle_matrix_element_derivation_summary()
    p12_summary = p12_matrix_element_derivation_robustness_audit_summary()
    su4_summary = su4_hypercharge_gauge_audit_summary()
    ben_achour = convention_record_by_gate("BEN_ACHOUR_S3_ONE_FORM_CONVENTION_EXTRACTION")

    scalar_meta = scalar_mode_metadata(2, 1, 0)
    return P13AVOperatorAnsatzConventionRegistry(
        p11_status=str(p11_summary["status"]),
        p12_status=str(p12_summary["status"]),
        source_geometry_status=str(ben_achour.status),
        source_geometry_source=str(ben_achour.source_convention),
        ben_achour_e_modes_status=BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE,
        ben_achour_e_modes_blocker=(
            "Executable low-mode E_i/E'_i functions are present; exact normalization remains dependent"
        ),
        ben_achour_status=BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE,
        su4_status=str(su4_summary["audit_result"]),
        coordinate_system="Hopf coordinates (alpha, phi, theta) with Ben Achour source geometry",
        metric_convention="dalpha^2 + cos^2(alpha) dtheta^2 + sin^2(alpha) dphi^2",
        coframe_convention="dalpha, cos(alpha) dtheta, sin(alpha) dphi",
        scalar_mode_convention=(
            "T_{L,m_plus,m_minus} scalar labels with source-supported Jacobi basis "
            f"({scalar_meta['domain']})"
        ),
        killing_vector_convention="xi = partial_phi + partial_theta; xi' = partial_phi - partial_theta",
        one_form_basis_convention="exact and coexact Ben Achour one-form basis E_i, E'_i",
        ansatz_expression="V_S3(x) = lambda * sum_{a,I} gamma^a A_a^I(x) T_I",
        field_mapping=(
            "A_a^I(x) is built from the source-supported Ben Achour one-form basis "
            "E_i / E'_i on S3; exact coefficients are not fixed here"
        ),
        basis_ordering=(
            "frozen P9/P10 basis ordering; S3 basis labels remain plus_plus, "
            "plus_minus, minus_plus, minus_minus"
        ),
        factor_order=(
            "S3 one-form basis × frozen spinor basis × SU4 generators; lexicographic "
            "bridge order inherited from P8"
        ),
        gamma_convention="Euclidean Pauli/Clifford scaffold with fixed factor order",
        su4_generator_convention="Hermitian T_I = lambda_I / 2 with Tr(T_a T_b) = 1/2 delta_ab",
        phase_convention="frozen Wigner/CG phase from P11/P12; no silent phase flips",
        normalization_status=(
            "exact coefficients normalization-dependent; symbolic matrix-element generation is allowed"
        ),
        readiness_verdict=P13_READY_FOR_SYMBOLIC_DERIVATION,
        physical_promotion_status=REQUIRES_PHYSICAL_INPUT,
        blocking_fields=(
            "exact coefficient normalization",
            "explicit physical V-operator density",
            "physical interpretation",
        ),
        scope=(
            "P13A registry only; freezes ansatz and conventions for a later symbolic derivation, "
            "not a physical promotion gate"
        ),
    )


def p13a_v_operator_ansatz_convention_registry_summary() -> dict[str, object]:
    """Return a compact summary suitable for report generation and tests."""

    registry = build_p13a_v_operator_ansatz_convention_registry()
    return {
        "p11_status": registry.p11_status,
        "p12_status": registry.p12_status,
        "source_geometry_status": registry.source_geometry_status,
        "source_geometry_source": registry.source_geometry_source,
        "ben_achour_e_modes_status": registry.ben_achour_e_modes_status,
        "ben_achour_e_modes_blocker": registry.ben_achour_e_modes_blocker,
        "ben_achour_status": registry.ben_achour_status,
        "su4_status": registry.su4_status,
        "coordinate_system": registry.coordinate_system,
        "metric_convention": registry.metric_convention,
        "coframe_convention": registry.coframe_convention,
        "scalar_mode_convention": registry.scalar_mode_convention,
        "killing_vector_convention": registry.killing_vector_convention,
        "one_form_basis_convention": registry.one_form_basis_convention,
        "ansatz_expression": registry.ansatz_expression,
        "field_mapping": registry.field_mapping,
        "basis_ordering": registry.basis_ordering,
        "factor_order": registry.factor_order,
        "gamma_convention": registry.gamma_convention,
        "su4_generator_convention": registry.su4_generator_convention,
        "phase_convention": registry.phase_convention,
        "normalization_status": registry.normalization_status,
        "readiness_verdict": registry.readiness_verdict,
        "physical_promotion_status": registry.physical_promotion_status,
        "blocking_fields": registry.blocking_fields,
        "scope": registry.scope,
        "forbidden_claims": registry.forbidden_claims,
        "status": P13A_V_OPERATOR_ANSATZ_AND_CONVENTION_REGISTRY_STATUS,
    }
