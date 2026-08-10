# Y2 — `A`'s diagonal part smaller than the twisted diagonal

**Experiment id:** `20260810-c11-y2-smaller-diagonal`
**Date:** 2026-08-10 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C50 (W1), C51 (Y1) — the last remaining residual they named

---

## Why this one is different from W1 and Y1

W1 and Y1 both run through **C50's W1a**: `A'`'s sector-off-diagonal blocks must factor
as `m·U_ι`, because they satisfy `T₀₁(f∘ι) = f T₀₁` **for all `f`**. That condition comes
from `A` containing the **full** twisted diagonal.

If `A`'s diagonal part is only a subalgebra `B ⊊ C^∞(S³)`, the condition weakens to
`b ∈ B` only, `A'` gets **bigger**, and it can contain off-diagonal operators that do
**not** carry `U_ι` — those have **bounded** commutator with `D`, so the step that forced
`JuJ⁻¹` sector-diagonal **fails**.

**In the extreme case `B = C·1` this is obvious and total:** `A = span{1⊗I, 1⊗s1} ≅ C⊕C`
is unital, `γ`-even (constants are `ι`-even), closed, and sector-mixing — and `1⊗s1` lies
in its **own** commutant. `[D, 1⊗s1] = −3i(I⊗s2)` is bounded. The entire `J` route
collapses. **So Y2 is not a formality; it is a genuine escape from everything C50/C51
established.** I expect the `J` argument to be unrecoverable here, and say so before
testing.

## The claim under test

> **C52 (proposed).** With a diagonal part smaller than the twisted diagonal, there is an
> admissible `A` — sector-mixing, `γ`-even, with a real structure — that survives all the
> spectral-triple axioms, so the doubling finally has a construction that earns it.

**Falsifier, fixed in advance:** if a *different* axiom — one that does not go through
`J` at all — excludes every such `A`, C52 is **REFUTED** and Y2 closes by a route
independent of the whole C48–C51 chain.

## Predictions, recorded before running

| # | Prediction |
|---|---|
| **Y2a** | with `B = C·1`, `A'` contains sector-off-diagonal elements **not** of the form `m·U_ι`, and their commutator with `D` is **bounded** — so C50's W1a/W1c genuinely fail. **The escape is real.** |
| **Y2b** | but **every** `a ∈ A` and **every** `[D,a]` is a **LOCAL** operator: `g·T·f = 0` whenever `f`, `g` have disjoint supports. `A`'s elements are multiplication operators times constant sector matrices; `[D,f] = c(df)` is a bundle endomorphism; `D` itself is a first-order differential operator. |
| **Y2c** | `γ = U_ι⊗s1` is **NOT local**: `ι` moves points, so for `f` supported near `x` and `g` near `ι(x)` (disjoint, since `ι` has only two fixed points) `g·γ·f ≠ 0`. |
| **Y2d** | therefore `π_D(c) = Σ a⁰[D,a¹][D,a²][D,a³]` is local for **every** Hochschild chain — products of local operators are local — so `π_D(c) ≠ γ`. **The ORIENTABILITY axiom fails, for every admissible `A`, whatever its diagonal part.** |
| **Y2e** | **discrimination:** the obstruction must be caused by `ι`'s non-locality specifically, not by the method. Replacing `U_ι` with a *local* bundle map must remove it. |

**Why this closes more than Y2.** The argument never mentions `B`, `J`, or the size of
`A'`. If it holds it retires Y2, Y1′ and the Lipschitz loophole at once — and it explains
C49: orientability produces the fundamental class, Poincaré duality needs it
non-degenerate, and **both fail for the same underlying reason.**

## The suspicious thing this makes explicit

`γ` is built from a **diffeomorphism**. Every `γ` in an ordinary even spectral triple is
built from the **Clifford algebra** — a bundle endomorphism, local by construction. C43,
C45 and C50 all found `ι` to be load-bearing; this is the bill for that.

## What this cannot show

- **CAVEAT O (the `A⊗A°` formulation).** Some statements of orientability use a Hochschild
  cycle in `Z_n(A, A⊗A°)`, so `π_D` also contains `J a* J⁻¹` factors. Those are local
  **provided** `JAJ⁻¹` is local — which C50/C51 established only when `A` contains the
  twisted diagonal. For a **smaller** `B` that is **not** established, and is an honest
  open sub-point rather than a step I get to assume.
- The finite model tests the **support bookkeeping**. The input `[D,f] = c(df)` (hence a
  bundle endomorphism) is the standard identity, used as `[VERIFIED-analytic]`, not
  re-derived.
- Inherits **ASSUMPTION A1**. Says nothing about `N_gen = 3` — step 7 untouched.
- It does **not** say `S³` is non-orientable. `S³`'s own odd triple is fine; what fails is
  the **doubled even** triple with a diffeomorphism-built `γ`.

## kill_criterion

C52 stands if some Hochschild chain over an admissible `A` has `π_D(c) = γ`, or if a
local `γ` anticommuting with `D_block` exists. Either would break Y2d or Y2e.
