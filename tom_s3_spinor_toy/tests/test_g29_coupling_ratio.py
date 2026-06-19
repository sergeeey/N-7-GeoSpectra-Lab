"""G29 tests: Geometric coupling ratio g2/g3 vs SM values."""

import math


# PDG 2022 SM values
ALPHA_EM_MZ = 1 / 127.951
SIN2_THETA_W = 0.23122
ALPHA_S_MZ = 0.1180

G2_SQ_MZ = 4 * math.pi * ALPHA_EM_MZ / SIN2_THETA_W
G3_SQ_MZ = 4 * math.pi * ALPHA_S_MZ
RATIO_SM_MZ = G2_SQ_MZ / G3_SQ_MZ


def g2_sq_over_g3_sq(rho3: float, rho6: float) -> float:
    """Geometric prediction g2^2/g3^2 = 15*rho3^3/(16*pi*rho6^6)."""
    return 15 * rho3**3 / (16 * math.pi * rho6**6)


def rho_ratio_needed(coupling_ratio: float) -> float:
    """rho3/rho6^2 = (R * 16*pi/15)^{1/3} that gives g2^2/g3^2 = R."""
    return (coupling_ratio * 16 * math.pi / 15) ** (1 / 3)


class TestSMValues:
    def test_g2_MZ(self):
        """g2(M_Z) ~ 0.65 from PDG inputs."""
        g2 = math.sqrt(G2_SQ_MZ)
        assert 0.63 < g2 < 0.67

    def test_g3_MZ(self):
        """g3(M_Z) ~ 1.22 from alpha_s PDG."""
        g3 = math.sqrt(G3_SQ_MZ)
        assert 1.20 < g3 < 1.24

    def test_ratio_SM_less_than_1(self):
        """g2 < g3 at M_Z (observed hierarchy)."""
        assert RATIO_SM_MZ < 1.0

    def test_ratio_SM_MZ_value(self):
        """g2^2/g3^2 at M_Z ~ 0.286 from PDG 2022."""
        assert abs(RATIO_SM_MZ - 0.2865) < 0.002


class TestGeometricPrediction:
    def test_equal_radii_ratio(self):
        """At rho3=rho6=1: g2^2/g3^2 = 15/(16*pi)."""
        predicted = g2_sq_over_g3_sq(1.0, 1.0)
        expected = 15 / (16 * math.pi)
        assert abs(predicted - expected) < 1e-12

    def test_equal_radii_less_than_1(self):
        """Equal-radius prediction gives g2 < g3 (correct hierarchy)."""
        assert g2_sq_over_g3_sq(1.0, 1.0) < 1.0

    def test_equal_radii_within_5pct_of_SM(self):
        """Equal-radius prediction within 5% of SM at M_Z."""
        predicted = g2_sq_over_g3_sq(1.0, 1.0)
        error = abs(predicted / RATIO_SM_MZ - 1.0)
        assert error < 0.05, f"Error {error:.3f} exceeds 5%"

    def test_equal_radii_within_4p5pct_of_SM(self):
        """Tighter bound: within 4.5% of SM (G29 result is +4.3%)."""
        predicted = g2_sq_over_g3_sq(1.0, 1.0)
        error = abs(predicted / RATIO_SM_MZ - 1.0)
        assert error < 0.045


class TestUnificationCondition:
    def test_unification_rho_ratio_exact(self):
        """Unification (g2=g3) requires rho3/rho6^2 = (16*pi/15)^(1/3)."""
        rho_unif = rho_ratio_needed(1.0)
        expected = (16 * math.pi / 15) ** (1 / 3)
        assert abs(rho_unif - expected) < 1e-12

    def test_unification_rho_ratio_numerical(self):
        """Unification radius ~ 1.496."""
        rho_unif = rho_ratio_needed(1.0)
        assert abs(rho_unif - 1.4964) < 1e-3

    def test_at_unification_radius_ratio_is_1(self):
        """At rho3/rho6^2 = (16pi/15)^{1/3} with rho6=1, get g2=g3."""
        rho6 = 1.0
        rho3 = (16 * math.pi / 15) ** (1 / 3)
        ratio = g2_sq_over_g3_sq(rho3, rho6)
        assert abs(ratio - 1.0) < 1e-10


class TestSMMatchRadius:
    def test_rho_ratio_for_SM_MZ(self):
        """ρ₃/ρ₆² needed to match SM at M_Z is 0.986 (near unity)."""
        rho_needed = rho_ratio_needed(RATIO_SM_MZ)
        assert abs(rho_needed - 0.9865) < 1e-3

    def test_SM_match_requires_less_than_2pct_tuning(self):
        """Matching SM at M_Z requires < 2% deviation from equal radii."""
        rho_needed = rho_ratio_needed(RATIO_SM_MZ)
        deviation = abs(1.0 - rho_needed)
        assert deviation < 0.02, f"Deviation {deviation:.4f} > 2%"

    def test_SM_match_requires_less_than_1p5pct_tuning(self):
        """Tighter: matching SM at M_Z within 1.5% of unity."""
        rho_needed = rho_ratio_needed(RATIO_SM_MZ)
        deviation = abs(1.0 - rho_needed)
        assert deviation < 0.015


class TestWindowAnalysis:
    def test_window_MZ_to_GUT(self):
        """ρ₃/ρ₆² increases from ~0.986 (M_Z) to ~1.496 (GUT)."""
        rho_MZ = rho_ratio_needed(RATIO_SM_MZ)
        rho_GUT = rho_ratio_needed(1.0)
        assert rho_MZ < rho_GUT
        assert abs(rho_MZ - 0.9865) < 1e-3
        assert abs(rho_GUT - 1.4964) < 1e-3

    def test_window_span(self):
        """Window spans factor ~1.52 in rho3/rho6^2 from M_Z to GUT."""
        rho_MZ = rho_ratio_needed(RATIO_SM_MZ)
        rho_GUT = rho_ratio_needed(1.0)
        span = rho_GUT / rho_MZ
        assert abs(span - 1.517) < 0.01
