from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260623-g88e-kk-scale-frame-consistency"
    / "g88e_kk_scale_frame_consistency.py"
)
SPEC = importlib.util.spec_from_file_location("g88e_kk_scale_frame_consistency", SCRIPT)
assert SPEC and SPEC.loader
G88E = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = G88E
SPEC.loader.exec_module(G88E)


def test_schema_and_allowed_verdict():
    result = G88E.run()
    required = {
        "gate",
        "verdict",
        "frame_definitions_found",
        "kk_scale_definitions",
        "coordinate_proxy_value",
        "canonical_proxy_value",
        "same_frame_comparison",
        "scale_map_explicit",
        "missing_inputs",
        "falsified_routes",
        "next_required_gate",
        "gates",
        "reproduction_command",
    }
    assert required <= set(result)
    assert result["verdict"] in {
        "FRAME_MAP_CLOSED",
        "FRAME_MAP_MISSING",
        "SCALE_CONVENTION_DEPENDENT",
        "INVALID_KK_SCALE",
        "MIXED",
    }


def test_frame_map_is_missing():
    result = G88E.run()
    assert result["verdict"] == "FRAME_MAP_MISSING"
    assert result["same_frame_comparison"] is False
    assert result["scale_map_explicit"] is False


def test_all_gates_pass():
    assert all(G88E.run()["gates"].values())

