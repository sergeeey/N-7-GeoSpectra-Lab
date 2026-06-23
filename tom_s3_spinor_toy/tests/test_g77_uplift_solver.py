from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260622-g77-uplift-solver"
    / "g77_uplift_solver.py"
)
SPEC = importlib.util.spec_from_file_location("g77_uplift_solver", SCRIPT)
assert SPEC and SPEC.loader
G77 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G77)


def test_target_radius_table_reproduces_reference():
    expected_a = {2: 0.4012, 4: 0.4073, 6: 0.4178, 8: 0.4405}
    for power, expected in expected_a.items():
        row = G77.solve_at_target(power, 1.0)
        assert abs(row["A_np"] - expected) < 5e-4
        assert abs(row["V_residual"]) < 1e-14
        assert abs(row["dV_residual"]) < 1e-10
        assert row["local_minimum"]


def test_fixed_amplitude_table_reproduces_reference():
    expected_rho = {2: 1.1964, 4: 1.2222, 6: 1.2644, 8: 1.3459}
    for power, expected in expected_rho.items():
        row = G77.solve_with_fixed_a(power, 1.0)
        assert abs(row["rho0"] - expected) < 5e-4
        assert row["D"] > 0
        assert row["local_minimum"]


def test_repository_and_unit_k_conventions_are_consistent():
    unit = G77.solve_at_target(2, 1.0)
    repo = G77.solve_at_target(2, G77.K_VOL)
    assert abs(unit["D"] / repo["D"] - G77.K_VOL) < 1e-8


def test_wrong_normalization_is_detected():
    unit = G77.solve_at_target(2, 1.0)
    wrong = G77.potential(
        G77.RHO_TARGET,
        amplitude=unit["A_np"],
        uplift_d=unit["D"],
        power=2,
        k=G77.K_VOL,
    )
    assert abs(wrong) > 1e-6


def test_full_gate_passes_with_scoped_verdict():
    result = G77.run()
    assert result["verdict"] == "PASS_ALGEBRAIC_TOY"
    assert all(result["gates"].values())
    assert result["microscopic_uplift_derived"] is False
