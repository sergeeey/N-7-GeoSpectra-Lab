"""G7: tests for S³×S⁶ Kaluza-Klein mass spectrum."""

import sympy as sp
import sys
import os

sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "..", "experiments", "20260615-g7-kk-spectrum")
)
from g7_kk_spectrum import lambda3, lambda6, mass_squared, kk_levels, rho3, rho6


def test_s3_eigenvalues():
    """S³ Dirac eigenvalues: (m+3/2)/ρ₃."""
    assert lambda3(0) == sp.Rational(3, 2) / rho3
    assert lambda3(1) == sp.Rational(5, 2) / rho3
    assert lambda3(2) == sp.Rational(7, 2) / rho3


def test_s6_eigenvalues():
    """S⁶ Dirac eigenvalues: (n+3)/ρ₆ — from G4."""
    assert lambda6(0) == sp.Integer(3) / rho6
    assert lambda6(1) == sp.Integer(4) / rho6
    assert lambda6(2) == sp.Integer(5) / rho6


def test_mass_squared_formula():
    """M²_{mn} = λ₃(m)² + λ₆(n)²."""
    M2 = mass_squared(0, 0)
    expected = sp.Rational(9, 4) / rho3**2 + sp.Integer(9) / rho6**2
    assert sp.simplify(M2 - expected) == 0


def test_no_zero_modes():
    """M²_{mn} > 0 for all m,n ≥ 0 (Lichnerowicz)."""
    for m in range(5):
        for n in range(5):
            M2 = mass_squared(m, n).subs([(rho3, 1), (rho6, 1)])
            assert float(M2) > 0, f"M²({m},{n}) = {M2} ≤ 0"


def test_minimum_at_m0_n0():
    """Lightest mode is at (m=0, n=0)."""
    M2_min = float(mass_squared(0, 0).subs([(rho3, 1), (rho6, 1)]))
    for m in range(4):
        for n in range(4):
            if m == 0 and n == 0:
                continue
            M2 = float(mass_squared(m, n).subs([(rho3, 1), (rho6, 1)]))
            assert M2 > M2_min, f"M²({m},{n})={M2} ≤ M²(0,0)={M2_min}"


def test_minimum_value_exact():
    """M²_min = 45/4 at ρ₃=ρ₆=1."""
    M2 = mass_squared(0, 0).subs([(rho3, 1), (rho6, 1)])
    assert M2 == sp.Rational(45, 4)


def test_s3_excitation_energy():
    """ΔM²(S³) = M²(1,0) - M²(0,0) = 4/ρ₃²."""
    delta = sp.simplify(mass_squared(1, 0) - mass_squared(0, 0))
    assert delta == 4 / rho3**2


def test_s6_excitation_energy():
    """ΔM²(S⁶) = M²(0,1) - M²(0,0) = 7/ρ₆²."""
    delta = sp.simplify(mass_squared(0, 1) - mass_squared(0, 0))
    assert delta == 7 / rho6**2


def test_kk_levels_sorted():
    """kk_levels returns entries sorted by mass² ascending."""
    levels = kk_levels(m_max=3, n_max=3)
    for i in range(len(levels) - 1):
        assert levels[i]["M2_num"] <= levels[i + 1]["M2_num"]


def test_kk_levels_count():
    """kk_levels(m_max=2, n_max=2) returns (2+1)×(2+1)=9 entries."""
    levels = kk_levels(m_max=2, n_max=2)
    assert len(levels) == 9


def test_mass_ratio_exact():
    """M²(1,0)/M²(0,0) = 61/45 at ρ₃=ρ₆=1."""
    ratio = sp.simplify(
        mass_squared(1, 0).subs([(rho3, 1), (rho6, 1)])
        / mass_squared(0, 0).subs([(rho3, 1), (rho6, 1)])
    )
    assert ratio == sp.Rational(61, 45)


def test_radius_ratio_crossover():
    """1a < 1b iff ρ₆/ρ₃ < √(7/4); equality at ρ₆/ρ₃ = √(7/4)."""
    # At crossover: 4/ρ₃² = 7/ρ₆² → (ρ₆/ρ₃)² = 7/4
    crossover_sq = sp.Rational(7, 4)
    rho6_val = sp.sqrt(crossover_sq)  # ρ₃=1
    delta_1a = sp.simplify(
        mass_squared(1, 0).subs([(rho3, 1), (rho6, rho6_val)])
        - mass_squared(0, 0).subs([(rho3, 1), (rho6, rho6_val)])
    )
    delta_1b = sp.simplify(
        mass_squared(0, 1).subs([(rho3, 1), (rho6, rho6_val)])
        - mass_squared(0, 0).subs([(rho3, 1), (rho6, rho6_val)])
    )
    assert sp.simplify(delta_1a - delta_1b) == 0, "1a and 1b should be equal at crossover"
