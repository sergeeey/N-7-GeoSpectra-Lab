"""P1b diagonal spectral Dirac operator prototype for round S3.

Scope:
    This module builds the clean Dirac operator in its exact spectral branch
    basis. The matrix is diagonal because the basis is already the eigenbasis.

    This is not a point-cloud/kNN graph operator, not a finite-difference
    operator, not a gauge-field operator, not an instanton calculation, and not
    an index or zero-mode claim.
"""

from __future__ import annotations

import numpy as np
from scipy.sparse import csr_matrix, diags

from s3_spinor_spectral_labels import generate_spectral_spinor_records


def build_dirac_matrix(
    k_max: int,
    radius: float = 1.0,
    convention: str = "ben_achour_displayed_phase",
) -> csr_matrix:
    """Build the clean round-S3 Dirac matrix in the spectral eigenbasis.

    The diagonal entries are generated from P1a spectral branch records. Each
    branch eigenvalue is repeated according to its representation degeneracy.
    """
    diagonal_entries: list[float] = []
    for record in generate_spectral_spinor_records(
        k_max=k_max,
        radius=radius,
        convention=convention,
    ):
        diagonal_entries.extend(
            [record["eigenvalue"]] * record["degeneracy_per_branch"]
        )

    diagonal = np.array(diagonal_entries, dtype=float)
    return diags(diagonal, offsets=0, format="csr")
