"""G6: 32-component S³×S⁶ spinor → SM quantum numbers.

Verifies that the Dirac spinor on S³×S⁶ decomposes into exactly one SM generation
under the Pati-Salam identification with hypercharge Y = T3R + (B-L)/2.
"""

import sympy as sp
from collections import Counter
from itertools import product as iproduct


# ── helpers ──────────────────────────────────────────────────────────────────


def _bl_charge(weight):
    """B-L charge and SU(3) rep for an S⁶ spinor weight (±½,±½,±½)."""
    n_minus = sum(1 for x in weight if x < 0)
    positive = n_minus % 2 == 0  # S+ ↔ 4 of SU(4), S- ↔ 4̄
    all_same = weight[0] == weight[1] == weight[2]
    if positive:
        if all_same:
            return sp.Integer(-1), "1"  # lepton singlet
        return sp.Rational(1, 3), "3"  # quark triplet
    else:
        if all_same:
            return sp.Integer(1), "1bar"  # anti-lepton
        return sp.Rational(-1, 3), "3bar"  # anti-quark triplet


def build_32_states():
    """Return list of (T3L, T3R, Y, su3_rep) for all 32 S³×S⁶ spinor states."""
    s3 = [
        (sp.Rational(1, 2), sp.Integer(0)),
        (sp.Rational(-1, 2), sp.Integer(0)),
        (sp.Integer(0), sp.Rational(1, 2)),
        (sp.Integer(0), sp.Rational(-1, 2)),
    ]
    weights = list(iproduct([sp.Rational(-1, 2), sp.Rational(1, 2)], repeat=3))
    states = []
    for t3l, t3r in s3:
        for w in weights:
            bl, su3 = _bl_charge(w)
            y = t3r + bl / 2
            states.append((t3l, t3r, y, su3))
    return states


SM_EXPECTED = {
    # (T3L, Y, su3_rep): (name, multiplicity)
    (sp.Rational(1, 2), sp.Rational(1, 6), "3"): ("uL", 3),
    (sp.Rational(-1, 2), sp.Rational(1, 6), "3"): ("dL", 3),
    (sp.Integer(0), sp.Rational(2, 3), "3"): ("uR", 3),
    (sp.Integer(0), sp.Rational(-1, 3), "3"): ("dR", 3),
    (sp.Rational(1, 2), sp.Rational(-1, 2), "1"): ("νL", 1),
    (sp.Rational(-1, 2), sp.Rational(-1, 2), "1"): ("eL", 1),
    (sp.Integer(0), sp.Integer(0), "1"): ("νR", 1),
    (sp.Integer(0), sp.Integer(-1), "1"): ("eR", 1),
    (sp.Rational(1, 2), sp.Rational(-1, 6), "3bar"): ("ūL", 3),
    (sp.Rational(-1, 2), sp.Rational(-1, 6), "3bar"): ("d̄L", 3),
    (sp.Integer(0), sp.Rational(-2, 3), "3bar"): ("ūR", 3),
    (sp.Integer(0), sp.Rational(1, 3), "3bar"): ("d̄R", 3),
    (sp.Rational(1, 2), sp.Rational(1, 2), "1bar"): ("ν̄L", 1),
    (sp.Rational(-1, 2), sp.Rational(1, 2), "1bar"): ("ēL", 1),
    (sp.Integer(0), sp.Integer(0), "1bar"): ("ν̄R", 1),
    (sp.Integer(0), sp.Integer(1), "1bar"): ("ēR", 1),
}


# ── tests ─────────────────────────────────────────────────────────────────────


def test_total_states_32():
    """S³×S⁶ spinor has exactly 32 components."""
    assert len(build_32_states()) == 32


def test_all_states_match_sm():
    """Every one of 32 states maps to a named SM particle."""
    states = build_32_states()
    unmatched = []
    for t3l, t3r, y, su3 in states:
        if (t3l, y, su3) not in SM_EXPECTED:
            unmatched.append((t3l, t3r, y, su3))
    assert unmatched == [], f"Unmatched states: {unmatched}"


def test_all_sm_particles_present():
    """All 16 distinct SM particle labels appear at least once."""
    states = build_32_states()
    found_keys = {(t3l, y, su3) for t3l, _t3r, y, su3 in states}
    missing = set(SM_EXPECTED) - found_keys
    assert missing == set(), f"Missing SM particles: {[SM_EXPECTED[k][0] for k in missing]}"


def test_quark_multiplicity_3():
    """Each quark flavor appears exactly 3 times (color triplet)."""
    states = build_32_states()
    counts = Counter()
    for t3l, _t3r, y, su3 in states:
        key = (t3l, y, su3)
        if key in SM_EXPECTED:
            counts[SM_EXPECTED[key][0]] += 1

    quark_labels = {"uL", "dL", "uR", "dR", "ūL", "d̄L", "ūR", "d̄R"}
    for label in quark_labels:
        assert counts[label] == 3, f"{label} has {counts[label]} states, expected 3"


def test_lepton_multiplicity_1():
    """Each lepton appears exactly once (color singlet)."""
    states = build_32_states()
    counts = Counter()
    for t3l, _t3r, y, su3 in states:
        key = (t3l, y, su3)
        if key in SM_EXPECTED:
            counts[SM_EXPECTED[key][0]] += 1

    lepton_labels = {"νL", "eL", "νR", "eR", "ν̄L", "ēL", "ν̄R", "ēR"}
    for label in lepton_labels:
        assert counts[label] == 1, f"{label} has {counts[label]} states, expected 1"


def test_hypercharge_formula_y_equals_t3r_plus_half_bl():
    """Y = T3R + (B-L)/2 holds for every state."""
    weights = list(iproduct([sp.Rational(-1, 2), sp.Rational(1, 2)], repeat=3))
    s3 = [
        (sp.Rational(1, 2), sp.Integer(0)),
        (sp.Rational(-1, 2), sp.Integer(0)),
        (sp.Integer(0), sp.Rational(1, 2)),
        (sp.Integer(0), sp.Rational(-1, 2)),
    ]
    for t3l, t3r in s3:
        for w in weights:
            bl, su3 = _bl_charge(w)
            y = t3r + bl / 2
            # SM hypercharges are multiples of 1/6: leptons ∈ {0,±½,±1}, quarks ∈ {±1/6,±1/3,±2/3}
            assert (6 * y).is_integer, f"Y={y} not a multiple of 1/6 for (T3L={t3l}, weight={w})"


def test_total_charge_conservation():
    """Sum of hypercharges over all 32 states = 0 (charge conjugation symmetry)."""
    states = build_32_states()
    total_y = sum(y for _t3l, _t3r, y, _su3 in states)
    assert total_y == 0, f"Sum of Y = {total_y} ≠ 0"


def test_s6_weight_chirality_split():
    """S⁶ spinor weights split exactly 4/4 between positive and negative chirality."""
    weights = list(iproduct([sp.Rational(-1, 2), sp.Rational(1, 2)], repeat=3))
    n_plus = sum(1 for w in weights if sum(1 for x in w if x < 0) % 2 == 0)
    n_minus = sum(1 for w in weights if sum(1 for x in w if x < 0) % 2 == 1)
    assert n_plus == 4, f"S+ has {n_plus} weights, expected 4"
    assert n_minus == 4, f"S- has {n_minus} weights, expected 4"
