"""C115 -- third matched-diagonal cell (j1=j2=2), a third data point for
C114's own open mechanism question. Reuses C114's run_cell unmodified
(imported directly, not copy-pasted) via importlib, matching this
project's own established reuse convention.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from sympy import S

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c115.json"


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

    cell_22 = c114.run_cell(c85, 4, S(2), "j1=2,j2=2", do_structured_intermediate=False)

    p0_ok = cell_22["full_sum_max_im"] < 1e-9

    norms = list(cell_22["component_norms"].values())
    norms_identical = max(norms) - min(norms) < 1e-9 if norms else False

    # P2: does |a|=j2 AND |b|=j2 ("both-extreme") classify the remove-one
    # results correctly? j2=2, so "extreme" means a or b == +-2.
    def parse_pair(s: str):
        inner = s.strip("()")
        a_str, b_str = [p.strip() for p in inner.split(",")]
        return S(a_str), S(b_str)

    j2_val = S(2)
    both_extreme_matches = 0
    both_extreme_total = 0
    remove_one_detail = []
    for entry in cell_22["subsets"]:
        if entry["type"] != "remove_one":
            continue
        a, b = parse_pair(entry["removed"])
        both_extreme = abs(a) == j2_val and abs(b) == j2_val
        breaks = entry["max_im"] > 1e-9
        matches = both_extreme == breaks
        both_extreme_total += 1
        both_extreme_matches += int(matches)
        remove_one_detail.append(
            {
                "removed": entry["removed"],
                "both_extreme": both_extreme,
                "breaks": breaks,
                "rule_matches": matches,
                "max_im": entry["max_im"],
            }
        )

    fraction = f"{both_extreme_matches}/{both_extreme_total}"
    print(f"\nP0 (full sum real): {p0_ok}")
    print(f"P1 (component norms identical): {norms_identical}")
    print(f"P2 (both-extreme rule matches): {fraction}")
    for d in remove_one_detail:
        print(f"  {d}")

    out = {
        "cell": cell_22,
        "p0_ok": p0_ok,
        "p1_norms_identical": norms_identical,
        "both_extreme_rule_fraction": fraction,
        "remove_one_detail": remove_one_detail,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
