"""
Phase 4B Recoverability Benchmark.

This is the benchmark replacement for the legacy fixed-threshold phase diagram.
It measures cross-geometry spectral separation against same-geometry seed
variation using AUC, relative separation, bootstrap confidence intervals, and
k=15/k=30 comparison.

Scope: synthetic/toy benchmark only; not a proof of physics.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import warnings
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent.parent))

from cc_toy_lab.geometry.graph_laplacian import build_knn_graph_laplacian


W_VALUES = [0, 1, 2, 5, 8, 10, 12, 15, 18, 20, 25, 30]
N_CURVED = [300]
PAIRS = [("T4", "S3xS1"), ("T4", "S2xS2"), ("S3xS1", "S2xS2")]
GEOMETRIES = ["T4", "S3xS1", "S2xS2"]
DEFAULT_SEEDS = [42, 123, 999, 777, 100, 200, 300, 400, 500, 600]
DEFAULT_K_VALUES = [15, 30]
OUT = Path(__file__).parent / "20260629-phase4b"


def t4_lap(n: int):
    main = 2.0 * np.ones(n)
    off = -1.0 * np.ones(n - 1)
    lap_1d = sparse.diags([off, main, off], [-1, 0, 1], format="csr")
    lap_1d[0, -1], lap_1d[-1, 0] = -1.0, -1.0
    ident = sparse.eye(n, format="csr")
    return (
        sparse.kron(sparse.kron(sparse.kron(lap_1d, ident), ident), ident)
        + sparse.kron(sparse.kron(sparse.kron(ident, lap_1d), ident), ident)
        + sparse.kron(sparse.kron(sparse.kron(ident, ident), lap_1d), ident)
        + sparse.kron(sparse.kron(sparse.kron(ident, ident), ident), lap_1d)
    )


def sphere(dim: int, n: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    points = rng.standard_normal((n, dim + 1))
    return points / np.linalg.norm(points, axis=1, keepdims=True)


def build_laps(n: int, seed: int = 42):
    n3 = max(10, int(np.sqrt(n)))
    n1 = max(5, n // n3)
    s3 = sphere(3, n3, seed)
    rng = np.random.default_rng(seed + 1)
    angles = rng.uniform(0, 2 * np.pi, n1)
    s1 = np.column_stack([np.cos(angles), np.sin(angles)])
    s31 = np.array([np.concatenate([x, y]) for x in s3 for y in s1])

    na = max(5, int(np.sqrt(n)))
    nb = max(5, n // na)
    sa = sphere(2, na, seed)
    sb = sphere(2, nb, seed + 1)
    s22 = np.array([np.concatenate([x, y]) for x in sa for y in sb])

    laps = {"T4": t4_lap(6)}
    for name, points in [("S3xS1", s31), ("S2xS2", s22)]:
        graph_lap = build_knn_graph_laplacian(
            points,
            k=min(12, len(points) - 1),
            normalized=True,
        )
        laps[name] = graph_lap.laplacian
    return laps


def add_disorder(lap, w: float, seed: int):
    if w == 0:
        return lap
    rng = np.random.default_rng(seed)
    return lap + sparse.diags(rng.uniform(-w, w, lap.shape[0]), format="csr")


def spectrum(lap, k: int):
    n0 = lap.shape[0]
    k = min(k, n0 - 2)
    try:
        eigenvalues = eigsh(lap, k=k, which="SM", return_eigenvectors=False, tol=1e-8)
    except Exception:
        return None
    eigenvalues = np.sort(np.real(eigenvalues))
    eigenvalues = eigenvalues[eigenvalues > 1e-10]
    if len(eigenvalues) < 3:
        return None
    return eigenvalues


def spectral_density_distance(ev_a: np.ndarray, ev_b: np.ndarray, bins: int = 15) -> float:
    if len(ev_a) < 2 or len(ev_b) < 2:
        return float("nan")
    lo = min(float(np.min(ev_a)), float(np.min(ev_b)))
    hi = max(float(np.max(ev_a)), float(np.max(ev_b)))
    if hi <= lo:
        return 0.0
    edges = np.linspace(lo, hi, bins + 1)
    hist_a, _ = np.histogram(ev_a, bins=edges, density=True)
    hist_b, _ = np.histogram(ev_b, bins=edges, density=True)
    return float(np.sum(np.abs(hist_a - hist_b)) / 2.0)


def auc_score(positive: list[float], negative: list[float]) -> float | None:
    if not positive or not negative:
        return None
    wins = 0.0
    total = 0
    for pos in positive:
        for neg in negative:
            if pos > neg:
                wins += 1.0
            elif pos == neg:
                wins += 0.5
            total += 1
    return wins / total if total else None


def relative_separation(positive: list[float], negative: list[float]) -> float | None:
    if not positive or not negative:
        return None
    pos = np.asarray(positive, dtype=float)
    neg = np.asarray(negative, dtype=float)
    pooled = math.sqrt((float(np.var(pos)) + float(np.var(neg))) / 2.0)
    diff = float(np.mean(pos) - np.mean(neg))
    if pooled < 1e-12:
        if abs(diff) < 1e-12:
            return 0.0
        return 999.0 if diff > 0 else -999.0
    return diff / pooled


def bootstrap_ci(
    positive: list[float],
    negative: list[float],
    metric,
    n_boot: int,
    seed: int,
) -> list[float | None]:
    if not positive or not negative or n_boot <= 0:
        return [None, None]
    rng = np.random.default_rng(seed)
    pos = np.asarray(positive, dtype=float)
    neg = np.asarray(negative, dtype=float)
    values = []
    for _ in range(n_boot):
        pos_s = rng.choice(pos, size=len(pos), replace=True).tolist()
        neg_s = rng.choice(neg, size=len(neg), replace=True).tolist()
        val = metric(pos_s, neg_s)
        if val is not None and np.isfinite(val):
            values.append(val)
    if not values:
        return [None, None]
    lo, hi = np.percentile(values, [2.5, 97.5])
    return [float(lo), float(hi)]


def classify_phase(auc: float | None, sep: float | None) -> str:
    if auc is None or sep is None:
        return "failed"
    if auc >= 0.90 and sep >= 1.0:
        return "recoverable"
    if auc >= 0.70 or sep >= 0.5:
        return "degraded"
    return "erased"


def pair_distances(fps, pair: tuple[str, str], seeds: list[int]):
    g1, g2 = pair
    between = []
    within = []

    for seed_a in seeds:
        for seed_b in seeds:
            ev_a = fps.get((g1, seed_a))
            ev_b = fps.get((g2, seed_b))
            if ev_a is not None and ev_b is not None:
                between.append(spectral_density_distance(ev_a, ev_b))

    for geom in pair:
        for i, seed_a in enumerate(seeds):
            for seed_b in seeds[i + 1 :]:
                ev_a = fps.get((geom, seed_a))
                ev_b = fps.get((geom, seed_b))
                if ev_a is not None and ev_b is not None:
                    within.append(spectral_density_distance(ev_a, ev_b))

    between = [x for x in between if np.isfinite(x)]
    within = [x for x in within if np.isfinite(x)]
    return between, within


def run(args):
    OUT.mkdir(exist_ok=True)
    seeds = DEFAULT_SEEDS[: args.seeds]
    k_values = args.k_values
    results = []

    print("=" * 72)
    print("PHASE 4B RECOVERABILITY BENCHMARK")
    print(f"W={W_VALUES}")
    print(f"N={N_CURVED}")
    print(f"seeds={len(seeds)} k={k_values} bootstrap={args.bootstrap}")
    print("=" * 72)

    for n in N_CURVED:
        print(f"\n[N={n}] Building base Laplacians")
        laps = build_laps(n)
        for w in W_VALUES:
            for k in k_values:
                print(f"  W={w:2d} k={k:2d}: spectra", end="", flush=True)
                fps = {}
                for geom in GEOMETRIES:
                    for seed in seeds:
                        lap = add_disorder(laps[geom], w, seed)
                        fps[(geom, seed)] = spectrum(lap, k)
                print(" done")

                for pair in PAIRS:
                    between, within = pair_distances(fps, pair, seeds)
                    auc = auc_score(between, within)
                    sep = relative_separation(between, within)
                    auc_ci = bootstrap_ci(
                        between,
                        within,
                        auc_score,
                        args.bootstrap,
                        seed=10_000 + int(w) + k,
                    )
                    sep_ci = bootstrap_ci(
                        between,
                        within,
                        relative_separation,
                        args.bootstrap,
                        seed=20_000 + int(w) + k,
                    )
                    phase = classify_phase(auc, sep)
                    result = {
                        "W": w,
                        "N": n,
                        "k": k,
                        "pair": f"{pair[0]}_vs_{pair[1]}",
                        "metric": "spectral_density_distance_auc_vs_same_geometry",
                        "auc": auc,
                        "auc_ci95": auc_ci,
                        "relative_separation": sep,
                        "relative_separation_ci95": sep_ci,
                        "mean_between": float(np.mean(between)) if between else None,
                        "mean_within": float(np.mean(within)) if within else None,
                        "n_between": len(between),
                        "n_within": len(within),
                        "phase": phase,
                        "evidence_status": "L3_EXPLORATORY" if len(seeds) < 10 else "L4_REPRODUCED_BENCHMARK",
                    }
                    results.append(result)
                    print(
                        f"    {result['pair']:18s} auc={auc:.3f} "
                        f"sep={sep:.2f} -> {phase}"
                    )

    by_cell = {(r["W"], r["N"], r["pair"], r["k"]): r for r in results}
    for result in results:
        if result["k"] != 30:
            continue
        base = by_cell.get((result["W"], result["N"], result["pair"], 15))
        if base and base["auc"] is not None and result["auc"] is not None:
            result["delta_auc_vs_k15"] = result["auc"] - base["auc"]
            result["delta_relative_separation_vs_k15"] = (
                result["relative_separation"] - base["relative_separation"]
            )

    out_path = OUT / args.output
    with open(out_path, "w", encoding="utf-8") as handle:
        json.dump(results, handle, indent=2)
    print(f"\nSaved: {out_path}")
    return results


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", type=int, default=10, help="Number of seeds to use.")
    parser.add_argument(
        "--k-values",
        type=int,
        nargs="+",
        default=DEFAULT_K_VALUES,
        help="Eigenmode counts to compare.",
    )
    parser.add_argument("--bootstrap", type=int, default=200, help="Bootstrap resamples.")
    parser.add_argument(
        "--output",
        default="phase4b_benchmark_results.json",
        help="Output JSON filename under experiments/20260629-phase4b.",
    )
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Fast smoke run: 3 seeds, k=15, 25 bootstrap samples.",
    )
    args = parser.parse_args()
    if args.quick:
        args.seeds = 3
        args.k_values = [15]
        args.bootstrap = 25
        args.output = "phase4b_benchmark_quick_results.json"
    if args.seeds < 2:
        raise SystemExit("--seeds must be >= 2")
    if args.seeds > len(DEFAULT_SEEDS):
        raise SystemExit(f"--seeds must be <= {len(DEFAULT_SEEDS)}")
    return args


if __name__ == "__main__":
    run(parse_args())
