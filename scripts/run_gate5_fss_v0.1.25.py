"""Gate 5 — Extended FSS (s1=256, 512) — v0.1.25

Pre-registration: reports/GATE5_FSS_PREREGISTRATION_v0.1.25.md
Families: ring, wilson_ring only (spectral_circle excluded)
Grid: 2 families × 2 W × 2 sizes × 1 j_max × 3 seeds = 24 cases
Runtime estimate: ~12 min on Hetzner CX52

Usage:
    python scripts/run_gate5_fss_v0.1.25.py --dry-run    # print plan
    python scripts/run_gate5_fss_v0.1.25.py --run        # execute
"""

from __future__ import annotations
import sys, time, json, argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
from scipy.linalg import eigh
from cc_toy_lab.spectral.s3_s1_product_discretized import build_s3_s1_product_operator
from cc_toy_lab.spectral.metrics import mean_adjacent_gap_ratio, inverse_participation_ratio

# ── Locked grid (pre-registered 2026-06-03, REVISED for true dimension) ───────
# Original s1=[256,512] was infeasible: true N=110×s1, so s1=512 → N=56320 → OOM.
# Corrected to feasible range. See DIMENSION_DISCREPANCY_AUDIT_v0.1.25.
# For s1≥256, use a sparse eigensolver (eigsh) — separate work item.
GRID = {
    "families":  ["ring", "wilson_ring"],
    "s1_sizes":  [160, 192],   # N = 17600, 21120 (dense eigh feasible on ≥32GB)
    "w_values":  [0, 20],
    "j_max":     3,
    "seeds":     [123, 456, 789],
    "alpha":     0.0,
    "radius":    1.0,
}

# Gate 4B s1=128 reference values (for decision rules)
GATE4B_REF = {
    "ring":        {"ipr_w20": 0.339, "contrast": 29.7},
    "wilson_ring": {"ipr_w20": 0.266, "contrast": 34.1},
}

SATURATION_TOL = 0.15   # ±15% of s1=128 IPR → SATURATION
REVERSAL_DROP  = 0.30   # >30% drop → REVERSAL

OUT = Path("reports/RUNS/gate5_fss_v0.1.25")


def generate_grid():
    cases = []
    for family in GRID["families"]:
        for s1 in GRID["s1_sizes"]:
            for w in GRID["w_values"]:
                for seed in GRID["seeds"]:
                    cases.append(dict(
                        family=family, s1_size=s1,
                        disorder_strength=w, seed=seed,
                        j_max=GRID["j_max"], alpha=GRID["alpha"],
                        radius=GRID["radius"],
                    ))
    return cases


def print_plan(cases):
    print("=" * 70)
    print("Gate 5 FSS — v0.1.25 — DRY RUN")
    print("=" * 70)
    print(f"Total cases: {len(cases)}")
    print(f"Families: {GRID['families']}")
    print(f"Sizes: {GRID['s1_sizes']} (N = {[110*s for s in GRID['s1_sizes']]} = 110×s1 for j_max=3)")
    print(f"W values: {GRID['w_values']}")
    print(f"Seeds: {GRID['seeds']}")
    print()
    print("Decision rules (pre-registered):")
    print(f"  SATURATION: IPR(W=20) within ±{SATURATION_TOL*100:.0f}% of s1=128 ref")
    print(f"  REVERSAL:   IPR(W=20) drops >{REVERSAL_DROP*100:.0f}% vs s1=128 ref")
    print()
    print("Gate 4B references:")
    for fam, ref in GATE4B_REF.items():
        print(f"  {fam}: IPR(W=20,s1=128) = {ref['ipr_w20']:.3f}, contrast = {ref['contrast']:.1f}x")
    print()
    print("Pre-registration: reports/GATE5_FSS_PREREGISTRATION_v0.1.25.md")
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
    verdicts = {}
    for family in GRID["families"]:
        ref = GATE4B_REF[family]["ipr_w20"]
        w20 = [r for r in results if r["family"] == family and r["disorder_strength"] == 20]
        for size in GRID["s1_sizes"]:
            cases = [r for r in w20 if r["s1_size"] == size]
            if not cases:
                continue
            ipr_mean = float(np.mean([r["true_ipr_mean"] for r in cases]))
            ratio = ipr_mean / ref
            if ratio < (1 - REVERSAL_DROP):
                verdict = "REVERSAL"
            elif abs(ratio - 1) <= SATURATION_TOL:
                verdict = "SATURATION"
            else:
                verdict = "CONTINUING"
            verdicts[f"{family}_s1_{size}"] = {
                "ipr_mean": ipr_mean, "ref": ref, "ratio": ratio, "verdict": verdict
            }
    return verdicts


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
        print(f"[{i:2d}/{len(cases)}] {case['family']:12s} s1={case['s1_size']:3d} "
              f"W={case['disorder_strength']:2d} seed={case['seed']} | "
              f"N={r['N']} IPR={r['true_ipr_mean']:.4f} t={dt:.0f}s ETA={eta/60:.1f}min")
        results.append(r)
        sys.stdout.flush()

    with open(OUT / "results.json", "w") as f:
        json.dump(results, f, indent=2)

    verdicts = apply_decision_rules(results)
    print("\n=== GATE 5 DECISION RULES ===")
    for key, v in verdicts.items():
        print(f"  {key}: IPR={v['ipr_mean']:.4f} ratio={v['ratio']:.2f}x [{v['verdict']}]")

    with open(OUT / "verdicts.json", "w") as f:
        json.dump(verdicts, f, indent=2)

    print(f"\nSaved: {OUT}/results.json + verdicts.json")


if __name__ == "__main__":
    main()
