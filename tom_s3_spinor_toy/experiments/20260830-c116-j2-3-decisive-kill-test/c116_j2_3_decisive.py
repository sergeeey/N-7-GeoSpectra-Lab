"""C116 -- decisive j2=3 test named by C115's own FL Step 8a skeptic
review: does the asymmetric rule's prediction for a=0 removals hold at
an integer j2 with real |b|<j2 resolution? Reuses C114's run_cell
unmodified via direct import.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from sympy import S

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c116.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    c85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )
    c114 = load_module(
        "c114_subset_analysis",
        HERE.parent
        / "20260830-c114-subset-analysis-matched-diagonal-cells"
        / "c114_subset_analysis.py",
    )

    cell_33 = c114.run_cell(c85, 6, S(3), "j1=3,j2=3", do_structured_intermediate=False)

    p0_ok = cell_33["full_sum_max_im"] < 1e-9
    norms = list(cell_33["component_norms"].values())
    norms_identical = max(norms) - min(norms) < 1e-9 if norms else False

    def parse_pair(s: str):
        inner = s.strip("()")
        a_str, b_str = [p.strip() for p in inner.split(",")]
        return S(a_str), S(b_str)

    j2_val = S(3)

    # The decisive prediction: all (0,b) removals should break.
    a0_removals = []
    all_remove_one = []
    both_extreme_matches = 0
    both_extreme_total = 0
    for entry in cell_33["subsets"]:
        if entry["type"] != "remove_one":
            continue
        a, b = parse_pair(entry["removed"])
        both_extreme = abs(a) == j2_val and abs(b) < j2_val
        breaks = entry["max_im"] > 1e-9
        rule_matches = both_extreme == (not breaks)
        both_extreme_total += 1
        both_extreme_matches += int(rule_matches)
        detail = {
            "removed": entry["removed"],
            "a": str(a),
            "b": str(b),
            "predicted_stays_real": both_extreme,
            "actual_breaks": breaks,
            "rule_matches": rule_matches,
            "max_im": entry["max_im"],
        }
        all_remove_one.append(detail)
        if a == 0:
            a0_removals.append(detail)

    all_a0_break = all(d["actual_breaks"] for d in a0_removals)
    zero_zero = next((d for d in a0_removals if d["b"] == "0"), None)

    print(f"\nP0 (full sum real): {p0_ok}")
    print(f"P1 (component norms identical): {norms_identical}")
    print(f"Asymmetric rule match: {both_extreme_matches}/{both_extreme_total}")
    print("\nDECISIVE TEST -- all 7 (0,b) removals:")
    for d in a0_removals:
        print(f"  {d}")
    print(f"\nALL (0,b) BREAK: {all_a0_break}")
    if zero_zero is not None:
        print(f"(0,0) specifically breaks: {zero_zero['actual_breaks']}")

    if all_a0_break:
        verdict = "ALL_A0_BREAK__LOW_SPIN_REGIME_READING_STRONGLY_FAVORED"
    elif (
        zero_zero is not None
        and not zero_zero["actual_breaks"]
        and all(d["actual_breaks"] for d in a0_removals if d["b"] != "0")
    ):
        verdict = "ONLY_00_STAYS_REAL__ZERO_SPECIFIC_STRUCTURE_READING_SUPPORTED"
    else:
        verdict = "UNEXPECTED_PATTERN__NEITHER_PREREGISTERED_READING_MATCHES__SEE_DETAILS"

    out = {
        "cell": cell_33,
        "p0_ok": p0_ok,
        "p1_norms_identical": norms_identical,
        "asymmetric_rule_fraction": f"{both_extreme_matches}/{both_extreme_total}",
        "a0_removals": a0_removals,
        "all_remove_one_detail": all_remove_one,
        "all_a0_break": all_a0_break,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
