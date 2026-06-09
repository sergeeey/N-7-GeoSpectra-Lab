"""Tests for the preliminary Dirac spectrum visualization layer."""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent))

from s3_dirac_spectrum_viz import (  # noqa: E402
    compute_spectrum_trajectory,
    render_spectrum_trajectory,
    summarize_first_levels,
)


def test_compute_spectrum_trajectory_shapes() -> None:
    trajectory = compute_spectrum_trajectory(k_max=3, lambda_values=[0.0, 0.5, 1.0])

    assert trajectory.sorted_eigenvalues.shape[0] == 3
    assert trajectory.sorted_eigenvalues.shape[1] == trajectory.d0_eigenvalues.shape[0]
    assert np.allclose(trajectory.sorted_eigenvalues[0], trajectory.d0_eigenvalues)


def test_render_spectrum_trajectory(tmp_path: Path) -> None:
    trajectory = compute_spectrum_trajectory(k_max=3, lambda_values=[0.0, 1.0])
    out_path = render_spectrum_trajectory(trajectory, tmp_path / "spectrum.png")

    assert out_path.exists()
    assert out_path.stat().st_size > 0


def test_summarize_first_levels_returns_preliminary_views() -> None:
    trajectory = compute_spectrum_trajectory(k_max=3, lambda_values=[0.0, 1.0])
    summary = summarize_first_levels(trajectory, n_levels=5)

    assert set(summary) == {"lambda_min", "lambda_max", "d0"}
    assert len(summary["lambda_min"]) == 5
    assert len(summary["lambda_max"]) == 5
    assert len(summary["d0"]) == 5
