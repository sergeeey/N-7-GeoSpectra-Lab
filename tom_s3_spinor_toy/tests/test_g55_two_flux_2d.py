"""
G55: Two-flux system (F₃ on S³ + F₆ on S⁶) in full 2D (ρ₃, ρ₆) space.

Extends G54-A (single flux) and G54-F (4D EH frame) to the two-flux case.
Key question: does adding a second flux (F₃ on S³) create a 2D minimum in the
4D Einstein-Hilbert potential, or does the Dine-Seiberg runaway persist?

Formulas:
  V_flux3(ρ₃, ρ₆) = q₃² × vol(S⁶) / (2 × vol(S³)) = (4πq₃²/15) × ρ₆⁶/ρ₃³
  V_flux6(ρ₃, ρ₆) = q₆² × vol(S³) / (2 × vol(S⁶)) = (15q₆²/16π) × ρ₃³/ρ₆⁶

In 4D EH frame, V_int = V_INT_COEFF × ρ₃³ × ρ₆⁶:
  V^EH_flux3 = V_flux3 / V_int = A_F3 / (V_INT_COEFF × ρ₃⁶)  — depends ONLY on ρ₃
  V^EH_flux6 = V_flux6 / V_int = B_F6 / (V_INT_COEFF × ρ₆¹²) — depends ONLY on ρ₆

Gates:
  A1: V^EH_flux3 ∝ 1/ρ₃⁶ (independent of ρ₆)
  A2: V^EH_flux6 ∝ 1/ρ₆¹² (independent of ρ₃)
  A3: V_flux_min = q₃q₆ exactly (AM-GM identity, geometry-independent)
  A4: C_opt = (A_F3/B_F6)^{1/6} ≈ 1.188 ≠ C_SM = 0.986 (flux competition ≠ SM)
  B1: dV^EH_total/dρ₃ < 0 on SM constraint (no minimum at C_SM)
  B2: Off-constraint 2D grid: minimum is at corner (Dine-Seiberg in 2D confirmed)
  B3: V_flux_min / |ζ_FP_max| >> 1 (Casimir too small to compete with unit flux)
"""

from math import sqrt, pi, exp

import numpy as np
from scipy.integrate import quad
from scipy.linalg import lstsq
from scipy.special import comb, digamma

# ── constants ──────────────────────────────────────────────────────────────────
A0_S3 = sqrt(pi) / 2
A2_S3 = -sqrt(pi) / 4
CONSTRAINT_C = 0.986
GAMMA_NEG_HALF = -2.0 * sqrt(pi)
PSI_NEG_HALF = float(digamma(-0.5))
EPS_IREG = 0.10

VOL_S3_COEFF = 2 * pi**2  # vol(S³, r) = 2π²r³
VOL_S6_COEFF = 16 * pi**3 / 15  # vol(S⁶, r) = 16π³r⁶/15
V_INT_COEFF = VOL_S3_COEFF * VOL_S6_COEFF  # V_int = V_INT_COEFF × r3³ × r6⁶

A_F3 = 4 * pi / 15  # V_flux3 = A_F3 × r6⁶/r3³  (q3=1)
B_F6 = 15 / (16 * pi)  # V_flux6 = B_F6 × r3³/r6⁶  (q6=1)

# ── heat kernels ───────────────────────────────────────────────────────────────


def _hs3(tau: float, n: int = 200) -> float:
    return 2.0 * sum((k + 1) * (k + 2) * exp(-tau * (k + 1.5) ** 2) for k in range(n))


def _hs6(tau: float, n: int = 150) -> float:
    return sum(16 * comb(k + 5, 5, exact=True) * exp(-tau * (k + 3) ** 2) for k in range(n))


# ── SW coefficients ────────────────────────────────────────────────────────────

_SW_CACHE: dict | None = None


def _sw() -> dict:
    global _SW_CACHE
    if _SW_CACHE is None:
        tau = np.array([0.005, 0.008, 0.012, 0.018, 0.025, 0.035, 0.050, 0.070, 0.080])
        k = np.array([_hs6(t, n=150) for t in tau])
        basis = np.column_stack(
            [tau ** (-3), tau ** (-2), tau ** (-1), np.ones(len(tau)), tau, tau**2]
        )
        c, *_ = lstsq(basis, k)
        _SW_CACHE = {
            "B0": c[0],
            "B2": c[1],
            "B4": c[2],
            "B6": c[3],
            "B8": c[4],
            "B10": c[5],
        }
    return _SW_CACHE


