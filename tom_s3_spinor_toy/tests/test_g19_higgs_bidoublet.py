"""G19 tests: Higgs (2,2)₀ bidoublet quantum numbers from D_F Yukawa structure."""

import os
import sys

import sympy as sp

_g19_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260619-g19-higgs-bidoublet"
)
sys.path.insert(0, _g19_dir)

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

from g19_higgs_bidoublet import (  # noqa: E402
    BIDOUBLET_COMPONENTS,
    HIGGS_COMPONENT_M,
    HIGGS_COMPONENT_P,
    HIGGS_QN,
)

half = sp.Rational(1, 2)


# ── Coverage ───────────────────────────────────────────────────────────────────


def test_higgs_qn_sixteen_pairs():
    """HIGGS_QN covers all 16 Yukawa pairs from G18."""
    assert len(HIGGS_QN) == 16


# ── T1: neutral Higgs (dQ = 0) ────────────────────────────────────────────────


def test_dQ_zero_all_pairs():
    """dQ = 0 for every Yukawa pair — only neutral Higgs mediates (T1)."""
    for qn in HIGGS_QN:
        assert qn["dQ"] == 0, f"pair {qn['pair']}: dQ = {qn['dQ']}"


def test_neutrino_dQ_zero():
    """ν_L(0) ↔ ν_R(16): dQ = 0."""
    qn = next(q for q in HIGGS_QN if q["pair"] == (0, 16))
    assert qn["dQ"] == 0


def test_electron_dQ_zero():
    """e_L(8) ↔ e_R(24): dQ = 0."""
    qn = next(q for q in HIGGS_QN if q["pair"] == (8, 24))
    assert qn["dQ"] == 0


# ── T2: SU(2)_L doublet (|dT3L| = 1/2) ───────────────────────────────────────


def test_abs_dT3L_half_all_pairs():
    """|dT3L| = 1/2 for every pair — SU(2)_L doublet, not singlet or adjoint (T2)."""
    for qn in HIGGS_QN:
        assert abs(qn["dT3L"]) == half, f"pair {qn['pair']}: |dT3L| = {abs(qn['dT3L'])}"


def test_dT3L_not_zero():
    """dT3L ≠ 0 for any pair — rules out SU(2)_L singlet assignment."""
    for qn in HIGGS_QN:
        assert qn["dT3L"] != 0, f"pair {qn['pair']}: dT3L = 0 (singlet forbidden)"


# ── T3: SU(2)_R doublet (|dT3R| = 1/2) ───────────────────────────────────────


def test_abs_dT3R_half_all_pairs():
    """|dT3R| = 1/2 for every pair — SU(2)_R doublet (T3)."""
    for qn in HIGGS_QN:
        assert abs(qn["dT3R"]) == half, f"pair {qn['pair']}: |dT3R| = {abs(qn['dT3R'])}"


# ── T4: bidoublet anti-diagonal (dT3L + dT3R = 0) ────────────────────────────


def test_dT3L_plus_dT3R_zero_all_pairs():
    """dT3L + dT3R = 0 for every pair — anti-diagonal bidoublet structure (T4)."""
    for qn in HIGGS_QN:
        assert qn["dT3L"] + qn["dT3R"] == 0, (
            f"pair {qn['pair']}: dT3L+dT3R = {qn['dT3L'] + qn['dT3R']}"
        )


# ── T5: B−L singlet (dBL = 0) ────────────────────────────────────────────────


def test_dBL_zero_all_pairs():
    """dBL = 0 for every pair — Higgs carries no B−L charge (T5)."""
    for qn in HIGGS_QN:
        assert qn["dBL"] == 0, f"pair {qn['pair']}: dBL = {qn['dBL']}"


def test_higgs_lives_in_s3_not_s6():
    """dBL = 0 geometrically: both Yukawa partners share same S⁶ fiber index."""
    # BmL_32 = kron(I₄, BmL) — depends only on S⁶ index, not L/R sector.
    # Yukawa pairs (i_L, j_R) differ only in S³ sector → same S⁶ index → dBL = 0.
    assert all(qn["dBL"] == 0 for qn in HIGGS_QN)


