"""Repo-wide scan for the Clifford sign-convention mixing OB10 hit.

WHAT THIS IS FOR. C32/pearl 2026-08-09 recorded that two long-standing
sub-projects carry OPPOSITE Clifford sign conventions --

    S3 side  (round67 and descendants):  Z_i = i*sigma_i,  {Z_i,Z_j} = -2 delta   -> Cl(0,n)
    S6 side  (s6-harm-g0, dolan-casimir): Gamma_a hermitian, {G_a,G_b} = +2 delta -> Cl(n,0)

-- and that OB10 was the FIRST round ever to combine them, silently producing
a mixed Cl(6,3) signature that was then reported as a geometric finding. The
pearl's own next-check said the repo-wide audit had NOT been run. This is it.

WHAT IT DOES NOT CLAIM. A file using ONE convention is not a finding: both are
legitimate in isolation, and the choice is free as long as it is uniform
within a construction. The finding condition is MIXING -- a single file (or a
single import chain) that combines objects built under BOTH, because that is
where a signature/reality-type verdict silently becomes convention-dependent.

METHOD (three passes, each independently reported):
  PASS 1  classify every .py by the Clifford anticommutator sign it asserts,
          read off the ACTUAL assertion targets in the source, not from
          docstring prose (prose was wrong at least once -- see round34).
  PASS 2  flag files carrying BOTH signs, then check whether they actually
          COMBINE the two (kron/tensor/matmul) or merely mention both (an
          audit or a comparison file legitimately does the latter).
  PASS 3  follow cross-directory import edges and flag any edge that crosses
          the convention boundary -- a file can inherit a foreign convention
          without ever naming it.

NEGATIVE CONTROL. The scanner must FIND the two known cases (OB10's original
ob10_reality_structure.py = MIXED, and convention_correction.py = MIXED by
design, it is the file that diagnoses the mixing). If it reports zero mixed
files, the scanner is broken, not the repo clean.
"""

from __future__ import annotations

import ast
import json
import re
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
RESULTS_PATH = HERE / "results_clifford_convention_scan.json"

SCAN_ROOTS = ["experiments", "scripts", "tests"]

# --- convention detectors -----------------------------------------------------
# WHY regex on assertion TARGETS rather than on docstring prose: round34's own
# docstring says "Cl(7,0) (7 anticommuting generators squaring to -1)", which is
# self-contradictory -- generators squaring to -1 is Cl(0,7). The code asserts
# `-2 * sp.eye(N)`, so the CODE is Cl(0,7) and the LABEL is wrong. Prose lies;
# the assertion target does not.

NEG_PATTERNS = [
    r"-\s*2\s*\*\s*(sp\.)?eye",
    r"-\s*2\s*\*\s*np\.eye",
    r"-\s*2\s*\*\s*I\d?\b",
    r"-\s*2\s*\*\s*Id\b",
    r"-\s*2\s*\*?\s*delta",
    r"-2\s*delta",
    r"=\s*-\s*2\s*\*\s*\(?1 if",
    r"Cl\(0\s*,",
    r"i\s*\*\s*sigma_i",
    r"Z_i\s*=\s*i\*sigma",
]
POS_PATTERNS = [
    r"(?<![-\w])\+?\s*2\s*\*\s*(sp\.)?eye",
    r"(?<![-\w])\+?\s*2\s*\*\s*np\.eye",
    r"(?<![-\w])\+\s*2\s*\*?\s*delta",
    r"\+2\s*delta",
    r"Cl\(6\s*,\s*0\)",
    r"Cl\(7\s*,\s*0\)",
    r"Cl\(8\s*,\s*0\)",
    r"Cl\(9\s*,\s*0\)",
]
# a line only counts if it is ALSO about the Clifford relation, not any random
# `2*np.eye` used as an ordinary matrix somewhere
CLIFFORD_CONTEXT = re.compile(
    r"anticomm|anti_comm|\{Z|\{G|\{e_|\{Gamma|\{L_|clifford|Cl\(\d|gamma|Gamma|Z_i|Z\[",
    re.IGNORECASE,
)

