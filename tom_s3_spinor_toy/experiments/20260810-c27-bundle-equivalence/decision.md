# C27 test 1 — the two `t`-kernels ARE the two halves of the `Spin(4)` spinor

**Date:** 2026-08-10
**Verdict:** `KERNELS_ARE_THE_TWO_HALVES_OF_THE_SPIN4_SPINOR__C27_REFRAMED_NOT_RESOLVED`
**Runs:** the cheapest differentiating test named by the consortium run
(`experiments/20260810-consortium-c27-framework-reconciliation/decision.md`),
prioritised by external review as the highest-information next step.

## Result [VERIFIED-numpy]

Both kernels were already constructed explicitly in this repo (E12's own
`section_B_t0` and `section_B_t1_right_frame`). Acting with the isometry group
`SO(4) = (SU(2)_a × SU(2)_b)/ℤ₂`, `g ↦ a g b⁻¹`, with the frame lift
`(T_{(a,b)}ψ)(g) = ρ(b)·ψ(a⁻¹gb)`:

| kernel | construction | closed under both | `SU(2)_a` | `SU(2)_b` | content |
|---|---|---|---|---|---|
| `ker(D_{S³}, t=0)` | `ψ(g) = v` (constant, left-inv. frame) | ✓ | trivial | fundamental | **`(1,2)`** |
| `ker(D_{S³}, t=1)` | `ψ(g) = ḡ(g)·v = g⁻¹v` (right-inv. frame) | ✓ | fundamental | trivial | **`(2,1)`** |

```
ker(t=0) ⊕ ker(t=1) = (1,2) ⊕ (2,1) = g24's 4-dimensional Spin(4) spinor, EXACTLY
```

**The crux, checked rather than assumed:** for `SU(2)` the spin representation
*is* the fundamental, so `ρ(b) = b` and the cancellation `ρ(b)·b⁻¹ = I` is what
makes `V1` closed. Verified over 200 random `b ∈ SU(2)`. The quaternion facts
`g ḡ = I` and `g ∈ SU(2)` were re-derived here, not cited from E10.

**Negative control passes:** the deliberately mixed space
`ψ(g) = (I + g⁻¹)v` **fails** the membership test — the method can tell a clean
bi-multiplet from a mixture.

## What this means for C27

C27's "6 modes vs 3 needed" compared a **fixed-`t`** count against a
**both-`t`** requirement. Per triality channel the S³ side supplies 2 at `t=0`
*plus* 2 at `t=1` = the one 4-dimensional `Spin(4)` spinor framework A asks for.

**C27 is REFRAMED, NOT RESOLVED, and its status is unchanged.** Matching
representation content is bookkeeping; it does **not** show both `t` are
simultaneously physically realized. That is `C11`'s product-ansatz fork, and it
is OPEN. Round78's standing instruction not to manufacture a comfortable
resolution is honoured: this does not supply the physics, it identifies which
physics question the counting was always standing on.

## The consolidation this produces — three open items are one question

| item | was | now |
|---|---|---|
| `C27` | "6 modes vs 3 — where are the missing states?" | needs both `t` |
| `C25`/`H1c` | "which of `t=0`/`t=1` is selected?" | **neither — both**, they are the two chiral halves |
| `C11` | "does 'two coexisting D's' make sense?" | **the actual question all three rest on** |

This also independently supports C37/OB13's inversion branch: if both `t` are
required, asking *which one is selected* was ill-posed, and every even-parity
null result was exactly what that predicts.

## ⚠️ ~~The same mismatch exists on the S⁶ side and is NOT explained~~ — WITHDRAWN

> **WITHDRAWN 2026-08-10, same day, by `experiments/20260810-s6-factor8/`.** The
> section below compared `ker(D_{S⁶}⊗S⁻) = 1` against framework A's `8`. That is
> the wrong pairing: G74A's own twist is `S⁻ = 3 ⊕ 1`, **four**-dimensional,
> while `8 = S⁺ ⊕ S⁻` is the full Dirac spinor the twisted operator does not act
> on. Computed: `SU(3)`-singlets are **2** in the full `8`, **1** in `S⁺`, **1**
> in `S⁻`. The correct comparison is **1-of-4**, and it obeys the *same* rule as
> the S³ side — kernel = the invariant subspace of the bundle actually used
> (S³: 2 of 4; S⁶: 1 of 4). **There is no unexplained systematic residue**, and
> the category-error reading (M3) is correspondingly weakened. Original text kept
> below for the record.

## ~~The same mismatch exists on the S⁶ side and is NOT explained~~ (original)

Stated because the S³ result is otherwise easy to over-sell:

```
              framework A (rep content)   framework B (kernel dim)   ratio
  S³ side     Spin(4) spinor      = 4     ker(D_S³, fixed t) = 2       2   <- now explained
  S⁶ side     G₂/Spin(7) spinor   = 8     ker(D_S⁶,twisted)  = 1       8   <- NOT explained
  product     4 × 8 = 32                  2 × 1 = 2 per channel
```

There is **no second parameter on the S⁶ side** playing the role `t` plays on
S³. So the systematic pattern — framework A counts *representation dimensions of
the fibre*, framework B counts *kernel dimensions of an operator on sections* —
is confirmed on both factors, and only one of the two discrepancies now has a
mechanism.

**This strengthens the consortium's M3 (category-error) branch considerably**,
and with it the consequence M3 carries: if the two frameworks systematically
count different objects, then `N_gen=3`'s representation-content half and its
index half were computed in different bundles and **the derivation needs
re-joining**, independently of whether C27's number works out.

## What this does NOT establish

1. **C27 is not resolved**; status unchanged (`REFUTED` as stated).
2. Does not show both `t` are simultaneously realized — that is `C11`, OPEN, and
   it is now the load-bearing question for all three items above.
3. Does not explain the S⁶-side factor 8. Only the S³-side factor 2.
4. Does not touch the 3-channel/triality structure or OB4.
5. Says nothing about which framework is the *physically* correct bookkeeping —
   it shows they count different things, not which one to keep.

## Check

```
python experiments/20260810-c27-bundle-equivalence/bundle_equivalence.py
```
Expect `VERDICT: KERNELS_ARE_THE_TWO_HALVES_OF_THE_SPIN4_SPINOR`; `t=0` → `(1,2)`,
`t=1` → `(2,1)`; crux cancellation True; negative control passes.
