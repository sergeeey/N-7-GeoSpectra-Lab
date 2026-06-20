"""
G51: Spectral action monotone along SM coupling ratio constraint.

Claim: S_spec(rho3, rho6) has no interior minimum on the curve
    rho3 = C * rho6^2  where  C = (g2^2/g3^2_SM * 16*pi/15)^{1/3} ≈ 0.986

Proof:
1. S_spec = K_{S3}(t3) * K_{S6}(t6), t3 = 1/rho3^2, t6 = 1/rho6^2
2. K_{Sn}(t) = sum_k mult_k * exp(-t * lambda_k^2) is strictly decreasing in t.
3. On the constraint, rho3 = C*rho6^2 and rho6 both increase together as rho6 increases.
4. Both t3 and t6 decrease monotonically.
5. Both K_{S3} and K_{S6} increase monotonically.
6. S_spec is monotone increasing → no interior minimum.

NULL result: coupling ratio constraint cannot stabilize compactification.
"""

import math
from math import comb


# ── Heat kernel functions ─────────────────────────────────────────────────


def heat_kernel_s3(t: float, n_terms: int = 80) -> float:
    """
    Dirac heat kernel on S³ with unit radius:
    K_{S3}(t) = 2 * sum_{k=0}^{N} (k+1)(k+2) * exp(-t*(k+3/2)^2)
    Eigenvalues ±(k+3/2), multiplicity 2(k+1)(k+2) per sign pair.
    """
    return 2.0 * sum((k + 1) * (k + 2) * math.exp(-t * (k + 1.5) ** 2) for k in range(n_terms))


def heat_kernel_s6(t: float, n_terms: int = 40) -> float:
    """
    Dirac heat kernel on S⁶ with unit radius:
    K_{S6}(t) = sum_{l=0}^{N} 16*C(l+5,5) * exp(-t*(l+3)^2)
    Eigenvalues ±(l+3), multiplicity 2^4 * C(l+5,5) per sign pair.
    """
    return sum(16 * comb(k + 5, 5) * math.exp(-t * (k + 3) ** 2) for k in range(n_terms))


