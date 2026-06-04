"""Cross-Geometry S²×S¹ Pilot — v0.1.25

Pre-registration: reports/CROSS_GEOMETRY_S2S1_PREREGISTRATION_v0.1.25.md
Families: ring on S²×S¹
Grid: 1 family × 2 W × 3 sizes × 1 j_max × 3 seeds = 18 cases

METHODOLOGY FIX (2026-06-04):
The first version used a HAND-ROLLED S²×S¹ operator (crude Laplacian⊗ring with
disorder on the full diagonal) → gave IPR(W=20)≈0.83, a construction ARTIFACT
not comparable to S³×S¹. Replaced with the ESTABLISHED, methodology-matched
builder `build_product_discretized_operator` (q=0, cutoff=j_max), which is
byte-identical in structure to build_s3_s1_product_operator:
    H = kron(D_S2², I_S1) + kron(I_S2, P_S1)
with the SAME build_s1_operator for the S¹ part (identical disorder machinery).
This makes the S²×S¹ vs S³×S¹ comparison fair (only the sphere factor differs).
Verified: IPR(W=20)≈0.30-0.35, same regime as S³×S¹ ring (~0.32).

Usage:
    python scripts/run_cross_geometry_s2s1_v0.1.25.py --dry-run
    python scripts/run_cross_geometry_s2s1_v0.1.25.py --run
"""

from __future__ import annotations
import sys, time, json, argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
from scipy.linalg import eigh
from cc_toy_lab.spectral.metrics import mean_adjacent_gap_ratio, inverse_participation_ratio
from cc_toy_lab.spectral.s2_s1_product_discretized import build_product_discretized_operator

# ── Locked grid (pre-registered 2026-06-03) ──────────────────────────────────
GRID = {
    "geometry": "S2xS1",
    "s1_family": "ring",
    "s1_sizes": [16, 32, 64],
    "w_values": [0, 20],
    "j_max": 3,
    "seeds": [123, 456, 789],
    "alpha": 0.0,
    "radius": 1.0,
}

# Gate 4B S³×S¹ ring references
GATE4B_S3S1_REF = {
    16: {"ipr_w20": 0.326, "ipr_w0": 0.0797, "contrast": 4.1},
    32: {"ipr_w20": 0.322, "ipr_w0": 0.0434, "contrast": 7.4},
    64: {"ipr_w20": 0.320, "ipr_w0": 0.0226, "contrast": 14.2},
}

TRANSFER_THRESH  = 0.50   # ≥50% of S³×S¹ contrast → TRANSFER
PARTIAL_THRESH   = 0.20   # 20-50% → PARTIAL

OUT = Path("reports/RUNS/cross_geometry_s2s1_v0.1.25")


def build_s2s1_operator(*, j_max, s1_size, alpha, disorder_strength, seed, radius):
    """Build methodology-matched S²×S¹ operator (established builder).

    Uses build_product_discretized_operator (q=0, cutoff=j_max):
        H = kron(D_S2², I_S1) + kron(I_S2, P_S1)
    with the SAME build_s1_operator (ring, geometric_weight disorder) as
    build_s3_s1_product_operator. q=0 = plain S² Dirac (no monopole charge);
    cutoff=j_max mirrors the S³ truncation. This makes S²×S¹ vs S³×S¹
    comparable: only the sphere factor (D_S2² vs D_S3²) differs.
    """
    op, _lifted, meta = build_product_discretized_operator(
        q=0,
        cutoff=int(j_max),
        s1_size=int(s1_size),
        alpha=float(alpha),
        mode="clean" if disorder_strength == 0 else "geometric_weight",
        disorder_strength=float(disorder_strength),
        seed=seed,
        radius=float(radius),
        s1_family="ring",
    )
    return op, {"geometry": "S2xS1", "s2_dim": meta["s2_dimension"],
                "s1_size": int(s1_size), "total_dim": meta["total_dimension"],
                "j_max": int(j_max)}


def generate_grid():
    cases = []
    for s1 in GRID["s1_sizes"]:
        for w in GRID["w_values"]:
            for seed in GRID["seeds"]:
                cases.append(dict(
                    s1_size=s1, disorder_strength=w, seed=seed,
                    j_max=GRID["j_max"], alpha=GRID["alpha"], radius=GRID["radius"],
                ))
    return cases


