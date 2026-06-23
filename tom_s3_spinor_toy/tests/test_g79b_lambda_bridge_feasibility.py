from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260622-g79b-lambda-bridge-feasibility"
    / "g79b_lambda_bridge_feasibility.py"
)
SPEC = importlib.util.spec_from_file_location("g79b_lambda_bridge_feasibility", SCRIPT)
assert SPEC and SPEC.loader
G79B = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G79B)


def test_schema_and_route_set():
    result = G79B.audit()
    assert result["gate"] == "G79B"
    assert result["route_count"] == 5
    assert {row["id"] for row in result["routes"]} == {
        "DIRECT_OPERATOR_MATCHING",
        "DIMENSIONAL_REDUCTION_GAUGE_KINETIC",
        "GAUGINO_CONDENSATION",
        "INSTANTON_ACTION",
        "NUMERICAL_COINCIDENCE",
    }


def test_all_evidence_files_exist():
    result = G79B.audit()
    assert result["missing_evidence"] == []
    assert result["gates"]["G79B-1_evidence_files_exist"]


def test_each_route_has_missing_inputs_and_falsifier():
    result = G79B.audit()
    for route in result["routes"]:
        assert route["required_derivation"]
        assert route["missing_inputs"]
        assert route["falsifier"]


def test_numerical_coincidence_cannot_promote_identity():
    result = G79B.audit()
    row = next(x for x in result["routes"] if x["id"] == "NUMERICAL_COINCIDENCE")
    assert row["current_status"] == "INSUFFICIENT_FOR_IDENTITY"


def test_default_verdict_and_g78_scope():
    result = G79B.audit()
    assert result["verdict"] == "OPEN_MISSING_DERIVATION"
    assert result["verdict"] in G79B.ALLOWED_VERDICTS
    assert result["bridge_derivations_executable_now"] == []
    assert "CONDITIONAL_FOR_LAMBDA_NP" in result["g78_status"]
    assert "BLOCKED_AS_DERIVATION_OF_LAMBDA_V_OPERATOR" in result["g78_status"]
