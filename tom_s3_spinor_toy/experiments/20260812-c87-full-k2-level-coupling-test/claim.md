# C87 -- extends C86's joint-level coupling test to k=2 (physical n=1<->n=2)

**Experiment id:** `20260812-c87-full-k2-level-coupling-test`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C86 (first n=0<->n=1 joint coupling test, clean NULL).
Continuation named explicitly in C86's own "what survives" section.

---

## The claim under test

> **C87.** Level k=2's own full 18-dimensional S3 Hilbert space (q x p x r)
> simultaneously contains physical n=2's sigma=-1 branch (D=-3.5,
> multiplicity 12) and physical n=1's sigma=+1 branch (D=2.5, multiplicity
> 6) -- a SECOND, independent adjacent-n pair (n=1<->n=2), genuinely
> different from C86's n=0<->n=1 test (k=2's own space does not contain
> n=0 at all). C79-C83's coupling operator T, tested on this pair for the
> first time via the exact same methodology C86 established, is predicted
> to again show no crossing -- extending, not merely repeating, the clean-
> null pattern one level deeper into the Peter-Weyl tower.

## Predictions, recorded before running the permanent script

| # | Prediction | Outcome |
|---|---|---|
| **P1 (D_S3 construction)** | full level-k=2 D_S3 reproduces n=1's sigma=+1 (D=2.5, mult 6) and n=2's sigma=-1 (D=-3.5, mult 12) exactly | pending |
| **P2 (self-dual triple)** | no crossing | pending |
| **P3 (anti-self-dual triple)** | no crossing | pending |

## kill_criterion

Same structure as C86: P1 failing means a construction bug, stop and fix
before trusting anything downstream (the script asserts this). P2/P3 are
the actual test -- a "no crossing" result extends the pattern one level
deeper; a crossing would be the first positive evidence anywhere in this
arc for the reviewer's own hypothesized inter-level mixing mechanism, and
would require the same extra scrutiny every unexpectedly positive result
in this arc has received.

## What this cannot show

- Does **not** test n=0<->n=2 (a "next-nearest" pair) -- that would
  require a joint construction spanning two non-adjacent k-levels
  simultaneously, not attempted here.
- Does **not** test any coupling candidate beyond round119's `so(4)_1`
  pair.
- Does **not** rule out inter-level mixing for a genuinely different
  coupling construction.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
