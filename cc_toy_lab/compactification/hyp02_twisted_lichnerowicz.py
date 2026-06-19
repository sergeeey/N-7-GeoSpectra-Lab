"""HYP_02 — twisted Lichnerowicz / transversality eigenvalue toy on P13B1 modes."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal

import numpy as np

from cc_toy_lab.compactification.p13b1_basis import ConventionId, load_modes, normalize_spinor
from cc_toy_lab.compactification.p13h_integral import matrix_element
from cc_toy_lab.compactification.s3_lawrence_hopf import volume_weight

HypothesisStatus = Literal[
    "hypothesis_supported",
    "hypothesis_killed",
    "inconclusive",
]


@dataclass(frozen=True)
class Hyp02Report:
    hypothesis_id: str
    convention: ConventionId
    kernel_dimension: int
    admissible_eigenvalues: tuple[float, ...]
    status: HypothesisStatus
    falsifier_triggered: bool
    message: str


def _integration_grid(n: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    alpha = np.linspace(1e-3, 0.5 * np.pi - 1e-3, n)
    theta = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    theta_tilde = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    return alpha, theta, theta_tilde


def _cell_weights(alpha: np.ndarray, theta: np.ndarray, theta_tilde: np.ndarray) -> np.ndarray:
    aa, tt, ttt = np.meshgrid(alpha, theta, theta_tilde, indexing="ij")
    alpha_f = aa.ravel()
    dalpha = (0.5 * np.pi) / max(alpha.size - 1, 1)
    dtheta = (2.0 * np.pi) / theta.size
    dtheta_tilde = (2.0 * np.pi) / theta_tilde.size
    return volume_weight(alpha_f) * dalpha * dtheta * dtheta_tilde


def overlap_matrix(
    convention: ConventionId,
    *,
    grid_n: int = 16,
) -> np.ndarray:
    modes = load_modes()
    alpha, theta, theta_tilde = _integration_grid(grid_n)
    aa, tt, ttt = np.meshgrid(alpha, theta, theta_tilde, indexing="ij")
    alpha_f = aa.ravel()
    theta_f = tt.ravel()
    theta_tilde_f = ttt.ravel()
    weight = _cell_weights(alpha, theta, theta_tilde)

    fields: list[np.ndarray] = []
    for mode in modes:
        psi, _ = normalize_spinor(mode, alpha_f, theta_f, theta_tilde_f, convention)
        fields.append(psi)

    n = len(fields)
    g = np.zeros((n, n), dtype=complex)
    for i in range(n):
        for j in range(n):
            acc = 0.0 + 0.0j
            for p in range(alpha_f.size):
                acc += np.vdot(fields[i][:, p], fields[j][:, p]) * weight[p]
            g[i, j] = acc
    return g


def v_coefficient_matrix(
    convention: ConventionId,
    *,
    grid_n: int = 16,
) -> np.ndarray:
    modes = load_modes()
    n = len(modes)
    c = np.zeros((n, n), dtype=complex)
    for i in range(n):
        for j in range(n):
            c[i, j] = matrix_element(i, j, convention, grid_n=grid_n).coefficient
    return c


def transversality_constraints() -> np.ndarray:
    """Toy bundle compatibility: c_0 - c_1 = 0 (1 constraint on 2 modes)."""
    return np.array([[1.0, -1.0]])


def constrained_kernel_dimension(constraint_rows: np.ndarray) -> int:
    """Dimension of admissible coefficient subspace after linear constraints."""
    n_modes = 2
    rank = int(np.linalg.matrix_rank(constraint_rows))
    return max(n_modes - rank, 0)


def projected_generalized_eigenvalues(
    convention: ConventionId,
    *,
    grid_n: int = 16,
) -> tuple[np.ndarray, int]:
    g = overlap_matrix(convention, grid_n=grid_n)
    c = v_coefficient_matrix(convention, grid_n=grid_n)
    b = transversality_constraints()

    # Project to null(B): admissible directions v with B v = 0
    _, _, vh = np.linalg.svd(b)
    rank = int(np.linalg.matrix_rank(b))
    null_dim = g.shape[0] - rank
    if null_dim <= 0:
        return np.array([]), 0
    projector = vh[rank:, :].T.conj()  # columns span null space

    g_red = projector.conj().T @ g @ projector
    c_red = projector.conj().T @ c @ projector
    g_sym = 0.5 * (g_red + g_red.conj().T)
    c_sym = 0.5 * (c_red + c_red.conj().T)

    if g_sym.shape[0] == 1:
        # 1D admissible subspace — single eigenvalue ratio
        denom = float(np.real(projector.conj().T @ g @ projector)[0, 0])
        numer = float(np.real(projector.conj().T @ c @ projector)[0, 0])
        if abs(denom) < 1e-15:
            return np.array([]), null_dim
        return np.array([numer / denom]), null_dim

    eigvals = np.linalg.eigvalsh(np.linalg.solve(g_sym, c_sym).real)
    return np.sort(eigvals.real), null_dim


def run_hyp02_experiment(*, grid_n: int = 16) -> tuple[Hyp02Report, Hyp02Report]:
    """Run for both conventions; kill hypothesis if kernel > 1D or eigenvalue convention-dependent."""
    b = transversality_constraints()
    kernel_dim = constrained_kernel_dimension(b)

    unit_eigs, _ = projected_generalized_eigenvalues("CONV_HAAR_UNIT", grid_n=grid_n)
    sqrt2_eigs, _ = projected_generalized_eigenvalues("CONV_HAAR_HARMONIC_SQRT2", grid_n=grid_n)

    if kernel_dim > 1:
        status: HypothesisStatus = "hypothesis_killed"
        falsifier = True
        msg = f"Constrained kernel dimension {kernel_dim} > 1 — normalization freedom survives."
    elif unit_eigs.size == 0:
        status = "inconclusive"
        falsifier = False
        msg = "No admissible eigenvalue extracted."
    else:
        rel = float(abs(unit_eigs[0] - sqrt2_eigs[0]) / max(abs(unit_eigs[0]), 1e-15))
        if rel > 0.05:
            status = "hypothesis_killed"
            falsifier = True
            msg = (
                "Admissible eigenvalue convention-dependent "
                f"(rel change {rel:.4f}) — normalization not locked."
            )
        else:
            status = "hypothesis_supported"
            falsifier = False
            msg = "Single admissible eigenvalue stable across conventions in toy truncation."

    unit_report = Hyp02Report(
        hypothesis_id="HYP_02_TWISTED_LICHNEROWICZ",
        convention="CONV_HAAR_UNIT",
        kernel_dimension=kernel_dim,
        admissible_eigenvalues=tuple(float(x) for x in unit_eigs),
        status=status,
        falsifier_triggered=falsifier,
        message=msg,
    )
    sqrt2_report = Hyp02Report(
        hypothesis_id="HYP_02_TWISTED_LICHNEROWICZ",
        convention="CONV_HAAR_HARMONIC_SQRT2",
        kernel_dimension=kernel_dim,
        admissible_eigenvalues=tuple(float(x) for x in sqrt2_eigs),
        status=status,
        falsifier_triggered=falsifier,
        message=msg,
    )
    return unit_report, sqrt2_report


def report_to_dict(report: Hyp02Report) -> dict:
    return asdict(report)
