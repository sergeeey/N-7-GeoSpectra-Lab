"""Tests — AV1C_PRIME_CROSS_BILINEAR_DICTIONARY (v0.2.0).

Pre-registered: experiments/.../claim_av1c_prime.md (BEFORE code ran).
Outcomes locked as regressions:
  PRIMARY (D2): 13.0% > 10%  -> KILL, H-T1 stays NOT_PROMOTED (honest)
  P1 CONFIRMED: residual peaks at alpha = pi/2 (boundary cos-exponent obstruction)
  P2 CONFIRMED: constant f^(phi) term is load-bearing (37.9% -> 13.0%)
  D3: full-LS ~5e-4 (target IS in extended span) but greedy 5-term only 8.9%
      -> eq. 49 radial layer is DENSE in bilinears, not sparse
"""

from __future__ import annotations

import pytest

from tom_s3_spinor_toy.av1c_prime_cross_bilinear import (
    BOUNDARY_FAMILY,
    run_av1c_prime,
    run_dictionary,
    verdict_from_residual,
)

N_GRID = 2000


@pytest.fixture(scope="module")
def av1cp():
    return run_av1c_prime(n_grid=N_GRID)


# ---------------------------------------------------------------------------
# Primary endpoint — KILL locked as regression
# ---------------------------------------------------------------------------

def test_primary_verdict_is_kill(av1cp):
    """D2 5-term residual 13.0% > 10% pre-registered kill threshold.

    H-T1 (sparse boundary-family bilinear structure) is KILLED in its sparse
    form. If this starts passing the promote threshold after a code change,
    the math changed — investigate before celebrating.
    """
    assert av1cp["verdict"] == "KILL_HT1_STAYS_NOT_PROMOTED"
    assert 0.10 < av1cp["d2_primary"]["residual_5term"] < 0.16


def test_verdict_rule_boundaries():
    assert verdict_from_residual(0.04) == "PROMOTE_HT1_RADIAL_BILINEAR_STRUCTURE_SUPPORTED"
    assert verdict_from_residual(0.07) == "IMPROVED_BUT_INSUFFICIENT_HT1_STAYS_EXPLORATORY"
    assert verdict_from_residual(0.13) == "KILL_HT1_STAYS_NOT_PROMOTED"


# ---------------------------------------------------------------------------
# P2 — constant f^(phi) term is load-bearing (eq. 49 structure)
# ---------------------------------------------------------------------------

def test_p2_constant_term_load_bearing(av1cp):
    """Adding const drops residual by >2x (37.9% -> 13.0%): f^(phi) necessary."""
    assert av1cp["mechanism"]["P2_constant_term_load_bearing"] is True
    d1_res = av1cp["d1_pure_bilinears"]["residual_5term"]
    d2_res = av1cp["d2_primary"]["residual_5term"]
    assert d2_res < 0.5 * d1_res


def test_d1_pure_bilinears_fail_badly(av1cp):
    """Boundary-family bilinears WITHOUT const: ~38% — worse than diagonal AV-1c."""
    assert av1cp["d1_pure_bilinears"]["residual_5term"] > 0.30


def test_constant_chosen_by_greedy(av1cp):
    assert av1cp["d2_primary"]["constant_in_top5"] is True
    assert av1cp["d3_extended"]["constant_in_top5"] is True


# ---------------------------------------------------------------------------
# P1 — residual concentrates at alpha = pi/2 (pre-registered analytic prior)
# ---------------------------------------------------------------------------

def test_p1_residual_peaks_at_boundary(av1cp):
    """cos^1 (target) vs cos^>=2 (bilinears) mismatch -> peak at alpha/pi = 0.5."""
    assert abs(av1cp["d2_primary"]["residual_peak_alpha_over_pi"] - 0.5) < 0.02
    assert abs(av1cp["d3_extended"]["residual_peak_alpha_over_pi"] - 0.5) < 0.02


# ---------------------------------------------------------------------------
# D3 — dense representability: span contains target, sparsity does not
# ---------------------------------------------------------------------------

def test_d3_full_span_contains_target(av1cp):
    """Full LS over 120 pairs + const: residual < 1%.

    Caveat: 120-element Gram matrix is ill-conditioned; this is evidence the
    target is (numerically) in the span, not a sparse-structure claim.
    """
    assert av1cp["d3_extended"]["residual_full_ls"] < 0.01


def test_d3_sparse_still_insufficient(av1cp):
    """Greedy 5-term on D3: ~8.9% — in the improved-but-insufficient band."""
    assert 0.05 < av1cp["d3_extended"]["residual_5term"] <= 0.10


# ---------------------------------------------------------------------------
# Sensitivity (pre-registered)
# ---------------------------------------------------------------------------

def test_sensitivity_fine_grid_stable(av1cp):
    d2 = av1cp["d2_primary"]["residual_5term"]
    fine = av1cp["sensitivity_fine_grid"]["residual_5term"]
    assert abs(d2 - fine) < 0.01


def test_sensitivity_unweighted_also_kills(av1cp):
    """KILL must be convention-robust: unweighted residual also > 10%."""
    assert av1cp["sensitivity_unweighted"]["residual_5term"] > 0.10


# ---------------------------------------------------------------------------
# Scope fences
# ---------------------------------------------------------------------------

def test_no_promotion_scope(av1cp):
    assert "NOT full spinor identification" in av1cp["scope"]["promotion_ceiling"]
    assert av1cp["scope"]["lambda"] == "FREE_COUPLING_PARAMETER"
    assert "AV-2 pending" in av1cp["scope"]["angular"]


def test_deterministic():
    r1 = run_dictionary("t", BOUNDARY_FAMILY, True, n_grid=500)
    r2 = run_dictionary("t", BOUNDARY_FAMILY, True, n_grid=500)
    assert r1["residual_5term"] == r2["residual_5term"]
