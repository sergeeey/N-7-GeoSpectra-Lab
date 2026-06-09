"""Tests for the P13A V-operator ansatz and convention registry."""

from __future__ import annotations

from p13a_v_operator_ansatz_convention_registry import (
    BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE,
    P13_READY_FOR_SYMBOLIC_DERIVATION,
    REQUIRES_PHYSICAL_INPUT,
    build_p13a_v_operator_ansatz_convention_registry,
    p13a_v_operator_ansatz_convention_registry_summary,
)


def test_p13a_registry_is_concrete_but_not_promoted() -> None:
    summary = p13a_v_operator_ansatz_convention_registry_summary()

    assert summary["status"] == "passed"
    assert summary["readiness_verdict"] == P13_READY_FOR_SYMBOLIC_DERIVATION
    assert summary["physical_promotion_status"] == REQUIRES_PHYSICAL_INPUT
    assert "V_S3(x)" in summary["ansatz_expression"]
    assert "gamma^a A_a^I(x) T_I" in summary["ansatz_expression"]
    assert "Ben Achour" in summary["field_mapping"]
    assert "E_i" in summary["one_form_basis_convention"]
    assert "E'_i" in summary["one_form_basis_convention"]
    assert summary["normalization_status"].startswith(
        "exact coefficients normalization-dependent"
    )
    assert "explicit physical V-operator density" in summary["blocking_fields"]
    assert summary["ben_achour_e_modes_status"] == BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE
    assert "exact normalization remains dependent" in summary["ben_achour_e_modes_blocker"]


def test_p13a_registry_has_frozen_scaffold_inputs() -> None:
    registry = build_p13a_v_operator_ansatz_convention_registry()

    assert registry.p11_status == "passed"
    assert registry.p12_status == "passed"
    assert registry.source_geometry_status == "SOURCE_SUPPORTED_GEOMETRY"
    assert registry.source_geometry_source.endswith("scalar and one-form extraction")
    assert registry.ben_achour_e_modes_status == BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE
    assert registry.coordinate_system.startswith("Hopf coordinates")
    assert registry.metric_convention == "dalpha^2 + cos^2(alpha) dtheta^2 + sin^2(alpha) dphi^2"
    assert registry.coframe_convention == "dalpha, cos(alpha) dtheta, sin(alpha) dphi"
    assert registry.gamma_convention.startswith("Euclidean Pauli/Clifford")
    assert registry.su4_generator_convention == "Hermitian T_I = lambda_I / 2 with Tr(T_a T_b) = 1/2 delta_ab"
    assert registry.readiness_verdict == P13_READY_FOR_SYMBOLIC_DERIVATION
