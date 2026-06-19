"""G28 tests: Spectral action inner fluctuation on S3 x S6."""

import math

import sympy as sp


def sphere_vol(n: int, rho: float) -> float:
    """Volume of S^n with radius rho."""
    return 2 * math.pi ** ((n + 1) / 2) / math.gamma((n + 1) / 2) * rho**n


def coupling_coefficients(rho3: float, rho6: float):
    """
    Gauge kinetic term coefficients from inner fluctuation.
    Returns (C_SU2, C_SU3) — proportional to 1/g^2.
    """
    N_s3, N_s6 = 2, 8
    c_SU2 = 0.5  # Tr_{2-dim}(T^a T^b) / delta^{ab}
    c_SU3 = 1.0  # Tr_{8-dim}(t^a t^b) / delta^{ab}  (3+3* in SO(6) spinor)

    vol3 = sphere_vol(3, rho3)
    vol6 = sphere_vol(6, rho6)

    C_SU2 = c_SU2 * N_s6 * vol6 / 12
    C_SU3 = c_SU3 * N_s3 * vol3 / 12
    return C_SU2, C_SU3


def gauge_ratio(rho3: float, rho6: float) -> float:
    """g2^2/g3^2 = C_SU3/C_SU2 from geometry."""
    C_SU2, C_SU3 = coupling_coefficients(rho3, rho6)
    return C_SU3 / C_SU2


class TestSphericalData:
    def test_s3_volume_unit(self):
        """Vol(S3) at rho=1 = 2*pi^2."""
        assert abs(sphere_vol(3, 1.0) - 2 * math.pi**2) < 1e-10

    def test_s6_volume_unit(self):
        """Vol(S6) at rho=1 = 16*pi^3/15."""
        expected = 16 * math.pi**3 / 15
        assert abs(sphere_vol(6, 1.0) - expected) < 1e-10

    def test_s3_volume_scales_as_rho3(self):
        """Vol(S3, rho) / Vol(S3, 1) = rho^3."""
        for rho in [0.5, 2.0, 3.0]:
            assert abs(sphere_vol(3, rho) / sphere_vol(3, 1.0) - rho**3) < 1e-10

    def test_s6_volume_scales_as_rho6(self):
        """Vol(S6, rho) / Vol(S6, 1) = rho^6."""
        for rho in [0.5, 2.0]:
            assert abs(sphere_vol(6, rho) / sphere_vol(6, 1.0) - rho**6) < 1e-10


class TestCouplingCoefficients:
    def test_CSU2_unit_radii(self):
        """C_SU2 at rho3=rho6=1: (1/2)*8*(16*pi^3/15)/12 = 16*pi^3/45."""
        C_SU2, _ = coupling_coefficients(1.0, 1.0)
        expected = 16 * math.pi**3 / 45
        assert abs(C_SU2 - expected) < 1e-10

    def test_CSU3_unit_radii(self):
        """C_SU3 at rho3=rho6=1: 1*2*(2*pi^2)/12 = pi^2/3."""
        _, C_SU3 = coupling_coefficients(1.0, 1.0)
        expected = math.pi**2 / 3
        assert abs(C_SU3 - expected) < 1e-10

    def test_CSU2_positive(self):
        """C_SU2 > 0 (correct sign for gauge kinetic term)."""
        C_SU2, _ = coupling_coefficients(1.0, 1.0)
        assert C_SU2 > 0

    def test_CSU3_positive(self):
        """C_SU3 > 0 (correct sign for gauge kinetic term)."""
        _, C_SU3 = coupling_coefficients(1.0, 1.0)
        assert C_SU3 > 0

    def test_CSU2_scales_with_rho6(self):
        """C_SU2 proportional to rho6^6 (controlled by S6 volume)."""
        C_SU2_1, _ = coupling_coefficients(1.0, 1.0)
        C_SU2_2, _ = coupling_coefficients(1.0, 2.0)
        assert abs(C_SU2_2 / C_SU2_1 - 2.0**6) < 1e-10

    def test_CSU3_scales_with_rho3(self):
        """C_SU3 proportional to rho3^3 (controlled by S3 volume)."""
        _, C_SU3_1 = coupling_coefficients(1.0, 1.0)
        _, C_SU3_2 = coupling_coefficients(2.0, 1.0)
        assert abs(C_SU3_2 / C_SU3_1 - 2.0**3) < 1e-10


