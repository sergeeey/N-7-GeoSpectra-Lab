#!/usr/bin/env python3
"""Mechanical integrity lint for CLAIM_LEDGER.yaml (and DERIVATION_GRAPH.yaml).

What it checks (errors -> exit code 1):
  L0  the ledger declares ``schema.required`` and ``schema.enums``, and the
      enums cover all five status fields (truth_status, test_outcome,
      execution_status, evidence_status, lifecycle_status)
  L1  every claim has all fields listed in ``schema.required`` (a YAML null or
      empty string counts as missing)
  L2  enum fields use only values declared in ``schema.enums`` (the single
      source of truth lives in the ledger, not in this script)
  L3  claim ids are unique
  L4  ``depends_on`` is a list of existing ids, with no self-dependency
  L5  the ``depends_on`` graph is acyclic
  L6  every RECOGNISED reference in ``evidence_file`` points at something that
      exists, and any ``:line`` / ``:a-b`` reference is a valid range inside
      the file (globs are only checked for at least one match)
  L7  every premise ``claim:`` in DERIVATION_GRAPH.yaml is a ledger id
  L8  no mapping in either YAML file repeats a key (``yaml.safe_load`` silently
      keeps the last value, so the earlier one would be lost without notice)

Advisory checks (``--advisory``; never change the exit code):
  A1  a PROVED/SUPPORTED claim whose test_outcome is FAIL/CONFLICTING
  A2  an ACTIVE PROVED/SUPPORTED claim that depends on a premise which is
      REFUTED / SUPERSEDED / RETIRED / FAIL / CONTESTED

Why A1/A2 are advisory and not errors: in this ledger ``truth_status`` is often
the status of the ORIGINAL HYPOTHESIS ("REFUTED as worded"), while the entry
records the negative FINDING, and later claims legitimately build on that
finding. On 2026-10-03 the entries behind C3, C14, C27 and C45 were read and
were of this kind; the remaining hits were not each read. Until the schema
separates hypothesis-status from finding-status, A1/A2 are prompts for a
human, not defects.

What "recognised reference" means (stated so L6 is not over-read): only
tokens ending in a known file extension (case-insensitive, see ``_EXTS``) or
in ``/`` (a directory) are recognised; URLs are ignored. A malformed token
next to a valid one is NOT reported, because it is not recognised. A reference
that exists under both the repo root and ``tom_s3_spinor_toy/`` is line-checked
against the repo-root copy. L6 only proves existence/range, not that the cited
lines support the claim.

Usage:
    python scripts/lint_claim_ledger.py [--ledger PATH] [--graph PATH]
                                        [--advisory] [--tracked]

``--tracked`` additionally requires every referenced file to be tracked in git
with exactly the spelled case (a Windows checkout is case-insensitive and also
sees untracked files, so a ledger can pass locally and fail on a Linux CI).

Scope limit, stated plainly: this checks that the ledger is well-formed and its
references resolve. It says nothing about whether any claim is TRUE.
"""

from __future__ import annotations

import argparse
import glob
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
PROJECT_DIR = HERE.parent  # tom_s3_spinor_toy/
REPO_ROOT = PROJECT_DIR.parent  # N-7-GeoSpectra-Lab/

STATUS_FIELDS = (
    "truth_status",
    "test_outcome",
    "execution_status",
    "evidence_status",
    "lifecycle_status",
)

_EXTS = "md|py|yaml|yml|json|tex|txt|pdf|csv|npz|npy|ipynb|toml|cfg|ini|sh|log|html|bib|lean|png|jpg|svg"
# path[:a[-b]] where path ends in a known extension (a file) or in "/" (a
# directory); globs (*) allowed. Two guards against prose: the first lookahead
# requires a letter ("31/31 tests" is not the directory "31/"), and a directory
# slash must not be continued by a path character ("and/or" is not "and/").
_REF_RE = re.compile(
    r"(?P<path>(?=[\w./*\\\-]*[A-Za-z])[\w./*\\\-]+"
    rf"(?:\.(?i:{_EXTS})|/(?![\w./*\\\-])))"
    r"(?::(?P<a>\d+)(?:-(?P<b>\d+))?)?"
)
_URL_RE = re.compile(r"https?://\S+")

