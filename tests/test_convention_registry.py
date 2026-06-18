"""Tests for convention_registry and frozen P13E/P13F guards."""

from __future__ import annotations

import pytest

from cc_toy_lab.compactification.convention_registry import (
    Classification,
    P13E_FROZEN_CLASSIFICATION,
    get_gate_status,
    register_gate_result,
)
from cc_toy_lab.compactification.registry_loader import assert_frozen_registry_present


def test_frozen_registry_files_present():
    files = assert_frozen_registry_present()
    assert len(files) == 9


def test_p13e_frozen_no_go():
    gs = get_gate_status("P13E")
    assert gs.status == "fixed"
    assert gs.classification == P13E_FROZEN_CLASSIFICATION


def test_cannot_overwrite_p13e_without_evidence():
    with pytest.raises(ValueError, match="Cannot overwrite frozen"):
        register_gate_result(
            "P13E",
            Classification.CONVENTION_FIXED_CANDIDATE,
            overwrite_frozen=False,
        )


def test_p13h_registration_allowed():
    gs = register_gate_result("P13H", Classification.NORMALIZATION_DEPENDENT_NO_GO)
    assert gs.gate_id == "P13H"
    assert gs.classification == Classification.NORMALIZATION_DEPENDENT_NO_GO.value
