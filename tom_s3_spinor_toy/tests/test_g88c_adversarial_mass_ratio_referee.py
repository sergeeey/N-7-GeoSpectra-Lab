from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260623-g88c-adversarial-mass-ratio-referee"
    / "g88c_adversarial_mass_ratio_referee.py"
)
SPEC = importlib.util.spec_from_file_location("g88c_adversarial_mass_ratio_referee", SCRIPT)
assert SPEC and SPEC.loader
G88C = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = G88C
SPEC.loader.exec_module(G88C)


def test_schema_and_allowed_verdict():
    result = G88C.run()
    required = {
        "gate",
        "verdict",
        "reference_value_verdict",
        "old_coordinate_ratio",
        "canonical_metric_only_ratio",
        "canonical_to_coordinate_ratio",
        "physical_mass_ratio_identified",
        "missing_inputs",
        "gates",
        "reproduction_command",
    }
    assert required <= set(result)
    assert result["verdict"] in {"PHYSICAL_CONFIRMED", "CANONICAL_PROXY_ONLY", "COORDINATE_ARTIFACT", "INSUFFICIENT_ACTION", "INVALID_COMPARISON", "MIXED"}


def test_referee_classification_is_adversarial_and_not_physical():
    result = G88C.run()
    assert result["verdict"] == "CANONICAL_PROXY_ONLY"
    assert result["reference_value_verdict"] == "COORDINATE_ARTIFACT"
    assert result["physical_mass_ratio_identified"] is False


def test_all_gates_pass():
    assert all(G88C.run()["gates"].values())
