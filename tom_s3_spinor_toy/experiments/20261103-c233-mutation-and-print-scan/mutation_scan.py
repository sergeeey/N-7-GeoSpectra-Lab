"""C233a: automatic mutation testing of the Tom-line scripts.

For each target script, a seeded sample of AST mutation sites is mutated one at a time (operators: binary + <-> -, removal of a
unary minus, a small integer constant 2..4 changed by +1); the mutant is run in a temporary copy of the script's folder with a time
limit. Classification of a mutant:
  KILLED    exit code != 0 AND the output contains a FAIL/MISSED marker (a check noticed)
  CRASHED   exit code != 0 without such a marker (the mutant broke the script; NOT counted as a kill by a check)
  SURVIVED  exit code 0 and no FAIL/MISSED marker (no check noticed; may be an equivalent mutant, to be triaged by hand)
  TIMEOUT   exceeded the limit
Usage: python mutation_scan.py <seed> <k_per_file> <timeout_s> script1.py script2.py ...   writes mutation_report.json next to this file.
Original scripts are never modified.
"""

import ast
import json
import random
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent


class Sites(ast.NodeVisitor):
    def __init__(self):
        self.sites = []

    def visit_BinOp(self, node):
        if isinstance(node.op, (ast.Add, ast.Sub)):
            self.sites.append(("binop", node.lineno, node))
        self.generic_visit(node)

    def visit_UnaryOp(self, node):
        if isinstance(node.op, ast.USub):
            self.sites.append(("unary-minus", node.lineno, node))
        self.generic_visit(node)

    def visit_Constant(self, node):
        if type(node.value) is int and node.value in (2, 3, 4):
            self.sites.append(("const", node.lineno, node))
        self.generic_visit(node)


class Apply(ast.NodeTransformer):
    def __init__(self, target):
        self.target = target

    def visit_BinOp(self, node):
        self.generic_visit(node)
        if node is self.target:
            node.op = ast.Sub() if isinstance(node.op, ast.Add) else ast.Add()
        return node

    def visit_UnaryOp(self, node):
        self.generic_visit(node)
        if node is self.target:
            return node.operand
        return node

    def visit_Constant(self, node):
        if node is self.target:
            return ast.copy_location(ast.Constant(node.value + 1), node)
        return node


def run_mutant(src_dir, fname, new_src, timeout):
    with tempfile.TemporaryDirectory() as td:
        d = Path(td) / "w"
        shutil.copytree(
            src_dir, d, ignore=shutil.ignore_patterns("run_output*", "__pycache__", "*.txt")
        )
        (d / fname).write_text(new_src, encoding="utf-8")
        t0 = time.time()
        try:
            p = subprocess.run(
                [sys.executable, fname],
                cwd=d,
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=timeout,
            )
        except subprocess.TimeoutExpired:
            return "TIMEOUT", time.time() - t0
        out = p.stdout + p.stderr
        marker = re.search(r"^(FAIL|MISSED)\b(?!S)", out, re.M) is not None or "FAILS: [" in out
        if p.returncode == 0 and not marker:
            return "SURVIVED", time.time() - t0
        if p.returncode != 0 and marker:
            return "KILLED", time.time() - t0
        if p.returncode == 0 and marker:
            return "KILLED", time.time() - t0
        return "CRASHED", time.time() - t0


def main(argv):
    seed, k, timeout = int(argv[1]), int(argv[2]), int(argv[3])
    files = [Path(f) for f in argv[4:]]
    rng = random.Random(seed)
    report = []
    for f in files:
        src = f.read_text(encoding="utf-8")
        tree = ast.parse(src)
        v = Sites()
        v.visit(tree)
        picks = rng.sample(range(len(v.sites)), min(k, len(v.sites)))
        for idx in sorted(picks):
            kind, line, _ = v.sites[idx]
            tree2 = ast.parse(src)
            v2 = Sites()
            v2.visit(tree2)
            target = v2.sites[idx][2]
            new_tree = Apply(target).visit(tree2)
            ast.fix_missing_locations(new_tree)
            new_src = ast.unparse(new_tree)
            status, secs = run_mutant(f.parent, f.name, new_src, timeout)
            seg = src.splitlines()[line - 1].strip()[:90]
            rec = {
                "file": f.parent.name + "/" + f.name,
                "line": line,
                "kind": kind,
                "status": status,
                "seconds": round(secs, 1),
                "source_line": seg,
            }
            report.append(rec)
            print(json.dumps(rec, ensure_ascii=False), flush=True)
    (HERE / "mutation_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    from collections import Counter

    print("SUMMARY", dict(Counter(r["status"] for r in report)))


if __name__ == "__main__":
    main(sys.argv)
