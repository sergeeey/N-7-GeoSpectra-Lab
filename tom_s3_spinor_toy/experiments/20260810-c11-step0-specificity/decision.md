# Step 0 — C43's grading is GENERIC. The doubling is not yet earned.

**Date:** 2026-08-10
**Verdict:** `C43_GRADING_IS_GENERIC__DOUBLING_NOT_YET_EARNED`
**Partially deflates:** C43, from yesterday's own run — found by running the
step the portfolio review placed *before* the algebra search.

## The question step 0 asks

C43 called the block's grading "the first positive structural result for the
two-operator reading". Before spending effort on an algebra over a doubled
space: **does the doubling buy anything specific to `t=0,1`, or would any mirror
pair do?** If any pair works, the grading cannot be cited as evidence that the
`t=0/t=1` doubling is motivated — that is the red-flag criterion (structure vs
relabelling) applied one level earlier than intended.

## Answer: any mirror pair does [VERIFIED-sympy]

The family is **affine** in `t` and `spec(D^{1/2}) = {±(n+3/2)}` is **already
symmetric**. So:

```
D^t(n,+1) = n + 3t        ==  −D^(1−t)(n,−1)     identically
D^t(n,−1) = −n + 3t − 3   ==  −D^(1−t)(n,+1)     identically
```

`spec(D^{1−t}) = −spec(D^t)` is an **identity in `t`**, not a fact about `t=0,1`.
Swept over `t ∈ {0, 1, ¼, ½, −⅓, 4/3, 2.7, −1.12}` — mirror and grading hold at
**every** one.

**Negative control passes:** non-mirror pairs `(0, 0.7)`, `(0, 0)`, `(0.25, 0.9)`,
`(1, 2)` all **fail** both mirror and grading. The test is not vacuous.

## What must be withdrawn, and what survives

**Withdrawn:** C43's grading may **not** be cited as evidence that the `t=0/t=1`
doubling is structurally motivated. It holds for every mirror pair.

**Survives, and is real:** the grading is not *obstructed* for the block, where
C35 showed it *is* obstructed for a single operator. **That is a removed
obstacle, not a positive reason to double.** The distinction is the whole point
of this step.

## Where the specificity actually lives — the kernel

| `t` | `dim ker(D^t ⊕ D^{1−t})` |
|---|---|
| **0, 1** | **4** |
| ½, ¼, 0.7 | **0** |
| −⅓, 4/3 | 12 |
| 2 | 40 |

Empty at generic `t`; jumps only at level crossings. And `(0,1)` is not merely
round116's *innermost* crossing pair — it is the one with the **smallest
non-zero kernel**. Every other crossing over-produces.

That is a **minimality** observation, not a derivation: it says `(0,1)` is the
least-excess choice among crossings, not that anything selects it. Recorded as
such.

## Consequence for the programme

Step 0's question is answered: **the doubling is not yet earned.** Whether it is
earned at all now rests **wholly on the algebra** — exactly where the portfolio
review pointed, but now with the grading no longer available as supporting
evidence, so the algebra search carries the full weight.

PARENT_ACTION_GATE stays 3/6 by *count*, but the γ entry must be read as
"exists, generically" rather than "exists, because of this structure".

## What this does NOT establish

1. **Does not show the doubling is wrong** — only that the grading does not argue
   for it.
2. **Does not touch C42** (no single `t` has a 4-dim kernel) or C38/C39.
3. Does not decide whether an algebra exists.
4. The minimality of `(0,1)`'s kernel is an observation about crossings, not a
   selection principle — nothing here derives `(0,1)`.

## Check

```
python experiments/20260810-c11-step0-specificity/step0_is_doubling_earned.py
```
Expect: mirror identity in `t` **True**; grading at every swept `t` **True**;
kernel 4 / 0 / 12 / 40 as tabled; all four non-mirror controls **False**.
