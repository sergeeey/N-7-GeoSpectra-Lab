"""Smoke tests for the S6 implementation contract."""

from __future__ import annotations

from s6_g2_su3_implementation import build_s6_implementation_contract, s6_implementation_summary


def test_s6_implementation_contract_preserves_the_formula_spec_identity() -> None:
    """The implementation layer must keep the homogeneous-space identity fixed."""

    contract = build_s6_implementation_contract()

    assert contract.identity == "S6 ≅ G2 / SU(3)"
    assert contract.reductive_split == "g2 = su(3) ⊕ m"
    assert contract.dirac_baseline == "D ~ C_G + (1/8) s"
    assert "implementation contract only" in contract.scope


def test_s6_implementation_contract_keeps_the_claim_fence_explicit() -> None:
    """The implementation layer must not drift into forbidden claims."""

    summary = s6_implementation_summary()

    assert summary["implementation_status"] == "started"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False
    assert summary["metric_normalization"] == "unit round S6 normalization"
    assert summary["connection_choice"] == "Levi-Civita connection on the canonical homogeneous metric"
    assert summary["spinor_bundle_convention"] == "canonical spin structure induced by the G2/SU(3) reductive frame"
    assert summary["dirac_operator_convention"] == "homogeneous Dirac operator with Casimir cross-check target"
    assert summary["selection_rules_status"] == "not started"

    forbidden_claims = set(summary["forbidden_claims"])
    assert "SU4 gauge decomposition" in forbidden_claims
    assert "hypercharge" in forbidden_claims
    assert "instanton" in forbidden_claims
    assert "index" in forbidden_claims
    assert "chirality" in forbidden_claims
    assert "final spectrum" in forbidden_claims
