"""C117 -- j2=5/2 gap test, named by the FL Step 8a skeptic pass on the
C116 addendum (2026-08-31): fills the only untested cell between j2=2
(window clean) and j2=3 (window fully collapsed), directly testing
RULE_HOLDS / PARTIAL / FULL_COLLAPSE per claim.md's pre-registration.

Reuses C114's run_cell unmodified via direct import, same as C115/C116.

Fixes a serialization hazard the skeptic found in results_c116.json:
`abs(a) == j2_val` on sympy Rationals can return a sympy Boolean type
(not a Python bool) for some rows, which `json.dumps(..., default=str)`
then serializes as the STRING "True"/"False" -- truthy in Python
regardless of value. All boolean fields here are explicitly cast with
`bool(...)` before being placed in the output dict.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from sympy import S

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c117.json"


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

    j2_val = S(5) / 2
    k_source = 5  # 2 * j2_val
    cell = c114.run_cell(c85, k_source, j2_val, "j1=5/2,j2=5/2", do_structured_intermediate=False)

    p0_ok = cell["full_sum_max_im"] < 1e-9
    norms = list(cell["component_norms"].values())
    norms_identical = max(norms) - min(norms) < 1e-9 if norms else False

    def parse_pair(s: str):
        inner = s.strip("()")
        a_str, b_str = [p.strip() for p in inner.split(",")]
        return S(a_str), S(b_str)

    all_remove_one = []
    rule_matches_count = 0
    sector_entries = []  # |a| == j2 entries (the rule-relevant sector)
    for entry in cell["subsets"]:
        if entry["type"] != "remove_one":
            continue
        a, b = parse_pair(entry["removed"])
        predicted_stays_real = bool(abs(a) == j2_val and abs(b) < j2_val)
        actual_breaks = bool(entry["max_im"] > 1e-9)
        rule_matches = bool(predicted_stays_real == (not actual_breaks))
        rule_matches_count += int(rule_matches)
        detail = {
            "removed": entry["removed"],
            "a": str(a),
            "b": str(b),
            "predicted_stays_real": predicted_stays_real,
            "actual_breaks": actual_breaks,
            "rule_matches": rule_matches,
            "max_im": entry["max_im"],
        }
        all_remove_one.append(detail)
        if bool(abs(a) == j2_val):
            sector_entries.append(detail)

    sector_size = len(sector_entries)
    sector_real = sum(1 for d in sector_entries if not d["actual_breaks"])
    predicted_real_in_sector = sum(1 for d in sector_entries if d["predicted_stays_real"])

    print(f"\nP0 (full sum real): {p0_ok}")
    print(f"P1 (component norms identical): {norms_identical}")
    print(f"Total remove-one tested: {len(all_remove_one)} (expect 36)")
    print(
        f"|a|=j2 sector size: {sector_size} (expect 12), rule predicts {predicted_real_in_sector} real"
    )
    print(f"Rule match overall: {rule_matches_count}/{len(all_remove_one)}")
    print(f"Sector actual real: {sector_real}/{sector_size}")
    print("\nSector detail (|a|=j2=5/2):")
    for d in sector_entries:
        print(f"  {d}")

    if sector_real == predicted_real_in_sector and all(d["rule_matches"] for d in sector_entries):
        verdict = "RULE_HOLDS"
    elif sector_real == 0:
        verdict = "FULL_COLLAPSE"
    else:
        verdict = "PARTIAL"

    out = {
        "cell": cell,
        "p0_ok": p0_ok,
        "p1_norms_identical": norms_identical,
        "rule_match_fraction": f"{rule_matches_count}/{len(all_remove_one)}",
        "sector_real_fraction": f"{sector_real}/{sector_size}",
        "predicted_real_in_sector": predicted_real_in_sector,
        "all_remove_one_detail": all_remove_one,
        "sector_entries": sector_entries,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
