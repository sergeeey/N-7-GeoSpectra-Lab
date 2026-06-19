"""G25 tests: Yukawa texture — S³×S⁶ predicts 4 Yukawa parameters."""

import os
import sys

import sympy as sp

_g25_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260619-g25-yukawa-texture"
)
sys.path.insert(0, _g25_dir)

for _p in [
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g18-ncg-dirac-df"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g21-extended-schur"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g17-electric-charge"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g16-t3r-from-k3"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g15-hypercharge"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g11-block-generators"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g10b-su3-in-so6"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260617-g10-s6-so6-gauge"),
]:
    sys.path.insert(0, _p)

from g25_yukawa_texture import (  # noqa: E402
    DECODED_PAIRS,
    MODE_PAIR_COUNT,
    N_CHIRAL_BLOCK,
    N_FINAL,
    N_S6_DIAGONAL,
    N_YUKAWA_PARAMS,
    Q_VALUES,
    S3_HOPF_PAIRINGS,
    SU3_SINGLET_MODES,
    SU3_TRIPLET_MODES,
    YUKAWA_Q_VALUES,
    YUKAWA_SYMBOLS,
    verify_gates,
)
from g18_ncg import Y_nu, Y_e, Y_u, Y_d  # noqa: E402


# ── P1: S⁶-diagonal ───────────────────────────────────────────────────────


def test_all_yukawa_pairs_preserve_s6_mode():
    """S³×S⁶ product: Yukawa connects same S⁶ mode across S³ components."""
    for s3_i, s6_i, s3_j, s6_j, _ in DECODED_PAIRS:
        assert s6_i == s6_j, f"Pair ({s3_i},{s6_i})↔({s3_j},{s6_j}) mixes S⁶ modes"


def test_s6_diagonal_covers_all_modes():
    """Every S⁶ mode 0–7 participates in Yukawa coupling."""
    modes_covered = {s6_i for _, s6_i, _, _, _ in DECODED_PAIRS}
    assert modes_covered == set(range(8))


def test_no_off_diagonal_s6_mixing():
    """D_F has zero off-diagonal S⁶ blocks — pure S⁶-diagonal structure."""
    for s3_i, s6_i, s3_j, s6_j, _ in DECODED_PAIRS:
        assert s6_i == s6_j


# ── P2: S³ Hopf-pairing ───────────────────────────────────────────────────


def test_s3_pairings_are_hopf_adjacent():
    """All Yukawa S³ connections are (0,2) or (1,3) — Hopf adjacency on S³."""
    assert S3_HOPF_PAIRINGS == frozenset([(0, 2), (1, 3)])


def test_no_non_hopf_s3_connections():
    """No Yukawa pair connects S³ components outside {(0,2), (1,3)}."""
    for s3_i, _, s3_j, _, _ in DECODED_PAIRS:
        pair = (min(s3_i, s3_j), max(s3_i, s3_j))
        assert pair in {(0, 2), (1, 3)}, f"Non-Hopf pairing: S³ {s3_i}↔{s3_j}"


def test_both_hopf_pairings_used():
    """Both S³ Hopf pairings (0,2) and (1,3) appear in YUKAWA_PAIRS."""
    pairings_seen = {(min(s3_i, s3_j), max(s3_i, s3_j)) for s3_i, _, s3_j, _, _ in DECODED_PAIRS}
    assert (0, 2) in pairings_seen
    assert (1, 3) in pairings_seen


# ── P3: Mode coverage ─────────────────────────────────────────────────────


def test_every_s6_mode_has_exactly_two_yukawa_pairs():
    """Each S⁶ mode participates in exactly 2 Yukawa pairs (one per Hopf pairing)."""
    for mode, count in MODE_PAIR_COUNT.items():
        assert count == 2, f"S⁶ mode {mode}: {count} pairs (expected 2)"


def test_singlet_modes_are_0_and_7():
    """SU(3) singlet S⁶ modes from Spin(7)→G₂→SU(3) branching are {0,7}."""
    assert SU3_SINGLET_MODES == frozenset([0, 7])


def test_triplet_modes_are_1_to_6():
    """SU(3) triplet+antitriplet S⁶ modes are {1,2,3,4,5,6}."""
    assert SU3_TRIPLET_MODES == frozenset([1, 2, 3, 4, 5, 6])


def test_singlet_plus_triplet_covers_all_modes():
    """SU3_SINGLET + SU3_TRIPLET = all 8 S⁶ modes (no overlap, no gap)."""
    assert SU3_SINGLET_MODES | SU3_TRIPLET_MODES == frozenset(range(8))
    assert SU3_SINGLET_MODES & SU3_TRIPLET_MODES == frozenset()


