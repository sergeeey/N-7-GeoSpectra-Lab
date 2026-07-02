"""
Phase 4B: Spectral Recoverability Phase Diagram
Maps recoverability across (W, N, pair) → recoverable / degraded / erased.
New framing: "When does geometry become unrecoverable?"
"""

import json
import sys
import warnings
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent.parent))
from cc_toy_lab.geometry.graph_laplacian import build_knn_graph_laplacian

# ── CONFIG ──────────────────────────────────────────────────────
W_VALUES = [0, 1, 2, 5, 8, 10, 12, 15, 18, 20, 25, 30]
N_CURVED = [300]  # 1 resolution (fast)
PAIRS = [("T4", "S3xS1"), ("T4", "S2xS2"), ("S3xS1", "S2xS2")]
N_SEEDS = 3
SEEDS = [42, 123, 999]
K = 15
OUT = Path(__file__).parent / "20260629-phase4b"
OUT.mkdir(exist_ok=True)


# ── UTILS ───────────────────────────────────────────────────────
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


def build_laps(n, s=42):
    n3 = max(10, int(np.sqrt(n)))
    n1 = max(5, n // n3)
    s3 = sphere(3, n3, s)
    rng = np.random.default_rng(s + 1)
    a = rng.uniform(0, 2 * np.pi, n1)
    s1 = np.column_stack([np.cos(a), np.sin(a)])
    s31 = np.array([np.concatenate([x, y]) for x in s3 for y in s1])

    na = max(5, int(np.sqrt(n)))
    nb = max(5, n // na)
    sa, sb = sphere(2, na, s), sphere(2, nb, s + 1)
    s22 = np.array([np.concatenate([x, y]) for x in sa for y in sb])

    laps = {"T4": t4_lap(6)}
    for name, pts in [("S3xS1", s31), ("S2xS2", s22)]:
        gl = build_knn_graph_laplacian(pts, k=min(12, len(pts) - 1), normalized=True)
        laps[name] = gl.laplacian
    return laps


def ad(L, W, s):
    rng = np.random.default_rng(s)
    return L + sparse.diags(rng.uniform(-W, W, L.shape[0]), format="csr")


def get_fp(L, k=15):
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
    return {
        "r": r,
        "d": float(deff),
        "cv": cv,
        "ds": dens.tolist() if dens is not None else [],
        "ev": ev.tolist(),
    }


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


def fe2(a, b):
    return [sd(a["ev"], b["ev"]), abs(a["d"] - b["d"])]


def phase_cell(W, n, pair, laps):
    g1, g2 = pair
    sd_vals = []
    fe2s = []
    lbs = []

    for s in SEEDS:
        L1 = ad(laps[g1], W, s) if W > 0 else laps[g1]
        L2 = ad(laps[g2], W, s) if W > 0 else laps[g2]
        p1 = get_fp(L1, K)
        p2 = get_fp(L2, K)
        if p1 and p2:
            sd_vals.append(sd(p1["ev"], p2["ev"]))
            fe2s.append(fe2(p1, p2))
            lbs.append(1 if g1 != g2 else 0)

    if not sd_vals:
        return None

    sd_acc = sum(1 for d, lb in zip(sd_vals, lbs) if (d > 4) == lb) / len(lbs)
    mean_sd = float(np.mean(sd_vals))

    two_acc = None
    if len(fe2s) >= 3:
        correct = 0
        for i in range(len(fe2s)):
            sd_d, deff_d = fe2s[i][0], fe2s[i][1]
            pred = 1 if (sd_d > 4 or deff_d > 2.0) else 0
            if pred == lbs[i]:
                correct += 1
        two_acc = correct / len(fe2s)

    p = "erased"
    if sd_acc >= 0.95 or (two_acc is not None and two_acc >= 0.95):
        p = "recoverable"
    elif sd_acc >= 0.70 or (two_acc is not None and two_acc >= 0.70):
        p = "degraded"

    return {
        "W": W,
        "N": n,
        "pair": f"{g1}_vs_{g2}",
        "sd_acc": sd_acc,
        "two_acc": two_acc,
        "mean_sd": mean_sd,
        "phase": p,
        "n_samples": len(sd_vals),
    }


# ── MAIN ────────────────────────────────────────────────────────
print("=" * 60)
print("PHASE 4B: Spectral Recoverability Phase Diagram")
print(
    f"Grid: {len(W_VALUES)} W x {len(N_CURVED)} N x {len(PAIRS)} pairs = {len(W_VALUES) * len(N_CURVED) * len(PAIRS)} cells"
)
print("=" * 60)

diagram = []
cell_idx = 0
total = len(W_VALUES) * len(N_CURVED) * len(PAIRS)

for n in N_CURVED:
    print(f"\n[N={n}] Building Laplacians...")
    laps = build_laps(n)
    print(
        f"  T4: {laps['T4'].shape[0]}, S3xS1: {laps['S3xS1'].shape[0]}, S2xS2: {laps['S2xS2'].shape[0]}"
    )

    for pair in PAIRS:
        for W in W_VALUES:
            cell_idx += 1
            cell = phase_cell(W, n, pair, laps)
            if cell:
                diagram.append(cell)
                sym = {"recoverable": "G", "degraded": "Y", "erased": "R"}[cell["phase"]]
                two_str = f"2f={cell['two_acc']:.1%}" if cell["two_acc"] is not None else "2f=N/A"
                print(
                    f"  [{cell_idx}/{total}] W={W:2d} {pair[0]}v{pair[1]:5s}: sd={cell['sd_acc']:.1%} {two_str:8s} -> {sym} {cell['phase']}"
                )
            else:
                print(f"  [{cell_idx}/{total}] W={W:2d} {pair[0]}v{pair[1]:5s}: FAILED")

# ── SUMMARY ─────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("PHASE DIAGRAM SUMMARY")
print("=" * 60)

for p in ["recoverable", "degraded", "erased"]:
    c = sum(1 for x in diagram if x["phase"] == p)
    sym = {"recoverable": "RECOVERABLE", "degraded": "DEGRADED", "erased": "ERASED"}[p]
    print(f"  {sym:12s}: {c:2d} / {len(diagram)} ({c / len(diagram) * 100:.1f}%)")

for pair in PAIRS:
    pname = f"{pair[0]}_vs_{pair[1]}"
    cells = sorted([c for c in diagram if c["pair"] == pname], key=lambda x: (x["N"], x["W"]))
    print(f"\n{pname}:")
    for c in cells:
        sym = {"recoverable": "G", "degraded": "Y", "erased": "R"}[c["phase"]]
        print(f"  W={c['W']:2d} N={c['N']:3d} {sym} {c['phase']:12s} sd={c['sd_acc']:.1%}")

with open(OUT / "phase4b_results.json", "w") as f:
    json.dump(diagram, f, indent=2, default=str)
print(f"\nSaved: {OUT / 'phase4b_results.json'}")
