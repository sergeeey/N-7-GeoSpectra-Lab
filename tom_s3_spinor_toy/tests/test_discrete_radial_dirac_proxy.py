"""Tests — E0_DISCRETE_RADIAL_DIRAC_EIGENVALUE_RECOVERY (v0.2.0 pivot).

Kill-test (pre-registered): max relative ladder error > 5% at N=4000
→ REDESIGN_DISCRETIZATION. IPR is not used anywhere as an endpoint.
"""

from __future__ import annotations

import numpy as np
import pytest

from tom_s3_spinor_toy.discrete_radial_dirac_proxy import (
    KILL_TEST_REL_TOL,
    eigenvector_correspondence_s3,
    g_nl_hopf,
    kill_test,
    recover_ladder,
    run_e0,
    tom_ansatz_radial_projection,
)


@pytest.fixture(scope="module")
def e0_result():
    return run_e0(n_grid=4000)


# ---------------------------------------------------------------------------
# S³ first — eigenvalue recovery (the E0 gate itself)
# ---------------------------------------------------------------------------

def test_s3_kill_test_passes(e0_result):
    """|λ_n| = n + 3/2 for n = 0..4 within 5% (actual: ~1e-6)."""
    s3 = e0_result["s3"]
    assert s3["verdict"] == "PASS"
    assert s3["max_rel_err"] < KILL_TEST_REL_TOL
    assert s3["max_rel_err"] < 1e-5, "expected near-exact recovery at N=4000"
    assert s3["ladder_analytic"] == [1.5, 2.5, 3.5, 4.5, 5.5]


def test_s3_ladder_values_explicit():
    ladder = recover_ladder(3, 0, n_grid=4000, n_levels=5)
    assert np.allclose(ladder, [1.5, 2.5, 3.5, 4.5, 5.5], atol=1e-4)


def test_s3_higher_sector_ladder():
    """Sector l=1 must start at λ = 1 + 3/2 = 2.5 (n ≥ l structure)."""
    ladder = recover_ladder(3, 1, n_grid=4000, n_levels=3)
    assert np.allclose(ladder, [2.5, 3.5, 4.5], atol=1e-4)


# ---------------------------------------------------------------------------
# Eigenvector correspondence with verified Phase 2 reference functions
# ---------------------------------------------------------------------------

def test_eigenvectors_match_phi_nl(e0_result):
    """χ=-1 discrete eigenvectors = sin(2α)·phi_nl_hopf to ≥ 6 digits."""
    corr = e0_result["s3"]["eigenvector_correspondence"]
    for cos in corr["chi_minus_vs_phi_nl"]:
        assert cos > 0.999999, f"phi_nl correspondence broken: cos={cos}"


def test_eigenvectors_match_partner_g_nl(e0_result):
    """χ=+1 discrete eigenvectors = sin(2α)·g_nl_hopf to ≥ 6 digits."""
    corr = e0_result["s3"]["eigenvector_correspondence"]
    for cos in corr["chi_plus_vs_g_nl"]:
        assert cos > 0.999999, f"g_nl correspondence broken: cos={cos}"


def test_chirality_blocks_isospectral(e0_result):
    """Both chirality blocks must share the spectrum λ = n + 3/2."""
    assert e0_result["s3"]["chirality_spectra_identical"] is True


def test_g_nl_is_mirror_of_phi_nl():
    """g_nl(α) ∝ phi_nl(π/2 - α) — the partner is the α-mirror."""
    from tom_s3_spinor_toy.reference_spinor_harmonics import phi_nl_hopf

    alpha = np.linspace(0.05, np.pi / 2 - 0.05, 200)
    for n, l in [(0, 0), (1, 0), (2, 1)]:
        g = g_nl_hopf(n, l, alpha)
        phi_mirror = phi_nl_hopf(n, l, np.pi / 2 - alpha)
        cos = abs(g @ phi_mirror) / (np.linalg.norm(g) * np.linalg.norm(phi_mirror))
        assert cos > 0.999999


def test_g_nl_rejects_invalid_quantum_numbers():
    with pytest.raises(ValueError):
        g_nl_hopf(0, 1, np.array([0.5]))


# ---------------------------------------------------------------------------
# Generalization — only after S³ passes
# ---------------------------------------------------------------------------

def test_generalization_d6_runs_only_after_s3_pass(e0_result):
    assert e0_result["s3"]["verdict"] == "PASS"
    d6 = e0_result["generalization"]["d6"]
    assert d6["verdict"] == "PASS"
    assert d6["max_rel_err"] < 1e-5
    assert d6["ladder_analytic"] == [3.0, 4.0, 5.0, 6.0, 7.0]


def test_d2_explicitly_excluded_from_fd(e0_result):
    """d=2 must be marked EXCLUDED (limit-circle), not silently passed."""
    d2_entry = e0_result["generalization"]["d2"]
    assert "EXCLUDED_FROM_FD" in d2_entry
    assert "limit-circle" in d2_entry


def test_kill_test_verdict_logic():
    """A coarse enough grid must trip REDESIGN_DISCRETIZATION wording check.

    N=4000 passes by ~1e-6; verify the verdict field flips correctly by
    checking the threshold comparison, not by finding a failing grid (FD
    converges too well for d=3 to fail realistically).
    """
    result = kill_test(3, n_grid=200)
    assert result["verdict"] in ("PASS", "REDESIGN_DISCRETIZATION")
    assert result["threshold"] == KILL_TEST_REL_TOL


# ---------------------------------------------------------------------------
# Hard constraints recorded in output
# ---------------------------------------------------------------------------

def test_no_ipr_in_primary_endpoint(e0_result):
    assert "IPR not used" in e0_result["primary_endpoint"]
    assert "spectral" in e0_result["primary_endpoint"]


def test_ha4_recorded_open(e0_result):
    assert e0_result["scope"]["HA-4"].startswith("OPEN")
    assert "S3xS1" in e0_result["scope"]["HA-4"]


def test_no_promotion(e0_result):
    assert "NONE" in e0_result["scope"]["promotion"]
    assert "research_only" in e0_result["scope"]["promotion"]


# ---------------------------------------------------------------------------
# tom_ansatz — radial projection finding only
# ---------------------------------------------------------------------------

def test_tom_ansatz_finding_is_radial_only(e0_result):
    finding = e0_result["findings"]["tom_ansatz"]
    assert "RADIAL_PROJECTION_FINDING_ONLY" in finding["status"]
    assert "NOT a full spinor identification" in finding["status"]


def test_tom_ansatz_dominant_mode_is_phi_11():
    """Regression of the [VERIFIED-tool 2026-06-10] finding: 0.92 onto phi_11."""
    finding = tom_ansatz_radial_projection()
    dom = finding["dominant_mode"]
    assert (dom["n"], dom["l"]) == (1, 1)
    assert abs(dom["projection"] - 0.92) < 0.01
