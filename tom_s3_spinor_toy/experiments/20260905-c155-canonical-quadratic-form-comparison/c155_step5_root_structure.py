r"""
C155 STEP 5 -- is the sign pattern (+,-,+) explained by the ROOT SYSTEM?

Steps 4/4b established: the three root planes A,B,C map onto ONE common real
2-plane in Sigma, with per-plane signs (+,-,+):  M(A) = -M(B) = M(C).

That pattern is either (i) an accident of basis ordering, or (ii) a shadow of
the A_2 root relation  alpha_3 = alpha_1 + alpha_2.  Distinguishing them
matters: under (ii) the rank/kernel result would generalise to other flag
manifolds with a PREDICTION, under (i) it is one-space bookkeeping.

Method: read the actual T^2 weights off the Cartan generators plane by plane
(no guessing which block is which root), then test whether the observed
coefficient pattern is a function of those weights.

FALSIFIABLE: if the signs do NOT line up with the weight data, hypothesis (ii)
is dead and must be reported as such.
"""
import importlib.util
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
EXP = HERE.parent


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, EXP / rel)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


S2 = load("c153_step2", "20260904-c153-nk-linearity-structural-derivation/c153_step2_exact_rational_verification.py")

print("=" * 78)
print("STEP 5  weights of the three planes, read off the Cartan generators")
print("=" * 78)

# T2_M[0], T2_M[1] act on m (6x6, block-antisymmetric). On plane k = {2k,2k+1}
# the action is  [[0,-w],[w,0]]  and w is that plane's value of the root.
PLANES = {"A": (0, 1), "B": (2, 3), "C": (4, 5)}
weights = {}
for name, (p, q) in PLANES.items():
    w = []
    for gen_idx, G in enumerate(S2.T2_M):
        wq = sp.simplify(G[q, p])
        # confirm the block really is a pure rotation on this plane
        assert sp.simplify(G[p, q] + wq) == 0, "plane is not a rotation block"
        w.append(sp.nsimplify(wq))
    weights[name] = tuple(w)
    print(f"  plane {name} (m-indices {p},{q}) : weight under the 2 Cartan gens = {tuple(w)}")

wa, wb, wc = weights["A"], weights["B"], weights["C"]
print()
print("  linear relations among the three weights:")
for combo, label in (
    ((1, 1, -1), "wA + wB - wC"),
    ((1, -1, -1), "wA - wB - wC"),
    ((1, -1, 1), "wA - wB + wC"),
    ((1, 1, 1), "wA + wB + wC"),
):
    s = tuple(
        sp.simplify(combo[0] * wa[t] + combo[1] * wb[t] + combo[2] * wc[t]) for t in range(2)
    )
    print(f"    {label:>14} = {s}   vanishes: {all(x == 0 for x in s)}")

print()
print("=" * 78)
print("  OBSERVED mu-map pattern (Steps 4/4b): M(A) = -M(B) = M(C)")
print("  i.e. coefficient vector (1, -1, 1) annihilates nothing by itself;")
print("  the KERNEL relations found were  A+B  and  -A+C .")
print("=" * 78)
print("  So the mu-map coefficients per plane are proportional to (1, -1, 1).")
print("  Hypothesis (ii) predicts this equals the pattern of the weight relation.")
match = None
for combo, label in (
    ((1, 1, -1), "wA + wB - wC"),
    ((1, -1, 1), "wA - wB + wC"),
    ((1, -1, -1), "wA - wB - wC"),
    ((1, 1, 1), "wA + wB + wC"),
):
    s = tuple(
        sp.simplify(combo[0] * wa[t] + combo[1] * wb[t] + combo[2] * wc[t]) for t in range(2)
    )
    if all(x == 0 for x in s):
        match = (combo, label)
print(f"  vanishing weight relation found: {match}")
if match and match[0] == (1, -1, 1):
    print("  MATCH: the mu coefficient pattern (1,-1,1) IS the root relation.")
elif match:
    print(f"  MISMATCH: root relation is {match[1]} but mu pattern is (1,-1,1).")
    print("  Hypothesis (ii) as stated is FALSIFIED -- report the mismatch,")
    print("  do not re-label planes until it fits.")
else:
    print("  no vanishing relation among the weights at all -- (ii) dead.")
