"""Tests for the negative-control convention (helper + checker).

The first test is the point of the file: this checker's OWN negative control.
A checker that returns OK on every input would be exactly the cannot-fail
check it was built to catch, so `test_checker_flags_a_file_with_no_control`
feeds it a results file with no control record and asserts it FLAGS. If that
test ever passes trivially, the checker is worthless regardless of what the
other tests say.

Added 2026-09-07 with `experiments/_template/negative_control.py` and
`scripts/check_negative_control.py`. See `docs/negative_control_pattern.md`.
"""

from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent
REPO = str(REPO_ROOT)


def _load(name: str, path: Path):
    """Load a module that lives outside any package.

    Neither `scripts/` nor `experiments/_template/` is importable as a package,
    and this is how the rest of this repo's tests reach such modules (see
    test_c85_certification.py) -- matching the established convention rather
    than adding a sys.path mechanism as a side effect of adding tests.
    """
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


chk = _load("check_negative_control", REPO_ROOT / "scripts" / "check_negative_control.py")
_nc = _load("negative_control", REPO_ROOT / "experiments" / "_template" / "negative_control.py")

CONVENTION_START = chk.CONVENTION_START
FIRED, LEGACY, MISSING, OK = chk.FIRED, chk.LEGACY, chk.MISSING, chk.OK
classify, main = chk.classify, chk.main
negative_control = _nc.negative_control


def _write(tmp_path, name, doc):
    p = tmp_path / name
    p.write_text(json.dumps(doc), encoding="utf-8")
    return str(p)


# --------------------------------------------------------------------------
# The checker's own negative control -- see the module docstring.
# --------------------------------------------------------------------------


def test_checker_flags_a_file_with_no_control(tmp_path):
    """An input for which the checker MUST report failure."""
    doc = {"eigenvalues": [1.0, 2.0], "verdict": "CONFIRMED", "all_levels_match": True}
    status, _reason = classify(_write(tmp_path, "results_x.json", doc))
    assert status == MISSING


def test_checker_flags_a_plausible_looking_results_table(tmp_path):
    """Booleans of both polarities in a per-level table are NOT a control.

    Without this, `_mixed_polarity_table` alone would pass an ordinary results
    table -- which is how C182 (one of the five cannot-fail checks) would have
    slipped through. The corruption must be DECLARED as well as visible.
    """
    doc = {
        "per_level": [
            {"k": 0, "parity": "even", "half_integer_weight_present": False},
            {"k": 1, "parity": "odd", "half_integer_weight_present": True},
        ],
        "verdict": "DESCENT-CONFIRMED",
    }
    status, _reason = classify(_write(tmp_path, "results_c182_like.json", doc))
    assert status == MISSING


# --------------------------------------------------------------------------
# The helper produces a block the checker accepts, in both directions.
# --------------------------------------------------------------------------


def test_helper_discriminating_check_round_trips_to_OK(tmp_path):
    nc = negative_control(
        lambda xs: sum(xs) == 6,
        real=[1, 2, 3],
        controls={"one entry shifted by +1": [1, 2, 4], "all entries doubled": [2, 4, 6]},
        label="sum equals 6",
    )
    assert nc.discriminates is True
    status, _reason = classify(
        _write(tmp_path, "results_ok.json", {"negative_control": nc.as_dict()})
    )
    assert status == OK


def test_helper_cannot_fail_check_is_caught_by_its_own_control(tmp_path):
    """The check the C179-C182 sequence kept writing: one that passes on anything."""
    nc = negative_control(
        lambda xs: len(xs) >= 0,  # true for every input
        real=[1, 2, 3],
        controls={"unrelated junk input": ["nonsense"]},
        label="length is non-negative",
    )
    assert nc.discriminates is False
    assert nc.surviving_controls == ["unrelated junk input"]
    assert "CANNOT-FAIL CHECK" in nc.report()
    status, reason = classify(
        _write(tmp_path, "results_fired.json", {"negative_control": nc.as_dict()})
    )
    assert status == FIRED
    assert "unrelated junk input" in reason


def test_helper_refuses_an_empty_control_set():
    nc = negative_control(lambda xs: True, real=[1], controls={}, label="uncontrolled")
    assert nc.discriminates is False
    assert "NO CONTROL RUN" in nc.report()


