"""Tests — NC2_PERMUTED_GRID_NEGATIVE_CONTROL (v0.2.0 Tier-3 control).

NC-2 passes when permuting V(α_i) destroys the spectral fingerprint.
Observed deviation: ~300-460% — confirmed in numerical probe 2026-06-10.
"""

from __future__ import annotations

import pytest

from tom_s3_spinor_toy.nc2_permuted_grid import (
    NC2_MIN_DEVIATION,
    N_SEEDS,
    permuted_grid_lambda_min,
    run_nc2,
    run_nc2_full,
)

N_GRID = 2000


@pytest.fixture(scope="module")
def nc2_full():
    return run_nc2_full(n_grid=N_GRID)


@pytest.fixture(scope="module")
def nc2_s3():
    return run_nc2(d=3, n_grid=N_GRID)


# ---------------------------------------------------------------------------
# Tier-3 pass verdict — the main NC-2 gate
# ---------------------------------------------------------------------------

def test_nc2_overall_verdict_is_pass(nc2_full):
    """NC-2 must pass for both S³ and S⁶ to clear the Tier-3 gate."""
    assert nc2_full["overall_verdict"] == "NC2_PASS", (
        f"NC-2 FAILED: {nc2_full['overall_verdict']}. "
        "Fingerprint may be a matrix artifact — Phase 3 blocked."
    )


def test_nc2_s3_verdict_is_pass(nc2_full):
    assert nc2_full["s3"]["verdict"] == "NC2_PASS"


def test_nc2_s6_verdict_is_pass(nc2_full):
    assert nc2_full["s6"]["verdict"] == "NC2_PASS"


# ---------------------------------------------------------------------------
# Deviation magnitude — confirms geometric sensitivity, not edge-case pass
# ---------------------------------------------------------------------------

def test_nc2_s3_all_seeds_deviate_large(nc2_s3):
    """All S³ seeds must show deviation > 50% (actual observed: ~300-460%)."""
    for r in nc2_s3["seed_results"]:
        assert r["fingerprint_destroyed"] is True, (
            f"Seed {r['seed']}: deviation={r['deviation_fraction']:.1%} "
            f"< threshold={NC2_MIN_DEVIATION:.0%}"
        )


def test_nc2_s3_min_deviation_is_large(nc2_s3):
    """Even the best-case (smallest) deviation must be >> 50% (observed: ~250%)."""
    assert nc2_s3["min_deviation_fraction"] > 1.5, (
        f"min deviation {nc2_s3['min_deviation_fraction']:.1%} unexpectedly small; "
        "check permutation logic"
    )


def test_nc2_s3_permuted_lambda_shoots_up(nc2_s3):
    """Permuted |λ_min| must be much larger than analytic d/2 = 1.5."""
    for r in nc2_s3["seed_results"]:
        assert r["lambda_min_permuted"] > 3.0, (
            f"Seed {r['seed']}: permuted |λ_min|={r['lambda_min_permuted']:.3f} "
            "not large enough — SUSY structure may not be destroyed"
        )


# ---------------------------------------------------------------------------
# Contrast with clean baseline
# ---------------------------------------------------------------------------

def test_nc2_clean_baseline_matches_analytic(nc2_s3):
    """Clean baseline (W=0, no permutation) = 1.5 to tolerance."""
    assert abs(nc2_s3["clean_baseline"] - 1.5) < 1e-4


def test_nc2_permuted_differs_from_clean(nc2_s3):
    """Each seed's |λ_min|_perm must differ dramatically from clean baseline."""
    baseline = nc2_s3["clean_baseline"]
    for r in nc2_s3["seed_results"]:
        assert r["lambda_min_permuted"] > baseline * 3, (
            f"Seed {r['seed']}: permuted not 3× clean — unexpected proximity"
        )


# ---------------------------------------------------------------------------
# Determinism
# ---------------------------------------------------------------------------

def test_nc2_deterministic():
    """Same seed must give identical result on re-run."""
    lm1 = permuted_grid_lambda_min(3, 0, 500, seed=7)
    lm2 = permuted_grid_lambda_min(3, 0, 500, seed=7)
    assert lm1 == lm2


def test_nc2_different_seeds_differ():
    """Different seeds must give different permuted eigenvalues."""
    lm0 = permuted_grid_lambda_min(3, 0, 500, seed=0)
    lm1 = permuted_grid_lambda_min(3, 0, 500, seed=1)
    assert abs(lm0 - lm1) > 0.1


# ---------------------------------------------------------------------------
# Hard constraints
# ---------------------------------------------------------------------------

def test_ipr_not_in_endpoint(nc2_full):
    assert "NOT USED" in nc2_full["s3"]["scope"]["ipr"]


def test_ha4_open(nc2_full):
    assert nc2_full["s3"]["scope"]["HA-4"].startswith("OPEN")


def test_no_promotion(nc2_full):
    assert "research_only" in nc2_full["s3"]["scope"]["promotion"]


def test_sweep_covers_all_seeds(nc2_s3):
    assert len(nc2_s3["seed_results"]) == N_SEEDS
