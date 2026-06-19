"""P13H — explicit S3 normalization integral smoke tests."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

from cc_toy_lab.compactification.convention_registry import Classification
from cc_toy_lab.compactification.p13_fixed_inputs import assert_p13_chain_fixed
from cc_toy_lab.compactification.p13h_integral import (
    hermiticity_check_primary_pair,
    matrix_element,
    run_p13h_integral_test,
)
from cc_toy_lab.compactification.p11_p12_pattern import p11_expectation
from cc_toy_lab.compactification.registry_loader import assert_frozen_registry_present
from cc_toy_lab.compactification.s3_lawrence_hopf import VOLUME_DOC, volume_weight


def test_frozen_p13_chain():
    assert_p13_chain_fixed()
    assert_frozen_registry_present()


def test_lawrence_hopf_volume_not_wrong_measure():
    assert "sin(alpha) * cos(alpha)" in VOLUME_DOC
    assert "sin^2" not in VOLUME_DOC.replace("sin(alpha)", "")


def test_volume_weight_formula():
    a = np.linspace(0.1, 1.4, 5)
    w = volume_weight(a)
    expected = np.sin(a) * np.cos(a)
    np.testing.assert_allclose(w, expected, rtol=1e-12)


def test_primary_off_diagonal_zero_p11_pattern():
    i, j = 0, 1
    exp = p11_expectation(i, j)
    assert exp.expected == "zero"
    result = matrix_element(i, j, "CONV_HAAR_UNIT", grid_n=24)
    assert abs(result.coefficient) < 1e-7


def test_hermiticity_primary_pair():
    err = hermiticity_check_primary_pair("CONV_HAAR_UNIT", grid_n=20)
    assert err < 1e-6


def test_diagonal_11_convention_dependent():
    u = matrix_element(1, 1, "CONV_HAAR_UNIT", grid_n=24).coefficient
    s = matrix_element(1, 1, "CONV_HAAR_HARMONIC_SQRT2", grid_n=24).coefficient
    denom = max(abs(u), abs(s), 1e-15)
    rel = abs(s - u) / denom
    assert denom > 1e-9
    # P13G sqrt(2) amplitude convention shifts diagonal scale
    assert rel > 0.1


def test_p13h_classification_normalization_no_go():
    report = run_p13h_integral_test(grid_n=24)
    assert report.p11_pattern_compatible
    assert report.classification in {
        Classification.NORMALIZATION_DEPENDENT_NO_GO,
        Classification.FREE_COUPLING_PARAMETER_CONFIRMED,
    }
    assert report.lambda_role == "FREE_COUPLING_PARAMETER"
    assert report.p13e_status_preserved
    assert report.safe_for_runtime is False
    assert report.selection_rules == "smoke_only"


def test_p13h_script_runs():
    root = Path(__file__).resolve().parents[1]
    proc = subprocess.run(
        [sys.executable, str(root / "scripts/p13h_s3_absolute_normalization_integral_test.py")],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr + proc.stdout
    assert Path("reports/P13H_S3_ABSOLUTE_NORMALIZATION_INTEGRAL_TEST.md").exists()
