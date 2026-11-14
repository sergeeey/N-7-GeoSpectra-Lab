r"""
C157 STEP 2 -- exhaustive census of Z(Phi) = {S subset Phi+ : sum(S) = rho},
split by parity(|S|), via dynamic programming over partial sums (a dict keyed
by the running vector), NOT 2^N brute force.

For each beta_k, either it is IN S (contributes +beta_k, flips parity) or NOT
(contributes 0). So this is a signed subset-sum DP: states are integer/rational
vectors, values are (even_count, odd_count) reachable with that partial sum.

Regression (P4): must reproduce the actual Clifford-algebra chirality splits
already computed in C156: A_2 -> 1+1, G_2 -> 2+2, A_2xA_2 -> 2+2.

Run:  python c157_step2_census.py
"""

import importlib.util
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("c157s1", HERE / "c157_step1_root_systems.py")
S1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(S1)


class StateBlowup(Exception):
    """Raised when the DP state space exceeds max_states -- a substrate
    limit, NOT evidence about the census. Random vector sets (c157_step3's
    null model) have no algebraic cancellation and can blow up combinatorially
    where a real root system collapses; this must be reported as
    BLOCKED-INFRASTRUCTURE, never silently hung or misread as a result."""


def census(roots, target, max_states=None):
    """DP: dp[v] = (n_even, n_odd) = counts of subsets with sum v, by parity
    of subset size. Vectors used as dict keys via sp.Rational tuples (exact).

    CORRECTION (self-caught, recorded honestly): a first pass at rewriting
    this function suspected a double-counting bug in the `new = dict(dp)`
    initialisation and "fixed" it with an explicit two-branch accumulation.
    Re-running the full P1/P4 suite gave IDENTICAL numbers to the byte before
    the "fix" (same |Z|, same even/odd split, on every one of the 18 systems,
    including E_6's 13697920). The two formulations are mathematically
    equivalent -- `dict(dp)` already supplies exactly the "beta excluded"
    contribution, the following loop adds only the "beta included" one, so
    there is no double count. There was no bug. Recorded here rather than
    silently reverted, per this project's own policy of not fabricating a
    fix that did not do anything -- the version kept below is the rewrite,
    since it is equally correct and slightly more explicit, not because it
    corrected anything.
    """
    dp = {tuple(sp.Rational(0) for _ in roots[0]): (1, 0)}
    for beta in roots:
        beta = tuple(sp.Rational(x) for x in beta)
        new = {}
        for v, (ne, no) in dp.items():
            # excluded: state v persists unchanged
            cur = new.get(v, (0, 0))
            new[v] = (cur[0] + ne, cur[1] + no)
            # included: state v+beta, parity flips
            v2 = tuple(v[t] + beta[t] for t in range(len(v)))
            cur2 = new.get(v2, (0, 0))
            new[v2] = (cur2[0] + no, cur2[1] + ne)
        dp = new
        if max_states is not None and len(dp) > max_states:
            raise StateBlowup(len(dp))
    return dp.get(tuple(target), (0, 0))


def run(name, roots, dim):
    N = len(roots)
    rho = S1.rho_of(roots)
    ne, no = census(roots, rho)
    total = ne + no
    print(
        f"  {name:6s}: N={N:3d}  |Z|={total:4d}  even(+)={ne:4d}  odd(-)={no:4d}  "
        f"balanced={ne == no}"
    )
    return {"name": name, "N": N, "total": total, "even": ne, "odd": no, "balanced": ne == no}


if __name__ == "__main__":
    print("=" * 78)
    print("P4  REGRESSION -- must reproduce C156's Clifford-algebra chirality splits")
    print("=" * 78)
    a2, _ = S1.SYSTEMS["A_2"]
    r = run("A_2", a2, 2)
    assert (r["even"], r["odd"]) in ((1, 1),), f"A_2 regression FAILED: got {r}"
    g2, _ = S1.SYSTEMS["G_2"]
    r = run("G_2", g2, 2)
    assert (r["even"], r["odd"]) == (2, 2), f"G_2 regression FAILED: got {r}"
    # A_2 x A_2: two independent A_2 copies in orthogonal coordinate blocks
    a2a2 = [(x, y, sp.Integer(0), sp.Integer(0)) for (x, y, _z) in a2] + [
        (sp.Integer(0), sp.Integer(0), x, y) for (x, y, _z) in a2
    ]
    r = run("A_2xA_2", a2a2, 4)
    assert (r["even"], r["odd"]) == (2, 2), f"A_2xA_2 regression FAILED: got {r}"
    print("  P4 REGRESSION PASSED: reformulation reproduces C156's actual numbers.")

    print()
    print("=" * 78)
    print("P1  FULL CENSUS -- every root system in scope")
    print("=" * 78)
    results = []
    for name, (roots, dim) in S1.SYSTEMS.items():
        results.append(run(name, roots, dim))

    print()
    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    all_balanced = all(r["balanced"] for r in results)
    has_spinors = [r for r in results if r["total"] > 0]
    print(f"  systems with |Z|>0 (admit invariant spinors): {[r['name'] for r in has_spinors]}")
    print(f"  ALL BALANCED (even==odd) across every system, N odd or even: {all_balanced}")
    n_even_with_spinors = [r for r in has_spinors if r["N"] % 2 == 0]
    print(
        f"  N-EVEN systems with spinors (the genuinely open cases before this "
        f"round): {[r['name'] for r in n_even_with_spinors]}"
    )
    print(f"  P1 CONFIRMED: {all_balanced}")
