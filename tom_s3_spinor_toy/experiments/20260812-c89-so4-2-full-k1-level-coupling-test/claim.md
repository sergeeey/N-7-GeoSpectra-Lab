# C89 -- extends C86's n=0<->n=1 joint coupling test to round119's so(4)_2

**Experiment id:** `20260812-c89-so4-2-full-k1-level-coupling-test`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C86 (n=0<->n=1 joint test, so(4)_1, clean NULL), C88
(direct selection-rule matrix elements: the S3-side coupling channel is
candidate-independent, real, and nonzero -- the necessary condition for
a crossing is already known to hold for ANY candidate using this T
construction; what remains open is whether a specific candidate's own
S6-side factor combines with it to produce an actual crossing).

---

## The claim under test

> **C89.** round119's so(4)_2 (BLOCK2=[4,5,6,7], `so4_all[6:12]`),
> previously tested only at n=0's scalar approximation (C82, clean NULL
> there too, but unable to probe inter-level mixing at all), is tested
> for the first time on the genuinely richer k=1 joint Hilbert space
> (containing physical n=0's sigma=+1 and n=1's sigma=-1 branches
> simultaneously), via C86's exact, now-Hermiticity-corrected
> methodology.

## Predictions, recorded before running the permanent script

| # | Prediction | Outcome |
|---|---|---|
| **P1 (su(2) closure)** | self-dual/anti-self-dual triples close as genuine su(2) (matching C82's own already-established result) | pending |
| **P2 (D_S3 construction)** | reproduces round67's target exactly (reused, already certified in C86) | pending |
| **P3/P4 (self-dual/anti-self-dual)** | no crossing, consistent with C86's own so(4)_1 result and C82's own n=0-only so(4)_2 result | pending |

## kill_criterion

P1/P2 failing means a construction bug -- stop and fix. P3/P4 are the
actual test; a crossing would be the first candidate anywhere in this
extended arc to survive the joint-level test and would require the same
extra scrutiny every unexpectedly positive result here has received.

## What this cannot show

- Does **not** test k>=2 for this candidate.
- Does **not** test C75's or C83's remaining complement candidates on
  this joint space.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
