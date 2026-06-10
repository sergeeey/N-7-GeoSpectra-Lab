"""Tests for BG-H1-E1 product proxy gate.

Tests cover:
  1. analytic_gap formula correctness (closed-form values)
  2. product_gap formula math
  3. gap_rel_error computation
  4. s3_ground_eigenvalue convergence (reuses E0 FD operator)
  5. Primary gate: δ_disc(R) vs δ_analytic(R) for both spin structures
  6. Negative control: periodic m=0 ground state δ=0
  7. Grid convergence: monotone decrease as N_alpha grows
  8. Edge behavior: large-R and small-R limits
  9. Kronecker sum identity (machine precision)
  10. Scope guards: no forbidden claims in gate output
"""

from __future__ import annotations

import math

import numpy as np
import pytest

from tom_s3_spinor_toy.bg_h1_e1_product_proxy import (
    E1_N_ALPHA_CONV,
    E1_N_ALPHA_PRIMARY,
    E1_PERIODIC_M1,
    E1_ANTIPERIODIC_M1,
    E1_R_VALUES,
    E1_REL_ERROR_KILL,
    K0_ANALYTIC,
    analytic_gap,
    product_gap,
    gap_rel_error,
    run_edge_behavior,
    run_e1_gate,
    run_gap_vs_R,
    run_grid_convergence,
    run_kronecker_sum_check,
    run_negative_control_periodic_ground,
    s1_discrete_eigenvalues,
    s3_ground_eigenvalue,
)


# ---------------------------------------------------------------------------
# 1. Analytic gap formula
# ---------------------------------------------------------------------------


class TestAnalyticGap:
    """Closed-form values for δ_analytic(R) = √(9/4+(m₁/R)²) − 3/2."""

    def test_periodic_m1_R05(self):
        """Periodic m₁=1, R=0.5: √(9/4+4)−3/2 = 2.5−1.5 = 1.0 (exact)."""
        assert analytic_gap(0.5, 1.0) == pytest.approx(1.0, abs=1e-12)

    def test_periodic_m1_R1(self):
        """Periodic m₁=1, R=1: √(13/4)−3/2 ≈ 0.30278."""
        expected = math.sqrt(13.0 / 4.0) - 1.5
        assert analytic_gap(1.0, 1.0) == pytest.approx(expected, rel=1e-12)

    def test_periodic_m1_R2(self):
        """Periodic m₁=1, R=2: √(9/4+1/4)−3/2 = √(10/4)−3/2."""
        expected = math.sqrt(10.0 / 4.0) - 1.5
        assert analytic_gap(2.0, 1.0) == pytest.approx(expected, rel=1e-12)

    def test_periodic_m1_R8(self):
        """Periodic m₁=1, R=8: gap is small (large-R regime)."""
        d = analytic_gap(8.0, 1.0)
        assert d > 0.0
        assert d < 0.02  # much smaller than small-R gap

    def test_antiperiodic_m_half_R05(self):
        """Antiperiodic m₁=1/2, R=0.5: √(9/4+1)−3/2 = √(13/4)−3/2 ≈ 0.30278."""
        expected = math.sqrt(13.0 / 4.0) - 1.5
        assert analytic_gap(0.5, 0.5) == pytest.approx(expected, rel=1e-12)

    def test_antiperiodic_m_half_R1(self):
        """Antiperiodic m₁=1/2, R=1: √(9/4+1/4)−3/2 = √(10/4)−3/2."""
        expected = math.sqrt(10.0 / 4.0) - 1.5
        assert analytic_gap(1.0, 0.5) == pytest.approx(expected, rel=1e-12)

    def test_m0_returns_zero(self):
        """Periodic m=0 ground state: gap = 0 (R-independent)."""
        for R in (0.5, 1.0, 2.0, 8.0):
            assert analytic_gap(R, 0.0) == 0.0

    def test_gap_positive_for_m1_gt_0(self):
        """δ > 0 whenever m₁ > 0."""
        for R in (0.5, 1.0, 2.0, 8.0):
            for m1 in (0.5, 1.0, 2.0):
                assert analytic_gap(R, m1) > 0.0

    def test_gap_decreasing_in_R(self):
        """δ is monotone decreasing in R for fixed m₁ > 0."""
        R_vals = [0.5, 1.0, 2.0, 4.0, 8.0]
        gaps = [analytic_gap(R, 1.0) for R in R_vals]
        for i in range(len(R_vals) - 1):
            assert gaps[i] > gaps[i + 1], (
                f"Expected δ({R_vals[i]}) > δ({R_vals[i + 1]}), "
                f"got {gaps[i]:.6f} vs {gaps[i + 1]:.6f}"
            )

    def test_large_R_leading_order(self):
        """Large R: δ ≈ (m₁/R)²/(2k₀) = m₁²/(3R²) for m₁=1."""
        R = 8.0
        d = analytic_gap(R, 1.0)
        approx = 1.0 / (3.0 * R**2)
        assert d == pytest.approx(approx, rel=0.03)  # 3% tolerance (leading order)


