# C115 claim -- third matched-diagonal cell (j1=j2=2) as a third data
point for C114's own open mechanism question, plus a properly-formalized
attempt at the anti-Hermitian diagnostic C114 had to abandon (dimension
bug) rather than repeating that mistake

## L0 gate (EstimandOps)

**Question type:** Descriptive.

## Background

C114 found: at both tested matched-diagonal cells `(1,1)` and
`(3/2,3/2)`, specific proper subsets of the summed coupling components
break reality even though the full sum does not. Two candidate
mechanism rules were checked directly against the data and BOTH
refuted: `|a|=j2 AND |b|=j2` fits `(1,1)` perfectly (9/9) but only half
of `(3/2,3/2)` (8/16); an a-vs-b-asymmetric refinement fits `(3/2,3/2)`
but fails on `(1,1)`'s own `(0,1)` case. `pearl_registry/INDEX.md`'s
C114 row named two next steps: a third matched cell for a third data
point, and a correctly-formalized anti-Hermitian-projection diagnostic
(C114's own first attempt hit a real dimension mismatch -- `M_ab` is a
rectangular `dim_target^2 x dim_source^2` coupling map, not a member of
`D2`'s own square `dim(dbar) x dim(dbar)` space; `kron(M_ab,I_2)` does
NOT fix this, since the padded object is still rectangular, shape
`(n2,n1)`, not `(n2,n2)` -- confirmed by re-deriving the dimensions
here before writing any code this round, not just asserting it).

## Part 1 -- third data point: cell (j1=2, j2=2)

Same construction as C112/C114, `k_source=4`, `j2=2` (integer spin,
5 magnetic values `{-2,-1,0,1,2}`, 25 components), `j_target=4`,
`target_level=8`. Larger than `(3/2,3/2)` (16 components) -- tested
with the same "large cell" scope as `(3/2,3/2)` in C114 (remove-one +
single-alone only, no structured-intermediate sampling, per the
established Cheapest Differentiating Test scoping).

**Predictions (honest uncertainty, matching C114's own precedent):**

| # | Prediction |
|---|---|
| P0 | Full sum at `(2,2)` reproduces a real spectrum (extrapolating C112's own pattern at `(1,1)`/`(3/2,3/2)` -- not yet certain, stated as the leading expectation, not an assumption). |
| P1 | Component norms are identical within the cell (extends C114's own finding that ruled out the "trivial near-zero component" explanation -- expected to hold again, stated as a check not a foregone conclusion). |
| P2 | **No predicted sign.** Does `\|a\|=j2 AND \|b\|=j2` correctly classify ALL 25 remove-one results at `(2,2)`, a FRACTION, or NONE? A clean fraction matching neither 100% (like `(1,1)`) nor the `(3/2,3/2)`-style partial pattern would itself be informative (e.g. if the fraction scales with `j2` in a specific way). |

## Part 2 -- properly-formalized mechanism diagnostic (only attempted
if Part 1's three-point data does not itself resolve the pattern
cleanly, and only using a dimensionally-verified construction)

Rather than projecting the rectangular coupling map onto `D2`'s square
anti-Hermitian part (C114's own dimension error), the dimensionally
sound version: `D1`'s and `D2`'s full eigendecompositions give a real
spectrum each (`D1 = V1 Λ1 V1^{-1}`, `D2 = V2 Λ2 V2^{-1}`, generally
non-orthogonal `V1,V2` since `D1,D2` are non-normal). The coupling
element that governs whether a NEAR-DEGENERATE pair `(λ1_i, λ2_j)`
hybridizes into a complex pair is, to leading order in non-Hermitian
degenerate perturbation theory, controlled by
`(left-eigenvector of D2 at λ2_j)^H @ B_ab @ (right-eigenvector of D1
at λ1_i)` -- a well-defined SCALAR (shapes: `(1,n2) @ (n2,n1) @ (n1,1)`,
dimensionally consistent, unlike C114's attempt). Requires identifying
the actual near-degenerate `(λ1_i,λ2_j)` pair(s) first (via the smallest
`|λ1_i - λ2_j|` gaps) -- genuinely more involved than Part 1, attempted
only if warranted after seeing Part 1's results, and abandoned honestly
(not force-fixed) if it runs into further difficulty, matching this
project's own standing practice.

## What this cannot show

- Does not guarantee Part 2 will be attempted or completed -- explicitly
  conditional on Part 1's own results and this round's remaining time
  budget, stated up front rather than silently dropped later.
- Does not change `N_gen=3`'s CONDITIONAL status; this lineage stays
  entirely internal to S3, touches neither S6 nor triality.
- Does not solicit Tom Lawrence's Part 5.

## kill_criterion

If P0 or P1 fails at `(2,2)`, stop and investigate before drawing any
mechanism conclusions -- do not average an anomalous third point into
the existing pattern. If P2's fraction is exactly 25/25 or 0/25 (unlike
either prior cell), report this distinctly rather than forcing it into
the existing two-cell framing.
