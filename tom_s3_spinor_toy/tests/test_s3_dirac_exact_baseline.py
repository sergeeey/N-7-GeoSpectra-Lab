"""Tests for the exact clean Dirac spectrum baseline on S3.

This is an analytic negative-control layer. It does not include gauge fields,
instantons, numerical kNN data, or a Tom Lawrence theory validation claim.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from s3_dirac_exact_baseline import (
    analytic_dirac_spectrum_s3,
    total_number_of_modes,
)


def test_spectrum_symmetric() -> None:
    """For each positive level there is a negative level with the same degeneracy."""
    spectrum = analytic_dirac_spectrum_s3(k_max=5, radius=1.0)
    positive = {entry["k"]: entry["degeneracy"] for entry in spectrum if entry["sign"] == "+"}
    negative = {entry["k"]: entry["degeneracy"] for entry in spectrum if entry["sign"] == "-"}

    assert positive == negative


def test_no_zero_eigenvalue() -> None:
    """The clean round S3 Dirac spectrum has no zero eigenvalues."""
    spectrum = analytic_dirac_spectrum_s3(k_max=5, radius=1.0)

    assert all(abs(entry["eigenvalue"]) > 1e-12 for entry in spectrum)


def test_first_levels() -> None:
    """The first three levels for R=1 are +/-1.5, +/-2.5, +/-3.5."""
    spectrum = analytic_dirac_spectrum_s3(k_max=2, radius=1.0)
    by_level = {
        (entry["k"], entry["sign"]): entry["eigenvalue"] for entry in spectrum
    }

    assert by_level[(0, "+")] == 1.5
    assert by_level[(0, "-")] == -1.5
    assert by_level[(1, "+")] == 2.5
    assert by_level[(1, "-")] == -2.5
    assert by_level[(2, "+")] == 3.5
    assert by_level[(2, "-")] == -3.5


def test_degeneracies() -> None:
    """Degeneracies per sign are k=0 -> 2, k=1 -> 6, k=2 -> 12."""
    spectrum = analytic_dirac_spectrum_s3(k_max=2, radius=1.0)
    positive = {entry["k"]: entry["degeneracy"] for entry in spectrum if entry["sign"] == "+"}

    assert positive[0] == 2
    assert positive[1] == 6
    assert positive[2] == 12


def test_radius_scaling() -> None:
    """Dirac eigenvalues scale as 1/R when the sphere radius changes."""
    spectrum_r1 = analytic_dirac_spectrum_s3(k_max=2, radius=1.0)
    spectrum_r2 = analytic_dirac_spectrum_s3(k_max=2, radius=2.0)

    for entry_r1, entry_r2 in zip(spectrum_r1, spectrum_r2):
        assert abs(entry_r1["eigenvalue"] / 2.0 - entry_r2["eigenvalue"]) < 1e-12


def test_total_modes() -> None:
    """For k_max=2 the total counted modes are (2+6+12)*2 = 40."""
    assert total_number_of_modes(2) == 40