# WHY this exists: the first run of this scanner reported g102_spin8_fiber.py as
# MIXED. It is not. Its check reads `{G_a,G_b} + 2 delta_ab I` and requires the
# result to be ZERO -- which asserts {G,G} = -2 delta, the NEGATIVE convention.
# A RESIDUAL written as `<anticommutator> + 2*delta` means the opposite of what
# the bare `+2` looks like. Caught by reading the file the scanner accused, per
# audit-verification-gate.md; the scanner's own verdict was the false positive.
RESIDUAL_FORM_RE = re.compile(
    r"(\}|\)|\bac\b|\banticomm\w*\b|gj\s*@\s*gi|\[j\]\s*\*\s*\w+\[i\])\s*\+\s*2"
    r"|\+\s*2\.?0?\s*\*\s*\(?1\.?0?\s+if"
)

NEG_RE = [re.compile(p) for p in NEG_PATTERNS]
POS_RE = [re.compile(p) for p in POS_PATTERNS]

COMBINE_RE = re.compile(
    r"\bkron\b|np\.kron|sp\.kronecker_product|TensorProduct|\bmatmul\b|@\s*[A-Z]"
)


def classify_file(path: Path) -> dict:
    """Return the Clifford sign evidence found in one file, with line numbers."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}
    neg_hits, pos_hits = [], []
    for lineno, line in enumerate(text.splitlines(), start=1):
        if not CLIFFORD_CONTEXT.search(line):
            continue
        residual = bool(RESIDUAL_FORM_RE.search(line))
        if any(r.search(line) for r in NEG_RE) or residual:
            neg_hits.append((lineno, line.strip()[:110]))
        if any(r.search(line) for r in POS_RE) and not residual:
            pos_hits.append((lineno, line.strip()[:110]))
    if not neg_hits and not pos_hits:
        return {}
    if neg_hits and pos_hits:
        conv = "MIXED"
    elif neg_hits:
        conv = "NEG_Cl(0,n)"
    else:
        conv = "POS_Cl(n,0)"
    return {
        "convention": conv,
        "neg_hits": neg_hits,
        "pos_hits": pos_hits,
        "combines": bool(COMBINE_RE.search(text)),
    }


def cross_dir_imports(path: Path) -> list[str]:
    """Directories other than this file's own that it loads modules from.

    WHY textual, not import-graph: these scripts load siblings via
    sys.path.insert / spec_from_file_location with a computed path, so a real
    import resolver would have to execute them. The path literal is enough.
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    targets = set()
    for m in re.finditer(r'["\'](?:\.\./|experiments/)?(\d{8}-[A-Za-z0-9_.-]+)["\']', text):
        targets.add(m.group(1))
    for m in re.finditer(r'parent\s*/\s*["\'](\d{8}-[A-Za-z0-9_.-]+)["\']', text):
        targets.add(m.group(1))
    own = path.parent.name
    return sorted(t for t in targets if t != own)


print("=" * 78)
print("Repo-wide Clifford sign-convention scan (the audit the 08-09 pearl deferred)")
print("=" * 78)

files: list[Path] = []
for root in SCAN_ROOTS:
    rp = REPO / root
    if rp.is_dir():
        files.extend(sorted(rp.rglob("*.py")))
print(f"\nScanned roots: {SCAN_ROOTS}  ->  {len(files)} python files")

results: dict = {"n_files_scanned": len(files)}

# --- PASS 1 -------------------------------------------------------------------
classified: dict[str, dict] = {}
for f in files:
    info = classify_file(f)
    if info:
        classified[str(f.relative_to(REPO)).replace("\\", "/")] = info

by_conv: dict[str, list[str]] = defaultdict(list)
for rel, info in classified.items():
    by_conv[info["convention"]].append(rel)

print("\nPASS 1 -- convention by ASSERTED anticommutator sign (not by docstring prose)")
for conv in ("NEG_Cl(0,n)", "POS_Cl(n,0)", "MIXED"):
    print(f"  {conv:14s} {len(by_conv[conv]):3d} files")
results["pass1_counts"] = {k: len(v) for k, v in by_conv.items()}
results["pass1_by_convention"] = {k: sorted(v) for k, v in by_conv.items()}

