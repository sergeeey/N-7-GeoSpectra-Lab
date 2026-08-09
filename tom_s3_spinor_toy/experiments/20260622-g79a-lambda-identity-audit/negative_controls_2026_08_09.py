"""Negative controls for the 2026-08-09 relaxations of classify_occurrence.

WHY THIS FILE EXISTS SEPARATELY FROM tests/: three rules were ADDED to the
classifier to clear genuine false-positives in the new `paper/` manuscript
directory (which postdates the audit). Relaxing a classifier is exactly the
move that can silently blind a guard, so each relaxation needs a control
proving it does NOT fire on a case the audit must still flag. `tests/` is
write-protected by project permission rules, so these live here and are run
manually; they SHOULD be moved into tests/test_g79a_lambda_identity_audit.py
once the user approves editing that directory.

The three relaxations under test:
  R1  LaTeX capital \\Lambda (exterior algebra) -> UNRELATED, case-sensitively,
      and only when the line carries no lowercase \\lambda and no bare lambda.
  R2  "free coupling parameter" (prose form) added to V_LINE_MARKERS; the
      audit previously knew only the underscored code identifier.
  R3  Scope-fence exclusions ("does not address lambda ... out of scope")
      recognized path-independently; previously only inside tom_s3_spinor_toy/.

Each control asserts AMBIGUOUS -- i.e. the new rule correctly declines to fire.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "g79a_lambda_identity_audit", HERE / "g79a_lambda_identity_audit.py"
)
assert SPEC and SPEC.loader
G79A = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G79A)

CONTROLS = [
    (
        "R1 -- \\Lambda guard must NOT mask a real lowercase \\lambda on the same line",
        "paper/NEW.md",
        r"`\Sigma = \Lambda^\bullet(\mathbb{C}^3)` while the coupling `\lambda` is newly fixed here.",
    ),
    (
        "R2 -- prose marker must require the ACTUAL phrase, not coupling+lambda nearby",
        "paper/NEW.md",
        "A new lambda enters through the coupling parameter introduced in this section.",
    ),
    (
        "R3 -- scope-fence rule must require a fence marker AND a scope verb",
        "paper/NEW.md",
        "We now derive lambda from first principles, and safe_for_runtime remains false.",
    ),
]


def main() -> None:
    print("Negative controls for the 2026-08-09 classifier relaxations")
    print("=" * 74)
    all_ok = True
    for name, path, line in CONTROLS:
        classification, reason = G79A.classify_occurrence(path, line)
        ok = classification == "AMBIGUOUS"
        all_ok = all_ok and ok
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        print(f"      -> {classification}  ({reason})")
    print()
    print(f"ALL NEGATIVE CONTROLS PASS: {all_ok}")
    print()
    print("Interpretation: each relaxation declines to fire on a line it must")
    print("still flag, so the three fixes narrowed false positives without")
    print("blinding the audit to genuine unclassified lambda usage.")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
