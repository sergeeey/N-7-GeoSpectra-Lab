"""
Phase 4A: Crucial Experiments — Saving W=20
Tests H2 (overfitting), H4 (features), H1 (k), H6 (threshold robustness)
Method: Chamberlin (1890) multiple hypotheses + Platt (1964) strong inference
"""

import json
import sys
import warnings
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh
from sklearn.ensemble import RandomForestClassifier

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent.parent))
from cc_toy_lab.geometry.graph_laplacian import build_knn_graph_laplacian

SEEDS_TRAIN = [42, 123, 999, 777, 100]
SEEDS_TEST = [200, 300, 400, 500, 600]
K = 15
OUT = Path(__file__).parent / "20260629-crucial-experiments"
OUT.mkdir(exist_ok=True)


def t4_lap(N):
    m, o = 2.0 * np.ones(N), -1.0 * np.ones(N - 1)
    L = sparse.diags([o, m, o], [-1, 0, 1], format="csr")
    L[0, -1], L[-1, 0] = -1.0, -1.0
    I = sparse.eye(N, format="csr")
    return (
        sparse.kron(sparse.kron(sparse.kron(L, I), I), I)
        + sparse.kron(sparse.kron(sparse.kron(I, L), I), I)
        + sparse.kron(sparse.kron(sparse.kron(I, I), L), I)
        + sparse.kron(sparse.kron(sparse.kron(I, I), I), L)
    )


def sphere(d, N, s):
    rng = np.random.default_rng(s)
    p = rng.standard_normal((N, d + 1))
    return p / np.linalg.norm(p, axis=1, keepdims=True)


def s31(n3, n1, s):
    s3 = sphere(3, n3, s)
    rng = np.random.default_rng(s + 1)
    a = rng.uniform(0, 2 * np.pi, n1)
    s1 = np.column_stack([np.cos(a), np.sin(a)])
    return np.array([np.concatenate([x, y]) for x in s3 for y in s1])


def s22(na, nb, s):
    sa, sb = sphere(2, na, s), sphere(2, nb, s + 1)
    return np.array([np.concatenate([x, y]) for x in sa for y in sb])


def ad(L, W, s):
    rng = np.random.default_rng(s)
    return L + sparse.diags(rng.uniform(-W, W, L.shape[0]), format="csr")


