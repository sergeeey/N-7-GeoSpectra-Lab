"""Gate 4C: projector (multiplet) IPR, pre-registered in reports/GATE4C_PROJECTOR_IPR_PREREG_v0.1.26.md.

Definitions (see the preregistration, sections 2-4):
- Multiplet = cluster of eigenvalues with gap <= 1e-8.
- Projector IPR of a multiplet g: sum_x rho_g(x)^2 / d_g, rho_g(x) = sum_{i in g} |v_i(x)|^2.
- Product operators (ring, wilson_ring): full multiplets are (k, g) with d_k + e_g = lambda,
  where k runs over the S^3 blocks (110 at j_max=3). Computed from one eigh(P) per seed.
- Controls (random Hermitian, broken Wilson): dense N x N eigh, same multiplet rule on the full spectrum.
- Selection: multiplets in ascending lambda, included whole while cumulative count <= n_low = floor(0.10 N).
- Naive (per-state) IPR is reported next to it for comparison only; it does not decide the verdict.

WHY one eigh(P): block k equals d_k * I + P, so eigenvectors are shared across all 110 blocks.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import eigh

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from cc_toy_lab.controls.negative_controls import build_broken_wilson_control
from cc_toy_lab.spectral.dirac_s3 import build_s3_dirac_operator
from cc_toy_lab.spectral.metrics import inverse_participation_ratio
from cc_toy_lab.spectral.s1_discretizations import build_s1_operator

TOL = 1e-8
J_MAX = 3
SIZES = [16, 32, 64, 128, 256]
CONTROL_SIZES = [16, 32, 64]
FAMILIES = ["ring", "wilson_ring"]
SEEDS = [7, 11, 23, 42, 101]
ALPHA = 0.0
W_LOCAL = 20.0
OUT = Path("results/gate4c_projector")
REF_THRESHOLD = 0.16


def groups_of(e: np.ndarray) -> list[list[int]]:
    groups, start = [], 0
    for i in range(1, len(e) + 1):
        if i == len(e) or e[i] - e[i - 1] > TOL:
            groups.append(list(range(start, i)))
            start = i
    return groups


def product_projector(e: np.ndarray, V: np.ndarray, dvals: np.ndarray) -> tuple[float, float, int]:
    """Projector IPR for the full S3 x S1 product operator from one eigh(P)."""
    n_blocks = len(dvals)
    N = n_blocks * len(e)
    n_low = max(1, int(0.10 * N))
    groups = groups_of(e)
    q2 = [float(np.sum(np.sum(np.abs(V[:, g]) ** 2, axis=1) ** 2)) for g in groups]
    gd = [len(g) for g in groups]
    ge = [float(e[g[0]]) for g in groups]
    entries = sorted(
        (float(dvals[k] + ge[gi]), gi) for k in range(n_blocks) for gi in range(len(groups))
    )
    clusters, cur = [], [entries[0]]
    for ent in entries[1:]:
        if ent[0] - cur[0][0] <= TOL:
            cur.append(ent)
        else:
            clusters.append(cur)
            cur = [ent]
    clusters.append(cur)
    count, num, den = 0, 0.0, 0.0
    for cl in clusters:
        dl = sum(gd[gi] for _, gi in cl)
        if count + dl > n_low:
            break
        count += dl
        num += sum(q2[gi] for _, gi in cl)
        den += dl
    return num / den, count / N, len(clusters)


def naive_product_ipr(e: np.ndarray, V: np.ndarray, dvals: np.ndarray) -> float:
    iprs = inverse_participation_ratio(V)
    all_e = (e[None, :] + dvals[:, None]).ravel()
    all_i = np.tile(iprs, len(dvals))
    N = all_e.size
    n_low = max(1, int(0.10 * N))
    return float(np.mean(all_i[np.argsort(all_e, kind="stable")[:n_low]]))


def dense_projector(op: np.ndarray) -> tuple[float, float]:
    """Projector IPR for a general dense Hermitian operator (controls)."""
    e, V = eigh(op)
    N = op.shape[0]
    n_low = max(1, int(0.10 * N))
    groups = groups_of(e)
    q2 = [float(np.sum(np.sum(np.abs(V[:, g]) ** 2, axis=1) ** 2)) for g in groups]
    gd = [len(g) for g in groups]
    count, num, den = 0, 0.0, 0.0
    for gi in range(len(groups)):
        if count + gd[gi] > n_low:
            break
        count += gd[gi]
        num += q2[gi]
        den += gd[gi]
    return num / den, count / N


def invariance_std(e: np.ndarray, V: np.ndarray, dvals: np.ndarray, draws: int = 10) -> float:
    rng = np.random.default_rng(1)
    vals = []
    for _ in range(draws):
        Vr = V.copy()
        for g in groups_of(e):
            if len(g) > 1:
                Z = rng.normal(size=(len(g), len(g))) + 1j * rng.normal(size=(len(g), len(g)))
                U, _ = np.linalg.qr(Z)
                Vr[:, g] = V[:, g] @ U
        vals.append(product_projector(e, Vr, dvals)[0])
    return float(np.std(vals))


def main() -> None:
    d, _ = build_s3_dirac_operator(j_max=J_MAX, radius=1.0)
    dvals = np.diag(d.real @ d.real).real
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for fam in FAMILIES:
        for s1 in SIZES:
            for W, seeds in [(0.0, [7]), (W_LOCAL, SEEDS)]:
                mode = "clean" if W == 0.0 else "geometric_weight"
                for seed in seeds:
                    P = np.asarray(
                        build_s1_operator(
                            size=s1,
                            alpha=ALPHA,
                            family=fam,
                            mode=mode,
                            disorder_strength=W,
                            seed=seed,
                            radius=1.0,
                        ),
                        dtype=complex,
                    )
                    e, V = eigh(P)
                    proj, frac, ncl = product_projector(e, V, dvals)
                    naive = naive_product_ipr(e, V, dvals)
                    std = invariance_std(e, V, dvals) if s1 <= 64 else None
                    rows.append(
                        {
                            "family": fam,
                            "s1": s1,
                            "W": W,
                            "seed": seed,
                            "ipr_proj": proj,
                            "ipr_naive": naive,
                            "selected_fraction": frac,
                            "clusters": ncl,
                            "invariance_std": std,
                        }
                    )
                    print(
                        f"{fam} s1={s1} W={W} seed={seed}: proj={proj:.6f} naive={naive:.6f} frac={frac:.4f}",
                        flush=True,
                    )

    # Consistency: full dense projector on the s1=16 product operator must equal the reduced formula.
    from cc_toy_lab.spectral.s3_s1_product_discretized import (
        build_s3_s1_product_operator,
    )

    consistency = {}
    for fam in FAMILIES:
        op, _, _ = build_s3_s1_product_operator(
            j_max=J_MAX,
            s1_size=16,
            alpha=ALPHA,
            mode="geometric_weight",
            disorder_strength=W_LOCAL,
            seed=7,
            radius=1.0,
            s1_family=fam,
        )
        dense_val, _ = dense_projector(op)
        reduced = next(
            r["ipr_proj"]
            for r in rows
            if r["family"] == fam and r["s1"] == 16 and r["W"] == W_LOCAL and r["seed"] == 7
        )
        consistency[fam] = {
            "dense": dense_val,
            "reduced": reduced,
            "diff": abs(dense_val - reduced),
        }
        print(f"consistency {fam} s1=16: dense={dense_val:.12f} reduced={reduced:.12f}", flush=True)

    controls = []
    for s1 in CONTROL_SIZES:
        N = 110 * s1  # 110 S3 blocks at j_max=3
        rng = np.random.default_rng(7)
        X = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
        rh = 0.5 * (X + X.conj().T)
        v_rh, f_rh = dense_projector(rh)
        controls.append(
            {"control": "random_hermitian", "s1": s1, "ipr_proj": v_rh, "selected_fraction": f_rh}
        )
        print(f"control random_hermitian s1={s1}: proj={v_rh:.6f}", flush=True)
        bw, _ = build_broken_wilson_control(
            j_max=J_MAX,
            s1_size=s1,
            alpha=ALPHA,
            disorder_strength=W_LOCAL,
            seed=7,
            radius=1.0,
            wilson_mode="scrambled",
        )
        v_bw, f_bw = dense_projector(np.asarray(bw, dtype=complex))
        controls.append(
            {
                "control": "broken_wilson_scrambled",
                "s1": s1,
                "ipr_proj": v_bw,
                "selected_fraction": f_bw,
            }
        )
        print(f"control broken_wilson s1={s1}: proj={v_bw:.6f}", flush=True)

    # Verdict, exactly as pre-registered.
    verdict = {}
    for fam in FAMILIES:
        fr = [r for r in rows if r["family"] == fam]

        # WHY: helpers take the family rows explicitly; closures over the loop variable `fr`
        # would silently bind to whichever family is current if called later.
        def mean_w20(family_rows: list[dict], s1: int, key: str) -> float:
            return float(
                np.mean([r[key] for r in family_rows if r["s1"] == s1 and r["W"] == W_LOCAL])
            )

        def ratio(family_rows: list[dict], s1: int, key: str) -> float:
            w20 = [r[key] for r in family_rows if r["s1"] == s1 and r["W"] == W_LOCAL]
            w0 = next(r[key] for r in family_rows if r["s1"] == s1 and r["W"] == 0.0)
            return float(np.mean(w20) / w0)

        out = {}
        for key in ["ipr_proj", "ipr_naive"]:
            p1 = mean_w20(fr, 256, key) >= 0.25
            xs = np.log(np.array([64, 128, 256], dtype=float))
            ys = np.log(np.array([mean_w20(fr, s, key) for s in [64, 128, 256]]))
            slope = float(np.polyfit(xs, ys, 1)[0])
            p2 = abs(slope) <= 0.10
            p3 = all(ratio(fr, s, key) >= 2.0 for s in [32, 64, 128, 256])
            # P4 reference is always the ring family (pre-registered), for both families.
            ring_rows = [
                r for r in rows if r["family"] == "ring" and r["s1"] == 64 and r["W"] == W_LOCAL
            ]
            ref = float(np.mean([r[key] for r in ring_rows]))
            ctrl = [c for c in controls if c["s1"] == 64]
            p4 = (
                all(c["ipr_proj"] < REF_THRESHOLD * ref for c in ctrl)
                if key == "ipr_proj"
                else None
            )
            out[key] = {
                "P1": bool(p1),
                "P1_value": mean_w20(fr, 256, key),
                "P2": bool(p2),
                "P2_slope": slope,
                "P3": bool(p3),
                "P3_ratios": {s: ratio(fr, s, key) for s in [32, 64, 128, 256]},
                "P4": None if p4 is None else bool(p4),
            }
        proj_pass = (
            all(out["ipr_proj"][k] for k in ["P1", "P2", "P3"])
            and out["ipr_proj"]["P4"] is not False
        )
        out["verdict_projector"] = "PASS" if proj_pass else "FAIL"
        naive_pass = all(out["ipr_naive"][k] for k in ["P1", "P2", "P3"])
        out["verdict_naive_for_sensitivity"] = "PASS" if naive_pass else "FAIL"
        out["definition_sensitive"] = (
            out["verdict_projector"] != out["verdict_naive_for_sensitivity"]
        )
        verdict[fam] = out
        print(
            f"{fam}: projector verdict={out['verdict_projector']} naive={out['verdict_naive_for_sensitivity']}",
            flush=True,
        )

    result = {
        "rows": rows,
        "controls": controls,
        "consistency": consistency,
        "verdict": verdict,
        "thresholds": {
            "P1": 0.25,
            "P2_abs_slope": 0.10,
            "P3_ratio": 2.0,
            "P4_fraction": REF_THRESHOLD,
        },
        "note_P4": "reference = mean over seeds of ring IPR_proj(W=20) at s1=64; controls use seed 7",
    }
    with open(OUT / "results.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False, default=float)
    print("written", OUT / "results.json", flush=True)


if __name__ == "__main__":
    main()
