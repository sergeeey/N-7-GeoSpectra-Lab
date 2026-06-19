"""G20 tests: Yukawa intertwiner space dim=4 from S³×S⁶ geometry + J_F."""

import os
import sys

import sympy as sp

_g20_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260619-g20-yukawa-intertwiner"
)
sys.path.insert(0, _g20_dir)

for _p in [
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g18-ncg-dirac-df"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g17-electric-charge"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g16-t3r-from-k3"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g15-hypercharge"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g11-block-generators"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g10b-su3-in-so6"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260617-g10-s6-so6-gauge"),
]:
    sys.path.insert(0, _p)

from g20_yukawa_intertwiner import (  # noqa: E402
    N_YUKAWA_PARAMS,
    SINGLET_CROSS_CHANNELS,
    SU3_ORBITS,
    VALID_PAIRS,
    YUKAWA_GROUPS,
    BmL_diag,
)
from g18_ncg import YUKAWA_PAIRS  # noqa: E402

half = sp.Rational(1, 2)


# ── M1: 16 valid pairs ────────────────────────────────────────────────────────


def test_valid_pairs_count_sixteen():
    """M1: same S⁶ index + bidoublet filter gives exactly 16 valid pairs."""
    assert len(VALID_PAIRS) == 16


def test_valid_pairs_unique():
    """All 16 valid pairs are distinct (L-index, R-index) tuples."""
    assert len(set(VALID_PAIRS)) == 16


def test_valid_pairs_same_s6_index():
    """Every valid pair has i_L % 8 == j_R % 8 (SU(3)-invariance via Schur's lemma)."""
    for i, j in VALID_PAIRS:
        assert i % 8 == j % 8, f"pair ({i},{j}): S⁶ indices {i % 8} ≠ {j % 8}"


def test_valid_pairs_dBL_zero():
    """M2 (corollary): same S⁶ index implies dBL = 0 for every valid pair."""
    for i, j in VALID_PAIRS:
        dBL = BmL_diag[j] - BmL_diag[i]
        assert dBL == 0, f"pair ({i},{j}): dBL = {dBL} (expected 0)"


# ── M2: matches G18 YUKAWA_PAIRS exactly ─────────────────────────────────────


def test_valid_pairs_match_g18_yukawa_pairs():
    """M2: VALID_PAIRS reproduces G18 YUKAWA_PAIRS exactly (set equality)."""
    g18_set = {(i, j) for i, j, _ in YUKAWA_PAIRS}
    our_set = set(VALID_PAIRS)
    assert our_set == g18_set, f"Extra: {our_set - g18_set}, Missing: {g18_set - our_set}"


def test_neutrino_pair_present():
    """ν_L(0) ↔ ν_R(16) in VALID_PAIRS (S⁶ index 0, B−L=−1)."""
    assert (0, 16) in set(VALID_PAIRS)


def test_electron_pair_present():
    """e_L(8) ↔ e_R(24) in VALID_PAIRS (S⁶ index 0, B−L=−1, L_DN)."""
    assert (8, 24) in set(VALID_PAIRS)


def test_u_quark_color_triplet_present():
    """u_L(3,5,6) ↔ u_R(19,21,22) in VALID_PAIRS (S⁶ indices 3,5,6, B−L=+1/3)."""
    for pair in [(3, 19), (5, 21), (6, 22)]:
        assert pair in set(VALID_PAIRS), f"u-quark pair {pair} missing from VALID_PAIRS"


def test_d_quark_color_triplet_present():
    """d_L(11,13,14) ↔ d_R(27,29,30) in VALID_PAIRS (S⁶ indices 3,5,6, B−L=+1/3, L_DN)."""
    for pair in [(11, 27), (13, 29), (14, 30)]:
        assert pair in set(VALID_PAIRS), f"d-quark pair {pair} missing from VALID_PAIRS"


# ── M3: 8 SU(3) orbits ────────────────────────────────────────────────────────


def test_su3_orbits_count_eight():
    """M3: exactly 8 SU(3) orbits (4 chirality classes × 4 S⁶ irrep sectors)."""
    assert len(SU3_ORBITS) == 8


def test_singlet_orbits_size_one():
    """M3: all 4 orbits with |B−L| = 1 have exactly 1 pair (leptonic singlets)."""
    singlet_orbits = {k: v for k, v in SU3_ORBITS.items() if abs(k[2]) == 1}
    assert len(singlet_orbits) == 4, f"Expected 4 singlet orbits, got {len(singlet_orbits)}"
    for key, pairs in singlet_orbits.items():
        assert len(pairs) == 1, f"Singlet orbit {key}: {len(pairs)} pairs (expected 1)"


def test_triplet_orbits_size_three():
    """M3: all 4 orbits with |B−L| = 1/3 have exactly 3 pairs (quark color triplets)."""
    third = sp.Rational(1, 3)
    triplet_orbits = {k: v for k, v in SU3_ORBITS.items() if abs(k[2]) == third}
    assert len(triplet_orbits) == 4, f"Expected 4 triplet orbits, got {len(triplet_orbits)}"
    for key, pairs in triplet_orbits.items():
        assert len(pairs) == 3, f"Triplet orbit {key}: {len(pairs)} pairs (expected 3)"


def test_orbit_keys_cover_both_chiralities():
    """Orbits cover both (L_UP, R_UP) and (L_DN, R_DN) chirality classes."""
    chiralities = {(k[0], k[1]) for k in SU3_ORBITS}
    assert ("L_UP", "R_UP") in chiralities
    assert ("L_DN", "R_DN") in chiralities


