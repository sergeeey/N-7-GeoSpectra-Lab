"""Tests for the P1a spectral spinor label scaffold on S3.

This scaffold only labels the exact spectral branches. It does not construct a
Dirac matrix, spinor wavefunctions, gauge fields, instantons, or graph data.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from s3_dirac_exact_baseline import analytic_dirac_spectrum_s3
from s3_spinor_spectral_labels import generate_spectral_spinor_records


def test_consistency_with_p0_exact_baseline() -> None:
    """P1a records agree with the P0 exact eigenvalues and degeneracies."""
    records = generate_spectral_spinor_records(k_max=3, radius=1.0)
    baseline = analytic_dirac_spectrum_s3(k_max=3, radius=1.0)

    by_level = {
        (entry["k"], "positive" if entry["sign"] == "+" else "negative"): entry
        for entry in baseline
    }

    assert len(records) == len(baseline)
    for record in records:
        expected = by_level[(record["k"], record["branch"])]
        assert record["eigenvalue"] == expected["eigenvalue"]
        assert record["degeneracy_per_branch"] == expected["degeneracy"]


def test_convention_is_explicit() -> None:
    """Every emitted record carries the selected convention metadata."""
    records = generate_spectral_spinor_records(k_max=2)

    assert records
    assert all(record["convention"] == "ben_achour_displayed_phase" for record in records)
    assert all("not a Dirac matrix" in record["note"] for record in records)


def test_no_zero_eigenvalue() -> None:
    """Clean round S3 spectral records have no zero eigenvalues."""
    records = generate_spectral_spinor_records(k_max=5)

    assert all(abs(record["eigenvalue"]) > 1e-12 for record in records)


def test_branch_symmetry() -> None:
    """Each positive branch has a matching negative branch with the same degeneracy."""
    records = generate_spectral_spinor_records(k_max=4)
    positive = {record["k"]: record for record in records if record["branch"] == "positive"}
    negative = {record["k"]: record for record in records if record["branch"] == "negative"}

    assert positive.keys() == negative.keys()
    for k in positive:
        assert positive[k]["eigenvalue"] == -negative[k]["eigenvalue"]
        assert positive[k]["degeneracy_per_branch"] == negative[k]["degeneracy_per_branch"]


def test_su2_labels_reproduce_branch_degeneracy() -> None:
    """The SU(2)_L x SU(2)_R labels reproduce (k+1)(k+2) per branch."""
    records = generate_spectral_spinor_records(k_max=4)

    for record in records:
        j_left = record["su2_L_label"]["j"]
        j_right = record["su2_R_label"]["j"]
        representation_dimension = int((2 * j_left + 1) * (2 * j_right + 1))

        assert representation_dimension == record["degeneracy_per_branch"]
