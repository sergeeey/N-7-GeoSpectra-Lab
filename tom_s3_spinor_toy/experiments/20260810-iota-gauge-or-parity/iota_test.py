"""Test (c): is iota(g) = g^-1 a GAUGE symmetry or a PARITY-like discrete one?

WHY THIS DECIDES THE CONSOLIDATED QUESTION. C38 showed ker(D_S3,t=0) = (1,2) and
ker(D_S3,t=1) = (2,1) -- the two halves of one Spin(4) spinor, exchanged by iota.
C37/OB13 raised the branch that iota might be a GAUGE redundancy, in which case
"which t" is ill-posed. But those two readings CONFLICT:

  - if iota is GAUGE, then (1,2) and (2,1) are the same physical state and there
    is no 4-dim spinor -- C38's reconciliation collapses;
  - if iota is a DISCRETE symmetry (parity-like), the two halves are genuinely
    distinct physical states and C38's reconciliation stands.

One computation separates them: a gauge symmetry is connected to the identity
and orientation-PRESERVING. A parity is orientation-REVERSING.

THE COMPUTATION. On S^3 = SU(2) in quaternion coordinates,
g(x) = x0 + x1 Z1 + x2 Z2 + x3 Z3 with |x| = 1, so

    iota : (x0, x1, x2, x3)  ->  (x0, -x1, -x2, -x3)

Its differential on the ambient R^4 is diag(1,-1,-1,-1). What matters is the
induced map on the TANGENT space of S^3, computed here at several points rather
than argued at the north pole only.

WHAT THIS CANNOT SHOW, fixed before running: orientation-reversal establishes
that iota is not gauge; it does NOT establish that any particular term in an
action actually selects an endpoint. That remains C11's question.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_iota_test.json"
results: dict = {}

I2 = np.eye(2, dtype=complex)
Z = [1j * np.array([[0, 1], [1, 0]], dtype=complex),
     1j * np.array([[0, -1j], [1j, 0]], dtype=complex),
     1j * np.array([[1, 0], [0, -1]], dtype=complex)]
IOTA4 = np.diag([1.0, -1.0, -1.0, -1.0])


def g_of(x):
    return x[0] * I2 + x[1] * Z[0] + x[2] * Z[1] + x[3] * Z[2]



def oriented_tangent_basis(x):
    """Orthonormal basis of T_x S^3, oriented CONSISTENTLY w.r.t. the ambient R^4.

    WHY this is not just QR: np.linalg.qr returns a basis whose orientation
    depends on sign conventions inside the factorisation, so comparing det
    between two independently-QR'd bases is meaningless -- it measures the
    two QR calls, not the map. The second failure of this file's own negative
    control was exactly that. Fix: pin the orientation by demanding
    det([normal | basis]) = +1, which ties every tangent basis to the SAME
    ambient orientation.
    """
    B = np.linalg.qr(np.column_stack([x, np.eye(4)[:, :3]]))[0][:, 1:]
    if np.linalg.det(np.column_stack([x, B])) < 0:
        B[:, -1] *= -1.0
    return B


def rand_unit(rng):
    v = rng.normal(size=4)
    return v / np.linalg.norm(v)


print("=" * 78)
print("Is iota(g) = g^-1 gauge, or parity?")
print("=" * 78)
rng = np.random.default_rng(20260810)

# --- STEP 1: iota in coordinates is (x0, -x) --------------------------------
print("\nSTEP 1 -- confirm iota(g) = g^-1 is (x0,x) -> (x0,-x) in coordinates")
ok = True
for _ in range(200):
    x = rand_unit(rng)
    ok &= bool(np.allclose(np.linalg.inv(g_of(x)), g_of(IOTA4 @ x)))
print(f"  g(x)^-1 = g(iota x) for 200 random unit x: {ok}")
results["step1_iota_is_coordinate_flip"] = ok

# --- STEP 2: orientation on the TANGENT space of S^3, at many points ---------
print("\nSTEP 2 -- orientation of the induced map on T_x S^3 (not just at a pole)")
dets, all_neg = [], True
for _ in range(200):
    x = rand_unit(rng)
    # orthonormal basis of T_x S^3 = x^perp
    B = oriented_tangent_basis(x)
    Bi = oriented_tangent_basis(IOTA4 @ x)
    M = Bi.T @ IOTA4 @ B          # iota expressed T_x S^3 -> T_{iota x} S^3
    d = float(np.linalg.det(M))
    dets.append(d)
    all_neg &= d < 0
print(f"  det of the induced tangent map: min {min(dets):+.3f}, max {max(dets):+.3f}")
print(f"  NEGATIVE at all 200 sampled points: {all_neg}")
print(f"  |det| = 1 everywhere (isometry): {bool(np.allclose(np.abs(dets), 1.0))}")
results["step2_tangent_det_all_negative"] = bool(all_neg)
results["step2_is_isometry"] = bool(np.allclose(np.abs(dets), 1.0))

# --- STEP 3: NEGATIVE CONTROL -- a genuine rotation must come out POSITIVE ---
print("\nSTEP 3 -- NEGATIVE CONTROL: left translation g -> a g is orientation-PRESERVING")
ctrl_pos = True
for _ in range(100):
    a = g_of(rand_unit(rng))
    x = rand_unit(rng)
    # left translation as a 4x4 real matrix on quaternion coordinates
    # WHY spelled out: the first version of this hard-coded the wrong entry for
    # x2 (Re g[1,0] = -x2 instead of Re g[0,1] = +x2), which flipped the
    # determinant sign and made this control FAIL. The control caught it. With
    # g = x0 I + x1(i s1) + x2(i s2) + x3(i s3) the matrix is
    #   [[x0 + i x3,  x2 + i x1],
    #    [-x2 + i x1, x0 - i x3]]
    # so x0 = Re g[0,0], x3 = Im g[0,0], x2 = Re g[0,1], x1 = Im g[0,1].
    L = np.zeros((4, 4))
    for j in range(4):
        prod = a @ g_of(np.eye(4)[j])
        L[:, j] = [prod[0, 0].real, prod[0, 1].imag, prod[0, 1].real, prod[0, 0].imag]
    B = oriented_tangent_basis(x)
    y = L @ x
    y = y / np.linalg.norm(y)
    Bi = oriented_tangent_basis(y)
    d = float(np.linalg.det(Bi.T @ L @ B))
    ctrl_pos &= d > 0
print(f"  left translation has POSITIVE tangent det at all 100 points: {ctrl_pos}")
print("  (if this came out negative the orientation machinery itself would be wrong)")
results["step3_control_left_translation_positive"] = bool(ctrl_pos)

# --- VERDICT -----------------------------------------------------------------
is_parity = all_neg and ctrl_pos and ok
verdict = "IOTA_IS_ORIENTATION_REVERSING__PARITY_NOT_GAUGE" if is_parity else "INCONCLUSIVE"
print("\n" + "=" * 78)
print(f"VERDICT: {verdict}")
print("=" * 78)
if is_parity:
    print("  iota is an orientation-REVERSING isometry of S^3.")
    print("  A gauge symmetry is connected to the identity, hence")
    print("  orientation-preserving. iota is NOT gauge -- it is parity-like.")
    print()
    print("  => C37/OB13's 'H1c may be ill-posed because iota is gauge' branch is DEAD.")
    print("  => C38 stands: (1,2) and (2,1) are genuinely distinct physical states,")
    print("     exchanged by PARITY -- which is exactly how SU(2)_L and SU(2)_R relate.")
    print("  => C37's 'the selector must be ODD in (t-1/2)' and 'iota is parity' are")
    print("     THE SAME STATEMENT: a parity-odd term is what breaks a parity pair.")
results["verdict"] = verdict
RESULTS_PATH.write_text(json.dumps(results, indent=2))
print(f"\nResults -> {RESULTS_PATH}")
