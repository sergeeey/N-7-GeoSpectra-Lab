"""
Negative-control checker: does a round's results JSON record a check that was
run on an input for which it MUST fail?

Added 2026-09-07 alongside `experiments/_template/negative_control.py`, after
the C179-C182 sequence produced five checks that could not fail by construction
(pearl_registry 2026-09-07). Three of the five were found by external
context-blind skeptics AFTER the round closed; one by a control in the script;
one by a corrupted-input replay. This script exists so the question is asked
mechanically, BEFORE the round closes.

USAGE

    python scripts/check_negative_control.py experiments/20260908-c183-.../
    python scripts/check_negative_control.py path/to/results_x.json
    python scripts/check_negative_control.py --since    # enforce from the
                                                        # convention start date
    python scripts/check_negative_control.py --all      # coverage report,
                                                        # never enforces

Exit code 1 if any enforced results file is MISSING a negative control, or if a
control FIRED (the round's own control says the check discriminates nothing --
that check must not be quoted as evidence). Exit 0 otherwise.

WHAT IS ENFORCED, AND ON WHAT

Only rounds dated on or after CONVENTION_START. Rounds before it were written
under no such convention and are NOT retro-flagged: --all reports their
coverage for the record and always exits 0. Nothing about how an existing round
reports its results has to change.

WHAT THIS CANNOT CHECK -- stated because a checker that appears to verify more
than it does is the same defect it was built to catch

  1. It cannot tell whether the control input was genuinely adversarial. A
     control drawn from the same family as the real input (C180's multiplicity
     check could not have been broken by any su(2)-derived input) passes this
     checker and is still worthless. That judgement stays human/skeptic.
  2. It asks for AT LEAST ONE negative control per results file. It cannot map
     controls onto individual checks, because that would require every round to
     report its checks in a uniform schema -- a far larger change than the
     observation justifies.
  3. On the two legacy forms below it validates the SHAPE of a control record,
     not the control itself. Only the canonical form is fully validated.
"""

import argparse
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPERIMENTS_DIR = os.path.join(REPO, "experiments")

# Rounds dated on or after this carry the convention. Earlier rounds are
# reported but never enforced -- see WHAT IS ENFORCED above.
CONVENTION_START = "20260908"

ROUND_DATE_RE = re.compile(r"^(\d{8})-")

# Form B2: a top-level boolean whose NAME declares that a corruption was
# replayed and detected. Deliberately narrow -- the name alone is never
# sufficient, it must be paired with the mixed-polarity case table below.
CORRUPTION_NAME_RE = re.compile(
    r"(^|_)(broken|corrupt|corrupted|scrambled|shuffled|junk|control)(_|$)"
    r"|_detected$|^detects_"
)

OK = "OK"
LEGACY = "OK-LEGACY"
FIRED = "CONTROL-FIRED"
MISSING = "MISSING"


def _canonical(doc):
    """Form A: the block emitted by experiments/_template/negative_control.py."""
    if not isinstance(doc, dict):
        return None
    blocks = doc.get("negative_control")
    if blocks is None:
        return None
    if isinstance(blocks, dict):
        blocks = [blocks]
    if not isinstance(blocks, list) or not blocks:
        return (MISSING, "`negative_control` present but empty or not a dict/list")

    # WHY the three-bucket sort instead of returning on the first bad block:
    # an earlier version returned MISSING as soon as it met a malformed entry,
    # which threw away a co-located block that WAS a genuine, discriminating
    # control -- contradicting this module's own "at least one" contract. Found
    # by an independent context-blind review and reproduced before the fix.
    good, fired, malformed = [], [], []
    for b in blocks:
        if not isinstance(b, dict):
            malformed.append("an entry that is not an object")
            continue
        name = repr(b.get("check"))
        absent = {"check", "passed_on_real", "control_inputs", "discriminates"} - set(b)
        if absent:
            malformed.append(name + " missing field(s) " + str(sorted(absent)))
        elif not isinstance(b.get("control_inputs"), dict) or not b["control_inputs"]:
            malformed.append(name + " declares no control input")
        elif not b.get("passed_on_real"):
            malformed.append(
                name + " did not pass on the real input, so there is no PASS to control"
            )
        elif b.get("deterministic_on_rerun") is False:
            fired.append(
                name
                + " is not a function of its input (differed on a re-run of the SAME real input)"
            )
        elif not b.get("discriminates"):
            survivors = b.get("controls_that_also_passed") or [
                k for k, v in b["control_inputs"].items() if v
            ]
            fired.append(name + " also passed on control input(s) " + str(survivors))
        else:
            good.append(name)

    suffix = ("; malformed entries ignored: " + "; ".join(malformed)) if malformed else ""
    # A fired control outranks a good one: that check must be withdrawn regardless
    # of what else in the file is well controlled.
    if fired:
        return (FIRED, "; ".join(fired) + " -- must not be quoted as evidence" + suffix)
    if good:
        return (OK, "canonical control(s) on: " + ", ".join(good) + suffix)
    return (MISSING, "no usable `negative_control` entry -- " + "; ".join(malformed))