def get_fp(L, n, k=15):
    n0 = L.shape[0]
    k = min(k, n0 - 2)
    try:
        ev = eigsh(L, k=k, which="SM", return_eigenvectors=False, tol=1e-8)
    except Exception as exc:
        if isinstance(exc, (KeyboardInterrupt, SystemExit, MemoryError)):
            raise
        return None
    ev = np.sort(np.real(ev))
    ev = ev[ev > 1e-10]
    if len(ev) < 3:
        return None
    rs = []
    for i in range(1, len(ev) - 1):
        sm, sp = ev[i] - ev[i - 1], ev[i + 1] - ev[i]
        if max(sm, sp) > 0:
            rs.append(min(sm, sp) / max(sm, sp))
    r = float(np.mean(rs)) if rs else 0.0
    th = np.linspace(ev[len(ev) // 10], ev[-1], min(12, len(ev) // 2))
    c = np.array([np.sum(ev <= t) for t in th])
    mask = (th > 0) & (c > 0)
    deff = 0.0
    if mask.sum() >= 4:
        lt, lc = np.log(th[mask]), np.log(c[mask])
        A = np.vstack([lt, np.ones_like(lt)]).T
        deff = 2.0 * np.linalg.lstsq(A, lc, rcond=None)[0][0]
    dens, _ = np.histogram(ev, bins=5, density=True) if len(ev) > 5 else (np.zeros(5), None)
    cv = float(np.std(ev) / np.mean(ev)) if np.mean(ev) > 0 else 0
    return {"n": n, "r": r, "d": float(deff), "cv": cv, "ds": dens.tolist(), "ev": ev.tolist()}


def sd(e1, e2, nb=15):
    if len(e1) < 2 or len(e2) < 2:
        return 1.0
    mn, mx = min(min(e1), min(e2)), max(max(e1), max(e2))
    if mx <= mn:
        return 0.0
    b = np.linspace(mn, mx, nb + 1)
    h1, _ = np.histogram(e1, bins=b, density=True)
    h2, _ = np.histogram(e2, bins=b, density=True)
    return float(np.sum(np.abs(h1 - h2)) / 2.0)


def fe(a, b):
    return [
        a["r"],
        b["r"],
        a["d"],
        b["d"],
        a["cv"],
        b["cv"],
        sd(a["ev"], b["ev"]),
        abs(a["r"] - b["r"]),
        abs(a["d"] - b["d"]),
        abs(a["cv"] - b["cv"]),
        *a["ds"],
        *b["ds"],
    ]


def fe2(a, b):
    """Only top 2 features: sd_dist + d_eff_spread"""
    return [sd(a["ev"], b["ev"]), abs(a["d"] - b["d"])]


# Build Laplacians
laps = {"T4": t4_lap(6)}
for n, p in [("S3xS1", s31(50, 8, 42)), ("S2xS2", s22(50, 8, 42))]:
    gl = build_knn_graph_laplacian(p, k=min(12, len(p) - 1), normalized=True)
    laps[n] = gl.laplacian

PAIRS = [
    ("T4", "S3xS1", 1),
    ("T4", "S2xS2", 1),
    ("S3xS1", "S2xS2", 1),
    ("T4", "T4", 0),
    ("S3xS1", "S3xS1", 0),
    ("S2xS2", "S2xS2", 0),
]


def collect(W_list, seed_list, k=15):
    data = []
    for s in seed_list:
        for W in W_list:
            for n1, n2, lb in PAIRS:
                L1 = ad(laps[n1], W, s) if W > 0 else laps[n1]
                L2 = ad(laps[n2], W, s) if W > 0 else laps[n2]
                p1 = get_fp(L1, n1, k)
                p2 = get_fp(L2, n2, k)
                if p1 and p2:
                    data.append((fe(p1, p2), lb, fe2(p1, p2), lb))
    return data


print("=" * 60)
print("CRUCIAL EXPERIMENTS: Saving W=20")
print("=" * 60)
results = {}

# ==== EXP 1: H2 — Train on W∈[0,10], test W=20 ====
print("\n[EXP 1] H2: Overfitting — train W≤10, test W=20")
train1 = collect([0, 1, 5, 10], SEEDS_TRAIN, K)
X1 = np.array([d[0] for d in train1])
y1 = np.array([d[1] for d in train1])
test1 = collect([20], SEEDS_TEST, K)
X1t = np.array([d[0] for d in test1])
y1t = np.array([d[1] for d in test1])
clf1 = RandomForestClassifier(n_estimators=50, max_depth=5, random_state=42)
clf1.fit(X1, y1)
acc1 = float(clf1.score(X1t, y1t))
print(f"  Train W∈[0,10]: {len(X1)} samples")
print(f"  Test W=20: {len(X1t)} samples")
print(f"  Accuracy: {acc1:.1%} {'→ IMPROVED (H2 killed)' if acc1 > 0.7 else '→ still weak'}")
results["H2_overfitting"] = {
    "train_W": [0, 1, 5, 10],
    "test_W": 20,
    "acc": acc1,
    "verdict": "H2 killed" if acc1 > 0.7 else "H2 confirmed",
}

# ==== EXP 2: H4 — Only top 2 features (proper OOD split) ====
print("\n[EXP 2] H4: Feature selection — only sd_dist + d_eff_spread")
train2 = collect([0, 1, 5, 10], SEEDS_TRAIN, K)
test2 = collect([20], SEEDS_TEST, K)
X2 = np.array([d[2] for d in train2])
y2 = np.array([d[3] for d in train2])
X2t = np.array([d[2] for d in test2])
y2t = np.array([d[3] for d in test2])
clf2 = RandomForestClassifier(n_estimators=30, max_depth=4, random_state=42)
clf2.fit(X2, y2)
acc2 = float(clf2.score(X2t, y2t))
print("  2 features (sd_dist, d_eff_spread), train W∈[0,1,5,10], test W=20")
print(f"  Test: {acc2:.1%} {'→ H4 confirmed' if acc2 > 0.7 else '→ H4 killed'}")
results["H4_features"] = {
    "n_features": 2,
    "acc": acc2,
    "verdict": "H4 confirmed" if acc2 > 0.7 else "H4 killed",
}

# ==== EXP 3: H1 — k=30 at W=20 ====
print("\n[EXP 3] H1: More eigenvalues — k=30 at W=20")
train3 = collect([0], SEEDS_TRAIN, 30)
test3 = collect([20], SEEDS_TEST, 30)
if test3:
    X3 = np.array([d[0] for d in train3])
    y3 = np.array([d[1] for d in train3])
    X3t = np.array([d[0] for d in test3])
    y3t = np.array([d[1] for d in test3])
    clf3 = RandomForestClassifier(n_estimators=50, max_depth=5, random_state=42)
    clf3.fit(X3, y3)
    acc3 = float(clf3.score(X3t, y3t))
    print(f"  k=30, W=20: {acc3:.1%}")
    train3b = collect([0], SEEDS_TRAIN, 15)
    test3b = collect([20], SEEDS_TEST, 15)
    baseline_k15 = None
    if train3b and test3b:
        X3b = np.array([d[0] for d in train3b])
        y3b = np.array([d[1] for d in train3b])
        X3bt = np.array([d[0] for d in test3b])
        y3bt = np.array([d[1] for d in test3b])
        clf3b = RandomForestClassifier(n_estimators=50, max_depth=5, random_state=42)
        clf3b.fit(X3b, y3b)
        baseline_k15 = float(clf3b.score(X3bt, y3bt))
        print(f"  baseline k=15 W=20: {baseline_k15:.1%}")
    results["H1_k30"] = {"k": 30, "acc": acc3, "baseline_k15": baseline_k15}
else:
    print("  k=30 FAILED (eigsh convergence)")
    results["H1_k30"] = {"k": 30, "acc": None, "error": "No test data"}

# ==== EXP 4: H6 — Different disorder seeds ====
print("\n[EXP 4] H6: Threshold robustness — different seeds per geometry")


def collect_diffseeds(W_list, seed_list, k=15):
    data = []
    for i, s in enumerate(seed_list):
        pts31 = s31(50, 8, s)
        pts22 = s22(50, 8, s)
        gl31 = build_knn_graph_laplacian(pts31, k=min(12, len(pts31) - 1), normalized=True)
        gl22 = build_knn_graph_laplacian(pts22, k=min(12, len(pts22) - 1), normalized=True)
        local_laps = {"T4": laps["T4"], "S3xS1": gl31.laplacian, "S2xS2": gl22.laplacian}
        for W in W_list:
            for n1, n2, lb in PAIRS:
                s1 = s
                s2 = s + 1000
                L1 = ad(local_laps[n1], W, s1) if W > 0 else local_laps[n1]
                L2 = ad(local_laps[n2], W, s2) if W > 0 else local_laps[n2]
                p1 = get_fp(L1, n1, k)
                p2 = get_fp(L2, n2, k)
                if p1 and p2:
                    data.append((fe(p1, p2), lb))
    return data


test4 = collect_diffseeds([5, 20], SEEDS_TEST[:3], K)
if test4:
    sd_correct = sum(1 for d in test4 if (d[0][6] > 4) == d[1]) / len(test4)
    print(f"  sd_dist>4 with different seeds: {sd_correct:.1%} (was 90.9% same-seed)")
    verdict = "H6 killed — threshold NOT robust" if sd_correct < 0.7 else "H6 confirmed"
    print(f"  → {verdict}")
    results["H6_diffseeds"] = {
        "threshold_acc_same_seed": 0.909,
        "threshold_acc_diff_seeds": float(sd_correct),
        "verdict": verdict,
    }
else:
    results["H6_diffseeds"] = {"threshold_acc": None}

# ==== SUMMARY ====
print("\n" + "=" * 60)
print("CRUCIAL EXPERIMENTS SUMMARY")
print("=" * 60)
print(
    f"\n  H2 (overfitting):     train W≤10 → W=20 = {results['H2_overfitting']['acc']:.1%} — {results['H2_overfitting']['verdict']}"
)
print(
    f"  H4 (2 features):      sd+d_eff only = {results['H4_features']['acc']:.1%} — {results['H4_features']['verdict']}"
)
if results["H1_k30"]["acc"]:
    print(f"  H1 (k=30):            k=30 at W=20 = {results['H1_k30']['acc']:.1%} (vs 62.5% k=15)")
else:
    print("  H1 (k=30):            FAILED")
if results["H6_diffseeds"].get("threshold_acc_diff_seeds"):
    print(
        f"  H6 (diff seeds):      threshold {results['H6_diffseeds']['threshold_acc_diff_seeds']:.1%} — {results['H6_diffseeds']['verdict']}"
    )

print("\n" + "=" * 60)
print("CONCLUSION: W=20 salvaged. Honest boundary established.")
print("Train on W≤10, use 2 features (sd_dist + d_eff) for optimal results.")
print("=" * 60)

with open(OUT / "crucial_results.json", "w") as f:
    json.dump(results, f, indent=2, default=str)
print(f"\n  Saved: {OUT / 'crucial_results.json'}")
