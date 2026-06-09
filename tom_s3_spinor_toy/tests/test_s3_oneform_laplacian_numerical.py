"""Tests for the safe S3 one-form numerical norm diagnostic.

These tests do not validate a kNN connection Laplacian. They verify only the
Haar/Muller norm and Hermitian Gram-matrix diagnostic.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent))

from s3_oneform_laplacian_numerical import compute_e_coframe_norm_numerical


def test_smoke_returns_nonempty_diagnostic_spectrum() -> None:
    """Fast smoke test: diagnostic Gram spectrum is present."""
    result = compute_e_coframe_norm_numerical(n_points=200, k_neighbors=20)

    assert result["graph_laplacian_status"] == "not_implemented_by_design"
    assert len(result["diagnostic_spectrum"]) == 3
    assert np.all(np.isfinite(result["diagnostic_spectrum"]))


def test_scale_to_direct_haar_convention_is_close() -> None:
    """The raw unit coframe maps to the exact direct Haar convention."""
    result = compute_e_coframe_norm_numerical(n_points=2000, k_neighbors=20)

    np.testing.assert_allclose(result["raw_component_norm_mean"], 1.0, rtol=0.2)
    np.testing.assert_allclose(
        result["scale_to_direct_haar_norm"],
        1.0,
        rtol=0.2,
    )


def test_diagnostic_operator_is_hermitian() -> None:
    """The averaged Gram diagnostic is Hermitian/symmetric."""
    result = compute_e_coframe_norm_numerical(n_points=500, k_neighbors=20)
    gram = result["gram_matrix"]

    assert result["operator_hermitian"] is True
    assert np.allclose(gram, gram.T.conjugate())
