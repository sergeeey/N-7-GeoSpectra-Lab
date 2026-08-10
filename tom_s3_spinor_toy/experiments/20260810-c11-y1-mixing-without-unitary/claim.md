# Y1 — a sector-mixing algebra with NO sector-swap unitary

**Experiment id:** `20260810-c11-y1-mixing-without-unitary`
**Date:** 2026-08-10 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessor:** C50 (W1) — which closed the escape *only* for algebras containing `u = 1⊗s1`

---

## Why this is a real sliver and not a formality

C50's chain enters at **W1c**, through `[D, u] = −3i(I⊗s₂)` for the sector-**swap unitary**
`u = 1⊗s1`. If `A` is sector-mixing but contains no such unitary, the chain has no
entry point and C50 says nothing.

**Such an algebra exists and is easy to write down.** By C46 the `γ`-even off-diagonal
symbols are `f_even⊗s1` and `g_odd⊗s2`. Take `f = x₀` — the first quaternion coordinate,
`ι`-even since `ι:(x₀,x) → (x₀,−x)`. Then `A = ⟨twisted diagonal, x₀⊗s1⟩` is
sector-mixing, and **every element of its off-diagonal part is `G·x₀ ⊗ s1`, which
vanishes on the equator `{x₀ = 0}`** — so no element of it is invertible, hence none is
unitary. C50 does not touch this algebra.

*(Why a non-vanishing `f` would not be a sliver at all: if `f` were nowhere zero on the
connected `S³` it has constant sign, `|f|` is smooth, and stability under holomorphic
functional calculus puts `f/|f| ⊗ s1 = ±u` back in `A`. So Y1 is exactly the
**vanishing-`f`** case.)*

## The claim under test

> **C51 (proposed).** There is a sector-mixing algebra `A` containing no sector-swap
> unitary, together with an antiunitary `J` satisfying `JD = ε'DJ`, order-zero and
> first-order.

**Falsifier, fixed in advance:** if `[D,a]` is boundedly invertible for some mixing
`a ∈ A`, and that forces the same contradiction C50 reached, C51 is **REFUTED** and Y1
closes — with C50 becoming a special case rather than the general result.

## Predictions, recorded before running

| # | Prediction |
|---|---|
| **Y1a** | for `a = f⊗s1` (`f` real, `ι`-even) the identity `([D,a])*[D,a] = (\|df\|² + 9f²) ⊗ I` holds **exactly**; same for `g⊗s2` with `g` `ι`-odd |
| **Y1b** | hence `[D,a]` is boundedly invertible iff `f` and `df` never vanish **together** — which does **not** require `f ≠ 0`. So a NON-unitary mixing element can still have invertible `[D,a]`, and C50's chain reruns with *invertible* in place of *unitary* |
| **Y1c** | the chain then gives `[D_M, h]` invertible with `h = λ·I`; but `[D, h⊗I] = [D_M,h]⊗I` has **no mass term** — the torsion `(3/2)I⊗s3` commutes with anything sector-diagonal — so `\|[D,h⊗I]\|² = \|dλ\|²`, and on the **compact** `S³` every smooth `λ` has a critical point. `c(dλ)` vanishes there. **NOT invertible. CONTRADICTION.** |
| **Y1d** | the natural candidates clear the bar: on `S³`, `\|∇x_i\|² = 1 − x_i²`, so `\|df\|² + 9f² = 1 + 8x_i² ≥ 1 > 0` for both `f = x₀` (with `s1`) and `g = x₁` (with `s2`) |
| **Y1e** | neither candidate algebra contains a swap unitary — every off-diagonal element vanishes on a 2-sphere |
| **Y1f** | **discrimination:** the criterion must be able to FAIL. `f = x₀²` vanishes to second order on the equator, giving `\|df\|² + 9f² = 0` there — so the residual sliver is real and is exactly identified, not hand-waved |

**The mechanism, stated in one line so it can be checked rather than admired:** the
torsion shift gives every sector-**mixing** element a mass term `9f²` in `|[D,a]|²` and
gives sector-**diagonal** elements **none**. `J` must send mixing to diagonal (C50's
boundedness step). So `J` would have to turn an everywhere-invertible operator into one
that must vanish somewhere. On a compact manifold that is impossible.

## Assumptions used, named

- **ASSUMPTION R (regularity).** `λ` is smooth. This is Connes' regularity axiom applied
  to `JAJ⁻¹`, and it is **needed here but was NOT needed by C50**, whose special case
  concluded `h = ±I` from `h` being a unitary involution. Named because it is a genuine
  cost of the generalisation. Residual: a merely **Lipschitz** `λ` can have `|dλ| = 1`
  a.e. (a distance function), which would evade the critical-point step.
- **ASSUMPTION A1** (`U_ι D^{1/2} U_ι† = −D^{1/2}`), inherited, still not re-derived.
- `A ⊇` the full twisted diagonal. A smaller diagonal part is **Y2**, still separate.

## kill_criterion

C51 stands if some sector-mixing `A` has **every** mixing element with `[D,a]` non-
invertible, i.e. all its off-diagonal functions vanish to second order at a common point.
Otherwise Y1 closes and C50 is subsumed.

## What this cannot show

- Nothing about **Y2** (diagonal part smaller than the twisted diagonal).
- Nothing about `N_gen = 3` — step 7 remains untouched by agreement.