# ── Hadamard ζ_FP — generalized to arbitrary (r3, r6) ────────────────────────


def _sigma_prime(r3: float, r6: float) -> float:
    sw = _sw()
    A0, A2 = A0_S3, A2_S3
    B0, B2, B4, B6, B8, B10 = sw["B0"], sw["B2"], sw["B4"], sw["B6"], sw["B8"], sw["B10"]
    cns = {
        -4.5: A0 * r3**3 * B0 * r6**6,
        -3.5: A0 * r3**3 * B2 * r6**4 + A2 * r3 * B0 * r6**6,
        -2.5: A0 * r3**3 * B4 * r6**2 + A2 * r3 * B2 * r6**4,
        -1.5: A0 * r3**3 * B6 + A2 * r3 * B4 * r6**2,
        -0.5: A0 * r3**3 * B8 / r6**2 + A2 * r3 * B6,
        1.5: A2 * r3 * B10 / r6**4,
    }
    return sum(cn / (alpha - 0.5) for alpha, cn in cns.items())


def _c_half(r3: float, r6: float) -> float:
    sw = _sw()
    return A0_S3 * r3**3 * sw["B10"] / r6**4 + A2_S3 * r3 * sw["B8"] / r6**2


def _k_sw(t: float, r3: float, r6: float) -> float:
    sw = _sw()
    A0, A2 = A0_S3, A2_S3
    B0, B2, B4, B6, B8, B10 = sw["B0"], sw["B2"], sw["B4"], sw["B6"], sw["B8"], sw["B10"]
    ta = (
        A0
        * r3**3
        * (
            B0 * r6**6 * t ** (-4.5)
            + B2 * r6**4 * t ** (-3.5)
            + B4 * r6**2 * t ** (-2.5)
            + B6 * t ** (-1.5)
            + B8 / r6**2 * t ** (-0.5)
            + B10 / r6**4 * t**0.5
        )
    )
    t2 = (
        A2
        * r3
        * (
            B0 * r6**6 * t ** (-3.5)
            + B2 * r6**4 * t ** (-2.5)
            + B4 * r6**2 * t ** (-1.5)
            + B6 * t ** (-0.5)
            + B8 / r6**2 * t**0.5
            + B10 / r6**4 * t**1.5
        )
    )
    return ta + t2


def _k_full(t: float, r3: float, r6: float) -> float:
    return _hs3(t / r3**2) * _hs6(t / r6**2)


def zeta_fp_2d(r3: float, r6: float) -> float:
    """Hadamard ζ_FP for arbitrary (r3, r6) — off SM constraint."""
    Sig = _sigma_prime(r3, r6)
    Ir, _ = quad(
        lambda t: t ** (-1.5) * (_k_full(t, r3, r6) - _k_sw(t, r3, r6)),
        EPS_IREG,
        1.0,
        limit=200,
        epsabs=1e-9,
        epsrel=1e-7,
    )
    I2, _ = quad(
        lambda t: t ** (-1.5) * _k_full(t, r3, r6),
        1.0,
        50.0,
        limit=100,
        epsabs=1e-12,
        epsrel=1e-10,
    )
    c12 = _c_half(r3, r6)
    return (Sig + Ir + I2 - PSI_NEG_HALF * c12) / GAMMA_NEG_HALF


# ── flux and EH potentials ─────────────────────────────────────────────────────


def v_int(r3: float, r6: float) -> float:
    return V_INT_COEFF * r3**3 * r6**6


def v_flux3(r3: float, r6: float, q3: float = 1.0) -> float:
    """F₃ flux on S³: (q3²/2) × vol(S⁶)/vol(S³)."""
    return q3**2 * A_F3 * r6**6 / r3**3


def v_flux6(r3: float, r6: float, q6: float = 1.0) -> float:
    """F₆ flux on S⁶: (q6²/2) × vol(S³)/vol(S⁶)."""
    return q6**2 * B_F6 * r3**3 / r6**6


def v_eh_flux3(r3: float, r6: float) -> float:
    """V_flux3 in 4D EH frame = A_F3 / (V_INT_COEFF × r3⁶)."""
    return v_flux3(r3, r6) / v_int(r3, r6)


def v_eh_flux6(r3: float, r6: float) -> float:
    """V_flux6 in 4D EH frame = B_F6 / (V_INT_COEFF × r6¹²)."""
    return v_flux6(r3, r6) / v_int(r3, r6)


