# decision — CAVEAT O′: can unbounded commutators cancel?

**Verdict:** `CAVEAT_O_PRIME_DISSOLVED__SPAN_ARGUMENT_IS_IMMUNE_TO_CANCELLATION` →
**C54 REFUTED**. The last technically open door in the C11 line is closed.
**Date:** 2026-08-10 · L0: descriptive · ruff clean · `results_o_prime.json` persisted.

---

## The worry was mine, and it was not empty

C53's own caveat: `J u J⁻¹` could be a **sum** in which a `U_ι` term's unbounded
commutator **cancels** against another unbounded term, and a finite model cannot exclude
it.

**Cancellation is real** [VERIFIED-numpy]:

| operator | `‖[D_M,·]‖` at N=32 | grows? |
|---|---|---|
| `Z₁ = U_ι` | 67.0 | **yes** |
| `Z₂ = I − U_ι` | 67.0 | **yes** |
| `Z₁ + Z₂ = I` | 0.0 | **no** |

Two unbounded commutators, bounded sum. So the caveat was pointing at something that
genuinely happens.

## But it was aimed at a step the proof does not take

The worry presupposes a **decomposition** argument — *split `T` into a `U_ι` part and a
rest, bound each piece*. What orientability actually needs is a **span** argument, and a
span argument is immune to cancellation.

Let `𝔅 := {Z bounded : [D_M, Z] bounded}`.

| step | content |
|---|---|
| **P1** | `𝔅` is a **linear subspace and an algebra** — `[D_M, aZ₁+bZ₂] = a[D_M,Z₁]+b[D_M,Z₂]` and the Leibniz rule, both [VERIFIED-numpy] over 200 random pairs |
| **P2** | `U_ι ∉ 𝔅` — `[D_M, U_ι] = 2 D_M U_ι` holds exactly at every cutoff, with norms `11 → 19 → 35 → 67` |
| **P3** | **every available operator is in `𝔅`** — the `H_M` factors of `a`, of `[D,a]`, and of each block of `J b* J⁻¹` all have non-growing commutators |
| **P4** | so everything reachable lies in `𝔅`, and `U_ι` does not. **`γ` unreachable.** |

> **Cancellation would have to happen *inside* `𝔅`, and a sum of `𝔅`-elements is a
> `𝔅`-element. It can never leave.**

`Z₁ = U_ι` is precisely the operator that is **not available** — not in `A`, not a
`[D,a]`, not a `J b* J⁻¹`. That is the entire content of the resolution.

## Control — is the detector sound, or only tuned to `U_ι`?

The obvious control ("admit `U_ι`, check `γ` returns") is `I @ γ == γ` — true by
construction, the **sixth** cannot-fail check of this session, and a duplicate of C53's
O4. Written out. Replaced by a two-directional soundness test of the `grows` detector:

| test operator | `[D_M,·]` grows? | expected |
|---|---|---|
| level shift `n → n+1` (constant gap) | **False** | False |
| long range `n → 2n` (growing gap) | **True** | True |

So the detector answers correctly for a bounded case that is not the identity and an
unbounded case that is not `U_ι`.

---

## Kill Analysis

**Killed:** C54, and with it CAVEAT O′ — **the last technically open door in the whole
C11 line**. Note the shape: the caveat **dissolved** rather than being defeated. It was a
correct observation about operators aimed at an argument that never decomposes anything.

**What the whole chain now rests on — two named assumptions, both still standing:**

| Assumption | Content | Status |
|---|---|---|
| **A1** | `U_ι D^{1/2} U_ι† = −D^{1/2}` | inherited from C39 + the standard orientation-reversal result; **never re-derived** in this project. **And it is exactly what makes `[D_M,U_ι]` unbounded — so this round depends on it.** |
| **R** | regularity (`[D,[D,a]]` bounded) | needed for `[D,a] ∈ 𝔅`; **not** needed when `B = C·1`, where the `H_M` factor is exactly `I` |

If A1 were false, `U_ι` would commute with `D_M` up to bounded terms, `U_ι` could be in
`𝔅`, and this argument — along with C50, C51, C53 — would need rebuilding. **A1 is the
single load-bearing input of the entire J/orientability chain.** That is worth stating
plainly rather than leaving in a convention field.

## Where C11 stands

The doubling is unearned from four directions (C44, C45, C48+C50+C51, C49), plus an
independent orientability failure (C52) that survives the `A⊗A°` formulation (C53) and now
the cancellation objection (C54). The root is one conflict: **anticommutation demands `ι`;
orientability forbids it.** What survives is **C46** (if taken, it is a *parity* doubling)
and **C47** (the 4-dim kernel is isolated — and C48 made that isolation a *selection*).

## What this does NOT show

- It does **not** show the doubling is wrong — only that nothing in this framework
  requires it.
- Boundedness is operationalised as "norm does not grow with the cutoff";
  `[INFERRED-analytic]` where it stands for a genuine operator-norm statement.
- **ASSUMPTION A1 remains unverified in this project.** The most valuable remaining check
  in this line is not another escape route — it is A1 itself.
- Nothing about `N_gen = 3` — **step 7 remains untouched by agreement.**