def _legacy_discriminates(doc):
    """Form B1: a top-level boolean `discriminates` (as in C181's c181b)."""
    if not isinstance(doc, dict) or not isinstance(doc.get("discriminates"), bool):
        return None
    if doc["discriminates"]:
        return (LEGACY, "top-level `discriminates: true` (shape only, not validated)")
    return (FIRED, "top-level `discriminates: false` -- the check discriminates nothing")


def _mixed_polarity_table(doc):
    """Find a list of case objects in which some boolean field takes BOTH values.

    Structurally this is exactly "the check answered differently on different
    inputs". Never sufficient on its own -- an ordinary per-level results table
    can look like this by accident -- so `_legacy_replay` pairs it with a
    declared corruption-named boolean.
    """
    stack = [doc]
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            stack.extend(node.values())
        elif isinstance(node, list) and node and all(isinstance(e, dict) for e in node):
            keys = set()
            for e in node:
                keys.update(e.keys())
            for k in sorted(keys):
                vals = [e[k] for e in node if isinstance(e.get(k), bool)]
                if True in vals and False in vals:
                    return k
            stack.extend(node)
    return None


def _legacy_replay(doc):
    """Form B2: declared corruption booleans PLUS a mixed-polarity case table."""
    if not isinstance(doc, dict):
        return None
    declared = [
        k for k, v in doc.items() if isinstance(v, bool) and CORRUPTION_NAME_RE.search(k.lower())
    ]
    if not declared:
        return None
    field = _mixed_polarity_table(doc)
    if field is None:
        return (
            MISSING,
            "declares " + str(declared) + " but no case table where a boolean takes "
            "both values -- nothing shows the check ever reported failure",
        )
    if not any(doc[k] for k in declared):
        return (FIRED, "declared corruption checks are all false: " + str(declared))
    return (
        LEGACY,
        "corruption replay: " + str(declared) + " over `" + field + "` (shape only, not validated)",
    )


def classify(path):
    """-> (status, reason). Canonical form wins, then the two legacy forms."""
    try:
        with open(path, encoding="utf-8") as f:
            doc = json.load(f)
    except (OSError, json.JSONDecodeError) as exc:
        return (MISSING, "unreadable: " + str(exc))
    for probe in (_canonical, _legacy_discriminates, _legacy_replay):
        verdict = probe(doc)
        if verdict is not None:
            return verdict
    return (MISSING, "no negative-control record found")


def results_files(target):
    if os.path.isfile(target):
        return [target]
    out = []
    for root, _dirs, files in os.walk(target):
        out.extend(
            os.path.join(root, f) for f in files if f.startswith("results") and f.endswith(".json")
        )
    return sorted(out)


def _display(path, start):
    """relpath, falling back to the absolute path.

    WHY: on Windows os.path.relpath raises ValueError when the two paths are on
    different drives, which happens whenever the checker is pointed at a file
    outside the repo (a scratch results file, a CI temp dir). Reporting is not
    worth crashing the check over.
    """
    try:
        return os.path.relpath(path, start).replace("\\", "/")
    except ValueError:
        return path.replace("\\", "/")


