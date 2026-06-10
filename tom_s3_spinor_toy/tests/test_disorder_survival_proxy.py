"""Tests — KT3_DISORDER_SURVIVAL_TEST (v0.2.0 spinor-geometry pivot).

Pre-registered kill condition: max shift of |λ_min| at W=0.1 > 0.25 → KT3_FAIL.
Tests use n_grid=2000 (baseline error ~3e-6, well below any W-induced shift).
"""

from __future__ import annotations

import numpy as np
import pytest

from tom_s3_spinor_toy.disorder_survival_proxy import (
    KT3_THRESHOLD,
    N_SEEDS,
    W_KILL,
    W_VALUES,
    baseline_lambda_min,
    disordered_lambda_min,
    disorder_survival_sweep,
    kt3_verdict,
    run_kt3,
)

N_GRID = 2000


@pytest.fixture(scope="module")
def kt3_result():
    return run_kt3(n_grid=N_GRID)


@pytest.fixture(scope="module")
def s3_sweep():
    return disorder_survival_sweep(d=3, l_sector=0, n_grid=N_GRID)


# ---------------------------------------------------------------------------
# Pre-registered kill-test — main verdict gate
# ---------------------------------------------------------------------------

def test_kt3_s3_verdict_is_pass(kt3_result):
    """Pre-registered: max shift at W=0.1 must be < 0.25 for KT3_PASS."""
    verdict = kt3_result["s3"]["verdict"]
    assert verdict["verdict"] == "KT3_PASS", (
        f"KT3 kill-test FAILED: {verdict['verdict']}. "
        f"max_shift={verdict['max_shift_at_W_kill']:.4f}, "
        f"threshold={verdict['threshold']}"
    )


def test_kt3_s3_max_shift_at_w01(kt3_result):
    """max-over-seeds shift at W=0.1 must be < KT3_THRESHOLD=0.25."""
    verd = kt3_result["s3"]["verdict"]
    assert verd["max_shift_at_W_kill"] < KT3_THRESHOLD
    assert verd["max_shift_at_W_kill"] < 0.05, (
        "max shift unexpectedly large (>5% of |λ_min|); check W=0.1 disorder"
    )


def test_kt3_safety_margin_positive(kt3_result):
    """Safety margin = threshold - max_shift must be positive (PASS side)."""
    verd = kt3_result["s3"]["verdict"]
    assert verd["safety_margin"] > 0.0


# ---------------------------------------------------------------------------
# Baseline consistency with E0
# ---------------------------------------------------------------------------

def test_s3_baseline_matches_e0():
    """W=0 baseline |λ_min| ≈ 1.5 to E0 accuracy (error < 1e-4)."""
    lm = baseline_lambda_min(d=3, l_sector=0, n_grid=N_GRID)
    assert abs(lm - 1.5) < 1e-4, f"baseline {lm} deviates from 1.5"


def test_s6_baseline_matches_analytic():
    """W=0 baseline |λ_min| for d=6 ≈ 3.0."""
    lm = baseline_lambda_min(d=6, l_sector=0, n_grid=N_GRID)
    assert abs(lm - 3.0) < 1e-4, f"d=6 baseline {lm} deviates from 3.0"


# ---------------------------------------------------------------------------
# Disorder properties
# ---------------------------------------------------------------------------

def test_disorder_shifts_nonzero_at_large_W(s3_sweep):
    """At W=0.5, disorder must produce measurable shifts (otherwise suspicious)."""
    entry = next(r for r in s3_sweep if abs(r["W"] - 0.5) < 1e-9)
    assert entry["max_shift"] > 1e-6, "W=0.5 produced no shift — seeding broken?"


def test_disorder_mean_shift_grows_with_W(s3_sweep):
    """Mean shifts should be monotonically non-decreasing across W values."""
    sorted_entries = sorted(s3_sweep, key=lambda r: r["W"])
    mean_shifts = [r["mean_shift"] for r in sorted_entries]
    for i in range(1, len(mean_shifts)):
        assert mean_shifts[i] >= mean_shifts[i - 1] * 0.5, (
            f"Mean shift not growing: W={sorted_entries[i]['W']}, "
            f"mean_shift={mean_shifts[i]:.6f} < 0.5 × prev={mean_shifts[i-1]:.6f}"
        )


