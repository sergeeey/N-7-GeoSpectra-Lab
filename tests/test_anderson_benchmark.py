import numpy as np

from cc_toy_lab.spectral.anderson import (
    _central_eigensystem,
    build_anderson_hamiltonian,
    run_anderson_sweep,
)
from cc_toy_lab.spectral.metrics import inverse_participation_ratio, mean_adjacent_gap_ratio


def test_anderson_matrix_is_symmetric():
    h = build_anderson_hamiltonian(size=64, disorder=2.0, seed=7)
    dense = h.toarray()
    assert np.allclose(dense, dense.T)


def test_anderson_reproducible_seed():
    h1 = build_anderson_hamiltonian(size=32, disorder=4.0, seed=42).toarray()
    h2 = build_anderson_hamiltonian(size=32, disorder=4.0, seed=42).toarray()
    assert np.allclose(h1, h2)


def test_anderson_ipr_increases_with_strong_disorder_smoke():
    result = run_anderson_sweep(
        sizes=[96],
        disorder_values=[0.5, 30.0],
        realizations=4,
        seed=12,
        window_fraction=0.5,
    )
    low = result.by_size[96][0]
    high = result.by_size[96][1]
    assert high.mean_ipr > low.mean_ipr


def test_central_eigensystem_window_size_scales_smoothly_across_solver_switch():
    """Regression test for the dense/sparse window-size bug.

    Before the fix, the window's half-width was derived from
    ``values[-1] - values[0]`` of whichever eigenvalues had already been
    computed -- the full spectrum for the dense path (size<=192), but only
    the truncated `k`-nearest-zero eigenvalues for the sparse path. That
    made `window_fraction` apply to two different ranges, so the number of
    eigenvalues captured jumped 2-4x right at the size=192 solver switch
    instead of scaling smoothly with size. See
    reports/TRACK_A_NUMERICAL_AUDIT_2026-07-17.md.
    """
    disorder, seed = 20.0, 3
    window_counts = {}
    for size in (150, 192, 193, 260):
        h = build_anderson_hamiltonian(size=size, disorder=disorder, seed=seed)
        values, _ = _central_eigensystem(h)
        window_counts[size] = len(values)

    # Population should scale roughly with size, not jump discontinuously
    # at the size=192 dense/sparse solver boundary.
    ratio_193_to_192 = window_counts[193] / window_counts[192]
    assert 0.7 < ratio_193_to_192 < 1.4, (
        f"window size jumped discontinuously across the solver switch: "
        f"{window_counts[192]} (size=192, dense) vs {window_counts[193]} "
        f"(size=193, sparse), ratio={ratio_193_to_192:.2f}"
    )
    # Sanity: window population should grow monotonically-ish with size.
    assert window_counts[260] > window_counts[150]


def test_central_eigensystem_dense_sparse_statistics_agree_near_switch():
    """r-statistic and IPR should not differ beyond realization noise when
    the same physical setup crosses the size=192 solver boundary."""
    disorder = 4.0
    r_values, ipr_values = [], []
    for size in (188, 196):  # symmetric straddle of the size<=192 switch
        h = build_anderson_hamiltonian(size=size, disorder=disorder, seed=11)
        values, vectors = _central_eigensystem(h)
        r_values.append(mean_adjacent_gap_ratio(values))
        ipr_values.append(float(np.mean(inverse_participation_ratio(vectors))))

    assert abs(r_values[0] - r_values[1]) < 0.15
    assert abs(ipr_values[0] - ipr_values[1]) < 0.05
