r"""
C157 STEP 3 -- the null model the C156 skeptic would demand before anything
here is trusted. P3, pre-registered:

Replace Phi+ by a random set of N integer vectors (no root-system structure)
with the SAME N and dimension as a real system, and ask: for a random even
target, is the signed count balanced too? If YES at anywhere near 100%, the
theorem's balance is a property of "sum to a fixed target over a symmetric
random walk", not of root systems specifically. If balance is NOT generic,
that supports the balance needing the actual algebraic cancellation the Weyl
proof supplies, rather than being dimension-generic the way C156's
surjectivity turned out to be.

SUBSTRATE NOTE: random vector sets have NO algebraic cancellation, so the DP
state space can explode combinatorially where a real root system collapses
(root systems are closed under reflection, which is exactly what keeps their
reachable-sum sets small). A `StateBlowup` here is reported as
BLOCKED-INFRASTRUCTURE for that trial, not as evidence for or against P3.

Run:  python -u c157_step3_null_model.py
"""

import random
import sys

import sympy as sp
from c157_step2_census import StateBlowup, census

MAX_STATES = 60_000


def random_system(N, dim, low, high, seed):
    rnd = random.Random(seed)
    return [tuple(rnd.randint(low, high) for _ in range(dim)) for _ in range(N)]


def random_reachable_target(roots, rnd):
    subset = [b for b in roots if rnd.random() < 0.5]
    n = len(roots[0])
    tot = [sp.Integer(0)] * n
    for b in subset:
        for t in range(n):
            tot[t] += b[t]
    return tuple(tot)


def trial(N, dim, low, high, seed):
    rnd = random.Random(seed)
    roots = random_system(N, dim, low, high, seed)
    target = random_reachable_target(roots, rnd)
    ne, no = census(roots, target, max_states=MAX_STATES)
    return ne + no, ne, no


if __name__ == "__main__":
    print("=" * 78, flush=True)
    print("C157 STEP 3  NULL MODEL -- is balance generic for random sign-sum sets?", flush=True)
    print(
        f"  (state-space guard: max_states={MAX_STATES}, overflow = BLOCKED-INFRASTRUCTURE)",
        flush=True,
    )
    print("=" * 78, flush=True)
    # small integer range keeps the state space tractable; N kept modest for
    # the same reason -- this is a substrate constraint, stated as such.
    cases = [
        ("A_2 shape", 3, 3, 2),
        ("G_2 shape", 6, 2, 2),
        ("A_2xA_2 shape", 6, 4, 2),
        ("D_4 shape", 10, 3, 1),
        ("F_4 shape", 16, 2, 1),
    ]
    summary = []
    for label, N, dim, hi in cases:
        trials = 100
        balanced = 0
        nonempty = 0
        blown = 0
        for s in range(trials):
            try:
                total, ne, no = trial(N, dim, -hi, hi, seed=10000 + s)
            except StateBlowup:
                blown += 1
                continue
            if total == 0:
                continue
            nonempty += 1
            if ne == no:
                balanced += 1
            if s % 20 == 0:
                print(f"    ...{label}: trial {s}/{trials} done", flush=True)
        rate = 100 * balanced / nonempty if nonempty else float("nan")
        print(
            f"  {label:16s} (N={N:2d}, dim={dim}, range=+-{hi}): "
            f"balanced {balanced}/{nonempty} nonempty ({rate:.1f}%), "
            f"blown_up={blown}/{trials}",
            flush=True,
        )
        summary.append((label, balanced, nonempty, blown, trials))

    print(flush=True)
    print("=" * 78, flush=True)
    print("VERDICT", flush=True)
    print("=" * 78, flush=True)
    for label, balanced, nonempty, blown, trials in summary:
        if nonempty == 0:
            print(
                f"  {label}: NO USABLE TRIALS (all empty or blown up) -- "
                f"BLOCKED-INFRASTRUCTURE for this shape, not evidence",
                flush=True,
            )
        else:
            rate = 100 * balanced / nonempty
            print(
                f"  {label}: {rate:.1f}% balanced over {nonempty} usable trials "
                f"({blown} blown up, not counted)",
                flush=True,
            )
    print(flush=True)
    print("  Near 100% => balance is dimension/parity-generic (vacuous, C156-style).", flush=True)
    print("  Well below 100% => root-system structure does real algebraic work.", flush=True)
    sys.stdout.flush()
