"""Tests — spectral-fingerprint proxy, v0.2.0 spinor-geometry pivot.

Primary endpoint: spectral fingerprint separation (ladder, |λ_min| = d/2,
spectral distance). IPR appears ONLY in NC-A as a closed-channel regression.

Analytic targets are independent ground truth (Camporesi-Higuchi,
VERIFIED_FROM_PDF) — the operator construction (W = κ/sinθ) does not embed
them, so a match is evidence, not tautology.
"""

from __future__ import annotations

import numpy as np
import pytest

from tom_s3_spinor_toy.spectral_fingerprint_proxy import (
    analytic_degeneracy_s3_dirac,
    analytic_dirac_ladder,
    analytic_lambda_min,
    analytic_scalar_eigenvalues,
    dirac_ladder,
    dirac_ladder_fd,
    dirac_ladder_shooting,
    discretization_survival,
    fingerprint_match_score,
    ipr_shift_invariance_gap,
    random_hermitian_match_score,
    s3_sector_structure,
    scalar_radial_eigenvalues,
    scalar_vs_dirac_same_sphere,
    spectral_distance,
    compute_fingerprint,
)

MCID_REL_TOL = 0.05  # estimand_v0.2.0.md §3


# ---------------------------------------------------------------------------
# Primary endpoint: eigenvalue ladder recovery (KT-1 / gate C9a)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("d", [3, 6])
def test_dirac_ladder_fd_matches_analytic(d):
    """FD ladder must hit λ = n + d/2 well inside the 5% MCID."""
    ladder = dirac_ladder_fd(d, 0, n_grid=4000, n_levels=4)
    target = np.asarray(analytic_dirac_ladder(d, 4))
    rel_err = np.max(np.abs(ladder - target) / target)
    assert rel_err < 1e-4, f"d={d}: rel_err={rel_err:.2e} (target <1e-4, MCID 5%)"


def test_dirac_ladder_d2_shooting_matches_analytic():
    """d=2 critical case (κ=1/2): shooting solver must recover λ = n + 1.

    Uniform FD fails here (limit-circle endpoint, ~5% error, rate h^0.1) —
    recorded as discretization-survival limitation.
    """
    ladder = dirac_ladder_shooting(2, 0, n_levels=3, e_max=14.0, n_scan=300)
    target = np.asarray(analytic_dirac_ladder(2, 3))
    assert len(ladder) == 3
    rel_err = np.max(np.abs(ladder - target) / target)
    assert rel_err < 1e-6, f"d=2 shooting rel_err={rel_err:.2e}"


@pytest.mark.parametrize("d", [3, 6])
def test_lambda_min_equals_half_d(d):
    """|λ_min| = d/2 — the dimension fingerprint (gate C9c)."""
    lam = dirac_ladder_fd(d, 0, n_grid=4000, n_levels=1)[0]
    assert abs(lam - analytic_lambda_min(d)) < 1e-3


# ---------------------------------------------------------------------------
# Cross-sphere discrimination (KT-2)
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def fingerprints():
    return {d: compute_fingerprint(d, n_levels=3) for d in (2, 3, 6)}


def test_cross_sphere_gap_s2_s3(fingerprints):
    """λ_min gap S³ − S² = 0.5; kill condition: error > 0.25 (KT-2)."""
    gap = fingerprints[3].lambda_min - fingerprints[2].lambda_min
    assert abs(gap - 0.5) < 0.05, f"gap={gap:.4f}, expected 0.5"


def test_spectral_distance_matches_analytic(fingerprints):
    """Ladder distance = |d_a − d_b| / 2 exactly (ladders are n + d/2)."""
    for (da, db), expected in {(2, 3): 0.5, (3, 6): 1.5, (2, 6): 2.0}.items():
        dist = spectral_distance(fingerprints[da], fingerprints[db])
        assert abs(dist - expected) < 0.05, (
            f"S{da}-S{db}: distance={dist:.4f}, expected {expected}"
        )