# --------------------------------------------------------------------------
# The two pre-convention scripts named in the pearl as already correct must
# keep passing -- they are the worked examples the convention was read off.
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "rel",
    [
        "experiments/20260907-c181-gamma-projection-and-normal-coordinates/results_c181b.json",
        "experiments/20260907-c180-explicit-s3-spinor-harmonics/results_c180b.json",
    ],
)
def test_pre_convention_exemplars_are_recognised(rel):
    path = os.path.join(REPO, *rel.split("/"))
    if not os.path.exists(path):
        pytest.skip("exemplar not present: " + rel)
    status, _reason = classify(path)
    assert status == LEGACY


def test_a_malformed_canonical_block_is_flagged_not_waved_through(tmp_path):
    doc = {"negative_control": {"check": "x", "discriminates": True}}
    status, reason = classify(_write(tmp_path, "results_bad.json", doc))
    assert status == MISSING
    assert "missing field" in reason


# --------------------------------------------------------------------------
# Regressions for four defects found by an independent context-blind review
# on 2026-09-07, each reproduced before being fixed. See
# docs/negative_control_pattern.md "Defects found in this machinery itself".
# --------------------------------------------------------------------------


def test_stateful_check_cannot_fabricate_falsifying_power():
    """A check answering from call order, never inspecting its argument.

    Before the re-run guard this produced the exact signature of success --
    pass on the real input, fail on every control -- and was certified as
    discriminating.
    """

    def counter(_x):
        counter.n = getattr(counter, "n", 0) + 1
        return counter.n == 1

    nc = negative_control(
        counter, real=[1, 2, 3], controls={"a": [9, 9, 9], "b": [0]}, label="counter"
    )
    assert nc.deterministic_on_rerun is False
    assert nc.discriminates is False
    assert "NOT A FUNCTION OF ITS INPUT" in nc.report()


def test_a_genuine_control_survives_a_malformed_neighbour(tmp_path):
    """ "At least one" must mean at least one, not "the first entry decides"."""
    good = negative_control(
        lambda xs: sum(xs) == 6,
        real=[1, 2, 3],
        controls={"one entry shifted by +1": [1, 2, 4]},
        label="genuine sum check",
    )
    doc = {"negative_control": [good.as_dict(), {"check": "junk", "discriminates": True}]}
    status, reason = classify(_write(tmp_path, "results_mixed.json", doc))
    assert status == OK
    assert "malformed entries ignored" in reason


def test_a_fired_control_outranks_a_good_one_in_the_same_file(tmp_path):
    good = negative_control(
        lambda xs: sum(xs) == 6, real=[1, 2, 3], controls={"shifted": [1, 2, 4]}, label="good"
    )
    bad = negative_control(lambda xs: True, real=[1], controls={"junk": [9]}, label="always true")
    doc = {"negative_control": [good.as_dict(), bad.as_dict()]}
    status, _reason = classify(_write(tmp_path, "results_both.json", doc))
    assert status == FIRED


def test_scanning_zero_files_is_never_reported_as_a_pass(tmp_path, capsys):
    """Exit 0 on an empty scan would make the checker itself cannot-fail."""
    rc = main([str(tmp_path / "no_such_dir")])
    out = capsys.readouterr().out
    assert rc == 1
    assert "PASS" not in out
    assert "NOTHING SCANNED" in out


def test_legacy_shape_does_not_satisfy_enforcement_for_a_post_cutoff_round(tmp_path, capsys):
    """A lone `discriminates: true` must not clear the gate in a new round.

    Both legacy forms are cheap to satisfy without a real control. They stay
    readable for the pre-convention files that have them, and stop counting
    once a round is inside the enforced window.
    """
    round_dir = tmp_path / (CONVENTION_START + "-c999-demo")
    round_dir.mkdir()
    (round_dir / "results_x.json").write_text(json.dumps({"discriminates": True}), encoding="utf-8")
    original = chk.EXPERIMENTS_DIR
    try:
        chk.EXPERIMENTS_DIR = str(tmp_path)  # so round_date() can see the date prefix
        rc = main([str(round_dir)])
    finally:
        chk.EXPERIMENTS_DIR = original
    out = capsys.readouterr().out
    assert rc == 1
    assert "not sufficient for a round" in out