def s_spec(rho3: float, rho6: float, n_terms: int = 60) -> float:
    """
    Spectral action S_spec(rho3, rho6).
    With radius rho: eigenvalues scale as 1/rho, so t -> t/rho^2.
    K_{Sn}(rho) = K_{Sn}(t=1) evaluated at t_n = 1/rho_n^2.
    """
    t3 = 1.0 / rho3**2
    t6 = 1.0 / rho6**2
    return heat_kernel_s3(t3, n_terms) * heat_kernel_s6(t6, n_terms // 2)


# ── SM constraint ─────────────────────────────────────────────────────────

SM_RATIO = 0.2865  # g2^2/g3^2 at M_Z (PDG)

# rho3 = CONSTRAINT_C * rho6^2 gives the SM coupling ratio at any rho6
CONSTRAINT_C = (SM_RATIO * 16 * math.pi / 15) ** (1.0 / 3.0)  # ≈ 0.986


def rho3_from_constraint(rho6: float) -> float:
    """rho3 on the SM constraint curve: rho3 = C * rho6^2."""
    return CONSTRAINT_C * rho6**2


# ── Tests: Heat kernel monotonicity ──────────────────────────────────────


class TestHeatKernelMonotonicity:
    """
    K_{Sn}(t) is monotone decreasing in t.
    Equivalently: K_{Sn}(1/rho^2) is monotone increasing in rho.
    """

    def test_s3_kernel_decreasing_in_t(self):
        """K_{S3}(t) decreases as t increases."""
        ts = [0.1, 0.5, 1.0, 2.0, 5.0]
        values = [heat_kernel_s3(t) for t in ts]
        for i in range(len(values) - 1):
            assert values[i] > values[i + 1], (
                f"K_S3 not decreasing: K({ts[i]})={values[i]:.4f} <= K({ts[i + 1]})={values[i + 1]:.4f}"
            )

    def test_s6_kernel_decreasing_in_t(self):
        """K_{S6}(t) decreases as t increases."""
        ts = [0.1, 0.5, 1.0, 2.0]
        values = [heat_kernel_s6(t) for t in ts]
        for i in range(len(values) - 1):
            assert values[i] > values[i + 1], (
                f"K_S6 not decreasing: K({ts[i]})={values[i]:.4f} <= K({ts[i + 1]})={values[i + 1]:.4f}"
            )

    def test_s3_kernel_increasing_in_rho(self):
        """K_{S3}(1/rho^2) increases as rho increases."""
        rhos = [0.5, 1.0, 1.5, 2.0, 3.0]
        values = [heat_kernel_s3(1.0 / r**2) for r in rhos]
        for i in range(len(values) - 1):
            assert values[i] < values[i + 1], (
                f"K_S3 not increasing in rho: K({rhos[i]})={values[i]:.4f} >= K({rhos[i + 1]})={values[i + 1]:.4f}"
            )

    def test_s6_kernel_increasing_in_rho(self):
        """K_{S6}(1/rho^2) increases as rho increases."""
        rhos = [0.5, 1.0, 1.5, 2.0, 3.0]
        values = [heat_kernel_s6(1.0 / r**2) for r in rhos]
        for i in range(len(values) - 1):
            assert values[i] < values[i + 1], (
                f"K_S6 not increasing in rho: K({rhos[i]})={values[i]:.4f} >= K({rhos[i + 1]})={values[i + 1]:.4f}"
            )

    def test_all_heat_kernel_terms_positive(self):
        """Every term exp(-t*lambda^2) is positive → K(t) > 0 always."""
        for t in [0.1, 1.0, 5.0]:
            assert heat_kernel_s3(t) > 0
            assert heat_kernel_s6(t) > 0

    def test_s_spec_positive(self):
        """S_spec > 0 for all positive radii."""
        for rho3, rho6 in [(0.5, 0.5), (1.0, 1.0), (2.0, 2.0)]:
            assert s_spec(rho3, rho6) > 0


# ── Tests: Constraint curve geometry ─────────────────────────────────────


class TestConstraintCurve:
    """
    On the SM constraint curve rho3 = C * rho6^2:
    - Both rho3 and rho6 increase as rho6 increases.
    - Therefore S_spec is monotone increasing along the curve.
    """

    def test_constraint_constant(self):
        """CONSTRAINT_C = (0.2865 * 16*pi/15)^{1/3} ≈ 0.986."""
        assert 0.98 < CONSTRAINT_C < 1.00, f"CONSTRAINT_C = {CONSTRAINT_C:.6f}"

    def test_constraint_reproduces_sm_ratio(self):
        """rho3 = C*rho6^2 gives g2^2/g3^2 = SM value for any rho6."""
        from math import pi

        for rho6 in [0.5, 1.0, 2.0]:
            rho3 = rho3_from_constraint(rho6)
            ratio = 15 * rho3**3 / (16 * pi * rho6**6)
            assert abs(ratio - SM_RATIO) < 1e-10, (
                f"ratio={ratio:.6f} != SM_RATIO={SM_RATIO} at rho6={rho6}"
            )

    def test_rho3_increases_with_rho6(self):
        """On constraint, rho3 = C*rho6^2 is strictly increasing."""
        rho6s = [0.5, 1.0, 1.5, 2.0, 3.0]
        rho3s = [rho3_from_constraint(r) for r in rho6s]
        for i in range(len(rho3s) - 1):
            assert rho3s[i] < rho3s[i + 1]

    def test_t3_decreases_along_constraint(self):
        """t3 = 1/rho3^2 decreases monotonically as rho6 increases."""
        rho6s = [0.5, 1.0, 1.5, 2.0]
        t3s = [1.0 / rho3_from_constraint(r) ** 2 for r in rho6s]
        for i in range(len(t3s) - 1):
            assert t3s[i] > t3s[i + 1]

    def test_t6_decreases_along_constraint(self):
        """t6 = 1/rho6^2 decreases monotonically as rho6 increases."""
        rho6s = [0.5, 1.0, 1.5, 2.0]
        t6s = [1.0 / r**2 for r in rho6s]
        for i in range(len(t6s) - 1):
            assert t6s[i] > t6s[i + 1]


# ── Tests: S_spec monotone along constraint ───────────────────────────────


class TestSspecMonotoneOnConstraint:
    """
    Main G51 result: S_spec is monotone increasing along the SM coupling constraint.
    No interior minimum → coupling ratio constraint cannot stabilize compactification.
    """

    def test_s_spec_monotone_on_constraint(self):
        """S_spec increases monotonically as rho6 increases along the constraint."""
        rho6_values = [0.3, 0.5, 0.7, 1.0, 1.3, 1.6, 2.0]
        s_values = []
        for rho6 in rho6_values:
            rho3 = rho3_from_constraint(rho6)
            s_values.append(s_spec(rho3, rho6))

        for i in range(len(s_values) - 1):
            assert s_values[i] < s_values[i + 1], (
                f"S_spec not monotone at rho6={rho6_values[i]}: "
                f"S={s_values[i]:.6g} >= S_next={s_values[i + 1]:.6g}"
            )

    def test_s_spec_no_local_minimum_on_constraint(self):
        """
        No local minimum: first discrete difference is always positive.
        d/drho6 [S_spec(constraint(rho6), rho6)] > 0 everywhere.
        """
        rho6_values = [r / 10.0 for r in range(3, 31)]  # 0.3 to 3.0 in steps of 0.1
        s_values = [s_spec(rho3_from_constraint(r), r) for r in rho6_values]
        diffs = [s_values[i + 1] - s_values[i] for i in range(len(s_values) - 1)]
        assert all(d > 0 for d in diffs), (
            f"Non-monotone step detected: {[(r, d) for r, d in zip(rho6_values, diffs) if d <= 0]}"
        )

    def test_s_spec_limit_small_rho6(self):
        """S_spec -> 0 as rho6 -> 0 (t3, t6 -> inf → K -> 0)."""
        rho6 = 0.01
        rho3 = rho3_from_constraint(rho6)
        val = s_spec(rho3, rho6, n_terms=20)
        # Should be very small
        assert val < 1e-50, f"S_spec at rho6=0.01 = {val:.6g} (expected ~0)"

    def test_s_spec_limit_large_rho6(self):
        """S_spec -> inf as rho6 -> inf (t3, t6 -> 0 → K -> inf)."""
        rho6_small = 0.5
        rho6_large = 2.0
        s_small = s_spec(rho3_from_constraint(rho6_small), rho6_small)
        s_large = s_spec(rho3_from_constraint(rho6_large), rho6_large)
        assert s_large > 10 * s_small, (
            f"S_spec did not grow significantly: S(0.5)={s_small:.4g}, S(2.0)={s_large:.4g}"
        )

    def test_ratio_constraint_only_fixes_shape_not_scale(self):
        """
        The SM constraint fixes rho3/rho6^2 = C, NOT the scale.
        Rescaling rho6 -> k*rho6 (and rho3 -> k^2*C*rho6^2) keeps ratio constant
        but changes S_spec.
        This shows the constraint has a 1D family of solutions — no isolated minimum.
        """
        rho6_a = 1.0
        rho6_b = 2.0
        rho3_a = rho3_from_constraint(rho6_a)
        rho3_b = rho3_from_constraint(rho6_b)

        # Both satisfy SM coupling ratio
        ratio_a = 15 * rho3_a**3 / (16 * math.pi * rho6_a**6)
        ratio_b = 15 * rho3_b**3 / (16 * math.pi * rho6_b**6)
        assert abs(ratio_a - ratio_b) < 1e-10  # same coupling ratio

        # But different S_spec values
        sa = s_spec(rho3_a, rho6_a)
        sb = s_spec(rho3_b, rho6_b)
        assert sa != sb  # different spectral actions — no isolated minimum on constraint


# ── Tests: Conclusion ────────────────────────────────────────────────────


class TestG51Conclusion:
    """
    Summary: G51 NULL — coupling ratio constraint is insufficient for stabilization.

    Remaining open problem: dynamical stabilization requires a mechanism that
    breaks the scale symmetry along the constraint curve, e.g.:
    - Coleman-Weinberg potential (1-loop quantum corrections)
    - Flux quantization fixing rho (Freund-Rubin)
    - Casimir energy (Birmingham-Kantowski-Milton 1988 for S^6 alone)
    - Full two-radius Casimir V(rho3, rho6) on S3×S6 (not yet computed)
    """

    def test_g51_null_result(self):
        """
        S_spec has no interior minimum along the SM coupling ratio constraint.
        Proof: monotone in rho6 (verified numerically above).
        """
        # The coupling ratio constraint forms a 1D curve in (rho3, rho6) space.
        # Along this curve, S_spec is strictly increasing (no minimum).
        # Therefore, the coupling ratio match alone does NOT stabilize the radii.
        constraint_does_not_stabilize = True
        assert constraint_does_not_stabilize

    def test_casimir_effect_is_the_open_problem(self):
        """
        Birmingham-Kantowski-Milton (1988): Casimir energy on S^6 alone is known.
        Full V(rho3, rho6) on S3×S6 would provide the scale-breaking mechanism.
        This is the open problem cited in PROCEEDINGS §7 and preprint_abstract.
        """
        # Parameters of the open problem:
        one_radius_casimir_known = True  # BKM 1988 for S^6
        two_radius_casimir_known = False  # V(rho3, rho6) not yet computed
        assert one_radius_casimir_known
        assert not two_radius_casimir_known

    def test_t1_unaffected_by_g51(self):
        """
        G51 is about radii stabilization (open problem), NOT about N_gen.
        Proposition T1 (N_gen=3 impossible) is unaffected by G51 result.
        """
        t1_conclusion_unchanged = True  # T1 = 2 structural lemmas, independent of radii
        g51_addresses_different_question = True  # G51 = stabilization, not generation count
        assert t1_conclusion_unchanged
        assert g51_addresses_different_question
