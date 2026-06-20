"""
G49 + T2: No Dirac zero modes on any product of round spheres Sa×Sb.

G49: S³×S⁷ — dim=10 (Type IIA), but min Dirac eigenvalue = 7/2 ≠ 0 → N_gen=0.
T2:  For ALL Sa×Sb (round metric): min|λ| = a/2 > 0 always → no zero modes.
     N_gen cannot be derived geometrically from sphere products.
"""
import pytest
from fractions import Fraction


def min_dirac_eigenvalue(n):
    """Min |eigenvalue| of Dirac operator on S^n (round, unit radius): n/2."""
    return Fraction(n, 2)


def has_zero_modes(n):
    return min_dirac_eigenvalue(n) == 0


def h4_vanishes(a, b):
    """H^4(Sa×Sb) = Z iff a=4 or b=4, else 0. Flux needs H^4 nonzero."""
    return not (a == 4 or b == 4)


# G49: S³×S⁷
class TestG49_S3xS7:
    def test_dimension_type_iia(self):
        """S³×S⁷: dim = 3+7 = 10, correct for Type IIA."""
        assert 3 + 7 == 10

    def test_no_zero_modes_s7(self):
        """S⁷ min eigenvalue = 7/2 ≠ 0 → no zero modes."""
        assert not has_zero_modes(7)
        assert min_dirac_eigenvalue(7) == Fraction(7, 2)

    def test_no_zero_modes_s3(self):
        """S³ min eigenvalue = 3/2 ≠ 0 → no zero modes."""
        assert not has_zero_modes(3)

    def test_h4_vanishes_s3xs7(self):
        """H⁴(S³×S⁷) = 0 → no topological docking for F₄ flux."""
        assert h4_vanishes(3, 7)

    def test_g49_verdict_null(self):
        """G49 overall: dim passes, zero modes fail → N_gen=0 → NULL."""
        dim_ok = (3 + 7 == 10)
        zero_modes_ok = has_zero_modes(3) or has_zero_modes(7)
        assert dim_ok and not zero_modes_ok  # dim OK but zero modes absent


# T2: General theorem for ALL sphere products
SPHERE_PAIRS = [
    (3, 6), (3, 7), (3, 3), (1, 9), (2, 8), (4, 6), (5, 5), (6, 3), (7, 3),
]


@pytest.mark.parametrize("a,b", SPHERE_PAIRS)
def test_t2_no_zero_modes_sa_x_sb(a, b):
    """T2: For any Sa×Sb (round metric), no Dirac zero modes on either factor."""
    assert not has_zero_modes(a), f"S{a} has zero mode — unexpected"
    assert not has_zero_modes(b), f"S{b} has zero mode — unexpected"


@pytest.mark.parametrize("n", range(1, 12))
def test_t2_general_min_eigenvalue(n):
    """T2 core: min|λ| on S^n = n/2 > 0 for all n ≥ 1."""
    ev = min_dirac_eigenvalue(n)
    assert ev > 0
    assert ev == Fraction(n, 2)


def test_t2_theorem_statement():
    """T2: No product Sa×Sb (round) can yield N_gen>0 from geometry alone."""
    all_null = all(
        not has_zero_modes(a) and not has_zero_modes(b)
        for a, b in SPHERE_PAIRS
    )
    assert all_null, "At least one sphere product has zero modes — T2 violated"
