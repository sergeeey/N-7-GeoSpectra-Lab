from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260622-g76-parameter-registry"
    / "g76_parameter_registry.py"
)
SPEC = importlib.util.spec_from_file_location("g76_parameter_registry", SCRIPT)
assert SPEC and SPEC.loader
G76 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G76)


def test_registry_audit_passes():
    result = G76.audit_registry(G76.load_registry())
    assert result["verdict"] == "PASS"
    assert all(result["gates"].values())


def test_lambda_parameters_are_not_conflated():
    entries = {x["symbol"]: x for x in G76.load_registry()["parameters"]}
    assert entries["lambda_np"]["scope"] != entries["lambda_v_operator"]["scope"]
    assert entries["lambda_np"]["value"] is None
    assert entries["lambda_v_operator"]["value"] is None


def test_external_and_free_parameters_remain_visible():
    entries = {x["symbol"]: x for x in G76.load_registry()["parameters"]}
    assert entries["C_SM"]["provenance"] == "external"
    assert entries["uplift_p"]["class"] == "free"
    assert entries["alpha_casimir"]["class"] == "free"
    assert entries["M4_over_Ms"]["class"] == "free"


def test_amplitudes_are_conditional():
    entries = {x["symbol"]: x for x in G76.load_registry()["parameters"]}
    assert entries["A_np"]["class"] == "conditional"
    assert entries["uplift_D"]["class"] == "conditional"
