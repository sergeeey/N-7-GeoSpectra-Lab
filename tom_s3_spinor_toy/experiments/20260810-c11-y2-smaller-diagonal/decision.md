# decision — Y2: smaller diagonal part, and the locality obstruction

**Verdict:** `Y2_CLOSED__ORIENTABILITY_FAILS_BY_LOCALITY_FOR_EVERY_ADMISSIBLE_A` → **C52
REFUTED**, by a route that owes nothing to the C48–C51 chain.
**Date:** 2026-08-10 · L0: descriptive · ruff clean · `results_y2.json` persisted.

---

## Y2 really is an escape from the `J` argument — confirmed, as predicted

With `B = C·1`, `A = span{1⊗I, 1⊗s1} ≅ C⊕C` is unital, `γ`-even, closed and
sector-mixing. In the 16-dimensional model `dim A' = 128`; `u = 1⊗s1` lies in **its own
commutant**; its off-diagonal block does **not** factor as `m·U_ι`; and `[D,u] =
−3i(I⊗s2)` is bounded. **C50's W1a and W1c simply do not apply.** That was recorded in
`claim.md` as the expectation before running, and it held.

## A different axiom closes it

| step | content |
|---|---|
| **Y2b** | every `a ∈ A` and every `[D,a]` is **LOCAL** (`g·T·f = 0` for disjoint supports). `A`'s symbols are multiplication × constant sector matrix; `[D,f] = c(df)` is a bundle endomorphism. |
| **Y2c** | `γ = U_ι⊗s1` is **NOT** local. Witness: `‖1_c · γ · 1_{c'}‖ = 2.0` for the free orbit `c ↔ c' = ι(c)`. `ι`'s fixed set in the model is `{a,b}` — two points, exactly as `ι(g)=g⁻¹` on `S³` fixes only `±1` — so disjoint pairs `(x, ι x)` exist. |
| **Y2d** | **closure lemma:** 400 random chains of local factors → `π_D(c)` local, in every case. So `π_D(c) ≠ γ` for **every** Hochschild chain. **ORIENTABILITY FAILS.** |

> **C52 is REFUTED.** No Hochschild cycle over a **local** algebra can produce a
> **non-local** `γ`. The argument never mentions `B`, `J`, or the size of `A'`.

## The check that could actually fail

The obvious version — "count how many random chains equal `γ`" — is 0 by genericity and
would confirm nothing (the fourth instance of that disease this session, so it was
written out rather than committed). Replaced by:

- **closure lemma:** local factors → local product (400/400);
- **counter-case:** smuggle **one** `U_ι` factor into the same chains → **400/400 become
  non-local**, so the lemma can fail;
- and with `U_ι` admitted, `γ` is reachable **exactly** (`a⁰ = U_ι⊗s1`).

So the obstruction is precisely that `U_ι ∉ A`, not that `γ` is a hard target.

## Discrimination — is this about `ι`, or about the method?

Replacing `U_ι` with a **local** bundle map (identity, a sign field, a random bundle
endomorphism) makes `γ` local every time — the obstruction disappears. And the odd-case
target `1` is local. **The obstruction fires only on a `γ` built from a diffeomorphism.**

*(Those local replacements do **not** anticommute with `D_block` — that is C45's result,
and it is exactly why the construction needed a diffeomorphism in the first place. The two
requirements are in direct conflict: anticommutation demands `ι`, orientability forbids
it.)*

## What this makes explicit

`γ` here is built from a **diffeomorphism**. Every `γ` in an ordinary even spectral triple
is built from the **Clifford algebra** — a bundle endomorphism, local by construction.
C43, C45 and C50 each found `ι` load-bearing. **This is the bill for that.**

It also **explains C49**: orientability produces the fundamental class, Poincaré duality
needs that class non-degenerate, and both fail for the same underlying reason.

---

## Kill Analysis

**Killed:** C52; and, because the argument is independent of `B`, `J` and `A'`, it retires
**Y2, Y1′ and the Lipschitz loophole together**. The C11 doubled-even-triple construction
has no remaining escape route inside this framework.

**Not killed:**
- `S³`'s own **odd** triple — it has no `γ` and needs `π_D(c) = 1`, which is local. This
  argument does **not** say `S³` is non-orientable.
- C46 (parity doubling) and C47 (isolated kernel, made a selection by C48) — both stand.
- **CAVEAT O**, below, which is a genuine open sub-point rather than a formality.

**CAVEAT O — the `A⊗A°` formulation.** Some statements of orientability use a cycle in
`Z_n(A, A⊗A°)`, so `π_D` also carries `J a* J⁻¹` factors. Those are local **provided**
`JAJ⁻¹` is local — which C50/C51 established only when `A` contains the twisted diagonal.
For a **smaller** `B` that is **not** established. Stated, not assumed.

**Relaxation Map:**

| Variant | Assumption relaxed | Assessment |
|---|---|---|
| Z1 | the `A⊗A°` orientability formulation with a non-local `JAJ⁻¹` (CAVEAT O) | the only technically open door; needs `JAJ⁻¹` non-local, and C50's boundedness argument pushes against it whenever `A` is large enough to see `S³` |
| Z2 | drop orientability as a requirement | then the object is not a noncommutative *manifold*; combined with C49 (PD fails) the remaining structure is an algebra with an operator, not a geometry |
| Z3 | find a **local** `γ` anticommuting with `D_block` | **excluded by C45** — both factors of `U_ι⊗s1` are needed |

## What this does NOT show

- It does **not** show the doubling is wrong — only that nothing in this framework
  requires it, and that the even triple it would need is not a geometry.
- The finite model tests the **support bookkeeping**; `[D,f] = c(df)` is used as
  `[VERIFIED-analytic]`, not re-derived. The spinor part of the `ι`-lift is trivial in the
  toy, which does not affect locality.
- Inherits **ASSUMPTION A1** (`U_ι D^{1/2} U_ι† = −D^{1/2}`), still not re-derived.
- Says nothing about `N_gen = 3` — **step 7 remains untouched by agreement.**
