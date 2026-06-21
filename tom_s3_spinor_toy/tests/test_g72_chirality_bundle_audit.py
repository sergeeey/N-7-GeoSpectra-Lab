"""G72: chirality audit for triality-related twisting bundles on S6."""

import csv
import os
import sys
from fractions import Fraction
from pathlib import Path

import pytest

_EXP_DIR = os.path.join(
    os.path.dirname(__file__),
    "..",
    "experiments",
    "20260621-g72-chirality-bundle-audit",
)
sys.path.insert(0, _EXP_DIR)

from g72_chirality_audit import (  # noqa: E402
    CANONICAL_TANGENT_BUNDLE,
    G30_UNIVERSAL_NO_GO_SURVIVES,
    REQUIRED_TOTAL_C3,
    TARGET_INDEX,
    TRIALITY_CHANNELS,
    TwistBundle,
    bundle_index,
    classify_triality_claim,
    total_index,
)


def test_s6_index_is_c3_over_two():
    for c3 in (-6, -2, 0, 2, 6):
        bundle = TwistBundle("test", rank=3, c3=c3)
        assert bundle_index(bundle) == Fraction(c3, 2)


def test_odd_c3_is_rejected():
    with pytest.raises(ValueError, match="even"):
        TwistBundle("invalid", rank=3, c3=1)


def test_canonical_tangent_bundle_is_g2_equivariant_with_index_one():
    bundle = CANONICAL_TANGENT_BUNDLE
    assert bundle.g2_equivariant is True
    assert bundle.c3 == 2
    assert bundle_index(bundle) == 1


def test_g30_universal_equivariant_index_zero_claim_does_not_survive():
    assert G30_UNIVERSAL_NO_GO_SURVIVES is False


def test_triality_channels_do_not_have_derived_bundles():
    assert [channel.name for channel in TRIALITY_CHANNELS] == ["8_v", "8_s", "8_c"]
    assert all(channel.c3 is None for channel in TRIALITY_CHANNELS)
    assert all(channel.appears_in_action is False for channel in TRIALITY_CHANNELS)


def test_current_triality_claim_is_unresolved_not_index_three():
    result = classify_triality_claim(TRIALITY_CHANNELS)
    assert result.status == "UNRESOLVED"
    assert result.total_c3 is None
    assert result.index is None


def test_same_number_of_channels_can_be_vectorlike_or_chiral():
    same_sign = [
        TwistBundle("8_v", rank=3, c3=2, appears_in_action=True),
        TwistBundle("8_s", rank=3, c3=2, appears_in_action=True),
        TwistBundle("8_c", rank=3, c3=2, appears_in_action=True),
    ]
    vectorlike = [
        TwistBundle("8_v", rank=3, c3=0, appears_in_action=True),
        TwistBundle("8_s", rank=3, c3=2, appears_in_action=True),
        TwistBundle("8_c", rank=3, c3=-2, appears_in_action=True),
    ]

    assert len(same_sign) == len(vectorlike) == 3
    assert total_index(same_sign) == 3
    assert total_index(vectorlike) == 0


def test_index_three_requires_total_c3_six():
    assert TARGET_INDEX == 3
    assert REQUIRED_TOTAL_C3 == 6

    candidates = [
        TwistBundle("8_v", rank=3, c3=2, appears_in_action=True),
        TwistBundle("8_s", rank=3, c3=2, appears_in_action=True),
        TwistBundle("8_c", rank=3, c3=2, appears_in_action=True),
    ]
    result = classify_triality_claim(candidates)
    assert result.status == "CONDITIONAL_INDEX_3"
    assert result.total_c3 == REQUIRED_TOTAL_C3
    assert result.index == TARGET_INDEX


def test_index_three_is_not_enough_if_a_channel_is_absent_from_action():
    candidates = [
        TwistBundle("8_v", rank=3, c3=2, appears_in_action=True),
        TwistBundle("8_s", rank=3, c3=2, appears_in_action=True),
        TwistBundle("8_c", rank=3, c3=2, appears_in_action=False),
    ]
    result = classify_triality_claim(candidates)
    assert result.status == "UNRESOLVED"


def test_bundle_ledger_csv_matches_open_state():
    ledger_path = Path(_EXP_DIR) / "bundle_ledger.csv"
    assert ledger_path.exists()

    with ledger_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    assert [row["channel"] for row in rows] == ["8_v", "8_s", "8_c"]
    assert all(row["c3"] == "UNKNOWN" for row in rows)
    assert all(row["index"] == "UNKNOWN" for row in rows)
    assert all(row["appears_in_action"] == "NO" for row in rows)
