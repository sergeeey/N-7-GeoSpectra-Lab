"""Unified Result Reconciliation Audit — v0.1.24

Purpose: Re-read all Gate 4B v0.1.24 + Negative Controls v0.1.22 + diagnostics
using ONE loader and ONE metric formula to verify DISCRETIZATION_SENSITIVE /
GEOMETRY_AGNOSTIC verdict is reproducible.

READ-ONLY: Does NOT modify raw outputs or reports/RUNS.
"""

import json
import sys
from pathlib import Path
from typing import Any
from dataclasses import dataclass, field
from collections import defaultdict
import numpy as np
from scipy.stats import linregress

# === DATA STRUCTURES ===


@dataclass
class Case:
    """Normalized case representation."""

    run_id: str | None = None
    case_id: int | str | None = None
    family: str | None = None
    control_type: str | None = None
    wilson_mode: str | None = None
    discretization: str | None = None
    W: float | None = None
    seed: int | None = None
    s1_size: int | None = None
    N: int | None = None
    j_max: int | None = None
    matrix_dim: int | None = None
    true_ipr_mean: float | None = None
    r_stat: float | None = None
    runtime_seconds: float | None = None
    python_version: str | None = None
    numpy_version: str | None = None
    scipy_version: str | None = None
    git_commit: str | None = None
    source_file: str | None = None  # For tracing back to raw JSON


@dataclass
class GroupStats:
    """Aggregated statistics for one group."""

    name: str
    case_count: int = 0
    w0_count: int = 0
    w20_count: int = 0
    w0_mean_ipr: float | None = None
    w20_mean_ipr: float | None = None
    contrast: float | None = None
    fss_slope: float | None = None
    fss_r2: float | None = None
    fss_stderr: float | None = None
    trend: str = "INSUFFICIENT_DATA"
    mean_r_stat: float | None = None
    sizes: list[int] = field(default_factory=list)
    seeds: list[int] = field(default_factory=list)
    dimensions: list[int] = field(default_factory=list)
    python_versions: list[str] = field(default_factory=list)
    numpy_versions: list[str] = field(default_factory=list)
    scipy_versions: list[str] = field(default_factory=list)
    git_commits: list[str] = field(default_factory=list)


# === FILE LOADING ===


