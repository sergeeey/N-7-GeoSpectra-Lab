# A1 — the "S⁶ factor 8" was my own wrong pairing. No systematic residue exists.

**Date:** 2026-08-10
**Verdict:** `MY_FACTOR8_CLAIM_WAS_A_WRONG_PAIRING__UNIFIED_RULE_HOLDS_ON_BOTH_FACTORS`
**Withdraws:** a claim I made earlier the same day, in C38's `decision.md`, its
commit message, `activeContext`, and a pearl.

## What I claimed, and it was wrong

> *"the SAME rep-content-vs-kernel-dimension mismatch exists on the S⁶ side at
> ratio 8 (`Spin(7)` spinor = 8 vs `ker(D_S⁶,twisted)` = 1) with NO analogue of
> `t` there — so the pattern is systematic and only one of its two instances now
> has a mechanism."*

That was written from a table I typed, not from a computation. **Both halves
are false.**

## What the computation says [VERIFIED-numpy]

`G74A` states its own twist explicitly: `S⁻ = T^{1,0}S⁶ ⊕ trivial = 3 ⊕ 1` under
`SU(3)` — **four**-dimensional. Framework A's `8` is the FULL Dirac spinor of
`Spin(6)`, which splits by chirality as `8 = 4 ⊕ 4̄ = S⁺ ⊕ S⁻`. **I compared a
kernel against a bundle the twisted operator does not act on.**

Built the `Spin(6)` spinor module from this repo's own `s6-harm-g0` gammas, split
by chirality, lifted `g10b`'s explicit `su(3) ⊂ so(6)`, and counted singlets as
joint-kernel dimensions:

| module | `SU(3)`-singlets |
|---|---|
| full `8` (framework A's S⁶ fibre) | **2** |
| `S⁺` (4) | **1** |
| **`S⁻` (4) — the bundle the twist actually uses** | **1** |

`8 = 4 ⊕ 4̄`, each half `= 3 ⊕ 1`, one singlet each. So the correct S⁶ comparison
is **1-of-4**, not 1-of-8.

**Negative control passes:** the *larger* group `so(6)` has **0** singlets in
`S⁻` versus `su(3)`'s 1 — a bigger group cannot have more invariants, so the
counting method is measuring the group and not the matrix count.

## The unified rule — no residue is left over

```
kernel = the invariant / singlet subspace of the bundle the operator ACTUALLY uses

  S³ :  2 of 4    invariant under one SU(2) factor of Spin(4)      (C38)
  S⁶ :  1 of 4    SU(3)-singlet of S⁻                              (here)
```

One rule, both factors, nothing unexplained. **The "systematic mismatch" I
reported does not exist.**

## Consequence — this is good news, and it is not a resolution

The **category-error reading (M3) is substantially weakened.** Its force came
from the claim that the two frameworks count incompatible objects on *both*
factors; with the S⁶ half withdrawn, what remains is one coherent rule relating
them. So the worry that `N_gen=3`'s representation half and index half were
"computed in different bundles and must be re-joined" is **not supported** by
this evidence.

**What is unchanged:** `C27`'s S³-side multiplicity, and `C11` — whether both
`t` are simultaneously realized. The frontier is exactly where C38/C39 left it.
This test removed a threat to the headline; it did not advance the headline.

## The near-miss in this file's own machinery

The first run printed `bracket-homomorphism residual: 5.00e-01` — the spinor
lift carried a stray factor and **was not a Lie homomorphism at all**. Its
singlet counts were therefore meaningless. They nevertheless came out `2/1/1`,
**exactly matching the prediction written at the top of this file** — because a
joint kernel is invariant under scaling.

A right answer from broken machinery, agreeing with a stated prediction, is the
most persuasive wrong result available. It was caught only because the residual
was computed and printed. It is now **asserted**, so the file cannot report a
verdict from a broken lift again.

## What this does NOT establish

1. Does **not** resolve `C27` or `C11`. Nothing about the S³ multiplicity moved.
2. Does **not** show `N_gen=3` is correct — it removes one specific objection.
3. Does **not** verify `dim ker = 1` itself; that is G74A's (Lemma A + B), used
   here as given.
4. The singlet counts are for the **fibre** representations. Whether the actual
   zero mode occupies the singlet slot is Lemma A's separate question.

## Check

```
python experiments/20260810-s6-factor8/factor8_check.py
```
Expect residual `0.00e+00` (asserted), singlets `2 / 1 / 1`, control `so(6) → 0`.
