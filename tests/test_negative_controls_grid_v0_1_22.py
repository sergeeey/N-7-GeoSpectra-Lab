"""Tests for negative controls grid coverage and integrity (v0.1.22).

Grid updated 2026-09-06 to match the documented 2026-06-03 batch redesign
(reports/BATCH_DESIGN_v0.1.22.md): a skeptic audit found the original
54-case pre-registration needed a 4th control (spectral_circle_scrambled)
and s1_size=128 restored (to compare against Gate 4B's strongest finding
point). scripts/run_negative_controls_v0_1_22.py's own PILOT_GRID was
updated accordingly at the time; these tests were not, until now.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.run_negative_controls_v0_1_22 import (
    generate_full_grid,
    split_into_batches,
)


def test_grid_total_cases():
    """Verify pilot grid has exactly 96 cases (4 controls x 2 W x 4 sizes x 1 j_max x 3 seeds,
    per the 2026-06-03 batch redesign, reports/BATCH_DESIGN_v0.1.22.md)."""
    cases = generate_full_grid()
    assert len(cases) == 96, f"Expected 96 cases, got {len(cases)}"


def test_grid_no_duplicates():
    """Verify no duplicate (control, W, size, j_max, seed) combinations."""
    cases = generate_full_grid()

    unique_keys = set()
    for case in cases:
        key = (
            case["control"],
            case["disorder_strength"],
            case["s1_size"],
            case["j_max"],
            case["seed"],
        )
        assert key not in unique_keys, f"Duplicate case detected: {key}"
        unique_keys.add(key)

    assert len(unique_keys) == 96


def test_grid_controls_set():
    """Verify controls set exactly matches protocol (4 controls including
    Control D, spectral_circle_scrambled, added 2026-06-03)."""
    cases = generate_full_grid()
    controls = {c["control"] for c in cases}

    expected_controls = {
        "random_hermitian",
        "scrambled_geometry",
        "broken_wilson_term",
        "spectral_circle_scrambled",
    }
    assert controls == expected_controls, f"Controls mismatch: {controls}"


def test_grid_disorder_values():
    """Verify W set = {0, 20} (skip W=12)."""
    cases = generate_full_grid()
    w_values = {c["disorder_strength"] for c in cases}

    expected_w = {0, 20}
    assert w_values == expected_w, f"W values mismatch: {w_values}"


def test_grid_sizes():
    """Verify s1_size set = {16, 32, 64, 128} (all 4, restored 2026-06-03
    for full FSS coverage per reports/BATCH_DESIGN_v0.1.22.md)."""
    cases = generate_full_grid()
    sizes = {c["s1_size"] for c in cases}

    expected_sizes = {16, 32, 64, 128}
    assert sizes == expected_sizes, f"Sizes mismatch: {sizes}"


def test_grid_j_max():
    """Verify j_max set = {3} (max dimension only)."""
    cases = generate_full_grid()
    j_max_values = {c["j_max"] for c in cases}

    expected_j_max = {3}
    assert j_max_values == expected_j_max, f"j_max mismatch: {j_max_values}"


def test_grid_seeds():
    """Verify seeds = {123, 456, 789}."""
    cases = generate_full_grid()
    seeds = {c["seed"] for c in cases}

    expected_seeds = {123, 456, 789}
    assert seeds == expected_seeds, f"Seeds mismatch: {seeds}"


def test_batch_count():
    """Verify 8 batches (4 controls × 2 W, per the 2026-06-03 redesign)."""
    cases = generate_full_grid()
    batches = split_into_batches(cases)

    assert len(batches) == 8, f"Expected 8 batches, got {len(batches)}"


def test_batch_sizes():
    """Verify each batch has exactly 12 cases (4 sizes x 1 j_max x 3 seeds)."""
    cases = generate_full_grid()
    batches = split_into_batches(cases)

    for batch in batches:
        assert len(batch["cases"]) == 12, (
            f"Batch {batch['batch_id']} has {len(batch['cases'])} cases, expected 12"
        )


def test_batch_coverage():
    """Verify batches cover all 96 cases without overlap."""
    cases = generate_full_grid()
    batches = split_into_batches(cases)

    all_batch_case_ids = []
    for batch in batches:
        all_batch_case_ids.extend([c["id"] for c in batch["cases"]])

    # No duplicates across batches
    assert len(all_batch_case_ids) == len(set(all_batch_case_ids)), "Batch overlap detected"

    # All 96 cases covered
    assert len(all_batch_case_ids) == 96, (
        f"Batches cover {len(all_batch_case_ids)} cases, expected 96"
    )


def test_control_dimension_consistency():
    """Verify all cases with same (j_max, s1_size) have same expected dimension."""
    from cc_toy_lab.spectral.dirac_s3 import s3_dimension

    cases = generate_full_grid()

    # Group by (j_max, s1_size)
    dimension_map = {}
    for case in cases:
        key = (case["j_max"], case["s1_size"])
        expected_dim = s3_dimension(case["j_max"]) * case["s1_size"]

        if key not in dimension_map:
            dimension_map[key] = expected_dim
        else:
            assert dimension_map[key] == expected_dim, (
                f"Dimension mismatch for {key}: {dimension_map[key]} vs {expected_dim}"
            )


def test_alpha_fixed():
    """Verify alpha=0.0 (PBC) for all cases."""
    cases = generate_full_grid()
    alphas = {c["alpha"] for c in cases}

    assert alphas == {0.0}, f"Alpha should be 0.0 for all cases, got {alphas}"


def test_radius_fixed():
    """Verify radius=1.0 for all cases."""
    cases = generate_full_grid()
    radii = {c["radius"] for c in cases}

    assert radii == {1.0}, f"Radius should be 1.0 for all cases, got {radii}"