def round_date(path):
    rel = _display(path, EXPERIMENTS_DIR)
    m = ROUND_DATE_RE.match(rel.split("/")[0])
    return m.group(1) if m else None


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Does a round's results JSON record a negative control?"
    )
    ap.add_argument("paths", nargs="*", help="results*.json files or round directories")
    ap.add_argument(
        "--since",
        nargs="?",
        const=CONVENTION_START,
        metavar="YYYYMMDD",
        help="enforce over experiments/ rounds dated >= this (default " + CONVENTION_START + ")",
    )
    ap.add_argument(
        "--all",
        action="store_true",
        help="coverage report over every round; never enforces",
    )
    args = ap.parse_args(argv)

    if args.all:
        targets = results_files(EXPERIMENTS_DIR)
        enforcing, scope = False, "ALL rounds"
    elif args.since:
        targets = []
        for p in results_files(EXPERIMENTS_DIR):
            d = round_date(p)
            if d and d >= args.since:
                targets.append(p)
        enforcing, scope = True, "rounds dated >= " + args.since
    elif args.paths:
        targets = []
        for t in args.paths:
            targets.extend(results_files(t))
        enforcing, scope = True, "explicit paths"
    else:
        ap.error("give a path, or --since, or --all")

    print("=== NEGATIVE-CONTROL CHECK ===")
    print("Scope: " + scope + "   Enforcing: " + str(enforcing))
    print("Results files scanned: " + str(len(targets)))
    print()

    tally = {OK: 0, LEGACY: 0, FIRED: 0, MISSING: 0}
    legacy_rejected = 0
    for path in targets:
        status, reason = classify(path)
        # A legacy shape describes the 4 pre-convention files that happened to
        # carry a control. It is NOT sufficient for a round written under the
        # convention: both legacy forms are cheap to satisfy accidentally (a
        # lone `discriminates: true`; a corruption-named boolean anywhere plus
        # an unrelated mixed-polarity table), which an independent review
        # demonstrated. Rather than make the heuristics cleverer -- an arms
        # race on shapes nobody should be writing any more -- they simply stop
        # counting once a round is inside the enforced window.
        d = round_date(path)
        if status == LEGACY and d and d >= CONVENTION_START:
            status = MISSING
            reason = (
                "legacy control shape (" + reason + ") is not sufficient for a round "
                "dated >= " + CONVENTION_START + " -- use the canonical helper block"
            )
            legacy_rejected += 1
        tally[status] += 1
        rel = _display(path, REPO)
        print("  " + status.ljust(13) + " " + rel)
        print("                " + reason)

    print()
    print("--- SCOREBOARD (pearl_registry 2026-09-07, cannot-fail-check prediction) ---")
    print("  negative control present (canonical) : " + str(tally[OK]))
    print(
        "  negative control present (legacy)    : "
        + str(tally[LEGACY])
        + (
            "  (+" + str(legacy_rejected) + " rejected: post-cutoff round)"
            if legacy_rejected
            else ""
        )
    )
    print("  control FIRED -- caught by the script: " + str(tally[FIRED]))
    print("  MISSING -- no control recorded       : " + str(tally[MISSING]))
    print("  caught by an external skeptic instead: count by hand from each")
    print("      round's decision.md Step 8a section -- not machine-readable.")
    print()

    bad = tally[MISSING] + tally[FIRED]

    # Zero files scanned is never a PASS. An earlier version printed
    # "RESULT: PASS" after scanning nothing, so a mistyped path or an empty
    # directory read as a clean bill of health to anything gating on the exit
    # code alone -- itself a cannot-fail check, in the script built to forbid
    # them. Found by an independent context-blind review.
    if not targets:
        if args.since:
            print(
                "RESULT: NOTHING IN SCOPE -- no round dated >= "
                + args.since
                + " exists yet, so nothing was checked. This is not a pass."
            )
            return 0
        print(
            "RESULT: NOTHING SCANNED -- the given path(s) matched no results*.json "
            "file. Check the path; this is not a pass."
        )
        return 1

    if not enforcing:
        print(
            "RESULT: REPORT ONLY -- "
            + str(bad)
            + " file(s) without a passing control (not enforced)"
        )
        return 0
    if bad == 0:
        print("RESULT: PASS -- every scanned results file records a negative control")
        return 0
    print("RESULT: NEEDS FIX -- " + str(bad) + " file(s) flagged")
    return 1


if __name__ == "__main__":
    sys.exit(main())