# ---------------------------------------------------------------------------
# 2. product_gap formula
# ---------------------------------------------------------------------------


class TestProductGap:
    """product_gap with analytic k₀=3/2 should equal analytic_gap exactly."""

    def test_equals_analytic_at_k0_32(self):
        """With k₀=3/2, product_gap == analytic_gap exactly."""
        for R in (0.5, 1.0, 2.0, 8.0):
            for m1 in (0.5, 1.0):
                pg = product_gap(K0_ANALYTIC, R, m1)
                ag = analytic_gap(R, m1)
                assert pg == pytest.approx(ag, rel=1e-12)

    def test_m0_returns_zero(self):
        """m₁=0: gap = 0 regardless of k₀ or R."""
        assert product_gap(1.5, 1.0, 0.0) == 0.0
        assert product_gap(1.5, 8.0, 0.0) == 0.0

    def test_larger_k0_smaller_gap(self):
        """Larger k₀ → smaller gap for fixed m₁, R (standard result)."""
        R, m1 = 1.0, 1.0
        d1 = product_gap(1.5, R, m1)
        d2 = product_gap(2.5, R, m1)
        assert d1 > d2

    def test_positive_for_m1_gt_0(self):
        """product_gap > 0 whenever m₁ > 0."""
        assert product_gap(1.5, 1.0, 1.0) > 0.0
        assert product_gap(1.499, 1.0, 1.0) > 0.0  # slightly off k₀


# ---------------------------------------------------------------------------
# 3. gap_rel_error
# ---------------------------------------------------------------------------


class TestGapRelError:
    """gap_rel_error is 0 when k₀_disc=3/2 (analytic value)."""

    def test_zero_at_analytic_k0(self):
        """Rel error = 0 exactly when k₀_disc = k₀_analytic = 3/2."""
        for R in (0.5, 1.0, 8.0):
            for m1 in (0.5, 1.0):
                err = gap_rel_error(K0_ANALYTIC, R, m1)
                assert err == pytest.approx(0.0, abs=1e-14)

    def test_zero_for_m0(self):
        """m=0: rel error = 0 by definition."""
        assert gap_rel_error(1.5, 1.0, 0.0) == 0.0

    def test_nonzero_for_perturbed_k0(self):
        """Perturbed k₀ → nonzero rel error."""
        err = gap_rel_error(1.5 + 0.01, 1.0, 1.0)
        assert err > 0.0

    def test_error_proportional_to_perturbation(self):
        """Doubling k₀ perturbation roughly doubles rel error (linear regime)."""
        e1 = gap_rel_error(1.5 + 0.001, 1.0, 1.0)
        e2 = gap_rel_error(1.5 + 0.002, 1.0, 1.0)
        assert e2 == pytest.approx(2.0 * e1, rel=0.05)


