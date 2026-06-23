from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260623-g88a-canonical-radion-normalization"
    / "g88a_canonical_radion_normalization.py"
)
SPEC = importlib.util.spec_from_file_location("g88a_canonical_radion_normalization", SCRIPT)
assert SPEC and SPEC.loader
G88A = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = G88A
SPEC.loader.exec_module(G88A)


def test_schema_and_allowed_verdict():
    result = G88A.run()
    required = {
        "gate",
        "verdict",
        "rho_min",
        "path_kinetic_coefficient",
        "coordinate_mass_ratio_proxy",
        "canonical_hessian_metric_only",
        "canonical_mass_ratio_metric_only",
        "canonical_to_coordinate_ratio",
        "finite_difference_canonical_hessian",
        "relative_agreement",
        "physical_mass_ratio_identified",
        "missing_inputs",
        "gates",
        "reproduction_command",
    }
    assert required <= set(result)
    assert result["verdict"] in {"CANONICAL_PROXY_ONLY", "PHYSICAL_CONFIRMED", "COORDINATE_ARTIFACT", "INSUFFICIENT_ACTION", "MIXED"}


def test_canonical_proxy_is_smaller_and_reproducible():
    result = G88A.run()
    assert result["path_kinetic_coefficient"] == 90.0
    assert result["canonical_mass_ratio_metric_only"] < result["coordinate_mass_ratio_proxy"]
    assert result["relative_agreement"] < 1e-4
    assert result["physical_mass_ratio_identified"] is False


def test_all_gates_pass():
    assert all(G88A.run()["gates"].values())
