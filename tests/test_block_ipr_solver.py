"""Dense-vs-block equivalence tests for the block IPR/r-stat solver (v0.1.25).

Verifies that solve_block_ipr_rstat reproduces full dense `eigh` results to
machine precision on the S³×S¹ product operator, which is exactly block-diagonal
in the S³ index. These are the committed, reproducible counterpart of the
in-session verification recorded in reports/BLOCK_SOLVER_VERIFICATION_v0.1.25.md.

Sizes are kept small (s1 ≤ 32) so dense eigh is feasible and the whole module
runs in well under 30 seconds. No large lattices, no experiment --run.
"""

from __future__ import annotations

import numpy as np
import pytest
from scipy.linalg import eigh

from cc_toy_lab.spectral.s3_s1_product_discretized import build_s3_s1_product_operator
from cc_toy_lab.spectral.metrics import mean_adjacent_gap_ratio, inverse_participation_ratio
from cc_toy_lab.spectral.block_ipr_solver import (
    solve_block_ipr_rstat,
    block_diagonalize,
)

TOL = 1e-10  # required agreement (observed ~1e-14)


def _dense_reference(op: np.ndarray, low_fraction: float = 0.10) -> tuple[float, float]:
    """Bottom-fraction mean IPR + r-stat via full dense eigh (reference)."""
    N = op.shape[0]
    n_low = max(1, int(low_fraction * N))
    eigvals, eigvecs = eigh(op)
    idx = np.argsort(eigvals)[:n_low]
    ipr = float(np.mean(inverse_participation_ratio(eigvecs[:, idx])))
    r_stat = float(mean_adjacent_gap_ratio(np.sort(eigvals)))
    return ipr, r_stat


def _build(family: str, s1_size: int, W: float, seed: int = 123) -> np.ndarray:
    op, _, _ = build_s3_s1_product_operator(
        j_max=3,
        s1_size=s1_size,
        alpha=0.0,
        mode="clean" if W == 0 else "geometric_weight",
        disorder_strength=W,
        seed=seed,
        radius=1.0,
        s1_family=family,
    )
    return op


# Minimum required coverage: ring/wilson_ring × W=0/20, plus one larger-s1 sanity.
CASES = [
    ("ring", 16, 0.0),
    ("ring", 16, 20.0),
    ("wilson_ring", 16, 0.0),
    ("wilson_ring", 16, 20.0),
    ("ring", 32, 20.0),
    ("wilson_ring", 32, 20.0),
]


@pytest.mark.parametrize("family,s1_size,W", CASES)
def test_block_matches_dense_ipr_and_rstat(family, s1_size, W):
    op = _build(family, s1_size, W)
    ipr_dense, r_dense = _dense_reference(op)
    res = solve_block_ipr_rstat(op, low_fraction=0.10)

    assert abs(res["true_ipr_mean"] - ipr_dense) < TOL, (
        f"{family} s1={s1_size} W={W}: IPR block={res['true_ipr_mean']} "
        f"vs dense={ipr_dense}"
    )
    assert abs(res["r_stat"] - r_dense) < TOL, (
        f"{family} s1={s1_size} W={W}: r_stat block={res['r_stat']} "
        f"vs dense={r_dense}"
    )


def test_operator_is_block_diagonal():
    """S³×S¹ ring operator must decompose into uniform S³-index blocks."""
    op = _build("ring", 16, 20.0)
    blocks = block_diagonalize(op)
    assert len(blocks) > 1, "expected multiple S³ blocks (not a single dense block)"
    sizes = {len(b) for b in blocks}
    assert sizes == {16}, f"expected all blocks of size s1=16, got {sorted(sizes)}"


def test_block_solver_rejects_non_block_diagonal():
    """A dense (single-component) operator must raise, not silently mis-solve."""
    rng = np.random.default_rng(0)
    dense = rng.standard_normal((12, 12)) + 1j * rng.standard_normal((12, 12))
    dense = dense + dense.conj().T  # Hermitian, fully connected
    with pytest.raises(ValueError):
        solve_block_ipr_rstat(dense)
