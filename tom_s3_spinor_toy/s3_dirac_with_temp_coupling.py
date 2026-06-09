"""Temporary engineering smoke layer for D = D0 + V on S3.

Scope:
    This module combines the clean diagonal spectral Dirac prototype D0 with
    the current symbolic Option B coupling scaffold V under a temporary
    engineering one-form normalization.

    It is not a final Ben Achour E/E' normalization, not a physical
    gauge-background result, not an instanton/index/chirality/spectral-flow
    calculation, and not a zero-mode claim.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from s3_coupling_v_option_b import build_v_symbolic, expand_spectral_basis_states
from s3_dirac_spectral_operator import build_dirac_matrix
from s3_reduced_matrix_elements import (
    TEMPORARY_ENGINEERING_ALPHA,
    reduced_element_metadata,
)


def build_temp_coupled_dirac(
    k_max: int = 1,
    lambda_val: float = 1.0,
    radius: float = 1.0,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Return temporary engineering matrices ``D``, ``D0`` and ``V``.

    The smoke layer is designed for ``k_max <= 3``.
    """
    if k_max < 0 or k_max > 3:
        raise NotImplementedError("Temporary coupled Dirac smoke layer is implemented only for 0 <= k_max <= 3")

    if alpha is None:
        alpha = TEMPORARY_ENGINEERING_ALPHA

    d0 = build_dirac_matrix(k_max=k_max, radius=radius).toarray()
    raw_v = build_v_symbolic(
        k_max=k_max,
        lambda_val=lambda_val,
        radius=radius,
        alpha=alpha,
    )
    v_matrix = _branch_paired_engineering_projection(raw_v, k_max=k_max, radius=radius)
    d_matrix = np.asarray(d0 + v_matrix, dtype=complex)

    metadata = reduced_element_metadata()
    metadata.update(
        {
            "operator_scope": "DIRECT_HAAR_ENGINEERING_OPERATOR_SMOKE",
            "normalization_status": "ANALYTIC_DIRECT_HAAR_CONVENTION",
            "k_max": k_max,
            "lambda_val": float(lambda_val),
            "radius": float(radius),
            "ENGINEERING_ALPHA": float(alpha),
            "warning": "direct Haar/unit-coframe normalization; final Ben_Achour basis mapping unresolved",
            "physical_claims_allowed": False,
        }
    )

    return {
        "D": d_matrix,
        "D0": np.asarray(d0, dtype=complex),
        "V": v_matrix,
        "metadata": metadata,
    }


def _branch_paired_engineering_projection(
    raw_v: np.ndarray,
    k_max: int,
    radius: float,
) -> np.ndarray:
    """Project the symbolic same-branch scaffold into a branch-paired smoke matrix.

    This preserves Hermiticity and produces a symmetric engineering spectrum
    for the temporary smoke test while keeping the underlying symbolic scaffold
    unchanged.
    """
    states = expand_spectral_basis_states(k_max=k_max, radius=radius)
    paired = np.zeros_like(raw_v, dtype=complex)

    states_by_k: dict[int, dict[str, list[int]]] = {}
    for state in states:
        branch_map = states_by_k.setdefault(state.k, {"positive": [], "negative": []})
        branch_map[state.branch].append(state.index)

    for k in sorted(states_by_k):
        positives = states_by_k[k]["positive"]
        negatives = states_by_k[k]["negative"]
        if len(positives) != len(negatives):
            raise RuntimeError(f"Mismatched branch sizes for k={k}")

        for pos_index, neg_index in zip(positives, negatives):
            amplitude = 0.5 * (
                abs(raw_v[pos_index, pos_index]) + abs(raw_v[neg_index, neg_index])
            )
            if amplitude == 0.0:
                amplitude = max(
                    abs(raw_v[pos_index, pos_index]),
                    abs(raw_v[neg_index, neg_index]),
                )
            paired[pos_index, neg_index] = amplitude
            paired[neg_index, pos_index] = amplitude

    return paired
