"""Debug: break down Castellani's riemann() into its 4 terms (t1,t2,t3,t4)
separately on BOTH controls, to isolate exactly which term(s) carry the
factor-of-2 discrepancy found in C216 (SO(7)/SO(6) control: Castellani gives
2.5 instead of the textbook-correct 5.0; G2/SU(3): Castellani gives 2.5 while
KN's independently-calibrated route gives 4.0, not matching C215's naive
Ric^grad=1.5 either).

Hypothesis under test: term2's coefficient (0.5) should be 1.0 -- i.e. a
missing factor of 2 specifically in the H-curvature term, not a global
normalization issue. Tested by recomputing ricci with t2 coefficient doubled,
on BOTH controls, and checking whether:
  (a) SO(7)/SO(6) control -> 5.0 (textbook correct)
  (b) G2/SU(3) -> matches KN's independently-verified Ric^c=4.0
If BOTH hold with the SAME fix, that pins down the bug precisely.
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


def riemann_ricci_breakdown(C_KKK, C_KKH, C_HKK, r, t2_coeff=0.5):
    n_K, n_H = C_KKK.shape[0], C_KKH.shape[0]

    def cbold(a, b, c):
        return (
            (r[b] * r[c] / r[a]) * C_KKK[a, b, c]
            - (r[a] * r[c] / r[b]) * C_KKK[b, a, c]
            - (r[a] * r[b] / r[c]) * C_KKK[c, a, b]
        )

    def riemann_terms(a, b, d, e):
        t1 = sum((r[d] * r[e] / r[c]) * cbold(a, b, c) * C_KKK[c, d, e] for c in range(n_K)) * 0.25
        t2 = sum(-C_HKK[b, i, a] * C_KKH[i, d, e] for i in range(n_H)) * t2_coeff * r[d] * r[e]
        t3 = sum(cbold(a, c, d) * cbold(c, b, e) for c in range(n_K)) * 0.125
        t4 = -sum(cbold(a, c, e) * cbold(c, b, d) for c in range(n_K)) * 0.125
        return t1, t2, t3, t4

    ricci_t1 = np.zeros((n_K, n_K))
    ricci_t2 = np.zeros((n_K, n_K))
    ricci_t3 = np.zeros((n_K, n_K))
    ricci_t4 = np.zeros((n_K, n_K))
    for b in range(n_K):
        for d in range(n_K):
            for a in range(n_K):
                t1, t2, t3, t4 = riemann_terms(a, b, a, d)
                ricci_t1[b, d] += t1
                ricci_t2[b, d] += t2
                ricci_t3[b, d] += t3
                ricci_t4[b, d] += t4
    return ricci_t1, ricci_t2, ricci_t3, ricci_t4


def a_ij(i, j, n=7):
    m = np.zeros((n, n))
    m[i, j], m[j, i] = 1.0, -1.0
    return m / np.sqrt(2.0)


def so7_control():
    K = [a_ij(i, 6) for i in range(6)]
    H = [a_ij(i, j) for i in range(6) for j in range(i + 1, 6)]
    N = np.zeros(7)
    N[6] = 1.0
    norm_sq = float(np.mean([np.dot(g @ N, g @ N) for g in K]))
    scale = 1.0 / np.sqrt(norm_sq)
    return K, H, scale


def g2su3_data():
    spec2 = importlib.util.spec_from_file_location(
        "g96_g2_su3", HERE.parent / "20260626-g96-s6-g2-su3" / "g96_g2_su3.py"
    )
    g96 = importlib.util.module_from_spec(spec2)
    spec2.loader.exec_module(g96)

    phi = g96.build_phi()
    gens = g96.find_g2_generators(phi)
    N = np.zeros(7)
    N[6] = 1.0
    A = np.column_stack([G @ N for G in gens])
    _, sv, Vt = np.linalg.svd(A, full_matrices=True)
    rank = int(np.sum(sv > 1e-10))
    null = Vt[rank:]
    gm = np.array([G.flatten() for G in gens])
    su3 = [row.reshape(7, 7) for row in (null @ gm)]
    Qsu3, _ = np.linalg.qr(np.column_stack([g.flatten() for g in su3]), mode="reduced")
    comp_vecs = []
    for G in gens:
        gf = G.flatten()
        res = gf - Qsu3 @ (Qsu3.T @ gf)
        if np.linalg.norm(res) > 1e-10:
            comp_vecs.append(res)
    Qc, Rc = np.linalg.qr(np.column_stack(comp_vecs), mode="reduced")
    ncomp = int(np.sum(np.abs(np.diag(Rc)) > 1e-10))
    comp = [Qc[:, k].reshape(7, 7) for k in range(ncomp)]
    tangent = np.array([G @ N for G in comp])
    norm_sq = float(np.mean(np.diag(tangent @ tangent.T)))
    rescale = 1.0 / np.sqrt(norm_sq)
    return comp, su3, rescale


def report(label, K, H, scale):
    print(f"\n--- {label} ---")
    C_KKK, C_KKH, C_HKK, _C_HHH, _max_res = c213.build_structure_constants(K, H)
    r = scale * np.ones(len(K))

    for t2c, tag in [(0.5, "ORIGINAL t2_coeff=0.5"), (1.0, "TEST t2_coeff=1.0")]:
        t1, t2, t3, t4 = riemann_ricci_breakdown(C_KKK, C_KKH, C_HKK, r, t2_coeff=t2c)
        total = t1 + t2 + t3 + t4
        e1, e2, e3, e4 = (float(np.mean(np.diag(x))) for x in (t1, t2, t3, t4))
        etot = float(np.mean(np.diag(total)))
        off = float(np.max(np.abs(total - np.diag(np.diag(total)))))
        print(
            f"  [{tag}] t1={e1:.6f} t2={e2:.6f} t3={e3:.6f} t4={e4:.6f}  TOTAL={etot:.6f}  off-diag={off:.2e}"
        )


K0, H0, s0 = so7_control()
report("CONTROL SO(7)/SO(6), expect textbook Ric=5", K0, H0, s0)

K1, H1, s1 = g2su3_data()
report("G2/SU(3), ambient-unit frame", K1, H1, s1)

print("\nKN independently-verified values for comparison:")
print("  CONTROL: Ric^c_KN = 5.000000 (textbook n-1=5)")
print("  G2/SU(3): Ric^c_KN = 4.000000")
