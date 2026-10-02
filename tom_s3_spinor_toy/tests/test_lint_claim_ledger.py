"""Tests for scripts/lint_claim_ledger.py and a guard on the real CLAIM_LEDGER.yaml.

Design (this project's own negative-control discipline):
  * a valid synthetic ledger MUST pass (positive control);
  * for every error code there is a mutation that MUST trigger exactly that
    code (and no other) on top of the valid baseline (negative controls), so
    "0 errors on the real ledger" cannot be a check that is unable to fail;
  * defect classes that only exist at YAML-TEXT level (an unquoted NULL, a
    repeated key) are tested through the linter's own loader, not on
    already-parsed dicts;
  * the defect classes actually found in the real ledger on 2026-10-03 are
    re-injected into a copy of it and must be caught again (regression);
  * the real ledger + derivation graph must lint clean (the guard itself).

Evidence level: the synthetic tests verify the TOOL ([VERIFIED-SYNTHETIC], valid
for unit tests); the real-ledger tests run it on the real files. Nothing here
validates any scientific claim.
"""

from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

PROJECT = Path(__file__).resolve().parents[1]
SCRIPT = PROJECT / "scripts" / "lint_claim_ledger.py"


def _load_module():
    # scripts/ is not a package (same approach as test_negative_control.py);
    # the module must be registered in sys.modules for @dataclass to resolve
    # its string annotations.
    name = "lint_claim_ledger_under_test"
    spec = importlib.util.spec_from_file_location(name, SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


lint = _load_module()

ENUMS = {
    "truth_status": ["PROVED", "SUPPORTED", "REFUTED"],
    "test_outcome": ["PASS", "FAIL", "NOT_RUN"],
    "execution_status": ["READY"],
    "evidence_status": ["INTERNALLY_CERTIFIED"],
    "lifecycle_status": ["ACTIVE", "SUPERSEDED"],
}
REQUIRED = [
    "id",
    "statement",
    "truth_status",
    "test_outcome",
    "execution_status",
    "evidence_status",
    "lifecycle_status",
    "evidence_file",
    "depends_on",
]


def _claim(cid, deps=(), evidence="ev.md:1-2", **over):
    c = {
        "id": cid,
        "statement": f"statement of {cid}",
        "truth_status": "SUPPORTED",
        "test_outcome": "PASS",
        "execution_status": "READY",
        "evidence_status": "INTERNALLY_CERTIFIED",
        "lifecycle_status": "ACTIVE",
        "evidence_file": evidence,
        "depends_on": list(deps),
    }
    c.update(over)
    return c


@pytest.fixture
def world(tmp_path):
    """A valid two-claim ledger whose evidence files exist under tmp_path."""
    (tmp_path / "ev.md").write_text("line1\nline2\nline3\n", encoding="utf-8")
    (tmp_path / "evdir").mkdir()
    ledger = {
        "schema": {"required": list(REQUIRED), "enums": copy.deepcopy(ENUMS)},
        "claims": [_claim("A"), _claim("B", deps=["A"])],
    }
    graph = {
        "derivations": [
            {
                "derivation_id": "D1",
                "premises": [{"claim": "A", "role": "x"}, {"claim": "B"}],
            }
        ]
    }
    return ledger, graph, [tmp_path]


def run(world_tuple, **kw):
    ledger, graph, roots = world_tuple
    return lint.lint_ledger(ledger, graph, roots, **kw)


# ---------------------------------------------------------------- positive control
def test_valid_synthetic_ledger_has_no_errors(world):
    rep = run(world)
    assert rep.errors == []
    assert rep.n_claims == 2


# ---------------------------------------------------------------- negative controls
def _del_statement(w):
    del w[0]["claims"][0]["statement"]


def _none_outcome(w):
    w[0]["claims"][0]["test_outcome"] = None  # what an unquoted YAML NULL becomes


def _bad_enum(w):
    w[0]["claims"][0]["truth_status"] = "PARTLY_TRUE"


def _dup_id(w):
    w[0]["claims"].append(_claim("A"))


def _dangling(w):
    w[0]["claims"][1]["depends_on"] = ["A", "NO_SUCH_CLAIM"]


def _self_dep(w):
    w[0]["claims"][0]["depends_on"] = ["A"]


def _cycle(w):
    w[0]["claims"][0]["depends_on"] = ["B"]  # A -> B -> A


def _depends_on_dict(w):
    w[0]["claims"][0][
        "depends_on"
    ] = {}  # must not be silently read as "no dependencies"


def _depends_on_false(w):
    w[0]["claims"][0]["depends_on"] = False


def _depends_on_non_string(w):
    w[0]["claims"][1]["depends_on"] = ["A", 7]


def _missing_file(w):
    w[0]["claims"][0]["evidence_file"] = "nope/missing.md:1-2"


def _line_past_eof(w):
    w[0]["claims"][0]["evidence_file"] = "ev.md:2-99"


def _start_past_eof(w):
    w[0]["claims"][0]["evidence_file"] = "ev.md:9-12"


def _reversed_range(w):
    w[0]["claims"][0]["evidence_file"] = "ev.md:3-1"


def _no_path(w):
    w[0]["claims"][0]["evidence_file"] = "see the discussion above"


def _glob_no_match(w):
    w[0]["claims"][0]["evidence_file"] = "evdir/round*/decision.md"


def _no_enums(w):
    del w[0]["schema"]["enums"]


def _one_enum_field_missing(w):
    del w[0]["schema"]["enums"][
        "test_outcome"
    ]  # would silently switch L2 off for that field


def _graph_unknown_premise(w):
    w[1]["derivations"][0]["premises"].append({"claim": "GHOST"})


def _graph_dup_derivation(w):
    w[1]["derivations"].append(copy.deepcopy(w[1]["derivations"][0]))


CONTROLS = [
    (_del_statement, "L1"),
    (_none_outcome, "L1"),
    (_bad_enum, "L2"),
    (_dup_id, "L3"),
    (_dangling, "L4"),
    (_self_dep, "L4"),
    (_depends_on_dict, "L4"),
    (_depends_on_false, "L4"),
    (_depends_on_non_string, "L4"),
    (_cycle, "L5"),
    (_missing_file, "L6"),
    (_line_past_eof, "L6"),
    (_start_past_eof, "L6"),
    (_reversed_range, "L6"),
    (_no_path, "L6"),
    (_glob_no_match, "L6"),
    (_no_enums, "L0"),
    (_one_enum_field_missing, "L0"),
    (_graph_unknown_premise, "L7"),
    (_graph_dup_derivation, "L7"),
]


@pytest.mark.parametrize("mutate,code", CONTROLS, ids=[m.__name__ for m, _ in CONTROLS])
def test_each_defect_class_triggers_exactly_its_code(world, mutate, code):
    assert run(world).errors == [], (
        "baseline must be clean, else the control proves nothing"
    )
    mutate(world)
    rep = run(world)
    assert rep.error_codes() == {code}, (
        f"{mutate.__name__}: expected only {code}, got {rep.errors}"
    )


# ---------------------------------------------------------------- YAML-text-level defects
def _dump(ledger) -> str:
    return yaml.safe_dump(ledger, sort_keys=False)


def test_unquoted_null_in_yaml_text_is_caught_end_to_end(world):
    """The trap found in the real ledger: `test_outcome: NULL` is YAML null."""
    ledger, graph, roots = world
    text = _dump(ledger)
    assert "test_outcome: PASS" in text
    bad = text.replace("test_outcome: PASS", "test_outcome: NULL", 1)
    assert yaml.safe_load("test_outcome: NULL") == {
        "test_outcome": None
    }  # the underlying trap
    data, dups = lint.load_yaml_text(bad)
    rep = lint.lint_ledger(data, graph, roots, ledger_dups=dups)
    assert [f.code for f in rep.errors] == ["L1"]
    # quoting it keeps the string, which is then (correctly) judged by the enum list instead
    good, dups = lint.load_yaml_text(
        text.replace("test_outcome: PASS", 'test_outcome: "NULL"', 1)
    )
    assert lint.lint_ledger(good, graph, roots, ledger_dups=dups).error_codes() == {
        "L2"
    }


def test_duplicate_keys_in_yaml_text_are_caught(world):
    ledger, graph, roots = world
    text = _dump(ledger)
    dup = text.replace(
        "test_outcome: PASS", "test_outcome: PASS\n  test_outcome: FAIL", 1
    )
    # same key twice in one claim: safe_load keeps the LAST value and says nothing
    assert yaml.safe_load(dup)["claims"][0]["test_outcome"] == "FAIL"
    data, dups = lint.load_yaml_text(dup)
    assert [k for _, k in dups] == ["test_outcome", "test_outcome"]
    rep = lint.lint_ledger(data, graph, roots, ledger_dups=dups)
    assert rep.error_codes() == {"L8"}
    # control: the clean text has no repeated keys
    assert lint.load_yaml_text(text)[1] == []


def test_duplicate_keys_in_graph_text_are_caught(world):
    ledger, graph, roots = world
    gtext = yaml.safe_dump(graph, sort_keys=False)
    bad = gtext.replace(
        "derivation_id: D1", "derivation_id: D1\n  derivation_id: D2", 1
    )
    gdata, gdups = lint.load_yaml_text(bad)
    assert lint.lint_ledger(ledger, gdata, roots, graph_dups=gdups).error_codes() == {
        "L8"
    }


# ---------------------------------------------------------------- accepted forms / parser
def test_directory_glob_and_line_forms_are_accepted(world, tmp_path):
    (tmp_path / "evdir" / "round90-x").mkdir()
    (tmp_path / "evdir" / "round90-x" / "decision.md").write_text(
        "x\n", encoding="utf-8"
    )
    ledger = world[0]
    ledger["claims"][0]["evidence_file"] = "evdir/"  # directory reference
    ledger["claims"][1]["evidence_file"] = (
        "evdir/round90-*/decision.md; ev.md:3 (note, 31/31 tests)"  # glob + single line + prose
    )
    assert run(world).errors == []


def test_parse_evidence_refs_forms():
    parse = lint.parse_evidence_refs
    refs = parse("tom_s3_spinor_toy/RESEARCH_STATUS_REPORT.md:31-33 (G73)")
    assert [(r.path, r.start, r.end) for r in refs] == [
        ("tom_s3_spinor_toy/RESEARCH_STATUS_REPORT.md", 31, 33)
    ]
    refs = parse("a/one.md;\n b/two.py:7")
    assert [(r.path, r.start, r.end) for r in refs] == [
        ("a/one.md", None, None),
        ("b/two.py", 7, 7),
    ]
    assert [r.path for r in parse("x/round90-*/decision.md")] == [
        "x/round90-*/decision.md"
    ]
    assert [r.path for r in parse("experiments/20260717-round94-bl/")] == [
        "experiments/20260717-round94-bl/"
    ]
    # prose with numbers and slashes must not produce references
    assert parse("G74B, 31/31 tests, and/or nothing") == []
    # other extensions and upper case are recognised (a bad one cannot hide as "unrecognised")
    assert [
        r.path for r in parse("data/Table.CSV and notes/paper.PDF and nb/run.ipynb")
    ] == [
        "data/Table.CSV",
        "notes/paper.PDF",
        "nb/run.ipynb",
    ]
    # URLs are not local references
    assert parse("https://arxiv.org/abs/2502.14016 and https://x.org/a/b.md") == []


# ---------------------------------------------------------------- --tracked mode
def test_tracked_mode_requires_exact_case_and_tracking(world, tmp_path):
    ledger = world[0]
    ledger["claims"][0]["evidence_file"] = "ev.md:1-2"
    tracked_ok = {"ev.md", "evdir/placeholder.md"}
    assert run(world, tracked=tracked_ok, repo_root=tmp_path).errors == []
    # exists on disk but is not tracked (e.g. never `git add`-ed) -> flagged
    rep = run(world, tracked={"other.md"}, repo_root=tmp_path)
    assert rep.error_codes() == {"L6"}
    # spelled with the wrong case: a Linux checkout would not find it
    ledger["claims"][0]["evidence_file"] = "EV.md:1-2"
    assert run(world, tracked=tracked_ok, repo_root=tmp_path).error_codes() == {"L6"}
    # directory references need at least one tracked file below them
    ledger["claims"][0]["evidence_file"] = "evdir/"
    assert run(world, tracked=tracked_ok, repo_root=tmp_path).errors == []
    assert run(world, tracked={"ev.md"}, repo_root=tmp_path).error_codes() == {"L6"}


# ---------------------------------------------------------------- advisories
def test_advisories_never_become_errors(world):
    ledger = world[0]
    ledger["claims"][0].update(
        truth_status="REFUTED", test_outcome="FAIL"
    )  # negative finding
    ledger["claims"][1].update(truth_status="PROVED")  # builds on it
    rep = run(world)
    assert rep.errors == []
    assert {f.code for f in rep.advisories} == {"A2"}
    ledger["claims"][0].update(truth_status="SUPPORTED", test_outcome="FAIL")
    assert "A1" in {f.code for f in run(world).advisories}


# ---------------------------------------------------------------- the real ledger
REAL_LEDGER = PROJECT / "CLAIM_LEDGER.yaml"
REAL_GRAPH = PROJECT / "DERIVATION_GRAPH.yaml"


@pytest.fixture(scope="module")
def real():
    ledger, ledger_dups = lint.load_yaml_file(REAL_LEDGER)
    graph, graph_dups = lint.load_yaml_file(REAL_GRAPH)
    return ledger, graph, ledger_dups, graph_dups


def _real_lint(ledger, graph, ledger_dups=(), graph_dups=()):
    return lint.lint_ledger(
        ledger, graph, ledger_dups=list(ledger_dups), graph_dups=list(graph_dups)
    )


def test_real_ledger_lints_clean(real):
    ledger, graph, ledger_dups, graph_dups = real
    rep = _real_lint(ledger, graph, ledger_dups, graph_dups)
    assert rep.n_claims > 100
    assert rep.errors == [], "CLAIM_LEDGER.yaml has mechanical defects:\n" + "\n".join(
        str(f) for f in rep.errors
    )


def test_real_ledger_regressions_are_caught(real):
    """The defect classes found on 2026-10-03, re-injected into a copy of the real ledger."""
    base_ledger, base_graph, _, _ = real
    assert _real_lint(base_ledger, base_graph).errors == []

    def variant():
        return copy.deepcopy(base_ledger), copy.deepcopy(base_graph)

    idx = next(
        i for i, c in enumerate(base_ledger["claims"]) if str(c["id"]).startswith("C5_")
    )

    # (1) the unquoted-NULL trap: a required field parsed to None
    ledger, graph = variant()
    ledger["claims"][idx]["test_outcome"] = None
    assert "L1" in _real_lint(ledger, graph).error_codes()

    # (2) off-vocabulary value (the old `MIXED` / `REJECT` synonyms)
    for bad in ("MIXED", "REJECT", "NULL"):
        ledger, graph = variant()
        ledger["claims"][idx]["test_outcome"] = bad
        assert "L2" in _real_lint(ledger, graph).error_codes(), bad

    # (3) a renamed id leaving a dangling depends_on
    ledger, graph = variant()
    victim = next(c for c in ledger["claims"] if c["depends_on"])
    victim["depends_on"] = [victim["depends_on"][0] + "_RENAMED"]
    assert "L4" in _real_lint(ledger, graph).error_codes()

    # (4) an evidence path abbreviated without its directory prefix
    ledger, graph = variant()
    ledger["claims"][idx]["evidence_file"] = (
        "20260717-round108-codex-item1-full-background-stabilizer/decision.md"
    )
    assert "L6" in _real_lint(ledger, graph).error_codes()

    # (5) the derivation graph points at a claim that is not in the ledger
    ledger, graph = variant()
    graph["derivations"][0]["premises"][0]["claim"] = "C0_NOT_A_CLAIM"
    assert "L7" in _real_lint(ledger, graph).error_codes()


def test_real_ledger_text_level_regressions_are_caught(real):
    """Unquoted NULL and a repeated key, injected into the real file TEXT."""
    _, graph, _, _ = real
    text = REAL_LEDGER.read_text(encoding="utf-8")
    assert "    test_outcome: PASS\n" in text

    nulled = text.replace("    test_outcome: PASS\n", "    test_outcome: NULL\n", 1)
    data, dups = lint.load_yaml_text(nulled)
    assert "L1" in _real_lint(data, graph, dups).error_codes()

    doubled = text.replace(
        "    test_outcome: PASS\n",
        "    test_outcome: PASS\n    test_outcome: FAIL\n",
        1,
    )
    data, dups = lint.load_yaml_text(doubled)
    assert "L8" in _real_lint(data, graph, dups).error_codes()


def test_real_ledger_has_no_null_valued_status_fields(real):
    ledger, *_ = real
    enums = ledger["schema"]["enums"]
    assert (
        "NULL" not in enums["test_outcome"]
    )  # deliberately not a value (see the schema comment)
    for c in ledger["claims"]:
        for f in lint.STATUS_FIELDS:
            assert c[f] is not None, f"{c['id']}: {f} is null"


# ---------------------------------------------------------------- CLI
def test_cli_exit_codes(tmp_path, capsys):
    assert lint.main([]) == 0  # real ledger + real graph
    out = capsys.readouterr().out
    assert "errors=0" in out

    broken = {
        "schema": {"required": REQUIRED, "enums": ENUMS},
        "claims": [_claim("A", evidence="nowhere/at_all.md")],
    }
    path = tmp_path / "broken.yaml"
    path.write_text(yaml.safe_dump(broken), encoding="utf-8")
    assert (
        lint.main(["--ledger", str(path), "--graph", str(tmp_path / "none.yaml")]) == 1
    )
    assert "[L6]" in capsys.readouterr().out
