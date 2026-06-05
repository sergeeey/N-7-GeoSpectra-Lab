"""S³ geometry in Hopf coordinates — VERIFIED_FROM_PDF.

Hopf coordinates (Ben Achour 2016, arXiv:1505.03426v2, eq 1):
    x¹ = sinα cosφ,  x² = sinα sinφ
    x³ = cosα cosθ,  x⁴ = cosα sinθ
    α ∈ [0, π/2],  φ, θ ∈ [0, 2π]

Metric (VERIFIED_FROM_PDF):
    ds² = dα² + cos²α dθ² + sin²α dφ²
    det(g) = cos²α sin²α,  √det(g) = sinα cosα

Volume sanity check: ∫₀^{π/2} ∫₀^{2π} ∫₀^{2π} sinα cosα dα dθ dφ = 2π²
"""

from __future__ import annotations

import numpy as np
from scipy import integrate


def volume_measure(alpha: np.ndarray) -> np.ndarray:
    """Volume measure √g = sinα cosα = sin(2α)/2 in Hopf coordinates."""
    return np.sin(alpha) * np.cos(alpha)


def s3_volume_numerical() -> float:
    """Compute S³ volume numerically. Expected: 2π² ≈ 19.7392."""
    radial, _ = integrate.quad(lambda a: np.sin(a) * np.cos(a), 0.0, np.pi / 2)
    return radial * (2.0 * np.pi) ** 2


def s3_volume_analytical() -> float:
    """Analytical S³ volume = 2π²."""
    return 2.0 * np.pi**2


def weighted_inner_product(
    f: np.ndarray,
    g_func: np.ndarray,
    alpha_grid: np.ndarray,
) -> float:
    """Compute ⟨f, g⟩_w = ∫ f(α) g(α) sinα cosα dα · (2π)².

    Weighted L²(S³, sinα cosα dα dθ dφ) inner product.
    The (2π)² factor integrates over θ, φ ∈ [0, 2π].
    """
    integrand = f * np.conj(g_func) * volume_measure(alpha_grid)
    return float(np.trapz(integrand, alpha_grid).real) * (2.0 * np.pi) ** 2