# ---------------------------------------------------------------------------
# 4. S³ ground-state discrete eigenvalue
# ---------------------------------------------------------------------------


class TestS3GroundEigenvalue:
    """Discrete S³ ground state converges to k₀=3/2."""

    def test_rough_accuracy_n500(self):
        """N_alpha=500: k₀_disc within 0.5% of 3/2."""
        k0 = s3_ground_eigenvalue(500)
        assert k0 == pytest.approx(K0_ANALYTIC, rel=0.005)

    def test_good_accuracy_n2000(self):
        """N_alpha=2000: k₀_disc within 0.01% of 3/2."""
        k0 = s3_ground_eigenvalue(2000)
        assert k0 == pytest.approx(K0_ANALYTIC, rel=1e-4)

    def test_high_accuracy_n4000(self):
        """N_alpha=4000: k₀_disc within 0.001% of 3/2 (primary gate grid)."""
        k0 = s3_ground_eigenvalue(4000)
        assert k0 == pytest.approx(K0_ANALYTIC, rel=1e-5)

    def test_converges_toward_analytic(self):
        """Convergence: |k₀_disc(N2) - 3/2| < |k₀_disc(N1) - 3/2| for N2>N1."""
        k1 = s3_ground_eigenvalue(1000)
        k2 = s3_ground_eigenvalue(4000)
        err1 = abs(k1 - K0_ANALYTIC)
        err2 = abs(k2 - K0_ANALYTIC)
        assert err2 < err1


# ---------------------------------------------------------------------------
# 5. S¹ discrete eigenvalues
# ---------------------------------------------------------------------------


class TestS1DiscreteEigenvalues:
    """Discrete S¹ spectrum converges to exact Fourier modes."""

    def test_periodic_ground_zero(self):
        """Periodic S¹ ground eigenvalue = 0 (m=0 mode)."""
        eigs = s1_discrete_eigenvalues(32, 1.0, "periodic")
        assert float(np.min(eigs)) == pytest.approx(0.0, abs=1e-12)

    def test_periodic_first_mode_at_R1(self):
        """Periodic first KK eigenvalue ≈ (1/R)² = 1.0 at R=1, large N_s1."""
        eigs = np.sort(s1_discrete_eigenvalues(128, 1.0, "periodic"))
        # Second smallest (first nonzero) should be near 1.0
        assert eigs[1] == pytest.approx(1.0, rel=0.01)

    def test_antiperiodic_ground_near_quarter(self):
        """Antiperiodic ground ≈ (1/2R)² = 0.25 at R=1, large N_s1."""
        eigs = np.sort(s1_discrete_eigenvalues(128, 1.0, "antiperiodic"))
        assert eigs[0] == pytest.approx(0.25, rel=0.02)

    def test_R_scaling(self):
        """Eigenvalues scale as 1/R²: doubling R halves all eigenvalues."""
        eigs_R1 = np.sort(s1_discrete_eigenvalues(64, 1.0, "periodic"))
        eigs_R2 = np.sort(s1_discrete_eigenvalues(64, 2.0, "periodic"))
        # Nonzero modes should scale by 1/4
        assert eigs_R1[1] == pytest.approx(4.0 * eigs_R2[1], rel=0.01)


# ---------------------------------------------------------------------------
# 6. Negative control: periodic m=0
# ---------------------------------------------------------------------------


class TestNegativeControlPeriodicGround:
    """Periodic m=0: δ = 0 for all R (R-independent pure-S³ ground state)."""

    def test_gap_zero_all_R(self):
        result = run_negative_control_periodic_ground(2000)
        assert result["all_zero"] is True
        assert result["pass"] is True

    def test_gap_individual_points(self):
        result = run_negative_control_periodic_ground(2000)
        for rec in result["results"]:
            assert rec["is_zero"] is True, f"Expected δ=0 at R={rec['R']}, got {rec['delta']}"


