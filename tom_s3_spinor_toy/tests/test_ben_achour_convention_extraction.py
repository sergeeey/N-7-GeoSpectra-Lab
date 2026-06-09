"""Regression checks for the Ben Achour S3 geometry extraction."""

from __future__ import annotations

from ben_achour_scalar_modes import (
    ben_achour_phase_eigenvalues,
    pdf_stated_killing_eigenvalues,
    scalar_mode_metadata,
)


def test_ben_achour_scalar_metadata_has_hopf_domain() -> None:
    meta = scalar_mode_metadata(2, 1, 0)

    assert meta["domain"] == "alpha in [0, pi/2], phi/theta in [0, 2pi)"
    assert meta["S"] == 1
    assert meta["D"] == 1
    assert meta["jacobi_order"] == 0


def test_ben_achour_phase_convention_is_recorded() -> None:
    displayed = ben_achour_phase_eigenvalues(1, 0)
    stated = pdf_stated_killing_eigenvalues(1, 0)

    assert displayed["xi"] == 2j
    assert displayed["xi_prime_from_displayed_phase"] == 0j
    assert stated["xi_pdf_stated"] == 2j
    assert stated["xi_prime_pdf_stated"] == 0j
