"""Smoke tests for the S6 spectrum baseline contract."""

from __future__ import annotations

from s6_g2_su3_spectrum_baseline import build_s6_spectrum_baseline, s6_spectrum_baseline_summary


def test_s6_spectrum_baseline_preserves_the_operator_fence() -> None:
    """The baseline layer must keep the homogeneous-space identity fixed."""

    baseline = build_s6_spectrum_baseline()

    assert baseline.identity == "S6 ≅ G2 / SU(3)"
    assert baseline.reductive_split == "g2 = su(3) ⊕ m"
    assert baseline.metric_normalization == "unit round S6 normalization"
    assert baseline.connection_choice == "Levi-Civita connection on the canonical homogeneous metric"
    assert baseline.spinor_bundle_convention == "canonical spin structure induced by the G2/SU(3) reductive frame"
    assert baseline.dirac_operator_convention == "homogeneous Dirac operator with Casimir cross-check target"
    assert baseline.casimir_cross_check == "D ~ C_G + (1/8) s"
    assert baseline.spectrum_target == "homogeneous Dirac spectrum on S6, to be derived later"
    assert "spectrum baseline only" in baseline.scope


def test_s6_spectrum_baseline_keeps_the_claim_fence_explicit() -> None:
    """The baseline layer must not drift into forbidden claims."""

    summary = s6_spectrum_baseline_summary()

    assert summary["status"] == "started"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False
    assert summary["scope"] == "S6 spectrum baseline only; no spectrum computed and no gauge claim"

    forbidden_claims = set(summary["forbidden_claims"])
    assert "SU4 gauge decomposition" in forbidden_claims
    assert "hypercharge" in forbidden_claims
    assert "instanton" in forbidden_claims
    assert "index" in forbidden_claims
    assert "chirality" in forbidden_claims
    assert "final spectrum" in forbidden_claims
