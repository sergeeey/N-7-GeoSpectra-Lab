"""
Phase 4D: Cross-Geometry Spectral Transfer

Tests whether spectral features transfer across geometry types.
Pairs: T4 vs S3xS1, T4 vs S2xS2, S3xS1 vs S2xS2.
"""
import json, sys, warnings
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent.parent))
from cc_toy_lab.geometry.graph_laplacian import build_knn_graph_laplacian

OUT = Path(__file__).parent / "20260629-phase4d"
OUT.mkdir(exist_ok=True)

def t4_lap(N):
    m, o = 2.0*np.ones(N), -1.0*np.ones(N-1)
    L = sparse.diags([o,m,o],[-1,0,1],format="lil")
    L[0,-1], L[-1,0] = -1.0, -1.0
    L = L.tocsr()
    I = sparse.eye(N,format="csr")
    return (sparse.kron(sparse.kron(sparse.kron(L,I),I),I) +
            sparse.kron(sparse.kron(sparse.kron(I,L),I),I) +
            sparse.kron(sparse.kron(sparse.kron(I,I),L),I) +
            sparse.kron(sparse.kron(sparse.kron(I,I),I),L))

def sphere(d,N,s):
    rng = np.random.default_rng(s)
    p = rng.standard_normal((N, d+1))
    return p / np.linalg.norm(p, axis=1, keepdims=True)

def build_all_laps():
    laps = {"T4": t4_lap(6)}
    s3 = sphere(3, 50, 42)
    rng = np.random.default_rng(43)
    a = rng.uniform(0, 2*np.pi, 8)
    s1 = np.column_stack([np.cos(a), np.sin(a)])
    pts = np.array([np.concatenate([x,y]) for x in s3 for y in s1])
    laps["S3xS1"] = build_knn_graph_laplacian(pts, k=min(12,len(pts)-1), normalized=True).laplacian
    sa, sb = sphere(2, 50, 42), sphere(2, 50, 43)
    pts2 = np.array([np.concatenate([x,y]) for x in sa for y in sb])
    laps["S2xS2"] = build_knn_graph_laplacian(pts2, k=min(12,len(pts2)-1), normalized=True).laplacian
    return laps

def get_fp(L, k=15):
    n0 = L.shape[0]
    k = min(k, n0-2)
    try:
        ev = eigsh(L, k=k, which="SM", return_eigenvectors=False, tol=1e-8)
    except Exception:
        return None
    ev = np.sort(np.real(ev))
    ev = ev[ev > 1e-10]
    if len(ev) < 5: return None
    dens, _ = np.histogram(ev, bins=5, density=True)
    return {"density": dens.tolist(), "mean": float(np.mean(ev)), "std": float(np.std(ev))}

laps = build_all_laps()
print("="*60)
print("PHASE 4D: Cross-Geometry Spectral Transfer")
print("="*60)

geoms = {n: get_fp(L, 15) for n, L in laps.items() if get_fp(L, 15)}
for n in geoms: print(f"  {n}: features extracted")

PAIRS = [("T4","S3xS1"), ("T4","S2xS2"), ("S3xS1","S2xS2")]
results = []
for g1, g2 in PAIRS:
    if g1 not in geoms or g2 not in geoms: continue
    d1, d2 = np.array(geoms[g1]["density"]), np.array(geoms[g2]["density"])
    dist = float(np.sum(np.abs(d1-d2))/2.0)
    distinct = dist > 0.3
    results.append({"pair": f"{g1}_vs_{g2}", "dist": dist, "distinct": distinct})
    print(f"  {g1} vs {g2}: dist={dist:.1f} {'DISTINCT' if distinct else 'SIMILAR'}")

n_d = sum(1 for r in results if r["distinct"])
pct = n_d/len(results)*100 if results else 0
print(f"\n  Distinct: {n_d}/{len(results)} ({pct:.0f}%)")

summary = {"pairs": results, "distinct": n_d, "total": len(results), "percent": pct,
           "verdict": "CROSS_GEOMETRY_DISTINCT" if pct >= 50 else "SIMILAR"}
with open(OUT / "phase4d_results.json", "w") as f:
    json.dump(summary, f, indent=2)
print(f"  Saved: {OUT / 'phase4d_results.json'}")
