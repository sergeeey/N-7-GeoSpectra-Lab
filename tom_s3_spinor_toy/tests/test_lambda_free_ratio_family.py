"""Tests for the λ-free ratio family R²(j,m) = 2(j−m+1)/(j+m)."""

import os
import sys

import sympy as sp
from sympy.physics.wigner import clebsch_gordan as CG

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(__file__), "..", "experiments", "20260617-lambda-free-ratio-family"
    ),
)
from lambda_free_ratio_family import R2_closed, R2_from_cg  # noqa: E402

R = sp.Rational


def test_closed_form_matches_cg_full_tower():
    """Closed form equals the Clebsch-Gordan ratio at every valid (j,m), j=1/2..3."""
    mismatches = 0
    checked = 0
    for j2 in range(1, 7):
        j = R(j2, 2)
        for m2 in range(-j2, j2 + 1, 2):
            m = R(m2, 2)
            cg = R2_from_cg(j, m)
            if cg is None:
                continue
            checked += 1
            if sp.simplify(cg - R2_closed(j, m)) != 0:
                mismatches += 1
    assert checked >= 15
    assert mismatches == 0


def test_symbolic_closed_form():
    """For general symbolic (j,m), CG-formula ratio reduces to 2(j−m+1)/(j+m)."""
    j, m = sp.symbols("j m", positive=True)
    cgA2 = ((j + 1) ** 2 - m**2) / ((j + 1) * (2 * j + 1))
    cgB2 = ((j + m) * (j + m + 1)) / ((2 * j + 1) * (2 * j + 2))
    assert sp.simplify(cgA2 / cgB2 - 2 * (j - m + 1) / (j + m)) == 0


def test_sqrt2_special_case():
    """R²(1/2,1/2) = 2 recovers the V-RATIO-G0 result R = √2."""
    assert R2_closed(R(1, 2), R(1, 2)) == 2


def test_new_predictions_values():
    """Specific new λ-free ratios from the closed form."""
    assert R2_closed(R(1), R(0)) == 4  # R = 2
    assert R2_closed(R(2), R(0)) == 3  # R = √3
    assert R2_closed(R(2), R(-1)) == 8  # R = 2√2
    assert R2_closed(R(3, 2), R(3, 2)) == R(2, 3)  # R = √6/3


def test_ratio_is_lambda_free():
    """A within-sector matrix-element ratio has zero derivative in λ."""
    lam, vred, geom = sp.symbols("lambda vred geom", positive=True)
    j, m = R(3, 2), R(1, 2)
    a = CG(j, 1, j + 1, m, 0, m)
    b = CG(j, 1, j + 1, m - 1, 1, m)
    ratio = sp.simplify((lam * vred * geom * a) / (lam * vred * geom * b))
    assert sp.diff(ratio, lam) == 0


def test_closed_form_positive_on_tower():
    """Every ratio² in the raising tower is positive (real ratio exists)."""
    for j2 in range(1, 7):
        j = R(j2, 2)
        for m2 in range(-j2, j2 + 1, 2):
            m = R(m2, 2)
            if R2_from_cg(j, m) is None:
                continue
            assert R2_closed(j, m) > 0
