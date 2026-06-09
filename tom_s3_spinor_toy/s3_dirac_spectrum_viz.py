"""Preliminary spectrum visualization utilities for the temporary Dirac smoke layer.

Scope:
    This module is a debug / preliminary artifact only. It sweeps the coupled
    operator D = D0 + lambda V across a lambda grid, extracts sorted spectra,
    and optionally renders a simple line plot.

    It does not claim a physical spectrum, an instanton, an index, chirality,
    spectral flow, eta invariants, or zero modes.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import numpy as np

from s3_dirac_with_temp_coupling import build_temp_coupled_dirac


@dataclass(frozen=True)
class SpectrumTrajectory:
    """Container for a lambda-sweep of sorted eigenvalues."""

    lambda_values: np.ndarray
    sorted_eigenvalues: np.ndarray
    d0_eigenvalues: np.ndarray
    metadata: dict[str, Any]


def compute_spectrum_trajectory(
    k_max: int = 3,
    lambda_values: Iterable[float] | None = None,
    radius: float = 1.0,
    alpha: float | None = None,
) -> SpectrumTrajectory:
    """Compute sorted spectra for the temporary D = D0 + lambda V smoke layer."""
    if lambda_values is None:
        lambda_values = np.linspace(0.0, 1.0, 11)

    lambda_array = np.asarray(list(lambda_values), dtype=float)
    if lambda_array.ndim != 1 or lambda_array.size == 0:
        raise ValueError("lambda_values must be a non-empty 1D iterable")

    spectra: list[np.ndarray] = []
    d0_reference: np.ndarray | None = None
    metadata: dict[str, Any] | None = None

    for lambda_val in lambda_array:
        result = build_temp_coupled_dirac(
            k_max=k_max,
            lambda_val=float(lambda_val),
            radius=radius,
            alpha=alpha,
        )
        eigenvalues = np.linalg.eigvalsh(result["D"])
        spectra.append(np.sort(eigenvalues))
        if d0_reference is None:
            d0_reference = np.sort(np.linalg.eigvalsh(result["D0"]))
            metadata = dict(result["metadata"])

    assert d0_reference is not None
    assert metadata is not None
    return SpectrumTrajectory(
        lambda_values=lambda_array,
        sorted_eigenvalues=np.stack(spectra, axis=0),
        d0_eigenvalues=d0_reference,
        metadata=metadata,
    )


def render_spectrum_trajectory(
    trajectory: SpectrumTrajectory,
    output_path: str | Path,
) -> Path:
    """Render a preliminary spectrum plot for the engineering smoke layer."""
    import matplotlib

    matplotlib.use("Agg", force=True)
    import matplotlib.pyplot as plt

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(9, 6), dpi=160)
    spectra = trajectory.sorted_eigenvalues
    lambda_values = trajectory.lambda_values

    for mode_index in range(spectra.shape[1]):
        ax.plot(
            lambda_values,
            spectra[:, mode_index],
            color="tab:blue",
            alpha=0.14,
            linewidth=0.9,
        )

    ax.plot(
        lambda_values,
        np.tile(trajectory.d0_eigenvalues[None, :], (lambda_values.size, 1)),
        color="tab:gray",
        alpha=0.08,
        linewidth=0.7,
    )

    ax.set_title("Temporary Dirac spectrum sweep: D = D0 + lambda V")
    ax.set_xlabel("lambda")
    ax.set_ylabel("eigenvalue")
    ax.axhline(0.0, color="black", linewidth=0.6, alpha=0.5)
    ax.grid(True, alpha=0.2)
    ax.text(
        0.01,
        0.01,
        "preliminary / pending final Ben Achour E/E' normalization / no physical claims",
        transform=ax.transAxes,
        fontsize=8,
        va="bottom",
        ha="left",
        alpha=0.75,
    )
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
    return output_path


def summarize_first_levels(trajectory: SpectrumTrajectory, n_levels: int = 10) -> dict[str, list[float]]:
    """Return the first few ordered eigenvalues at the endpoints of the sweep."""
    if n_levels <= 0:
        raise ValueError("n_levels must be positive")
    n_levels = min(n_levels, trajectory.sorted_eigenvalues.shape[1])
    return {
        "lambda_min": trajectory.sorted_eigenvalues[0, :n_levels].tolist(),
        "lambda_max": trajectory.sorted_eigenvalues[-1, :n_levels].tolist(),
        "d0": trajectory.d0_eigenvalues[:n_levels].tolist(),
    }
