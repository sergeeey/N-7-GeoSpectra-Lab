# Consortium #2 — C27: the "excess factor 2" may be a bundle mismatch, not a physics excess

**Date:** 2026-08-10 · **Depth:** Глубокий (FL Standard)
**Verdict:** `RELOCATED__NOT_RESOLVED__CHEAPEST_TEST_IDENTIFIED`
**Target:** row 1 of C27's Relaxation Map (round78) — the 32-state ↔ zero-mode
reconciliation, which round78 itself named the thing to tackle first.

**Round78's own standing warning, honoured here:** concluding "the doublet IS
the generation, so multiplicity 2 is fine" would be *"exactly the kind of
forced, comfortable resolution this experiment was explicitly instructed not to
manufacture."* **Nothing below resolves C27.** It relocates the question and
names a cheap test that discriminates.

## L0 — question type: Descriptive

*Which mathematical object does each of the two frameworks actually count?* No
intervention, no counterfactual. **Does NOT mean:** (1) that C27 is resolved;
(2) that `N_gen=3` is restored; (3) anything about `t`-selection or OB4.

## The anomaly (mode: Аномалия)

Two numbers the project treats as commensurable:

```
framework A (preprint §sm-content, g24):  32 = Spin(4)_spinor(4) (x) Spin(7)_spinor(8)
framework B (C27, E2/E9/E12):             6  = ker(D_S3)(2) x ker(D_S6,tw)(1) x 3 channels
```

## The invisible line [INFERRED — chain stated, not asserted]

`g24`'s own decision.md states the A-side rep explicitly:

> `Spin(4)_spinor = (2,1)+(1,2) [4D]`

— **two** SU(2) doublets of opposite chirality. Framework B's kernel is computed
on `ℂ²` with `Z_i = i·σ_i` (E2/E9/E12), a **single** SU(2) doublet: the
`Cl(0,3)` module, i.e. the intrinsic 3-dimensional spin structure of S³.

**These are two different bundles on the same S³**, and the project has been
reading their dimensions as if they were the same object. `Spin(4)` is not the
spin group of S³ — it is the spin group of the 4-dimensional structure in which
S³ sits (its isometry group `SO(4)`, acting as `SU(2)_L×SU(2)_R`). `Spin(3) =
SU(2)` is.

**The factor 2 between "6 modes" and "3 needed" and the factor 2 between
"4-component" and "2-component" are plausibly the same factor 2** — arising not
from missing physics but from counting in one bundle and taking a kernel in
another.

**E15 (round81) makes this sharp rather than speculative.** It found the S³
Clifford volume element `ω = Z₁Z₂Z₃` is **exactly `I₂`** — because `n=3` is odd,
there is *no* chirality grading on the S³ spinor factor at all. So the
`(2,1)` / `(1,2)` distinction that framework A relies on **cannot be made on the
S³ factor by any Clifford operator.** It lives in `SO(4)`-isometry
representation theory, a structure the Dirac operator `D_{S³,t}` was never built
from.

## Four readings (mode: Контрфактуальный мир — one map element varied)

| # | reading | consequence |
|---|---|---|
| M1 | 1 generation = 1 SU(2) doublet | `6/2 = 3` ✓, but framework A's other doublet is unaccounted for. Round78's "comfortable" answer |
| M2 | a missing mechanism supplies the `(1,2)` | the excess is real physics; keep hunting |
| **M3** | **category error** — A counts fibre *representation content*, B counts the *kernel of an operator on sections*; different objects, no contradiction | C27 dissolves — **but `N_gen=3` must then be re-derived**, because the index argument is B-side and the SM-content argument is A-side |
| M4 | the product-decoupling premise fails for torsion-deformed S³ (row 4) | removes the premise entirely; larger finding |

**M3 is the reading this analysis newly surfaces**, and it is the uncomfortable
one: it does not rescue `N_gen=3`, it questions whether the two halves of the
existing derivation were ever computed in the same bundle.

## Levels (mode: Уровни масштаба) — where the frameworks diverge

| level | framework A | framework B | agree? |
|---|---|---|---|
| fibre | 32 components | 32-dim module | ✓ |
| sections / operator | — (no operator) | `ker D_full` = 6 | **not comparable** |
| 4D spectrum | 1 generation + CPT | 3 generations claimed | **untested link** |

The divergence appears exactly at the level where A has no operator and B has no
representation-content statement. Neither framework covers both.

## Anti-confirmation

- 🔴 **Category error risk** — the whole finding above *is* one, if M3 holds.
- 🟡 **Survivorship** — E15 and G27/G31 closed three projection routes; "only the
  hard ones remain" is expected under M3 too, so their failure is not evidence
  against it.
- 🟡 **Goodhart** — "get 3" has been the target for many rounds; M3 is the branch
  that makes 3 harder to claim, which is precisely why it deserves the test.

## Cheapest differentiating test — ONE

**Are `g24`'s `Spin(4)` spinor bundle and `E2/E9`'s `Cl(0,3)` module the same
bundle on S³, or different ones?** Concretely: does the 4-component `SO(4)`
spinor restrict to `S³` as `2 ⊕ 2` of the *same* `Cl(0,3)` module the Dirac
operator acts on, or as something else?

- Different bundles → **M3**, and `N_gen=3`'s two halves need re-joining.
- Same bundle → M3 dies, M1/M2 survive, and the missing `(1,2)` is real physics.

Cheap, purely representation-theoretic, needs no new machinery, and it is
**differentiating** (the answer changes which branch is alive) and
**non-circular** (it does not assume any generation count).

## What this does NOT establish

1. **C27 is NOT resolved.** Status unchanged: `REFUTED` as stated.
2. Does not show M3 is correct — only that it is available and untested.
3. Does not touch OB4/`C_G67C3`, `t`-selection, or the S⁶ side.
4. The `[INFERRED]` chain above rests on `g24`'s decision.md wording plus E2's
   module definition; it has **not** been verified by an explicit branching
   computation. That computation *is* the cheapest test.
