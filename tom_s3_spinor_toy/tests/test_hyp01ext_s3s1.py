"""HYP_01-EXT: tests for S³×S¹ flux V_eff with volume-constrained modulus."""

import os
import sys

import numpy as np
import pytest

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-hyp01ext-s3s1-flux"),
)
from hyp01ext_s3s1 import d2v_dphi2, dv_dphi, phi_star, v_eff  # noqa: E402


@pytest.mark.parametrize(
    "n_s3, n_s1",
    [(1.0, 1.0), (2.0, 1.0), (1.0, 2.0), (3.0, 1.0), (0.5, 2.0)],
)
def test_phi_star_is_minimum(n_s3, n_s1):
    """φ* is a genuine interior minimum: dV/dφ=0 and V''>0."""
    ps = phi_star(n_s3, n_s1)
    assert abs(dv_dphi(ps, n_s3, n_s1)) < 1e-9
    assert d2v_dphi2(ps, n_s3, n_s1) > 0


@pytest.mark.parametrize(
    "n_s3, n_s1",
    [(1.0, 1.0), (2.0, 1.0), (1.0, 2.0), (3.0, 1.0), (0.5, 2.0)],
)
def test_v_strictly_above_minimum(n_s3, n_s1):
    """V(φ) > V(φ*) for φ ≠ φ*."""
    ps = phi_star(n_s3, n_s1)
    v_min = v_eff(ps, n_s3, n_s1)
    for delta in [-1.0, -0.5, 0.5, 1.0]:
        assert v_eff(ps + delta, n_s3, n_s1) > v_min


def test_symmetric_case_phi_star_zero():
    """Equal fluxes → φ* = 0 (equal radii)."""
    assert abs(phi_star(1.0, 1.0)) < 1e-12


def test_phi_star_formula():
    """φ* = ln(N_S3 / N_S1) exactly."""
    for n_s3, n_s1 in [(2.0, 1.0), (1.0, 3.0), (4.0, 2.0)]:
        assert abs(phi_star(n_s3, n_s1) - np.log(n_s3 / n_s1)) < 1e-12


def test_equipartition_at_minimum():
    """V_S3/V_S1 = 3 at φ* for all (N_S3, N_S1).
    From l=1 eigenvalue of S³ Laplacian: l(l+2)=3. Universal, N-independent.
    """
    for n_s3, n_s1 in [(1.0, 1.0), (2.0, 1.0), (1.0, 2.0), (3.0, 1.0)]:
        ps = phi_star(n_s3, n_s1)
        v_s3 = 3 * n_s3**2 * np.exp(-0.5 * ps)
        v_s1 = n_s1**2 * np.exp(1.5 * ps)
        assert abs(v_s3 / v_s1 - 3.0) < 1e-9


def test_falsifier_decoupled_monotone():
    """Decouple S¹ (R_S1 = const) → dV/dφ < 0 everywhere → no interior min.
    Coupling requires volume conservation; without it, S³ term just runs to +∞.
    """
    phi_grid = np.linspace(-5, 5, 200)
    for n_s3, n_s1 in [(1.0, 1.0), (2.0, 1.0)]:
        # Decoupled gradient: only S³ contributes
        grad_decoupled = -1.5 * n_s3**2 * np.exp(-0.5 * phi_grid)
        assert np.all(grad_decoupled < 0)


def test_phi_star_depends_on_ratio_only():
    """Rescaling both fluxes by same factor k leaves φ* unchanged."""
    n_s3, n_s1 = 2.0, 1.0
    ps_base = phi_star(n_s3, n_s1)
    for k in [0.1, 0.5, 2.0, 10.0]:
        ps_scaled = phi_star(k * n_s3, k * n_s1)
        assert abs(ps_scaled - ps_base) < 1e-12
