from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260623-g88d-full-4d-reduced-action-mass-extraction"
    / "g88d_full_4d_reduced_action_mass_extraction.py"
)
SPEC = importlib.util.spec_from_file_location("g88d_full_4d_reduced_action_mass_extraction", SCRIPT)
assert SPEC and SPEC.loader
G88D = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = G88D
SPEC.loader.exec_module(G88D)


def test_schema_and_allowed_verdict():
    result = G88D.run()
    required = {
        "gate",
        "verdict",
        "searched_terms",
        "files_examined_count",
        "action_sources_found",
        "frame_definitions_found",
        "canonical_field_defined",
        "canonical_normalization_explicit",
        "kk_scale_definition_found",
        "coordinate_proxy_value",
        "canonical_proxy_value",
        "physical_ratio_value",
        "ratio_invariant_under_reparametrization",
        "same_frame_comparison",
        "missing_inputs",
        "falsified_routes",
        "next_required_gate",
        "gates",
        "reproduction_command",
    }
    assert required <= set(result)
    assert result["verdict"] in {
        "PHYSICAL_CONFIRMED",
        "CANONICAL_PROXY_ONLY",
        "COORDINATE_ARTIFACT",
        "INVALID_ACTION",
        "INSUFFICIENT_ACTION",
        "MIXED",
    }


def test_physical_ratio_not_confirmed():
    result = G88D.run()
    assert result["verdict"] == "CANONICAL_PROXY_ONLY"
    assert result["physical_ratio_value"] is None
    assert result["canonical_normalization_explicit"] is True
    assert result["same_frame_comparison"] is False


def test_all_gates_pass():
    assert all(G88D.run()["gates"].values())

