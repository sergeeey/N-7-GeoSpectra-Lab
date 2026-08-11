# C73 -- round59's real twisted D_S6 battery: chirality verified directly, deformation-robust, negative control honestly incomplete

**Experiment id:** `20260811-c73-round59-real-twisted-dirac-battery`
**Date:** 2026-08-11 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** round59 (`20260714-round59-trivial-rank-certification`, the ONLY
real, non-surrogate curvature-twisted Dirac operator construction in this
project); G74B/C21 (chirality claim, derived abstractly, three weeks BEFORE
round59 existed); Rounds 52-56 (Casimir-difference certified bound for
non-trivial isotypic sectors)

---

## Why this round is scoped the way it is

`predictions_before_data.md`'s P4 (ledger-C73) asks for "index/kernel=1 under
admissible connection deformations, correct chirality and SU(3) kernel
content, negative controls (wrong twist) failing as they must." An Explore
agent survey found all five pieces genuinely open for round59's SPECIFIC
operator (chirality was derived abstractly by an EARLIER, unrelated
construction; index/gap/deformation/negative-control were never computed for
round59's own matrix at all).

**Before writing any test, the target had to be pinned down precisely** —
this round's own first attempt (raw kernel of the full 64x64 D) gave **36**,
not 1, which does NOT match the headline claim. Reading `preprint.tex`
sec:kernel directly resolved this: "kernel=1" refers to `D` restricted to the
**SU(3)-invariant sub-blocks specifically** (`domain_inv`=2-dim, within
`Sigma_odd(x)Sigma_even`; `target_inv`=1-dim, within `Sigma_even(x)Sigma_even`)
— exactly round59's own `(2,1)` domain/target dimensions. The raw kernel (36)
and even the full un-restricted `odd_even->even_even` block's kernel (9)
measure a broader, mostly physically-irrelevant quantity, addressed for
non-trivial content by Rounds 52-56's SEPARATE certified bound, not by
round59's own computation.

## The claim under test

> **C73 (working).** Reproduces round59's own certified `(a,b,s)=(-1,-sqrt3,4)`
> as a positive control; directly verifies (for the first time, from round59's
> own matrix rather than an abstract dimension-counting argument) that the
> zero mode is purely left-handed (`ker(D+)=1, ker(D-)=0`); shows the
> invariant-sector kernel dimension is EXACTLY 1 for any nonzero uniform
> rescaling of the connection (a closed-form linear result, not merely
> observed), degenerating only at the singular point of no connection at all;
> and honestly reports that every attempted "wrong twist" negative control
> within round59's own fixed construction either reproduces the identical
> physical result (a hidden even/odd duality) or vanishes for purely
> algebraic/structural reasons unrelated to physical correctness — a genuine
> discriminating negative control needs a different twisting representation,
> not attempted.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1 (reproduction)** | numerical `(a,b,s)` matches round59's exact-arithmetic `(-1,-sqrt3,4)` | pending |
| **P2 (chirality)** | `ker(D+)=1`, `ker(D-)=0` on the invariant sector, matching G74B/C21 | pending |
| **P3 (scope)** | raw/full-block kernel counts differ from the invariant-sector count, and this difference is explicable (not a contradiction) | pending |
| **P4 (deformation)** | kernel dimension is robust (stays 1) under at least a nontrivial neighborhood of connection-scale deformations | pending |
| **P5 (negative control)** | at least one genuinely discriminating "wrong twist" test can be constructed within round59's existing objects | pending -- flagged in advance as the piece most likely to fail given round59's construction is fixed, not parametrized by a twist choice |

## kill_criterion

P1 fails if the numerical reproduction disagrees with round59's certified
values (would indicate a genuine construction bug, either in round59's
original or this round's numeric translation). P2 fails if chirality is
mixed (would contradict G74B/C21). P4 fails if kernel dimension changes for
ANY t != 0 near t=1 (would indicate the zero mode is a fine-tuned accident,
not topologically protected). P5's prediction is explicitly allowed to fail
honestly — see "what this cannot show" below.

## What this cannot show

- Does **not** independently re-verify Rounds 52-56's Casimir bound for
  non-trivial isotypic sectors -- cited, not re-derived.
- Does **not** supply a genuine wrong-twist negative control if P5 fails as
  anticipated -- this would leave the "negative controls failing as they
  must" piece of the original C73 spec genuinely open, honestly reported.
- Does **not** test a general (non-uniform-scale) connection deformation --
  no alternative admissible S6 connection dataset exists in this project.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
