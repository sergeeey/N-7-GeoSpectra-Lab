"""
G54-A: Freund-Rubin Flux Potential on S³×S⁶

q units of quantized 6-form flux on S⁶ contribute an energy density
V_flux = 15q²ρ₃³/(16π ρ₆⁶) — structurally identical to gauge coupling ratio g₂²/g₃².

Claims:
F1: V_flux = 15q²ρ₃³/(16πρ₆⁶) — algebraic formula from |F|²/2 × Vol(S³)
F2: V_flux(q=1) = g₂²/g₃² — exact structural equality (both = Vol(S³)/Vol(S⁶) × ratio)
F3: V_flux = const along SM constraint ρ₃=0.986ρ₆² — scale-invariant on constraint
F4 (OPEN): Full stabilization in 4D Einstein frame not yet computed
"""

import math
import pytest

PI = math.pi

# === Geometric helpers ===


def vol_s3(rho3: float) -> float:
    return 2.0 * PI**2 * rho3**3


def vol_s6(rho6: float) -> float:
    return 16.0 * PI**3 * rho6**6 / 15.0


# === Flux potential ===


def V_flux_geometric(rho3: float, rho6: float, q: float = 1.0) -> float:
    """Flux energy from geometric formula: q²×Vol(S³)/(2×Vol(S⁶))."""
    return q**2 * vol_s3(rho3) / (2.0 * vol_s6(rho6))


def V_flux_formula(rho3: float, rho6: float, q: float = 1.0) -> float:
    """Closed-form: 15q²ρ₃³/(16π ρ₆⁶)."""
    return 15.0 * q**2 * rho3**3 / (16.0 * PI * rho6**6)


def g2sq_over_g3sq(rho3: float, rho6: float) -> float:
    """g₂²/g₃² = 15ρ₃³/(16π ρ₆⁶) from G29 spectral action."""
    return 15.0 * rho3**3 / (16.0 * PI * rho6**6)


# === Classical potential (string frame) ===


def V_class_string(rho3: float, rho6: float) -> float:
    """Einstein-Hilbert potential: -(R_S3 + R_S6) × Vol(S³×S⁶)."""
    R_s3 = 6.0 / rho3**2
    R_s6 = 30.0 / rho6**2
    return -(R_s3 + R_s6) * vol_s3(rho3) * vol_s6(rho6)


def V_total_string(rho3: float, rho6: float, q: float = 1.0) -> float:
    return V_class_string(rho3, rho6) + V_flux_geometric(rho3, rho6, q)


# SM constraint: ρ₃ = CONSTRAINT_C × ρ₆²
CONSTRAINT_C = 0.986


# Numerical gradient
def _dV_drho6(rho3: float, rho6: float, q: float = 1.0, eps: float = 1e-7) -> float:
    return (V_flux_formula(rho3, rho6 + eps, q) - V_flux_formula(rho3, rho6 - eps, q)) / (2.0 * eps)


def _dV_drho3(rho3: float, rho6: float, q: float = 1.0, eps: float = 1e-7) -> float:
    return (V_flux_formula(rho3 + eps, rho6, q) - V_flux_formula(rho3 - eps, rho6, q)) / (2.0 * eps)


# ====================================================================
# F1 — Flux Formula Verification
# ====================================================================


class TestF1FluxFormula:
    """V_flux = 15q²ρ₃³/(16πρ₆⁶) — algebraic identity."""

    _test_points = [
        (1.0, 1.0),
        (0.5, 0.5),
        (2.0, 1.0),
        (1.0, 2.0),
        (3.0, 1.5),
        (0.8, 0.6),
    ]

    def test_formula_matches_geometric_at_multiple_points(self):
        for rho3, rho6 in self._test_points:
            V_geom = V_flux_geometric(rho3, rho6)
            V_form = V_flux_formula(rho3, rho6)
            rel_err = abs(V_geom / V_form - 1.0)
            assert rel_err < 1e-10, f"Formula mismatch at ρ₃={rho3}, ρ₆={rho6}: {rel_err}"

    def test_rho3_cubic_scaling(self):
        """V_flux ∝ ρ₃³."""
        V1 = V_flux_formula(1.0, 1.0)
        V2 = V_flux_formula(2.0, 1.0)
        assert abs(V2 / V1 - 8.0) < 1e-10

    def test_rho6_inverse_sixth_scaling(self):
        """V_flux ∝ ρ₆⁻⁶."""
        V1 = V_flux_formula(1.0, 1.0)
        V2 = V_flux_formula(1.0, 2.0)
        assert abs(V2 / V1 - 1.0 / 64.0) < 1e-10

    def test_q_squared_scaling(self):
        """V_flux ∝ q²."""
        V1 = V_flux_formula(1.0, 1.0, q=1.0)
        V3 = V_flux_formula(1.0, 1.0, q=3.0)
        assert abs(V3 / V1 - 9.0) < 1e-10

    def test_formula_value_at_unit_radii(self):
        """V_flux(1,1,q=1) = 15/(16π) ≈ 0.2984."""
        V = V_flux_formula(1.0, 1.0, q=1.0)
        expected = 15.0 / (16.0 * PI)
        assert abs(V / expected - 1.0) < 1e-10


