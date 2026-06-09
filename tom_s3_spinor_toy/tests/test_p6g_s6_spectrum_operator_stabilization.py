"""Smoke tests for the S6 spectrum operator stabilization contract."""

from __future__ import annotations

from s6_g2_su3_spectrum_operator_stabilization import (
    build_s6_spectrum_operator_stabilization,
    s6_spectrum_operator_stabilization_summary,
)


def test_s6_spectrum_operator_stabilization_preserves_the_fence() -> None:
    """The stabilization layer must keep the homogeneous-space identity fixed."""

    stabilization = build_s6_spectrum_operator_stabilization()

    assert stabilization.identity == "S6 ≅ G2 / SU(3)"
    assert stabilization.reductive_split == "g2 = su(3) ⊕ m"
    assert stabilization.spectrum_target == "homogeneous Dirac spectrum on S6, to be derived later"
    assert stabilization.dirac_operator_convention == "homogeneous Dirac operator with Casimir cross-check target"
    assert stabilization.casimir_cross_check == "D ~ C_G + (1/8) s"
    assert stabilization.review_result == "contract_fence_preserved"
    assert stabilization.stabilization_result == "contract_fence_preserved"
    assert "stabilization only" in stabilization.scope


def test_s6_spectrum_operator_stabilization_keeps_the_claim_fence_explicit() -> None:
    """The stabilization layer must not drift into forbidden claims."""

    summary = s6_spectrum_operator_stabilization_summary()

    assert summary["status"] == "started"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False
    assert summary["scope"] == "S6 spectrum operator stabilization only; no spectrum computation or gauge claim"
    assert summary["stabilization_result"] == "contract_fence_preserved"

    forbidden_claims = set(summary["forbidden_claims"])
    assert "SU4 gauge decomposition" in forbidden_claims
    assert "hypercharge" in forbidden_claims
    assert "instanton" in forbidden_claims
    assert "index" in forbidden_claims
    assert "chirality" in forbidden_claims
    assert "final spectrum" in forbidden_claims
