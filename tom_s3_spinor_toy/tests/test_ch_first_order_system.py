"""Tests — AV-2 G0: Camporesi-Higuchi first-order system verified from PDF.

Source: references/camporesi_higuchi_grqc9505009.pdf, eqs 3.27-3.30, 3.38.
Register: experiments/.../source_register_av2.md.

These regressions pin the code to the PDF formulas:
  eq 3.27: g_nl_hopf IS the C-H partner component (not just a mirror guess)
  eq 3.28: mirror identity with sign (-1)^(n-l)
  eq 3.29/3.30: coupled first-order Dirac system (the 2-component G1 system)
  eq 3.38: closed-form normalization with weight sin^2(theta)
"""

from __future__ import annotations

from math import factorial, gamma

import numpy as np
import pytest

from tom_s3_spinor_toy.discrete_radial_dirac_proxy import g_nl_hopf
from tom_s3_spinor_toy.reference_spinor_harmonics import phi_nl_hopf

N_SPHERE = 3          # S³
RHO = (N_SPHERE - 1) / 2.0
MODES = [(0, 0), (1, 0), (1, 1), (2, 1), (3, 2)]


@pytest.fixture(scope="module")
def theta_grid():
    theta = np.linspace(0.05, np.pi - 0.05, 4001)
    return theta, theta / 2.0, theta[1] - theta[0]


# ---------------------------------------------------------------------------
# eq 3.28 — mirror identity (machine precision)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n,l", MODES + [(4, 1)])
def test_eq_3_28_mirror_identity(n, l, theta_grid):
    theta, alpha, _ = theta_grid
    psi = g_nl_hopf(n, l, alpha)
    mirror = (-1) ** (n - l) * phi_nl_hopf(n, l, (np.pi - theta) / 2.0)
    assert np.max(np.abs(psi - mirror)) / np.max(np.abs(psi)) < 1e-12


# ---------------------------------------------------------------------------
# eq 3.29 / 3.30 — coupled first-order system (FD precision)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n,l", MODES)
def test_eq_3_29_lowering(n, l, theta_grid):
    """[d/dθ + ρcotθ − (l+ρ)/sinθ] φ_nl = −(n+N/2) ψ_nl."""
    theta, alpha, h = theta_grid
    phi = phi_nl_hopf(n, l, alpha)
    psi = g_nl_hopf(n, l, alpha)
    lhs = (
        np.gradient(phi, h)
        + RHO * np.cos(theta) / np.sin(theta) * phi
        - (l + RHO) / np.sin(theta) * phi
    )
    rhs = -(n + N_SPHERE / 2.0) * psi
    interior = slice(200, -200)
    rel = np.max(np.abs(lhs[interior] - rhs[interior])) / np.max(np.abs(rhs[interior]))
    assert rel < 1e-5


@pytest.mark.parametrize("n,l", MODES)
def test_eq_3_30_raising(n, l, theta_grid):
    """[d/dθ + ρcotθ + (l+ρ)/sinθ] ψ_nl = +(n+N/2) φ_nl."""
    theta, alpha, h = theta_grid
    phi = phi_nl_hopf(n, l, alpha)
    psi = g_nl_hopf(n, l, alpha)
    lhs = (
        np.gradient(psi, h)
        + RHO * np.cos(theta) / np.sin(theta) * psi
        + (l + RHO) / np.sin(theta) * psi
    )
    rhs = (n + N_SPHERE / 2.0) * phi
    interior = slice(200, -200)
    rel = np.max(np.abs(lhs[interior] - rhs[interior])) / np.max(np.abs(rhs[interior]))
    assert rel < 1e-5


# ---------------------------------------------------------------------------
# eq 3.38 — closed-form normalization, weight sin^{N-1}θ
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n,l", MODES)
def test_eq_3_38_normalization(n, l):
    theta = np.linspace(1e-6, np.pi - 1e-6, 200001)
    numeric = np.trapezoid(
        np.sin(theta) ** (N_SPHERE - 1) * phi_nl_hopf(n, l, theta / 2.0) ** 2, theta
    )
    closed = (
        2 ** (N_SPHERE - 2)
        * gamma(N_SPHERE / 2.0 + n) ** 2
        / (factorial(n - l) * factorial(N_SPHERE + n + l - 1))
    )
    assert abs(numeric - closed) / closed < 1e-10


def test_eq_3_37_both_components_equal_norm():
    """By eq 3.28 the φ and ψ integrals in eq 3.37 are equal."""
    theta = np.linspace(1e-6, np.pi - 1e-6, 100001)
    alpha = theta / 2.0
    w = np.sin(theta) ** 2
    for n, l in MODES:
        i_phi = np.trapezoid(w * phi_nl_hopf(n, l, alpha) ** 2, theta)
        i_psi = np.trapezoid(w * g_nl_hopf(n, l, alpha) ** 2, theta)
        assert abs(i_phi - i_psi) / i_phi < 1e-10


# ---------------------------------------------------------------------------
# H-AV2 ingredient (PDF p.9): partner is NONZERO at south pole for l=0
# ---------------------------------------------------------------------------

def test_partner_l0_nonzero_at_south_pole():
    """ψ_n0(θ→π) ≠ 0 — the cos⁰ boundary behavior the radial proxy lacked."""
    alpha_near_pi2 = np.array([np.pi / 2 - 1e-6])
    for n in range(4):
        val = abs(g_nl_hopf(n, 0, alpha_near_pi2)[0])
        assert val > 0.1, f"psi_{n}0 unexpectedly small at south pole: {val}"


def test_phi_l_vanishes_at_south_pole():
    """Contrast: φ_nl(θ→π) → 0 as cos^{l+1} — the proxy-level obstruction."""
    alpha_near_pi2 = np.array([np.pi / 2 - 1e-6])
    for n, l in [(0, 0), (1, 1), (2, 2)]:
        assert abs(phi_nl_hopf(n, l, alpha_near_pi2)[0]) < 1e-5
