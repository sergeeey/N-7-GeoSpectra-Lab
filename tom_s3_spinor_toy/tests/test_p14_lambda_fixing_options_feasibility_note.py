"""Tests for the P14 lambda-fixing options feasibility note."""

from __future__ import annotations

from p14_lambda_fixing_options_feasibility_note import (
    P14_LAMBDA_FIXING_OPTIONS_FEASIBILITY_NOTE_STATUS,
    S3X_S6_SCALE_RADIUS_RELATION,
    build_p14_lambda_fixing_options_feasibility_note,
    p14_lambda_fixing_options_feasibility_note_summary,
)


def test_p14_summary_records_free_lambda_and_priority_order() -> None:
    summary = p14_lambda_fixing_options_feasibility_note_summary()

    assert summary["status"] == P14_LAMBDA_FIXING_OPTIONS_FEASIBILITY_NOTE_STATUS
    assert summary["registry_status"] == "CONVENTION_REGISTRY_FIXED"
    assert summary["physics_status"] == "PROMOTION_BLOCKED"
    assert summary["lambda_status"] == "FREE_COUPLING_PARAMETER"
    assert summary["p13h_status"] == "passed"
    assert summary["p13h_lambda_status"] == "FREE_COUPLING_PARAMETER"
    assert summary["lambda_fixed"] is False
    assert summary["best_priority_key"] == S3X_S6_SCALE_RADIUS_RELATION
    assert "No option fixes lambda" in summary["overall_conclusion"]
    assert "S3×S6 scale/radius relation" in summary["overall_recommendation"]

    options = summary["options"]
    assert len(options) == 6
    assert [option["recommended_priority"] for option in options] == [1, 2, 3, 4, 5, 6]
    assert options[0]["key"] == S3X_S6_SCALE_RADIUS_RELATION
    assert options[4]["lambda_effect"] == "reinterpret_only"
    assert options[5]["lambda_effect"] == "hypothesis_generation_only"


def test_p14_build_contract_tracks_no_lambda_fix_claim() -> None:
    note = build_p14_lambda_fixing_options_feasibility_note()

    assert note.lambda_fixed is False
    assert note.registry_status == "CONVENTION_REGISTRY_FIXED"
    assert note.physics_status == "PROMOTION_BLOCKED"
    assert note.lambda_status == "FREE_COUPLING_PARAMETER"
    assert note.p13h_lambda_status == "FREE_COUPLING_PARAMETER"
    assert note.best_priority_key == S3X_S6_SCALE_RADIUS_RELATION
    assert "No option fixes lambda" in note.overall_conclusion
    assert note.overall_recommendation.startswith("Start with S3×S6 scale/radius relation")
    assert "Do not treat calibration or ML search as physical proof" in note.overall_recommendation