def test_three_spheres_pairwise_separated(fingerprints):
    """All three |λ_min| values mutually distinct beyond numerical error."""
    mins = sorted(fp.lambda_min for fp in fingerprints.values())
    assert min(b - a for a, b in zip(mins, mins[1:])) > 0.4


# ---------------------------------------------------------------------------
# S³ sector structure — partial numerical degeneracy (gate C9b, honest split)
# ---------------------------------------------------------------------------

def test_s3_sector_structure_and_degeneracy():
    """λ_n = n + 3/2 must appear in sectors l = 0..n (numerical content);
    with analytic angular factors 2(l+1) this reconstructs (n+1)(n+2).
    """
    result = s3_sector_structure(max_l=2)
    for entry in result["degeneracy_reconstruction"]:
        n = entry["n"]
        assert entry["sectors_containing"] == list(range(n + 1)), (
            f"λ_{n} found in sectors {entry['sectors_containing']}, expected 0..{n}"
        )
        assert entry["degeneracy_reconstructed"] == analytic_degeneracy_s3_dirac(n)
    # Dirac pattern differs from scalar (l+1)² at every level
    assert [e["degeneracy_analytic"] for e in result["degeneracy_reconstruction"]] == [2, 6, 12]


# ---------------------------------------------------------------------------
# Negative controls
# ---------------------------------------------------------------------------

def test_nc_a_ipr_shift_invariance():
    """NC-A (permanent regression): H → H + cI leaves IPR unchanged.

    R/4 = const on a homogeneous sphere ⟹ curvature term alone cannot make
    IPR geometry-sensitive. IPR is SECONDARY/EXPLORATORY, never primary.
    """
    assert ipr_shift_invariance_gap() < 1e-12


def test_nc_b_random_hermitian_no_fingerprint():
    """NC-B: GOE matrix must not reproduce the Dirac ladder."""
    assert random_hermitian_match_score() <= 0.25


def test_nc_c_scalar_vs_dirac_distinguishable():
    """NC-C: scalar and Dirac operators on the SAME sphere differ spectrally.

    Honest framing: the scalar SPECTRUM is geometry-sensitive (λ₁ = d);
    v0.1.22 GEOMETRY_AGNOSTIC concerned the vector/IPR channel on lattice
    products. This control shows operator-structure discrimination.
    """
    result = scalar_vs_dirac_same_sphere(d=3)
    assert result["cross_match_score"] <= 0.34


def test_scalar_radial_matches_analytic():
    """Scalar radial operator sanity: eigenvalues = L(L+d-1)."""
    for d in (3, 6):
        vals = scalar_radial_eigenvalues(d, n_levels=4)
        target = analytic_scalar_eigenvalues(d, 4)
        assert np.allclose(vals, target, atol=2e-3), f"d={d}: {vals} vs {target}"


# ---------------------------------------------------------------------------
# Discretization survival (estimand §7 / SA-1)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("d", [3, 6])
def test_discretization_survival_monotone(d):
    """Error must decrease with grid refinement and beat MCID at N=4000."""
    errors = discretization_survival(d, grids=(1000, 2000, 4000))
    assert errors[4000] < MCID_REL_TOL
    assert errors[1000] >= errors[2000] >= errors[4000]


def test_d2_fd_limitation_is_real():
    """Document the d=2 critical-case FD failure (must NOT silently pass).

    If this test ever fails because FD became accurate, the limitation
    entry in the module docstring and reports must be updated.
    """
    ladder = dirac_ladder_fd(2, 0, n_grid=4000, n_levels=1)
    err = abs(ladder[0] - 1.0)
    assert 0.01 < err < 0.10, (
        f"d=2 FD error {err:.4f} outside known band — update limitation docs"
    )


# ---------------------------------------------------------------------------
# Match-score helper
# ---------------------------------------------------------------------------

def test_fingerprint_match_score_basics():
    target = analytic_dirac_ladder(3, 3)  # [1.5, 2.5, 3.5]
    assert fingerprint_match_score(np.array([1.5, 2.5, 3.5]), target) == 1.0
    assert fingerprint_match_score(np.array([10.0, 20.0, 30.0]), target) == 0.0