# ── T6: dY = dT3R ────────────────────────────────────────────────────────────


def test_dY_equals_dT3R_all_pairs():
    """dY = dT3R for every pair — Y of Higgs entirely from T3R (T6)."""
    for qn in HIGGS_QN:
        assert qn["dY"] == qn["dT3R"], f"pair {qn['pair']}: dY={qn['dY']}, dT3R={qn['dT3R']}"


# ── T7: exactly 2 bidoublet components ────────────────────────────────────────


def test_bidoublet_exactly_two_components():
    """Exactly 2 distinct (dT3L, dT3R) values — the (2,2)₀ bidoublet (T7)."""
    observed = frozenset((qn["dT3L"], qn["dT3R"]) for qn in HIGGS_QN)
    assert observed == BIDOUBLET_COMPONENTS


def test_bidoublet_component_values():
    """The two components are (−1/2, +1/2) and (+1/2, −1/2)."""
    assert HIGGS_COMPONENT_P == (-half, +half)
    assert HIGGS_COMPONENT_M == (+half, -half)


# ── T8: equal 8-8 split ───────────────────────────────────────────────────────


def test_equal_split_eight_each():
    """8 pairs in (−1/2, +1/2) and 8 in (+1/2, −1/2) — symmetric spectrum (T8)."""
    n_p = sum(1 for qn in HIGGS_QN if (qn["dT3L"], qn["dT3R"]) == HIGGS_COMPONENT_P)
    n_m = sum(1 for qn in HIGGS_QN if (qn["dT3L"], qn["dT3R"]) == HIGGS_COMPONENT_M)
    assert n_p == 8 and n_m == 8, f"unequal split: {n_p} vs {n_m}"


# ── Specific pair quantum numbers ─────────────────────────────────────────────


def test_neutrino_qn_uptype_component():
    """ν_L(0)↔ν_R(16): (dT3L, dT3R) = (−1/2, +1/2) — uptype component."""
    qn = next(q for q in HIGGS_QN if q["pair"] == (0, 16))
    assert (qn["dT3L"], qn["dT3R"]) == HIGGS_COMPONENT_P
    assert qn["dY"] == half  # Y of Higgs = +1/2 (SM Higgs hypercharge)


def test_electron_qn_downtype_component():
    """e_L(8)↔e_R(24): (dT3L, dT3R) = (+1/2, −1/2) — downtype component."""
    qn = next(q for q in HIGGS_QN if q["pair"] == (8, 24))
    assert (qn["dT3L"], qn["dT3R"]) == HIGGS_COMPONENT_M
    assert qn["dY"] == -half  # Y of conjugate Higgs = −1/2


# ── Color triplet consistency ──────────────────────────────────────────────────


def test_u_quark_triplet_same_component():
    """All 3 u-quark color pairs use the same (−1/2, +1/2) bidoublet component."""
    for pair in [(3, 19), (5, 21), (6, 22)]:
        qn = next(q for q in HIGGS_QN if q["pair"] == pair)
        assert (qn["dT3L"], qn["dT3R"]) == HIGGS_COMPONENT_P, (
            f"u_L pair {pair}: component = {(qn['dT3L'], qn['dT3R'])}"
        )


def test_d_quark_triplet_same_component():
    """All 3 d-quark color pairs use the same (+1/2, −1/2) bidoublet component."""
    for pair in [(11, 27), (13, 29), (14, 30)]:
        qn = next(q for q in HIGGS_QN if q["pair"] == pair)
        assert (qn["dT3L"], qn["dT3R"]) == HIGGS_COMPONENT_M, (
            f"d_L pair {pair}: component = {(qn['dT3L'], qn['dT3R'])}"
        )


def test_quark_triplets_dBL_zero():
    """dBL = 0 for all quark Yukawa pairs — u,d quarks have same B−L in L and R."""
    for pair in [(3, 19), (5, 21), (6, 22), (11, 27), (13, 29), (14, 30)]:
        qn = next(q for q in HIGGS_QN if q["pair"] == pair)
        assert qn["dBL"] == 0, f"pair {pair}: dBL = {qn['dBL']}"
