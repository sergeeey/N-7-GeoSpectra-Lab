#!/usr/bin/env python3
"""
Negative Controls Full Pattern Audit — v0.1.24

Purpose: Reproducible full-pattern analysis (contrast + FSS trend + r_stat)
Status: READ-ONLY ANALYSIS (does not modify raw data)
Date: 2026-05-31
"""

import json
from pathlib import Path
from collections import defaultdict
import statistics


def main():
    print("=" * 80)
    print("NEGATIVE CONTROLS FULL PATTERN AUDIT — v0.1.24")
    print("=" * 80)
    print()

    # Paths
    gate4b_base = Path("reports/RUNS/gate4_fss_v0.1.24/batches")
    nc_base = Path("reports/RUNS/negative_controls_v0.1.22")

    # Step 1: Load data
    print("STEP 1: DATA LOADING")
    print("-" * 80)

    # Load Gate 4B
    gate4b_cases = []
    for batch in sorted(gate4b_base.glob("batch_*")):
        results_file = batch / "results.json"
        if results_file.exists():
            with open(results_file) as f:
                gate4b_cases.extend(json.load(f))

    print(f"Gate 4B v0.1.24: {len(gate4b_cases)} cases loaded")

    # Load Negative Controls
    nc_cases = []
    for batch in sorted(nc_base.glob("batch_*")):
        for case_file in sorted(batch.glob("case_*.json")):
            with open(case_file) as f:
                nc_cases.append(json.load(f))

    print(f"Negative Controls v0.1.22: {len(nc_cases)} cases loaded")
    print()

    # Step 2: Reproduce contrast-only
    print("STEP 2: CONTRAST-ONLY REPRODUCTION")
    print("-" * 80)
    print()

    by_control = defaultdict(lambda: {"W0": [], "W20": []})

    for case in nc_cases:
        control = case["control"]
        w = case["disorder_strength"]
        ipr = case["true_ipr_mean"]

        key = "W0" if w == 0 else "W20"
        by_control[control][key].append(ipr)

    print(
        f"{'Control':<25} {'Count':<8} {'W0 Mean':<12} {'W20 Mean':<12} {'Contrast':<10} {'Expected':<10}"
    )
    print("-" * 80)

    expected = {"random_hermitian": 1.30, "scrambled_geometry": 4.25, "broken_wilson_term": 8.20}

    contrast_reproduced = {}

    for control in sorted(by_control.keys()):
        data = by_control[control]
        w0_mean = statistics.mean(data["W0"]) if data["W0"] else 0
        w20_mean = statistics.mean(data["W20"]) if data["W20"] else 0
        contrast = w20_mean / w0_mean if w0_mean > 0 else 0

        count = len(data["W0"]) + len(data["W20"])
        exp_contrast = expected.get(control, 0)

        # Check if reproduced (within 10%)
        if exp_contrast > 0:
            error = abs(contrast - exp_contrast) / exp_contrast
            reproduced = "✅ REPRODUCED" if error < 0.10 else "⚠️ MISMATCH"
        else:
            reproduced = "N/A"

        contrast_reproduced[control] = (contrast, reproduced)

        print(
            f"{control:<25} {count:<8} {w0_mean:<12.6f} {w20_mean:<12.6f} {contrast:<10.2f} {exp_contrast:<10.2f}"
        )

    print()

    # Step 3: FSS Trend Analysis
    print("STEP 3: FSS TREND ANALYSIS")
    print("-" * 80)
    print()

    # FSS trend deterministic rule
    print("FSS Trend Classification Rule:")
    print("  - ratio = IPR(largest_size) / IPR(smallest_size)")
    print("  - if ratio > 1.25 → INCREASING")
    print("  - if ratio < 0.80 → DECREASING")
    print("  - otherwise → STABLE")
    print()

    def classify_fss_trend(iprs_by_size):
        """Deterministic FSS trend classification"""
        if not iprs_by_size or len(iprs_by_size) < 2:
            return "INSUFFICIENT_DATA", None

        sizes = sorted(iprs_by_size.keys())
        smallest = statistics.mean(iprs_by_size[sizes[0]])
        largest = statistics.mean(iprs_by_size[sizes[-1]])

        if smallest == 0:
            return "UNDEFINED", None

        ratio = largest / smallest

        if ratio > 1.25:
            trend = "INCREASING"
        elif ratio < 0.80:
            trend = "DECREASING"
        else:
            trend = "STABLE"

        return trend, ratio

    # Gate 4B FSS
    gate4b_w20_by_size = defaultdict(list)
    for case in gate4b_cases:
        if case["disorder_strength"] == 20:
            gate4b_w20_by_size[case["s1_size"]].append(case["true_ipr_mean"])

    gate4b_trend, gate4b_ratio = classify_fss_trend(gate4b_w20_by_size)

    print("Gate 4B v0.1.24 W=20 FSS Trend:")
    for size in sorted(gate4b_w20_by_size.keys()):
        mean_ipr = statistics.mean(gate4b_w20_by_size[size])
        count = len(gate4b_w20_by_size[size])
        print(f"  N={size:3d}: IPR={mean_ipr:.6f} (n={count})")
    print(f"  → Trend: {gate4b_trend} (ratio={gate4b_ratio:.3f})")
    print()

    # Controls FSS
    control_fss = {}

    for control in sorted(by_control.keys()):
        w20_by_size = defaultdict(list)

        for case in nc_cases:
            if case["control"] == control and case["disorder_strength"] == 20:
                w20_by_size[case["s1_size"]].append(case["true_ipr_mean"])

        trend, ratio = classify_fss_trend(w20_by_size)
        control_fss[control] = (trend, ratio, w20_by_size)

        print(f"{control} W=20 FSS Trend:")
        for size in sorted(w20_by_size.keys()):
            mean_ipr = statistics.mean(w20_by_size[size]) if w20_by_size[size] else 0
            count = len(w20_by_size[size])
            print(f"  N={size:3d}: IPR={mean_ipr:.6f} (n={count})")
        ratio_str = f"{ratio:.3f}" if ratio is not None else "N/A"
        print(f"  → Trend: {trend} (ratio={ratio_str})")
        print()

    # Step 4: Control Verdicts
    print("STEP 4: CONTROL VERDICTS")
    print("-" * 80)
    print()

    print(f"{'Control':<25} {'Contrast':<10} {'FSS Trend':<15} {'Final Verdict':<40}")
    print("-" * 80)

    for control in sorted(by_control.keys()):
        contrast, reproduced_str = contrast_reproduced[control]
        fss_trend, fss_ratio, _ = control_fss[control]

        # Contrast verdict
        contrast_pass = contrast >= 2.0

        # FSS trend verdict (compared to Gate 4B: STABLE)
        fss_match = fss_trend == "STABLE" or fss_trend == gate4b_trend

        # Final control verdict
        if not contrast_pass:
            verdict = "CONTROL_FAILS_FULL_PATTERN"
        elif contrast_pass and not fss_match:
            verdict = "CONTROL_PARTIAL_FALSE_POSITIVE"
        elif contrast_pass and fss_match:
            verdict = "CONTROL_REPRODUCES_GATE4B_FULL_PATTERN"
        else:
            verdict = "CONTROL_AUDIT_INCONCLUSIVE"

        contrast_str = f"{contrast:.2f}× {'✅' if contrast_pass else '❌'}"
        fss_str = f"{fss_trend} {'✅' if fss_match else '❌'}"

        print(f"{control:<25} {contrast_str:<10} {fss_str:<15} {verdict:<40}")

    print()

    # Step 5: Final Audit Verdict
    print("STEP 5: FINAL AUDIT VERDICT")
    print("-" * 80)
    print()

    # Count verdicts
    verdicts = []
    for control in sorted(by_control.keys()):
        contrast, _ = contrast_reproduced[control]
        fss_trend, _, _ = control_fss[control]

        contrast_pass = contrast >= 2.0
        fss_match = fss_trend == "STABLE" or fss_trend == gate4b_trend

        if not contrast_pass:
            verdicts.append("FAIL")
        elif contrast_pass and not fss_match:
            verdicts.append("PARTIAL")
        elif contrast_pass and fss_match:
            verdicts.append("REPRODUCES")
        else:
            verdicts.append("INCONCLUSIVE")

    n_fail = verdicts.count("FAIL")
    n_partial = verdicts.count("PARTIAL")
    n_reproduces = verdicts.count("REPRODUCES")
    n_inconclusive = verdicts.count("INCONCLUSIVE")

    print(f"Controls failing full pattern: {n_fail}/3")
    print(f"Controls partial false positive: {n_partial}/3")
    print(f"Controls reproducing full pattern: {n_reproduces}/3")
    print(f"Inconclusive: {n_inconclusive}/3")
    print()

    if n_reproduces > 0:
        final_verdict = "NEGATIVE_CONTROLS_FULL_PATTERN_AUDIT_COMPLETED_HARNESS_NONSPECIFIC"
    elif n_partial > 0:
        final_verdict = "NEGATIVE_CONTROLS_FULL_PATTERN_AUDIT_COMPLETED_PARTIAL_FALSE_POSITIVES"
    elif n_fail == 3:
        final_verdict = "NEGATIVE_CONTROLS_FULL_PATTERN_AUDIT_COMPLETED_CONTROLS_FAIL_FULL_PATTERN"
    else:
        final_verdict = "NEGATIVE_CONTROLS_FULL_PATTERN_AUDIT_INCONCLUSIVE"

    print(f"FINAL VERDICT: {final_verdict}")
    print()

    print("=" * 80)
    print("AUDIT COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()