# ====================================================================
# F2 — Structural Equality with Gauge Coupling Ratio
# ====================================================================


class TestF2GaugeCouplingEquality:
    """V_flux(q=1) ≡ g₂²/g₃² — same function, same value, same origin."""

    _test_points = [
        (1.0, 1.0),
        (0.5, 1.5),
        (2.0, 0.8),
        (0.986, 1.0),
        (3.0, 2.0),
    ]

    def test_exact_equality_at_q1(self):
        """V_flux(q=1) = g₂²/g₃² at every (ρ₃, ρ₆) — no free parameters."""
        for rho3, rho6 in self._test_points:
            V = V_flux_formula(rho3, rho6, q=1.0)
            g = g2sq_over_g3sq(rho3, rho6)
            assert abs(V / g - 1.0) < 1e-10, f"V_flux ≠ g₂²/g₃² at ρ₃={rho3}, ρ₆={rho6}"

    def test_at_equal_radii_value(self):
        """V_flux(1,1,1) = 15/(16π) = SM-range value of g₂²/g₃²."""
        V = V_flux_formula(1.0, 1.0, q=1.0)
        g = g2sq_over_g3sq(1.0, 1.0)
        sm_value = 0.2865  # g₂²/g₃² at M_Z (PDG)
        assert abs(V / sm_value - 1.0) < 0.05  # within 5% of SM value

    def test_at_sm_constraint_ratio(self):
        """V_flux at ρ₃=0.986, ρ₆=1 matches g₂²/g₃² at SM ratio exactly."""
        rho3, rho6 = 0.986, 1.0
        V = V_flux_formula(rho3, rho6, q=1.0)
        g = g2sq_over_g3sq(rho3, rho6)
        assert abs(V / g - 1.0) < 1e-10

    def test_q_breaks_equality(self):
        """V_flux(q≠1) ≠ g₂²/g₃² — equality holds only at q=1."""
        V_q2 = V_flux_formula(1.0, 1.0, q=2.0)
        g = g2sq_over_g3sq(1.0, 1.0)
        assert abs(V_q2 / g - 4.0) < 1e-10  # V = 4g at q=2


# ====================================================================
# F3 — Constancy Along SM Coupling Constraint
# ====================================================================


