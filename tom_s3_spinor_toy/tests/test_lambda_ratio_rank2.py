"""λ-free rank-2 ratio family tests: R₂,A² = 3(j-m+1)/(2(j+m)), R₂,B² = 4(j-m+2)/(j+m-1)."""

import os
import sys

import pytest
import sympy as sp
from sympy.physics.wigner import clebsch_gordan as CG

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-lambda-ratio-rank2"),
)
from lambda_ratio_rank2 import closed_A, closed_B, ratio_A, ratio_B  # noqa: E402

R = sp.Rational

TOWER_SMALL = [
    (R(1), R(0)),
    (R(1), R(1)),
    (R(3, 2), R(-1, 2)),
    (R(3, 2), R(1, 2)),
    (R(3, 2), R(3, 2)),
    (R(2), R(-1)),
    (R(2), R(0)),
    (R(2), R(1)),
    (R(2), R(2)),
]

TOWER_FULL_A = [(R(j2, 2), R(m2, 2)) for j2 in range(2, 9) for m2 in range(-j2 + 2, j2 + 1, 2)]

TOWER_FULL_B = [(j, m) for j, m in TOWER_FULL_A if ratio_B(j, m) is not None]


@pytest.mark.parametrize("j,m", TOWER_SMALL)
def test_closed_A_matches_cg(j, m):
    """R₂,A²(j,m) = 3(j-m+1)/(2(j+m)) agrees with sympy CG at each tower point."""
    numeric = ratio_A(j, m)
    assert numeric is not None, f"ratio_A returned None at j={j}, m={m}"
    predicted = closed_A(j, m)
    assert sp.simplify(numeric - predicted) == 0, (
        f"j={j}, m={m}: numeric={numeric}, predicted={predicted}"
    )


@pytest.mark.parametrize("j,m", TOWER_FULL_A)
def test_closed_A_full_tower(j, m):
    """Closed form R₂,A² verified at all 35 points in j=1..4 tower."""
    numeric = ratio_A(j, m)
    assert sp.simplify(numeric - closed_A(j, m)) == 0


@pytest.mark.parametrize("j,m", TOWER_FULL_B)
def test_closed_B_full_tower(j, m):
    """Closed form R₂,B² = 4(j-m+2)/(j+m-1) verified at all 28 valid tower points."""
    numeric = ratio_B(j, m)
    assert sp.simplify(numeric - closed_B(j, m)) == 0


def test_lambda_free():
    """CG ratio is independent of λ — Wigner-Eckart theorem."""
    lam, vred = sp.symbols("lambda vred", positive=True)
    j0, m0 = R(2), R(1)
    a = CG(j0, 2, j0 + 2, m0, 0, m0)
    b = CG(j0, 2, j0 + 2, m0 - 1, 1, m0)
    ratio_sym = sp.simplify((lam * vred * a) / (lam * vred * b))
    assert sp.diff(ratio_sym, lam) == 0


def test_rank_connection_at_max_m():
    """R₂,A²(j,j) = (3/4) × R₁²(j,j) = 3/(4j) — prefactor is exactly 3/4."""
    jv = sp.Symbol("j", positive=True)
    js, ms = sp.symbols("j m")
    formula = sp.Rational(3, 2) * (js - ms + 1) / (js + ms)
    at_max = sp.simplify(formula.subs([(js, jv), (ms, jv)]))
    expected = sp.Rational(3, 1) / (4 * jv)
    assert sp.simplify(at_max - expected) == 0


def test_R2B_boundary_at_max_m():
    """R₂,B²(j,j) = 8/(2j-1) — e.g. j=1→8, j=2→8/3, j=4→8/7."""
    for j, expected in [(R(1), R(8)), (R(2), R(8, 3)), (R(4), R(8, 7))]:
        val = ratio_B(j, j)
        assert val is not None
        assert sp.simplify(val - expected) == 0, f"j={j}: R₂B²(j,j)={val} ≠ {expected}"


def test_R2A_rank1_proportional():
    """R₂,A²(j,m) = (3/4) R₁²(j,m) at all small tower points."""
    for j, m in TOWER_SMALL:
        r2a = closed_A(j, m)
        r1 = R(2) * (j - m + 1) / (j + m)
        ratio_forms = sp.simplify(r2a / r1)
        assert sp.simplify(ratio_forms - sp.Rational(3, 4)) == 0, (
            f"j={j}, m={m}: R₂A/R₁ = {ratio_forms} ≠ 3/4"
        )


def test_positivity():
    """Both ratios are strictly positive for all valid (j,m) in the tower."""
    for j, m in TOWER_FULL_A:
        assert closed_A(j, m) > 0, f"R₂,A²({j},{m}) ≤ 0"
    for j, m in TOWER_FULL_B:
        assert closed_B(j, m) > 0, f"R₂,B²({j},{m}) ≤ 0"
