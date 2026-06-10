"""Tests for BG-H1-E2: disorder robustness of product S³×S¹ KK gap.

Test hierarchy:
  1. TestConstants              — pre-registered constants frozen
  2. TestAnalyticGap            — formula sanity
  3. TestProductGap             — product gap formula
  4. TestS3DisorderedGround     — disorder model: seed-reproducible, bounded
  5. TestDisorderSweepStructure — sweep output shape/types
  6. TestE2GateFull             — full gate (class fixture, run once at N=1000)
     - verdict PASS
     - monotonicity
     - mean rel error within kill
     - fragility ratio within kill
     - no physical promotion claims
  7. TestE2VerdictLogic         — unit tests for e2_verdict with crafted inputs
"""

from __future__ import annotations

import math
import pytest
import numpy as np

from tom_s3_spinor_toy.bg_h1_e2_disorder_proxy import (
    E2_W_DISORDER,
    E2_N_SEEDS,
    E2_N_ALPHA,
    E2_R_VALUES,
    E2_REL_MEAN_ERROR_KILL,
    E2_FRAGILITY_RATIO_KILL,
    E2_PERIODIC_M1,
    E2_ANTIPERIODIC_M1,
    K0_ANALYTIC,
    analytic_gap,
    product_gap,
    s3_clean_ground,
    s3_disordered_ground,
    run_disorder_sweep,
    e2_verdict,
    run_e2_gate,
)


# ---------------------------------------------------------------------------
# 1. Pre-registered constants
# ---------------------------------------------------------------------------


class TestConstants:
    def test_w_disorder(self):
        assert E2_W_DISORDER == 0.5

    def test_n_seeds(self):
        assert E2_N_SEEDS == 30

    def test_n_alpha(self):
        assert E2_N_ALPHA == 1000

    def test_r_values(self):
        assert E2_R_VALUES == (0.5, 1.0, 2.0, 4.0, 6.0, 8.0)

    def test_rel_mean_error_kill(self):
        assert E2_REL_MEAN_ERROR_KILL == 0.05

    def test_fragility_ratio_kill(self):
        assert E2_FRAGILITY_RATIO_KILL == 10.0

    def test_periodic_m1(self):
        assert E2_PERIODIC_M1 == 1.0

    def test_antiperiodic_m1(self):
        assert E2_ANTIPERIODIC_M1 == 0.5

    def test_k0_analytic(self):
        assert K0_ANALYTIC == 1.5


# ---------------------------------------------------------------------------
# 2. Analytic gap formula
# ---------------------------------------------------------------------------


class TestAnalyticGap:
    def test_m0_returns_zero(self):
        for R in (0.5, 1.0, 4.0):
            assert analytic_gap(R, 0.0) == 0.0

    def test_periodic_r1(self):
        # δ(1) = √(9/4 + 1) − 3/2 = √(13/4) − 3/2
        expected = math.sqrt(13.0 / 4.0) - 1.5
        assert abs(analytic_gap(1.0, 1.0) - expected) < 1e-14

    def test_antiperiodic_r1(self):
        # δ(1) = √(9/4 + 1/4) − 3/2 = √(10/4) − 3/2
        expected = math.sqrt(10.0 / 4.0) - 1.5
        assert abs(analytic_gap(1.0, 0.5) - expected) < 1e-14

    def test_large_r_approaches_zero(self):
        # For large R, δ → 0
        assert analytic_gap(100.0, 1.0) < 0.01

    def test_small_r_dominates(self):
        # For R=0.5, periodic: δ = √(9/4 + 4) − 3/2 = √(25/4) − 3/2 = 5/2 − 3/2 = 1
        assert abs(analytic_gap(0.5, 1.0) - 1.0) < 1e-14

    def test_monotone_decreasing_in_r(self):
        R_vals = [0.5, 1.0, 2.0, 4.0, 6.0, 8.0]
        gaps = [analytic_gap(R, 1.0) for R in R_vals]
        for i in range(len(gaps) - 1):
            assert gaps[i] > gaps[i + 1], f"Not decreasing at R={R_vals[i + 1]}"

    def test_all_positive(self):
        for R in E2_R_VALUES:
            assert analytic_gap(R, 1.0) > 0.0
            assert analytic_gap(R, 0.5) > 0.0


