# decision — W1-lift: `A1-lift` is a theorem, not an assumption

**Verdict:** `A1_LIFT_IS_A_THEOREM_NOT_AN_ASSUMPTION__SCHUR_FORCES_BLOCK_PRESERVATION` → **C59**.
**Date:** 2026-08-10 · L0: descriptive · ruff clean · `results_a1lift.json` persisted.

---

## What was flagged

C55 derived A1 from the bare Peter–Weyl pullback and flagged: *"the geometric spinor lift
may differ from the bare pullback by a unitary. The conclusion survives any such factor
that preserves the isotypic decomposition — a much weaker input than A1 itself, but it IS
an input."* Same shape as **W1** (C50: does a non-factorizing `J` reopen anything?) applied
one level earlier — to the **lift itself**, before `J` even enters.

## The argument

`ι(ag) = g⁻¹a⁻¹` is pure group associativity: `ι` intertwines left translation by `a` with
right translation by `a⁻¹`. Any operator `U` implementing `ι` **equivariantly** — which is
what "lift of an isometry" *means*, independent of Clifford sign, metric convention, or
Pin choice — must satisfy that intertwining on each isotypic `(j,k)` block. Since
`V_j ⊗ V_k*` is one irrep per factor of a product group, this forces `U` (by **Schur's
lemma**) to map `(j,k)` **only** to `(k,j)`, unique up to a **phase**.

## Verified, not just cited — and a real bug caught along the way

The equivariance condition was built explicitly from `su(2)` generator matrices and solved
as a linear system (SVD null space), rather than trusting the Lie-algebra bookkeeping by
hand — the same discipline every prior round in this chain used for a lemma name.

**The first version had a real sign bug**, and its diagnosis matters: `dual_generators`
returned `conj(J)` for the contragredient generator. Hand-checking the simplest case
`(j,k)=(0,½)` against explicit Pauli matrices caught it — `conj(J)` alone **flips the sign
of the `su(2)` commutator** (`[conj(Jx),conj(Jy)] = −i·conj(Jz)`, not `+i`), so it is not
even a valid representation on its own. The correct contragredient generator for the
anti-Hermitian Lie-algebra convention is `−conj(J)`. With the fix:

| check | before fix | after fix | expected |
|---|---|---|---|
| **S2** matching pairs, e.g. `(0,½)→(½,0)` | null dim **0** | null dim **1** | 1 |
| **S3** negative control, mismatched same-dim | null dim **0** | null dim **0** | 0 |
| **S4** different-dim sanity | 0 | 0 | 0 |

The bug was caught **before** the verdict was accepted, exactly per this project's own
audit-verification-gate discipline: a numeric result that contradicted a hand-derivable
special case was not written off as "the theory must be more subtle" — it was traced to a
specific, nameable, fixed line.

## Results, all [VERIFIED-numpy]

- **S2** — every matching pair (`(0,½)→(½,0)`, `(½,1)→(1,½)`, `(1,½)→(½,1)`, `(1½,1)→(1,1½)`,
  `(1,1)→(1,1)`) gives **exactly** dimension 1: existence and uniqueness, the two halves of
  Schur's lemma, both checked.
- **S3, the load-bearing negative control** — same total dimension, label **not** swapped
  (`(1,0)→(1,0)`, `(½,1½)→(½,1½)`): dimension **0**. Dimension-matching alone does not force
  a solution — only the label match does. (The `j=k` rows give 1, correctly: when `j=k`,
  `(j,k)` **is** its own correct target `(k,j)`, not a control failure.)
- **S4** — different-dimension pairs: trivially 0, confirming the machinery isn't vacuously
  nonzero everywhere.
- **S5** — applied to C55's own `(0,½)` pair (the `n=0` level): dimension 1. **This is
  exactly the phase freedom C56 exploited** (`c = ±1` or `c = ±i`). C56/C57 are corroborated,
  not contradicted — the freedom they used was always Schur's scalar, nothing more and
  nothing less.

---

## Kill Analysis

**Killed:** ASSUMPTION A1-lift as an open input. It is not a free choice — it is forced by
equivariance, which is definitional for "lift of an isometry."

**Not killed:** nothing upstream. C55–C58 are strengthened, not revised — their reliance on
block-preservation now rests on a proof rather than a named assumption.

**One premise, stated rather than hidden:** the round assumes a genuine geometric lift of
`ι` *is* equivariant in this sense. A linear map that is **not** a lift of the isometry
(i.e., does not intertwine `L_a` with `R_{a⁻¹}`) is mathematically nameable but would not
be implementing `ι` at all — so this is the definition being used, not an extra physical
assumption layered on top.

## What this does NOT show

- Does not re-derive the `V_j^* ⊗ V_{1/2} = V_{j+1/2} ⊕ V_{j−1/2}` Clebsch–Gordan step —
  used as given, exactly as C55 established it.
- Does not address whether a non-equivariant operator could exist mathematically (it can —
  any linear map does) — only that such an operator is not a lift of `ι`.
- Nothing about `N_gen = 3` — closed by C58; untouched here.

## Where this leaves the whole `A1`/`J`/orientability line

C55 derived A1. This round discharges the one input C55 left open. **The `U_ι`-dependent
chain (C50, C51, C53, C54, C57) now rests on zero named assumptions about the lift** — only
on the definition of what a lift of an isometry is, plus the phase freedom (S5) already
correctly used throughout C56–C57.
