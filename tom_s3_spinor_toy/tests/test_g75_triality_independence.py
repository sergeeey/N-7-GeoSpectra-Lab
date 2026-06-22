"""G75 — Triality Channel Independence (pytest wrapper).

Tests that the three SO(8) triality channels 8_v, 8_s, 8_c contribute
independent zero modes: distinct Z₃-eigenspaces → orthogonal zero modes.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "experiments" / "20260622-g75-triality-independence"),
)

from g75_triality import (
    test_G75_G1_z3_unitary,
    test_G75_G2_eigenvalues_distinct,
    test_G75_G3_zero_mode_orthogonality,
    test_G75_G4_character_orthogonality,
    test_G75_G5_ngen_count,
)


@pytest.mark.parametrize(
    "gate_fn, gate_id",
    [
        (test_G75_G1_z3_unitary, "G75-G1"),
        (test_G75_G2_eigenvalues_distinct, "G75-G2"),
        (test_G75_G3_zero_mode_orthogonality, "G75-G3"),
        (test_G75_G4_character_orthogonality, "G75-G4"),
        (test_G75_G5_ngen_count, "G75-G5"),
    ],
)
def test_g75_gate(gate_fn, gate_id: str) -> None:
    """Each G75 gate must return PASS."""
    result = gate_fn()
    assert result["verdict"] == "PASS", f"{gate_id} FAIL: {result}"


def test_g75_cross_gate_n_channels() -> None:
    """G75 N_gen=3 agrees with G73 N_TRIALITY_CHANNELS constant."""
    from g75_triality import test_G75_G5_ngen_count

    r = test_G75_G5_ngen_count()
    assert r["n_channels"] == 3, "G75 must use 3 channels (matches G73.N_TRIALITY_CHANNELS)"
    assert r["n_gen"] == 3, "G75 N_gen must be 3"
    assert r["n_independent_eigenspaces"] == 3, "All 3 Z3 eigenspaces must be distinct"
