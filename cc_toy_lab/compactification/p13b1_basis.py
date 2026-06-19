"""P13B1 repaired spinor-state basis on Lawrence/Hopf S3 chart."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np

from cc_toy_lab.compactification.registry_loader import load_registry
from cc_toy_lab.compactification.s3_lawrence_hopf import total_s3_volume_analytic, volume_weight

ConventionId = Literal["CONV_HAAR_UNIT", "CONV_HAAR_HARMONIC_SQRT2"]


@dataclass(frozen=True)
class SpinorMode:
    index: int
    label: str
    spinor: np.ndarray  # shape (4,)
    profile: str


def _spatial_profile(name: str, alpha: np.ndarray, theta: np.ndarray) -> np.ndarray:
    if name == "constant":
        return np.ones_like(alpha, dtype=float)
    if name == "sin(alpha) * cos(theta)":
        return np.sin(alpha) * np.cos(theta)
    raise ValueError(f"Unknown profile: {name}")


def load_modes() -> list[SpinorMode]:
    data = load_registry("P13B1_spinor_basis.yaml")
    modes: list[SpinorMode] = []
    for entry in data["modes"]:
        modes.append(
            SpinorMode(
                index=int(entry["index"]),
                label=str(entry["label"]),
                spinor=np.array(entry["spinor_direction"], dtype=complex),
                profile=str(entry["spatial_profile"]),
            )
        )
    return modes


def spinor_field(
    mode: SpinorMode,
    alpha: np.ndarray,
    theta: np.ndarray,
    convention: ConventionId,
) -> np.ndarray:
    """Return psi(x) shape (4, n_points)."""
    spatial = _spatial_profile(mode.profile, alpha, theta)
    if mode.index == 1 and convention == "CONV_HAAR_HARMONIC_SQRT2":
        spatial = spatial * np.sqrt(2.0)
    return mode.spinor[:, None] * spatial[None, :]


def normalize_spinor(
    mode: SpinorMode,
    alpha: np.ndarray,
    theta: np.ndarray,
    theta_tilde: np.ndarray,
    convention: ConventionId,
) -> tuple[np.ndarray, float]:
    """L2 normalize on Haar grid; return field and norm factor."""
    psi = spinor_field(mode, alpha, theta, convention)
    w = volume_weight(alpha)
    dtheta = 2.0 * np.pi / max(theta.size - 1, 1)
    dtheta_tilde = 2.0 * np.pi / max(theta_tilde.size - 1, 1)
    dalpha = (0.5 * np.pi) / max(alpha.size - 1, 1)
    weight = w * dalpha * dtheta * dtheta_tilde
    norm_sq = 0.0
    for p in range(psi.shape[1]):
        norm_sq += float(np.vdot(psi[:, p], psi[:, p]).real * weight[p])
    scale = 1.0 / np.sqrt(norm_sq)
    psi = psi * scale
    # P13G: allowed amplitude convention for harmonic mode (not a silent repair)
    if mode.index == 1 and convention == "CONV_HAAR_HARMONIC_SQRT2":
        psi = psi * np.sqrt(2.0)
    return psi, float(scale)


def primary_pair_indices() -> tuple[int, int]:
    data = load_registry("P13B1_spinor_basis.yaml")
    pair = data.get("primary_test_pair") or data.get("low_mode_pair")
    return int(pair[0]), int(pair[1])