def test_disorder_deterministic_with_seeds():
    """Same seed → identical λ_min (reproducibility)."""
    lm1 = disordered_lambda_min(3, 0, 500, W=0.1, seed=42)
    lm2 = disordered_lambda_min(3, 0, 500, W=0.1, seed=42)
    assert lm1 == lm2


def test_disorder_different_seeds_differ():
    """Different seeds → different λ_min values."""
    lm0 = disordered_lambda_min(3, 0, 500, W=0.2, seed=0)
    lm1 = disordered_lambda_min(3, 0, 500, W=0.2, seed=1)
    assert abs(lm0 - lm1) > 1e-10, "Seeds 0 and 1 gave identical result"


# ---------------------------------------------------------------------------
# Cross-sphere separation at W=0.1
# ---------------------------------------------------------------------------

def test_s3_s6_remain_separated_at_w01(kt3_result):
    """S³ and S⁶ |λ_min| must stay separated by > 0.5 under W=0.1 disorder.

    Analytic gap = |3.0 - 1.5| = 1.5; even with shifts the gap >> threshold.
    """
    sep = kt3_result["cross_sphere_separation_at_W01"]
    assert sep["separation_ok"] is True, (
        f"Fingerprints crossed! S³_max={sep['s3_max_lambda_min']:.4f}, "
        f"S⁶_min={sep['s6_min_lambda_min']:.4f}, gap={sep['gap']:.4f}"
    )
    assert sep["gap"] > 0.5


# ---------------------------------------------------------------------------
# W* — applicable disorder range
# ---------------------------------------------------------------------------

def test_w_star_recorded(kt3_result):
    """W* (largest W with max_shift < threshold) must be present and > W_KILL."""
    verd = kt3_result["s3"]["verdict"]
    w_star = verd["w_star"]
    assert w_star is not None, "W* not determined — sweep may have failed"
    assert w_star >= W_KILL, f"W*={w_star} < W_kill={W_KILL} (fingerprint fragile)"


# ---------------------------------------------------------------------------
# Hard constraints (identical to E0)
# ---------------------------------------------------------------------------

def test_ipr_not_primary_endpoint(kt3_result):
    """IPR must not appear as primary endpoint in KT-3 output."""
    ep = kt3_result["primary_endpoint"]
    assert "IPR not used" in ep
    assert "shift" in ep.lower()


def test_ha4_recorded_open(kt3_result):
    """HA-4 scope gap (S^d ≠ S³×S¹) must be explicitly open."""
    ha4 = kt3_result["scope"]["HA-4"]
    assert ha4.startswith("OPEN")
    assert "S3xS1" in ha4


def test_no_promotion(kt3_result):
    """No physical promotion claim in KT-3 output."""
    promo = kt3_result["scope"]["promotion"]
    assert "NONE" in promo
    assert "research_only" in promo


def test_tom_ansatz_radial_only(kt3_result):
    """tom_ansatz scope must remain RADIAL_PROJECTION_FINDING_ONLY."""
    ta = kt3_result["scope"]["tom_ansatz"]
    assert "RADIAL_PROJECTION_FINDING_ONLY" in ta


def test_sweep_covers_all_w_values(kt3_result):
    """All pre-registered W values must be present in S³ sweep."""
    w_present = {r["W"] for r in kt3_result["s3"]["sweep"]}
    for W in W_VALUES:
        assert any(abs(W - w) < 1e-9 for w in w_present), f"W={W} missing from sweep"


def test_sweep_covers_all_seeds(kt3_result):
    """Each W entry must have N_SEEDS samples."""
    for entry in kt3_result["s3"]["sweep"]:
        assert len(entry["lambda_min_samples"]) == N_SEEDS, (
            f"W={entry['W']}: expected {N_SEEDS} seeds, "
            f"got {len(entry['lambda_min_samples'])}"
        )
