"""Persisted re-derivation script for the C116 ADDENDUM fraction-real
table, written in response to the FL Step 8a skeptic pass on the
addendum (2026-08-31) which flagged that the addendum's own claim of
"independently re-derived from source" left no artifact -- see
decision.md ADDENDUM section and its "Skeptic response (2026-08-31)"
subsection for the full response-matrix.

Computes, per cell, both:
  (a) fraction_total  -- real count / (2*j2+1)^2  (the addendum's
      original normalization)
  (b) fraction_sector -- real count / (2*(2*j2+1))  (restricted to the
      |a|=j2 sector where the asymmetric rule permits reality at all;
      the skeptic's alternate normalization)
to make explicit that monotonicity in (a) is a property of the
denominator, not of the underlying physics -- (b) is NOT monotone.
"""

import json
from fractions import Fraction
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent


def parse_a(removed_str):
    """'(3/2, -1/2)' -> Fraction(3, 2); '(1, 1)' -> Fraction(1)."""
    inner = removed_str.strip("()")
    a_str = inner.split(",")[0].strip()
    return Fraction(a_str)


def rows_c114(cell_key):
    path = BASE / "20260830-c114-subset-analysis-matched-diagonal-cells" / "results_c114.json"
    with open(path) as f:
        d = json.load(f)
    subsets = d[cell_key]["subsets"]
    remove_one = [s for s in subsets if s["type"] == "remove_one"]
    return [(parse_a(s["removed"]), s["max_im"] <= 1e-8) for s in remove_one]


def rows_c115():
    path = BASE / "20260830-c115-third-cell-2-2-mechanism-test" / "results_c115.json"
    with open(path) as f:
        d = json.load(f)
    return [(parse_a(r["removed"]), not r["breaks"]) for r in d["remove_one_detail"]]


def rows_c116():
    path = BASE / "20260830-c116-j2-3-decisive-kill-test" / "results_c116.json"
    with open(path) as f:
        d = json.load(f)
    return [(Fraction(r["a"]), not r["actual_breaks"]) for r in d["all_remove_one_detail"]]


CELLS = [
    ("1", Fraction(1), lambda: rows_c114("cell_j1_1_j2_1")),
    ("3/2", Fraction(3, 2), lambda: rows_c114("cell_j1_1p5_j2_1p5")),
    ("2", Fraction(2), rows_c115),
    ("3", Fraction(3), rows_c116),
]

if __name__ == "__main__":
    print(
        f"{'j2':>5} {'n':>3} {'total':>6} {'real':>5} {'frac_total':>11} "
        f"{'sector_real':>12} {'frac_sector':>12}"
    )
    for label, j2, fn in CELLS:
        rows = fn()
        n = round(2 * j2 + 1)
        expected_total = n * n
        assert len(rows) == expected_total, f"j2={label}: total={len(rows)} != n^2={expected_total}"
        real = sum(1 for _, is_real in rows if is_real)
        frac_total = real / len(rows)

        sector_rows = [is_real for a, is_real in rows if abs(a) == j2]
        sector_size = 2 * n
        assert len(sector_rows) == sector_size, (
            f"j2={label}: |a|=j2 sector size {len(sector_rows)} != 2n={sector_size}"
        )
        sector_real = sum(1 for is_real in sector_rows if is_real)
        frac_sector = sector_real / sector_size

        print(
            f"{label:>5} {n:>3} {len(rows):>6} {real:>5} {frac_total:>11.4f} "
            f"{sector_real:>12} {frac_sector:>12.4f}"
        )
