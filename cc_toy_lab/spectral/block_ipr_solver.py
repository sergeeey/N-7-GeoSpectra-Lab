"""Block-diagonal eigensolver for S³×S¹ product operators (v0.1.25).

WHY THIS EXISTS:
The S³×S¹ product operator (ring / wilson_ring / spectral_circle families) is
EXACTLY block-diagonal in the S³ index: it decomposes into s3_dimension(j_max)
independent S¹ chains of size s1_size (verified: 110 blocks of size s1 for
j_max=3). Each row has only ~3 nonzeros (diagonal + 2 S¹ ring neighbours).

This lets us replace dense `eigh` (O(N³), OOM at s1≥256) with per-block dense
diagonalization (110 × eigh(s1)), which is:
  - EXACT: reproduces dense-eigh IPR and r_stat to machine precision (1e-16)
  - FAST: ~88× speedup at s1=64 (0.71s vs 62s)
  - LOW-MEMORY for the eigendecomposition (no N×N workspace)

WHY NOT sparse eigsh:
Benchmarked `eigsh(which='SA', k=N//10)` at s1=64: returned WRONG IPR
(0.036 vs true 0.296) due to non-convergence for 10% of eigenpairs, AND was
6× SLOWER than dense (399s vs 62s). ARPACK is unsuited to "bottom 10%" — that
is too large a fraction. The block structure is the correct exploit.

REMAINING BOTTLENECK:
`build_s3_s1_product_operator` returns a DENSE N×N array. The block solver
removes the eigh OOM but not the operator-construction memory:
  - s1=256: dense op 12.7 GB → feasible on 32 GB
  - s1=512: dense op 50.8 GB → requires sparse operator CONSTRUCTION (future work)

VALIDITY:
Block decomposition is exact ONLY if the operator is genuinely block-diagonal.
This solver ASSERTS the block structure at runtime and raises if violated, so it
can never silently return a wrong answer on a non-block operator.

References:
- reports/DIMENSION_DISCREPANCY_AUDIT_v0.1.25.md
- reports/GATE5_FSS_PREREGISTRATION_v0.1.25.md
"""

from __future__ import annotations

import numpy as np
from scipy.linalg import eigh
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

from cc_toy_lab.spectral.metrics import mean_adjacent_gap_ratio, inverse_participation_ratio


def block_diagonalize(operator: np.ndarray, *, tol: float = 1e-12) -> list[np.ndarray]:
    """Return the list of index arrays for each independent block.

    Blocks are connected components of the operator's nonzero pattern.
    """
    pattern = csr_matrix(np.abs(operator) > tol)
    n_blocks, labels = connected_components(pattern, directed=False)
    return [np.where(labels == b)[0] for b in range(n_blocks)]


def solve_block_ipr_rstat(
    operator: np.ndarray,
    *,
    low_fraction: float = 0.10,
    require_uniform_blocks: bool = True,
    tol: float = 1e-12,
) -> dict:
    """Exact bottom-fraction IPR + r-statistic via per-block diagonalization.

    Reproduces dense `eigh` results to machine precision for block-diagonal
    operators, at ~88× speedup and without the O(N²) eigh workspace.

    Args:
        operator: Hermitian operator (dense ndarray). MUST be block-diagonal
            in its nonzero pattern (asserted).
        low_fraction: fraction of lowest eigenstates for IPR mean (Gate 4B: 0.10).
        require_uniform_blocks: if True, assert all blocks have equal size
            (sanity check for the S³×S¹ structure: s3_dim blocks of size s1).
        tol: nonzero threshold for block detection.

    Returns:
        dict with: true_ipr_mean, r_stat, N, n_blocks, block_size, n_low

    Raises:
        ValueError: if the operator is NOT block-diagonal (single block = dense),
            or blocks are non-uniform when require_uniform_blocks is set.
    """
    N = operator.shape[0]
    blocks = block_diagonalize(operator, tol=tol)
    n_blocks = len(blocks)

    if n_blocks < 2:
        raise ValueError(
            "Operator is NOT block-diagonal (single connected component) — "
            "block solver invalid; use dense eigh instead."
        )

    block_sizes = {len(b) for b in blocks}
    if require_uniform_blocks and len(block_sizes) != 1:
        raise ValueError(
            f"Non-uniform block sizes {sorted(block_sizes)} — expected uniform "
            f"S³×S¹ structure. Set require_uniform_blocks=False to override."
        )

    all_eigvals: list[np.ndarray] = []
    all_iprs: list[np.ndarray] = []

    for idx in blocks:
        sub = operator[np.ix_(idx, idx)]
        evals, evecs = eigh(sub)
        # IPR per eigenvector is invariant to embedding in the full space
        # (zero components outside the block contribute nothing to Σ|ψ|⁴ or Σ|ψ|²).
        iprs = inverse_participation_ratio(evecs)
        all_eigvals.append(evals)
        all_iprs.append(iprs)

    eigvals = np.concatenate(all_eigvals)
    iprs = np.concatenate(all_iprs)

    # Bottom-fraction selection is GLOBAL across all blocks.
    n_low = max(1, int(low_fraction * N))
    order = np.argsort(eigvals)
    low_order = order[:n_low]
    true_ipr_mean = float(np.mean(iprs[low_order]))

    # r-statistic uses the full combined spectrum (identical multiset to dense eigh
    # because block-diagonal eigenvalues are the union of block eigenvalues).
    r_stat = float(mean_adjacent_gap_ratio(np.sort(eigvals)))

    return {
        "true_ipr_mean": true_ipr_mean,
        "r_stat": r_stat,
        "N": N,
        "n_blocks": n_blocks,
        "block_size": next(iter(block_sizes)),
        "n_low": n_low,
    }
