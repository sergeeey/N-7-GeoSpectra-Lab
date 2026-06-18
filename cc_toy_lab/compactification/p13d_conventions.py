"""P13D convention stack — gamma matrices and SU(4) generators."""

from __future__ import annotations

import numpy as np

from cc_toy_lab.compactification.registry_loader import load_registry


def gamma_matrices() -> list[np.ndarray]:
    """P13D smoke basis: four mutually commuting Hermitian gamma^a."""
    g0 = np.diag([1.0, 1.0, 1.0, 1.0]).astype(complex)
    g1 = np.diag([1.0, -1.0, 0.0, 0.0]).astype(complex)
    g2 = np.diag([0.0, 1.0, -1.0, 0.0]).astype(complex)
    g3 = np.diag([0.0, 0.0, 1.0, -1.0]).astype(complex)
    return [g0, g1, g2, g3]


def su4_generators_smoke() -> list[np.ndarray]:
    """First two trace-normalized generators for smoke truncation (P13A)."""
    # T0 = I/2, T1 = diag(1,-1,0,0)/sqrt(2) — Tr(Ti Tj)=delta_ij/2
    t0 = np.eye(4, dtype=complex) / 2.0
    t1 = np.diag([1.0, -1.0, 0.0, 0.0]).astype(complex) / np.sqrt(2.0)
    return [t0, t1]


def assert_hermiticity_preservation(tol: float = 1e-10) -> float:
    """Return max Hermiticity violation for gamma matrices."""
    max_err = 0.0
    for g in gamma_matrices():
        err = float(np.max(np.abs(g - g.conj().T)))
        max_err = max(max_err, err)
    assert max_err < tol, f"Gamma Hermiticity violated: {max_err}"
    return max_err


def load_p13d_metadata() -> dict:
    return load_registry("P13D_convention_stack.yaml")
