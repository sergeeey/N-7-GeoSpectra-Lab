"""Rebuild control summary tables directly from raw run JSONs.

WHY THIS EXISTS: summary tables in reports/ and docs/ were copied by hand and disagreed
with the raw outputs (e.g. broken_wilson IPR listed as 0.007 while raw runs give 0.22-0.74).
This script is the single source for control numbers. Reports should cite its output,
not re-type numbers.

Reads: reports/RUNS/**/*.json  (files with true_ipr_mean and a control or scenario field)
Ring reference: reports/RUNS/gate4_fss_v0.1.24/batches/batch_06/results.json (ring, W=20)
Writes: results/controls_from_raw.json and prints a markdown table.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "reports" / "RUNS"
REF_FILE = RUNS / "gate4_fss_v0.1.24" / "batches" / "batch_06" / "results.json"
OUT = ROOT / "results" / "controls_from_raw.json"
W_LOCAL = 20


def load_items(path: Path) -> list[dict]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    return data if isinstance(data, list) else [data]


def collect_controls() -> dict[tuple[str, int], list[float]]:
    agg: dict[tuple[str, int], list[float]] = defaultdict(list)
    for path in RUNS.rglob("*.json"):
        for item in load_items(path):
            if not isinstance(item, dict) or "true_ipr_mean" not in item:
                continue
            name = item.get("control")
            if not name:
                continue
            if item.get("disorder_strength") != W_LOCAL:
                continue
            agg[(name, int(item["s1_size"]))].append(float(item["true_ipr_mean"]))
    return agg


def collect_ring_reference() -> dict[int, float]:
    ref: dict[int, list[float]] = defaultdict(list)
    for item in load_items(REF_FILE):
        if item.get("family") != "ring":
            continue
        if item.get("disorder_strength", item.get("W")) != W_LOCAL:
            continue
        ref[int(item["s1_size"])].append(float(item["true_ipr_mean"]))
    return {s: sum(v) / len(v) for s, v in ref.items()}


def main() -> None:
    controls = collect_controls()
    ring = collect_ring_reference()
    rows = []
    for (name, s1), vals in sorted(controls.items()):
        ref = ring.get(s1)
        rows.append(
            {
                "control": name,
                "s1": s1,
                "n": len(vals),
                "ipr_max": max(vals),
                "ipr_mean": sum(vals) / len(vals),
                "ring_ref_mean": ref,
                "max_over_ring": (max(vals) / ref) if ref else None,
            }
        )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"rows": rows, "ring_reference": ring}, indent=2), encoding="utf-8")

    print("| control | s1 | n | IPR max | IPR mean | ring ref | max / ring |")
    print("|---|---|---|---|---|---|---|")
    for r in rows:
        ref = f"{r['ring_ref_mean']:.4f}" if r["ring_ref_mean"] else "—"
        rat = f"{100 * r['max_over_ring']:.1f} %" if r["max_over_ring"] else "—"
        print(
            f"| {r['control']} | {r['s1']} | {r['n']} | {r['ipr_max']:.4f} | {r['ipr_mean']:.4f} | {ref} | {rat} |"
        )
    print(f"\nwritten {OUT}")


if __name__ == "__main__":
    main()
