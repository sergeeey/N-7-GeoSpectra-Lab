"""Analytic Dirac spectrum computation for the round S6 baseline.

This module turns the frozen S6 contract into an explicit closed-form
computation layer. It stays within the round S6 / G2-SU(3) convention fixed by
the earlier contract layers and does not claim any SU(4), hypercharge,
instanton, index, or chirality result.

The standard round-sphere Dirac spectrum is

    lambda_{k,+/-} = +/- (k + n/2) / R

with multiplicity

    mu_k = 2^{floor(n/2)} * binomial(k + n - 1, k)

for the n-sphere. For S6 this becomes

    lambda_{k,+/-} = +/- (k + 3) / R
    mu_k = 8 * binomial(k + 5, k)

This is the closed-form spectrum we compute here.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb
from typing import Any, Final


S6_SPECTRUM_COMPUTATION_STATUS: Final[str] = "started"
S6_RUNTIME_STATUS: Final[str] = "research_only"
S6_V_SELECTION_STATUS: Final[str] = "smoke_only"
S6_SAFE_FOR_RUNTIME: Final[bool] = False


def _validate_inputs(k_max: int, radius: float) -> None:
    if not isinstance(k_max, int):
        raise TypeError(f"k_max must be an int, got {type(k_max).__name__}")
    if k_max < 0:
        raise ValueError(f"k_max must be non-negative, got {k_max!r}")
    if radius <= 0:
        raise ValueError(f"radius must be positive, got {radius!r}")


@dataclass(frozen=True)
class S6DiracSpectrumLevel:
    """Single signed spectral level for the round S6 Dirac operator."""

    k: int
    sign: str
    eigenvalue: float
    degeneracy: int
    radius: float


def analytic_dirac_spectrum_s6(k_max: int, radius: float = 1.0) -> list[dict[str, Any]]:
    """Return the exact clean Dirac spectrum on round S6 up to ``k_max``."""

    _validate_inputs(k_max, radius)

    spectrum: list[dict[str, Any]] = []
    for k in range(k_max + 1):
        degeneracy = 8 * comb(k + 5, k)
        eigenvalue = (k + 3.0) / radius
        spectrum.append(
            {
                "k": k,
                "sign": "+",
                "eigenvalue": eigenvalue,
                "degeneracy": degeneracy,
            }
        )
        spectrum.append(
            {
                "k": k,
                "sign": "-",
                "eigenvalue": -eigenvalue,
                "degeneracy": degeneracy,
            }
        )
    return spectrum


def total_number_of_modes_s6(k_max: int) -> int:
    """Return the total degeneracy count for both signs through ``k_max``."""

    _validate_inputs(k_max, radius=1.0)
    return 2 * sum(8 * comb(k + 5, k) for k in range(k_max + 1))


def s6_spectrum_computation_summary(k_max: int = 3, radius: float = 1.0) -> dict[str, object]:
    """Return a compact summary suitable for report generation and testing."""

    spectrum = analytic_dirac_spectrum_s6(k_max=k_max, radius=radius)
    return {
        "status": S6_SPECTRUM_COMPUTATION_STATUS,
        "runtime_status": S6_RUNTIME_STATUS,
        "v_selection_status": S6_V_SELECTION_STATUS,
        "safe_for_runtime": S6_SAFE_FOR_RUNTIME,
        "identity": "S6 ≅ G2 / SU(3)",
        "reductive_split": "g2 = su(3) ⊕ m",
        "metric_normalization": "unit round S6 normalization",
        "connection_choice": "Levi-Civita connection on the canonical homogeneous metric",
        "spinor_bundle_convention": "canonical spin structure induced by the G2/SU(3) reductive frame",
        "dirac_operator_convention": "homogeneous Dirac operator with Casimir cross-check target",
        "casimir_cross_check": "D ~ C_G + (1/8) s",
        "spectrum_target": "homogeneous Dirac spectrum on S6, derived as the round-sphere baseline",
        "radius": radius,
        "k_max": k_max,
        "spectrum": spectrum,
        "total_number_of_modes": total_number_of_modes_s6(k_max),
    }