# ---------------------------------------------------------------------------
# 7. Primary gate sweep: δ_disc vs δ_analytic
# ---------------------------------------------------------------------------


class TestPrimaryGateSweep:
    """Main gate: δ_disc(R) within 1% of δ_analytic(R) for both structures."""

    def test_periodic_max_rel_error_below_kill(self):
        result = run_gap_vs_R(E1_N_ALPHA_PRIMARY, E1_R_VALUES, E1_PERIODIC_M1, "periodic")
        assert result["max_rel_error"] < E1_REL_ERROR_KILL, (
            f"Periodic max rel error {result['max_rel_error']:.4e} ≥ {E1_REL_ERROR_KILL}"
        )

    def test_antiperiodic_max_rel_error_below_kill(self):
        result = run_gap_vs_R(E1_N_ALPHA_PRIMARY, E1_R_VALUES, E1_ANTIPERIODIC_M1, "antiperiodic")
        assert result["max_rel_error"] < E1_REL_ERROR_KILL, (
            f"Antiperiodic max rel error {result['max_rel_error']:.4e} ≥ {E1_REL_ERROR_KILL}"
        )

    def test_periodic_all_R_points_pass(self):
        result = run_gap_vs_R(E1_N_ALPHA_PRIMARY, E1_R_VALUES, E1_PERIODIC_M1, "periodic")
        for rec in result["results"]:
            assert rec["pass"] is True, (
                f"Periodic R={rec['R']} failed: rel_err={rec['rel_error']:.4e}"
            )

    def test_antiperiodic_all_R_points_pass(self):
        result = run_gap_vs_R(E1_N_ALPHA_PRIMARY, E1_R_VALUES, E1_ANTIPERIODIC_M1, "antiperiodic")
        for rec in result["results"]:
            assert rec["pass"] is True, (
                f"Antiperiodic R={rec['R']} failed: rel_err={rec['rel_error']:.4e}"
            )

    def test_periodic_gap_values_match_analytic_R05(self):
        """Periodic R=0.5: δ_disc ≈ 1.0 (strong KK regime)."""
        result = run_gap_vs_R(E1_N_ALPHA_PRIMARY, (0.5,), E1_PERIODIC_M1, "periodic")
        rec = result["results"][0]
        assert rec["delta_disc"] == pytest.approx(1.0, rel=E1_REL_ERROR_KILL)

    def test_periodic_gap_values_match_analytic_R8(self):
        """Periodic R=8: δ_disc ≈ 0.0052 (large-R, small gap)."""
        expected = analytic_gap(8.0, E1_PERIODIC_M1)
        result = run_gap_vs_R(E1_N_ALPHA_PRIMARY, (8.0,), E1_PERIODIC_M1, "periodic")
        rec = result["results"][0]
        assert rec["delta_disc"] == pytest.approx(expected, rel=E1_REL_ERROR_KILL)

    def test_antiperiodic_ground_is_r_sensitive(self):
        """Antiperiodic ground (m₁=1/2): δ(R=0.5) ≠ δ(R=8) by large margin."""
        d_small = analytic_gap(0.5, E1_ANTIPERIODIC_M1)
        d_large = analytic_gap(8.0, E1_ANTIPERIODIC_M1)
        assert d_small > d_large * 10  # large R-sensitivity


# ---------------------------------------------------------------------------
# 8. Grid convergence
# ---------------------------------------------------------------------------


