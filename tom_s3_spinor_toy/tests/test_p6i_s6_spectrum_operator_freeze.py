"""Smoke tests for the S6 spectrum operator freeze contract."""

from __future__ import annotations

from s6_g2_su3_spectrum_operator_freeze import (
    build_s6_spectrum_operator_freeze,
    s6_spectrum_operator_freeze_summary,
)


def test_s6_spectrum_operator_freeze_preserves_the_fence() -> None:
    """The freeze layer must keep the homogeneous-space identity fixed."""

    freeze = build_s6_spectrum_operator_freeze()

    assert freeze.identity == "S6 ≅ G2 / SU(3)"
    assert freeze.reductive_split == "g2 = su(3) ⊕ m"
    assert freeze.spectrum_target == "homogeneous Dirac spectrum on S6, to be derived later"
    assert freeze.dirac_operator_convention == "homogeneous Dirac operator with Casimir cross-check target"
    assert freeze.casimir_cross_check == "D ~ C_G + (1/8) s"
    assert freeze.review_result == "contract_fence_preserved"
    assert freeze.stabilization_result == "contract_fence_preserved"
    assert freeze.lockdown_result == "contract_fence_preserved"
    assert freeze.freeze_result == "contract_fence_preserved"
    assert "freeze only" in freeze.scope


def test_s6_spectrum_operator_freeze_keeps_the_claim_fence_explicit() -> None:
    """The freeze layer must not drift into forbidden claims."""

    summary = s6_spectrum_operator_freeze_summary()

    assert summary["status"] == "started"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False
    assert summary["scope"] == "S6 spectrum operator freeze only; no spectrum computation or gauge claim"
    assert summary["freeze_result"] == "contract_fence_preserved"

    forbidden_claims = set(summary["forbidden_claims"])
    assert "SU4 gauge decomposition" in forbidden_claims
    assert "hypercharge" in forbidden_claims
    assert "instanton" in forbidden_claims
    assert "index" in forbidden_claims
    assert "chirality" in forbidden_claims
    assert "final spectrum" in forbidden_claims
