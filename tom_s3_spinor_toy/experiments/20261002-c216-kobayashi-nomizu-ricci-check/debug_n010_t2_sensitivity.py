"""Debug: does doubling term2's coefficient (0.5 -> 1.0) in Castellani's
riemann() break the N^010 double-calibration (published R=12 at eq 5.72 and
5.73) that C213 originally validated against? This tells us whether the
factor-of-2 bug isolated on the SO(7)/SO(6) symmetric control (where only
term2 survives) is a uniform coefficient bug, or something narrower/different
that the N^010 calibration (which exercises all 4 terms together) happens not
to expose the same way.
"""

import importlib.util
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "c213",
    HERE.parent / "20261002-c213-castellani-ricci-g2su3-calibrated" / "c213_castellani_ricci.py",
)
c213 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c213)

K, H = c213.build_n010()
C_KKK, C_KKH, C_HKK, C_HHH, max_res = c213.build_structure_constants(K, H)
print("max_res", max_res)


def riemann_ricci_t2(C_KKK, C_KKH, C_HKK, r, t2_coeff):
    n_K, n_H = C_KKK.shape[0], C_KKH.shape[0]

    def cbold(a, b, c):
        return (
            (r[b] * r[c] / r[a]) * C_KKK[a, b, c]
            - (r[a] * r[c] / r[b]) * C_KKK[b, a, c]
            - (r[a] * r[b] / r[c]) * C_KKK[c, a, b]
        )

    def riemann(a, b, d, e):
        t1 = sum((r[d] * r[e] / r[c]) * cbold(a, b, c) * C_KKK[c, d, e] for c in range(n_K)) * 0.25
        t2 = sum(-C_HKK[b, i, a] * C_KKH[i, d, e] for i in range(n_H)) * t2_coeff * r[d] * r[e]
        t3 = sum(cbold(a, c, d) * cbold(c, b, e) for c in range(n_K)) * 0.125
        t4 = -sum(cbold(a, c, e) * cbold(c, b, d) for c in range(n_K)) * 0.125
        return t1 + t2 + t3 + t4

    ricci = np.zeros((n_K, n_K))
    for b in range(n_K):
        for d in range(n_K):
            ricci[b, d] = sum(riemann(a, b, a, d) for a in range(n_K))
    return ricci


for label, a2, b2 in [("5.72", 4, 32), ("5.73", 100 / 9, 160 / 9)]:
    alpha, beta = math.sqrt(a2), math.sqrt(b2)
    r = np.array([alpha, alpha, alpha, beta, beta, beta, beta])
    ricci05 = riemann_ricci_t2(C_KKK, C_KKH, C_HKK, r, 0.5)
    ricci10 = riemann_ricci_t2(C_KKK, C_KKH, C_HKK, r, 1.0)
    print(f"{label} (published target R=12):")
    print(f"  t2=0.5 (original) diag={np.round(np.diag(ricci05), 6)}")
    print(f"  t2=1.0 (test fix) diag={np.round(np.diag(ricci10), 6)}")
