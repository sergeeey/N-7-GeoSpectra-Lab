"""
Methodology audit: checks Kill Analysis and caveats coverage across all experiments.
Run from repo root: python scripts/audit_methodology.py
"""

import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPERIMENTS_DIR = os.path.join(REPO, "experiments")
NULL_RESULTS_FILE = os.path.join(REPO, "null_results", "INDEX.md")
ALIVE_FILE = os.path.join(REPO, "ALIVE_BRANCHES.md")

# Keywords for Kill Analysis (REJECT experiments) — any one is sufficient
KILL_ANALYSIS_PATTERNS = [
    r"kill analysis",
    r"not killed",
    r"what was not",
    r"what.*ruled out",
    r"positive results.*that still stand",
    r"survived",
    r"does not mean",
    r"does not prove",
    r"not claim",
    r"not prove",
    r"what this does not",
    r"what.*not.*mean",
    r"what.*not.*claim",
    r"what.*not.*prove",
    r"limitations?",
    r"caveats?",
    r"scope.*restriction",
]

# Keywords for PROMOTE caveats — any one is sufficient
CAVEATS_PATTERNS = [
    r"does not mean",
    r"does not prove",
    r"not claim",
    r"not prove",
    r"what this does not",
    r"what.*not.*mean",
    r"what.*not.*claim",
    r"what.*not.*prove",
    r"what.*not.*show",
    r"what.*not.*establish",
    r"what's not",
    r"what is not",
    r"limitations?",
    r"caveats?",
    r"scope.*restriction",
    r"not.*imply",
    r"not.*establish",
]

# PROMOTE experiments that are significant enough to require caveats
KEY_PROMOTE_SLUGS = [
    "g62",
    "g73",
    "g74a",
    "g74b",
    "g75",
    "g67",
    "g66",
    "exhaustion",
    "h1-lambda",
]


def detect_verdict(content: str) -> str:
    low = content.lower()
    if any(
        k in low
        for k in [
            "verdict:** reject",
            "verdict: reject",
            "verdict:** null",
            "verdict: null",
            "verdict:** exhausted",
            "verdict:** weak",
            "verdict: weak",
        ]
    ):
        return "REJECT"
    if any(
        k in low
        for k in [
            "verdict:** promote",
            "verdict: promote",
            "verdict:** pass",
            "verdict: pass",
            "verdict:** confirm",
        ]
    ):
        return "PROMOTE"
    if "promote" in low:
        return "PROMOTE"
    if "reject" in low:
        return "REJECT"
    return "UNKNOWN"


def has_pattern(content: str, patterns: list[str]) -> bool:
    low = content.lower()
    return any(re.search(p, low) for p in patterns)


def audit_alive_branches() -> list[tuple[str, str]]:
    vague = []
    if not os.path.exists(ALIVE_FILE):
        return vague
    with open(ALIVE_FILE, encoding="utf-8", errors="ignore") as f:
        content = f.read()
    for line in content.split("\n"):
        if not line.startswith("|") or "OPEN" not in line:
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 6:
            continue
        branch_id = parts[1]
        next_falsifier = parts[5] if len(parts) > 5 else ""
        is_specific = any(
            k in next_falsifier
            for k in [
                "PASS",
                "FAIL",
                "=0",
                ">0",
                "<0",
                "∂",
                "∫",
                "sympy",
                "pytest",
                "PASS если",
                "FAIL если",
            ]
        )
        if not is_specific:
            vague.append((branch_id, next_falsifier[:70]))
    return vague


def run_audit() -> int:
    folders = sorted(
        [
            f
            for f in os.listdir(EXPERIMENTS_DIR)
            if os.path.isdir(os.path.join(EXPERIMENTS_DIR, f)) and not f.startswith("_")
        ]
    )

    reject_missing_kill: list[str] = []
    promote_missing_caveats: list[str] = []

    for folder in folders:
        dec_path = os.path.join(EXPERIMENTS_DIR, folder, "decision.md")
        if not os.path.exists(dec_path):
            # Missing decision.md entirely is a separate issue
            continue

        content = open(dec_path, encoding="utf-8", errors="ignore").read()
        verdict = detect_verdict(content)

        if verdict == "REJECT":
            if not has_pattern(content, KILL_ANALYSIS_PATTERNS):
                reject_missing_kill.append(folder)

        elif verdict == "PROMOTE":
            is_key = any(slug in folder.lower() for slug in KEY_PROMOTE_SLUGS)
            if is_key and not has_pattern(content, CAVEATS_PATTERNS):
                promote_missing_caveats.append(folder)

    vague_falsifiers = audit_alive_branches()

    # Report
    total = len(reject_missing_kill) + len(promote_missing_caveats) + len(vague_falsifiers)

    print("=== METHODOLOGY AUDIT ===")
    print(f"Experiments scanned: {len(folders)}")
    print()

    if reject_missing_kill:
        print(f"REJECT without Kill Analysis: {len(reject_missing_kill)}")
        for f in reject_missing_kill:
            print(f"  FAIL: {f}")
        print()
    else:
        print("REJECT Kill Analysis: ALL OK ✓")

    if promote_missing_caveats:
        print(f"\nKey PROMOTE without caveats: {len(promote_missing_caveats)}")
        for f in promote_missing_caveats:
            print(f"  WARN: {f}")
    else:
        print("Key PROMOTE caveats:    ALL OK ✓")

    if vague_falsifiers:
        print(f"\nALIVE_BRANCHES vague falsifiers: {len(vague_falsifiers)}")
        for bid, nf in vague_falsifiers:
            print(f'  WARN {bid}: "{nf}"')
    else:
        print("ALIVE_BRANCHES falsifiers: ALL OK ✓")

    print()
    if total == 0:
        print("RESULT: PASS — methodology clean")
    else:
        print(f"RESULT: NEEDS FIX — {total} issues found")

    return total


if __name__ == "__main__":
    issues = run_audit()
    sys.exit(1 if issues > 0 else 0)