def print_plan(cases):
    print("=" * 70)
    print("Cross-Geometry S²×S¹ Pilot — v0.1.25 — DRY RUN")
    print("=" * 70)
    print(f"Total cases: {len(cases)}")
    print(f"Geometry: S²×S¹ (j_max={GRID['j_max']}, S² dim = {(GRID['j_max']+1)**2})")
    print(f"S¹: ring, sizes {GRID['s1_sizes']}")
    print(f"W values: {GRID['w_values']}, seeds: {GRID['seeds']}")
    print()
    print("Decision rules:")
    print(f"  TRANSFER:    contrast ≥ {TRANSFER_THRESH*100:.0f}% of S³×S¹ ref")
    print(f"  PARTIAL:     {PARTIAL_THRESH*100:.0f}–{TRANSFER_THRESH*100:.0f}% of S³×S¹ ref")
    print(f"  NO_TRANSFER: < {PARTIAL_THRESH*100:.0f}% of S³×S¹ ref")
    print()
    print("S³×S¹ ring references:")
    for s, ref in GATE4B_S3S1_REF.items():
        print(f"  s1={s}: contrast {ref['contrast']:.1f}x, IPR(W=20)={ref['ipr_w20']:.3f}")
    print("=" * 70)


def run_case(case: dict) -> dict:
    op, meta = build_s2s1_operator(**case)
    N = op.shape[0]
    eigvals, eigvecs = eigh(op)
    n_low = max(1, int(0.1 * N))
    ipr = float(np.mean(inverse_participation_ratio(eigvecs[:, :n_low])))
    r_stat = float(mean_adjacent_gap_ratio(eigvals))
    return {**case, "geometry": "S2xS1", "N": N,
            "s2_dim": meta["s2_dim"], "true_ipr_mean": ipr, "r_stat": r_stat}


def apply_decision_rules(results: list[dict]) -> dict:
    verdicts = {}
    for s1 in GRID["s1_sizes"]:
        ref = GATE4B_S3S1_REF.get(s1)
        if not ref:
            continue
        w0_cases  = [r for r in results if r["s1_size"] == s1 and r["disorder_strength"] == 0]
        w20_cases = [r for r in results if r["s1_size"] == s1 and r["disorder_strength"] == 20]
        if not (w0_cases and w20_cases):
            continue
        ipr_w0  = float(np.mean([r["true_ipr_mean"] for r in w0_cases]))
        ipr_w20 = float(np.mean([r["true_ipr_mean"] for r in w20_cases]))
        contrast = ipr_w20 / ipr_w0 if ipr_w0 > 0 else 0
        transfer_ratio = contrast / ref["contrast"]

        if transfer_ratio >= TRANSFER_THRESH:
            verdict = "TRANSFER"
        elif transfer_ratio >= PARTIAL_THRESH:
            verdict = "PARTIAL"
        else:
            verdict = "NO_TRANSFER"

        verdicts[f"s1_{s1}"] = {
            "ipr_w0": round(ipr_w0, 5),
            "ipr_w20": round(ipr_w20, 5),
            "contrast_s2s1": round(contrast, 2),
            "contrast_s3s1_ref": ref["contrast"],
            "transfer_ratio": round(transfer_ratio, 3),
            "verdict": verdict,
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
        ref_w20 = GATE4B_S3S1_REF.get(case["s1_size"], {}).get("ipr_w20", 0)
        ratio = f"{r['true_ipr_mean']/ref_w20:.2f}x" if ref_w20 and case["disorder_strength"]==20 else "W=0"
        print(f"[{i:2d}/{len(cases)}] S²×S¹ s1={case['s1_size']:3d} W={case['disorder_strength']:2d} "
              f"seed={case['seed']} | N={r['N']} IPR={r['true_ipr_mean']:.4f} ({ratio}) "
              f"t={dt:.1f}s ETA={eta/60:.1f}min")
        results.append(r)
        sys.stdout.flush()

    with open(OUT / "results.json", "w") as f:
        json.dump(results, f, indent=2)

    verdicts = apply_decision_rules(results)
    print("\n=== S²×S¹ CROSS-GEOMETRY VERDICT ===")
    for key, v in verdicts.items():
        print(f"  {key}: contrast={v['contrast_s2s1']:.1f}x "
              f"(S³×S¹ ref={v['contrast_s3s1_ref']:.1f}x, ratio={v['transfer_ratio']:.2f}) "
              f"[{v['verdict']}]")

    with open(OUT / "verdicts.json", "w") as f:
        json.dump(verdicts, f, indent=2)

    print(f"\nSaved: {OUT}/results.json + verdicts.json")


if __name__ == "__main__":
    main()
