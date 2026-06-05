"""Tests: √sin(2α) is NOT a Dirac eigenfunction on S³."""

from __future__ import annotations

import numpy as np
import pytest

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from reference_spinor_harmonics import (
    phi_nl_hopf,
    tom_ansatz,
    eigenvalue_s3,
    unweighted_mode,
)
from geometry_s3_hopf import volume_measure, weighted_inner_product


def test_lowest_dirac_eigenfunction_is_cosine() -> None:
    """φ_{00}(α) ∝ cosα (lowest Dirac mode, Camporesi-Higuchi eq 3.25 with n=l=0)."""
    alpha = np.linspace(0.1, np.pi / 2 - 0.1, 200)
    phi = phi_nl_hopf(0, 0, alpha)
    expected = np.cos(alpha)
    ratio = phi / expected
    # Must be constant (proportional)
    np.testing.assert_allclose(
        ratio,
        ratio[0],
        rtol=1e-10,
        err_msg="φ_{00} must be proportional to cosα",
    )


def test_eigenvalue_formula_s3() -> None:
    """λ = +(n+3/2) for n=0,1,2 (Camporesi-Higuchi eq 3.26, VERIFIED_FROM_PDF)."""
    assert eigenvalue_s3(0) == pytest.approx(1.5)
    assert eigenvalue_s3(1) == pytest.approx(2.5)
    assert eigenvalue_s3(2) == pytest.approx(3.5)


def test_tom_ansatz_is_sqrt2_times_sqrt_measure() -> None:
    """√sin(2α) = √2 · √(sinα cosα) = √2 · (volume_measure)^{1/2}.

    This is the key structural fact: Tom's ansatz is proportional to the
    square root of the Riemannian volume density, not to an eigenfunction.
    """
    alpha = np.linspace(0.05, np.pi / 2 - 0.05, 500)
    tom = tom_ansatz(alpha)
    sqrt_measure = np.sqrt(volume_measure(alpha))
    np.testing.assert_allclose(
        tom,
        np.sqrt(2.0) * sqrt_measure,
        rtol=1e-12,
        err_msg="√sin(2α) must equal √2 · √(sinα cosα)",
    )


def test_tom_ansatz_not_proportional_to_any_eigenfunction() -> None:
    """√sin(2α) is not proportional to φ_{nl}(α) for any tested (n,l).

    If Tom's ansatz were a Dirac eigenfunction, the ratio φ_{nl}/√sin(2α)
    would be constant. We check it varies significantly.
    """
    alpha = np.linspace(0.1, np.pi / 2 - 0.1, 500)
    tom = tom_ansatz(alpha)
    for n in range(4):
        phi = phi_nl_hopf(n, 0, alpha)
        ratio = phi / (tom + 1e-30)
        rel_var = np.std(ratio) / (abs(np.mean(ratio)) + 1e-30)
        assert rel_var > 0.01, (
            f"φ_{{n={n},l=0}} appears proportional to √sin(2α)! rel_var={rel_var:.4f}"
        )


def test_tom_ansatz_overlaps_multiple_eigenfunctions() -> None:
    """Tom's ansatz has nonzero overlap with ≥2 eigenfunctions in weighted L².

    A true eigenfunction is orthogonal to all eigenfunctions of different
    eigenvalue. Nonzero overlap with multiple modes → it is a superposition.
    """
    alpha = np.linspace(0.01, np.pi / 2 - 0.01, 3000)
    tom = tom_ansatz(alpha)
    nonzero = 0
    for n in range(5):
        phi = phi_nl_hopf(n, 0, alpha)
        norm_sq = weighted_inner_product(phi, phi, alpha)
        norm = np.sqrt(abs(norm_sq))
        phi_normed = phi / norm if norm > 1e-12 else phi
        overlap = abs(weighted_inner_product(tom, phi_normed, alpha))
        if overlap > 1e-5:
            nonzero += 1
    assert nonzero >= 2, (
        f"Tom's ansatz overlaps {nonzero} eigenfunctions — expected ≥2 (superposition)"
    )


def test_require_n_geq_l() -> None:
    """phi_nl_hopf raises ValueError when n < l."""
    with pytest.raises(ValueError, match="n ≥ l"):
        phi_nl_hopf(0, 1, np.array([0.5]))
