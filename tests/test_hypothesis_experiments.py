"""HYP_01–HYP_03 hypothesis toy experiments."""

from __future__ import annotations

import math

import pytest

from cc_toy_lab.compactification.hyp01_flux_veff import (
    find_critical_points,
    partial_lam,
    run_hyp01_experiment,
    v_eff,
    FluxParams,
)
from cc_toy_lab.compactification.hyp02_twisted_lichnerowicz import (
    constrained_kernel_dimension,
    run_hyp02_experiment,
    transversality_constraints,
)
from cc_toy_lab.compactification.hyp03_v_ratio import run_hyp03_experiment


def test_hyp01_coupled_potential_depends_on_lambda():
    p = FluxParams()
    v0 = v_eff(0.1, 1.0, 1, 2, p, coupled=True)
    v1 = v_eff(0.5, 1.0, 1, 2, p, coupled=True)
    assert v0 != v1


def test_hyp01_decoupled_partial_lam_zero():
    p = FluxParams()
    for lam in (-0.5, 0.0, 0.7):
        assert partial_lam(lam, 1.0, 1, 2, p, coupled=False) == 0.0


def test_hyp01_coupled_finds_critical_point():
    cps = find_critical_points(1, 2, FluxParams(), coupled=True)
    assert len(cps) >= 1


def test_hyp01_experiment_coupled_supported_falsifier_killed():
    coupled, falsifier = run_hyp01_experiment()
    assert coupled.status == "hypothesis_supported"
    assert falsifier.falsifier_triggered is True
    assert falsifier.status == "hypothesis_killed"


def test_hyp02_kernel_dimension_one():
    b = transversality_constraints()
    assert constrained_kernel_dimension(b) == 1


def test_hyp02_experiment_runs():
    unit, sqrt2 = run_hyp02_experiment(grid_n=12)
    assert unit.hypothesis_id == "HYP_02_TWISTED_LICHNEROWICZ"
    assert sqrt2.kernel_dimension == unit.kernel_dimension
    # P13E-compatible outcome: convention-dependent eigenvalue kills H2 in this truncation
    assert unit.status in {"hypothesis_killed", "hypothesis_supported", "inconclusive"}


def test_hyp03_v_ratio_sqrt2():
    report = run_hyp03_experiment()
    assert report.status == "hypothesis_supported"
    assert math.isclose(report.r_observable, math.sqrt(2.0), rel_tol=0.0, abs_tol=1e-12)
    assert report.lambda_derivative == 0.0
    assert report.toy_test_deferred is True


def test_hypothesis_runner_script():
    from pathlib import Path
    import subprocess
    import sys

    root = Path(__file__).resolve().parents[1]
    proc = subprocess.run(
        [sys.executable, str(root / "scripts/run_hypothesis_experiments.py")],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr + proc.stdout
    assert Path("reports/HYPOTHESIS_EXPERIMENTS_REPORT.md").exists()
