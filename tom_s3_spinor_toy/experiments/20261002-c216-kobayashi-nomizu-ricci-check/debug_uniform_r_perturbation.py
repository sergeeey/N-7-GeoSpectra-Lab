"""Debug: is the SO(7)/SO(6) control's 2.5-vs-5.0 discrepancy a smooth function
of r, or a discontinuity specific to EXACTLY uniform r? If Castellani's Ricci
stays at ~2.5 even for slightly non-uniform r (while KN would still give ~5.0
for the now-slightly-squashed metric, computed separately for comparison),
that rules out "degenerate uniform-r code path" as the mechanism and points
back toward either a genuine C_KKK=0 (symmetric-space) issue or a generator-
normalization mismatch in how this control's K/H were built.
"""

import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "c213",
    HERE.parent / "20261002-c213-castellani-ricci-g2su3-calibrated" / "c213_castellani_ricci.py",
)
c213 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c213)


def a_ij(i, j, n=7):
    m = np.zeros((n, n))
    m[i, j], m[j, i] = 1.0, -1.0
    return m / np.sqrt(2.0)


K = [a_ij(i, 6) for i in range(6)]
H = [a_ij(i, j) for i in range(6) for j in range(i + 1, 6)]
N = np.zeros(7)
N[6] = 1.0
norm_sq = float(np.mean([np.dot(g @ N, g @ N) for g in K]))
scale = 1.0 / np.sqrt(norm_sq)

C_KKK, C_KKH, C_HKK, C_HHH, max_res = c213.build_structure_constants(K, H)
print(
    f"max_res={max_res:.2e}, C_KKK max abs = {np.max(np.abs(C_KKK)):.6f} (expect 0 for symmetric space)"
)

for eps in [0.0, 1e-6, 1e-3, 1e-2, 0.1, 0.3]:
    # Perturb: generator 0 gets scale*(1+eps), rest stay at scale.
    r = scale * np.ones(6)
    r[0] = scale * (1.0 + eps)
    ricci = c213.riemann_ricci(C_KKK, C_KKH, C_HKK, r)
    print(f"eps={eps:8.1e}  diag(ricci)={np.round(np.diag(ricci), 6)}")
