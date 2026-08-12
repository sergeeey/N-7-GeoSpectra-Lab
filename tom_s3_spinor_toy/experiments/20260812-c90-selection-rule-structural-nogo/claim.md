# C90 -- structural no-go for the entire C79-C89 coupling family; verified characterization of the genuine alternative

**Experiment id:** `20260812-c90-selection-rule-structural-nogo`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C86-C89 (per-level joint coupling tests, all clean
NULL). Directed by an external reviewer's proposal: assemble the
per-level tests into one block-tridiagonal Peter-Weyl Dirac matrix
`D_PW` and test truncation convergence as more levels are included.

---

## The claim under test

> **C90.** Before building the reviewer's proposed `D_PW`, check whether
> `T_k` (C86's own coupling construction, `I_q (x) I_p (x) Z_i (x)
> Leibniz(g_i)`) can even in principle define an off-diagonal block
> `T_{k,k+1}` connecting different Peter-Weyl levels. Prediction: it
> cannot, for a structural reason (both `Z_i` and `l_{e_i}` are
> infinitesimal generators of the group's own regular representation,
> and Peter-Weyl levels are exactly that representation's isotypic
> components) -- meaning the literally-proposed `D_PW`, built from the
> existing `T`, would reduce to a direct sum of already-tested,
> non-interacting blocks. Separately: verify, via sympy's own exact
> Clebsch-Gordan class (not hand-derived), whether a genuinely different
> construction (pointwise multiplication by a level-1 matrix-coefficient
> function) is mathematically capable of bridging adjacent levels.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1 (structural)** | `T_k` has no shared index with `T_{k+1}` -- different-dimensional `(p,q)` ranges, `Z_i` acts as identity on `(p,q)` by construction | pending |
| **P2 (CG verification)** | combining level `k` (spin `k/2`) with a level-1 multiplication function (spin `1/2`) gives a nonzero Clebsch-Gordan coefficient to level `k+1`, for `k=1,2,3` | pending |

## kill_criterion

P1 is a structural/dimensional fact, verifiable by direct inspection of
the existing code -- if it turned out `T_k` and `T_{k+1}` DID share a
well-defined index after all, this would refute the "structural no-go"
framing and the reviewer's literal proposal should be built as stated.
P2 is the actual mathematical claim under test for the proposed
alternative -- a zero coefficient would mean even the multiplication-
operator idea fails to bridge levels via this specific mechanism, and a
different alternative would be needed.

## What this cannot show

- Does **not** build a certified, usable multiplication-type coupling
  operator -- only verifies its mathematical basis (nonzero CG
  coefficients) via a standard, already-trusted symbolic library.
- Does **not** run any spectral-flow test on the alternative construction.
- Does **not** claim NO coupling construction could ever bridge levels --
  only that the SPECIFIC family used throughout C79-C89 (built from
  translation generators alone) cannot, for a general, verifiable reason.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
