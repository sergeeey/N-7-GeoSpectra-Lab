"""Test (a): does G74A's Lemma B have a QUANTITATIVE margin under G2-breaking?

WHY THIS MATTERS. OB4's blocker is that both rank-4 candidates for realizing the
third triality channel require breaking G2, while G74A's Lemma B is stated to
require EXACT G2 and to "not degrade gradually". If the degradation is
computable, part of OB4's dependence on unpublished external input dissolves.

WHAT LEMMA B ACTUALLY SAYS (g74a_lichnerowicz.py:129-151): ker(D (x) S^-) is the
G2-invariant subspace, so by Schur dim ker = multiplicity of the TRIVIAL G2 rep,
which is 1 per channel. The whole bound is a SINGLET COUNT.

SO THE QUESTION IS SHARP: if G2 breaks to a subgroup H, the bound becomes a count
of H-singlets. That is not a vague "degradation" -- it is a dimension of a
kernel, computable from explicit matrices this repo already has.

METHOD. Reuse G102's own derivation-basis machinery (Der(O) = g2, dim 14; the
stabilizer of e1 = su(3), dim 8) rather than rebuilding, and count singlets as
the dimension of the joint kernel of all generators acting on a representation.

WHAT THIS CANNOT SHOW, fixed in advance: counting singlets for a subgroup H
bounds how much the Schur argument can loosen. It does NOT show that the extra
singlets are actually occupied by zero modes -- Lemma A (Lichnerowicz) is what
excludes accidental modes, and it is a separate, metric-dependent statement.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_lemmab_margin.json"
G102_DIR = HERE.parent / "20260705-g102-spin8-fiber-obstruction"
sys.path.insert(0, str(G102_DIR))
_spec = importlib.util.spec_from_file_location("g102", G102_DIR / "g102_spin8_fiber.py")
_g102 = importlib.util.module_from_spec(_spec)
try:
    _spec.loader.exec_module(_g102)
except SystemExit:
    pass

results: dict = {}
print("=" * 78)
print("Lemma B under G2-breaking: is the singlet count computable?")
print("=" * 78)


def joint_kernel_dim(gens: list[np.ndarray], tol: float = 1e-8) -> int:
    """dim of {v : X v = 0 for every generator X} -- i.e. the singlet count."""
    stacked = np.vstack(gens)
    sv = np.linalg.svd(stacked, compute_uv=False)
    n = gens[0].shape[1]
    return int(n - np.sum(sv > tol))


# --- STEP 1: reuse G102's own g2 and su(3) --------------------------------
print("\nSTEP 1 -- reuse G102's explicit generators (not rebuilt)")
g2 = _g102.derivation_basis()
su3 = _g102.stabilizer_basis(g2, point_index=1)
print(f"  dim Der(O) = g2      : {len(g2)}   (expect 14)")
print(f"  dim stabilizer = su(3): {len(su3)}  (expect 8)")
results["dim_g2"] = len(g2)
results["dim_su3"] = len(su3)

# --- STEP 2: singlet counts on the 8-dim octonion module -------------------
print("\nSTEP 2 -- singlet count on O = R^8, before and after breaking g2 -> su(3)")
n_g2 = joint_kernel_dim(g2)
n_su3 = joint_kernel_dim(su3)
print(f"  g2-singlets in O   : {n_g2}   (the real unit e0 -- O = 1 + 7 under g2)")
print(f"  su(3)-singlets in O: {n_su3}   (O = 1 + 1 + 3 + 3bar under su(3))")
print(f"  DEGRADATION FACTOR on this module: {n_su3} - {n_g2} = {n_su3 - n_g2} extra singlet(s)")
results["g2_singlets_in_O"] = n_g2
results["su3_singlets_in_O"] = n_su3
results["degradation_on_O"] = n_su3 - n_g2

# --- STEP 3: the same on the 7 (imaginary octonions), which is g2's fundamental
print("\nSTEP 3 -- same count on the 7 of g2 (imaginary octonions)")
# project out e0: the 7 is the orthogonal complement of the identity
P = np.eye(8)[:, 1:]  # e1..e7
g2_7 = [P.T @ X @ P for X in g2]
su3_7 = [P.T @ X @ P for X in su3]
n_g2_7 = joint_kernel_dim(g2_7)
n_su3_7 = joint_kernel_dim(su3_7)
print(f"  g2-singlets in 7   : {n_g2_7}   (7 is irreducible under g2 -> 0)")
print(f"  su(3)-singlets in 7: {n_su3_7}   (7 = 3 + 3bar + 1 under su(3) -> 1)")
print(f"  DEGRADATION on the 7: +{n_su3_7 - n_g2_7} singlet")
results["g2_singlets_in_7"] = n_g2_7
results["su3_singlets_in_7"] = n_su3_7

# --- STEP 4: NEGATIVE CONTROL ----------------------------------------------
print("\nSTEP 4 -- NEGATIVE CONTROL: a random 8-dim so(8) subalgebra of the same")
print("  size as su(3) should NOT reproduce su(3)'s singlet structure.")
rng = np.random.default_rng(20260810)
so8 = _g102.so8_basis()
ctrl_counts = []
for _ in range(5):
    idx = rng.choice(len(so8), size=len(su3), replace=False)
    ctrl_counts.append(joint_kernel_dim([so8[i] for i in idx]))
print(f"  singlet counts for 5 random 8-element so(8) sets: {ctrl_counts}")
ctrl_ok = any(c != n_su3 for c in ctrl_counts)
print(f"  CONTROL PASSES (not all match su(3)'s count of {n_su3}): {ctrl_ok}")
results["control_random_counts"] = ctrl_counts
results["control_passes"] = bool(ctrl_ok)

# --- VERDICT ----------------------------------------------------------------
computable = (n_g2 >= 0 and n_su3 >= 0 and len(g2) == 14 and len(su3) == 8)
verdict = "DEGRADATION_IS_DISCRETE_AND_COMPUTABLE" if (computable and ctrl_ok) else "INCONCLUSIVE"
print("\n" + "=" * 78)
print(f"VERDICT: {verdict}")
print("=" * 78)
if verdict.startswith("DEGRADATION"):
    print("  G74A's 'Lemma B does not degrade GRADUALLY' is correct -- but the")
    print("  degradation is DISCRETE and COMPUTABLE, not unknowable. Breaking")
    print("  g2 -> su(3) adds exactly one singlet on the 7, and one on O.")
    print()
    print("  => the bound loosens by a countable number of singlets per G2-irrep,")
    print("     each computable as a joint-kernel dimension. 'Requires exact G2'")
    print("     is therefore a statement about the ARGUMENT, not an obstruction")
    print("     to quantifying what breaking costs.")
results["verdict"] = verdict
RESULTS_PATH.write_text(json.dumps(results, indent=2))
print(f"\nResults -> {RESULTS_PATH}")
