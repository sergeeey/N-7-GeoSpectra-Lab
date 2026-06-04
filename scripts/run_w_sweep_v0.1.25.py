"""W-Sweep — Systematic disorder strength scan — v0.1.25

Pre-registration: reports/W_SWEEP_PREREGISTRATION_v0.1.25.md
Families: ring (primary), wilson_ring (secondary)
Grid: 2 families × 7 W × 1 size × 1 j_max × 3 seeds = 42 cases
Runtime estimate: ~7 min on Hetzner CX52

Usage:
    python scripts/run_w_sweep_v0.1.25.py --dry-run
    python scripts/run_w_sweep_v0.1.25.py --run
"""

from __future__ import annotations
import sys, time, json, argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
from scipy.linalg import eigh
from cc_toy_lab.spectral.s3_s1_product_discretized import build_s3_s1_product_operator
from cc_toy_lab.spectral.metrics import mean_adjacent_gap_ratio, inverse_participation_ratio

# ── Locked grid (pre-registered 2026-06-03) ──────────────────────────────────
GRID = {
    "families": ["ring", "wilson_ring"],
    "w_values": [0, 5, 10, 15, 20, 25, 30],
    "s1_size":  64,    # fixed for efficiency
    "j_max":    3,
    "seeds":    [123, 456, 789],
    "alpha":    0.0,
    "radius":   1.0,
}

# Gate 4B reference at s1=64
GATE4B_W20_REF = {"ring": 0.320, "wilson_ring": 0.235}
ONSET_FACTOR = 1.5   # IPR(W) > 1.5 × IPR(W=0) → onset

OUT = Path("reports/RUNS/w_sweep_v0.1.25")


def generate_grid():
    cases = []
    for family in GRID["families"]:
        for w in GRID["w_values"]:
            for seed in GRID["seeds"]:
                cases.append(dict(
                    family=family, disorder_strength=w,
                    s1_size=GRID["s1_size"], j_max=GRID["j_max"],
                    seed=seed, alpha=GRID["alpha"], radius=GRID["radius"],
                ))
    return cases


def print_plan(cases):
    print("=" * 70)
    print("W-Sweep — v0.1.25 — DRY RUN")
    print("=" * 70)
    print(f"Total cases: {len(cases)}")
    print(f"W values: {GRID['w_values']}")
    print(f"Fixed s1_size: {GRID['s1_size']} (N = {7*64} for j_max=3)")
    print(f"Families: {GRID['families']}")
    print(f"Seeds: {GRID['seeds']}")
    print()
    print("Decision rules:")
    print(f"  ONSET: first W where IPR > {ONSET_FACTOR}× IPR(W=0)")
    print(f"  PEAK: W where IPR is maximum")
    print(f"  MONOTONE: IPR strictly increasing through W=30")
    print()
    print("Gate 4B refs (s1=64, W=20):")
    for fam, ref in GATE4B_W20_REF.items():
        print(f"  {fam}: {ref:.3f}")
    print("=" * 70)


def run_case(case: dict) -> dict:
    op, _, _ = build_s3_s1_product_operator(
        j_max=case["j_max"],
        s1_size=case["s1_size"],
        alpha=case["alpha"],
        mode="clean" if case["disorder_strength"] == 0 else "geometric_weight",
        disorder_strength=case["disorder_strength"],
        seed=case["seed"],
        radius=case["radius"],
        s1_family=case["family"],
    )
    N = op.shape[0]
    eigvals, eigvecs = eigh(op)
    n_low = max(1, int(0.1 * N))
    ipr = float(np.mean(inverse_participation_ratio(eigvecs[:, :n_low])))
    r_stat = float(mean_adjacent_gap_ratio(eigvals))
    return {**case, "N": N, "true_ipr_mean": ipr, "r_stat": r_stat}


def apply_decision_rules(results: list[dict]) -> dict:
    summary = {}
    for family in GRID["families"]:
        fam_results = [r for r in results if r["family"] == family]
        by_w = {}
        for r in fam_results:
            w = r["disorder_strength"]
            by_w.setdefault(w, []).append(r["true_ipr_mean"])
        ipr_by_w = {w: float(np.mean(v)) for w, v in by_w.items()}

        ipr_w0 = ipr_by_w.get(0, None)
        if ipr_w0 is None:
            continue

        onset_w = next((w for w in sorted(ipr_by_w) if w > 0 and ipr_by_w[w] > ONSET_FACTOR * ipr_w0), None)
        peak_w = max(ipr_by_w, key=ipr_by_w.get)
        monotone = all(ipr_by_w[w1] <= ipr_by_w[w2]
                       for w1, w2 in zip(sorted(ipr_by_w)[:-1], sorted(ipr_by_w)[1:]))

        summary[family] = {
            "ipr_by_w": {str(w): round(v, 5) for w, v in ipr_by_w.items()},
            "onset_w": onset_w,
            "peak_w": int(peak_w),
            "peak_ipr": round(ipr_by_w[peak_w], 5),
            "monotone": monotone,
            "gate4b_w20_ref": GATE4B_W20_REF.get(family),
            "verdict": "MONOTONE" if monotone else (
                f"PEAK_AT_{peak_w}" if abs(peak_w - 20) <= 5 else
                f"PEAK_AT_{peak_w}_DEVIATES"
            ),
        }
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--run", action="store_true")
    args = parser.parse_args()

    cases = generate_grid()

    if args.dry_run or not args.run:
        print_plan(cases)
        return

    OUT.mkdir(parents=True, exist_ok=True)
    results = []
    t0 = time.perf_counter()

    for i, case in enumerate(cases, 1):
        ct = time.perf_counter()
        r = run_case(case)
        dt = time.perf_counter() - ct
        elapsed = time.perf_counter() - t0
        eta = elapsed / i * (len(cases) - i)
        print(f"[{i:2d}/{len(cases)}] {case['family']:12s} W={case['disorder_strength']:2d} "
              f"seed={case['seed']} | IPR={r['true_ipr_mean']:.4f} t={dt:.1f}s ETA={eta/60:.1f}min")
        results.append(r)
        sys.stdout.flush()

    with open(OUT / "results.json", "w") as f:
        json.dump(results, f, indent=2)

    summary = apply_decision_rules(results)
    print("\n=== W-SWEEP SUMMARY ===")
    for fam, s in summary.items():
        print(f"\n{fam}:")
        print(f"  IPR by W: {s['ipr_by_w']}")
        print(f"  Onset W:  {s['onset_w']}")
        print(f"  Peak W:   {s['peak_w']} (IPR={s['peak_ipr']:.4f})")
        print(f"  Monotone: {s['monotone']}")
        print(f"  Verdict:  {s['verdict']}")

    with open(OUT / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\nSaved: {OUT}/results.json + summary.json")


if __name__ == "__main__":
    main()
