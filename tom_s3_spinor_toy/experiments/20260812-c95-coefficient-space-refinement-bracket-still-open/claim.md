# C95 -- coefficient-space correction to C94's generators; bracket inconsistency persists on BOTH sides

**Experiment id:** `20260812-c95-coefficient-space-refinement-bracket-still-open`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C94 (group-action certification found `+l_{e_i}^T`
left / `-l_{e_i}^T` right, but a bracket-consistency check on the left
candidate failed and 3 resolution attempts within that round did not
succeed).

**Scope note:** this is NOT the reviewer's own proposed "C95"
(double-Clebsch-Gordan multiplication-operator certification) -- that
remains explicitly gated closed per C94's decision.md. This round works
ON the blocker itself (C94's unresolved P3), which the gate permits and
the reviewer's own instruction implies is the required next step before
anything past the gate can proceed.

---

## What prompted this round

While reasoning about how to resolve C94's P3 puzzle, validated my own
differentiation *technique* against a textbook-unambiguous case (the
adjoint representation, `d(Ad)(X)(Y)=[X,Y]`) -- technique confirmed
correct. Reapplying it carefully to the `L_h`/`R_h` case by hand found a
likely source: C94's `Y_i` was computed as "how `g0`'s own raw matrix
entries transform," which is NOT the same object as "how the abstract
function space's coefficients transform" -- these differ by a
transpose, a classic function-vs-coefficient contragredience subtlety.
A first hand attempt at applying this correction produced a
self-contradiction on the right-translation side, so this round redoes
the ENTIRE derivation via direct sympy symbolic substitution and
coefficient extraction, with NO manual index-tracking at any step, to
eliminate that specific class of error.

## The claim under test

> **C95.** Represent a generic linear function on `SU(2)` as
> `F = sum_{m,n} c_{m,n} g_{m,n}` (`g_{m,n}` treated as 4 independent
> symbols, matching C85's own convention). Substitute `g -> h(eps)^{-1}
> g` (left) or `g -> g h(eps)` (right), re-expand in the SAME `g_{m,n}`
> monomial basis via sympy's own polynomial coefficient extraction (not
> hand comparison), differentiate the new coefficients at `eps=0`. This
> gives the генuine coefficient-space generator, free of the row/column
> vs operator-index conflation found in C94.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1** | the coefficient-space LEFT generator equals `+l_{e_i}(1)` directly (no transpose), matching a hand re-derivation done while scoping this round (not fully trusted, hence this symbolic re-check) | pending |
| **P2** | the coefficient-space RIGHT generator equals `-l_{e_i}(1)` directly | pending |
| **P3 (bracket check, carried over from C94)** | does EITHER corrected candidate now satisfy `[X1,X2]=2X3` for its own normalization? | pending |

## kill_criterion

If P1 or P2 fails to match the hand-predicted form, the hand
re-derivation done while scoping this round was itself wrong (unhelpful,
but informative -- would mean a 4th independent hand-derivation attempt
produced a 4th inconsistent answer, a strong signal to stop entirely).
If P1/P2 hold but P3 still fails for both, this confirms the bracket
inconsistency is not an artifact of C94's specific row/column
convention -- it is a deeper, unresolved fact about this construction
that needs literature consultation or a completely different approach,
not further hand or symbolic re-derivation this session.

## What this cannot show

- Does **not** resolve the P3 bracket inconsistency even if found to
  persist under the corrected convention -- this round's purpose is to
  rule out ONE specific candidate source of the discrepancy (the
  row/column-vs-operator conflation), not to guarantee a resolution.
- Does **not** unblock C95/C96 in the reviewer's own sequence (the
  multiplication-operator build and spectral-flow experiment) -- that
  gate stays closed regardless of this round's outcome, pending an
  actual resolution or literature consultation.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
