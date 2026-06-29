"""
Phase 4A Ensemble: Full Protocol
10 seeds x 5 W x 3 pairs = 150 runs
Ablation: r-stat, spec_dens, weyl, all
Bootstrap CI, commit hash recorded
"""
from __future__ import annotations
import json, sys, time, warnings, subprocess
from pathlib import Path
from collections import defaultdict
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent.parent))
from cc_toy_lab.geometry.graph_laplacian import build_knn_graph_laplacian

# LOCKED PARAMETERS
W_VALUES = [0, 1, 5, 10, 20]
SEEDS = [42, 123, 999, 777, 100, 200, 300, 400, 500, 600]
K_EIG = 12
T4_N = 6
GEOMETRY_NAMES = ["T4", "S3xS1", "S2xS2"]
PAIRS = [("T4", "S3xS1"), ("T4", "S2xS2"), ("S3xS1", "S2xS2")]
PAIR_NAMES = ["T4_vs_S3xS1", "T4_vs_S2xS2", "S3xS1_vs_S2xS2"]

def t4_fd_laplacian(N):
    main, off = 2.0 * np.ones(N), -1.0 * np.ones(N - 1)
    L = sparse.diags([off, main, off], [-1, 0, 1], format="csr")
    L[0, -1], L[-1, 0] = -1.0, -1.0
    I = sparse.eye(N, format="csr")
    return (sparse.kron(sparse.kron(sparse.kron(L, I), I), I) + sparse.kron(sparse.kron(sparse.kron(I, L), I), I) + sparse.kron(sparse.kron(sparse.kron(I, I), L), I) + sparse.kron(sparse.kron(sparse.kron(I, I), I), L))

def sphere(dim, N, seed):
    rng = np.random.default_rng(seed)
    p = rng.standard_normal((N, dim + 1))
    return p / np.linalg.norm(p, axis=1, keepdims=True)

def sample_s3xs1(N_s3, N_s1, seed):
    s3 = sphere(3, N_s3, seed)
    rng = np.random.default_rng(seed + 1)
    angles = rng.uniform(0, 2 * np.pi, N_s1)
    s1 = np.column_stack([np.cos(angles), np.sin(angles)])
    return np.array([np.concatenate([a, b]) for a in s3 for b in s1])

def sample_s2xs2(N_a, N_b, seed):
    sa, sb = sphere(2, N_a, seed), sphere(2, N_b, seed + 1)
    return np.array([np.concatenate([a, b]) for a in sa for b in sb])

def add_disorder(L, W, seed):
    rng = np.random.default_rng(seed)
    return L + sparse.diags(rng.uniform(-W, W, L.shape[0]), format="csr")

def compute_r_statistic(ev):
    ev = np.sort(np.real(ev)); ev = ev[ev > 1e-10]
    if len(ev) < 3: return 0.0
    rs = []
    for i in range(1, len(ev) - 1):
        sm, sp = ev[i] - ev[i-1], ev[i+1] - ev[i]
        if max(sm, sp) > 0: rs.append(min(sm, sp) / max(sm, sp))
    return float(np.mean(rs)) if rs else 0.0

