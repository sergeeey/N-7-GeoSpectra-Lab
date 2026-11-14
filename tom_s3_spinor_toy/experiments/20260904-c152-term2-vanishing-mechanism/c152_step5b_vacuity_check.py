r"""
C152 STEP 5b -- VACUITY CHECK on Step 5's scan, run BEFORE Step 5's result is
allowed to count for anything.

THE SUSPICION, stated before measuring
  The twisted Dirac operator D = sum_i E_i . grad_i is built from the metric
  and the Levi-Civita connection. J does not appear in it anywhere. In C151
  the sign tuple eps was only ever an ALIGNMENT DEVICE -- it reorders the m
  basis so that J_NK becomes the standard J_0 and round59's Clifford code can
  be reused unmodified. Reordering permutes E_i and Lambda_i TOGETHER, and
  sum_i E_i (x) Lambda_i is invariant under exactly that. If so, the 8 "different
  almost-complex structures" are 8 relabellings of ONE operator, the scan
  cannot distinguish them, and "all 8 give zero" is worth nothing.

  This is the same shape as C151 Stage 2b's own false confirmation (a check
  that 0 = i*0 satisfies perfectly). It is checked here rather than assumed,
  in either direction.

TEST: evaluate each eps's operator on the SAME fixed random vector, off the
invariant sector. If the values coincide across all 8, the scan is vacuous.

Run:  python c152_step5b_vacuity_check.py
"""

import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SCAN = importlib.util.spec_from_file_location("scan", HERE / "c152_step5_j_scan.py")
mod = importlib.util.module_from_spec(SCAN)
SCAN.loader.exec_module(mod)

E, spin_lift_np, PAIRS_M = mod.E, mod.spin_lift_np, mod.PAIRS_M


def operator(eps):
    """Rebuild ONLY the operator (no sectors), exactly as build() does."""
    basis = []
    for k, (p, q) in enumerate(PAIRS_M):
        X = np.zeros((3, 3), dtype=complex)
        X[p, q], X[q, p] = 1, -1
        Y = np.zeros((3, 3), dtype=complex)
        Y[p, q], Y[q, p] = 1j, 1j
        basis.extend([X, Y] if eps[k] > 0 else [Y, X])
    def killing_B(A, C):
        """CH2016's B(X,Y) = -(1/12)Tr(ad X ad Y) = -(1/2)Tr(XY) for su(3)."""
        return -0.5 * np.trace(A @ C)

    def to_m(M):
        """Coordinates of M in the (J-aligned) m basis."""
        return np.array([killing_B(M, b).real for b in basis])
    lam = {}
    for i in range(6):
        L = np.zeros((6, 6))
        for j in range(6):
            L[:, j] = 0.5 * to_m(basis[i] @ basis[j] - basis[j] @ basis[i])
        lam[i + 1] = L
    return sum(np.kron(E[i], -lam[i]) for i in range(1, 7))


rng = np.random.default_rng(7)
probe = rng.normal(size=48) + 1j * rng.normal(size=48)

print()
print("=" * 78)
print("VACUITY CHECK: are the 8 eps genuinely different operators?")
print("=" * 78)
ref = operator((1, 1, 1))
vals, diffs = [], []
for e1 in (1, -1):
    for e2 in (1, -1):
        for e3 in (1, -1):
            eps = (e1, e2, e3)
            op = operator(eps)
            v = float(np.linalg.norm(op @ probe))
            d = float(np.max(np.abs(op - ref)))
            vals.append(v)
            diffs.append(d)
            print(f"  eps={eps!s:>14}   ||D.probe|| = {v:.10f}   max|D - D_ref| = {d:.3e}")

spread = max(vals) - min(vals)
identical = max(diffs) < 1e-10
print()
print(f"  spread of ||D.probe|| across the 8      : {spread:.3e}")
print(f"  all 8 operators literally IDENTICAL     : {identical}")
print()
print("=" * 78)
print("VERDICT ON STEP 5")
print("=" * 78)
if identical:
    print("  *** STEP 5 IS VACUOUS. NOT A RESULT. ***")
    print("  The 8 sign tuples produce ONE operator, not eight. The scan could")
    print("  not have come out any other way, so 'zero for all 8 J' says nothing")
    print("  about whether J matters -- J is simply absent from D. The claim that")
    print("  the scan SUPPORTS the root-type reading is WITHDRAWN; the scan")
    print("  neither supports nor refutes it. The root-type reading remains an")
    print("  UNTESTED hypothesis resting on the n=2 contrast of Step 4.")
elif spread > 1e-8:
    print("  Step 5 is a genuine test: the 8 operators differ, and all still")
    print("  annihilate the invariant sector. The J-independence conclusion stands.")
else:
    print("  Operators differ as matrices but agree on the probe -- inconclusive,")
    print("  investigate before using Step 5 for anything.")