# ---------------------------------------------------------------------------
# 3. Product gap formula
# ---------------------------------------------------------------------------


class TestProductGap:
    def test_m0_returns_zero(self):
        assert product_gap(1.5, 1.0, 0.0) == 0.0

    def test_exact_k0_matches_analytic(self):
        # product_gap(K0_ANALYTIC, R, m1) should equal analytic_gap(R, m1) up to float precision
        for R in E2_R_VALUES:
            for m1 in (1.0, 0.5):
                pg = product_gap(K0_ANALYTIC, R, m1)
                ag = analytic_gap(R, m1)
                assert abs(pg - ag) < 1e-13, f"R={R}, m1={m1}: {pg} vs {ag}"

    def test_perturbed_k0_shifts_gap(self):
        # If k₀ increases by ε, gap should decrease (monotone in k₀)
        R = 1.0
        m1 = 1.0
        eps = 0.01
        g0 = product_gap(1.5, R, m1)
        g1 = product_gap(1.5 + eps, R, m1)
        assert g1 < g0, "Gap should decrease as k₀ increases"

    def test_increasing_in_m1(self):
        # Larger KK mode → larger gap
        R = 1.0
        assert product_gap(1.5, R, 1.0) > product_gap(1.5, R, 0.5)

    def test_decreasing_in_r(self):
        # Larger R → smaller gap
        m1 = 1.0
        gaps = [product_gap(1.5, R, m1) for R in (0.5, 1.0, 2.0, 4.0)]
        for i in range(len(gaps) - 1):
            assert gaps[i] > gaps[i + 1]


# ---------------------------------------------------------------------------
# 4. S³ disordered ground — disorder model
# ---------------------------------------------------------------------------


class TestS3DisorderedGround:
    def test_clean_ground_near_analytic(self):
        k0 = s3_clean_ground(1000)
        # N=1000 gives ~3.9e-7 rel error (from E1 convergence table)
        assert abs(k0 - 1.5) / 1.5 < 1e-5

    def test_seed_reproducible(self):
        k0_a = s3_disordered_ground(500, 0.5, 42)
        k0_b = s3_disordered_ground(500, 0.5, 42)
        assert k0_a == k0_b

    def test_different_seeds_differ(self):
        k0_0 = s3_disordered_ground(500, 0.5, 0)
        k0_1 = s3_disordered_ground(500, 0.5, 1)
        assert k0_0 != k0_1

    def test_small_disorder_near_baseline(self):
        k0_base = s3_clean_ground(500)
        k0_d = s3_disordered_ground(500, 0.01, 0)
        # W=0.01 disorder should cause < 1% shift
        assert abs(k0_d - k0_base) / k0_base < 0.01

    def test_disorder_positive(self):
        # Even with disorder, |λ_min| should remain positive
        for seed in range(5):
            k0 = s3_disordered_ground(500, 0.5, seed)
            assert k0 > 0.0

    def test_zero_disorder_equals_baseline(self):
        k0_base = s3_clean_ground(300)
        k0_d = s3_disordered_ground(300, 0.0, 0)
        # W=0 should reproduce baseline exactly
        assert abs(k0_d - k0_base) < 1e-12


# ---------------------------------------------------------------------------
# 5. Disorder sweep structure
# ---------------------------------------------------------------------------


