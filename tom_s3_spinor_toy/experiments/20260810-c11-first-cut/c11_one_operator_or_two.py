"""C11, first cut: can ONE operator host both t-sectors, or does it take two?

WHY THIS IS THE RIGHT FIRST QUESTION. C38 showed ker(D^0) = (1,2) and
ker(D^1) = (2,1) -- the two halves of one Spin(4) spinor. C39 showed they are
exchanged by PARITY, not gauge, so they are genuinely distinct physical states.
C27 and C25 both reduce to C11: "does the product ansatz with both t cohere?"

But "both t" is ambiguous, and the ambiguity is the whole question:

    reading (i)   ONE operator whose kernel is the full 4-dim (2,1)+(1,2)
    reading (ii)  TWO operators, one per sector, somehow coexisting

Reading (i) is a two-line algebra question against machinery this repo already
has. Reading (ii) is the hard spectral-triple question. **If (i) is impossible,
C11 is forced onto (ii) and its scope narrows to something nameable.** That is
worth knowing before any harder work starts.

METHOD. Two independent sub-questions, neither requiring new theory:

  Q1  Is there ANY t with dim ker(D^t) = 4?
      E2/round67 established the closed-form family
          D^t(n,sigma) = sigma*(n + 3/2) + (t - 1/2)*h_H,   h_H = 3
      so this is solvable exactly, not by scanning.

  Q2  Are the two kernels even subspaces of the SAME space of sections?
      They are written in different frames (left- vs right-invariant), so this
      is not automatic. Express both in one trivialization and compute
      dim(V0 + V1) and dim(V0 ∩ V1) numerically.

WHAT THIS CANNOT SHOW, fixed before running: nothing here decides whether two
coexisting operators make sense as a spectral triple. That is C11 proper. This
only settles whether the ONE-operator reading is available, and whether the two
kernels live in a common space at all.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c11_first_cut.json"
results: dict = {}

print("=" * 78)
print("C11 first cut -- one operator with a 4-dim kernel, or necessarily two?")
print("=" * 78)

# =============================================================================
# Q1 -- is there ANY t with a 4-dimensional kernel?
# =============================================================================
print("\nQ1 -- solve the closed-form family exactly (no scanning)")
t = sp.Symbol("t", real=True)
h_H = sp.Rational(3, 1)  # round67's own calibration: h_H = (3/2)/(1/2) = 3


def eig(n: int, sigma: int):
    """round67's family, rho3 = 1."""
    return sigma * (n + sp.Rational(3, 2)) + (t - sp.Rational(1, 2)) * h_H


print(f"  h_H = {h_H} (round67's calibration, reproduced here)")
crossings = {}
for n in range(4):
    for sgn in (+1, -1):
        sol = sp.solve(sp.Eq(eig(n, sgn), 0), t)
        if sol:
            crossings[f"n={n},sigma={sgn:+d}"] = sp.nsimplify(sol[0])
for k, v in sorted(crossings.items(), key=lambda kv: float(kv[1])):
    print(f"    {k:16s} vanishes at t = {v}")
results["crossings"] = {k: str(v) for k, v in crossings.items()}

# a 4-dim kernel needs TWO distinct (n,sigma) levels vanishing at the SAME t
from collections import defaultdict

by_t = defaultdict(list)
for k, v in crossings.items():
    by_t[sp.nsimplify(v)].append(k)
coincident = {str(k): v for k, v in by_t.items() if len(v) > 1}
print(f"\n  values of t where TWO levels vanish simultaneously: {coincident or 'NONE'}")

# the two sectors of interest, explicitly
t0_levels = [k for k, v in crossings.items() if v == 0]
t1_levels = [k for k, v in crossings.items() if v == 1]
print(f"  t=0 kernel comes from: {t0_levels}")
print(f"  t=1 kernel comes from: {t1_levels}")
print("  Each level is a 2-dim SU(2) doublet (E12), so each t gives dim ker = 2.")
one_operator_possible = bool(coincident)
print(f"\n  ONE operator with dim ker = 4 exists: {one_operator_possible}")
results["t0_levels"] = t0_levels
results["t1_levels"] = t1_levels
results["coincident_t"] = coincident
results["one_operator_4dim_kernel_possible"] = one_operator_possible