# --- PASS 2 -------------------------------------------------------------------
print("\nPASS 2 -- files carrying BOTH signs: do they COMBINE, or only compare?")
mixed_detail = {}
for rel in sorted(by_conv["MIXED"]):
    info = classified[rel]
    mixed_detail[rel] = {
        "combines_tensor_or_matmul": info["combines"],
        "neg_example": info["neg_hits"][0] if info["neg_hits"] else None,
        "pos_example": info["pos_hits"][0] if info["pos_hits"] else None,
        "n_neg": len(info["neg_hits"]),
        "n_pos": len(info["pos_hits"]),
    }
    flag = "COMBINES" if info["combines"] else "mentions-only"
    print(f"  [{flag:13s}] {rel}")
results["pass2_mixed_files"] = mixed_detail

# --- PASS 3 -------------------------------------------------------------------
print("\nPASS 3 -- cross-directory import edges that CROSS the convention boundary")
dir_conv: dict[str, set[str]] = defaultdict(set)
for rel, info in classified.items():
    dir_conv[Path(rel).parent.name].add(info["convention"])


def dir_side(d: str) -> str:
    convs = dir_conv.get(d, set())
    if not convs:
        return "UNKNOWN"
    if "MIXED" in convs or ("NEG_Cl(0,n)" in convs and "POS_Cl(n,0)" in convs):
        return "MIXED"
    return next(iter(convs))


crossing = []
for f in files:
    rel = str(f.relative_to(REPO)).replace("\\", "/")
    src_side = dir_side(f.parent.name)
    if src_side in ("UNKNOWN", "MIXED"):
        continue
    for tgt in cross_dir_imports(f):
        tgt_side = dir_side(tgt)
        if tgt_side in ("UNKNOWN", "MIXED"):
            continue
        if tgt_side != src_side:
            crossing.append(
                {"file": rel, "file_side": src_side, "imports": tgt, "target_side": tgt_side}
            )

if crossing:
    for c in crossing:
        print(f"  {c['file']}  [{c['file_side']}]  <-  {c['imports']}  [{c['target_side']}]")
else:
    print("  none found")
results["pass3_boundary_crossing_imports"] = crossing

# --- NEGATIVE CONTROL ---------------------------------------------------------
print("\nNEGATIVE CONTROL -- the scanner must find the two KNOWN mixed files")
known = [
    "tom_s3_spinor_toy/experiments/20260803-ob10-ko-dimension-majorana-check/ob10_reality_structure.py",
    "tom_s3_spinor_toy/experiments/20260809-ob10-convention-correction/convention_correction.py",
]
found_known = {}
for k in known:
    tail = k.split("/", 1)[1] if k.startswith("tom_s3_spinor_toy/") else k
    hit = next((r for r in classified if r.endswith(tail)), None)
    conv = classified[hit]["convention"] if hit else "NOT-DETECTED"
    found_known[tail] = conv
    print(f"  {conv:12s}  {tail}")
control_passes = all(v == "MIXED" for v in found_known.values())
print(f"  CONTROL PASSES (both detected as MIXED): {control_passes}")
results["negative_control_known_mixed"] = found_known
results["negative_control_passes"] = bool(control_passes)

# --- AST cross-check on the combining question --------------------------------
# WHY a second method: the COMBINE_RE above is a regex on the whole file, which
# says "this file contains a kron somewhere", NOT "this file krons an object
# from each convention". For the MIXED files only, re-check by parsing and
# reporting which names are actually passed to kron/TensorProduct.
print("\nCROSS-CHECK (AST) -- what the MIXED files actually pass to kron/tensor")
ast_detail = {}
for rel in sorted(by_conv["MIXED"]):
    p = REPO / rel
    try:
        tree = ast.parse(p.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        ast_detail[rel] = ["<unparseable>"]
        continue
    args: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            fn = node.func
            name = getattr(fn, "attr", None) or getattr(fn, "id", None)
            if name in ("kron", "TensorProduct", "kronecker_product"):
                for a in node.args:
                    if isinstance(a, ast.Name):
                        args.append(a.id)
                    elif isinstance(a, ast.Subscript) and isinstance(a.value, ast.Name):
                        args.append(a.value.id + "[]")
    uniq = sorted(set(args))
    ast_detail[rel] = uniq
    print(f"  {rel}\n      kron args: {uniq}")
results["ast_kron_args_in_mixed_files"] = ast_detail

RESULTS_PATH.write_text(json.dumps(results, indent=2))
print(f"\nResults -> {RESULTS_PATH}")