_BAD_PREMISE_TRUTH = {"REFUTED"}
_BAD_PREMISE_LIFECYCLE = {"SUPERSEDED", "RETIRED"}
_BAD_PREMISE_TEST = {"FAIL", "CONFLICTING"}
_BAD_PREMISE_EVIDENCE = {"INVALIDATED", "CONTESTED"}


@dataclass(frozen=True)
class Finding:
    code: str
    claim_id: str
    message: str

    def __str__(self) -> str:
        return f"[{self.code}] {self.claim_id}: {self.message}"


@dataclass
class LintReport:
    errors: list[Finding] = field(default_factory=list)
    advisories: list[Finding] = field(default_factory=list)
    n_claims: int = 0

    def error_codes(self) -> set[str]:
        return {f.code for f in self.errors}


@dataclass(frozen=True)
class EvidenceRef:
    path: str
    start: int | None
    end: int | None


# ---------------------------------------------------------------- YAML loading
class _DupKeyLoader(yaml.SafeLoader):
    """SafeLoader that records repeated mapping keys instead of dropping them silently."""

    def __init__(self, stream):
        super().__init__(stream)
        self.duplicate_keys: list[tuple[int, str]] = []  # (1-based line, key)

    def construct_mapping(self, node, deep=False):
        keys = []
        for key_node, _ in node.value:
            if key_node.tag == "tag:yaml.org,2002:merge":
                continue
            key = self.construct_object(key_node, deep=True)
            try:
                hash(key)
            except TypeError:
                continue  # unhashable key: the base class reports it with its own error
            keys.append((key, key_node.start_mark.line + 1))
        counts = Counter(k for k, _ in keys)
        for key, line in keys:
            if counts[key] > 1:
                self.duplicate_keys.append((line, str(key)))
        return super().construct_mapping(node, deep=deep)


def load_yaml_text(text: str) -> tuple[object, list[tuple[int, str]]]:
    """Parse YAML; returns (data, repeated keys as (line, key))."""
    loader = _DupKeyLoader(text)
    try:
        data = loader.get_single_data()
    finally:
        loader.dispose()
    return data, loader.duplicate_keys