# =============================================================================
# Q2 -- do the two kernels live in a COMMON space of sections?
# =============================================================================
print("\nQ2 -- express both kernels in ONE trivialization and compare")
print("  V0 = {psi(g) = v}        (t=0, constant)")
print("  V1 = {psi(g) = g^-1 v}   (t=1, gbar-twisted)")
print("  Sample S^3 at many points, stack the section values, and read off ranks.")

I2 = np.eye(2, dtype=complex)
Zc = [
    1j * np.array([[0, 1], [1, 0]], dtype=complex),
    1j * np.array([[0, -1j], [1j, 0]], dtype=complex),
    1j * np.array([[1, 0], [0, -1]], dtype=complex),
]


def g_of(x):
    return x[0] * I2 + x[1] * Zc[0] + x[2] * Zc[1] + x[3] * Zc[2]


rng = np.random.default_rng(20260810)
pts = []
for _ in range(60):
    v = rng.normal(size=4)
    pts.append(v / np.linalg.norm(v))

basis_e = [np.array([1, 0], dtype=complex), np.array([0, 1], dtype=complex)]


def sample(section) -> np.ndarray:
    """Flatten a section's values over the sample points into one long vector."""
    return np.concatenate([section(g_of(x)) for x in pts])


cols_V0 = [sample(lambda g, v=e: v) for e in basis_e]
cols_V1 = [sample(lambda g, v=e: np.linalg.inv(g) @ v) for e in basis_e]
M0 = np.column_stack(cols_V0)
M1 = np.column_stack(cols_V1)
Mboth = np.column_stack(cols_V0 + cols_V1)

r0 = np.linalg.matrix_rank(M0, tol=1e-9)
r1 = np.linalg.matrix_rank(M1, tol=1e-9)
rb = np.linalg.matrix_rank(Mboth, tol=1e-9)
inter = r0 + r1 - rb
print(f"  dim V0 = {r0}, dim V1 = {r1}, dim(V0 + V1) = {rb}, dim(V0 n V1) = {inter}")
results["dim_V0"] = int(r0)
results["dim_V1"] = int(r1)
results["dim_span"] = int(rb)
results["dim_intersection"] = int(inter)

# =============================================================================
# NEGATIVE CONTROL
# =============================================================================
print("\nNEGATIVE CONTROL -- the method must report a NON-trivial intersection")
print("  when one genuinely exists. Feed it V0 against itself-plus-a-shared-vector.")
shared = [sample(lambda g, v=basis_e[0]: v)]
Mctrl = np.column_stack(cols_V0 + shared)
r_ctrl = np.linalg.matrix_rank(Mctrl, tol=1e-9)
inter_ctrl = r0 + 1 - r_ctrl
ctrl_ok = inter_ctrl == 1
print(f"  V0 vs span{{one of its own vectors}}: intersection = {inter_ctrl} (expect 1)")
print(f"  CONTROL PASSES: {ctrl_ok}")
results["control_intersection"] = int(inter_ctrl)
results["control_passes"] = bool(ctrl_ok)

# =============================================================================
verdict_ok = (not one_operator_possible) and rb == 4 and inter == 0 and ctrl_ok
verdict = "C11_FORCED_ONTO_THE_TWO_OPERATOR_READING" if verdict_ok else "INCONCLUSIVE"
print("\n" + "=" * 78)
print(f"VERDICT: {verdict}")
print("=" * 78)
if verdict_ok:
    print("  Q1: NO single t in the Cartan-Schouten family has a 4-dim kernel.")
    print("      t=0 kills (n=0, sigma=+1); t=1 kills (n=0, sigma=-1); the shift")
    print("      (t-1/2)*h_H is the SAME for both, so one t cannot kill both.")
    print("  Q2: the two kernels DO live in a common space of sections, are")
    print("      linearly independent (intersection 0) and span exactly 4.")
    print()
    print("  => 'both t' CANNOT mean one operator with a bigger kernel.")
    print("     C11 is forced onto the two-operator reading, and its scope")
    print("     narrows to: can two D's coexist as one spectral triple?")
results["verdict"] = verdict
RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
print(f"\nResults -> {RESULTS_PATH}")