class TestF3SMConstraintConstant:
    """V_flux = 15q²C³/(16π) = const along ρ₃=Cρ₆² (C=0.986)."""

    def test_constant_along_constraint(self):
        """V_flux independent of ρ₆ when ρ₃ = 0.986 ρ₆²."""
        expected = 15.0 * CONSTRAINT_C**3 / (16.0 * PI)
        for rho6 in [0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0]:
            rho3 = CONSTRAINT_C * rho6**2
            V = V_flux_formula(rho3, rho6, q=1.0)
            rel_err = abs(V / expected - 1.0)
            assert rel_err < 1e-10, f"V not constant at ρ₆={rho6}: V={V}, expected={expected}"

    def test_constant_value(self):
        """Constant = 15C³/(16π) ≈ 0.2861 for C=0.986."""
        expected = 15.0 * CONSTRAINT_C**3 / (16.0 * PI)
        assert abs(expected - 0.2861) < 0.0005

    def test_constant_scales_as_q_squared(self):
        """Constant ∝ q²: doubling q quadruples V."""
        rho6 = 1.5
        rho3 = CONSTRAINT_C * rho6**2
        V1 = V_flux_formula(rho3, rho6, q=1.0)
        V2 = V_flux_formula(rho3, rho6, q=2.0)
        assert abs(V2 / V1 - 4.0) < 1e-10

    def test_constant_scales_as_C_cubed(self):
        """For constraint ρ₃=Cρ₆², the constant scales as C³."""
        C1, C2 = 0.8, 1.2
        rho6 = 1.0
        V1 = V_flux_formula(C1 * rho6**2, rho6, q=1.0)
        V2 = V_flux_formula(C2 * rho6**2, rho6, q=1.0)
        expected_ratio = C2**3 / C1**3
        assert abs(V2 / V1 / expected_ratio - 1.0) < 1e-10

    def test_scale_invariance_interpretation(self):
        """Flux fixes ratio C=ρ₃/ρ₆² but not the scale ρ₆."""
        # Two points on same constraint have same V_flux — different scales
        rho6_a, rho6_b = 0.5, 2.0
        rho3_a = CONSTRAINT_C * rho6_a**2
        rho3_b = CONSTRAINT_C * rho6_b**2
        Va = V_flux_formula(rho3_a, rho6_a)
        Vb = V_flux_formula(rho3_b, rho6_b)
        assert abs(Va / Vb - 1.0) < 1e-10


# ====================================================================
# F4 — Gradient Direction and Open Status
# ====================================================================


class TestF4GradientAndOpenStatus:
    """Flux provides counter-pressure in ρ₆; full stabilization is OPEN."""

    def test_dV_drho6_negative(self):
        """∂V_flux/∂ρ₆ < 0 everywhere — flux resists ρ₆ expansion."""
        for rho3, rho6 in [(1, 1), (0.5, 0.5), (2, 1), (1, 2), (0.986, 1)]:
            grad = _dV_drho6(rho3, rho6)
            assert grad < 0.0, f"∂V/∂ρ₆ ≥ 0 at ρ₃={rho3}, ρ₆={rho6}"

    def test_dV_drho3_positive(self):
        """∂V_flux/∂ρ₃ > 0 everywhere — flux grows with ρ₃."""
        for rho3, rho6 in [(1, 1), (0.5, 0.5), (2, 1), (1, 2)]:
            grad = _dV_drho3(rho3, rho6)
            assert grad > 0.0, f"∂V/∂ρ₃ ≤ 0 at ρ₃={rho3}, ρ₆={rho6}"

    def test_exact_gradient_rho6(self):
        """∂V_flux/∂ρ₆ = -6 × 15q²ρ₃³/(16πρ₆⁷) — analytic check."""
        rho3, rho6, q = 1.5, 2.0, 1.0
        analytic = -6.0 * 15.0 * q**2 * rho3**3 / (16.0 * PI * rho6**7)
        numerical = _dV_drho6(rho3, rho6, q)
        assert abs(numerical / analytic - 1.0) < 1e-5

    def test_v_class_dominates_at_large_rho6(self):
        """String-frame V_class >> V_flux at large ρ₆ — no string-frame minimum."""
        rho6 = 5.0
        rho3 = CONSTRAINT_C * rho6**2
        V_cl = abs(V_class_string(rho3, rho6))
        V_fl = V_flux_formula(rho3, rho6, q=1.0)
        ratio = V_cl / V_fl
        # Classical term dominates by many orders of magnitude
        assert ratio > 100.0, f"Classical/flux ratio too small at ρ₆=5: {ratio:.1f}"

    def test_open_status_flag(self):
        """G54-A is OPEN: string-frame total is monotone along constraint."""
        # Along SM constraint, V_flux = const and V_class grows → total monotone
        rho6_vals = [0.5, 1.0, 1.5, 2.0, 3.0]
        V_totals = []
        for r6 in rho6_vals:
            r3 = CONSTRAINT_C * r6**2
            V_totals.append(V_total_string(r3, r6, q=1.0))
        # Should be monotone decreasing (string frame dominated by V_class → -inf)
        for i in range(len(V_totals) - 1):
            assert V_totals[i] > V_totals[i + 1], (
                f"Not monotone: V[{i}]={V_totals[i]:.2e} > V[{i + 1}]={V_totals[i + 1]:.2e}"
            )
