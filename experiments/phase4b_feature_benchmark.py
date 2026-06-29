"""
Phase 4B Feature Benchmark V2.

Tests whether better spectral normalization, unfolding, heat/zeta signatures,
moments, and multi-feature fingerprints improve recoverability against the
strict same-geometry disorder baseline.

Scope: synthetic/toy benchmark only.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from phase4b_recoverability_benchmark import (
    DEFAULT_K_VALUES,
    GEOMETRIES,
    PAIRS,
    W_VALUES,
    add_disorder,
    auc_score,
    bootstrap_ci,
    build_laps,
    classify_phase,
    relative_separation,
    spectrum,
)


OUT = Path(__file__).parent / "20260629-phase4b"
DEFAULT_SEEDS_20 = [
    42,
    123,
    999,
    777,
    100,
    200,
    300,
    400,
    500,
    600,
    700,
    800,
    900,
    1000,
    1100,
    1200,
    1300,
    1400,
    1500,
    1600,
]


def safe_stats(values: np.ndarray) -> tuple[float, float, float, float]:
    values = np.asarray(values, dtype=float)
    if values.size == 0:
        return 0.0, 0.0, 0.0, 0.0
    mean = float(np.mean(values))
    std = float(np.std(values))
    if std < 1e-12:
        return mean, 0.0, 0.0, 0.0
    centered = (values - mean) / std
    skew = float(np.mean(centered**3))
    kurt = float(np.mean(centered**4))
    return mean, std, skew, kurt


def normalized_spectrum(ev: np.ndarray) -> np.ndarray:
    ev = np.asarray(ev, dtype=float)
    ev = ev - float(np.min(ev))
    scale = float(np.max(ev))
    if scale <= 1e-12:
        return np.zeros_like(ev)
    return ev / scale


def normalized_gaps(ev: np.ndarray) -> np.ndarray:
    evn = normalized_spectrum(ev)
    gaps = np.diff(evn)
    mean_gap = float(np.mean(gaps)) if gaps.size else 0.0
    if mean_gap <= 1e-12:
        return np.zeros_like(gaps)
    return gaps / mean_gap


def gap_ratios(ev: np.ndarray) -> np.ndarray:
    gaps = np.diff(np.asarray(ev, dtype=float))
    ratios = []
    for i in range(len(gaps) - 1):
        a = abs(float(gaps[i]))
        b = abs(float(gaps[i + 1]))
        denom = max(a, b)
        ratios.append(0.0 if denom <= 1e-12 else min(a, b) / denom)
    return np.asarray(ratios, dtype=float)


def fixed_len(values: np.ndarray, length: int) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    if values.size == 0:
        return np.zeros(length)
    x_old = np.linspace(0.0, 1.0, values.size)
    x_new = np.linspace(0.0, 1.0, length)
    return np.interp(x_new, x_old, values)


def hist_feature(values: np.ndarray, bins: int, value_range: tuple[float, float]) -> np.ndarray:
    hist, _ = np.histogram(values, bins=bins, range=value_range, density=False)
    hist = hist.astype(float)
    total = float(np.sum(hist))
    return hist / total if total > 0 else hist


def heat_zeta_feature(ev: np.ndarray) -> np.ndarray:
    evn = normalized_spectrum(ev)
    eps = 1e-6
    heat_t = np.asarray([0.1, 0.3, 1.0, 3.0, 10.0], dtype=float)
    zeta_s = np.asarray([0.5, 1.0, 2.0, 3.0], dtype=float)
    heat = np.asarray([np.mean(np.exp(-t * evn)) for t in heat_t], dtype=float)
    zeta = np.asarray([np.mean((evn + eps) ** (-s)) for s in zeta_s], dtype=float)
    zeta = np.log1p(np.clip(zeta, 0.0, 1e6))
    return np.concatenate([heat, zeta])


def moment_feature(ev: np.ndarray) -> np.ndarray:
    evn = normalized_spectrum(ev)
    gaps = normalized_gaps(ev)
    ratios = gap_ratios(ev)
    return np.asarray(
        [
            *safe_stats(evn),
            *safe_stats(gaps),
            *safe_stats(ratios),
        ],
        dtype=float,
    )


def feature_vector(ev: np.ndarray, mode: str) -> np.ndarray:
    evn = normalized_spectrum(ev)
    gaps = normalized_gaps(ev)
    ratios = gap_ratios(ev)

    if mode == "aligned_density":
        return hist_feature(evn, bins=16, value_range=(0.0, 1.0))
    if mode == "unfolded_spacing":
        return hist_feature(np.clip(gaps, 0.0, 4.0), bins=16, value_range=(0.0, 4.0))
    if mode == "relative_spectrum":
        return fixed_len(evn, 24)
    if mode == "gap_ratios":
        return hist_feature(ratios, bins=12, value_range=(0.0, 1.0))
    if mode == "moments":
        return moment_feature(ev)
    if mode == "heat_zeta":
        return heat_zeta_feature(ev)
    if mode == "multi_feature":
        return np.concatenate(
            [
                feature_vector(ev, "aligned_density"),
                feature_vector(ev, "unfolded_spacing"),
                feature_vector(ev, "relative_spectrum"),
                feature_vector(ev, "gap_ratios"),
                moment_feature(ev),
                heat_zeta_feature(ev),
            ]
        )
    raise ValueError(f"Unknown feature mode: {mode}")


FEATURE_MODES = [
    "aligned_density",
    "unfolded_spacing",
    "relative_spectrum",
    "gap_ratios",
    "moments",
    "heat_zeta",
    "multi_feature",
]


def standardize_pair_features(features: dict[tuple[str, int], np.ndarray], pair, seeds):
    samples = []
    for geom in pair:
        for seed in seeds:
            value = features.get((geom, seed))
            if value is not None:
                samples.append(value)
    if not samples:
        return features
    matrix = np.vstack(samples)
    center = np.median(matrix, axis=0)
    spread = np.percentile(matrix, 75, axis=0) - np.percentile(matrix, 25, axis=0)
    spread = np.where(spread < 1e-9, np.std(matrix, axis=0), spread)
    spread = np.where(spread < 1e-9, 1.0, spread)
    return {key: (value - center) / spread for key, value in features.items()}


def euclidean(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.linalg.norm(np.asarray(a, dtype=float) - np.asarray(b, dtype=float)))


def pair_distances(features, pair, seeds, calibrated: bool):
    values = standardize_pair_features(features, pair, seeds) if calibrated else features
    g1, g2 = pair
    between = []
    within = []

    for seed_a in seeds:
        for seed_b in seeds:
            fa = values.get((g1, seed_a))
            fb = values.get((g2, seed_b))
            if fa is not None and fb is not None:
                between.append(euclidean(fa, fb))

    for geom in pair:
        for i, seed_a in enumerate(seeds):
            for seed_b in seeds[i + 1 :]:
                fa = values.get((geom, seed_a))
                fb = values.get((geom, seed_b))
                if fa is not None and fb is not None:
                    within.append(euclidean(fa, fb))

    return between, within


def summarize_best(results):
    best = {}
    for row in results:
        key = (row["W"], row["N"], row["k"], row["pair"])
        old = best.get(key)
        if old is None or (row["auc"] or -1.0) > (old["auc"] or -1.0):
            best[key] = row
    return list(best.values())


def run(args):
    OUT.mkdir(exist_ok=True)
    seeds = DEFAULT_SEEDS_20[: args.seeds]
    results = []

    print("=" * 76)
    print("PHASE 4B FEATURE BENCHMARK V2")
    print(f"N={args.n_values} W={W_VALUES} seeds={len(seeds)} k={args.k_values}")
    print(f"modes={FEATURE_MODES} calibrated={args.calibrated}")
    print("=" * 76)

    for n in args.n_values:
        print(f"\n[N={n}] Building base Laplacians")
        laps = build_laps(n)
        for w in W_VALUES:
            for k in args.k_values:
                print(f"  W={w:2d} k={k:2d}: spectra", end="", flush=True)
                spectra = {}
                for geom in GEOMETRIES:
                    for seed in seeds:
                        lap = add_disorder(laps[geom], w, seed)
                        spectra[(geom, seed)] = spectrum(lap, k)
                print(" features", end="", flush=True)

                mode_features = {}
                for mode in FEATURE_MODES:
                    mode_features[mode] = {
                        key: feature_vector(ev, mode)
                        for key, ev in spectra.items()
                        if ev is not None
                    }
                print(" done")

                for mode in FEATURE_MODES:
                    for calibrated in args.calibrated:
                        for pair in PAIRS:
                            between, within = pair_distances(
                                mode_features[mode],
                                pair,
                                seeds,
                                calibrated=calibrated,
                            )
                            auc = auc_score(between, within)
                            sep = relative_separation(between, within)
                            auc_ci = bootstrap_ci(
                                between,
                                within,
                                auc_score,
                                args.bootstrap,
                                seed=30_000 + int(w) + k + len(mode),
                            )
                            sep_ci = bootstrap_ci(
                                between,
                                within,
                                relative_separation,
                                args.bootstrap,
                                seed=40_000 + int(w) + k + len(mode),
                            )
                            phase = classify_phase(auc, sep)
                            results.append(
                                {
                                    "W": w,
                                    "N": n,
                                    "k": k,
                                    "pair": f"{pair[0]}_vs_{pair[1]}",
                                    "feature_mode": mode,
                                    "pair_calibrated": calibrated,
                                    "auc": auc,
                                    "auc_ci95": auc_ci,
                                    "relative_separation": sep,
                                    "relative_separation_ci95": sep_ci,
                                    "mean_between": float(np.mean(between)) if between else None,
                                    "mean_within": float(np.mean(within)) if within else None,
                                    "n_between": len(between),
                                    "n_within": len(within),
                                    "phase": phase,
                                }
                            )

                best_here = summarize_best(
                    [
                        row
                        for row in results
                        if row["W"] == w and row["N"] == n and row["k"] == k
                    ]
                )
                recovered = sum(1 for row in best_here if row["phase"] == "recoverable")
                degraded = sum(1 for row in best_here if row["phase"] == "degraded")
                print(f"    best-by-pair: recoverable={recovered} degraded={degraded}")

    by_cell = summarize_best(results)
    for row in by_cell:
        row["best_of_feature_search"] = True

    payload = {
        "protocol": "phase4b_feature_benchmark_v2",
        "scope": "synthetic_toy_recoverability_benchmark",
        "n_values": args.n_values,
        "w_values": W_VALUES,
        "k_values": args.k_values,
        "n_seeds": len(seeds),
        "feature_modes": FEATURE_MODES,
        "calibration_modes": args.calibrated,
        "results": results,
        "best_by_cell": by_cell,
    }

    out_path = OUT / args.output
    with open(out_path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
    print(f"\nSaved: {out_path}")
    return payload


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", type=int, default=20)
    parser.add_argument("--n-values", type=int, nargs="+", default=[300])
    parser.add_argument("--k-values", type=int, nargs="+", default=DEFAULT_K_VALUES)
    parser.add_argument("--bootstrap", type=int, default=100)
    parser.add_argument(
        "--output",
        default="phase4b_feature_benchmark_results.json",
    )
    parser.add_argument(
        "--calibration",
        choices=["both", "raw", "pair"],
        default="both",
    )
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    if args.quick:
        args.seeds = 5
        args.n_values = [300]
        args.k_values = [15]
        args.bootstrap = 25
        args.output = "phase4b_feature_benchmark_quick_results.json"
    if args.seeds < 2 or args.seeds > len(DEFAULT_SEEDS_20):
        raise SystemExit(f"--seeds must be in [2, {len(DEFAULT_SEEDS_20)}]")
    args.calibrated = {
        "both": [False, True],
        "raw": [False],
        "pair": [True],
    }[args.calibration]
    return args


if __name__ == "__main__":
    run(parse_args())
