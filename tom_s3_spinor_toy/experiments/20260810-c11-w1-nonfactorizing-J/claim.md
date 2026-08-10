# W1 — does a NON-factorizing `J` readmit a sector-mixing algebra?

**Experiment id:** `20260810-c11-w1-nonfactorizing-J`
**Date:** 2026-08-10 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C45 → C46 → C47 → C48 → C49

---

## Why this is the one question left

Three results say the `t=0/t=1` doubling is unearned — C44 (the grading is generic in
`t`), C45 (no algebra forces it), C48 (`J` makes the algebra sector-diagonal). But **C48
and C49 both rest on ANSATZ J1**, which I flagged when I wrote them:

> `J = J_M ⊗ j` is assumed to be a simple tensor. A general antilinear `J` on
> `H_M ⊗ C²` need not factor, and nothing there rules the non-factoring ones out.

That is escape route **W1**, and it matters because the whole chain hangs on it:

- if a non-factorizing `J` readmits the **crossed product** `C^∞(S³) ⋊_ι Z₂`, then the
  algebra mixes the sectors again, C48's result 2 is an artifact of my own ansatz, **and
  C49's failure of Poincaré duality is lifted too** — the sector-mixing projection
  `p = (1+u)/2` gives index pairing `2`, not `0` (C49 already computed the non-zero
  counter-case);
- if it does not, the no-go becomes **ansatz-free** and the C11 line is closed within
  this framework.

**The ansatz is doing real work and I should assume it is until shown otherwise.** The
natural crossed-product `J` — the Tomita–Takesaki conjugation of the regular
representation — *is* non-factorizing (it carries `U_ι` in one sector block only), and it
satisfies order-zero automatically. So the naive expectation is that W1 **succeeds**.

## The claim under test

> **C50 (proposed).** There is an antiunitary `J` on `H = L²(S³,S) ⊕ L²(S³,S)`, not of
> the form `J_M ⊗ j`, satisfying `J D = ε' D J` and the order-zero condition for a
> **sector-mixing** algebra containing the sector swap `u = 1 ⊗ s1`.

**Falsifier, fixed in advance:** if every such `J` forces `J u J⁻¹` to be sector-diagonal
and that in turn forces a contradiction, C50 is **REFUTED** and W1 closes.

## Predictions, recorded before running

| # | Prediction |
|---|---|
| **W1a** | `A'`'s sector-**off-diagonal** blocks all carry `U_ι` — they satisfy `T₀₁(f∘ι) = f T₀₁`, so `T₀₁ = m·U_ι` with `m` a bundle endomorphism |
| **W1b** | those have **UNBOUNDED** commutator with `D`: `[D_M, m U_ι] = {D_M,m}U_ι = ([D_M,m] + 2m D_M)U_ι`, norm growing like `2(n+3/2)` |
| **W1c** | `[D, u] = −3i(I⊗s2)` is **BOUNDED**, so `[D, JuJ⁻¹] = ε'⁻¹J[D,u]J⁻¹` is bounded, so by W1a+W1b **`JuJ⁻¹` is sector-DIAGONAL**, `= h ⊗ I` |
| **W1d** | then `J(I⊗s2)J⁻¹ ∝ [D_M,h] ⊗ I` must be a **unitary involution**, hence `[D_M,h]` invertible |
| **W1e** | but `[D_M,h]` bounded forces `h` to commute with all Clifford multiplications, hence `h` scalar, hence `h = ±1`, hence `[D_M,h] = 0` — **not invertible. CONTRADICTION.** |
| **W1f** | **discrimination:** the argument must NOT also kill the sector-**diagonal** algebra `T7`, for which step 5 already exhibited a `J`. If it kills that too, it proves too much and is wrong. |

**W1c is the load-bearing step, and it is where the ansatz is not used**: it derives
`JuJ⁻¹`'s sector-diagonality from boundedness alone, never from a factorization
assumption.

## kill_criterion

C50 stands if the finite-model commutant contains a sector-off-diagonal element with
**bounded** commutator with `D`, or if a bundle endomorphism `h` with `[D_M,h]`
**bounded and invertible** exists. Either would break the chain at W1b or W1e.

## What this cannot show

- It concerns algebras containing a sector-**swap unitary** `u` — that is exactly the
  crossed product, the only sector-mixing candidate the portfolio produced. A
  sector-mixing algebra with **no** such unitary is a remaining sliver.
- It assumes `A` contains the full twisted diagonal (true for `T4` by C46/C48); a smaller
  diagonal part would enlarge `A'` and must be treated separately.
- Inherits **ASSUMPTION A1** (`U_ι D^{1/2} U_ι† = −D^{1/2}`).
- Nothing about `N_gen = 3` (step 7, deferred).
