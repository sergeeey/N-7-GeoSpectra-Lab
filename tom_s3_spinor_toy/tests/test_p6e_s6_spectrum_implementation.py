"""Smoke tests for the S6 spectrum implementation contract."""

from __future__ import annotations

from s6_g2_su3_spectrum_implementation import (
    build_s6_spectrum_implementation,
    s6_spectrum_implementation_summary,
)


def test_s6_spectrum_implementation_preserves_the_spectrum_fence() -> None:
    """The implementation layer must keep the homogeneous-space identity fixed."""

    contract = build_s6_spectrum_implementation()

    assert contract.identity == "S6 ≅ G2 / SU(3)"
    assert contract.reductive_split == "g2 = su(3) ⊕ m"
    assert contract.metric_normalization == "unit round S6 normalization"
    assert contract.connection_choice == "Levi-Civita connection on the canonical homogeneous metric"
    assert contract.spinor_bundle_convention == "canonical spin structure induced by the G2/SU(3) reductive frame"
    assert contract.dirac_operator_convention == "homogeneous Dirac operator with Casimir cross-check target"
    assert contract.casimir_cross_check == "D ~ C_G + (1/8) s"
    assert contract.spectrum_target == "homogeneous Dirac spectrum on S6, to be derived later"
    assert "implementation contract only" in contract.scope


def test_s6_spectrum_implementation_keeps_the_claim_fence_explicit() -> None:
    """The implementation layer must not drift into forbidden claims."""

    summary = s6_spectrum_implementation_summary()

    assert summary["status"] == "started"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False
    assert summary["scope"] == "S6 spectrum implementation contract only; no spectrum or gauge claim"
    assert summary["selection_rules_status"] == "not started"

    forbidden_claims = set(summary["forbidden_claims"])
    assert "SU4 gauge decomposition" in forbidden_claims
    assert "hypercharge" in forbidden_claims
    assert "instanton" in forbidden_claims
    assert "index" in forbidden_claims
    assert "chirality" in forbidden_claims
    assert "final spectrum" in forbidden_claims
