# C97 -- k=3 replication: does the L/R swap follow a parity pattern?

**Experiment id:** `20260812-c97-k3-replication-parity-check`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C95 (k=1: `L_i=+l_{e_i}(1)`, `R_i=-l_{e_i}(1)^T`).
C96 (k=2: `L_i=-l_{e_i}(2)^T`, `R_i=+l_{e_i}(2)` -- roles SWAPPED
relative to k=1, both bracket-verified, after fixing two genuine bugs
in C96's own new construction: an abstract-vs-concrete symbol
conflation, and `build_d2_matrix` being an anti-homomorphism, fixed via
`D_correct(g):=D_raw(g^{-1})`).

---

## Why this is needed

C96's own decision.md named this explicitly as the next-cheapest test:
"the next-cheapest test (per this round's own kill_criterion) would be
a k=3 replication using the SAME (now-debugged) construction." Two
data points (k=1, k=2) with opposite L/R role assignments are
consistent with several different explanations -- a parity-alternating
rule (odd k matches k=1's pattern, even k matches k=2's), a
monotonic drift, or no clean pattern at all (each k independently
different). A third data point (k=3) is the cheapest way to
discriminate between "parity" and "no clean pattern," though it cannot
by itself fully confirm a parity rule (a genuine parity confirmation
would need k=4 to also match k=2, k=5 to match k=1/k=3, etc. -- not
attempted this round).

## Method

Generalize C96's now-debugged construction from k=2 to general k:
build `D^{(k)}(g)` as the k-th symmetric power via RAW (unnormalized)
monomial substitution matching C85's own `|p>` basis convention, using
the SAME `D_correct(g) := D_raw(g^{-1})` fix that repaired C96's
anti-homomorphism bug (verified there via direct symbolic composition
of two independent SU(2) elements; reused here unchanged, not
re-derived, since the fix is k-independent -- it corrects the raw
monomial-substitution trick's own pullback/pushforward direction,
which does not depend on the degree of the symmetric power). Apply the
SAME abstract-free-symbol coefficient-extraction method (`D_sym` of
size `(k+1)x(k+1)`, matching C95/C96's own convention) to derive
`L_i`, `R_i` at k=3, and calibrate against C85's certified `l_{e_i}(3)`
exactly as C96 calibrated against `l_{e_i}(2)`.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P0 (calibration)** | `R_i(k=3)` matches ONE of `{+l,-l,+lT,-lT}` uniformly across `e1,e2,e3`, with `[R1,R2]=2R3` holding exactly | pending |
| **P1 (parity hypothesis)** | `L_i(k=3)` matches `+l_{e_i}(3)` directly (matching k=1's odd-k pattern, NOT k=2's even-k pattern) | pending |
| **P2 (bracket)** | both `[L1,L2]=2L3` and `[R1,R2]=2R3` hold exactly at k=3 | pending |

## kill_criterion

If P0 fails (no uniform bracket-consistent match), the k=3 lift of the
construction itself has a bug analogous to C96's own two self-caught
bugs -- stop, debug before drawing any conclusion, exactly as C96's own
gate required. If P0 holds but P1 fails (i.e. k=3 matches k=2's
pattern instead, `L_i=-l_{e_i}(3)^T`), the parity hypothesis is
falsified by a single counterexample -- informative: would mean no
simple 2-cycle rule governs the L/R swap, and the multiplication-
operator build (task #59) needs genuine per-level certification, not a
short periodic formula. If P0 and P1 both hold, this is ONE additional
data point consistent with a parity rule -- not proof of one (a
genuine parity claim would still need k=4 to independently confirm the
even-k branch before being trusted).

## What this cannot show

- Does **not** prove a parity rule even if P1 holds -- one more
  consistent data point, not a proof; k=4 would be the next
  discriminating test on the even-k branch.
- Does **not** build the multiplication operator itself.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
