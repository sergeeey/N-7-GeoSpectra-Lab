"""Tests for the P13G handoff / limitations package."""

from __future__ import annotations

from p13g_handoff_limitations_and_next_evidence_package import (
    HANDOFF_RECORDED,
    P13G_HANDOFF_LIMITATIONS_AND_NEXT_EVIDENCE_PACKAGE_STATUS,
    build_p13g_handoff_limitations_and_next_evidence_package,
    p13g_handoff_limitations_and_next_evidence_package_summary,
)


def test_p13g_summary_records_final_handoff_and_blocker() -> None:
    summary = p13g_handoff_limitations_and_next_evidence_package_summary()

    assert summary["status"] == "passed"
    assert summary["p13a_status"] == "passed"
    assert summary["p13b1_status"] == "passed"
    assert summary["p13c_status"] == "passed"
    assert summary["p13d_status"] == "passed"
    assert summary["p13e_status"] == "passed"
    assert summary["p13f_status"] == "passed"
    assert summary["p11_status"] == "passed"
    assert summary["p12_status"] == "passed"
    assert summary["p7_status"] == "su4_algebra_audit_passed_with_normalization_dependent_yw"
    assert summary["validated_stack_status"] == "P13A-P13F frozen and consistent"
    assert summary["blocker_status"] == "lambda remains a free coupling parameter"
    assert "fixes lambda" in summary["next_evidence_requirement"]
    assert summary["handoff_status"] == HANDOFF_RECORDED
    assert summary["summary_status"] == P13G_HANDOFF_LIMITATIONS_AND_NEXT_EVIDENCE_PACKAGE_STATUS
    assert "source identities are fixed" in summary["verified_claims"]
    assert "physical V-operator derivation" in summary["not_verified"]


def test_p13g_build_contract_tracks_no_new_derivation() -> None:
    package = build_p13g_handoff_limitations_and_next_evidence_package()

    assert package.handoff_status == HANDOFF_RECORDED
    assert package.summary_status == P13G_HANDOFF_LIMITATIONS_AND_NEXT_EVIDENCE_PACKAGE_STATUS
    assert package.validated_stack_status == "P13A-P13F frozen and consistent"
    assert package.blocker_status == "lambda remains a free coupling parameter"
    assert "fixes lambda" in package.next_evidence_requirement
    assert "physical V-operator derivation" in package.not_verified
    assert "safe_for_runtime" in package.fence[1]

