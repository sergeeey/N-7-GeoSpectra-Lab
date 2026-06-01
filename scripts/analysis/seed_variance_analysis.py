#!/usr/bin/env python3
"""Seed Variance Analysis — Gate 4B v0.1.24 + Negative Controls v0.1.22

Purpose: Check if contrasts are stable across seeds or driven by outliers.
Date: 2026-06-01
Status: DIAGNOSTIC (read-only analysis)

Question: Is broken_wilson_term 8.20× contrast stable across seeds, or is it an outlier?

Analysis:
1. Load all cases
2. Group by: family/control, size, disorder, seed
3. Compute per-seed contrasts: IPR(W=20) / IPR(W=0) for each (family, size, seed)
4. Compute variance across seeds
5. Compare: broken_wilson_term variance vs Gate 4B families variance

Output: reports/SEED_VARIANCE_ANALYSIS_v0.1.24.md
"""

import json
from pathlib import Path
from collections import defaultdict
import numpy as np


def load_gate4b_cases(base_path: Path) -> list[dict]:
    """Load all Gate 4B v0.1.24 cases."""
    cases = []
    batches_dir = base_path / "batches"
    if not batches_dir.exists():
        return cases
    for batch_dir in sorted(batches_dir.glob("batch_*")):
        results_file = batch_dir / "results.json"
        if results_file.exists():
            with open(results_file) as f:
                batch_data = json.load(f)
                if isinstance(batch_data, list):
                    for case in batch_data:
                        case["_source"] = str(results_file)
                        cases.append(case)
                else:
                    for case in batch_data.get("cases", []):
                        case["_source"] = str(results_file)
                        cases.append(case)
    return cases


def load_negative_controls_cases(base_path: Path) -> list[dict]:
    """Load all Negative Controls v0.1.22 cases."""
    cases = []
    for batch_dir in sorted(base_path.glob("batch_*")):
        for case_file in sorted(batch_dir.glob("case_*.json")):
            with open(case_file) as f:
                case = json.load(f)
                case["_source"] = str(case_file)
                cases.append(case)
    return cases


def compute_seed_contrasts(cases: list[dict], group_key: str) -> dict:
    """Compute per-seed contrasts for each (group, size) pair.

    Args:
        cases: List of case dicts
        group_key: 'family' (Gate 4B) or 'control' (Negative Controls)

    Returns:
        nested dict: {group: {size: {seed: contrast}}}
    """
    # Group by (group, size, seed, disorder)
    data = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: {"W0": None, "W20": None})))

    for case in cases:
        group = case.get(group_key, "unknown")
        size = case["s1_size"]
        seed = case["seed"]
        w = case["disorder_strength"]
        ipr = case["true_ipr_mean"]

        w_key = "W0" if w == 0 else "W20"
        data[group][size][seed][w_key] = ipr

    # Compute contrasts
    contrasts = defaultdict(lambda: defaultdict(dict))

    for group in data:
        for size in data[group]:
            for seed in data[group][size]:
                w0 = data[group][size][seed]["W0"]
                w20 = data[group][size][seed]["W20"]

                if w0 is not None and w20 is not None and w0 > 0:
                    contrast = w20 / w0
                    contrasts[group][size][seed] = contrast

    return contrasts


