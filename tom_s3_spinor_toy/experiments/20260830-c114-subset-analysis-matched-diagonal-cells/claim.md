# C114 claim -- does ANY proper subset of the (j1=j2=1) or (j1=j2=3/2)
matched-diagonal cell's summed components break reality, even though the
FULL sum (C112's own finding) does not?

## L0 gate (EstimandOps)

**Question type:** Descriptive.

## Background -- surfaced by narrow-discovery-engines Engine 2

Ran Engine 2 (Constraint Relaxation Search) against the C90-C113
construction family's own assumptions (full 15-category mining + 4-axis
criticality ranking; see session record). Highest-scoring, cheapest
testable assumption: this project has ALWAYS tested only the FULL sum
over all `(2j2+1)^2` auxiliary components at every `(j1,j2)` cell --
never a proper subset -- except at the k=1 anchor itself, where C109
already found the opposite pattern is necessary there: any ONE component
REMOVED from the full 4-sum restores reality (the anomaly requires the
COMPLETE sum, not any partial one). Whether an analogous but INVERTED
pattern exists at the matched-diagonal cells `(1,1)` and `(3/2,3/2)`
(C112's own genuine "matched, higher-spin" test points, both found
exactly real at the full sum) -- i.e. does some PROPER SUBSET of their
9 or 16 components break reality even though the full sum does not --
has never been checked.

## Entity / falsifiable predicate / measurable outcome (Zero-Signal Gate)

- **Entity:** the `(j1=1,j2=1)` cell (9 components) and `(j1=3/2,j2=3/2)`
  cell (16 components), both already certified real at the full sum
  (C112). Every PROPER, non-empty subset of each cell's own component
  set.
- **Falsifiable predicate:** does any proper subset give
  `max|Im(eig(D_PW))| > 1e-9`, for either cell?
- **Measurable outcome:** `max|Im|` per subset, via the same
  `np.linalg.eigvals` convention as every prior round in this series.

## Predictions (stated before the script runs -- honest uncertainty, no
predicted sign, matching this project's own precedent for genuinely
open questions)

| # | Prediction |
|---|---|
| P0 | The FULL-sum result for both cells reproduces C112's own certified `max\|Im\|=0.0` / `3.1e-15` exactly (sanity check, not new information). |
| P1 | **No predicted sign.** Either: (a) some proper subset of `(1,1)` or `(3/2,3/2)` breaks reality (a genuinely new, unexpected structural finding -- would reopen the whole confound question in a new direction), or (b) every proper subset of both cells also stays exactly real (strengthens H_specific further -- the anchor's own full-sum-required pattern does NOT generalize even at the subset level, not just at the cell level). |

**Combinatorial scope, stated explicitly (Cheapest Differentiating Test
discipline):** `(1,1)` has `2^9-2=510` proper nonempty subsets, `(3/2,
3/2)` has `2^16-2=65534`. Testing ALL of them is not "under 4 hours" in
spirit even though each individual eigenvalue computation is fast --
this round tests a STRUCTURED, motivated subset of subsets, not an
exhaustive search:
1. All subsets of size `n-1` (remove exactly one component) -- direct
   analog of C109's own successful method at the anchor.
2. All subsets of size 1 (a single component alone) -- the opposite
   extreme, cheap to fully enumerate.
3. A structured sample of intermediate sizes: for `(1,1)`, all size-2
   through size-7 subsets restricted to those respecting the CG
   symmetry `(a,b) <-> (-a,-b)` (the natural pairing this construction's
   own reality-preserving structure suggests, per C109's own finding
   that certain symmetric combinations stay real) -- not a blind
   combinatorial search.
4. For `(3/2,3/2)` (larger, 16 components): sizes `n-1` and `1` only,
   per item 1-2 above; the intermediate structured sample from item 3 is
   deferred if items 1-2 already show no signal (per Cheapest
   Differentiating Test -- do not spend the larger cell's combinatorial
   budget before the smaller cell's cheaper result is known).

## What this cannot show

- Does not exhaustively search all `2^9` / `2^16` subsets -- a
  structured, motivated sample, not a full search; a negative result
  here does not prove NO subset breaks reality, only that the
  structurally-motivated candidates do not.
- Does not test subsets at k=3 beyond the `(3/2,3/2)` matched cell
  itself (e.g. does not extend to the off-diagonal cells).
- Does not change `N_gen=3`'s CONDITIONAL status; this lineage stays
  entirely internal to S3, touches neither S6 nor triality.
- Does not solicit Tom Lawrence's Part 5.

## kill_criterion

If P0 fails, stop -- the reused construction code has a regression, do
not trust any subset result until fixed. If P0 holds: report whichever
of P1(a)/P1(b) the structured sample shows; if ANY subset breaks
reality, this is a significant enough finding to warrant its own
follow-up round (do not bury it in this round's own summary), not
attempted here.