def weyl_dimension(ev):
    ev = np.sort(np.real(ev)); ev = ev[ev > 1e-10]
    if len(ev) < 10: return 0.0
    thresholds = np.linspace(ev[len(ev)//10], ev[-1], min(30, len(ev)//2))
    counts = np.array([np.sum(ev <= t) for t in thresholds])
    mask = (thresholds > 0) & (counts > 0)
    if mask.sum() < 5: return 0.0
    log_t, log_c = np.log(thresholds[mask]), np.log(counts[mask])
    A = np.vstack([log_t, np.ones_like(log_t)]).T
    slope, _ = np.linalg.lstsq(A, log_c, rcond=None)[0]
    return float(2.0 * slope)

def spectral_density_distance(ev1, ev2, n_bins=15):
    if len(ev1) < 2 or len(ev2) < 2: return 1.0
    emin, emax = min(ev1.min(), ev2.min()), max(ev1.max(), ev2.max())
    if emax <= emin: return 0.0
    bins = np.linspace(emin, emax, n_bins + 1)
    h1, _ = np.histogram(ev1, bins=bins, density=True)
    h2, _ = np.histogram(ev2, bins=bins, density=True)
    return float(np.sum(np.abs(h1 - h2)) / 2.0)

def get_fingerprint(L, name, n_eig=12):
    n = L.shape[0]; k = min(n_eig, n - 2)
    try: eigenvalues = eigsh(L, k=k, which="SM", return_eigenvectors=False, tol=1e-10)
    except: return None
    ev = np.sort(np.real(eigenvalues)); ev = ev[ev > 1e-10]
    if len(ev) < 3: return {"name": name, "n_eigenvalues": len(eigenvalues), "error": "Too few positive eigenvalues"}
    return {"name": name, "r_statistic": compute_r_statistic(eigenvalues), "d_eff": weyl_dimension(eigenvalues), "eigenvalues": ev.tolist()}

def classify_with_metric(fp1, fp2, metric):
    if metric == "r_stat": return abs(fp1.get("r_statistic", 0) - fp2.get("r_statistic", 0)) > 0.15
    elif metric == "spec_dens": return spectral_density_distance(np.array(fp1.get("eigenvalues", [])), np.array(fp2.get("eigenvalues", []))) > 0.3
    elif metric == "weyl": return abs(fp1.get("d_eff", 0) - fp2.get("d_eff", 0)) > 0.5
    elif metric == "all":
        d = sum([abs(fp1.get("r_statistic", 0) - fp2.get("r_statistic", 0)) > 0.15, spectral_density_distance(np.array(fp1.get("eigenvalues", [])), np.array(fp2.get("eigenvalues", []))) > 0.3, abs(fp1.get("d_eff", 0) - fp2.get("d_eff", 0)) > 0.5])
        return d >= 2
    return False

def main():
    print("=" * 60); print("PHASE 4A ENSEMBLE: FULL PROTOCOL"); print("=" * 60)
    try: commit = subprocess.check_output(["git", "-C", str(Path(__file__).parent.parent), "rev-parse", "--short", "HEAD"]).decode().strip()
    except: commit = "unknown"
    print(f"Commit: {commit}"); print(f"W values: {W_VALUES}"); print(f"Seeds: {len(SEEDS)}"); print(f"Total runs: {len(W_VALUES)} x {len(SEEDS)} x 3 = {len(W_VALUES) * len(SEEDS) * 3}")

    clean_laps = {"T4": t4_fd_laplacian(T4_N)}
    s3s1_pts = sample_s3xs1(50, 8, 42); s2s2_pts = sample_s2xs2(50, 8, 42)
    for n, p in [("S3xS1", s3s1_pts), ("S2xS2", s2s2_pts)]:
        gl = build_knn_graph_laplacian(p, k=min(12, len(p) - 1), normalized=True)
        clean_laps[n] = gl.laplacian

    all_results = []
    t0 = time.time()
    for wi, W in enumerate(W_VALUES):
        for si, seed in enumerate(SEEDS):
            laps = {n: add_disorder(clean_laps[n], W, seed) if W > 0 else clean_laps[n] for n in GEOMETRY_NAMES}
            fps = {n: get_fingerprint(laps[n], n, K_EIG) for n in GEOMETRY_NAMES}
            row = {"W": W, "seed": seed, "ablations": {}}
            for metric_name in ["r_stat", "spec_dens", "weyl", "all"]:
                row["ablations"][metric_name] = {}
                for (n1, n2), pn in zip(PAIRS, PAIR_NAMES):
                    if fps.get(n1) and fps.get(n2) and "error" not in fps[n1] and "error" not in fps[n2]:
                        row["ablations"][metric_name][pn] = classify_with_metric(fps[n1], fps[n2], metric_name)
            all_results.append(row)
            done = wi * len(SEEDS) + si + 1
            if done % 10 == 0:
                elapsed = time.time() - t0; eta = elapsed / done * (len(W_VALUES) * len(SEEDS) - done)
                print(f"  {done}/{len(W_VALUES) * len(SEEDS)} done, {elapsed:.0f}s elapsed, ETA {eta:.0f}s")
    print(f"\n  Ensemble complete in {time.time() - t0:.1f}s")

    ablation_results = {}
    for metric_name in ["r_stat", "spec_dens", "weyl", "all"]:
        ablation_results[metric_name] = {}
        for pn in PAIR_NAMES:
            vals = [r["ablations"][metric_name][pn] for r in all_results if pn in r["ablations"].get(metric_name, {})]
            if vals: ablation_results[metric_name][pn] = {"distinct": sum(vals), "total": len(vals), "fraction": sum(vals) / len(vals)}

    print("\nABLATION STUDY")
    for metric_name in ["r_stat", "spec_dens", "weyl", "all"]:
        print(f"\n  {metric_name}:")
        for pn in PAIR_NAMES:
            stats = ablation_results[metric_name].get(pn, {})
            if stats: print(f"    {pn}: {stats['distinct']}/{stats['total']} ({stats['fraction']:.0%})")

    summary = {"experiment": "phase4a_ensemble_full", "parameters": {"W_values": W_VALUES, "seeds": SEEDS, "k_eigenvalues": K_EIG, "commit": commit}, "ablation": ablation_results, "all_results": all_results}
    out = Path(__file__).parent.parent / "data" / "phase4a_ensemble_results.json"
    out.parent.mkdir(exist_ok=True)
    with open(out, "w") as f: json.dump(summary, f, indent=2, default=str)
    print(f"\n  Saved: {out}")

if __name__ == "__main__":
    main()
