"""Smoke tests for the P7 SU(4) / hypercharge gauge audit contract."""

from __future__ import annotations

import sympy as sp

from su4_hypercharge_gauge_breaking_audit import (
    candidate_yw,
    lambda_15,
    su3c_embedding_generators,
    su4_generators_T,
    su4_hypercharge_gauge_audit_summary,
    build_su4_hypercharge_gauge_audit,
)


def test_su4_generators_are_hermitian_traceless_and_closed() -> None:
    audit = build_su4_hypercharge_gauge_audit()

    assert audit.spin6_su4_relation == "Spin(6) ≅ SU(4)"
    assert audit.algebra_relation == "so(6) ≅ su(4)"
    assert audit.closure_verified is True
    assert audit.hermiticity_verified is True
    assert audit.tracelessness_verified is True
    assert audit.trace_convention_verified is True
    assert audit.audit_result == "su4_algebra_audit_passed_with_normalization_dependent_yw"

    generators = su4_generators_T()
    for g in generators:
        assert sp.simplify(g.trace()) == 0
        assert g == g.H


def test_lambda_15_and_su3_embedding_support_the_audit_convention() -> None:
    audit = build_su4_hypercharge_gauge_audit()

    lam15 = lambda_15()
    yw = candidate_yw()
    su3c = su3c_embedding_generators()

    assert lam15 == sp.diag(1, 1, 1, -3) / sp.sqrt(6)
    assert yw == lam15 / 2
    assert set(audit.lambda_15_eigenvalues) == {sp.sqrt(6) / 6, -sp.sqrt(6) / 2}
    assert all(sp.simplify((g * yw - yw * g)) == sp.zeros(4) for g in su3c)
    assert audit.right_neutrino_invariance.startswith("the 4th basis vector is SU(3)c-singlet")


def test_su4_audit_summary_classifies_claims_without_promotion() -> None:
    summary = su4_hypercharge_gauge_audit_summary()

    assert summary["status"] == "passed"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False
    assert summary["basis_ordering"].startswith("generalized Gell-Mann order")

    mapping = dict(summary["claim_classification"])
    assert mapping["Spin(6) ≅ SU(4) / so(6) ≅ su(4) algebra layer"] == "algebraically_verified"
    assert mapping["SU(4) generator closure"] == "algebraically_verified"
    assert mapping["trace convention"] == "algebraically_verified"
    assert mapping["Hermiticity"] == "algebraically_verified"
    assert mapping["tracelessness"] == "algebraically_verified"
    assert mapping["SU(3)c embedding"] == "basis_ordering_dependent"
    assert mapping["lambda_15 normalization"] == "normalization_dependent"
    assert mapping["candidate Y_W"] == "normalization_dependent"
    assert mapping["right-neutrino invariance"] == "basis_ordering_dependent"
    assert mapping["full fermion generation claim"] == "requires_physical_input"
    assert mapping["Standard Model reproduced claim"] == "requires_physical_input"
    assert mapping["S3xS6 tensor-product coupling claim"] == "requires_tensor_product_S3xS6"
    assert mapping["V-selection promotion"] == "smoke_only"
