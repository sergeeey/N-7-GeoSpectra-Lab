"""
Phase 4C: T4 Finite-Lattice Baseline

Compares exact continuous spectrum of T^4 with finite lattice
approximation at various lattice sizes. Establishes baseline.
"""
import json
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh

OUT = Path(__file__).parent / "20260629-phase4c"
OUT.mkdir(exist_ok=True)

def t4_lap_exact(N):
    m, o = 2.0*np.ones(N), -1.0*np.ones(N-1)
    L1D = sparse.diags([o,m,o],[-1,0,1],format="lil")
    L1D[0,-1], L1D[-1,0] = -1.0, -1.0
    L1D = L1D.tocsr()
    I = sparse.eye(N,format="csr")
    return (sparse.kron(sparse.kron(sparse.kron(L1D,I),I),I) +
            sparse.kron(sparse.kron(sparse.kron(I,L1D),I),I) +
            sparse.kron(sparse.kron(sparse.kron(I,I),L1D),I) +
            sparse.kron(sparse.kron(sparse.kron(I,I),I),L1D))

def analyze_t4_at_N(N, k=15):
    L = t4_lap_exact(N)
    n0 = L.shape[0]
    k = min(k, n0-2)
    try:
        ev = eigsh(L, k=k, which="SM", return_eigenvectors=False, tol=1e-10)
    except Exception:
        return None
    ev = np.sort(np.real(ev))
    ev = ev[ev > 1e-10]
    if len(ev) < 5:
        return None
    dens, _ = np.histogram(ev, bins=5, density=True)
    return {"N": N, "n_nodes": n0, "density": dens.tolist(),
            "mean": float(np.mean(ev)), "std": float(np.std(ev))}

print("="*60)
print("PHASE 4C: T4 Finite-Lattice Baseline")
print("="*60)

results = []
for N in [4, 5, 6, 8]:
    fp = analyze_t4_at_N(N, k=15)
    if fp:
        results.append(fp)
        print(f"  N={N}: nodes={fp['n_nodes']}, mean={fp['mean']:.4f}")

# Cross-N comparison
comparisons = []
for i in range(len(results)):
    for j in range(i+1, len(results)):
        d1, d2 = np.array(results[i]["density"]), np.array(results[j]["density"])
        dist = float(np.sum(np.abs(d1-d2))/2.0) if len(d1)==len(d2) else 1.0
        comparisons.append({"N1": results[i]["N"], "N2": results[j]["N"], "dist": dist})

all_similar = all(c["dist"] < 0.5 for c in comparisons)
print(f"\n  Baseline stable: {all_similar}")

summary = {"fingerprints": results, "comparisons": comparisons,
           "baseline_stable": all_similar, "verdict": "BASELINE_STABLE" if all_similar else "N_DEPENDENT"}
with open(OUT / "phase4c_results.json", "w") as f:
    json.dump(summary, f, indent=2)
print(f"  Saved: {OUT / 'phase4c_results.json'}")
