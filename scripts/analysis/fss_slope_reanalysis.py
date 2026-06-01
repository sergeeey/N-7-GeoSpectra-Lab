#!/usr/bin/env python3
"""FSS Slope Reanalysis — Gate 4B v0.1.24 + Negative Controls v0.1.22

Purpose: Quantify finite-size scaling slope for each family/control separately.
Date: 2026-06-01
Status: DIAGNOSTIC (read-only analysis)

Question: Can FSS slope distinguish intact geometry (Gate 4B families) from controls?

Analysis:
1. Load all Gate 4B cases (216) + Negative Controls cases (54)
2. Group by: family/control, disorder_strength
3. Fit: log(IPR) = a + b * log(N) for each group
4. Compare slopes: Gate families vs controls
5. Classify: STRENGTHENING (b>0), STABLE (b≈0), WEAKENING (b<0)

Output: reports/FSS_SLOPE_REANALYSIS_v0.1.24.md
"""

import json
from pathlib import Path
from collections import defaultdict
import numpy as np
from scipy import stats


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
                # Gate 4B stores list directly, not in "cases" field
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


def fit_fss_slope(sizes: list[int], iprs: list[float]) -> dict:
    """Fit log(IPR) ~ log(N) linear regression.

    Returns:
        slope: b coefficient (FSS exponent)
        intercept: a coefficient
        r_squared: goodness of fit
        p_value: significance of slope
    """
    if len(sizes) < 3:
        return {
            "slope": None,
            "intercept": None,
            "r_squared": None,
            "p_value": None,
            "n_points": len(sizes),
            "status": "INSUFFICIENT_DATA",
        }

    log_sizes = np.log(sizes)
    log_iprs = np.log(iprs)

    slope, intercept, r_value, p_value, std_err = stats.linregress(log_sizes, log_iprs)

    # Classify slope
    if abs(slope) < 0.05:
        classification = "STABLE"
    elif slope > 0:
        classification = "STRENGTHENING"
    else:
        classification = "WEAKENING"

    return {
        "slope": slope,
        "intercept": intercept,
        "r_squared": r_value**2,
        "p_value": p_value,
        "std_err": std_err,
        "n_points": len(sizes),
        "classification": classification,
        "status": "OK",
    }


