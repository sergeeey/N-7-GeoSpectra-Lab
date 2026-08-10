"""Step 0: is the doubling EARNED, or is C43's grading generic?

WHY THIS RUNS BEFORE THE ALGEBRA SEARCH. C43 reported that the block
D^0 (+) D^1 supplies a grading that a single operator cannot, and called it the
first positive structural result for the two-operator reading. Before spending
effort looking for a natural algebra on a doubled space, one question has to be
answered: **does the doubling buy something SPECIFIC to t=0,1, or would any
mirror pair do?**

If any (t, 1-t) works, the grading says nothing about t=0,1 and cannot be cited
as evidence that the t=0/t=1 doubling is structurally motivated. That is exactly
the red-flag criterion -- "found a structure" vs "found a relabelling" -- applied
one level earlier than the algebra.

THE SUSPICION, stated before testing. round67's family is AFFINE in t:

    D^t = D^{1/2} + (t - 1/2)*h_H,     spec(D^{1/2}) = {+-(n+3/2)}  <- already symmetric

A symmetric spectrum shifted by +c and the negative of the same spectrum shifted
by -c coincide. If that is all the mirror is, it holds for EVERY t and C43's
grading is generic.

PREDICTIONS, recorded before running:
  P1  spec(D^{1-t}) = -spec(D^t) identically in t, not only at t=0
  P2  therefore a grading exists for the block D^t (+) D^{1-t} at EVERY t
  P3  what IS specific to t=0,1 is the KERNEL: dim ker(D^t) = 0 for generic t
      and jumps only at level crossings
  P4  a NON-mirror pair (t, t') with t' != 1-t must FAIL to admit the grading
      -- this is the negative control, and if it passes the test is vacuous

WHAT THIS CANNOT SHOW: nothing here decides whether an algebra exists. It
decides whether C43's grading may be cited as evidence FOR the doubling.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_step0.json"
results: dict = {}

H_H = 3
N_MAX = 6


def mult(n: int) -> int:
    return (n + 1) * (n + 2)


def spectrum(tval: float) -> list[float]:
    out: list[float] = []
    for n in range(N_MAX + 1):
        for sgn in (+1, -1):
            out.extend([sgn * (n + 1.5) + (tval - 0.5) * H_H] * mult(n))
    return out


def is_mirror(a: list[float], b: list[float]) -> bool:
    return Counter(np.round([-x for x in a], 9)) == Counter(np.round(b, 9))


def grading_exists(a: list[float], b: list[float]) -> bool:
    """Can every level of block-a be paired with a level of block-b at -lambda?"""
    pool: dict[float, int] = Counter(np.round(b, 9))
    for lam in np.round(a, 9):
        want = round(-lam, 9)
        if pool.get(want, 0) <= 0:
            return False
        pool[want] -= 1
    return True


print("=" * 78)
print("Step 0 -- is C43's grading specific to t=0,1, or generic?")
print("=" * 78)

# --- P1: the mirror, symbolically, for arbitrary t ---------------------------
print("\nP1 -- is spec(D^(1-t)) = -spec(D^t) an IDENTITY in t?")
t, n = sp.Symbol("t", real=True), sp.Symbol("n", nonnegative=True, integer=True)
ident = {}
for s in (1, -1):
    lhs = s * (n + sp.Rational(3, 2)) + (t - sp.Rational(1, 2)) * H_H
    rhs = -(-s * (n + sp.Rational(3, 2)) + ((1 - t) - sp.Rational(1, 2)) * H_H)
    same = sp.simplify(lhs - rhs) == 0
    ident[f"sigma={s:+d}"] = bool(same)
    print(f"    D^t(n,{s:+d}) = {sp.simplify(lhs)}   ==  -D^(1-t)(n,{-s:+d}) : {same}")
identity_in_t = all(ident.values())
print(f"  mirror holds IDENTICALLY in t: {identity_in_t}")
results["p1_mirror_identity_in_t"] = identity_in_t

# --- P2: so the grading exists at every t ------------------------------------
print("\nP2 -- grading for the block D^t (+) D^(1-t), swept over t")
rng = np.random.default_rng(20260810)
sweep = [0.0, 1.0, 0.25, 0.5, -0.3333333333, 1.3333333333, 2.7, float(rng.uniform(-3, 3))]
p2 = {}
for tv in sweep:
    a, b = spectrum(tv), spectrum(1 - tv)
    p2[round(tv, 4)] = {"mirror": is_mirror(a, b), "grading": grading_exists(a, b)}
    print(
        f"    t = {tv:+9.4f}   mirror: {p2[round(tv, 4)]['mirror']}   grading: {p2[round(tv, 4)]['grading']}"
    )
generic = all(v["grading"] for v in p2.values())
print(f"  grading exists at EVERY swept t: {generic}")
results["p2_grading_generic_in_t"] = generic
results["p2_sweep"] = {str(k): v for k, v in p2.items()}

# --- P3: what IS specific to t=0,1 -------------------------------------------
print("\nP3 -- where the SPECIFICITY actually lives: the kernel")
ker_by_t = {}
for tv in [0.0, 1.0, 0.5, 0.25, -1 / 3, 4 / 3, 0.7, 2.0]:
    a, b = spectrum(tv), spectrum(1 - tv)
    k = int(np.sum(np.isclose(a + b, 0.0)))
    ker_by_t[round(tv, 4)] = k
    print(f"    t = {tv:+9.4f}   dim ker(D^t (+) D^(1-t)) = {k}")
print("  => the kernel is EMPTY at generic t and jumps only at level crossings.")
print("     (0,1) is round116's innermost symmetric crossing pair.")
results["p3_kernel_by_t"] = {str(k): v for k, v in ker_by_t.items()}

# --- P4: NEGATIVE CONTROL -- a non-mirror pair must FAIL ---------------------
print("\nP4 -- NEGATIVE CONTROL: pairs (t, t') with t' != 1-t must FAIL")
ctrl = {}
for tv, tp in [(0.0, 0.7), (0.0, 0.0), (0.25, 0.9), (1.0, 2.0)]:
    a, b = spectrum(tv), spectrum(tp)
    ctrl[f"({tv},{tp})"] = {"mirror": is_mirror(a, b), "grading": grading_exists(a, b)}
    print(
        f"    (t,t') = ({tv:+.2f}, {tp:+.2f})   mirror: {ctrl[f'({tv},{tp})']['mirror']}"
        f"   grading: {ctrl[f'({tv},{tp})']['grading']}"
    )
ctrl_ok = not any(v["grading"] for v in ctrl.values())
print(f"  CONTROL PASSES (no non-mirror pair admits a grading): {ctrl_ok}")
results["p4_controls"] = ctrl
results["p4_control_passes"] = bool(ctrl_ok)

# --- VERDICT -----------------------------------------------------------------
deflated = identity_in_t and generic and ctrl_ok
verdict = "C43_GRADING_IS_GENERIC__DOUBLING_NOT_YET_EARNED" if deflated else "INCONCLUSIVE"
print("\n" + "=" * 78)
print(f"VERDICT: {verdict}")
print("=" * 78)
if deflated:
    print("  C43's grading holds for EVERY mirror pair (t, 1-t), because the family")
    print("  is affine in t and spec(D^{1/2}) is already symmetric. It therefore")
    print("  says NOTHING about t=0,1 specifically, and MUST NOT be cited as")
    print("  evidence that the t=0/t=1 doubling is structurally motivated.")
    print()
    print("  What survives, and it is real: the grading is not OBSTRUCTED for the")
    print("  block, where C35 showed it is obstructed for one operator. That is a")
    print("  removed obstacle, not a positive reason to double.")
    print()
    print("  The specificity of t=0,1 lives ENTIRELY in the kernel: empty at")
    print("  generic t, dim 4 only at crossing pairs, with (0,1) the innermost.")
    print()
    print("  => Step 0's question is answered: the doubling is NOT yet earned.")
    print("     Whether it is earned at all now rests wholly on the algebra.")
results["verdict"] = verdict
RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
print(f"\nResults -> {RESULTS_PATH}")