def load_cases_from_file(file_path: Path) -> list[Case]:
    """Load cases from a single JSON file (handles multiple formats)."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"⚠️ Skipped {file_path.name}: {e}", file=sys.stderr)
        return []

    # Format detection
    if isinstance(raw, list):
        # Gate 4B v0.1.24 format: results.json = list[dict]
        return [normalize_case(item, source=str(file_path)) for item in raw]
    elif isinstance(raw, dict):
        if "cases" in raw:
            # Batch summary format
            return [normalize_case(c, source=str(file_path)) for c in raw["cases"]]
        else:
            # Single case format (Negative Controls, Wilson Scrambled, etc.)
            return [normalize_case(raw, source=str(file_path))]
    else:
        print(f"⚠️ Unknown JSON format in {file_path.name}", file=sys.stderr)
        return []


def normalize_case(raw: dict, source: str) -> Case:
    """Extract Case fields from raw JSON (handles multiple naming schemes)."""
    case = Case()
    case.source_file = source

    # Case identifiers
    case.case_id = raw.get("case_id") or raw.get("id")
    case.run_id = raw.get("run_id")

    # Family and control type
    case.family = raw.get("family") or raw.get("s1_family")
    case.control_type = raw.get("control") or raw.get("control_type")
    case.wilson_mode = raw.get("wilson_mode") or raw.get("meta", {}).get("wilson_mode")

    # Determine discretization method
    if case.family == "spectral_circle":
        case.discretization = "FFT"
    elif case.family in ("ring", "wilson_ring"):
        case.discretization = "lattice"
    elif case.control_type in ("broken_wilson_term",):
        case.discretization = "lattice"  # scrambled Wilson uses lattice base
    elif case.control_type in ("random_hermitian", "scrambled_geometry"):
        case.discretization = "N/A"
    else:
        case.discretization = "UNKNOWN"

    # Physical parameters
    case.W = raw.get("disorder_strength")
    case.seed = raw.get("seed")
    case.s1_size = raw.get("s1_size")
    case.j_max = raw.get("j_max")

    # Matrix dimension
    case.N = raw.get("N")
    case.matrix_dim = raw.get("matrix_dim") or raw.get("meta", {}).get("total_dimension") or case.N

    # Metrics
    case.true_ipr_mean = raw.get("true_ipr_mean") or raw.get("mean_low_ipr")
    case.r_stat = raw.get("r_stat")
    case.runtime_seconds = raw.get("runtime_seconds") or raw.get("runtime_sec")

    # Environment metadata
    meta = raw.get("meta", {})
    case.python_version = meta.get("python_version")
    case.numpy_version = meta.get("numpy_version")
    case.scipy_version = meta.get("scipy_version")
    case.git_commit = meta.get("git_commit")

    return case


def load_all_datasets() -> dict[str, list[Case]]:
    """Load all relevant datasets from reports/RUNS."""
    base = Path("reports/RUNS")
    datasets = {}

    # Gate 4B v0.1.24 (batch results.json format)
    gate4b_dir = base / "gate4_fss_v0.1.24" / "batches"
    if gate4b_dir.exists():
        cases = []
        for batch_dir in sorted(gate4b_dir.glob("batch_*")):
            results_file = batch_dir / "results.json"
            if results_file.exists():
                cases.extend(load_cases_from_file(results_file))
        datasets["gate4b_v0.1.24"] = cases

    # Negative Controls v0.1.22
    neg_dir = base / "negative_controls_v0.1.22"
    if neg_dir.exists():
        cases = []
        for case_file in sorted(neg_dir.glob("*/case_*.json")):
            cases.extend(load_cases_from_file(case_file))
        datasets["negative_controls_v0.1.22"] = cases

    # Wilson Scrambled diagnostic
    wil_dir = base / "broken_wilson_scrambled_v0.1.22"
    if wil_dir.exists():
        cases = []
        for case_file in sorted(wil_dir.glob("*/case_*.json")):
            cases.extend(load_cases_from_file(case_file))
        datasets["wilson_scrambled_v0.1.22"] = cases

    # Spectral Circle Extended
    spec_dir = base / "spectral_circle_extended_v0.1.22"
    if spec_dir.exists():
        cases = []
        for case_file in sorted(spec_dir.glob("*/case_*.json")):
            cases.extend(load_cases_from_file(case_file))
        datasets["spectral_circle_extended_v0.1.22"] = cases

    return datasets


# === GROUP CLASSIFICATION ===


def classify_case_into_group(case: Case) -> str:
    """Assign case to a logical group for aggregation."""
    if case.control_type == "random_hermitian":
        return "random_hermitian"
    elif case.control_type == "scrambled_geometry":
        return "scrambled_geometry"
    elif case.control_type == "broken_wilson_term":
        return "wilson_scrambled"  # After code audit: broken_wilson = scrambled
    elif case.family == "spectral_circle":
        return "spectral_circle"
    elif case.family == "ring":
        return "ring"
    elif case.family == "wilson_ring":
        return "wilson_ring"
    else:
        return "UNKNOWN"


# === METRIC COMPUTATION ===


def compute_group_stats(cases: list[Case], group_name: str) -> GroupStats:
    """Compute aggregated statistics for one group."""
    stats = GroupStats(name=group_name)
    stats.case_count = len(cases)

    if not cases:
        return stats

    # Split by W=0 and W=20
    w0_cases = [c for c in cases if c.W == 0]
    w20_cases = [c for c in cases if c.W == 20]

    stats.w0_count = len(w0_cases)
    stats.w20_count = len(w20_cases)

    # Mean IPR at W=0 and W=20
    if w0_cases:
        w0_iprs = [c.true_ipr_mean for c in w0_cases if c.true_ipr_mean is not None]
        if w0_iprs:
            stats.w0_mean_ipr = float(np.mean(w0_iprs))

    if w20_cases:
        w20_iprs = [c.true_ipr_mean for c in w20_cases if c.true_ipr_mean is not None]
        if w20_iprs:
            stats.w20_mean_ipr = float(np.mean(w20_iprs))

    # Contrast = W20 / W0
    if stats.w0_mean_ipr and stats.w20_mean_ipr and stats.w0_mean_ipr > 0:
        stats.contrast = stats.w20_mean_ipr / stats.w0_mean_ipr

    # FSS slope: dlog(IPR)/dlog(N) for W=20 only
    if len(w20_cases) >= 3:
        stats.fss_slope, stats.fss_r2, stats.fss_stderr = compute_fss_slope(w20_cases)
        stats.trend = classify_trend(stats.fss_slope)

    # Mean r_stat
    r_stats = [c.r_stat for c in cases if c.r_stat is not None]
    if r_stats:
        stats.mean_r_stat = float(np.mean(r_stats))

    # Coverage
    stats.sizes = sorted(set(c.s1_size for c in cases if c.s1_size is not None))
    stats.seeds = sorted(set(c.seed for c in cases if c.seed is not None))
    stats.dimensions = sorted(set(c.matrix_dim for c in cases if c.matrix_dim is not None))

    # Environment metadata
    stats.python_versions = sorted(set(c.python_version for c in cases if c.python_version))
    stats.numpy_versions = sorted(set(c.numpy_version for c in cases if c.numpy_version))
    stats.scipy_versions = sorted(set(c.scipy_version for c in cases if c.scipy_version))
    stats.git_commits = sorted(set(c.git_commit for c in cases if c.git_commit))

    return stats


def compute_fss_slope(w20_cases: list[Case]) -> tuple[float, float, float]:
    """Compute FSS slope: dlog(IPR)/dlog(N) via linear regression."""
    # Group by size
    by_size = defaultdict(list)
    for case in w20_cases:
        if case.s1_size and case.true_ipr_mean and case.true_ipr_mean > 0:
            by_size[case.s1_size].append(case.true_ipr_mean)

    if len(by_size) < 2:
        return (0.0, 0.0, 0.0)

    sizes = sorted(by_size.keys())
    mean_iprs = [np.mean(by_size[size]) for size in sizes]

    log_sizes = np.log(sizes)
    log_iprs = np.log(mean_iprs)

    result = linregress(log_sizes, log_iprs)
    slope = float(result.slope)
    r2 = float(result.rvalue**2)
    stderr = float(result.stderr)

    return (slope, r2, stderr)


def classify_trend(slope: float | None) -> str:
    """Classify FSS trend based on slope."""
    if slope is None:
        return "INSUFFICIENT_DATA"
    elif slope > 0.10:
        return "INCREASING"
    elif -0.10 <= slope <= 0.10:
        return "STABLE"
    elif slope < -0.10:
        return "WEAKENING"
    else:
        return "MIXED"


# === CONSISTENCY CHECKS ===


def check_dimension_consistency(group_stats: list[GroupStats]) -> dict:
    """Check for dimension mismatches across groups."""
    report = {}
    for stats in group_stats:
        if len(stats.dimensions) > 1:
            report[stats.name] = {
                "status": "MISMATCH",
                "dimensions": stats.dimensions,
                "note": "Multiple dimensions found — check s3_dimension bug history",
            }
        elif len(stats.dimensions) == 1:
            report[stats.name] = {"status": "CONSISTENT", "dimension": stats.dimensions[0]}
        else:
            report[stats.name] = {"status": "MISSING", "note": "No dimension metadata available"}
    return report


def check_environment_consistency(group_stats: list[GroupStats]) -> dict:
    """Check Python/NumPy/SciPy version consistency."""
    all_py = []
    all_np = []
    all_sp = []
    all_git = []

    for stats in group_stats:
        all_py.extend(stats.python_versions)
        all_np.extend(stats.numpy_versions)
        all_sp.extend(stats.scipy_versions)
        all_git.extend(stats.git_commits)

    return {
        "python_versions": sorted(set(all_py)) if all_py else ["METADATA_MISSING"],
        "numpy_versions": sorted(set(all_np)) if all_np else ["METADATA_MISSING"],
        "scipy_versions": sorted(set(all_sp)) if all_sp else ["METADATA_MISSING"],
        "git_commits": sorted(set(all_git)) if all_git else ["METADATA_MISSING"],
    }


# === MAIN EXECUTION ===


def main():
    print("=" * 70)
    print("UNIFIED RESULT RECONCILIATION AUDIT — v0.1.24")
    print("=" * 70)
    print()

    # Phase 1: Load datasets
    print("📂 Loading datasets...")
    datasets = load_all_datasets()

    print(f"   ✅ Loaded {len(datasets)} datasets:")
    for name, cases in datasets.items():
        print(f"      - {name}: {len(cases)} cases")
    print()

    # Phase 2: Classify into groups
    print("📊 Classifying cases into groups...")
    all_cases = []
    for cases in datasets.values():
        all_cases.extend(cases)

    grouped = defaultdict(list)
    for case in all_cases:
        group = classify_case_into_group(case)
        grouped[group].append(case)

    print(f"   ✅ Found {len(grouped)} groups:")
    for group_name in sorted(grouped.keys()):
        print(f"      - {group_name}: {len(grouped[group_name])} cases")
    print()

    # Phase 3: Compute statistics
    print("🔢 Computing group statistics...")
    group_stats = []
    for group_name in sorted(grouped.keys()):
        stats = compute_group_stats(grouped[group_name], group_name)
        group_stats.append(stats)

    print(f"   ✅ Statistics computed for {len(group_stats)} groups")
    print()

    # Phase 4: Consistency checks
    print("🔍 Running consistency checks...")
    dim_check = check_dimension_consistency(group_stats)
    env_check = check_environment_consistency(group_stats)
    print("   ✅ Consistency checks complete")
    print()

    # Phase 5: Print summary table
    print("=" * 120)
    print("UNIFIED RESULTS TABLE")
    print("=" * 120)
    print(
        f"{'Group':<20} {'Cases':>6} {'W0':>4} {'W20':>4} {'W0 IPR':>10} {'W20 IPR':>10} {'Contrast':>9} {'FSS Slope':>10} {'Trend':>12} {'R²':>6}"
    )
    print("-" * 120)

    for stats in group_stats:
        w0_str = f"{stats.w0_mean_ipr:.4f}" if stats.w0_mean_ipr else "N/A"
        w20_str = f"{stats.w20_mean_ipr:.4f}" if stats.w20_mean_ipr else "N/A"
        contrast_str = f"{stats.contrast:.2f}×" if stats.contrast else "N/A"
        slope_str = f"{stats.fss_slope:+.4f}" if stats.fss_slope is not None else "N/A"
        r2_str = f"{stats.fss_r2:.3f}" if stats.fss_r2 is not None else "N/A"

        print(
            f"{stats.name:<20} {stats.case_count:>6} {stats.w0_count:>4} {stats.w20_count:>4} {w0_str:>10} {w20_str:>10} {contrast_str:>9} {slope_str:>10} {stats.trend:>12} {r2_str:>6}"
        )

    print("=" * 120)
    print()

    # Phase 6: Dimension consistency report
    print("=" * 70)
    print("DIMENSION CONSISTENCY CHECK")
    print("=" * 70)
    for group_name, result in dim_check.items():
        status = result["status"]
        if status == "CONSISTENT":
            print(f"   ✅ {group_name}: {result['dimension']}")
        elif status == "MISMATCH":
            print(f"   ⚠️ {group_name}: MISMATCH — found {result['dimensions']}")
            print(f"      Note: {result['note']}")
        elif status == "MISSING":
            print(f"   ⚠️ {group_name}: METADATA_MISSING")
    print()

    # Phase 7: Environment consistency report
    print("=" * 70)
    print("ENVIRONMENT METADATA")
    print("=" * 70)
    print(f"   Python versions:  {', '.join(env_check['python_versions'])}")
    print(f"   NumPy versions:   {', '.join(env_check['numpy_versions'])}")
    print(f"   SciPy versions:   {', '.join(env_check['scipy_versions'])}")
    print(f"   Git commits:      {', '.join(env_check['git_commits'][:5])}")
    if len(env_check["git_commits"]) > 5:
        print(f"                     ... and {len(env_check['git_commits']) - 5} more")
    print()

    # Phase 8: Verdict stability check
    print("=" * 70)
    print("VERDICT STABILITY CHECK")
    print("=" * 70)

    verdict_checks = {
        "random_hermitian WEAKENING": grouped["random_hermitian"]
        and any(s.name == "random_hermitian" and s.trend == "WEAKENING" for s in group_stats),
        "scrambled_geometry WEAKENING": grouped["scrambled_geometry"]
        and any(s.name == "scrambled_geometry" and s.trend == "WEAKENING" for s in group_stats),
        "wilson_scrambled STABLE": grouped["wilson_scrambled"]
        and any(s.name == "wilson_scrambled" and s.trend == "STABLE" for s in group_stats),
        "spectral_circle WEAKENING": grouped["spectral_circle"]
        and any(s.name == "spectral_circle" and s.trend == "WEAKENING" for s in group_stats),
        "ring STABLE": grouped["ring"]
        and any(s.name == "ring" and s.trend == "STABLE" for s in group_stats),
        "wilson_ring STABLE": grouped["wilson_ring"]
        and any(s.name == "wilson_ring" and s.trend == "STABLE" for s in group_stats),
    }

    for check, result in verdict_checks.items():
        status = "✅" if result else "❌"
        print(f"   {status} {check}")

    print()

    # Phase 9: Final verdict
    print("=" * 70)
    print("FINAL VERDICT")
    print("=" * 70)

    all_passed = all(verdict_checks.values())
    any_dim_mismatch = any(r["status"] == "MISMATCH" for r in dim_check.values())
    metadata_missing = env_check["python_versions"] == ["METADATA_MISSING"]

    if all_passed and not any_dim_mismatch:
        verdict = "RECONCILIATION_VERIFIED_DISCRETIZATION_SENSITIVE"
        print(f"   ✅ {verdict}")
        print("      All key findings reproduced with unified loader.")
    elif all_passed and any_dim_mismatch:
        verdict = "RECONCILIATION_SUPPORTS_HYPOTHESIS_BUT_DIMENSION_MISMATCH_DETECTED"
        print(f"   ⚠️ {verdict}")
        print("      Findings consistent but dimension inconsistencies found.")
    elif not all_passed and not any_dim_mismatch:
        verdict = "RECONCILIATION_INCONSISTENT_RESULTS_MANUAL_REVIEW_REQUIRED"
        print(f"   ❌ {verdict}")
        print("      Some expected trends NOT reproduced — manual review needed.")
    else:
        verdict = "RECONCILIATION_INCONCLUSIVE"
        print(f"   ❌ {verdict}")
        print("      Multiple issues detected.")

    if metadata_missing:
        print("      ⚠️ Environment metadata missing from most runs.")

    print()
    print("=" * 70)
    print("Audit complete. Output written to stdout only (read-only mode).")
    print("=" * 70)


if __name__ == "__main__":
    main()