def v_eh_total_2d(r3: float, r6: float) -> float:
    """V^EH_total = (V_flux3 + V_flux6 + ζ_FP) / V_int."""
    return (v_flux3(r3, r6) + v_flux6(r3, r6) + zeta_fp_2d(r3, r6)) / v_int(r3, r6)


# ── G55 Gate A: Algebraic structure ───────────────────────────────────────────


class TestA1EHFlux3IndepOfR6:
    """V^EH_flux3 = A_F3/(V_INT_COEFF × r3⁶): independent of r6.

    Algebraic reason: V_flux3 = A_F3 × r6⁶/r3³, V_int = M × r3³ × r6⁶.
    V^EH_flux3 = V_flux3/V_int = A_F3/(M × r3⁶) — the r6⁶ factors cancel exactly.
    """

    def test_eh_flux3_ratio_exact_r3_power(self):
        """V^EH_flux3(r3=1.2)/V^EH_flux3(r3=0.8) = (0.8/1.2)^6 exactly."""
        for r6 in [0.8, 1.0, 1.2]:
            r1, r2 = 0.8, 1.2
            ratio = v_eh_flux3(r1, r6) / v_eh_flux3(r2, r6)
            expected = (r2 / r1) ** 6
            assert abs(ratio - expected) / expected < 1e-9, (
                f"r6={r6}: ratio={ratio:.8f} expected={expected:.8f}"
            )

    def test_eh_flux3_independent_of_r6(self):
        """Fixing r3=1.0, V^EH_flux3 is the same for all r6."""
        r3 = 1.0
        veh3_ref = v_eh_flux3(r3, 0.8)
        for r6 in [0.9, 1.0, 1.1, 1.2, 1.3]:
            veh3 = v_eh_flux3(r3, r6)
            assert abs(veh3 - veh3_ref) / veh3_ref < 1e-12, (
                f"V^EH_flux3 varies with r6={r6}: {veh3:.6e} vs {veh3_ref:.6e}"
            )


class TestA2EHFlux6IndepOfR3:
    """V^EH_flux6 = B_F6/(V_INT_COEFF × r6¹²): independent of r3.

    Algebraic reason: V_flux6 = B_F6 × r3³/r6⁶, V_int = M × r3³ × r6⁶.
    V^EH_flux6 = B_F6/(M × r6¹²) — the r3³ factors cancel exactly.
    """

    def test_eh_flux6_ratio_exact_r6_power(self):
        """V^EH_flux6(r6=0.9)/V^EH_flux6(r6=1.1) = (1.1/0.9)^12 exactly."""
        for r3 in [0.7, 1.0, 1.3]:
            r6_a, r6_b = 0.9, 1.1
            ratio = v_eh_flux6(r3, r6_a) / v_eh_flux6(r3, r6_b)
            expected = (r6_b / r6_a) ** 12
            assert abs(ratio - expected) / expected < 1e-9, (
                f"r3={r3}: ratio={ratio:.8f} expected={expected:.8f}"
            )

    def test_eh_flux6_independent_of_r3(self):
        """Fixing r6=1.0, V^EH_flux6 is the same for all r3."""
        r6 = 1.0
        veh6_ref = v_eh_flux6(0.7, r6)
        for r3 in [0.8, 1.0, 1.2, 1.4]:
            veh6 = v_eh_flux6(r3, r6)
            assert abs(veh6 - veh6_ref) / veh6_ref < 1e-12, (
                f"V^EH_flux6 varies with r3={r3}: {veh6:.6e} vs {veh6_ref:.6e}"
            )


