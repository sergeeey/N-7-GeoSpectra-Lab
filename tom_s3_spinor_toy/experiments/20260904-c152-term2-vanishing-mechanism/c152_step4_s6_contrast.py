r"""
C152 STEP 4 -- the cross-space control. Run the IDENTICAL per-direction
decomposition on S^6 = G2/SU(3), under the SAME T^2, and locate the exact
structural point at which the pairwise cancellation found on SU(3)/T^2 fails.

WHY THIS IS THE POINT OF THE ROUND
  Step 3 established that on SU(3)/T^2 the zero is forced by EQUIVARIANCE of
  the connection, not by nearly-Kahler geometry: every T^2-equivariant
  connection gives zero, a non-equivariant one does not. But the S^6
  connection is ALSO T^2-equivariant (it is SU(3)-equivariant, and T^2 is a
  subgroup) -- and there Term2 is NONZERO (C145/C147). So "equivariance" by
  itself cannot be the whole story. Something about the two m's must differ.

  m for SU(3)/T^2 = root spaces  (weights ARE roots)
  m for S^6       = 3 (+) 3bar   (weights are NOT roots)

  This file tests whether that is the discriminator, by measuring the same
  quantities on both sides.

Reuses round59's own Clifford/Nomizu/su(3) machinery unmodified, with its own
Killing-spinor calibration re-verified on import.

Run:  python c152_step4_s6_contrast.py
"""