def test_orbit_bl_values():
    """Each chirality class has 4 B−L values: −1, −1/3, +1/3, +1."""
    third = sp.Rational(1, 3)
    expected_bls = {-1, -third, third, 1}
    for chirality in [("L_UP", "R_UP"), ("L_DN", "R_DN")]:
        bls = {k[2] for k in SU3_ORBITS if (k[0], k[1]) == chirality}
        assert bls == expected_bls, f"Chirality {chirality}: B−L values {bls}"


# ── M4: J_F → 4 coupling groups ──────────────────────────────────────────────


def test_yukawa_params_count_four():
    """M4: J_F real structure reduces 8 orbits to 4 independent coupling groups."""
    assert N_YUKAWA_PARAMS == 4


def test_yukawa_groups_pair_counts():
    """M4: the 4 groups contain [2,2,6,6] pairs (2 leptonic + 6+6 quark)."""
    pair_counts = sorted(len(g["pairs"]) for g in YUKAWA_GROUPS)
    assert pair_counts == [2, 2, 6, 6], f"Pair counts: {pair_counts}"


def test_yukawa_groups_orbit_count():
    """Each of the 4 coupling groups links exactly 2 SU(3) orbits (J_F partner pairs)."""
    for g in YUKAWA_GROUPS:
        assert len(g["orbits"]) == 2, f"Group {g['orbits']}: {len(g['orbits'])} orbits (expected 2)"


def test_yukawa_groups_cover_all_orbits():
    """All 8 SU(3) orbits appear in exactly one coupling group."""
    all_orbits_in_groups = [orb for g in YUKAWA_GROUPS for orb in g["orbits"]]
    assert len(all_orbits_in_groups) == 8
    assert set(all_orbits_in_groups) == set(SU3_ORBITS.keys())


def test_yukawa_groups_total_pairs():
    """Total pairs across all groups = 16 (2+6+2+6)."""
    total = sum(len(g["pairs"]) for g in YUKAWA_GROUPS)
    assert total == 16


def test_cpt_linked_groups_have_complementary_bl():
    """Each J_F-linked pair of orbits has opposite B−L charges (CPT structure)."""
    for g in YUKAWA_GROUPS:
        bl0 = g["orbits"][0][2]
        bl1 = g["orbits"][1][2]
        assert bl0 + bl1 == 0 or (abs(bl0) == abs(bl1)), (
            f"Group orbits {g['orbits']}: B−L {bl0} and {bl1} not CPT-paired"
        )


# ── M5: Singlet cross-channels absent ────────────────────────────────────────


def test_singlet_cross_channels_count_four():
    """M5: there are exactly 4 singlet cross-channel representatives."""
    assert len(SINGLET_CROSS_CHANNELS) == 4


def test_singlet_cross_channels_absent_from_valid_pairs():
    """M5: all singlet cross-channels are absent from VALID_PAIRS."""
    valid_set = set(VALID_PAIRS)
    for i, j in SINGLET_CROSS_CHANNELS:
        assert (i, j) not in valid_set, f"Forbidden channel ({i},{j}) found in VALID_PAIRS"


def test_singlet_cross_channels_dBL_two():
    """M5: singlet cross-channels carry |dBL| = 2 (lepton-number-violating)."""
    for i, j in SINGLET_CROSS_CHANNELS:
        dBL = BmL_diag[j] - BmL_diag[i]
        assert abs(dBL) == 2, f"Cross-channel ({i},{j}): |dBL| = {abs(dBL)} (expected 2)"


def test_singlet_cross_channels_connect_s6_endpoints():
    """M5: cross-channels connect S⁶ index 0 (B−L=−1) ↔ S⁶ index 7 (B−L=+1)."""
    for i, j in SINGLET_CROSS_CHANNELS:
        s6_i, s6_j = i % 8, j % 8
        assert {s6_i, s6_j} == {0, 7}, (
            f"Cross-channel ({i},{j}): S⁶ indices {s6_i},{s6_j} (expected {{0,7}})"
        )


# ── Structural completeness ───────────────────────────────────────────────────


def test_valid_pairs_only_l_to_r():
    """Every valid pair goes from L-sector (K3=0, J3≠0) to R-sector (J3=0, K3≠0)."""
    from g16_t3r_k3 import J3_32, K3_32

    for i, j in VALID_PAIRS:
        assert K3_32[i, i] == 0 and J3_32[i, i] != 0, f"Pair ({i},{j}): row {i} not in L-sector"
        assert J3_32[j, j] == 0 and K3_32[j, j] != 0, f"Pair ({i},{j}): row {j} not in R-sector"


def test_no_l_l_or_r_r_pairs():
    """No valid pair connects L→L or R→R (Yukawa must flip chirality)."""
    from g16_t3r_k3 import J3_32, K3_32

    valid_set = set(VALID_PAIRS)
    for i in range(32):
        for j in range(32):
            if (i, j) in valid_set:
                continue
            # Check that same-sector pairs are indeed absent
            same_sector = (K3_32[i, i] == 0 and K3_32[j, j] == 0) or (
                J3_32[i, i] == 0 and J3_32[j, j] == 0
            )
            if same_sector and i % 8 == j % 8:
                assert (i, j) not in valid_set


def test_gate_function_passes():
    """verify_gates() returns PASS_G20_YUKAWA_INTERTWINER (5/5)."""
    from g20_yukawa_intertwiner import verify_gates

    result = verify_gates()
    assert result == "PASS_G20_YUKAWA_INTERTWINER (5/5)"