class TestA3VfluxMinIdentity:
    """V_flux_min = q₃q₆ exactly — universal AM-GM identity.

    For ANY product manifold S^a × S^b:
      V_flux3 × V_flux6 = q₃²q₆²/4  (algebraic, geometry-independent)
      V_flux3 + V_flux6 ≥ 2√(V_flux3 × V_flux6) = q₃q₆

    Minimum achieved when vol(S³)/vol(S⁶) = q₃/q₆, i.e., r3³/r6⁶ = const.
    For q3=q6=1: V_flux_min = 1 exactly (integer value for integer fluxes).

    Consequence: |ζ_FP| ≈ 10^{-3} << 1 = V_flux_min → Casimir is 1000× too small
    to compete with unit flux. No single-flux or two-flux Casimir stabilization.
    """

    def test_vflux_product_is_quarter_q3sq_q6sq(self):
        """V_flux3 × V_flux6 = q3²q6²/4 for any (r3, r6)."""
        for r3, r6 in [(0.7, 0.9), (1.0, 1.0), (1.3, 1.1)]:
            prod = v_flux3(r3, r6) * v_flux6(r3, r6)
            expected = 1.0 / 4  # q3=q6=1
            assert abs(prod - expected) / expected < 1e-12, (
                f"r3={r3},r6={r6}: product={prod:.6e} expected={expected:.6e}"
            )

    def test_vflux_sum_geq_q3_times_q6(self):
        """V_flux3 + V_flux6 ≥ q₃q₆ = 1 for all (r3, r6)."""
        for r3, r6 in [(0.5, 0.8), (0.7, 0.9), (1.0, 1.0), (1.2, 1.1), (1.5, 1.3)]:
            flux_sum = v_flux3(r3, r6) + v_flux6(r3, r6)
            assert flux_sum >= 1.0 - 1e-12, f"r3={r3},r6={r6}: sum={flux_sum:.6e} < 1"

    def test_vflux_min_equals_1_at_optimal_c(self):
        """At C_opt = (A_F3/B_F6)^{1/6}, V_flux3+V_flux6 = 1 exactly."""
        C_opt = (A_F3 / B_F6) ** (1 / 6)
        r6 = 1.0
        r3 = C_opt * r6**2
        flux_sum = v_flux3(r3, r6) + v_flux6(r3, r6)
        assert abs(flux_sum - 1.0) < 1e-10, f"V_flux_min = {flux_sum:.10f} (expected 1.0)"

    def test_casimir_much_smaller_than_vflux_min(self):
        """|ζ_FP| ≈ 0.00085 << V_flux_min = 1: Casimir is 1000× too small."""
        zfp_on_constraint = abs(zeta_fp_2d(CONSTRAINT_C * 1.0**2, 1.0))
        v_flux_minimum = 1.0  # q3*q6
        ratio = v_flux_minimum / zfp_on_constraint
        assert ratio > 500, f"|ζ_FP|/{V_flux_min} ratio = {ratio:.1f} (expected >> 500)"


class TestA4OptimalCNotSM:
    """Flux competition gives C_opt ≈ 1.188, NOT the SM value C_SM = 0.986.

    The flux competition optimal C = (A_F3/B_F6)^{1/6} = ((4π/15)/(15/(16π)))^{1/6}
    This is determined by the geometry of S³ and S⁶ alone, not by the SM couplings.
    C_SM = 0.986 requires additional physics (e.g., specific q₃/q₆ ratio, or Casimir).
    """

    def test_c_opt_from_flux_competition(self):
        """C_opt = (A_F3/B_F6)^{1/6} ≈ 1.188."""
        C_opt = (A_F3 / B_F6) ** (1 / 6)
        assert 1.18 < C_opt < 1.20, f"C_opt = {C_opt:.4f} (expected ~1.188)"

    def test_c_opt_not_equal_c_sm(self):
        """C_opt ≈ 1.188 ≠ 0.986 (SM): flux competition alone doesn't predict SM."""
        C_opt = (A_F3 / B_F6) ** (1 / 6)
        assert abs(C_opt - CONSTRAINT_C) > 0.1, (
            f"C_opt = {C_opt:.4f} suspiciously close to C_SM = {CONSTRAINT_C}"
        )

    def test_c_sm_requires_nonunit_flux_ratio(self):
        """To get C_SM=0.986, need q₃/q₆ = (C_SM/C_opt)³ (non-integer)."""
        C_opt_at_unit = (A_F3 / B_F6) ** (1 / 6)
        # The optimal C scales as C_opt(q3,q6) = C_opt_unit × (q3/q6)^{1/3}
        # For C = C_SM: q3/q6 = (C_SM/C_opt_unit)^3
        q_ratio_needed = (CONSTRAINT_C / C_opt_at_unit) ** 3
        assert q_ratio_needed < 0.75 or q_ratio_needed > 1.5, (
            f"Non-unit q3/q6 ratio needed: {q_ratio_needed:.4f} (not a simple integer)"
        )


# ── G55 Gate B: 2D gradient and landscape ─────────────────────────────────────


