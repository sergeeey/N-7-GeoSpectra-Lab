import os
import subprocess
import sys
from pathlib import Path

import numpy as np

from scipy.sparse.linalg import eigsh

from cc_toy_lab.spectral.anderson_3d import (
    Anderson3DConfig,
    build_anderson_3d_hamiltonian,
    central_eigensystem,
    run_anderson_3d_benchmark,
)
from cc_toy_lab.spectral.metrics import inverse_participation_ratio, mean_adjacent_gap_ratio


def test_anderson_3d_matrix_is_symmetric_and_right_size():
    hamiltonian = build_anderson_3d_hamiltonian(lattice_size=4, disorder=3.0, seed=7)
    dense = hamiltonian.toarray()
    assert dense.shape == (64, 64)
    assert np.allclose(dense, dense.T)


def test_anderson_3d_seed_is_reproducible():
    h1 = build_anderson_3d_hamiltonian(lattice_size=4, disorder=5.0, seed=11).toarray()
    h2 = build_anderson_3d_hamiltonian(lattice_size=4, disorder=5.0, seed=11).toarray()
    assert np.allclose(h1, h2)


def test_anderson_3d_ipr_increases_with_strong_disorder(tmp_path: Path):
    config = Anderson3DConfig(
        lattice_sizes=(4,),
        disorder_values=(4.0, 24.0),
        realizations=2,
        seed=5,
        eigen_count=24,
    )
    result = run_anderson_3d_benchmark(config=config, output_dir=tmp_path)
    points = result.by_size[4]
    assert points[-1].mean_ipr > points[0].mean_ipr
    assert (tmp_path / "metrics.json").exists()
    assert (tmp_path / "figures" / "anderson_3d_r_statistics.png").exists()
    assert (tmp_path / "figures" / "anderson_3d_ipr.png").exists()


def test_anderson_3d_reports_finite_values(tmp_path: Path):
    config = Anderson3DConfig(
        lattice_sizes=(4,),
        disorder_values=(4.0, 12.0),
        realizations=2,
        seed=9,
        eigen_count=24,
    )
    result = run_anderson_3d_benchmark(config=config, output_dir=tmp_path)
    for point in result.by_size[4]:
        assert np.isfinite(point.mean_r)
        assert np.isfinite(point.mean_ipr)
        assert point.realizations == 2


def test_central_eigensystem_dense_sparse_select_same_eigenvalues_near_switch():
    """Regression test for the dense/sparse eigenvalue-selection mismatch.

    Before the fix, the dense path (size<=260) selected eigenvalues nearest
    the spectrum's INDEX center while the sparse path (size>260) selected
    eigenvalues nearest VALUE 0 via shift-invert. These only coincide when
    the spectrum is exactly symmetric; on-site disorder breaks that
    symmetry, so the two paths could select different (though overlapping,
    62-96% in testing) eigenvalue sets right at the solver switch. See
    reports/TRACK_A_NUMERICAL_AUDIT_2026-07-17.md, Finding 2.

    L=7 (343 sites) is the project's own "final-size" 3D Anderson lattice
    (reports/NULL_RESULTS.md) and sits just above the size<=260 threshold.
    """
    eigen_count = 48
    for disorder, seed in [(4.0, 1), (24.0, 3), (24.0, 4)]:
        h = build_anderson_3d_hamiltonian(lattice_size=7, disorder=disorder, seed=seed)

        # Forced dense path, using the post-fix selection criterion directly.
        dense_values, dense_vectors = np.linalg.eigh(h.toarray())
        nearest_zero = np.argsort(np.abs(dense_values))[:eigen_count]
        dense_order = nearest_zero[np.argsort(dense_values[nearest_zero])]
        dense_values, dense_vectors = dense_values[dense_order], dense_vectors[:, dense_order]

        # Forced sparse path (same as central_eigensystem's size>260 branch).
        sparse_values, sparse_vectors = eigsh(h, k=eigen_count, sigma=0.0, which="LM")
        sparse_order = np.argsort(sparse_values)
        sparse_values, sparse_vectors = (
            sparse_values[sparse_order],
            sparse_vectors[:, sparse_order],
        )

        overlap = len(set(np.round(dense_values, 6)) & set(np.round(sparse_values, 6)))
        assert overlap == eigen_count, (
            f"dense and sparse selected different eigenvalue sets: "
            f"{overlap}/{eigen_count} shared (disorder={disorder}, seed={seed})"
        )
        r_dense = mean_adjacent_gap_ratio(dense_values)
        r_sparse = mean_adjacent_gap_ratio(sparse_values)
        ipr_dense = np.mean(inverse_participation_ratio(dense_vectors))
        ipr_sparse = np.mean(inverse_participation_ratio(sparse_vectors))
        assert abs(r_dense - r_sparse) < 1e-6
        assert abs(ipr_dense - ipr_sparse) < 1e-6


def test_central_eigensystem_selects_nearest_zero_not_index_center():
    """central_eigensystem's dense branch must pick eigenvalues by |value|,
    not by index position -- the two only agree for a symmetric spectrum."""
    h = build_anderson_3d_hamiltonian(
        lattice_size=4, disorder=20.0, seed=2
    )  # 64 sites, dense branch
    values, _ = central_eigensystem(h, eigen_count=16)
    all_values = np.linalg.eigh(h.toarray())[0]
    expected = np.sort(all_values[np.argsort(np.abs(all_values))[:16]])
    assert np.allclose(np.sort(values), expected)


def test_anderson_3d_cli_quick_smoke():
    env = dict(os.environ, CC_TOY_LAB_SKIP_REPORT_UPDATE="1")
    result = subprocess.run(
        [sys.executable, "scripts/anderson_3d_benchmark.py", "--quick"],
        check=False,
        capture_output=True,
        text=True,
        env=env,
    )
    assert result.returncode == 0
    assert "anderson_3d_benchmark_quick" in result.stdout
