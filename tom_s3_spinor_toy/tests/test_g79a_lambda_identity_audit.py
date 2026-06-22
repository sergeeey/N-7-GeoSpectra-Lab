from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260622-g79a-lambda-identity-audit"
    / "g79a_lambda_identity_audit.py"
)
SPEC = importlib.util.spec_from_file_location("g79a_lambda_identity_audit", SCRIPT)
assert SPEC and SPEC.loader
G79A = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G79A)


def test_json_schema_and_required_fields():
    result = G79A.audit()
    required = {
        "gate",
        "verdict",
        "occurrence_count",
        "classification_counts",
        "ambiguous_count",
        "identity_assertions",
        "gates",
        "occurrences",
    }
    assert required <= set(result)
    assert result["gate"] == "G79A"
    assert result["occurrence_count"] == len(result["occurrences"])


def test_no_new_ambiguous_lambda_usage():
    """Fails when a new lambda occurrence lacks a deterministic classification."""
    result = G79A.audit()
    assert result["ambiguous_count"] == 0, result["ambiguous_occurrences"][:10]
    assert result["gates"]["G79A-2_no_ambiguous_occurrences"]


def test_unknown_context_is_classified_ambiguous():
    classification, _ = G79A.classify_occurrence(
        "new_module.md",
        "The physical lambda controls this newly introduced mechanism.",
    )
    assert classification == "AMBIGUOUS"


def test_both_lambda_sectors_are_present():
    result = G79A.audit()
    counts = result["classification_counts"]
    assert counts["V_OPERATOR_COUPLING"] > 0
    assert counts["NP_EXPONENT"] > 0


def test_final_verdict_is_allowed_and_scoped():
    result = G79A.audit()
    assert result["verdict"] in G79A.ALLOWED_VERDICTS
    assert result["verdict"] == "OPEN_IDENTITY_UNPROVEN"
    assert result["explicit_identity_derivation_found"] is False