class TestB1GradientAtSMConstraint:
    """dV^EH_total/dρ₃ < 0 everywhere on SM constraint.

    The SM constraint ρ₃ = 0.986 ρ₆² is NOT a minimum of V^EH_total.
    The potential wants to move to larger ρ₃ (gradient pushes off constraint in +ρ₃ direction).
    This confirms Dine-Seiberg is operative not just along the constraint but perpendicular to it.
    """

    def test_gradient_dr3_negative_at_sm_constraint(self):
        """dV^EH/dr3 < 0 at (r3_SM, r6) for three values of r6."""
        dh = 0.02
        for r6 in [0.9, 1.0, 1.1]:
            r3_0 = CONSTRAINT_C * r6**2
            veh_lo = v_eh_total_2d(r3_0 * (1 - dh), r6)
            veh_hi = v_eh_total_2d(r3_0 * (1 + dh), r6)
            grad = (veh_hi - veh_lo) / (2 * r3_0 * dh)
            assert grad < 0, f"r6={r6}: dV^EH/dr3 = {grad:.4e} (expected < 0; no minimum at SM C)"


class TestB2TwoDLandscapeMonotone:
    """Off-constraint scan: V^EH_total is monotone — minimum at corner, not interior.

    On a 3×3 grid spanning the SM constraint (α = r3/(0.986×r6²) ∈ {0.75, 1.0, 1.25}
    and r6 ∈ {0.95, 1.05, 1.15}), the minimum is at (r6=1.15, α=1.25) — the largest
    corner. No interior minimum exists. Dine-Seiberg confirmed in 2D.
    """

    def test_v_total_decreases_along_r6_axis(self):
        """Along SM constraint, V^EH_total(r6=0.9) > V^EH_total(r6=1.0) > V^EH_total(r6=1.1)."""
        vals = [v_eh_total_2d(CONSTRAINT_C * r6**2, r6) for r6 in [0.9, 1.0, 1.1]]
        assert vals[0] > vals[1] > vals[2], (
            f"Not monotone along r6: {vals[0]:.3e} > {vals[1]:.3e} > {vals[2]:.3e}?"
        )

    def test_larger_alpha_gives_smaller_v_on_constraint(self):
        """At fixed r6, increasing α (larger r3 off constraint) reduces V^EH_total.

        This is the Dine-Seiberg direction: no lower bound in the ρ₃ direction.
        """
        r6 = 1.05
        vals = [v_eh_total_2d(alpha * CONSTRAINT_C * r6**2, r6) for alpha in [0.75, 1.0, 1.25]]
        assert vals[0] > vals[1] > vals[2], (
            f"V^EH not decreasing with α: {vals[0]:.3e} > {vals[1]:.3e} > {vals[2]:.3e}?"
        )

    def test_v_total_positive_everywhere_on_grid(self):
        """V^EH_total > 0 on the 3×3 grid — Dine-Seiberg runaway (no AdS minimum)."""
        for r6 in [0.95, 1.05, 1.15]:
            for alpha in [0.75, 1.0, 1.25]:
                r3 = alpha * CONSTRAINT_C * r6**2
                vt = v_eh_total_2d(r3, r6)
                assert vt > 0, f"V^EH_total({r3:.3f},{r6:.2f}) = {vt:.3e} (expected > 0)"


class TestB3CasimirTooSmall:
    """|ζ_FP| << V_flux_min = q₃q₆ everywhere on the 2D grid.

    The Casimir energy is suppressed by ~1000× compared to unit flux.
    Adding a second flux does not change this order-of-magnitude gap.
    Stabilization via Casimir + two-flux is ruled out for integer flux quanta.
    """

    def test_zeta_fp_much_smaller_than_flux_min_off_constraint(self):
        """At all 4 tested off-constraint points, |ζ_FP| < 0.01 × V_flux_min = 0.01."""
        for r6 in [0.85, 1.05]:
            for alpha in [0.75, 1.25]:
                r3 = alpha * CONSTRAINT_C * r6**2
                zfp = abs(zeta_fp_2d(r3, r6))
                assert zfp < 0.01, (
                    f"r3={r3:.3f},r6={r6:.2f}: |ζ_FP|={zfp:.3e} (expected << 0.01 = 1% of V_flux_min)"
                )

    def test_flux3_plus_flux6_geq_1_on_grid(self):
        """V_flux3 + V_flux6 ≥ 1 on all grid points (AM-GM lower bound holds off-constraint)."""
        for r6 in [0.85, 0.95, 1.05, 1.15]:
            for alpha in [0.5, 0.75, 1.0, 1.25, 1.5]:
                r3 = alpha * CONSTRAINT_C * r6**2
                flux_sum = v_flux3(r3, r6) + v_flux6(r3, r6)
                assert flux_sum >= 1.0 - 1e-10, (
                    f"r3={r3:.3f},r6={r6:.2f}: flux_sum={flux_sum:.6f} < 1"
                )
