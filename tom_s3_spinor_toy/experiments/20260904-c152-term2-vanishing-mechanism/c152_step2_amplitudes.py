r"""
C152 STEP 2 -- resolve Term2's invariant-sector block into its per-direction
contributions on SU(3)/T^2. Step 1 refuted H1 (6 admissible weight paths
exist); this file asks HOW the amplitudes along them come out to zero.

TWO STRUCTURALLY DIFFERENT WAYS TO GET ZERO, and they mean different things

  (a) each direction i contributes something nonzero, and the six
      contributions CANCEL in the sum        -> a real cancellation (H2)
  (b) each direction i contributes zero on its own
                                             -> a per-direction identity,
                                                stronger than a cancellation,
                                                and a candidate for H3

Distinguishing these costs nothing extra and is the whole point of resolving
the sum instead of re-printing the total. C151 Stage 2b only ever printed the
total.

Reuses C151 Stage 2a's construction unmodified (which passed its own
independent Killing-spinor calibration gate: 2 invariant spinors, D_Sigma
eigenvalues exactly +-3).

Run:  python c152_step2_amplitudes.py
"""

import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
S2A_PATH = HERE.parent / "20260904-c151-stage0-su3t2-scoping" / "c151_stage2_construct.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


S2A = load_module("c151_stage2_construct", S2A_PATH)
E, spin, dom, tgt = S2A.E, S2A.spin_lift_np, S2A.dom, S2A.tgt
LAM = {i: S2A.NOMIZU_LC[i].astype(complex) for i in range(1, 7)}
I6 = np.eye(6)

# ---------------------------------------------------------------------------
# Sign gate for the vector rep, re-derived here rather than inherited as a
# constant (same gate C151 Stage 2b ran).
# ---------------------------------------------------------------------------
signs = []
for i in range(1, 7):
    L = LAM[i]
    for j in range(1, 7):
        lhs = spin(L) @ E[j] - E[j] @ spin(L)
        rhs = sum((L[k - 1, j - 1] * E[k] for k in range(1, 7)), np.zeros((8, 8), dtype=complex))
        if np.max(np.abs(rhs)) > 1e-10:
            signs.append(1 if np.max(np.abs(lhs - rhs)) < 1e-10 else -1)
SPIN_VS_VEC = signs[0]
assert all(s == SPIN_VS_VEC for s in signs), "vector-rep sign not consistent -- STOP"
print(f"STEP 2  vector-rep sign gate: SPIN_VS_VEC = {SPIN_VS_VEC:+d} "
      f"(consistent across {len(signs)} pairs)")

# ---------------------------------------------------------------------------
# Per-direction contributions to the invariant-sector block.
# ---------------------------------------------------------------------------
term1_i = {i: tgt.conj().T @ np.kron(E[i] @ spin(LAM[i]), I6) @ dom for i in range(1, 7)}
term2_i = {i: tgt.conj().T @ np.kron(E[i], SPIN_VS_VEC * LAM[i]) @ dom for i in range(1, 7)}

T1 = sum(term1_i.values())
T2 = sum(term2_i.values())

print()
print("=" * 78)
print("PER-DIRECTION CONTRIBUTIONS TO THE 3x3 INVARIANT BLOCK")
print("=" * 78)
print(f"{'i':>3}  {'max|Term1_i|':>14}  {'max|Term2_i|':>14}")
for i in range(1, 7):
    print(f"{i:>3}  {np.max(np.abs(term1_i[i])):>14.6f}  {np.max(np.abs(term2_i[i])):>14.6f}")
print(f"{'SUM':>3}  {np.max(np.abs(T1)):>14.3e}  {np.max(np.abs(T2)):>14.3e}")

t2_alive = [i for i in range(1, 7) if np.max(np.abs(term2_i[i])) > 1e-10]
t1_alive = [i for i in range(1, 7) if np.max(np.abs(term1_i[i])) > 1e-10]

print()
print("=" * 78)
print("VERDICT ON THE MECHANISM")
print("=" * 78)
print(f"  directions with NONZERO Term1_i : {t1_alive if t1_alive else 'none'}")
print(f"  directions with NONZERO Term2_i : {t2_alive if t2_alive else 'none'}")
print()
if t2_alive:
    print("  (a) REAL CANCELLATION: individual directions contribute, the sum")
    print("      cancels. The zero is a property of the SUM, not of each term.")
    print("      -> consistent with H2; Step 3's perturbation must break it.")
else:
    print("  (b) PER-DIRECTION ZERO: every single direction annihilates the")
    print("      invariant domain on its own. Nothing cancels -- there is")
    print("      nothing to cancel. This is STRONGER than a cancellation and")
    print("      is the H3 signature: an identity holding term by term.")
    print("      -> Step 3's perturbation is then predicted NOT to break it")
    print("         (P1), since no coefficient balance is being relied on.")

# ---------------------------------------------------------------------------
# Which of the 9 entries were even allowed by weights? (Step 1 said 6 of 9.)
# Print the full block so the 3 weight-forbidden entries are visible as such.
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("THE 3x3 BLOCK ITSELF (all entries, so forbidden vs allowed is visible)")
print("=" * 78)
print("  Term2 block, entrywise |.|:")
for r in range(3):
    print("   ", "  ".join(f"{abs(T2[r, c]):.3e}" for c in range(3)))