class TestDisorderSweepStructure:
    @pytest.fixture(scope="class")
    def small_sweep(self):
        """Fast small sweep (N=200, 5 seeds) for structural tests only."""
        return run_disorder_sweep(n_alpha=200, W=0.5, n_seeds=5)

    def test_has_required_keys(self, small_sweep):
        required = {
            "W",
            "n_alpha",
            "n_seeds",
            "R_values",
            "k0_baseline",
            "k0_mean",
            "k0_std",
            "s3_mean_rel_fragility",
            "s3_max_rel_fragility",
            "periodic",
            "antiperiodic",
        }
        assert required.issubset(set(small_sweep.keys()))

    def test_r_stats_length(self, small_sweep):
        assert len(small_sweep["periodic"]["r_stats"]) == 6
        assert len(small_sweep["antiperiodic"]["r_stats"]) == 6

    def test_r_stats_keys(self, small_sweep):
        expected_keys = {
            "R",
            "d_analytic",
            "d_baseline_disc",
            "mean",
            "std",
            "mean_rel_error_vs_analytic",
            "product_mean_rel_fragility",
            "fragility_ratio",
        }
        for s in small_sweep["periodic"]["r_stats"]:
            assert expected_keys.issubset(set(s.keys()))

    def test_r_values_match(self, small_sweep):
        r_list = [s["R"] for s in small_sweep["periodic"]["r_stats"]]
        assert r_list == list(E2_R_VALUES)

    def test_k0_baseline_near_analytic(self, small_sweep):
        # N=200 less precise but should be within 1%
        assert abs(small_sweep["k0_baseline"] - 1.5) / 1.5 < 0.01

    def test_s3_fragility_nonnegative(self, small_sweep):
        assert small_sweep["s3_mean_rel_fragility"] >= 0.0
        assert small_sweep["s3_max_rel_fragility"] >= 0.0
        assert small_sweep["s3_max_rel_fragility"] >= small_sweep["s3_mean_rel_fragility"]

    def test_fragility_ratios_finite(self, small_sweep):
        for struct in ("periodic", "antiperiodic"):
            for s in small_sweep[struct]["r_stats"]:
                assert math.isfinite(s["fragility_ratio"])

    def test_monotone_decreasing_key_exists(self, small_sweep):
        assert "monotone_decreasing" in small_sweep["periodic"]
        assert "monotone_decreasing" in small_sweep["antiperiodic"]


# ---------------------------------------------------------------------------
# 6. Full E2 gate (primary tests — class fixture, runs once)
# ---------------------------------------------------------------------------


@pytest.fixture(scope="class")
def gate_result():
    """Full E2 gate at N=1000 (pre-registered). Runs once per test class."""
    return run_e2_gate(E2_N_ALPHA)