class TestGridConvergence:
    """Monotone convergence of δ_disc → δ_analytic as N_alpha grows."""

    def test_periodic_monotone_convergence(self):
        result = run_grid_convergence(1.0, E1_PERIODIC_M1, E1_N_ALPHA_CONV)
        assert result["monotone_convergence"] is True, (
            f"Periodic grid convergence not monotone: errors={[r['rel_error'] for r in result['records']]}"
        )

    def test_antiperiodic_monotone_convergence(self):
        result = run_grid_convergence(1.0, E1_ANTIPERIODIC_M1, E1_N_ALPHA_CONV)
        assert result["monotone_convergence"] is True, (
            f"Antiperiodic grid convergence not monotone: errors={[r['rel_error'] for r in result['records']]}"
        )

    def test_periodic_final_error_below_kill(self):
        result = run_grid_convergence(1.0, E1_PERIODIC_M1, E1_N_ALPHA_CONV)
        assert result["final_rel_error"] < E1_REL_ERROR_KILL

    def test_antiperiodic_final_error_below_kill(self):
        result = run_grid_convergence(1.0, E1_ANTIPERIODIC_M1, E1_N_ALPHA_CONV)
        assert result["final_rel_error"] < E1_REL_ERROR_KILL

    def test_error_decreases_by_factor_4_at_N4000_vs_N500(self):
        """Expect at least 4× improvement from N=500 to N=4000."""
        result = run_grid_convergence(1.0, E1_PERIODIC_M1, (500, 4000))
        err_500 = result["records"][0]["rel_error"]
        err_4000 = result["records"][1]["rel_error"]
        assert err_4000 < err_500 / 4.0, (
            f"Expected ≥4× improvement, got err(500)={err_500:.2e} vs err(4000)={err_4000:.2e}"
        )


# ---------------------------------------------------------------------------
# 9. Edge behavior
# ---------------------------------------------------------------------------


class TestEdgeBehavior:
    """Large-R and small-R predictions."""

    def setup_method(self):
        self.result = run_edge_behavior(E1_N_ALPHA_PRIMARY)

    def test_large_R_gap_is_small(self):
        assert self.result["large_R_is_small"] is True

    def test_small_R_kk_dominates(self):
        assert self.result["kk_dominates_at_small_R"] is True

    def test_analytic_gaps_monotone_in_R(self):
        assert self.result["analytic_gaps_monotone_in_R"] is True

    def test_discrete_gaps_monotone_in_R(self):
        assert self.result["discrete_gaps_monotone_in_R"] is True

    def test_large_R_leading_order_approx_close(self):
        """Large-R approx (m₁/R)²/(2k₀) agrees with analytic to 3%."""
        rel_err = self.result["large_R_approx_rel_err"]
        assert rel_err < 0.03, f"Large-R leading order rel err {rel_err:.4f} > 3%"

    def test_small_R_delta_exceeds_1(self):
        """Periodic R=0.5: δ > 0.99 (near exactly 1.0)."""
        d_anal = self.result["delta_small_R_analytic"]
        assert d_anal > 0.99

    def test_large_R_gap_vs_approx_quantitative(self):
        """R=8, m₁=1: δ_analytic ≈ 1/(3×64) ≈ 0.0052."""
        d = self.result["delta_large_R_analytic"]
        assert d == pytest.approx(1.0 / (3.0 * 64.0), rel=0.01)


# ---------------------------------------------------------------------------
# 10. Kronecker-sum identity
# ---------------------------------------------------------------------------


class TestKroneckerSumIdentity:
    """D²_prod = D²_S3 ⊗ I + I ⊗ D²_S1 eigenvalues = {λ_S3_i + λ_S1_j}."""

    def test_kronecker_identity_machine_precision(self):
        result = run_kronecker_sum_check(n_alpha_small=30, n_s1=16, R=1.0)
        assert result["kronecker_identity_pass"] is True, (
            f"Kronecker sum max abs err = {result['max_abs_err_kronecker']:.2e} (expected < 1e-8)"
        )

    def test_kronecker_identity_different_R(self):
        """Identity holds for R≠1 as well."""
        result = run_kronecker_sum_check(n_alpha_small=20, n_s1=12, R=2.0)
        assert result["kronecker_identity_pass"] is True

    def test_kronecker_lowest_eigenvalue_is_s3_ground(self):
        """Lowest product eigenvalue = λ_S3_0 + λ_S1_0 (S³ ground + m=0)."""
        result = run_kronecker_sum_check(n_alpha_small=30, n_s1=16, R=1.0)
        assert result["lowest_eigenvalue_actual"] == pytest.approx(
            result["lowest_eigenvalue_expected"], abs=1e-8
        )