def main():
    print("=" * 80)
    print("SEED VARIANCE ANALYSIS — v0.1.24")
    print("=" * 80)
    print()

    # Paths
    gate4b_base = Path("reports/RUNS/gate4_fss_v0.1.24")
    nc_base = Path("reports/RUNS/negative_controls_v0.1.22")

    # Load cases
    print("📂 Loading cases...")
    gate4b_cases = load_gate4b_cases(gate4b_base)
    nc_cases = load_negative_controls_cases(nc_base)

    print(f"   Gate 4B: {len(gate4b_cases)} cases")
    print(f"   Negative Controls: {len(nc_cases)} cases")
    print()

    # Compute per-seed contrasts
    print("📊 Computing per-seed contrasts...")
    gate4b_contrasts = compute_seed_contrasts(gate4b_cases, "family")
    nc_contrasts = compute_seed_contrasts(nc_cases, "control")
    print()

    # Analyze Gate 4B variance
    print("=" * 80)
    print("GATE 4B — SEED VARIANCE BY FAMILY")
    print("=" * 80)
    print()

    gate4b_summary = {}
    for family in sorted(gate4b_contrasts.keys()):
        print(f"Family: {family}")
        print("-" * 40)

        gate4b_summary[family] = {}

        # Aggregate across all sizes
        all_contrasts = []
        for size in sorted(gate4b_contrasts[family].keys()):
            seed_contrasts = list(gate4b_contrasts[family][size].values())
            all_contrasts.extend(seed_contrasts)

            if seed_contrasts:
                mean_c = np.mean(seed_contrasts)
                std_c = np.std(seed_contrasts, ddof=1) if len(seed_contrasts) > 1 else 0.0
                cv = (std_c / mean_c * 100) if mean_c > 0 else 0.0

                print(
                    f"  Size {size:3d}: {mean_c:.2f}× ± {std_c:.2f} (CV: {cv:.1f}%, n={len(seed_contrasts)})"
                )

        if all_contrasts:
            agg_mean = np.mean(all_contrasts)
            agg_std = np.std(all_contrasts, ddof=1) if len(all_contrasts) > 1 else 0.0
            agg_cv = (agg_std / agg_mean * 100) if agg_mean > 0 else 0.0

            gate4b_summary[family] = {
                "mean_contrast": agg_mean,
                "std_contrast": agg_std,
                "cv_percent": agg_cv,
                "n_seeds": len(all_contrasts),
            }

            print()
            print(
                f"  AGGREGATE: {agg_mean:.2f}× ± {agg_std:.2f} (CV: {agg_cv:.1f}%, n={len(all_contrasts)})"
            )

        print()

    # Analyze Negative Controls variance
    print("=" * 80)
    print("NEGATIVE CONTROLS — SEED VARIANCE BY CONTROL")
    print("=" * 80)
    print()

    nc_summary = {}
    for control in sorted(nc_contrasts.keys()):
        print(f"Control: {control}")
        print("-" * 40)

        nc_summary[control] = {}

        # Aggregate across all sizes
        all_contrasts = []
        for size in sorted(nc_contrasts[control].keys()):
            seed_contrasts = list(nc_contrasts[control][size].values())
            all_contrasts.extend(seed_contrasts)

            if seed_contrasts:
                mean_c = np.mean(seed_contrasts)
                std_c = np.std(seed_contrasts, ddof=1) if len(seed_contrasts) > 1 else 0.0
                cv = (std_c / mean_c * 100) if mean_c > 0 else 0.0

                print(
                    f"  Size {size:3d}: {mean_c:.2f}× ± {std_c:.2f} (CV: {cv:.1f}%, n={len(seed_contrasts)})"
                )

        if all_contrasts:
            agg_mean = np.mean(all_contrasts)
            agg_std = np.std(all_contrasts, ddof=1) if len(all_contrasts) > 1 else 0.0
            agg_cv = (agg_std / agg_mean * 100) if agg_mean > 0 else 0.0

            nc_summary[control] = {
                "mean_contrast": agg_mean,
                "std_contrast": agg_std,
                "cv_percent": agg_cv,
                "n_seeds": len(all_contrasts),
            }

            print()
            print(
                f"  AGGREGATE: {agg_mean:.2f}× ± {agg_std:.2f} (CV: {agg_cv:.1f}%, n={len(all_contrasts)})"
            )

        print()

    # Compare variance
    print("=" * 80)
    print("COMPARISON: COEFFICIENT OF VARIATION (CV)")
    print("=" * 80)
    print()

    print(f"{'Group':<25} {'Mean Contrast':<15} {'Std Dev':<10} {'CV (%)':<10} {'n':<5}")
    print("-" * 75)

    # Gate 4B families
    for family in sorted(gate4b_summary.keys()):
        s = gate4b_summary[family]
        if s:
            print(
                f"{family:<25} {s['mean_contrast']:>7.2f}×         {s['std_contrast']:>6.2f}    {s['cv_percent']:>6.1f}      {s['n_seeds']:<5}"
            )

    print()

    # Controls
    for control in sorted(nc_summary.keys()):
        s = nc_summary[control]
        if s:
            print(
                f"{control:<25} {s['mean_contrast']:>7.2f}×         {s['std_contrast']:>6.2f}    {s['cv_percent']:>6.1f}      {s['n_seeds']:<5}"
            )

    print()

    # Decision
    print("=" * 80)
    print("VERDICT")
    print("=" * 80)
    print()

    # Check if broken_wilson_term variance comparable to Gate 4B
    bwt = nc_summary.get("broken_wilson_term", {})

    if bwt:
        bwt_cv = bwt["cv_percent"]

        gate4b_cvs = [gate4b_summary[f]["cv_percent"] for f in gate4b_summary if gate4b_summary[f]]

        if gate4b_cvs:
            mean_gate4b_cv = np.mean(gate4b_cvs)

            print(f"broken_wilson_term CV: {bwt_cv:.1f}%")
            print(f"Gate 4B mean CV: {mean_gate4b_cv:.1f}%")
            print()

            if abs(bwt_cv - mean_gate4b_cv) < 5.0:
                print(
                    "✅ VARIANCE COMPARABLE — broken_wilson_term seed variance similar to Gate 4B"
                )
                print("   → 8.20× contrast is STABLE across seeds")
            else:
                print("⚠️  VARIANCE DIFFERS — broken_wilson_term may have higher/lower seed noise")
                if bwt_cv > mean_gate4b_cv + 5.0:
                    print("   → broken_wilson_term shows HIGHER variance (less stable)")
                else:
                    print("   → broken_wilson_term shows LOWER variance (more stable)")
    else:
        print("⚠️  Insufficient data for broken_wilson_term variance comparison")

    print()

    # Save results to JSON
    output = {
        "gate4b": gate4b_summary,
        "negative_controls": nc_summary,
        "analysis_date": "2026-06-01",
        "data_sources": {
            "gate4b": str(gate4b_base),
            "negative_controls": str(nc_base),
        },
    }

    output_file = Path("reports/seed_variance_data_v0.1.24.json")
    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)

    print(f"📊 Raw data saved: {output_file}")
    print()


if __name__ == "__main__":
    main()
