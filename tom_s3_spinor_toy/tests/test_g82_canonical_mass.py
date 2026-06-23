from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260622-g82-canonical-mass"
    / "g82_canonical_mass.py"
)
SPEC = importlib.util.spec_from_file_location("g82_canonical_mass", SCRIPT)
assert SPEC and SPEC.loader
G82 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G82)


def test_path_kinetic_coefficient():
    assert G82.path_kinetic_coefficient() == 90.0


def test_canonical_hessian_two_paths_agree():
    rho = G82.rho_minimum()
    analytic = G82.canonical_hessian_metric_only(rho)
    numeric = G82.finite_difference_canonical(rho)
    assert abs(analytic - numeric) / analytic < 1e-4


def test_g62_ratio_is_not_yet_canonical():
    result = G82.run()
    assert result["verdict"] == "CONDITIONAL"
    assert result["canonical_mass_ratio_metric_only"] < result["coordinate_mass_ratio_proxy"] / 5
    assert result["physical_mass_ratio_identified"] is False


def test_scale_map_is_explicitly_missing():
    result = G82.run()
    assert any("M4/Ms" in item for item in result["missing_inputs"])
