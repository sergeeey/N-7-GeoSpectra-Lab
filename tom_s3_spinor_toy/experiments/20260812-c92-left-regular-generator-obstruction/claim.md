# C92 -- does the naive left-multiplication analog of l_{e_i} exist as a complex-linear (k+1)-dim matrix?

**Experiment id:** `20260812-c92-left-regular-generator-obstruction`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C90 (named the multiplication-operator as the viable
level-bridging alternative), task #59 groundwork (confirmed `p` is the
standard magnetic quantum number `m=p-k/2` from C85's `l1` diagonal
eigenvalues). This round is the first concrete step toward certifying a
`q`-side generator (the "left-regular-representation" analog of Meier's
`l_{e_i}`, needed before the multiplication operator itself can be
built), scoped explicitly as substantial, not-to-be-rushed work.

---

## The question under test

> **C92.** C85's `right_mult_matrix_on_ab(unit)` extracts a 2x2
> complex-linear matrix for RIGHT quaternion multiplication by `unit`,
> acting on a quaternion parametrized as `(a,b)` complex pair (via
> `hamilton_product(q, unit)`, differentiated in the real coordinates of
> `q`, with an explicit complex-linearity check built in). The most
> natural candidate for a `q`-side ("left translation") generator is the
> same construction with the product order swapped: `hamilton_product(unit,
> q)` -- LEFT multiplication by `unit`. Does this candidate satisfy the
> SAME complex-linearity property (in the SAME `(a,b)` encoding), for all
> three quaternion units `e1(i), e2(j), e3(k)`?

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1** | `e1(i)`: C-linear (since `i` commutes with itself, left and right multiplication by `i` coincide with plain scalar multiplication in this encoding) | pending |
| **P2** | `e2(j)`, `e3(k)`: NOT C-linear in this same encoding (quaternions are a one-sided complex vector space -- the `(a,b)` parametrization's complex structure is built to make RIGHT multiplication linear; `i` does not commute with `j` or `k`, so LEFT multiplication by them should break that same linearity) | pending |

## kill_criterion

If P2 is wrong (left-mult by `j` or `k` IS C-linear in this encoding
too), that would be a genuinely useful, unexpected simplification for
building the `q`-side generator directly by symmetry with `l_{e_i}` --
worth pursuing immediately. If P2 holds as predicted, it rules out the
naive "same construction, swapped product order" approach and requires
a different strategy (the opposite-handed complex structure, an
explicitly anti-linear/conjugate-linear treatment for `j,k`, or -- more
likely -- reading Meier's own definition of the multiplicity index
directly, which this project does not have primary-source access to
this session).

## What this cannot show

- Does **not** construct a working `q`-side generator, for any unit.
- Does **not** determine what `q` actually IS in Meier's own
  construction (C86's own docstring calls it "a trivial multiplicity
  label," not committing to a specific group-theoretic role) -- this
  round only tests one specific hypothesis about what it might be.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
