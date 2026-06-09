"""Smoke tests for the S6 spectrum operator review contract."""

from __future__ import annotations

from s6_g2_su3_spectrum_operator_review import (
    build_s6_spectrum_operator_review,
    s6_spectrum_operator_review_summary,
)


def test_s6_spectrum_operator_review_preserves_the_operator_fence() -> None:
    """The review layer must keep the homogeneous-space identity fixed."""

    review = build_s6_spectrum_operator_review()

    assert review.identity == "S6 ≅ G2 / SU(3)"
    assert review.reductive_split == "g2 = su(3) ⊕ m"
    assert review.spectrum_target == "homogeneous Dirac spectrum on S6, to be derived later"
    assert review.dirac_operator_convention == "homogeneous Dirac operator with Casimir cross-check target"
    assert review.casimir_cross_check == "D ~ C_G + (1/8) s"
    assert review.review_result == "contract_fence_preserved"
    assert "operator review only" in review.scope


def test_s6_spectrum_operator_review_keeps_the_claim_fence_explicit() -> None:
    """The review layer must not drift into forbidden claims."""

    summary = s6_spectrum_operator_review_summary()

    assert summary["status"] == "started"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False
    assert summary["scope"] == "S6 spectrum operator review only; no spectrum computation or gauge claim"
    assert summary["review_result"] == "contract_fence_preserved"

    forbidden_claims = set(summary["forbidden_claims"])
    assert "SU4 gauge decomposition" in forbidden_claims
    assert "hypercharge" in forbidden_claims
    assert "instanton" in forbidden_claims
    assert "index" in forbidden_claims
    assert "chirality" in forbidden_claims
    assert "final spectrum" in forbidden_claims