# ── P4: |Q|-uniqueness ───────────────────────────────────────────────────


def test_coupling_uniquely_determined_by_abs_q():
    """Coupling = f(|Q|): all pairs with same |Q| share the same Yukawa parameter."""
    absq_coupling: dict[sp.Rational, object] = {}
    from g18_ncg import YUKAWA_PAIRS

    for i, j, y in YUKAWA_PAIRS:
        abs_q = abs(Q_VALUES[i])
        if abs_q in absq_coupling:
            assert absq_coupling[abs_q] == y, (
                f"|Q|={abs_q}: couplings {absq_coupling[abs_q]} vs {y} disagree"
            )
        else:
            absq_coupling[abs_q] = y


def test_four_distinct_abs_q_values():
    """|Q| takes exactly 4 values: {0, 1, 2/3, 1/3}."""
    from g18_ncg import YUKAWA_PAIRS

    abs_q_vals = {abs(Q_VALUES[i]) for i, _, _ in YUKAWA_PAIRS}
    assert len(abs_q_vals) == 4
    expected = {sp.Integer(0), sp.Integer(1), sp.Rational(2, 3), sp.Rational(1, 3)}
    assert abs_q_vals == expected


def test_q_values_are_same_within_each_pair():
    """Q[i] = Q[j] for every Yukawa pair (i,j) — charge conservation."""
    from g18_ncg import YUKAWA_PAIRS

    for i, j, _ in YUKAWA_PAIRS:
        assert Q_VALUES[i] == Q_VALUES[j], f"Q[{i}]={Q_VALUES[i]} ≠ Q[{j}]={Q_VALUES[j]}"


def test_cpt_pairs_share_coupling():
    """CPT conjugate pairs have |Q[i]| = |Q[j]| and share the same Yukawa."""
    from g18_ncg import YUKAWA_PAIRS, PAIR_MAP

    yukawa_dict = {(i, j): y for i, j, y in YUKAWA_PAIRS}
    yukawa_dict.update({(j, i): y for i, j, y in YUKAWA_PAIRS})
    for i, j, y in YUKAWA_PAIRS:
        pi, pj = PAIR_MAP[i], PAIR_MAP[j]
        if (pi, pj) in yukawa_dict:
            assert yukawa_dict[(pi, pj)] == y, (
                f"CPT pair: Y({i},{j})={y} ≠ Y({pi},{pj})={yukawa_dict[(pi, pj)]}"
            )


# ── P5: Parameter count ───────────────────────────────────────────────────


def test_exactly_four_yukawa_parameters():
    """Exactly 4 distinct Yukawa symbols in D_F: {Y_nu, Y_e, Y_u, Y_d}."""
    assert N_YUKAWA_PARAMS == 4


def test_yukawa_symbols_match_sm_species():
    """The 4 Yukawa parameters are Y_nu, Y_e, Y_u, Y_d — one per SM fermion species."""
    assert YUKAWA_SYMBOLS == {Y_nu, Y_e, Y_u, Y_d}


def test_yukawa_q_values_count():
    """7 distinct Q values in YUKAWA_PAIRS (particles + CPT conjugates)."""
    assert len(YUKAWA_Q_VALUES) == 7


# ── P6: Cascade 256 → 16 → 4 ─────────────────────────────────────────────


def test_chiral_block_size():
    """Unconstrained L→R Yukawa block = 16×16 = 256 entries."""
    assert N_CHIRAL_BLOCK == 256


def test_s6_diagonal_size():
    """After S⁶-diagonal constraint: 8 modes × 2 S³ pairings = 16 entries."""
    assert N_S6_DIAGONAL == 16


def test_final_parameter_count():
    """After |Q|-uniqueness constraint: exactly 4 independent parameters."""
    assert N_FINAL == 4


def test_cascade_factor_s6():
    """S⁶-diagonal reduces entries by factor 16: 256/16 = 16."""
    assert N_CHIRAL_BLOCK // N_S6_DIAGONAL == 16


def test_cascade_factor_q():
    """Q-conservation reduces entries by factor 4: 16/4 = 4."""
    assert N_S6_DIAGONAL // N_FINAL == 4


def test_total_reduction_factor():
    """Total reduction: 256 → 4, factor 64×."""
    assert N_CHIRAL_BLOCK // N_FINAL == 64


# ── Gate function ─────────────────────────────────────────────────────────


def test_gate_function_passes():
    """verify_gates() returns PASS_G25_YUKAWA_TEXTURE (6/6)."""
    assert verify_gates() == "PASS_G25_YUKAWA_TEXTURE (6/6)"
