"""Tests: S³ geometry sanity in Hopf coordinates."""

from __future__ import annotations

import numpy as np
import pytest

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from geometry_s3_hopf import (
    s3_volume_numerical,
    s3_volume_analytical,
    volume_measure,
    weighted_inner_product,
)


def test_volume_equals_2pi_squared() -> None:
    """S³ volume in Hopf coordinates must equal 2π²."""
    vol = s3_volume_numerical()
    expected = s3_volume_analytical()
    assert abs(vol - expected) / expected < 1e-8, (
        f"S³ volume = {vol:.8f}, expected 2π² = {expected:.8f}"
    )


def test_volume_measure_vanishes_at_endpoints() -> None:
    """√g = sinα cosα must vanish at α=0 and α=π/2."""
    assert volume_measure(np.array([0.0]))[0] == pytest.approx(0.0, abs=1e-15)
    assert volume_measure(np.array([np.pi / 2]))[0] == pytest.approx(0.0, abs=1e-15)


def test_volume_measure_maximum_at_pi_over_4() -> None:
    """√g = sinα cosα is maximized at α=π/4."""
    alpha = np.linspace(0.001, np.pi / 2 - 0.001, 10_000)
    w = volume_measure(alpha)
    max_idx = int(np.argmax(w))
    assert abs(alpha[max_idx] - np.pi / 4) < 2e-3


def test_volume_measure_equals_sin2alpha_over_2() -> None:
    """√g = sinα cosα = sin(2α)/2 (algebraic identity)."""
    alpha = np.linspace(0.1, np.pi / 2 - 0.1, 200)
    np.testing.assert_allclose(
        volume_measure(alpha),
        np.sin(2 * alpha) / 2.0,
        rtol=1e-12,
    )


def test_weighted_inner_product_symmetry() -> None:
    """⟨f, g⟩_w = ⟨g, f⟩_w (real functions)."""
    alpha = np.linspace(0.05, np.pi / 2 - 0.05, 500)
    f = np.sin(alpha)
    g = np.cos(alpha)
    assert weighted_inner_product(f, g, alpha) == pytest.approx(
        weighted_inner_product(g, f, alpha), rel=1e-10
    )
