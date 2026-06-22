"""Markdown claim audit — regression guard against public-facing overclaims.

Scans README, PROJECT_CURRENT_STATE, and experiment reports/summaries for
forbidden phrases that violate the project's hard fences:

    λ = FREE_COUPLING_PARAMETER  (never fixed, never claimed)
    research_only = yes          (no physical promotion)
    S³×S¹ solved = no
    tom_ansatz solved = no

A line is exempt if it contains a negation marker (NOT, no, ≠, FORBIDDEN, never,
blocked, does not). This allows "What This Does NOT Mean" sections and fence
declarations to use the forbidden phrases without triggering the test.

Audit files: README.md, PROJECT_CURRENT_STATE.md, experiment *_report.md,
*executive_summary.md. Excludes anti-hallucination audit logs and claim.md
pre-registrations (those are spec documents, not public claims).

Added: 2026-06-11 (Codex audit finding #5)
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]  # tom_s3_spinor_toy/

# --- Files to audit ---------------------------------------------------------


def _collect_audit_files() -> list[Path]:
    targets: list[Path] = [
        PROJECT_ROOT / "README.md",  # tom_s3_spinor_toy/README.md
        PROJECT_ROOT / "RESEARCH_STATUS_REPORT.md",
        PROJECT_ROOT / "preprint_abstract.md",
    ]
    exp_root = PROJECT_ROOT / "experiments"
    for pattern in ("**/*_report.md", "**/*executive_summary.md"):
        for p in sorted(exp_root.glob(pattern)):
            # Skip meta-audit logs — they discuss forbidden phrases explicitly
            if "anti_hallucination" in p.name or "audit" in p.name.lower():
                continue
            targets.append(p)
    return [p for p in targets if p.exists()]


AUDIT_FILES = _collect_audit_files()

# --- Forbidden phrases -------------------------------------------------------
# (regex pattern, human-readable description)
# Match = overclaim. Line is exempt if NEGATION_MARKERS also match.

FORBIDDEN: list[tuple[str, str]] = [
    (
        r"validates\s+(?:the\s+)?(?:lattice\s+product\s+)?topology",
        "topology validation overclaim (use: detects a product-structure pattern)",
    ),
    (
        r"KK\s+bridge\s+mechanism\s+works",
        "KK mechanism works overclaim (use: proxy Kronecker-sum check passes)",
    ),
    (r"\bS.3.{0,5}S.1\b.*\bsolved\b", "S³×S¹ solved claim"),
    (r"\blambda\s+(?:is\s+)?fixed\b", "lambda fixed claim (λ = FREE_COUPLING_PARAMETER always)"),
    (r"\bλ\s+(?:is\s+)?fixed\b", "λ fixed claim (unicode form)"),
    (r"\btom(?:'s)?\s+ansatz\b.*\bsolved\b", "Tom ansatz solved claim"),
    (r"\bH-T1\s+confirmed\b", "H-T1 confirmed claim"),
    (r"\beq\.?\s*49\b.*\b(?:derived|solved|confirmed)\b", "eq.49 derived/solved/confirmed claim"),
    (r"\btrue\s+geometry\s+is\b", "true geometry claim"),
    (r"\bφ.?1[,_]?1\b.*\bidentified\s+as\s+full\s+mode\b", "φ₁₁ full mode identification claim"),
    (
        r"\bphysical\s+promotion\b(?!\s*[=:]\s*(?:no|none|blocked|False))",
        "physical promotion claim (must be denied, not asserted)",
    ),
]

# A line matching any of these is treated as negation context → exempt
NEGATION_RE = re.compile(
    r"(?:"
    r"\b(?:not?|no|never|blocked|forbidden|does\s+not|overclaim|removed|absent|free|killed|cannot)\b"
    r"|≠"  # Unicode not-equal — \b doesn't work around non-ASCII
    r"|PASS\s*≠"  # common fence form: "PASS ≠ solved"
    r")",
    re.IGNORECASE,
)

# --- Test -------------------------------------------------------------------


def _violations(path: Path) -> list[tuple[int, str, str]]:
    hits: list[tuple[int, str, str]] = []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    for lineno, line in enumerate(lines, start=1):
        if NEGATION_RE.search(line):
            continue  # line has explicit negation — exempt
        for pattern, description in FORBIDDEN:
            if re.search(pattern, line, re.IGNORECASE):
                hits.append((lineno, description, line.strip()[:140]))
    return hits


@pytest.mark.parametrize(
    "audit_path",
    AUDIT_FILES,
    ids=lambda p: p.relative_to(PROJECT_ROOT).as_posix(),
)
def test_no_overclaim_phrases(audit_path: Path) -> None:
    """Fail if any forbidden overclaim phrase appears outside negation context."""
    violations = _violations(audit_path)
    if violations:
        lines = "\n".join(f"  line {ln}: [{desc}]\n    → {text}" for ln, desc, text in violations)
        pytest.fail(f"Overclaim phrase(s) in {audit_path.relative_to(PROJECT_ROOT)}:\n{lines}")
