"""Negative controls for hooks/claim_scope_gate.py.

WHY HERE and not tests/: tests/ is write-protected in the session this was
written in. Same pattern as
experiments/20260622-g79a-lambda-identity-audit/negative_controls_2026_08_09.py.

WHY AT ALL: this repo's own 2026-08-10 pearl says a search that cannot succeed
is indistinguishable from evidence of absence -- and a GATE that cannot fire is
indistinguishable from a repo that has nothing to report. The first run of these
controls "passed" by staying silent, which looked like the gate rejecting
nothing; the real cause was that the fixtures were named led_A.yaml while the
hook filters on the basename CLAIM_LEDGER.yaml. The fixtures must therefore be
written into per-case DIRECTORIES with the real filename.
"""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

HOOK = Path.home() / ".claude" / "hooks" / "claim_scope_gate.py"
LEDGER = Path(__file__).resolve().parents[2] / "CLAIM_LEDGER.yaml"


def _run(path: Path | str) -> str:
    p = subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps({"tool_input": {"file_path": str(path)}}),
        capture_output=True,
        text=True,
        check=False,
    )
    if not p.stdout.strip():
        return ""
    return json.loads(p.stdout)["hookSpecificOutput"]["additionalContext"]


def _fixture(tmp: Path, tag: str, mutate) -> Path:
    doc = copy.deepcopy(yaml.safe_load(LEDGER.read_text(encoding="utf-8")))
    mutate(doc)
    d = tmp / tag
    d.mkdir(parents=True, exist_ok=True)
    f = d / "CLAIM_LEDGER.yaml"  # basename matters: the hook filters on it
    f.write_text(yaml.safe_dump(doc, allow_unicode=True), encoding="utf-8")
    return f


def _drop(prefix: str, field: str):
    def m(doc):
        for c in doc["claims"]:
            if str(c.get("id", "")).startswith(prefix):
                c.pop(field, None)

    return m


def main() -> int:
    failures = []

    def check(name: str, cond: bool):
        print(f"  {'PASS' if cond else 'FAIL'}  {name}")
        if not cond:
            failures.append(name)

    print("claim_scope_gate.py negative controls")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)

        check("real ledger passes", _run(LEDGER).lstrip().startswith("[claim-scope-gate] ✓"))
        check(
            "fires when C35 loses does_not_imply",
            "does_not_imply MISSING" in _run(_fixture(tmp, "a", _drop("C35", "does_not_imply"))),
        )
        check(
            "fires when C36 loses convention (statement is convention-sensitive)",
            "convention MISSING" in _run(_fixture(tmp, "b", _drop("C36", "convention"))),
        )
        check(
            "does NOT fire for a pre-C32 legacy claim",
            "MISSING" not in _run(_fixture(tmp, "c", _drop("C27", "does_not_imply"))),
        )

        def empty(doc):
            for c in doc["claims"]:
                if str(c.get("id", "")).startswith("C35"):
                    c["does_not_imply"] = []

        check(
            "explicit `does_not_imply: []` is accepted as a decision",
            "MISSING" not in _run(_fixture(tmp, "d", empty)),
        )
        check("silent on a non-ledger file", _run("README.md") == "")

    print(f"\n{'ALL CONTROLS PASS' if not failures else 'FAILURES: ' + ', '.join(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
