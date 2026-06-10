"""Tests — AV1_ANGULAR_DICTIONARY_ROBUSTNESS (v0.2.0, item-40 partial closure).

Pre-registered claims: experiments/.../claim_av1_angular.md (written BEFORE code ran).
Outcomes locked in as regressions:
  AV-1a PASS  — argmax (1,1), cos = 0.9594 (= sqrt of legacy squared value 0.9204)
  AV-1b PASS  — 5-term residual 2.9% < 5%
  AV-1c FAIL  — 12.38% > 10% pre-registered kill threshold (HONEST FAIL, kept as regression)
  H-T1  NOT PROMOTED — signal present (92.4%) but promotion required AV-1c PASS
"""

from __future__ import annotations

import numpy as np
import pytest

from tom_s3_spinor_toy.av1_angular_dictionary import (
    AV1A_EXPECTED_ARGMAX,
    alpha_grid,
    build_dictionary,
    inner_w,
    normalize,
    run_av1,
)
from tom_s3_spinor_toy.reference_spinor_harmonics import tom_ansatz

N_GRID = 2000


@pytest.fixture(scope="module")
def av1():
    return run_av1(n_grid=N_GRID, weighted=True)


@pytest.fixture(scope="module")
def av1_unweighted():
    return run_av1(n_grid=N_GRID, weighted=False)


# ---------------------------------------------------------------------------
# AV-1a — global argmax (the decisive pre-registered check)
# ---------------------------------------------------------------------------

def test_av1a_argmax_is_phi11(av1):
    assert tuple(av1["av1a"]["argmax"]) == AV1A_EXPECTED_ARGMAX
    assert av1["av1a"]["verdict"] == "AV1A_PASS"


def test_av1a_value_matches_legacy_squared_convention(av1):
    """cos = 0.9594; legacy regression 0.9204 is cos² — same finding, two notations."""
    cos_val = av1["av1a"]["argmax_value"]
    assert abs(cos_val - 0.9594) < 0.001
    assert abs(cos_val**2 - 0.9204) < 0.001


def test_av1a_no_offdiagonal_mode_beats_phi11(av1):
    """Kill condition check: no n≠l mode may exceed the (1,1) projection."""
    top_value = av1["av1a"]["argmax_value"]
    for row in av1["av1a"]["top10"]:
        if row["n"] != row["l"]:
            assert row["abs_projection"] < top_value


def test_av1a_robust_to_unweighted_convention(av1_unweighted):
    """Sensitivity check 1 (pre-registered): argmax survives measure change."""
    assert tuple(av1_unweighted["av1a"]["argmax"]) == AV1A_EXPECTED_ARGMAX


def test_av1a_boundary_family_fills_top5(av1):
    """Observed: top-5 are all n=l diagonal modes — the H-T1 pattern."""
    top5 = av1["av1a"]["top10"][:5]
    assert all(row["n"] == row["l"] for row in top5)


# ---------------------------------------------------------------------------
# AV-1b — least-squares dominance (supportive)
# ---------------------------------------------------------------------------

def test_av1b_passes(av1):
    assert av1["av1b"]["verdict"] == "AV1B_PASS"
    assert av1["av1b"]["residual_5term"] < 0.05


def test_av1b_first_greedy_pick_is_phi11(av1):
    assert tuple(av1["av1b"]["greedy_5term_modes"][0]) == (1, 1)


# ---------------------------------------------------------------------------
# AV-1c — bilinear probe: HONEST FAIL locked as regression
# ---------------------------------------------------------------------------

def test_av1c_failed_preregistered_threshold(av1):
    """AV-1c FAILED its pre-registered 10% kill threshold (12.38%).

    This is a real recorded outcome, NOT a bug: sin(2α) is not efficiently
    captured by ≤5 diagonal Dirac bilinears. Scope: off-diagonal bilinears
    φ_nl·φ_n'l' were NOT tested. If this test starts passing after a code
    change — the change altered the math; investigate before celebrating.
    """
    assert av1["av1c"]["verdict"] == "AV1C_FAIL"
    assert 0.10 < av1["av1c"]["residual_5term"] < 0.15


def test_av1c_phi11_squared_still_dominant_term(av1):
    """Even though AV-1c failed, φ₁₁² is the FIRST greedy pick — partial signal."""
    assert tuple(av1["av1c"]["greedy_5term_modes"][0]) == (1, 1)
    assert av1["av1c"]["phi11_sq_in_top5"] is True


# ---------------------------------------------------------------------------
# H-T1 — exploratory, NOT promoted (promotion required AV-1c PASS)
# ---------------------------------------------------------------------------

def test_ht1_signal_present_but_not_promoted(av1):
    ht1 = av1["ht1_exploratory"]
    assert ht1["signal"] is True
    assert ht1["boundary_family_explained_norm"] > 0.90
    assert "EXPLORATORY_ONLY" in ht1["status"]


# ---------------------------------------------------------------------------
# Scope fences
# ---------------------------------------------------------------------------

def test_angular_still_not_verified(av1):
    assert "NOT VERIFIED" in av1["scope"]["angular"]
    assert "AV-2" in av1["scope"]["angular"]


def test_no_promotion(av1):
    assert "research_only" in av1["scope"]["promotion"]
    assert av1["scope"]["lambda"] == "FREE_COUPLING_PARAMETER"


# ---------------------------------------------------------------------------
# Numerical hygiene
# ---------------------------------------------------------------------------

def test_dictionary_modes_normalized():
    alpha = alpha_grid(N_GRID)
    _, dictionary = build_dictionary(alpha, l_max=2, n_extra=2)
    for mode in dictionary:
        assert abs(inner_w(mode, mode, alpha) - 1.0) < 1e-10


def test_tom_ansatz_normalization():
    alpha = alpha_grid(N_GRID)
    tom = normalize(tom_ansatz(alpha), alpha)
    assert abs(inner_w(tom, tom, alpha) - 1.0) < 1e-10


def test_deterministic():
    r1 = run_av1(n_grid=500)
    r2 = run_av1(n_grid=500)
    assert r1["av1a"]["argmax_value"] == r2["av1a"]["argmax_value"]