def load_yaml_file(path: Path) -> tuple[object, list[tuple[int, str]]]:
    return load_yaml_text(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- references
def parse_evidence_refs(text: str) -> list[EvidenceRef]:
    """Extract recognised file/directory references from an ``evidence_file`` value."""
    refs = []
    for m in _REF_RE.finditer(_URL_RE.sub(" ", str(text))):
        a = int(m.group("a")) if m.group("a") else None
        b = int(m.group("b")) if m.group("b") else a
        refs.append(EvidenceRef(m.group("path"), a, b))
    return refs


def _resolve(ref_path: str, roots: list[Path]) -> list[Path]:
    """All existing paths matching ``ref_path`` under any root (glob-aware)."""
    hits: list[Path] = []
    for root in roots:
        if "*" in ref_path:
            hits.extend(Path(p) for p in glob.glob(str(root / ref_path)))
        elif (root / ref_path).exists():
            hits.append(root / ref_path)
    return hits


def _is_tracked(hit: Path, tracked: set[str], repo_root: Path) -> bool:
    try:
        rel = hit.relative_to(repo_root).as_posix()
    except ValueError:
        return False
    if hit.is_dir():
        return any(t.startswith(rel.rstrip("/") + "/") for t in tracked)
    return rel in tracked


def _line_count(path: Path) -> int:
    with open(path, encoding="utf-8", errors="replace") as fh:
        return sum(1 for _ in fh)


def _find_cycles(deps: dict[str, list[str]]) -> list[list[str]]:
    """Depth-first search; returns one id path per back-edge found."""
    cycles: list[list[str]] = []
    state: dict[str, int] = {}  # 1 = on the current path, 2 = finished

    def visit(node: str, stack: list[str]) -> None:
        state[node] = 1
        for nxt in deps.get(node, []):
            if nxt not in deps or nxt == node:
                continue  # dangling / self-dependency: reported by L4, not L5
            if state.get(nxt) == 1:
                start = stack.index(nxt) if nxt in stack else 0
                cycles.append([*stack[start:], node, nxt])
            elif nxt not in state:
                visit(nxt, [*stack, node])
        state[node] = 2

    for node in deps:
        if node not in state:
            visit(node, [])
    return cycles


def _is_empty(value: object) -> bool:
    return value is None or (isinstance(value, str) and not value.strip())


# ---------------------------------------------------------------- the lint
def lint_ledger(
    ledger: dict,
    graph: dict | None = None,
    roots: list[Path] | None = None,
    *,
    ledger_dups: list[tuple[int, str]] | None = None,
    graph_dups: list[tuple[int, str]] | None = None,
    tracked: set[str] | None = None,
    repo_root: Path | None = None,
) -> LintReport:
    """Lint an already-loaded ledger (and optional derivation graph)."""
    roots = roots if roots is not None else [REPO_ROOT, PROJECT_DIR]
    repo_root = repo_root if repo_root is not None else REPO_ROOT
    rep = LintReport()
    claims = ledger.get("claims") or []
    rep.n_claims = len(claims)

    for line, key in ledger_dups or []:
        rep.errors.append(
            Finding(
                "L8",
                f"<ledger line {line}>",
                f"duplicate key '{key}' (last value silently wins)",
            )
        )
    for line, key in graph_dups or []:
        rep.errors.append(
            Finding(
                "L8",
                f"<graph line {line}>",
                f"duplicate key '{key}' (last value silently wins)",
            )
        )

    schema = ledger.get("schema") or {}
    required = [f for f in (schema.get("required") or []) if isinstance(f, str)]
    enums = {k: set(v) for k, v in (schema.get("enums") or {}).items()}
    if not required:
        rep.errors.append(
            Finding("L0", "<schema>", "ledger has no schema.required list")
        )
    if not enums:
        rep.errors.append(
            Finding("L0", "<schema>", "ledger has no schema.enums mapping")
        )
    else:
        for f in STATUS_FIELDS:
            if f not in enums:
                rep.errors.append(
                    Finding("L0", "<schema>", f"schema.enums has no entry for '{f}'")
                )

    entries = [c for c in claims if isinstance(c, dict)]
    for _ in range(len(claims) - len(entries)):
        rep.errors.append(Finding("L1", "<entry>", "claim entry is not a mapping"))
    by_id = {c["id"]: c for c in entries if c.get("id")}

    seen: set[str] = set()
    for c in entries:
        cid = c.get("id")
        if cid in seen:
            rep.errors.append(Finding("L3", str(cid), "duplicate claim id"))
        seen.add(cid)

    deps: dict[str, list[str]] = {}
    for c in entries:
        cid = str(c.get("id", "<no id>"))

        for f in required:
            # an empty depends_on list is legitimate; any other empty value is not
            if f == "depends_on" and c.get(f) == []:
                continue
            if f not in c or _is_empty(c[f]):
                rep.errors.append(
                    Finding("L1", cid, f"missing or empty required field '{f}'")
                )

        for f, allowed in enums.items():
            # None is reported once, by L1 (e.g. an unquoted YAML NULL), not twice
            if f in c and c[f] is not None and c[f] not in allowed:
                rep.errors.append(
                    Finding(
                        "L2",
                        cid,
                        f"{f}={c[f]!r} is not in schema.enums.{f} {sorted(allowed)}",
                    )
                )

        dep_list = c.get("depends_on", [])
        if dep_list is None:
            dep_list = []  # a null depends_on is already reported by L1
        elif not isinstance(dep_list, list):
            rep.errors.append(
                Finding(
                    "L4", cid, f"depends_on is {type(dep_list).__name__}, not a list"
                )
            )
            dep_list = []
        deps[cid] = [d for d in dep_list if isinstance(d, str)]
        for d in dep_list:
            if not isinstance(d, str):
                rep.errors.append(
                    Finding("L4", cid, f"depends_on entry {d!r} is not a string id")
                )
            elif d == cid:
                rep.errors.append(Finding("L4", cid, "depends on itself"))
            elif d not in by_id:
                rep.errors.append(
                    Finding("L4", cid, f"depends_on unknown claim id '{d}'")
                )

        ev = c.get("evidence_file")
        if not _is_empty(ev):
            refs = parse_evidence_refs(ev)
            if not refs:
                rep.errors.append(
                    Finding("L6", cid, "evidence_file has no recognizable file path")
                )
            for r in refs:
                hits = _resolve(r.path, roots)
                if tracked is not None:
                    hits = [h for h in hits if _is_tracked(h, tracked, repo_root)]
                if not hits:
                    where = (
                        "not found"
                        if tracked is None
                        else "not found / not tracked (exact case)"
                    )
                    rep.errors.append(
                        Finding("L6", cid, f"evidence file {where}: {r.path}")
                    )
                elif r.start is not None and "*" not in r.path and hits[0].is_file():
                    n = _line_count(hits[0])
                    if r.start > r.end:
                        rep.errors.append(
                            Finding(
                                "L6",
                                cid,
                                f"{r.path}:{r.start}-{r.end} is a reversed line range",
                            )
                        )
                    elif r.end > n:
                        rep.errors.append(
                            Finding(
                                "L6",
                                cid,
                                f"{r.path}:{r.start}-{r.end} is past end of file ({n} lines)",
                            )
                        )

        truth, outcome = c.get("truth_status"), c.get("test_outcome")
        if truth in {"PROVED", "SUPPORTED"} and outcome in _BAD_PREMISE_TEST:
            rep.advisories.append(
                Finding(
                    "A1",
                    cid,
                    f"truth_status={truth} with test_outcome={outcome} (negative finding?)",
                )
            )

    for cyc in _find_cycles(deps):
        rep.errors.append(
            Finding("L5", cyc[0], "dependency cycle: " + " -> ".join(cyc))
        )

    for c in entries:
        if c.get("lifecycle_status") == "ACTIVE" and c.get("truth_status") in {
            "PROVED",
            "SUPPORTED",
        }:
            for d in deps.get(str(c.get("id")), []):
                p = by_id.get(d)
                if p is not None and (
                    p.get("truth_status") in _BAD_PREMISE_TRUTH
                    or p.get("lifecycle_status") in _BAD_PREMISE_LIFECYCLE
                    or p.get("test_outcome") in _BAD_PREMISE_TEST
                    or p.get("evidence_status") in _BAD_PREMISE_EVIDENCE
                ):
                    rep.advisories.append(
                        Finding(
                            "A2",
                            str(c["id"]),
                            f"{c['truth_status']} claim rests on {d} "
                            f"(truth={p.get('truth_status')}, test={p.get('test_outcome')})",
                        )
                    )

    if graph is not None:
        seen_deriv: set[str] = set()
        for der in graph.get("derivations") or []:
            did = str(der.get("derivation_id", "<no derivation_id>"))
            if did in seen_deriv:
                rep.errors.append(Finding("L7", did, "duplicate derivation_id"))
            seen_deriv.add(did)
            for prem in der.get("premises") or []:
                cid = prem.get("claim") if isinstance(prem, dict) else None
                if cid not in by_id:
                    rep.errors.append(
                        Finding("L7", did, f"premise claim '{cid}' is not a ledger id")
                    )
    return rep


def _git_tracked(repo_root: Path) -> set[str]:
    out = subprocess.run(
        ["git", "ls-files"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    return set(out.stdout.splitlines())


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Mechanical lint of CLAIM_LEDGER.yaml")
    ap.add_argument("--ledger", type=Path, default=PROJECT_DIR / "CLAIM_LEDGER.yaml")
    ap.add_argument("--graph", type=Path, default=PROJECT_DIR / "DERIVATION_GRAPH.yaml")
    ap.add_argument(
        "--advisory", action="store_true", help="also print advisory (non-failing) hits"
    )
    ap.add_argument(
        "--tracked",
        action="store_true",
        help="require referenced files to be tracked in git with exactly the spelled case",
    )
    args = ap.parse_args(argv)

    ledger, ledger_dups = load_yaml_file(args.ledger)
    graph, graph_dups = (
        load_yaml_file(args.graph) if args.graph.exists() else (None, [])
    )
    tracked = None
    if args.tracked:
        try:
            tracked = _git_tracked(REPO_ROOT)
        except (OSError, subprocess.CalledProcessError) as exc:
            print(f"--tracked needs git: {exc}", file=sys.stderr)
            return 2
    rep = lint_ledger(
        ledger, graph, ledger_dups=ledger_dups, graph_dups=graph_dups, tracked=tracked
    )

    for f in rep.errors:
        print(f)
    if args.advisory:
        for f in rep.advisories:
            print(f)
    print(
        f"claims={rep.n_claims} errors={len(rep.errors)} advisories={len(rep.advisories)}"
        + ("" if args.advisory else " (advisories hidden; use --advisory)")
    )
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
