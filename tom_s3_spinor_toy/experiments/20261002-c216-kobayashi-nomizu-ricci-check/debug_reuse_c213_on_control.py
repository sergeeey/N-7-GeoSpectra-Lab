"""Debug: reuse C213's OWN validated riemann_ricci (not a C216 rewrite) on the
round S6=SO(7)/SO(6) control, to isolate whether the 2.5-vs-5.0 mismatch is a
C216 transcription bug or a real issue in C213's own uniform-r application."""

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


def a_ij(i, j):
    m = np.zeros((7, 7))
    m[i, j], m[j, i] = 1.0, -1.0
    return m / np.sqrt(2.0)


K = [a_ij(i, 6) for i in range(6)]
H = [a_ij(i, j) for i in range(6) for j in range(i + 1, 6)]
N = np.zeros(7)
N[6] = 1.0
norm_sq = float(np.mean([np.dot(g @ N, g @ N) for g in K]))
scale = 1.0 / np.sqrt(norm_sq)
print(f"scale={scale}, norm_sq={norm_sq}")

C_KKK, C_KKH, C_HKK, C_HHH, max_res = c213.build_structure_constants(K, H)
print(f"max_res={max_res:.2e}")
r = scale * np.ones(6)
ricci = c213.riemann_ricci(C_KKK, C_KKH, C_HKK, r)
print("diag(ricci) =", np.round(np.diag(ricci), 6))
print("off-diag max =", np.max(np.abs(ricci - np.diag(np.diag(ricci)))))
