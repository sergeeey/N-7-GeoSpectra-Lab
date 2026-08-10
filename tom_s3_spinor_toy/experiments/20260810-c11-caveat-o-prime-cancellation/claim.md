# CAVEAT O′ — can unbounded commutators cancel and let `U_ι` back in?

**Experiment id:** `20260810-c11-caveat-o-prime-cancellation`
**Date:** 2026-08-10 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessor:** C53 — the last open door in the whole C11 line

---

## The worry, as I stated it

C53 concluded `JAJ⁻¹` is `U_ι`-free because `[D_M, m'U_ι] = {D_M,m'}U_ι` is order one.
The caveat I recorded against my own result:

> `J u J⁻¹` could be a **sum** in which a `U_ι` term's unbounded commutator **cancels**
> against another unbounded term. A finite model has no unbounded operators and cannot
> exclude it.

**And cancellation is genuinely possible.** `Z₁ = U_ι` and `Z₂ = I − U_ι` both have
unbounded `[D_M,·]`, yet `Z₁ + Z₂ = I` has `[D_M, I] = 0`. So the worry was not silly.

## What I now think the worry got wrong

It presupposes a **decomposition-based** argument — "split `T` into a `U_ι` part and a
rest, then bound each piece." But the argument orientability actually needs is
**span-based**, and a span argument is immune to cancellation:

Let `𝔅 := {Z bounded : [D_M, Z] bounded}`. Then

1. `𝔅` is a **linear subspace** (and an algebra): `[D_M, aZ₁+bZ₂] = a[D_M,Z₁]+b[D_M,Z₂]`
   and `[D_M, Z₁Z₂] = [D_M,Z₁]Z₂ + Z₁[D_M,Z₂]`.
2. `U_ι ∉ 𝔅`: `U_ι D_M = −D_M U_ι` gives `[D_M, U_ι] = 2 D_M U_ι`, **unbounded**.
3. **Every available operator is individually in `𝔅`** — algebra elements by the
   bounded-commutator axiom, `[D,a]` by regularity, `J b* J⁻¹` blockwise because
   `[D, Jb*J⁻¹]` is bounded.
4. So everything reachable lies in `𝔅`, and `U_ι` does not. **`γ` is unreachable, and no
   cancellation can help — because any cancellation happens *inside* `𝔅`.**

`Z₁ = U_ι` is exactly the operator that is **not available**: it is not in `A`, not a
`[D,a]`, and not a `Jb*J⁻¹`. That is the whole content.

## The claim under test

> **C54 (proposed).** A cancellation between unbounded commutators can put `U_ι` into the
> span of available operators, so `γ = π_D(c)` is reachable after all and orientability is
> repaired.

**Falsifier, fixed in advance:** if `𝔅` is a linear subspace, every available operator is
in it, and `U_ι` is not, C54 is **REFUTED** — and CAVEAT O′ *dissolves* rather than being
defeated, because it was aimed at an argument the proof does not use.

## Predictions, recorded before running

| # | Prediction |
|---|---|
| **P1** | `𝔅` is closed under linear combinations **and** products — the Leibniz identities hold exactly |
| **P2** | `[D_M, U_ι] = 2 D_M U_ι` exactly, with norm growing linearly in the cutoff — so `U_ι ∉ 𝔅` |
| **P3** | every available operator is in `𝔅`: `a`, `[D,a]`, and each block of `J b* J⁻¹` |
| **P4** | therefore `span`/products of available operators ⊆ `𝔅` ∌ `U_ι`: `γ` unreachable, **cancellation irrelevant** |
| **P5** | **discriminator:** cancellation IS real — exhibit `Z₁, Z₂` with unbounded commutators and bounded sum. The caveat was not silly; it just aimed at the wrong step. `Z₁ = U_ι` is precisely the *unavailable* operator. |

**P5 is what keeps this honest.** Without it the verdict would read as "the worry was
always empty", which is false.

## Assumptions used, named

- **ASSUMPTION R (regularity)** — needed for `[D,a] ∈ 𝔅` (i.e. `[D,[D,a]]` bounded).
  Already named in C51. In the `B = C·1` case it is **not** needed: there `[D,a]` has
  `H_M`-factor exactly `I` (C53's O3), which is in `𝔅` trivially.
- **ASSUMPTION A1** (`U_ι D^{1/2} U_ι† = −D^{1/2}`), inherited, still not re-derived —
  and note it is precisely what makes `[D_M,U_ι]` unbounded, so this step depends on it.

## What this cannot show

- Boundedness is operationalised in a truncated model as "the norm does not grow with the
  cutoff". That is the standard idiom of this series (C50/C51/C53) and is
  `[INFERRED-analytic]` where it stands for a genuine operator-norm statement.
- Nothing about `N_gen = 3` — step 7 untouched by agreement.

## kill_criterion

C54 stands if some available operator has an unbounded `[D,·]`, or if `𝔅` fails to be a
linear subspace, or if `[D_M,U_ι]` turns out bounded.
