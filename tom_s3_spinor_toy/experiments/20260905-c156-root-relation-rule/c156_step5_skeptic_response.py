r"""
C156 STEP 5 -- tool-verification of the context-blind skeptic report.

The skeptic again had NO code execution and said so. Under
audit-verification-gate.md its verdicts are [HYPOTHESIS] until re-run here.
Two of its points are decisive and testable:

  V1 (its Attack 2, the killer): is surjectivity onto a SMALL target from a
     LARGE source simply generic?  Null model: replace the real construction
     with random linear maps V -> Sigma^T_opp of the SAME dimensions and see
     how often they surject.  If they always do, HYPOTHESIS S has no content.

  V2 (its Attack 4, a structural insight this round did NOT have): the even
     chirality split of Sigma^T is FORCED when N (number of positive roots)
     is ODD, because eps -> -eps maps solutions of sum eps_k beta_k = 0 to
     solutions and flips the +-count from k to N-k, changing parity iff N is
     odd.  For N EVEN the split is NOT forced and the observed 2+2 on G_2 and
     A_2xA_2 would be luck.  Verified here by enumerating the sign patterns.
"""

import importlib.util
import random
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent


def load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


G = load("c156g", "c156_general.py")

CASES = {
    "A_2  (N=3, odd)": [(-2, 1), (1, 1), (1, -2)],
    "G_2  (N=6, even)": [(2 * c1 - c2, -3 * c1 + 2 * c2) for (c1, c2) in
                          [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)]],
    "A_2xA_2 (N=6, even)": [(-2, 1, 0, 0), (1, 1, 0, 0), (1, -2, 0, 0),
                            (0, 0, -2, 1), (0, 0, 1, 1), (0, 0, 1, -2)],
}

print("=" * 78)
print("V2  is the EVEN chirality split forced by N parity?  (skeptic Attack 4)")
print("=" * 78)
for name, W in CASES.items():
    N = len(W)
    r = len(W[0])
    sols = []
    for mask in range(1 << N):
        eps = [1 if (mask >> t) & 1 else -1 for t in range(N)]
        tot = [sum(eps[k] * W[k][j] for k in range(N)) for j in range(r)]
        if all(x == 0 for x in tot):
            sols.append(eps)
    # chirality is the parity of the number of +1 entries
    par = {}
    for eps in sols:
        p = sum(1 for e in eps if e == 1) % 2
        par[p] = par.get(p, 0) + 1
    forced = N % 2 == 1
    print(f"  {name}: solutions = {len(sols)}, parity split = {par}, "
          f"N odd (=> forced by eps<->-eps) : {forced}")
    for eps in sols:
        neg = [-e for e in eps]
        same_parity = (sum(1 for e in eps if e == 1) % 2) == (
            sum(1 for e in neg if e == 1) % 2)
        print(f"     eps={tuple(eps)}  parity={sum(1 for e in eps if e == 1) % 2}"
              f"  -eps has SAME parity: {same_parity}")
print()
print("  => skeptic's parity argument is CONFIRMED if 'same parity' is True")
print("     exactly for the N-even cases and False for the N-odd ones.")

print()
print("=" * 78)
print("V1  NULL MODEL: is surjectivity onto the small target generic?")
print("     (skeptic Attack 2 -- the one it called the killer)")
print("=" * 78)
random.seed(20260905)
for dim_V, dim_T, label in ((6, 2, "A_2 shape"), (30, 4, "G_2 shape"), (12, 4, "A_2xA_2 shape")):
    surj = 0
    trials = 200
    for _ in range(trials):
        Mr = sp.Matrix(dim_T, dim_V, lambda i, j: random.randint(-3, 3))
        if Mr.rank() == dim_T:
            surj += 1
    print(f"  {label}: random {dim_T}x{dim_V} integer maps surjective in "
          f"{surj}/{trials} trials  ({100 * surj / trials:.1f}%)")
print()
print("  => if these are ~100%, then 'M is surjective onto Sigma^T_opp' is what")
print("     ANY map of these dimensions does, and HYPOTHESIS S's remaining")
print("     content (beyond the FORCED containment) is nil.")
