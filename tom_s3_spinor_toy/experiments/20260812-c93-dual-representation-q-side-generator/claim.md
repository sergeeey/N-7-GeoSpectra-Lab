# C93 -- does the dual/contragredient representation give a valid q-side generator?

**Experiment id:** `20260812-c93-dual-representation-q-side-generator`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C92 (falsified the naive "swap quaternion-multiplication
order" hypothesis for the `q`-side generator, for `e2(j)`, `e3(k)`).

---

## Scoping note: why C92's approach and this round's approach are NOT the same test

While scoping this round, worked out precisely why C92's quaternion-
multiplication approach hit an obstruction, and why it does not
contradict the approach tested here (both were candidates named in
C92's own "next steps," initially treated as competing -- they are not).

C92 tested LEFT multiplication of the raw `(aw,ax,bw,bx)` quaternion
4-tuple. For `k=1`, this 4-tuple's `(a,b)` pair is literally the FIRST
ROW of the group element's own `2x2` matrix `g=[[a,b],[-conj(b),conj(a)]]`
(a defining-representation, `SU(2)`-specific object). The matrix's SECOND
row is `(-conj(b),conj(a))` -- algebraically tied to the first row by
the unitarity constraint, i.e. by COMPLEX CONJUGATION. Left-multiplying
`g` by a generator necessarily mixes row 1 with row 2, which means it
necessarily mixes `(a,b)` with `(conj(a),conj(b))` -- this IS the
antilinear residual C92 found, not a separate phenomenon. The row/column
matrix-entry picture is inescapably antilinear for left translation,
for the STRUCTURAL reason that unitarity ties rows together via
conjugation.

The ABSTRACT Peter-Weyl decomposition `L^2(G) = V_j (x) V_j*` avoids
this entirely: `V_j*` (the index `q` lives on) is the FORMAL DUAL vector
space, not "the conjugate of `V_j`'s literal matrix rows" -- its
representation is the CONTRAGREDIENT representation, with Lie algebra
generators `sigma(X) = -rho(X)^T` (a standard, purely LINEAR
construction -- transpose and negation, no conjugation anywhere). This
round tests THIS construction instead of C92's.

## The claim under test

> **C93.** For Meier's certified `l_{e_i}(k)` (round `p`'s generator,
> `C85`), does `L_i := -l_{e_i}(k)^T` define a genuine representation of
> `su(2)` -- i.e. does it satisfy `[L1,L2]=2*L3` (cyclic), the SAME
> bracket normalization `l_{e_i}` itself satisfies -- for general `k`,
> not just `k=1`?

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1** | `[L1,L2]=2L3` (cyclic) holds exactly, for `k=1..5` (a standard fact about dual representations, `sigma([X,Y])=-rho([X,Y])^T=[sigma(X),sigma(Y)]` -- re-derived and checked here directly, not assumed from memory) | pending |
| **P2** | `L_i` is genuinely distinct from `l_{e_i}` and `-l_{e_i}` (not a trivial sign relationship) | pending |
| **P3 (exploratory, not predicted in advance)** | is `L_i` anti-Hermitian (the property needed for a genuine unitary-group generator)? | pending |

## kill_criterion

If P1 fails for any tested `k`, the dual-representation construction is
wrong (a sign or transpose-convention error somewhere) and this
candidate is dead. P2 failing would mean the construction is trivial/
uninteresting. P3 is exploratory -- its outcome (either way) narrows,
not kills, the candidate; a `k`-dependent Hermiticity pattern would need
to be checked against this project's ALREADY-KNOWN finding (C87/C88:
`l_{e_i}`-built `D-bar` itself is only exactly Hermitian at `k=1`) before
being treated as a NEW problem.

## What this cannot show

- Does **not** prove `L_i` is the CORRECT/PHYSICALLY MEANINGFUL q-side
  generator for Meier's own specific construction -- only that it is A
  valid `su(2)` representation, abstractly.
- Does **not** verify the combined `(q,p)` system actually transforms as
  a genuine Peter-Weyl `V_j (x) V_j*` bimodule under the FULL `G x G`
  action (would need checking the Casimir / full `so(4)` structure of
  `L_i` and `R_i=l_{e_i}` acting together, not attempted here).
- Does **not** build or test any coupling/multiplication operator.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
