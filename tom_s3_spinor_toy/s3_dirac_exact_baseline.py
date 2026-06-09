"""Exact clean Dirac spectrum baseline on the round three-sphere S3.

Scope:
    Analytic negative control only. This module does not construct spinor
    wavefunctions, gauge fields, instantons, numerical kNN spectra, or any
    Tom Lawrence theory-validation claim.

Working convention:
    Downstream representation checks use ``ben_achour_displayed_phase`` from
    ``wigner_d_micro_audit.py``. The Ben Achour xi' sign gap remains open but
    operationally unblocked.

Spectrum:
    lambda_{k,+/-} = +/- (k + 3/2) / R
    degeneracy per sign d_k = (k + 1)(k + 2)
    k = 0, 1, 2, ...
"""

from __future__ import annotations

from typing import Any


def _validate_inputs(k_max: int, radius: float) -> None:
    if not isinstance(k_max, int):
        raise TypeError(f"k_max must be an int, got {type(k_max).__name__}")
    if k_max < 0:
        raise ValueError(f"k_max must be non-negative, got {k_max!r}")
    if radius <= 0:
        raise ValueError(f"radius must be positive, got {radius!r}")


def analytic_dirac_spectrum_s3(k_max: int, radius: float = 1.0) -> list[dict[str, Any]]:
    """Return the exact clean Dirac spectrum on round S3 up to ``k_max``.

    Each returned dictionary has:
        k: non-negative level index;
        sign: "+" or "-";
        eigenvalue: signed Dirac eigenvalue;
        degeneracy: multiplicity for that sign.
    """
    _validate_inputs(k_max, radius)

    spectrum: list[dict[str, Any]] = []
    for k in range(k_max + 1):
        degeneracy = (k + 1) * (k + 2)
        eigenvalue = (k + 1.5) / radius
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


def total_number_of_modes(k_max: int) -> int:
    """Return the total degeneracy count for both signs through ``k_max``."""
    _validate_inputs(k_max, radius=1.0)
    return 2 * sum((k + 1) * (k + 2) for k in range(k_max + 1))
