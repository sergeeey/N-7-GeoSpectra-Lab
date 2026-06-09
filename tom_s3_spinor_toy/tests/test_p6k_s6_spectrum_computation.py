"""Tests for the analytic S6 Dirac spectrum computation layer."""

from __future__ import annotations

from s6_g2_su3_spectrum_computation import (
    analytic_dirac_spectrum_s6,
    s6_spectrum_computation_summary,
    total_number_of_modes_s6,
)


def test_s6_spectrum_is_symmetric() -> None:
    """For each positive level there is a negative level with the same degeneracy."""

    spectrum = analytic_dirac_spectrum_s6(k_max=4, radius=1.0)
    positive = {entry["k"]: entry["degeneracy"] for entry in spectrum if entry["sign"] == "+"}
    negative = {entry["k"]: entry["degeneracy"] for entry in spectrum if entry["sign"] == "-"}

    assert positive == negative


def test_s6_no_zero_eigenvalue() -> None:
    """The clean round S6 Dirac spectrum has no zero eigenvalues."""

    spectrum = analytic_dirac_spectrum_s6(k_max=4, radius=1.0)
    assert all(abs(entry["eigenvalue"]) > 1e-12 for entry in spectrum)


def test_s6_first_levels() -> None:
    """The first three levels for R=1 are +/-3, +/-4, +/-5."""

    spectrum = analytic_dirac_spectrum_s6(k_max=2, radius=1.0)
    by_level = {(entry["k"], entry["sign"]): entry["eigenvalue"] for entry in spectrum}

    assert by_level[(0, "+")] == 3.0
    assert by_level[(0, "-")] == -3.0
    assert by_level[(1, "+")] == 4.0
    assert by_level[(1, "-")] == -4.0
    assert by_level[(2, "+")] == 5.0
    assert by_level[(2, "-")] == -5.0


def test_s6_degeneracies() -> None:
    """Degeneracies per sign start at 8, 48, 168 for k=0,1,2."""

    spectrum = analytic_dirac_spectrum_s6(k_max=2, radius=1.0)
    positive = {entry["k"]: entry["degeneracy"] for entry in spectrum if entry["sign"] == "+"}

    assert positive[0] == 8
    assert positive[1] == 48
    assert positive[2] == 168


def test_s6_radius_scaling() -> None:
    """Dirac eigenvalues scale as 1/R when the sphere radius changes."""

    spectrum_r1 = analytic_dirac_spectrum_s6(k_max=2, radius=1.0)
    spectrum_r2 = analytic_dirac_spectrum_s6(k_max=2, radius=2.0)

    for entry_r1, entry_r2 in zip(spectrum_r1, spectrum_r2):
        assert abs(entry_r1["eigenvalue"] / 2.0 - entry_r2["eigenvalue"]) < 1e-12


def test_s6_total_modes() -> None:
    """For k_max=2 the total counted modes are (8 + 48 + 168) * 2 = 448."""

    assert total_number_of_modes_s6(2) == 448


def test_s6_summary_records_the_convention() -> None:
    """The summary should expose the fixed geometry and spectrum target."""

    summary = s6_spectrum_computation_summary(k_max=1, radius=1.0)

    assert summary["status"] == "started"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False
    assert summary["identity"] == "S6 ≅ G2 / SU(3)"
    assert summary["reductive_split"] == "g2 = su(3) ⊕ m"
    assert summary["metric_normalization"] == "unit round S6 normalization"
    assert summary["spectrum_target"] == "homogeneous Dirac spectrum on S6, derived as the round-sphere baseline"
    assert summary["total_number_of_modes"] == 112