import importlib.util
from itertools import combinations
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
R59_PATH = (
    HERE.parent / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


R59 = load_module("round59_route_a_independent", R59_PATH)

E_sym = R59.build_clifford(conj=False)
E = {i: np.array(E_sym[i].evalf(), dtype=complex) for i in range(1, 7)}
calib_ok, _ = R59.run_calibration(E_sym, R59.NOMIZU)
assert calib_ok, "round59's Killing-spinor calibration failed on import -- STOP"
print("STEP 4  round59 imported, its own calibration gate re-verified  [OK]")


def spin_lift_np(L: np.ndarray) -> np.ndarray:
    out = np.zeros((8, 8), dtype=complex)
    for a in range(6):
        for b in range(a + 1, 6):
            if abs(L[a, b]) > 1e-14:
                out += L[a, b] * 0.5 * (E[a + 1] @ E[b + 1])
    return out


def bivec_to_6x6(terms) -> np.ndarray:
    m = np.zeros((6, 6), dtype=complex)
    for coeff, a, b in terms:
        m[a - 1, b - 1] += float(coeff)
        m[b - 1, a - 1] -= float(coeff)
    return m


LAM = {i: bivec_to_6x6(R59.NOMIZU[i]) for i in range(1, 7)}
ADNU_M = {a: bivec_to_6x6(R59.ADNU[a]) for a in range(1, 9)}
ADNU_S = {a: spin_lift_np(ADNU_M[a]) for a in range(1, 9)}

# ---------------------------------------------------------------------------
# Locate a Cartan pair inside su(3) by commutation, not by index convention.
# ---------------------------------------------------------------------------
cartan = None
for a, b in combinations(range(1, 9), 2):
    if np.max(np.abs(ADNU_M[a] @ ADNU_M[b] - ADNU_M[b] @ ADNU_M[a])) < 1e-10:
        cartan = (a, b)
        break
assert cartan is not None, "no commuting pair found in su(3) action on m -- STOP"
print(f"STEP 4  Cartan pair of su(3) located by commutation: generators {cartan}")

I6 = np.eye(6)
SPIN_VS_VEC = -1  # same gate as SU(3)/T^2 side; re-checked below
sig = []
for i in range(1, 7):
    for j in range(1, 7):
        lhs = spin_lift_np(LAM[i]) @ E[j] - E[j] @ spin_lift_np(LAM[i])
        rhs = sum((LAM[i][k - 1, j - 1] * E[k] for k in range(1, 7)), np.zeros((8, 8), complex))
        if np.max(np.abs(rhs)) > 1e-10:
            sig.append(1 if np.max(np.abs(lhs - rhs)) < 1e-10 else -1)
assert all(s == sig[0] for s in sig), "vector-rep sign inconsistent on S^6 -- STOP"
SPIN_VS_VEC = sig[0]
print(f"STEP 4  vector-rep sign gate on S^6: {SPIN_VS_VEC:+d} ({len(sig)} pairs)")

# ---------------------------------------------------------------------------
# T^2-invariant domain / target inside Sigma (x) W, W = m_C.
# ---------------------------------------------------------------------------
# C139's vector rep of su(3) on W carries the SAME sign correction as the
# connection: rho_vector(X) = -bivec(X). Using +ADNU_M here silently builds a
# DIFFERENT group action and hence a wrong invariant sector -- this cost one
# false 'S^6 Term2 = 0' before the C145 regression below caught it.
RHO_W = {a: SPIN_VS_VEC * ADNU_M[a] for a in range(1, 9)}
gens48 = [np.kron(ADNU_S[a], I6) + np.kron(np.eye(8), RHO_W[a]) for a in cartan]
gens48_full = [np.kron(ADNU_S[a], I6) + np.kron(np.eye(8), RHO_W[a]) for a in range(1, 9)]


def invariant_in_block(rows: list[int], gens) -> np.ndarray:
    idx = [r * 6 + c for r in rows for c in range(6)]
    P = np.zeros((48, len(idx)))
    for k, j in enumerate(idx):
        P[j, k] = 1.0
    stacked = np.vstack([g @ P for g in gens])
    _, sv, vh = np.linalg.svd(stacked)
    padded = np.concatenate([sv, np.zeros(len(idx) - len(sv))])
    return P @ vh.conj().T[:, np.abs(padded) < 1e-8]


dom = invariant_in_block(R59.ODD_IDX, gens48)
tgt = invariant_in_block(R59.EVEN_IDX, gens48)

# --- HARD REGRESSION against C145's own published su(3)-sector value ---------
dom_su3 = invariant_in_block(R59.ODD_IDX, gens48_full)
tgt_su3 = invariant_in_block(R59.EVEN_IDX, gens48_full)
assert dom_su3.shape[1] == 1 and tgt_su3.shape[1] == 1, (
    f"su(3)-sector must be 1-dim per C139: got {dom_su3.shape[1]},{tgt_su3.shape[1]}")
_t2 = sum(np.kron(E[i], SPIN_VS_VEC * LAM[i]) for i in range(1, 7))
_val = complex((tgt_su3.conj().T @ _t2 @ dom_su3)[0, 0])
print(f"STEP 4  REGRESSION vs C145: |Term2| on the su(3)-sector = {abs(_val):.6f}  "
      f"(C145 published 1.154701)")
assert abs(abs(_val) - 1.154701) < 1e-5, (
    f"C145 regression FAILED: got {abs(_val)}, expected 1.154701 -- STOP, machinery is wrong")
print(f"STEP 4  T^2-invariant sectors on S^6 : domain {dom.shape[1]}, target {tgt.shape[1]} "
      f"(Step 1 predicted 3 and 3)")
assert dom.shape[1] == 3 and tgt.shape[1] == 3, "S^6 T^2-sector dims disagree with Step 1"

# ---------------------------------------------------------------------------
per_i = {i: tgt.conj().T @ np.kron(E[i], SPIN_VS_VEC * LAM[i]) @ dom for i in range(1, 7)}
T2 = sum(per_i.values())
t1_i = {i: tgt.conj().T @ np.kron(E[i] @ spin_lift_np(LAM[i]), I6) @ dom for i in range(1, 7)}
T1 = sum(t1_i.values())

print()
print("=" * 78)
print("S^6 : per-direction contributions to the T^2-invariant 3x3 block")
print("=" * 78)
print(f"{'i':>3}  {'max|Term1_i|':>14}  {'max|Term2_i|':>14}")
for i in range(1, 7):
    print(f"{i:>3}  {np.max(np.abs(t1_i[i])):>14.6f}  {np.max(np.abs(per_i[i])):>14.6f}")
print(f"{'SUM':>3}  {np.max(np.abs(T1)):>14.3e}  {np.max(np.abs(T2)):>14.3e}")

live = max(((r, c) for r in range(3) for c in range(3)),
           key=lambda rc: max(abs(per_i[i][rc]) for i in range(1, 7)))
print()
print(f"  entry {live} (most alive), contribution by direction:")
for i in range(1, 7):
    z = per_i[i][live]
    print(f"    i={i}:  {z.real:+.6f} {z.imag:+.6f}j   |z| = {abs(z):.6f}")
print(f"    SUM  :  {sum(per_i[i][live] for i in range(1,7)):.6f}")

print()
print("=" * 78)
print("THE DISCRIMINATOR")
print("=" * 78)
print("  SU(3)/T^2 : Term1 per-direction ZERO (weight-forced), Term2 per-direction")
print("              ALIVE (|.|=0.5) but summing to ZERO -- pairwise cancellation")
print(f"  S^6       : Term1 sum = {np.max(np.abs(T1)):.3e}, Term2 sum = {np.max(np.abs(T2)):.3e}")
if np.max(np.abs(T2)) > 1e-10:
    print()
    print("  -> Term2 SURVIVES on S^6 under the SAME T^2 and the SAME tensorial")
    print("     construction. Both connections are T^2-equivariant, so equivariance")
    print("     alone does NOT force the zero. The remaining difference between the")
    print("     two cases is the weight TYPE of m: root-type on SU(3)/T^2 (where m's")
    print("     weights are the roots themselves, so the 6 directions pair up inside")
    print("     root planes on which T^2 acts by rotation) versus fundamental-type on")
    print("     S^6 (m = 3 (+) 3bar, weights not roots, no such pairing).")
else:
    print("  -> Term2 ALSO vanishes on S^6 in the T^2-invariant sector. Then the")
    print("     nonzero C145/C147 value must live entirely outside it -- re-check,")
    print("     since the su(3)-invariant sector is a SUBSPACE of this one.")
