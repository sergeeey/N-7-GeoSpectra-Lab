# C11 first cut — the one-operator escape is closed; C11 is forced onto two D's

**Date:** 2026-08-10
**Verdict:** `C11_FORCED_ONTO_THE_TWO_OPERATOR_READING`
**Type (L0):** Descriptive — a question about the structure of existing objects.

## Why this was the right first question

"Both `t` are realized" was ambiguous, and the ambiguity *was* the question:

| reading | what it would mean |
|---|---|
| **(i)** | ONE operator whose kernel is the full 4-dim `(2,1) ⊕ (1,2)` |
| **(ii)** | TWO operators, one per sector, coexisting |

(i) is two lines of algebra against machinery already in the repo. (ii) is the
hard spectral-triple question. **Closing (i) narrows C11 to something nameable
before any expensive work starts.**

## Q1 — no single `t` has a 4-dimensional kernel [VERIFIED-sympy]

round67's closed form, `h_H = 3` reproduced here:

```
D^t(n,σ) = σ(n + 3/2) + (t − ½)·h_H
```

Solved exactly, not scanned:

| level | vanishes at |
|---|---|
| `n=0, σ=+1` | **t = 0** |
| `n=0, σ=−1` | **t = 1** |
| `n=1, σ=±1` | t = ∓⅓ |
| … | … |

**Values of `t` where two levels vanish simultaneously: NONE.**

The reason is structural, not numerical: the torsion shift `(t−½)·h_H` is the
**same for every level**, while the levels are separated by `2σ(n+3/2)`. A
uniform shift cannot bring two distinct levels to zero at once. So each `t`
gives `dim ker = 2` (one `SU(2)` doublet, E12), never 4.

## Q2 — but the two kernels *do* share a home [VERIFIED-numpy]

They are written in different frames (left- vs right-invariant), so this was not
automatic. Expressed in one trivialization and sampled at 60 points of `S³`:

```
dim V0 = 2,  dim V1 = 2,  dim(V0 + V1) = 4,  dim(V0 ∩ V1) = 0
```

Linearly independent, spanning exactly the 4 dimensions C38 predicted.
**Negative control passes:** fed `V0` against a span containing one of its own
vectors, the method reports intersection **1**, so it can detect overlap when
overlap exists.

## What this settles

**Reading (i) is dead.** "Both `t`" cannot mean one operator with a bigger
kernel — no member of the Cartan–Schouten family has one, for a reason that
holds for the whole family rather than at sampled points.

**C11 is therefore forced onto reading (ii)**, which is exactly what its own
original name asked: *"does 'two coexisting D's' even make sense as a spectral
triple?"* The framing was right; what this closes is the escape route that would
have made the question go away.

And Q2 says the two-operator reading is not obviously incoherent from the
kernel side: the sectors are independent subspaces of one section space, not
rival descriptions of the same states.

## What this does NOT establish

1. **Does not answer C11.** Whether two `D`s coexist as one spectral triple is
   untouched — this narrows the question, it does not decide it.
2. **Does not show both `t` are physically realized.** Q2 is about section
   spaces, not dynamics.
3. **Does not rule out a 4-dim kernel outside the Cartan–Schouten family.** The
   algebra covers that family only; a different connection or an added
   symmetry-breaking term (C37's torsion-odd requirement) is not excluded.
4. Says nothing about the S⁶ side or the 3-channel structure.

## Next

The narrowed question is now nameable: **can two `D`s coexist as one spectral
triple?** Concretely, that means the block/doubled construction round110 already
attempted and OB2's `PARENT_ACTION_GATE` fields — algebra, Hilbert space,
grading, real structure — of which C35 showed the grading **cannot** exist for
the toy `D` (non-symmetric spectrum) and `J` exists only pointwise. Those are
constraints the two-operator construction must now satisfy, and they are already
on record rather than hypothetical.

## Check

```
python experiments/20260810-c11-first-cut/c11_one_operator_or_two.py
```
Expect: coincident-`t` NONE; `dim(V0+V1) = 4`, intersection `0`; control `1`.
