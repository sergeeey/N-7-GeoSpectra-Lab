"""G70: stress-test the KKLT-gap functional form.

The comparison keeps the dimensionless exponent at the UV anchor fixed:
    u_star = a_p / rho_star**p.
This isolates the exponent shape p from the non-perturbative strength.
"""

import csv
import os
import sys
from math import sqrt
from pathlib import Path

import pytest

_EXP_DIR = os.path.join(
    os.path.dirname(__file__),
    "..",
    "experiments",
    "20260621-g70-functional-form",
)
sys.path.insert(0, _EXP_DIR)

from vary_exponent import (  # noqa: E402
    KAPPA_TARGET,
    MAX_RELATIVE_DEVIATION,
    P_VALUES,
    RHO_STAR,
    U_STAR,
    analytic_kappa,
    exponent_coefficient,
    run_scan,
)


@pytest.fixture(scope="module")
def scan_rows():
    return run_scan()


def test_scan_covers_preregistered_exponents(scan_rows):
    assert [row.p for row in scan_rows] == P_VALUES


@pytest.mark.parametrize("p", P_VALUES)
def test_uv_exponent_strength_is_held_fixed(p):
    a_p = exponent_coefficient(p)
    assert a_p / RHO_STAR**p == pytest.approx(U_STAR, rel=0, abs=1e-14)


def test_original_p2_reproduces_g62(scan_rows):
    original = next(row for row in scan_rows if row.p == 2.0)
    assert original.rho_min == pytest.approx(1.179059, abs=1e-5)
    assert original.kappa == pytest.approx(1.081706, abs=1e-5)


@pytest.mark.parametrize("p", P_VALUES)
def test_all_variants_have_an_interior_ads_minimum(scan_rows, p):
    row = next(item for item in scan_rows if item.p == p)
    assert row.rho_min > RHO_STAR
    assert row.v_min < 0
    assert row.second_derivative > 0


@pytest.mark.parametrize("p", P_VALUES)
def test_kappa_stays_within_half_percent_of_s6_target(scan_rows, p):
    row = next(item for item in scan_rows if item.p == p)
    relative_deviation = abs(row.kappa - KAPPA_TARGET) / KAPPA_TARGET
    assert relative_deviation < MAX_RELATIVE_DEVIATION


def test_leading_formula_tracks_numerical_scan(scan_rows):
    for row in scan_rows:
        predicted = analytic_kappa(row.p)
        relative_error = abs(row.kappa - predicted) / row.kappa
        assert relative_error < 0.003


def test_target_is_sqrt_seven_over_six():
    assert KAPPA_TARGET == pytest.approx(sqrt(7 / 6), rel=0, abs=1e-15)


def test_results_csv_matches_computed_scan(scan_rows):
    csv_path = Path(_EXP_DIR) / "results.csv"
    assert csv_path.exists()

    with csv_path.open(newline="", encoding="utf-8") as handle:
        csv_rows = list(csv.DictReader(handle))

    assert len(csv_rows) == len(scan_rows)
    for csv_row, computed in zip(csv_rows, scan_rows, strict=True):
        assert float(csv_row["p"]) == computed.p
        assert float(csv_row["rho_min"]) == pytest.approx(computed.rho_min, abs=5e-7)
        assert float(csv_row["kappa"]) == pytest.approx(computed.kappa, abs=5e-7)
        assert float(csv_row["relative_deviation"]) == pytest.approx(
            computed.relative_deviation,
            abs=5e-9,
        )