class TestCouplingRatio:
    def test_ratio_unit_radii(self):
        """g2^2/g3^2 = 15/(16*pi) at equal unit radii."""
        ratio = gauge_ratio(1.0, 1.0)
        expected = 15 / (16 * math.pi)
        assert abs(ratio - expected) < 1e-10

    def test_ratio_less_than_1_at_unit_radii(self):
        """g2 < g3 at equal unit radii (qualitatively correct for SM)."""
        ratio = gauge_ratio(1.0, 1.0)
        assert ratio < 1.0

    def test_ratio_formula(self):
        """g2^2/g3^2 = 15*rho3^3 / (16*pi*rho6^6) — symbolic check."""
        rho3_val, rho6_val = 2.0, 1.5
        ratio_num = gauge_ratio(rho3_val, rho6_val)
        ratio_formula = 15 * rho3_val**3 / (16 * math.pi * rho6_val**6)
        assert abs(ratio_num - ratio_formula) < 1e-10

    def test_ratio_scales_correctly_with_rho3(self):
        """Doubling rho3 multiplies g2^2/g3^2 by 8 (rho3^3 dependence)."""
        r1 = gauge_ratio(1.0, 1.0)
        r2 = gauge_ratio(2.0, 1.0)
        assert abs(r2 / r1 - 8.0) < 1e-10

    def test_ratio_scales_correctly_with_rho6(self):
        """Doubling rho6 divides g2^2/g3^2 by 64 (rho6^6 dependence)."""
        r1 = gauge_ratio(1.0, 1.0)
        r2 = gauge_ratio(1.0, 2.0)
        assert abs(r2 / r1 - 1 / 64.0) < 1e-10


class TestUnificationCondition:
    def test_unification_ratio_equals_1(self):
        """At rho3^3 = (16*pi/15)*rho6^6, the ratio g2^2/g3^2 = 1."""
        rho6 = 1.0
        rho3 = (16 * math.pi / 15 * rho6**6) ** (1 / 3)
        ratio = gauge_ratio(rho3, rho6)
        assert abs(ratio - 1.0) < 1e-10

    def test_unification_rho3_numerical(self):
        """At rho6=1, unification radius rho3 = (16pi/15)^{1/3} ≈ 1.496."""
        rho3_unif = (16 * math.pi / 15) ** (1 / 3)
        assert abs(rho3_unif - 1.4964) < 1e-3

    def test_unification_implies_g2_equals_g3(self):
        """At unification, C_SU2 = C_SU3."""
        rho6 = 1.0
        rho3 = (16 * math.pi / 15) ** (1 / 3)
        C_SU2, C_SU3 = coupling_coefficients(rho3, rho6)
        assert abs(C_SU2 - C_SU3) < 1e-10


class TestSymbolicFormula:
    def test_ratio_sympy_matches_numerical(self):
        """SymPy and numerical g2^2/g3^2 agree at rho3=rho6=1."""
        rho3_s, rho6_s = sp.Symbol("rho3", positive=True), sp.Symbol("rho6", positive=True)

        # Symbolic coupling coefficients
        vol_S3 = 2 * sp.pi**2 * rho3_s**3
        vol_S6 = sp.Rational(16, 15) * sp.pi**3 * rho6_s**6
        C_SU2_s = sp.Rational(1, 2) * 8 * vol_S6 / 12
        C_SU3_s = 1 * 2 * vol_S3 / 12

        ratio_s = sp.simplify(C_SU3_s / C_SU2_s)
        ratio_at_1 = ratio_s.subs({rho3_s: 1, rho6_s: 1})

        # Compare with numerical
        expected = 15 / (16 * math.pi)
        assert abs(float(ratio_at_1.evalf()) - expected) < 1e-10
