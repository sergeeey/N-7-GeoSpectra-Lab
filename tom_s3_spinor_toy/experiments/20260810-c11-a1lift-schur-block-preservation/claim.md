# W1-lift — is `A1-lift` an assumption, or a theorem? (Schur's lemma on `SU(2)×SU(2)`)

**Experiment id:** `20260810-c11-a1lift-schur-block-preservation`
**Date:** 2026-08-10 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessor:** C55 (A1 derived), which explicitly flagged **ASSUMPTION A1-lift** as the
one input it did not discharge

---

## What was flagged, and why "W1" is the right template for it

C55 derived A1 (`ι` flips `D`) from the bare Peter–Weyl pullback, then flagged:

> *"ASSUMPTION A1-lift, not discharged: the geometric spinor lift may differ from the bare
> pullback by a unitary. The conclusion survives any such factor that preserves the isotypic
> decomposition — a much weaker input than A1 itself, but it IS an input."*

This is structurally the same shape as **W1** (C50): there, the worry was *"a non-factorizing
`J` might do something the factorizing ansatz couldn't."* Here the worry is *"a
non-block-preserving lift of `U_ι` might do something the block-preserving one couldn't."*
**W1's answer was that the naive escape does not exist — boundedness alone forces it.** The
natural next question, following the same discipline, is whether **A1-lift** is similarly
forced rather than merely assumed.

## The claim under test

> **C59.** Any unitary `U` implementing `ι` **equivariantly** — i.e. satisfying
> `U ∘ π(L_a) = π(R_{a^{-1}}) ∘ U` for all `a ∈ SU(2)`, which is the group-theoretic identity
> `ι∘L_a = R_{a^{-1}}∘ι` (immediate from `ι(ag) = g^{-1}a^{-1}`, associativity alone — no
> convention, no Clifford sign, no metric choice) — is **forced** to map the `(j,k)` isotypic
> block **only** to `(k,j)`, and is **unique on that block up to a phase**. Any genuine
> geometric/Pin-group lift of the isometry `ι` must be equivariant in this sense, because
> equivariance is what "lift of `ι`" *means*.

**Falsifier, fixed in advance:** if the linear equivariance constraint, solved explicitly on
finite `(j,k)` blocks, has a **nonzero** solution space between blocks `(j,k)` and any
`(j',k') ≠ (k,j)`, C59 is refuted and A1-lift remains a genuine, undischarged assumption.

## The argument, stated in prose before being coded (Structure-Bias Guard)

Write `X = ι(g)`. The identity `ι(ag) = g^{-1}a^{-1}` means `ι` intertwines **left**
translation by `a` with **right** translation by `a^{-1}`. Define the *twisted* action of
`(a,b) ∈ SU(2)×SU(2)` on the `(j,k)` block (`V_j` under left, `V_k^*` under right) by
`(a,b)·v := [\text{plain }(a,b)\text{ action}](b,a)·v` — i.e. swap which factor sees which
group element. Because `V_j ⊗ V_k^*` is built from **one irrep on each factor of a product
group**, the *twisted* `(j,k)` representation is, as an abstract `SU(2)×SU(2)`-module,
**identical** to the *plain* `(k,j)` representation — a relabelling, not a new object.

So *"`U` intertwines the twisted-`(j,k)` action with the plain-`(k,j)` action"* is exactly
*"`U` is a plain `SU(2)×SU(2)`-equivariant map between the (now identically-labelled)
`(k,j)` representation and itself."* Two standard, convention-independent facts finish it:

1. `V_j ⊗ V_k^*` (one irrep per factor of a product group) is **irreducible**, and two such
   tensor irreps are equivalent **iff** both labels match.
2. **Schur's lemma:** an equivariant map between inequivalent irreps is **zero**; an
   equivariant self-map of an irrep (compact group, over `C`) is a **scalar**.

Applied: `U` between twisted-`(j,k)` and plain-`(j',k')` is an equivariant map between
`(k,j)` and `(j',k')`. If `(j',k') ≠ (k,j)`: **zero**. If `(j',k') = (k,j)`: a **scalar**,
i.e. — since `U` is required unitary — a **phase**.

**Nothing here depends on the fiber convention, the Clifford sign, or the specific Pin
lift chosen.** It depends only on group associativity and Schur's lemma.

## Predictions, recorded before running

| # | Prediction |
|---|---|
| **S1** | the equivariance constraint, built from the `su(2)⊕su(2)` generators (6 real directions), is a **linear** system in `U`'s entries — solvable by null-space/SVD, not requiring group-element sampling |
| **S2** | for the **matching** pair (twisted-`(j,k)` vs plain-`(k,j)`), the solution space is **exactly 1 complex-dimensional** — existence AND uniqueness, the two halves of Schur's lemma, both checked |
| **S3** | for a **same-total-dimension mismatch** (twisted-`(j,k)` vs plain-`(j,k)` itself, *not* swapped — same dimension, wrong label) the solution space is **exactly 0** — this is the load-bearing negative control: dimension-matching alone does *not* force a solution; only the *label* match does |
| **S4** | for a **different-dimension** pair, the solution space is trivially `0` — a basic sanity check that the machinery is not vacuously returning nonzero everywhere |
| **S5** | the phase freedom found in S2 is exactly the freedom C56/C57 already used (`c`, `k` in their notation) — this round should **not** contradict C56/C57, only explain *why* that freedom was there and *nothing more* was |

## What this cannot show

- It does not re-derive the fiber/spin-1/2 Clebsch–Gordan step that produces `k = j±1/2`
  from `V_j^* ⊗ V_{1/2}` — that is **used as given**, exactly as C55 established it
  (`[VERIFIED-sympy]` there), not re-verified here.
- It does not address whether a **non-equivariant** operator could exist mathematically —
  it can (any linear map at all) — only that such an operator would **not** be a genuine
  lift of the isometry `ι`, by the standard meaning of "lift." This is stated as the
  round's one real premise, not hidden.
- Nothing about `N_gen = 3` — closed by C58; untouched here.

## kill_criterion

C59 fails if S2 gives dimension `≠ 1`, or if S3/S4 give dimension `> 0`.
