r"""
C152 STEP 3 -- the negative control. Step 2 showed each of the 6 directions
contributes |amplitude| = 0.5 and the sum cancels. This file asks WHAT the
cancellation actually rests on, by destroying candidate ingredients one at a
time and seeing which destruction revives the block.

PRE-COMMITTED (PREREGISTRATION.md):
  P1  representation-forced -> zero SURVIVES generic coefficient perturbation
  P2  geometric            -> zero is DESTROYED by generic perturbation

CONTROLS, from least to most destructive
  A  random element of the T^2-EQUIVARIANT family (C73b's 6-dim Hom_T2)
     -- regression of C151's own result; equivariance kept, geometry gone
  B  perturb a SINGLE direction's connection (i=1 only), leaving the other
     five at Levi-Civita -- breaks the symmetry AMONG the six amplitudes
     without leaving antisymmetric matrices
  C  all six replaced by independent random ANTISYMMETRIC matrices
     -- equivariance destroyed as well; only the tensorial shape survives
  D  Levi-Civita, but with ONE direction rescaled by a free factor s
     -- the sharpest form: if the cancellation is a coefficient balance,
        it must fail for every s != 1

Run:  python c152_step3_control.py
"""

import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
S2A_PATH = HERE.parent / "20260904-c151-stage0-su3t2-scoping" / "c151_stage2_construct.py"
C73B_PATH = (
    HERE.parent
    / "20260811-c73b-torsion-family-genuine-deformation-and-twist-control"
    / "c73b_torsion_family.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


S2A = load_module("c151_stage2_construct", S2A_PATH)
C73B = load_module("c73b_torsion_family", C73B_PATH)
E, dom, tgt = S2A.E, S2A.dom, S2A.tgt
LAM = {i: S2A.NOMIZU_LC[i].astype(complex) for i in range(1, 7)}
SPIN_VS_VEC = -1  # re-derived and gated in Step 2, across 24 generator/index pairs


def term2_block(conn: dict[int, np.ndarray]) -> np.ndarray:
    """The 3x3 invariant-sector block of Sum_i E_i (x) sign*conn[i]."""
    D = np.zeros((48, 48), dtype=complex)
    for i in range(1, 7):
        D += np.kron(E[i], SPIN_VS_VEC * conn[i])
    return tgt.conj().T @ D @ dom


def report(tag: str, conn: dict[int, np.ndarray]) -> float:
    v = float(np.max(np.abs(term2_block(conn))))
    print(f"  {tag:<58} max|block| = {v:.6e}   {'ZERO' if v < 1e-10 else 'NONZERO'}")
    return v


# ---------------------------------------------------------------------------
print("=" * 78)
print("STRUCTURE OF THE CANCELLATION (what exactly is summing to zero)")
print("=" * 78)
per_i = {i: tgt.conj().T @ np.kron(E[i], SPIN_VS_VEC * LAM[i]) @ dom for i in range(1, 7)}
live = max(((r, c) for r in range(3) for c in range(3)),
           key=lambda rc: max(abs(per_i[i][rc]) for i in range(1, 7)))
print(f"  entry {live} of the block (the one with live per-direction terms):")
for i in range(1, 7):
    z = per_i[i][live]
    print(f"    i={i}:  {z.real:+.6f} {z.imag:+.6f}j   |z| = {abs(z):.6f}")
tot = sum(per_i[i][live] for i in range(1, 7))
print(f"    SUM  :  {tot.real:+.3e} {tot.imag:+.3e}j")

print()
print("=" * 78)
print("CONTROLS")
print("=" * 78)
base = report("LEVI-CIVITA (baseline, C151's result)", LAM)

rng = np.random.default_rng(20260904)
n_pairs = len(C73B.PAIRS)


def row_to_6x6(row: np.ndarray) -> np.ndarray:
    M = np.zeros((6, 6), dtype=complex)
    for idx, (a, b) in enumerate(C73B.PAIRS):
        M[a, b] += row[idx]
        M[b, a] -= row[idx]
    return M


family = C73B.equivariant_torsion_basis(S2A.T2_M)
assert family.shape[1] == 6, f"family dim drifted from C151's 6: {family.shape[1]}"

# --- Control A: random EQUIVARIANT connection --------------------------------
a_vals = []
for trial in range(5):
    vec = family @ rng.normal(size=6)
    T = vec.reshape(6, n_pairs)
    a_vals.append(report(f"A{trial}  random T^2-EQUIVARIANT family element",
                         {i + 1: row_to_6x6(T[i]) for i in range(6)}))

# --- REGRESSION against C151's own c_of (Term1+Term2 together) ----------------
print()
print("  REGRESSION: C151's own FULL coefficient (Term1+Term2) on the same draws")

for trial in range(5):
    vec = family @ rng.normal(size=6)
    T = vec.reshape(6, n_pairs)
    conn = {i + 1: row_to_6x6(T[i]) for i in range(6)}
    D = np.zeros((48, 48), dtype=complex)
    for i in range(1, 7):
        D += np.kron(E[i] @ S2A.spin_lift_np(conn[i]), np.eye(6))
        D += np.kron(E[i], SPIN_VS_VEC * conn[i])
    full = float(np.max(np.abs(tgt.conj().T @ D @ dom)))
    t1o = float(np.max(np.abs(tgt.conj().T @ sum(
        np.kron(E[i] @ S2A.spin_lift_np(conn[i]), np.eye(6)) for i in range(1, 7)) @ dom)))
    t2o = float(np.max(np.abs(term2_block(conn))))
    print(f"    draw {trial}: |Term1| = {t1o:.3e}   |Term2| = {t2o:.3e}   "
          f"|FULL| = {full:.3e}  {'C151-consistent' if full < 1e-10 else 'CONTRADICTS C151'}")

# --- Control B: perturb ONE direction ----------------------------------------
connB = dict(LAM)
pert = rng.normal(size=(6, 6))
connB[1] = LAM[1] + (pert - pert.T)
report("B   Levi-Civita with direction i=1 perturbed (antisym)", connB)

# --- Control C: all six random, NON-equivariant -------------------------------
c_vals = []
for trial in range(5):
    connC = {}
    for i in range(1, 7):
        r = rng.normal(size=(6, 6))
        connC[i] = (r - r.T).astype(complex)
    c_vals.append(report(f"C{trial}  all six random ANTISYMMETRIC (non-equivariant)", connC))

# --- Control D: Levi-Civita with one direction rescaled -----------------------
print()
for s in (0.5, 2.0, -1.0, 1.0):
    connD = dict(LAM)
    connD[3] = s * LAM[3]
    report(f"D   Levi-Civita, direction i=3 rescaled by s = {s:+.1f}", connD)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("VERDICT: P1 or P2?")
print("=" * 78)
equivariant_all_zero = all(v < 1e-10 for v in a_vals)
generic_all_zero = all(v < 1e-10 for v in c_vals)
print(f"  zero survives EQUIVARIANT perturbation (5 draws) : {equivariant_all_zero}")
print(f"  zero survives GENERIC   perturbation (5 draws) : {generic_all_zero}")
print()
if equivariant_all_zero and not generic_all_zero:
    print("  -> NEITHER P1 nor P2 in their pure forms. The discriminator is not")
    print("     'geometry vs representation' but EQUIVARIANCE:")
    print("       * ANY T^2-equivariant connection gives zero (not just LC/NK),")
    print("         so the zero does NOT use the special nearly-Kahler geometry;")
    print("       * a NON-equivariant connection of the same tensorial shape")
    print("         gives NONZERO, so the zero is not an identity of E_i and the")
    print("         invariant sectors alone either.")
    print("     The mechanism is: equivariance of the connection, combined with")
    print("     the weight structure, forces the six per-direction amplitudes")
    print("     into a configuration that always sums to zero.")
elif equivariant_all_zero and generic_all_zero:
    print("  -> P1. Zero survives everything; identity of E_i + sectors alone.")
elif not equivariant_all_zero:
    print("  -> P2 in its strongest form: even equivariant perturbation breaks it,")
    print("     contradicting C151's own finding of c == 0 on the whole family.")
    print("     THIS WOULD BE A CONTRADICTION -- stop and re-check before believing.")