def main():
    print("=" * 80)
    print("FSS SLOPE REANALYSIS — v0.1.24")
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

    # Group Gate 4B by family + disorder
    gate4b_groups = defaultdict(lambda: {"W0": [], "W20": []})

    for case in gate4b_cases:
        family = case.get("family", "unknown")
        w = case["disorder_strength"]
        size = case["s1_size"]
        ipr = case["true_ipr_mean"]

        w_key = "W0" if w == 0 else "W20"
        gate4b_groups[family][w_key].append((size, ipr))

    # Group Negative Controls by control + disorder
    nc_groups = defaultdict(lambda: {"W0": [], "W20": []})

    for case in nc_cases:
        control = case["control"]
        w = case["disorder_strength"]
        size = case["s1_size"]
        ipr = case["true_ipr_mean"]

        w_key = "W0" if w == 0 else "W20"
        nc_groups[control][w_key].append((size, ipr))

    # Fit FSS slopes
    print("=" * 80)
    print("GATE 4B — FSS SLOPES BY FAMILY")
    print("=" * 80)
    print()

    gate4b_results = {}
    for family in sorted(gate4b_groups.keys()):
        print(f"Family: {family}")
        print("-" * 40)

        gate4b_results[family] = {}

        for w_key in ["W0", "W20"]:
            data = gate4b_groups[family][w_key]
            if not data:
                print(f"  {w_key}: NO DATA")
                continue

            sizes = [d[0] for d in data]
            iprs = [d[1] for d in data]

            # Group by size to get mean IPR per size
            size_to_iprs = defaultdict(list)
            for s, i in zip(sizes, iprs):
                size_to_iprs[s].append(i)

            mean_sizes = sorted(size_to_iprs.keys())
            mean_iprs = [np.mean(size_to_iprs[s]) for s in mean_sizes]

            fit = fit_fss_slope(mean_sizes, mean_iprs)
            gate4b_results[family][w_key] = fit

            if fit["status"] == "OK":
                print(f"  {w_key}:")
                print(f"    Slope: {fit['slope']:.4f} ± {fit['std_err']:.4f}")
                print(f"    R²: {fit['r_squared']:.4f}")
                print(f"    p-value: {fit['p_value']:.4e}")
                print(f"    Classification: {fit['classification']}")
                print(f"    Data points: {fit['n_points']} sizes")
            else:
                print(f"  {w_key}: {fit['status']}")

        print()

    # Fit Negative Controls slopes
    print("=" * 80)
    print("NEGATIVE CONTROLS — FSS SLOPES BY CONTROL")
    print("=" * 80)
    print()

    nc_results = {}
    for control in sorted(nc_groups.keys()):
        print(f"Control: {control}")
        print("-" * 40)

        nc_results[control] = {}

        for w_key in ["W0", "W20"]:
            data = nc_groups[control][w_key]
            if not data:
                print(f"  {w_key}: NO DATA")
                continue

            sizes = [d[0] for d in data]
            iprs = [d[1] for d in data]

            # Group by size to get mean IPR per size
            size_to_iprs = defaultdict(list)
            for s, i in zip(sizes, iprs):
                size_to_iprs[s].append(i)

            mean_sizes = sorted(size_to_iprs.keys())
            mean_iprs = [np.mean(size_to_iprs[s]) for s in mean_sizes]

            fit = fit_fss_slope(mean_sizes, mean_iprs)
            nc_results[control][w_key] = fit

            if fit["status"] == "OK":
                print(f"  {w_key}:")
                print(f"    Slope: {fit['slope']:.4f} ± {fit['std_err']:.4f}")
                print(f"    R²: {fit['r_squared']:.4f}")
                print(f"    p-value: {fit['p_value']:.4e}")
                print(f"    Classification: {fit['classification']}")
                print(f"    Data points: {fit['n_points']} sizes")
            else:
                print(f"  {w_key}: {fit['status']}")

        print()

    # Compare Gate 4B vs Controls
    print("=" * 80)
    print("COMPARISON: GATE 4B vs CONTROLS (W=20 only)")
    print("=" * 80)
    print()

    print(f"{'Group':<25} {'Slope':<12} {'R²':<8} {'Classification':<15}")
    print("-" * 70)

    # Gate 4B families
    for family in sorted(gate4b_results.keys()):
        fit = gate4b_results[family].get("W20", {})
        if fit.get("status") == "OK":
            print(
                f"{family:<25} {fit['slope']:>6.4f}±{fit['std_err']:.4f}  {fit['r_squared']:>6.4f}  {fit['classification']:<15}"
            )

    print()

    # Controls
    for control in sorted(nc_results.keys()):
        fit = nc_results[control].get("W20", {})
        if fit.get("status") == "OK":
            print(
                f"{control:<25} {fit['slope']:>6.4f}±{fit['std_err']:.4f}  {fit['r_squared']:>6.4f}  {fit['classification']:<15}"
            )

    print()

    # Decision
    print("=" * 80)
    print("VERDICT")
    print("=" * 80)
    print()

    # Check if broken_wilson_term slope matches Gate 4B
    bwt_fit = nc_results.get("broken_wilson_term", {}).get("W20", {})

    if bwt_fit.get("status") == "OK":
        bwt_slope = bwt_fit["slope"]
        bwt_class = bwt_fit["classification"]

        # Compare to Gate 4B families
        gate4b_w20_slopes = [
            gate4b_results[f]["W20"]["slope"]
            for f in gate4b_results
            if gate4b_results[f].get("W20", {}).get("status") == "OK"
        ]

        if gate4b_w20_slopes:
            mean_gate4b_slope = np.mean(gate4b_w20_slopes)

            print(f"broken_wilson_term slope: {bwt_slope:.4f} ({bwt_class})")
            print(f"Gate 4B mean slope: {mean_gate4b_slope:.4f}")
            print()

            if abs(bwt_slope - mean_gate4b_slope) < 0.1:
                print("✅ FSS slopes MATCH — broken_wilson_term shows similar scaling to Gate 4B")
                print("   → Cannot distinguish by FSS slope alone")
            else:
                print("❌ FSS slopes DIFFER — broken_wilson_term scaling distinct from Gate 4B")
                print("   → FSS slope can distinguish control from intact geometry")
    else:
        print("⚠️  Insufficient data for broken_wilson_term slope comparison")

    print()

    # Save results to JSON
    output = {
        "gate4b": gate4b_results,
        "negative_controls": nc_results,
        "analysis_date": "2026-06-01",
        "data_sources": {
            "gate4b": str(gate4b_base),
            "negative_controls": str(nc_base),
        },
    }

    output_file = Path("reports/fss_slope_data_v0.1.24.json")
    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)

    print(f"📊 Raw data saved: {output_file}")
    print()


if __name__ == "__main__":
    main()
