# decision — C11 step 5: the real structure `J` and the first-order condition

**Verdict:** `AXIOMS_FORCE_ALPHA_BETA_ZERO__BUT_J_KILLS_THE_MAXIMAL_ALGEBRA` → claim **C48**.
**Date:** 2026-08-10 · L0: descriptive · ruff clean · `results_step5.json` persisted.

Two results pulling in opposite directions. Both recorded, neither is allowed to
overshadow the other.

---

## Result 1 — the deformation is killed. `(α,β) = (0,0)` is FORCED.

**`β = 0` by boundedness.** `[β D^{1/2}⊗s1, f⊗m]` expands to
`β([D^{1/2},f]⊗s1m + f·D^{1/2}⊗[s1,m])`. The second term carries the **unbounded** factor
`f·D^{1/2}`, so `[D,a]` is unbounded unless `[s1, m] = 0` for every `m` in the algebra.
Both `T4` and `T7` contain `s3`, and `[s1,s3] ≠ 0`. **`β = 0`.**

This is the same bounded-commutator axiom that step 1 found **completely blind** to the
sector index (because `D^0 − D^1 = −3·Id` is bounded). It becomes **sharp** the moment an
*unbounded* off-diagonal term is switched on. The axiom was never weak — the undeformed
question was simply invisible to it.

**`α = 0` by first-order.** For `A = T7` (sector part `span{I, s3}`), the condition
`α·[[s2,m], m''] = 0` is violated by the pair `[[s2,s3], s3'']` for **every** admissible
`k` (`diag(1,1)`, `diag(1,i)`, `diag(1,−1)`, `s1`, `s2`, `s3`). **`α = 0`.**

**Discrimination check** (the second half of the positive-control gate — run the same test
on the thing that must survive): the *undeformed* first-order condition `[[s3,m], m''] = 0`
**holds** for every one of those `k`. The test kills `α` without killing the undeformed
triple, so it is discriminating, not merely destructive.

**Consequence for C47:** steps 3+4 showed the 4-dim kernel survives at exactly one point
of the deformation family. That point is now the only axiom-compatible one, so the
isolation is a **selection**, not a fragility — the favourable branch, named in advance.

## Result 2 — `J` excludes the MAXIMAL algebra, not the small ones

Step 1's Relaxation Map recorded the hope **V2**: *"first-order could exclude the small
subalgebras and earn the maximal one without an axiom of convenience."* **The opposite
happened.**

| algebra | sector part | order-zero `[m, k m'ᵀk⁻¹] = 0` |
|---|---|---|
| `T4` crossed product | all of `M₂(C)` | **NO `k` works** |
| `T7` twisted diagonal | `span{I, s3}` | 6 of 7 tested `k` work |
| `T6` `A₊⊗I` | `{I}` | all work |

`M₂(C)`'s commutant inside `M₂(C)` is only `C·I`, so an `M₂` bimodule needs a **4-dim**
sector space — i.e. yet **another** doubling. What survives is the twisted diagonal, which
acts **sector-diagonally**.

> **Stated plainly: with `J` imposed, the algebra no longer mixes the sectors at all.**
> So the algebra cannot force the doubling in *any* form. The doubling rests on wanting a
> grading and nothing else — and C44 already showed a grading exists for **every** mirror
> pair. The `t=0/t=1` doubling remains **unearned**, now from three independent
> directions: C44 (grading generic), C45 (no algebra forces it), C48 (`J` makes the
> algebra sector-diagonal).

## Scope boundary, surfaced rather than buried

**`α = 0` is NOT forced for `T6`.** Its sector part is just `{I}`, so `[s2, I] = 0` and no
violation arises. The forcing of `α` needs the algebra to be at least the twisted
diagonal — i.e. to contain an `S³`-worth of functions. `T6` is the degenerate case where
only `ι`-even functions act and the "geometry" is no longer `S³`.

## Sign tuple — computed for the sector factor only, deliberately not combined

With `S³`'s KO-dim 3 inputs declared (`J_M² = −1`, `J_M D_M = D_M J_M`):

| `k` | `j²` | `ε_D` (sector) | `ε_γ` (sector) |
|---|---|---|---|
| `diag(1,1)` | +1 | +1 | +1 |
| `diag(1,−1)` | +1 | +1 | −1 |
| `s1` | +1 | −1 | +1 |
| `s2` | −1 | −1 | −1 |
| `s3` | +1 | +1 | −1 |

**This is NOT a KO-dimension claim.** Only sector-factor signs are computed; combining
them with `S³`'s own tuple is exactly the step C36 showed is easy to get wrong. Left
**OPEN** rather than asserted.

---

## Kill Analysis

**Killed:** step 1's hope V2 (first-order earns the maximal algebra). Also killed: the
off-diagonal deformation, hence any Yukawa-like sector coupling *of this minimal form*.

**Not killed:** C46 (parity doubling) — `T7` *is* the twisted diagonal, so C46's content
survives and is in fact now the whole algebra. C47 stands and is strengthened in meaning.
C42, C43 (amended), C44 untouched.

**Relaxation Map:**

| Variant | Assumption relaxed | Status |
|---|---|---|
| W1 | drop ANSATZ J1 — allow `J` that does not factor as `J_M ⊗ j` | **untested**, the one real escape |
| W2 | accept a 4-dim sector space (another doubling) so `M₂` gets its bimodule | changes the object; would need its own claim |
| W3 | drop `J` entirely — keep an even, non-real spectral triple | legal, but abandons Poincaré duality and the physical interpretation the whole line was for |

W1 is the honest next question if this line is continued. W2 is a warning: "add another
doubling" is exactly the move that would make the construction unfalsifiable.

## What this does NOT show

- **ANSATZ J1**, flagged not assumed: `J = J_M ⊗ j` is a restriction. A general antilinear
  `J` on `H_M ⊗ C²` need not factor, and nothing here rules the non-factoring ones out.
- The `k` search is over 7 representative invertible matrices, **not** a proof over all of
  `GL(2,C)`; the `T4` negative is therefore `[VERIFIED]` for those and `[INFERRED]` in
  general — though the commutant argument (`M₂`'s commutant is `C·I`) is basis-free and
  does hold generally.
- Inherits **ASSUMPTION A1** (`U_ι D^{1/2} U_ι† = −D^{1/2}`) and the KO-dim 3 inputs.
- Says nothing about `N_gen = 3` (step 7, deferred) or Poincaré duality (step 6, whose
  cost is now different: it is defined relative to an algebra that just turned out to be
  sector-diagonal).
