"""Minimal symbolic Option B coupling scaffold for k_max up to 3.

Scope:
    This module builds a nonzero Hermitian coefficient scaffold for the future
    homogeneous SU(2) connection term V on S3. It uses Clebsch-Gordan
    selection rules with working analytic reduced matrix elements from SU(2)
    triple-harmonic factors. The current implementation is engineered for
    ``k_max <= 3``.

    It is not a full physical gauge-background operator, not a full matrix
    element implementation for arbitrary k, not a numerical Dirac operator, and
    not an instanton/index/zero-mode calculation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
from sympy import S
from sympy.physics.wigner import clebsch_gordan

from s3_dirac_exact_baseline import total_number_of_modes
from s3_reduced_matrix_elements import (
    TEMPORARY_ENGINEERING_ALPHA,
    compute_reduced_V_element,
)
from s3_spinor_spectral_labels import generate_spectral_spinor_records


@dataclass(frozen=True)
class SpectralBasisState:
    """Expanded magnetic-label state from a P1a branch record."""

    index: int
    k: int
    branch: str
    j_left: float
    m_left: float
    j_right: float
    m_right: float


def _magnetic_labels(j_value: float) -> list[float]:
    count = int(round(2 * j_value)) + 1
    return [-j_value + offset for offset in range(count)]


def expand_spectral_basis_states(k_max: int, radius: float = 1.0) -> list[SpectralBasisState]:
    """Expand P1a records into individual ``m_L,m_R`` spectral states."""
    states: list[SpectralBasisState] = []
    for record in generate_spectral_spinor_records(k_max=k_max, radius=radius):
        j_left = float(record["su2_L_label"]["j"])
        j_right = float(record["su2_R_label"]["j"])
        for m_left in _magnetic_labels(j_left):
            for m_right in _magnetic_labels(j_right):
                states.append(
                    SpectralBasisState(
                        index=len(states),
                        k=int(record["k"]),
                        branch=str(record["branch"]),
                        j_left=j_left,
                        m_left=m_left,
                        j_right=j_right,
                        m_right=m_right,
                    )
                )
    return states


def _as_rational_half(value: float) -> Any:
    return S(int(round(2 * value))) / 2


def _left_invariant_cg_coefficient(
    source: SpectralBasisState,
    target: SpectralBasisState,
) -> complex:
    """Return the working (J_L,J_R)=(1,0) symbolic coefficient.

    This uses Clebsch-Gordan selection rules with the current working reduced
    matrix element. The final Ben Achour E/E' one-form normalization is still
    unresolved and is not encoded in this P1c scaffold.
    """
    if abs(target.j_right - source.j_right) > 1e-12:
        return 0.0 + 0.0j
    if abs(target.m_right - source.m_right) > 1e-12:
        return 0.0 + 0.0j
    if source.j_left == 0.0 and target.j_left == 0.0:
        return 0.0 + 0.0j
    if abs(target.j_left - source.j_left) > 1.0 + 1e-12:
        return 0.0 + 0.0j

    q_left = target.m_left - source.m_left
    if q_left not in {-1.0, 0.0, 1.0}:
        return 0.0 + 0.0j

    coefficient = clebsch_gordan(
        _as_rational_half(source.j_left),
        S(1),
        _as_rational_half(target.j_left),
        _as_rational_half(source.m_left),
        _as_rational_half(q_left),
        _as_rational_half(target.m_left),
    )
    reduced = compute_reduced_V_element(
        j_L=source.j_left,
        j_R=source.j_right,
        j_L_prime=target.j_left,
        j_R_prime=target.j_right,
    )
    return complex(reduced * coefficient.evalf())


def build_v_symbolic(
    k_max: int = 1,
    lambda_val: float = 1.0,
    radius: float = 1.0,
    alpha: float | None = None,
) -> np.ndarray:
    """Build the minimal Hermitian symbolic V scaffold.

    The returned matrix has dimension ``total_number_of_modes(k_max)``. Internal
    gauge-doublet indices are not expanded in this scaffold; the SU(2) gauge
    generator normalization is represented only by a global factor compatible
    with ``T_i = tau_i / 2``. The current reduced elements use working SU(2)
    triple-harmonic normalization, not the final Ben Achour E/E' normalization.
    """
    if k_max < 0 or k_max > 3:
        raise NotImplementedError("Symbolic V scaffold is implemented only for 0 <= k_max <= 3")

    states = expand_spectral_basis_states(k_max=k_max, radius=radius)
    size = total_number_of_modes(k_max)
    if len(states) != size:
        raise RuntimeError(f"Expanded basis size {len(states)} does not match expected {size}")

    raw = np.zeros((size, size), dtype=complex)
    gauge_generator_factor = 0.5
    if alpha is None:
        alpha = TEMPORARY_ENGINEERING_ALPHA
    engineering_scale = float(alpha) / float(TEMPORARY_ENGINEERING_ALPHA)
    scale = float(lambda_val) * gauge_generator_factor * engineering_scale / float(radius)

    for source in states:
        for target in states:
            coefficient = _left_invariant_cg_coefficient(source, target)
            if coefficient != 0.0:
                raw[target.index, source.index] = scale * coefficient

    return (raw + raw.conjugate().T) / 2.0
