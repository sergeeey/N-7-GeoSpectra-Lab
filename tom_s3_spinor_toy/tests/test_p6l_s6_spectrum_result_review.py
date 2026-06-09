"""Smoke tests for the S6 spectrum result review contract."""

from __future__ import annotations

from s6_g2_su3_spectrum_result_review import (
    build_s6_spectrum_result_review,
    s6_spectrum_result_review_summary,
)


def test_s6_spectrum_result_review_keeps_the_result_fence_closed() -> None:
    """The review layer must preserve the frozen S6 identity and formulas."""

    review = build_s6_spectrum_result_review()

    assert review.identity == "S6 ≅ G2 / SU(3)"
    assert review.reductive_split == "g2 = su(3) ⊕ m"
    assert review.metric_normalization == "unit round S6 normalization"
    assert review.connection_choice == "Levi-Civita connection on the canonical homogeneous metric"
    assert review.spinor_bundle_convention == "canonical spin structure induced by the G2/SU(3) reductive frame"
    assert review.dirac_operator_convention == "homogeneous Dirac operator with Casimir cross-check target"
    assert review.casimir_cross_check == "D ~ C_G + (1/8) s"
    assert review.spectrum_target == "homogeneous Dirac spectrum on S6, derived as the round-sphere baseline"
    assert review.spectrum_formula == "lambda_{k,+/-} = +/- (k + 3) / R"
    assert review.multiplicity_formula == "mu_k = 8 * binomial(k + 5, k)"
    assert review.computation_status == "started"
    assert "result review only" in review.scope


def test_s6_spectrum_result_review_keeps_the_claim_fence_explicit() -> None:
    """The review layer must not drift into forbidden claims."""

    summary = s6_spectrum_result_review_summary()

    assert summary["status"] == "passed"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False
    assert summary["scope"] == "S6 spectrum result review only; no new spectrum computation or gauge claim"
    assert summary["computation_status"] == "started"

    forbidden_claims = set(summary["forbidden_claims"])
    assert "SU4 gauge decomposition" in forbidden_claims
    assert "hypercharge" in forbidden_claims
    assert "instanton" in forbidden_claims
    assert "index" in forbidden_claims
    assert "chirality" in forbidden_claims
    assert "runtime safe promotion" in forbidden_claims
