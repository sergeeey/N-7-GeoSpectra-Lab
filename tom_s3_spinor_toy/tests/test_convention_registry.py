"""Tests for the convention / normalization registry."""

from __future__ import annotations

from convention_registry import (
    convention_record_by_gate,
    convention_registry_summary,
)


def test_convention_registry_summary_has_frozen_fence() -> None:
    summary = convention_registry_summary()

    assert summary["registry_status"] == "CONVENTION_REGISTRY_FIXED"
    assert summary["physics_status"] == "PROMOTION_BLOCKED"
    assert summary["lambda_status"] == "FREE_COUPLING_PARAMETER"
    assert summary["runtime_status"] == "research_only"
    assert summary["safe_for_runtime"] is False
    assert summary["selection_rules"] == "smoke_only"
    assert summary["promotion"] == "forbidden_without_separate_gate"
    assert len(summary["records"]) >= 5


def test_p7_p11_p12_and_s6k_conventions_are_recorded() -> None:
    ben_achour = convention_record_by_gate(
        "BEN_ACHOUR_S3_ONE_FORM_CONVENTION_EXTRACTION"
    )
    p13a1 = convention_record_by_gate(
        "P13A1_BEN_ACHOUR_ONE_FORM_MODE_IMPLEMENTATION"
    )
    p13a = convention_record_by_gate(
        "P13A_V_OPERATOR_ANSATZ_AND_CONVENTION_REGISTRY"
    )
    p13b = convention_record_by_gate(
        "P13B_SYMBOLIC_V_MATRIX_ELEMENT_PATTERN_BUILD"
    )
    p7 = convention_record_by_gate("P7_SU4_HYPERCHARGE_GAUGE_BREAKING_AUDIT")
    p11 = convention_record_by_gate("P11_EXTERNAL_ORACLE_MATRIX_ELEMENT_DERIVATION")
    p12 = convention_record_by_gate("P12_MATRIX_ELEMENT_DERIVATION_ROBUSTNESS_AUDIT")
    s6k = convention_record_by_gate("P6K_S6_SPECTRUM_COMPUTATION")

    assert ben_achour.basis_ordering.startswith("Hopf coordinates")
    assert "one-form basis" in ben_achour.factor_order
    assert "arXiv:1505.03426" in ben_achour.source_convention
    assert ben_achour.status == "SOURCE_SUPPORTED_GEOMETRY"

    assert p13a1.basis_ordering.startswith("Hopf coordinates alpha, theta, phi")
    assert "E/E' low-mode chain" in p13a1.factor_order
    assert p13a1.matrix_convention.startswith("symbolic one-form mode implementation only")
    assert p13a1.status == "BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE"

    assert p13a.basis_ordering.startswith("frozen P9/P10 basis ordering")
    assert "Ben Achour" in p13a.source_convention
    assert "candidate symbolic V ansatz" in p13a.matrix_convention
    assert p13a.status == "SOURCE_SUPPORTED_GEOMETRY"

    assert p13b.basis_ordering.startswith("P13A1 low-mode Ben Achour geometry bridge")
    assert "symbolic zero/nonzero pattern" in p13b.matrix_convention
    assert "P11/P12" in p13b.source_convention
    assert p13b.status == "NORMALIZATION_DEPENDENT"

    assert p7.basis_ordering.startswith("generalized Gell-Mann order")
    assert p7.matrix_convention == "Hermitian generators T_a = lambda_a / 2"
    assert p7.trace_convention == "Tr(T_a T_b) = 1/2 delta_ab"
    assert p7.generator_normalization == "lambda_15 = diag(1,1,1,-3)/sqrt(6)"
    assert p7.hypercharge_normalization.endswith("not promoted")
    assert p7.status == "NORMALIZATION_DEPENDENT"

    assert p11.basis_ordering == "frozen P9/P10 basis ordering"
    assert "Wigner/CG" in p11.matrix_convention
    assert p11.generator_normalization.endswith("normalization-dependent")
    assert p11.status == "NORMALIZATION_DEPENDENT"

    assert p12.phase_convention.startswith("phase-dependent")
    assert p12.generator_normalization.endswith("coefficients")
    assert p12.status == "NORMALIZATION_DEPENDENT"

    assert s6k.basis_ordering.startswith("k ascending")
    assert s6k.trace_convention == "Casimir baseline D ~ C_G + (1/8) s"
    assert s6k.radius_convention == "R = 1 unless explicitly parameterized"
    assert s6k.status == "CONVENTION_FIXED"