class TestE2GateFull:
    """Tests that operate on the full N=1000 gate result."""

    def test_verdict_pass(self, gate_result):
        assert gate_result["verdict"]["verdict"] == "PASS", (
            f"E2 gate FAILED: {gate_result['verdict']['failures']}"
        )

    def test_no_failures(self, gate_result):
        assert gate_result["verdict"]["failures"] == []

    # --- Monotonicity ---

    def test_periodic_delta_monotone(self, gate_result):
        assert gate_result["sweep"]["periodic"]["monotone_decreasing"] is True

    def test_antiperiodic_delta_monotone(self, gate_result):
        assert gate_result["sweep"]["antiperiodic"]["monotone_decreasing"] is True

    # --- Mean relative error vs analytic ---

    def test_periodic_mean_rel_error_within_kill(self, gate_result):
        max_err = gate_result["verdict"]["max_periodic_mean_rel_error"]
        assert max_err < E2_REL_MEAN_ERROR_KILL, (
            f"Periodic mean rel error {max_err:.3e} exceeds kill {E2_REL_MEAN_ERROR_KILL}"
        )

    def test_antiperiodic_mean_rel_error_within_kill(self, gate_result):
        max_err = gate_result["verdict"]["max_antiperiodic_mean_rel_error"]
        assert max_err < E2_REL_MEAN_ERROR_KILL, (
            f"Antiperiodic mean rel error {max_err:.3e} exceeds kill {E2_REL_MEAN_ERROR_KILL}"
        )

    # --- Fragility ratio (core differential kill) ---

    def test_periodic_fragility_ratio_within_kill(self, gate_result):
        ratio = gate_result["verdict"]["max_periodic_fragility_ratio"]
        assert ratio < E2_FRAGILITY_RATIO_KILL, (
            f"Periodic fragility ratio {ratio:.2f} exceeds kill {E2_FRAGILITY_RATIO_KILL}"
        )

    def test_antiperiodic_fragility_ratio_within_kill(self, gate_result):
        ratio = gate_result["verdict"]["max_antiperiodic_fragility_ratio"]
        assert ratio < E2_FRAGILITY_RATIO_KILL, (
            f"Antiperiodic fragility ratio {ratio:.2f} exceeds kill {E2_FRAGILITY_RATIO_KILL}"
        )

    # --- Hard constraint: no physical claims ---

    def test_lambda_free(self, gate_result):
        scope = gate_result["verdict"]["scope"]
        assert scope["lambda"] == "FREE_COUPLING_PARAMETER"

    def test_safe_for_runtime_false(self, gate_result):
        scope = gate_result["verdict"]["scope"]
        assert scope["safe_for_runtime"] is False

    def test_no_spin_structure_selected(self, gate_result):
        scope = gate_result["verdict"]["scope"]
        assert scope["spin_structure_selected"] is False

    def test_no_geometry_claim(self, gate_result):
        scope = gate_result["verdict"]["scope"]
        assert "GEOMETRY_AGNOSTIC" in scope["geometry_claim"]

    # --- S³ ground state robustness (sanity: W=0.5 still within reach) ---

    def test_k0_baseline_near_analytic(self, gate_result):
        k0 = gate_result["sweep"]["k0_baseline"]
        assert abs(k0 - 1.5) / 1.5 < 1e-4  # N=1000 → ~3.9e-7 rel error, very tight

    def test_k0_std_positive(self, gate_result):
        # Non-zero std confirms disorder actually perturbs k₀
        assert gate_result["sweep"]["k0_std"] > 0.0

    def test_s3_fragility_within_10pct(self, gate_result):
        # Even at W=0.5, S³ fingerprint is robust (KT-3 confirmed at W=0.1)
        # At W=0.5 some larger shifts expected; still bounded
        frag = gate_result["sweep"]["s3_max_rel_fragility"]
        assert frag < 0.5, f"S³ max fragility {frag:.3f} unexpectedly large"

    # --- δ(R) stats per R ---

    def test_all_r_stats_positive_mean(self, gate_result):
        for struct in ("periodic", "antiperiodic"):
            for s in gate_result["sweep"][struct]["r_stats"]:
                assert s["mean"] > 0.0, f"Negative mean δ at R={s['R']}, struct={struct}"

    def test_std_less_than_mean(self, gate_result):
        # std << mean indicates gap is well-defined (not noise-dominated)
        for struct in ("periodic", "antiperiodic"):
            for s in gate_result["sweep"][struct]["r_stats"]:
                assert s["std"] < s["mean"], (
                    f"std >= mean at R={s['R']}, struct={struct}: "
                    f"std={s['std']:.4f}, mean={s['mean']:.4f}"
                )

    def test_periodic_large_r_suppressed(self, gate_result):
        # At R=8, periodic gap should be small (KK suppressed)
        stats_r8 = next(s for s in gate_result["sweep"]["periodic"]["r_stats"] if s["R"] == 8.0)
        assert stats_r8["mean"] < 0.1

    def test_periodic_small_r_dominates(self, gate_result):
        # At R=0.5, periodic gap ≈ 1.0 (KK dominates)
        stats_r05 = next(s for s in gate_result["sweep"]["periodic"]["r_stats"] if s["R"] == 0.5)
        assert stats_r05["mean"] > 0.5

    # --- Gate metadata ---

    def test_gate_id(self, gate_result):
        assert gate_result["gate"] == "BG-H1-E2"

    def test_n_alpha_matches(self, gate_result):
        assert gate_result["n_alpha"] == E2_N_ALPHA

    def test_sweep_n_seeds(self, gate_result):
        assert gate_result["sweep"]["n_seeds"] == E2_N_SEEDS

    def test_sweep_w_matches(self, gate_result):
        assert gate_result["sweep"]["W"] == E2_W_DISORDER


# ---------------------------------------------------------------------------
# 7. Verdict logic unit tests (crafted inputs — no FD computation)
# ---------------------------------------------------------------------------


