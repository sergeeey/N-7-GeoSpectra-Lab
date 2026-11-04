"""C233b: heuristic static scan for results that are printed but never tested.

For each script, every `print(...)` call is examined: the variable names that occur in its arguments are collected. A name is
'tested' if it also occurs inside an `assert`, a call to a function named check/expect_caught/ok/test*, an `if` test, or in the
value passed to sys.exit. A print is FLAGGED if it mentions at least one name and none of its names is tested anywhere.
This is a heuristic with false positives (a value can be tested through an alias); it only lists candidates for hand triage.
Usage: python print_only_scan.py script1.py script2.py ...      writes print_only_report.json next to this file
"""

import ast
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECK_FUNCS = {"check", "expect_caught", "ok", "assert_", "ensure"}


def names_in(node):
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}


def scan(path):
    src = Path(path).read_text(encoding="utf-8")
    tree = ast.parse(src)
    tested = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Assert):
            tested |= names_in(n.test)
        elif isinstance(n, ast.If):
            tested |= names_in(n.test)
        elif isinstance(n, ast.Call):
            fn = n.func
            name = fn.id if isinstance(fn, ast.Name) else getattr(fn, "attr", "")
            if name in CHECK_FUNCS or name.startswith("test"):
                for a in n.args + [k.value for k in n.keywords]:
                    tested |= names_in(a)
            if name == "exit":
                for a in n.args:
                    tested |= names_in(a)
    flagged, total = [], 0
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "print":
            total += 1
            used = set()
            for a in n.args:
                used |= names_in(a)
            used -= {"print", "len", "str", "sorted", "sp", "np", "sum", "range", "round"}
            if used and not (used & tested):
                flagged.append(
                    {
                        "line": n.lineno,
                        "names": sorted(used),
                        "text": src.splitlines()[n.lineno - 1].strip()[:110],
                    }
                )
    return {
        "file": str(Path(path).parent.name + "/" + Path(path).name),
        "prints": total,
        "flagged": flagged,
    }


def main(argv):
    rep = [scan(p) for p in argv[1:]]
    (HERE / "print_only_report.json").write_text(
        json.dumps(rep, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    for r in rep:
        print(f"{r['file']}: {r['prints']} print calls, {len(r['flagged'])} flagged")
        for f in r["flagged"]:
            print(f"   line {f['line']}: {f['text']}   names={f['names']}")


if __name__ == "__main__":
    main(sys.argv)
