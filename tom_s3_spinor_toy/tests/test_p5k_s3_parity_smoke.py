"""Tests for the S3 parity smoke candidates."""

from __future__ import annotations

import numpy as np

from s3_parity_smoke import (
    evaluate_parity_candidate,
    parity_radius_preserved,
    parity_smoke_summary,
)
from s3_pauli_clifford_explicit import parity_candidate_p1, parity_candidate_p2


def test_parity_candidate_preserves_radius() -> None:
    """Both smoke candidates should preserve the Lawrence radius."""

    alpha = 0.47
    theta = 1.11
    theta_tilde = 0.73

    assert parity_radius_preserved(parity_candidate_p1, alpha, theta, theta_tilde)
    assert parity_radius_preserved(parity_candidate_p2, alpha, theta, theta_tilde)


def test_parity_smoke_constant_coefficients_on_standard_basis() -> None:
    """The standard basis does not stably close with constant coefficients for these smoke candidates."""

    alpha_grid = np.linspace(0.0, np.pi / 2.0, 15)
    p1 = evaluate_parity_candidate("P1", parity_candidate_p1, alpha_grid)
    p2 = evaluate_parity_candidate("P2", parity_candidate_p2, alpha_grid)

    assert p1.status == "inconclusive"
    assert p1.max_coefficient_variation > 1e-12
    assert p2.status == "passed"
    assert p2.max_coefficient_variation < 1e-12


def test_parity_smoke_summary_records_status_and_fence() -> None:
    """The summary should expose the smoke-only fence and candidate results."""

    summary = parity_smoke_summary()

    assert summary["status"] == "started"
    assert summary["runtime_status"] == "research_only"
    assert summary["v_selection_status"] == "smoke_only"
    assert summary["safe_for_runtime"] is False
    assert set(summary["results"]) == {"P1", "P2"}
    assert summary["results"]["P1"].status == "inconclusive"
    assert summary["results"]["P2"].status == "passed"
