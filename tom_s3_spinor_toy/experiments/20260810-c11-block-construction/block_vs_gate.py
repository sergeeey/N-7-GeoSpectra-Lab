"""C11 reading (ii): build the block D^0 (+) D^1 and run it at PARENT_ACTION_GATE.

WHY THIS IS NOW THE ONLY LIVE CONSTRUCTION. C42 closed the one-operator reading:
no member of the Cartan-Schouten family has a 4-dim kernel, because the torsion
shift (t-1/2)*h_H is the SAME for every level while levels are separated by
2*sigma*(n+3/2). So "both t" must mean TWO operators, and OB2's own title becomes
the whole question: does the pair cohere as one spectral triple?

WHAT PREVIOUS ATTEMPTS USED, and why this differs. round110 built a toy
D_block = diag(0,0,3c/2,3c/2); C35 analysed D = 3*(T (x) I2). Both are toys, and
C35's decisive negative -- NO grading can exist, because spec(D) = {0,0,3,3} is
not symmetric under lambda -> -lambda -- is a statement about the TOY, not about
the real pair. This file uses the ACTUAL operators, via round67's closed form.

THE OBSERVATION THIS TESTS. With h_H = 3:

    D^t(n,sigma) = sigma*(n + 3/2) + (t - 1/2)*3

    t=0:  sigma=+1 -> n            sigma=-1 -> -n-3
    t=1:  sigma=+1 -> n+3          sigma=-1 -> -n

so   spec(D^0) = {0,1,2,...} u {-3,-4,...}
     spec(D^1) = {0,-1,-2,...} u {3,4,...}

These are MIRROR IMAGES. Each spectrum alone is asymmetric -- which is exactly
why C35 found no grading -- but their UNION may be symmetric. If it is, the
block construction supplies precisely the structure the single operator cannot,
and it does so for a reason C39 already identified: iota is orientation-
REVERSING, and an orientation-reversing map flips the sign of a Dirac operator.

PREDICTION, recorded before running:
  (a) spec(D^1) = -spec(D^0) exactly, as multisets including multiplicities;
  (b) therefore spec(D^0 (+) D^1) is symmetric and a grading EXISTS;
  (c) ker(D^0 (+) D^1) = 2 + 2 = 4, matching C38's Spin(4) spinor;
  (d) the SAME construction applied to a single D^0 must FAIL -- that is the
      negative control, and it is C35's result reproduced as a control.

WHAT THIS CANNOT SHOW, fixed in advance: a grading is ONE of the six
PARENT_ACTION_GATE fields. Finding it does not supply the algebra, the real
structure, the first-order condition, orientability, Poincare duality, or any
physical motivation for why two copies should exist. Those are reported as
NOT SUPPLIED rather than quietly omitted.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_block_vs_gate.json"
results: dict = {}

H_H = 3  # round67's calibration
N_MAX = 6  # truncation level; multiplicities grow as (n+1)(n+2)


def mult(n: int) -> int:
    """round116's own recorded eigenspace multiplicity, (n+1)(n+2)."""
    return (n + 1) * (n + 2)


def spectrum(t: float) -> list[float]:
    """Eigenvalues of D^t with multiplicity, truncated at N_MAX."""
    out: list[float] = []
    for n in range(N_MAX + 1):
        for sgn in (+1, -1):
            lam = sgn * (n + 1.5) + (t - 0.5) * H_H
            out.extend([lam] * mult(n))
    return out


print("=" * 78)
print("C11 reading (ii): the block D^0 (+) D^1 at PARENT_ACTION_GATE")
print("=" * 78)

# --- STEP 1: are the two spectra mirror images? ------------------------------
print("\nSTEP 1 -- is spec(D^1) = -spec(D^0), multiplicities included?")
s0, s1 = spectrum(0.0), spectrum(1.0)
c0, c1 = Counter(np.round(s0, 9)), Counter(np.round(s1, 9))
neg_c0 = Counter(np.round([-x for x in s0], 9))
mirror = neg_c0 == c1
print(f"  truncation N_MAX = {N_MAX}, dim per block = {len(s0)}")
print(
    f"  spec(D^0) low end: {sorted(set(np.round(s0, 6)))[:4]} ... {sorted(set(np.round(s0, 6)))[-3:]}"
)
print(
    f"  spec(D^1) low end: {sorted(set(np.round(s1, 6)))[:4]} ... {sorted(set(np.round(s1, 6)))[-3:]}"
)
print(f"  spec(D^1) == -spec(D^0) as multisets: {mirror}")
results["mirror_spectra"] = bool(mirror)
results["dim_per_block"] = len(s0)

# --- STEP 2: is the BLOCK spectrum symmetric? --------------------------------
print("\nSTEP 2 -- symmetry of the block spectrum (this is what C35 lacked)")
sb = s0 + s1
cb = Counter(np.round(sb, 9))
cb_neg = Counter(np.round([-x for x in sb], 9))
block_sym = cb == cb_neg
s0_sym = c0 == neg_c0
print(f"  spec(D^0) alone symmetric : {s0_sym}   <- C35's obstruction, reproduced")
print(f"  spec(D^0 (+) D^1) symmetric: {block_sym}")
results["single_block_symmetric"] = bool(s0_sym)
results["block_symmetric"] = bool(block_sym)

# --- STEP 3: construct the grading explicitly --------------------------------
print("\nSTEP 3 -- construct gamma explicitly and verify the axioms")
diag = np.array(sb)
dim = len(diag)
D = np.diag(diag)

# pair each block-0 index (eigenvalue lam) with a block-1 index (eigenvalue -lam)
by_val_block1: dict[float, list[int]] = {}
for j in range(len(s0), dim):
    by_val_block1.setdefault(round(diag[j], 9), []).append(j)

