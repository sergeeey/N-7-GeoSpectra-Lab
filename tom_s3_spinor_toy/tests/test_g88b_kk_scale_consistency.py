from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260623-g88b-kk-scale-consistency"
    / "g88b_kk_scale_consistency.py"
)
SPEC = importlib.util.spec_from_file_location("g88b_kk_scale_consistency", SCRIPT)
assert SPEC and SPEC.loader
G88B = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = G88B
SPEC.loader.exec_module(G88B)


def test_schema_and_allowed_verdict():
    result = G88B.run()
    required = {
        "gate",
        "verdict",
        "rho_min",
        "mkk_string",
        "mmod_string",
        "coordinate_mass_ratio_proxy",
        "canonical_mass_ratio_metric_only",
        "canonical_to_coordinate_ratio",
        "path_kinetic_coefficient",
        "physical_mass_ratio_identified",
        "missing_inputs",
        "gates",
        "reproduction_command",
    }
    assert required <= set(result)
    assert result["verdict"] in {"SCALE_MAP_CLOSED", "SCALE_MAP_OPEN", "SCALE_CONVENTION_DEPENDENT", "INVALID_KK_COMPARISON", "MIXED"}


def test_ratio_is_convention_dependent_and_open():
    result = G88B.run()
    assert result["physical_mass_ratio_identified"] is False
    assert result["canonical_mass_ratio_metric_only"] < result["coordinate_mass_ratio_proxy"]
    assert result["canonical_to_coordinate_ratio"] < 0.2


def test_all_gates_pass():
    assert all(G88B.run()["gates"].values())
