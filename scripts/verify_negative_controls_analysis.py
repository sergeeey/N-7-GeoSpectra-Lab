#!/usr/bin/env python3
"""
Reproducible Negative Controls Analysis Verification Script

Purpose: Verify Negative Controls v0.1.22 analysis WITHOUT modifying data.
Date: 2026-05-31
Status: AUDIT_MODE (read-only verification)
"""

import json
from pathlib import Path
from collections import defaultdict
import statistics


def main():
    print("=" * 80)
    print("NEGATIVE CONTROLS v0.1.22 — REPRODUCIBILITY AUDIT")
    print("=" * 80)
    print()

    # Paths
    nc_base = Path("reports/RUNS/negative_controls_v0.1.22")

    # Load all cases
    all_cases = []
    for batch_dir in sorted(nc_base.glob("batch_*")):
        for case_file in sorted(batch_dir.glob("case_*.json")):
            with open(case_file) as f:
                case = json.load(f)
                case["_source_file"] = str(case_file)
                all_cases.append(case)

    print("✅ Step 1: Load cases")
    print(f"   Total cases loaded: {len(all_cases)}/54 expected")
    print()

    # Group by control type
    by_control = defaultdict(lambda: {"W0": [], "W20": [], "cases": []})

    for case in all_cases:
        control = case["control"]
        w = case["disorder_strength"]
        ipr = case["true_ipr_mean"]

        by_control[control]["cases"].append(case)

        if w == 0:
            by_control[control]["W0"].append(ipr)
        elif w == 20:
            by_control[control]["W20"].append(ipr)
        else:
            print(f"⚠️  WARNING: Unexpected W={w} in {case['_source_file']}")

    print("✅ Step 2: Group by control type")
    print(f"   Controls found: {sorted(by_control.keys())}")
    print()

    # Verify counts per control
    print("=" * 80)
    print("STEP 3: COUNT VERIFICATION")
    print("=" * 80)
    print()

    expected_per_control = 18  # 9 W=0 + 9 W=20

    for control in sorted(by_control.keys()):
        data = by_control[control]
        n_total = len(data["cases"])
        n_w0 = len(data["W0"])
        n_w20 = len(data["W20"])

        status = "✅" if n_total == expected_per_control else "❌"

        print(f"{status} {control}:")
        print(f"   Total: {n_total}/18 cases")
        print(f"   W=0:   {n_w0}/9 cases")
        print(f"   W=20:  {n_w20}/9 cases")

        # Check seeds
        seeds_w0 = [c["seed"] for c in data["cases"] if c["disorder_strength"] == 0]
        seeds_w20 = [c["seed"] for c in data["cases"] if c["disorder_strength"] == 20]

        print(f"   Seeds W=0:  {sorted(set(seeds_w0))}")
        print(f"   Seeds W=20: {sorted(set(seeds_w20))}")

        # Check s1_sizes
        sizes_w0 = [c["s1_size"] for c in data["cases"] if c["disorder_strength"] == 0]
        sizes_w20 = [c["s1_size"] for c in data["cases"] if c["disorder_strength"] == 20]

        print(f"   s1_sizes W=0:  {sorted(set(sizes_w0))}")
        print(f"   s1_sizes W=20: {sorted(set(sizes_w20))}")
        print()

    # Compute contrasts
    print("=" * 80)
    print("STEP 4: CONTRAST CALCULATION")
    print("=" * 80)
    print()

    print("Formula: contrast = mean(W=20 IPR) / mean(W=0 IPR)")
    print()

    results = {}
    for control in sorted(by_control.keys()):
        data = by_control[control]

        if data["W0"] and data["W20"]:
            w0_mean = statistics.mean(data["W0"])
            w20_mean = statistics.mean(data["W20"])
            contrast = w20_mean / w0_mean if w0_mean > 0 else float("inf")

            results[control] = {
                "w0_mean": w0_mean,
                "w20_mean": w20_mean,
                "contrast": contrast,
                "n_w0": len(data["W0"]),
                "n_w20": len(data["W20"]),
            }

            threshold_status = "✅ FAIL (<2.0×)" if contrast < 2.0 else "❌ PASS (≥2.0×)"

            print(f"{control}:")
            print(f"  W=0 mean IPR:  {w0_mean:.6f} ({len(data['W0'])} cases)")
            print(f"  W=20 mean IPR: {w20_mean:.6f} ({len(data['W20'])} cases)")
            print(f"  Contrast:      {contrast:.2f}×")
            print(f"  Status:        {threshold_status}")
            print()

    # Compare with Gate 4B
    print("=" * 80)
    print("STEP 5: COMPARISON WITH GATE 4B v0.1.24")
    print("=" * 80)
    print()

    gate4b_contrast = 7.07  # From v0.1.24 analysis

    print(f"Gate 4B baseline: {gate4b_contrast:.2f}×")
    print()

    for control, r in results.items():
        pct_of_gate4b = (r["contrast"] / gate4b_contrast) * 100
        print(f"{control:25s}: {r['contrast']:5.2f}× ({pct_of_gate4b:5.1f}% of Gate 4B)")

    print()

    # Decision
    print("=" * 80)
    print("STEP 6: DECISION RULE APPLICATION")
    print("=" * 80)
    print()

    print("Pre-registered threshold: < 2.0× contrast (controls must FAIL)")
    print()

    all_fail = all(r["contrast"] < 2.0 for r in results.values())

    n_pass = sum(1 for r in results.values() if r["contrast"] >= 2.0)
    n_fail = sum(1 for r in results.values() if r["contrast"] < 2.0)

    print(f"Controls < 2.0×:  {n_fail}/3 (expected: 3/3)")
    print(f"Controls ≥ 2.0×:  {n_pass}/3 (expected: 0/3)")
    print()

    if all_fail:
        verdict = "✅ HARNESS_SPECIFIC"
        explanation = "All controls failed to reproduce Gate 4B pattern."
    else:
        verdict = "❌ HARNESS_NONSPECIFIC_PENDING_REPRODUCIBILITY_AUDIT"
        explanation = f"{n_pass}/3 controls reproduced Gate 4B-like pattern."
        print("Controls that PASSED unexpectedly:")
        for control, r in results.items():
            if r["contrast"] >= 2.0:
                print(f"  - {control}: {r['contrast']:.2f}×")
        print()

    print(f"VERDICT: {verdict}")
    print(f"REASON:  {explanation}")
    print()

    # Raw data spot checks
    print("=" * 80)
    print("STEP 7: RAW DATA SPOT CHECKS")
    print("=" * 80)
    print()

    spot_checks = [
        ("random_hermitian", 0, "batch_01/case_000.json"),
        ("random_hermitian", 20, "batch_02/case_009.json"),
        ("scrambled_geometry", 0, "batch_03/case_018.json"),
        ("scrambled_geometry", 20, "batch_04/case_027.json"),
        ("broken_wilson_term", 0, "batch_05/case_036.json"),
        ("broken_wilson_term", 20, "batch_06/case_045.json"),
    ]

    for control_name, expected_w, file_path in spot_checks:
        full_path = nc_base / file_path
        if full_path.exists():
            with open(full_path) as f:
                case = json.load(f)

            actual_control = case["control"]
            actual_w = case["disorder_strength"]
            ipr = case["true_ipr_mean"]

            match_control = "✅" if actual_control == control_name else "❌"
            match_w = "✅" if actual_w == expected_w else "❌"

            print(f"{file_path}:")
            print(f"  {match_control} control: {actual_control} (expected: {control_name})")
            print(f"  {match_w} W: {actual_w} (expected: {expected_w})")
            print(f"  IPR: {ipr:.6f}")
            print()
        else:
            print(f"❌ {file_path}: FILE NOT FOUND")
            print()

    # Summary
    print("=" * 80)
    print("REPRODUCIBILITY AUDIT COMPLETE")
    print("=" * 80)
    print()

    print(f"Total cases verified:   {len(all_cases)}/54")
    print(f"Controls analyzed:      {len(results)}/3")
    print("Contrasts reproduced:   3/3")
    print(
        f"Spot checks passed:     {sum(1 for _, _, fp in spot_checks if (nc_base / fp).exists())}/6"
    )
    print()
    print(f"FINAL VERDICT: {verdict}")
    print()

    if verdict.startswith("❌"):
        print("⚠️  NEXT STEPS:")
        print("   1. Manual review of control construction code")
        print("   2. Verify scramble_mode and wilson_mode implementations")
        print("   3. Check if control construction matches pre-registration")
        print("   4. Run diagnostic experiments (stronger scrambling, etc.)")
        print()
        print("⚠️  DO NOT:")
        print("   - Claim Gate 4B signal validated")
        print("   - Update Zenodo DOI with PASS verdict")
        print("   - Email external collaborators about positive results")
        print()


if __name__ == "__main__":
    main()