perm = {}
ok_match = True
for i in range(len(s0)):
    want = round(-diag[i], 9)
    bucket = by_val_block1.get(want)
    if not bucket:
        ok_match = False
        break
    j = bucket.pop()
    perm[i] = j
    perm[j] = i

if ok_match and len(perm) == dim:
    gamma = np.zeros((dim, dim))
    for i, j in perm.items():
        gamma[i, j] = 1.0
    g_sq = bool(np.allclose(gamma @ gamma, np.eye(dim)))
    g_herm = bool(np.allclose(gamma, gamma.T))
    anti = bool(np.allclose(gamma @ D + D @ gamma, 0.0))
    print(f"  every block-0 level found a partner: {ok_match}")
    print(f"  gamma^2 = I        : {g_sq}")
    print(f"  gamma = gamma^dag  : {g_herm}")
    print(f"  {{gamma, D_block}} = 0: {anti}")
    grading_exists = g_sq and g_herm and anti
else:
    print(f"  matching FAILED (ok_match={ok_match}, matched {len(perm)} of {dim})")
    grading_exists = False
print(f"\n  GRADING EXISTS for the block: {grading_exists}")
results["grading_exists"] = bool(grading_exists)

# --- STEP 4: the kernel ------------------------------------------------------
print("\nSTEP 4 -- kernel of the block")
ker = int(np.sum(np.isclose(diag, 0.0)))
ker0 = int(np.sum(np.isclose(np.array(s0), 0.0)))
ker1 = int(np.sum(np.isclose(np.array(s1), 0.0)))
print(f"  dim ker(D^0) = {ker0}, dim ker(D^1) = {ker1}, dim ker(block) = {ker}")
print(f"  matches C38's 4-dim Spin(4) spinor: {ker == 4}")
results["ker_block"] = ker
results["ker_matches_spin4"] = bool(ker == 4)

# --- STEP 5: NEGATIVE CONTROL -- the same construction on ONE operator -------
print("\nSTEP 5 -- NEGATIVE CONTROL: run the identical construction on D^0 alone")
print("  C35 says this must FAIL (asymmetric spectrum). If it 'succeeds' the")
print("  matching logic above is broken, not the physics.")
d0 = np.round(np.array(s0), 9)
avail: dict[float, list[int]] = {}
for i, v in enumerate(d0):
    avail.setdefault(v, []).append(i)
solo_ok = True
used = set()
for i, v in enumerate(d0):
    if i in used:
        continue
    bucket = [j for j in avail.get(round(-v, 9), []) if j not in used and j != i]
    if not bucket:
        solo_ok = False
        break
    j = bucket[0]
    used.update({i, j})
print(f"  single-operator grading constructible: {solo_ok}  (expect False)")
ctrl_ok = not solo_ok
print(f"  CONTROL PASSES: {ctrl_ok}")
results["single_operator_grading"] = bool(solo_ok)
results["control_passes"] = bool(ctrl_ok)

# --- STEP 6: PARENT_ACTION_GATE, all six fields, honestly --------------------
print("\nSTEP 6 -- PARENT_ACTION_GATE's six OB2 fields, stated as they stand")
gate = {
    "Algebra A": "NOT SUPPLIED — no algebra is specified for the block; round110's C(+)C was a toy and does not follow from the two-operator structure",
    "Hilbert space H": f"SUPPLIED — L2(S3,S) (+) L2(S3,S), truncated here to {dim} states; the two copies are the t=0 and t=1 sectors",
    "Dirac operator D": "SUPPLIED — D_block = D^0 (+) D^1, both from round67's closed form, self-adjoint by construction (real diagonal)",
    "Grading gamma": ("SUPPLIED (new) — exists, verified" if grading_exists else "NOT SUPPLIED"),
    "Real structure J": "NOT SUPPLIED — C35 found J only pointwise on the toy; nothing here extends it to the block",
    "Physical interpretation": "NOT SUPPLIED — nothing here motivates WHY two copies should coexist; that is the physics C11 asks for",
}
for k, v in gate.items():
    mark = "OK " if v.startswith("SUPPLIED") else "-- "
    print(f"  {mark}{k:24s} {v[:96]}")
results["parent_action_gate"] = gate
n_supplied = sum(1 for v in gate.values() if v.startswith("SUPPLIED"))
print(f"\n  fields supplied: {n_supplied}/6")
results["fields_supplied"] = n_supplied

# --- VERDICT -----------------------------------------------------------------
verdict_ok = mirror and block_sym and grading_exists and ker == 4 and ctrl_ok
verdict = (
    "BLOCK_SUPPLIES_THE_GRADING_C35_PROVED_IMPOSSIBLE_FOR_ONE_OPERATOR"
    if verdict_ok
    else "INCONCLUSIVE"
)
print("\n" + "=" * 78)
print(f"VERDICT: {verdict}")
print("=" * 78)
if verdict_ok:
    print("  The obstruction C35 found is REAL for a single operator and DISSOLVES")
    print("  for the pair: spec(D^1) = -spec(D^0) exactly, so the block spectrum is")
    print("  symmetric and an explicit grading exists.")
    print()
    print("  This is the first POSITIVE structural result for the two-operator")
    print("  reading -- and it is not a coincidence: C39 showed iota is")
    print("  orientation-REVERSING, and reversing orientation flips a Dirac")
    print("  operator's sign. The mirror spectra are that fact, spectrally.")
    print()
    print("  3 of 6 gate fields now supplied. The three still missing (algebra,")
    print("  real structure, physical interpretation) are the actual content of")
    print("  C11 and are NOT advanced here.")
results["verdict"] = verdict
RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
print(f"\nResults -> {RESULTS_PATH}")
