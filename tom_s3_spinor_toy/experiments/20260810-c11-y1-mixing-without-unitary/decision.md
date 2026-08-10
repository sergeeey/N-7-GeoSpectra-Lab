# decision — Y1: a sector-mixing algebra with NO sector-swap unitary

**Verdict:** `Y1_CLOSED__MIXING_WITHOUT_A_UNITARY_IS_ALSO_EXCLUDED` → **C51 REFUTED**,
and **C50 becomes the `f ≡ 1` special case** of a more general argument.
**Date:** 2026-08-10 · L0: descriptive · ruff clean · `results_y1.json` persisted.

---

## The sliver was real, and it had a concrete inhabitant

C50's chain enters at `[D,u] = −3i(I⊗s₂)` for the **swap unitary** `u = 1⊗s1`. An
algebra that mixes sectors without one gives that chain no entry.

`A = ⟨twisted diagonal, x₀⊗s1⟩` is exactly that: `x₀` is `ι`-even, every off-diagonal
element is `G·x₀⊗s1`, and all of them **vanish on the equator** `{x₀ = 0}` — so none is
invertible, hence none is unitary. **C50 does not touch this algebra.**

*(A nowhere-vanishing `f` would not have been a sliver: on the connected `S³` it has
constant sign, `|f|` is smooth, and stability under holomorphic functional calculus puts
`f/|f|⊗s1 = ±u` back in `A`. Y1 is precisely the vanishing-`f` case.)*

## The mechanism — a mass term that only mixing elements get

| element | `[D, ·]` | `|[D,·]|²` |
|---|---|---|
| `f⊗s1` (mixing) | `c(df)⊗s1 − 3i f⊗s2` | `(\|df\|² + **9f²**) ⊗ I` |
| `g⊗s2` (mixing) | `3i g⊗s1 + c(dg)⊗s2` | `(\|dg\|² + **9g²**) ⊗ I` |
| `λ·I⊗I` (diagonal) | `c(dλ)⊗I` | `\|dλ\|² ⊗ I` — **no mass term** |

Both identities [VERIFIED-numpy] exactly over 300 random `(f, df)` each. The asymmetry is
structural: `(3/2)I⊗s3` **commutes** with anything sector-diagonal, so its contribution
survives only for mixing elements.

**The contradiction.** C50's boundedness step forces `J` to send mixing elements to
sector-**diagonal** ones. So `J` would have to carry an operator bounded below onto
`c(dλ)`. On `S³`:

- **mixing side** — `|∇x_i|² = 1 − x_i²`, so `|df|² + 9f² = 1 + 8x_i² ≥ 1` **everywhere**
  [VERIFIED-numpy, closed form matched on 200k samples], for both `f = x₀` (with `s1`) and
  `g = x₁` (with `s2`);
- **diagonal side** — every smooth `λ` on a **compact manifold without boundary** attains
  a maximum, where `dλ = 0`. Verified *at the maximiser* for four `λ`'s:
  `|dλ|² = 7e−70, 5e−140, 2e−32, 2e−214`.

An operator bounded below by 1 cannot be the antiunitary image of one that vanishes.
**C51 is refuted.**

## The random-sampling trap, caught — third of this shape this session

The first version of the compactness check took `min |dλ|²` over **200 000 random points**
and got `5.5e−04` for `λ = x₀`, so the check reported **False for a true statement**.
Reason: `|∇x₀|² = 1 − x₀²` vanishes only at the two poles — a measure-zero set random
sampling never hits. That measured the sampler, not the mathematics.

Replaced by projected gradient **ascent** to the actual maximiser, then evaluating `|dλ|²`
*there* — the theorem checked at the point it is about. The three earlier instances this
session (C47's `atol`, C49's shape-tautology, C50's `W1b` v1/v2) are the same disease in
different costumes; this one is logged as a fourth pearl because the failure mode is now
demonstrably recurrent rather than anecdotal.

## Discrimination — the criterion can fail, and where

`f = x₀²` vanishes to **second order** on the equator: `|df|² + 9f² → 4.3e−11` there,
**not** invertible. So the criterion is not vacuous, and the residual is *exactly*
identified rather than waved at.

**Control:** `f ≡ 1` gives `|df|² + 9f² = 9 > 0` — C50 is the `f ≡ 1` case, so the
generalisation **subsumes** it rather than competing with it.

---

## The cost of the generalisation, stated not hidden

**ASSUMPTION R (regularity)** — `λ` smooth. This is Connes' regularity axiom applied to
`JAJ⁻¹`, and it is **needed here but was NOT needed by C50**, which got `h = ±I` from `h`
being a unitary involution. More reach, one more axiom. Residual: a merely **Lipschitz**
`λ` can have `|dλ| = 1` a.e. (a distance function), evading the critical-point step.

## Kill Analysis

**Killed:** C51; the Y1 sliver for every algebra with at least one mixing element whose
`[D,a]` is invertible — which includes both natural candidates.

**Not killed, and now precisely bounded:**

| Residual | Content | Assessment |
|---|---|---|
| Y1′ | off-diagonal functions **all** vanish to second order at a common point (`f = x₀²` is the model) | the mixing "switches off" to second order at a point; not the crossed product, and not any algebra the portfolio produced |
| Lipschitz | `λ` non-smooth, evading ASSUMPTION R | requires `JAJ⁻¹` to violate Connes' own regularity axiom |
| **Y2** | `A`'s diagonal part smaller than the twisted diagonal (enlarging `A'`) | **untouched here — still open** |

**Upgraded:** C50 from "no `J` for algebras containing a swap unitary" to the `f ≡ 1` case
of "no `J` for algebras containing any mixing element with invertible `[D,a]`".

## What this does NOT show

- Nothing about **Y2**.
- It does **not** show the doubling is wrong — only that nothing here requires it.
- Inherits **ASSUMPTION A1** (`U_ι D^{1/2} U_ι† = −D^{1/2}`), still not re-derived.
- Nothing about `N_gen = 3` — **step 7 remains untouched by agreement.**