# ---------------------------------------------------------------------------
# 11. Full E1 gate
# ---------------------------------------------------------------------------


class TestE1Gate:
    """Full run_e1_gate() output structure and verdict."""

    @pytest.fixture(scope="class")
    def gate_result(self):
        return run_e1_gate(n_alpha=E1_N_ALPHA_PRIMARY)

    def test_verdict_pass(self, gate_result):
        assert gate_result["verdict"] == "PASS"

    def test_max_rel_error_below_kill(self, gate_result):
        assert gate_result["max_rel_error_overall"] < E1_REL_ERROR_KILL

    def test_periodic_max_error_present(self, gate_result):
        assert "max_rel_error_periodic" in gate_result

    def test_antiperiodic_max_error_present(self, gate_result):
        assert "max_rel_error_antiperiodic" in gate_result

    def test_spin_structure_fork_reported(self, gate_result):
        assert gate_result["spin_structure_fork_reported"] is True

    def test_no_physical_spin_structure_selected(self, gate_result):
        """SCOPE GUARD: physical_spin_structure_selected MUST be False."""
        assert gate_result["physical_spin_structure_selected"] is False

    def test_forbidden_claims_not_in_verdict_string(self, gate_result):
        """SCOPE GUARD: verdict is 'PASS' or 'FAIL', not a forbidden claim string."""
        assert gate_result["verdict"] in ("PASS", "FAIL")

    def test_negative_control_pass(self, gate_result):
        assert gate_result["negative_control"]["pass"] is True

    def test_grid_convergence_monotone_periodic(self, gate_result):
        assert gate_result["grid_convergence_periodic"]["monotone_convergence"] is True

    def test_grid_convergence_monotone_antiperiodic(self, gate_result):
        assert gate_result["grid_convergence_antiperiodic"]["monotone_convergence"] is True

    def test_kronecker_check_pass(self, gate_result):
        assert gate_result["kronecker_sum_check"]["kronecker_identity_pass"] is True

    def test_gate_name(self, gate_result):
        assert gate_result["gate"] == "BG-H1-E1"

    def test_precondition_recorded(self, gate_result):
        assert "BG-H1-G1 PASS" in gate_result["precondition"]

    def test_lambda_free_in_scope(self, gate_result):
        """SCOPE GUARD: scope explicitly states λ is free."""
        assert "FREE_COUPLING_PARAMETER" in gate_result["scope"]

    def test_geometry_agnostic_in_scope(self, gate_result):
        """SCOPE GUARD: GEOMETRY_AGNOSTIC is asserted in scope."""
        assert "GEOMETRY_AGNOSTIC" in gate_result["scope"]


# ---------------------------------------------------------------------------
# 12. Constants sanity
# ---------------------------------------------------------------------------


class TestConstants:
    def test_k0_analytic_is_3_over_2(self):
        assert K0_ANALYTIC == 1.5

    def test_periodic_m1_is_1(self):
        assert E1_PERIODIC_M1 == 1.0

    def test_antiperiodic_m1_is_half(self):
        assert E1_ANTIPERIODIC_M1 == 0.5

    def test_r_values_cover_full_range(self):
        assert min(E1_R_VALUES) <= 0.5
        assert max(E1_R_VALUES) >= 8.0

    def test_kill_threshold(self):
        assert E1_REL_ERROR_KILL == 1e-2

    def test_primary_n_alpha(self):
        assert E1_N_ALPHA_PRIMARY == 4000

    def test_conv_levels_ordered(self):
        assert list(E1_N_ALPHA_CONV) == sorted(E1_N_ALPHA_CONV)