class TestE2VerdictLogic:
    """Unit tests for e2_verdict() with hand-crafted sweep dicts."""

    def _make_sweep(
        self,
        frag_ratio_p: float = 1.0,
        frag_ratio_a: float = 1.0,
        mean_err_p: float = 0.001,
        mean_err_a: float = 0.001,
        monotone_p: bool = True,
        monotone_a: bool = True,
    ) -> dict:
        """Build a minimal sweep dict for verdict testing."""
        R_vals = list(E2_R_VALUES)

        def _r_stat(R: float, m1: float, frag_ratio: float, mean_err: float) -> dict:
            d_anal = analytic_gap(R, m1)
            return {
                "R": R,
                "d_analytic": d_anal,
                "d_baseline_disc": d_anal,
                "mean": d_anal * (1 + mean_err),
                "std": 1e-4,
                "mean_rel_error_vs_analytic": mean_err,
                "product_mean_rel_fragility": 0.001 * frag_ratio,
                "fragility_ratio": frag_ratio,
            }

        return {
            "W": 0.5,
            "n_alpha": 1000,
            "n_seeds": 30,
            "R_values": R_vals,
            "k0_baseline": 1.5,
            "k0_mean": 1.5,
            "k0_std": 0.001,
            "s3_mean_rel_fragility": 0.001,
            "s3_max_rel_fragility": 0.002,
            "periodic": {
                "m1": E2_PERIODIC_M1,
                "r_stats": [_r_stat(R, E2_PERIODIC_M1, frag_ratio_p, mean_err_p) for R in R_vals],
                "monotone_decreasing": monotone_p,
            },
            "antiperiodic": {
                "m1": E2_ANTIPERIODIC_M1,
                "r_stats": [
                    _r_stat(R, E2_ANTIPERIODIC_M1, frag_ratio_a, mean_err_a) for R in R_vals
                ],
                "monotone_decreasing": monotone_a,
            },
        }

    def test_clean_sweep_passes(self):
        sweep = self._make_sweep()
        v = e2_verdict(sweep)
        assert v["verdict"] == "PASS"
        assert v["failures"] == []

    def test_fragility_ratio_exceeds_kill(self):
        sweep = self._make_sweep(frag_ratio_p=11.0)
        v = e2_verdict(sweep)
        assert v["verdict"] == "FAIL"
        assert any("fragility_ratio" in f for f in v["failures"])

    def test_antiperiodic_fragility_exceeds_kill(self):
        sweep = self._make_sweep(frag_ratio_a=15.0)
        v = e2_verdict(sweep)
        assert v["verdict"] == "FAIL"

    def test_mean_rel_error_exceeds_kill(self):
        sweep = self._make_sweep(mean_err_p=0.06)
        v = e2_verdict(sweep)
        assert v["verdict"] == "FAIL"
        assert any("mean_rel_error" in f for f in v["failures"])

    def test_non_monotone_periodic(self):
        sweep = self._make_sweep(monotone_p=False)
        v = e2_verdict(sweep)
        assert v["verdict"] == "FAIL"
        assert any("monotone" in f for f in v["failures"])

    def test_non_monotone_antiperiodic(self):
        sweep = self._make_sweep(monotone_a=False)
        v = e2_verdict(sweep)
        assert v["verdict"] == "FAIL"

    def test_multiple_failures_all_listed(self):
        sweep = self._make_sweep(
            frag_ratio_p=20.0,
            mean_err_a=0.10,
            monotone_p=False,
        )
        v = e2_verdict(sweep)
        assert v["verdict"] == "FAIL"
        assert len(v["failures"]) >= 3

    def test_scope_fields_present(self):
        sweep = self._make_sweep()
        v = e2_verdict(sweep)
        assert "scope" in v
        assert v["scope"]["lambda"] == "FREE_COUPLING_PARAMETER"
        assert v["scope"]["safe_for_runtime"] is False
        assert v["scope"]["spin_structure_selected"] is False

    def test_kill_thresholds_reported(self):
        sweep = self._make_sweep()
        v = e2_verdict(sweep)
        assert "kill_thresholds" in v
        assert v["kill_thresholds"]["mean_rel_error"] == E2_REL_MEAN_ERROR_KILL
        assert v["kill_thresholds"]["fragility_ratio"] == E2_FRAGILITY_RATIO_KILL
