# C98 -- k=4 replication: does the k>=2 pattern stabilize, or was k=3 a fluke?

**Experiment id:** `20260812-c98-k4-replication-stability-check`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C95 (k=1: `L_i=+l_{e_i}(1)`, `R_i=-l_{e_i}(1)^T`).
C96 (k=2: `L_i=-l_{e_i}(2)^T`, `R_i=+l_{e_i}(2)`, roles swapped from
k=1). C97 (k=3: matches k=2's pattern exactly, NOT k=1's -- falsified
the parity/alternating hypothesis; tentative emerging picture is "k=1
is a distinct base case, k>=2 follows one fixed rule," explicitly not
yet proven with only 2 consistent points).

---

## Why this is needed

C97's own decision.md was explicit: "2 consistent points after 1
falsified hypothesis is encouraging, not conclusive... k=4 is the
next-cheapest discriminating test, deliberately not run in this same
round to avoid AOG-1 (pre-registration) violation." This round is that
independent, pre-registered k=4 check. It is now essentially free to
run: C97's own script already generalized the (now twice-debugged)
construction to arbitrary `k` via a single `K` parameter -- this round
only changes `K=3` to `K=4` and adds a fresh, honest prediction before
running, per this project's own discipline against re-labeling data
already in hand.

## Method

Identical to C97's method, `K=4` (dim=5) instead of `K=3`. Reuses
`build_dk_matrix` (the `D_correct(g):=D_raw(g^{-1})` anti-homomorphism
fix, verified in C96) and `coefficient_space_generator_general` (the
abstract-free-symbol `D_sym` extraction, verified in C96) completely
unchanged -- no new construction logic introduced.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P0 (calibration)** | `R_i(k=4)` matches ONE of `{+l,-l,+lT,-lT}` uniformly, with `[R1,R2]=2R3` holding exactly | pending |
| **P1 (k>=2 stability hypothesis)** | `L_i(k=4)` matches `-l_{e_i}(4)^T` (the k=2/k=3 pattern), NOT `+l_{e_i}(4)` (k=1's pattern) | pending |
| **P2 (bracket)** | both `[L1,L2]=2L3` and `[R1,R2]=2R3` hold exactly at k=4 | pending |

## kill_criterion

If P0 fails, this round's own k=4 lift of the construction has a bug
-- stop, debug before drawing any conclusion (though this is now the
THIRD independent use of the same construction, making a fresh bug
specific to k=4 alone less likely but not impossible; treat any
failure here with the same seriousness as C96's own two self-caught
bugs, not as an automatic pass-through). If P0 holds but P1 fails
(k=4 matches k=1's pattern instead, or matches neither cleanly), the
"k=1 special, k>=2 stable" hypothesis is FALSIFIED by this
counterexample -- informative: would mean each k potentially needs
independent certification, with no shortcut formula at all, and task
#59's multiplication-operator build must certify the q-side generator
per-level rather than trusting any extrapolated rule. If P0 and P1
both hold, this is a THIRD independent data point (k=2,3,4 all
consistent) -- meaningfully stronger support for the k>=2 rule, though
still not a formal proof for all k (an inductive/structural argument,
not tested here, would be needed for that).

## What this cannot show

- Does **not** prove the k>=2 rule for all k even if P1 holds -- 3
  consistent points is strong empirical support, not a general proof;
  a structural/inductive argument would still be needed for full
  confidence at, e.g., k=10 or k=20.
- Does **not** build the multiplication operator itself.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
