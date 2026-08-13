# C102 decision — real spectrum replicates exactly at k=2,3: second independent data point supports a structural origin

**Verdict:** `REAL_SPECTRUM_REPLICATES__SECOND_DATA_POINT_SUPPORTS_STRUCTURAL_ORIGIN`
**Status:** RESOLVED — clean replication, open question narrowed (not fully closed)

---

## Summary

Repeated C101's exact construction at `k=2,3` (instead of `k=1,2`),
reusing the code verbatim (only the level arguments changed), to test
whether the exactly-real coupled spectrum found in C101 was structural
or a coincidence of that one level pair.

**It replicates exactly.** `P0` (reuse sanity) passes cleanly,
matching C85's own certified eigenvalues for both levels exactly.
`P1` (the open question from C101): the coupled `D_PW` at `k=2,3` also
has an **exactly real spectrum** (`max|Im| = 0.0` exactly, not merely
small — identical to C101's own result). `P2`: a genuine, substantial
spectral shift is found again (max shift `= 7.0`, even larger than
C101's `≈5.08`).

## Predictions vs outcome

| # | Prediction | Outcome |
|---|---|---|
| P0 (reuse sanity) | `D̄_2^full` gives `{-2:12,4:6}`, `D̄_3^full` gives `{-3:20,5:12}` | **PASSES exactly**, zero imaginary residual. |
| P1 (the open question) | coupled `D_PW` (k=2,3) also has exactly real spectrum | **HOLDS** — `max\|Im\|=0.0` exactly, identical structure to C101. |
| P2 (spectral shift) | coupling produces a genuine, nonzero shift | **HOLDS** — max shift `7.0`. |

## The same qualitative pattern repeats

Uncoupled union: `{-3:20, -2:12, 4:6, 5:12}` (total dim 50).

Coupled: **ALL of level 2's eigenvalues (`-2`, `4`) shift completely**
(no states remain at exactly `-2` or `4`) -- consistent with C100's
own finding that `M_2` is an injective embedding touching all of
level 2, mirroring C101's finding that ALL of level 1 shifted in the
`k=1,2` case. **Only a subset of level 3's eigenvalues remain
protected**: 8 of 20 states stay exactly at `-3`, 3 of 12 stay exactly
at `5` -- mirroring C101's finding that only part of the higher level
(there, level 2) stayed protected. The exact fractions differ between
the two rounds (C101: 6/12 and 2/6 protected; C102: 8/20 and 3/12
protected) -- reported as computed, not fitted to a hand-derived rank
formula, matching C101's own discipline of not extrapolating an
unverified counting rule.

## Open question: narrowed, not closed

Two independent, fully consistent data points (`k=1,2` and `k=2,3`)
now support the exactly-real-spectrum property as likely STRUCTURAL
rather than coincidental -- but this is still empirical replication,
not a proof or mechanism. The two candidate explanations from C101's
own pearl-registry entry remain open:

1. `D-bar` may be similar to a Hermitian matrix via a fixed similarity
   transform `S` that `M_k`'s own construction happens to respect
   consistently across levels -- if true, this would make real-spectrum
   a provable, general fact, not requiring level-by-level verification.
2. It could still be an artifact specific to the particular `D^1_{1/2,1/2}`
   component and this particular `r`-untouched ansatz, without a deeper
   structural reason -- two consistent points is not enough to rule
   this out definitively, though it is now less likely than after one
   point alone.

**This round does not attempt to derive the mechanism** -- that would
require actually finding (or ruling out) the similarity transform `S`,
a genuinely different, more analytical undertaking than another
numerical replication. Left as the natural next step if this thread is
pursued further.

## Practical consequence

Two consistent replications meaningfully strengthens confidence that,
UNDER THE EXPLICITLY UNVERIFIED r-untouched ansatz, the resulting
`D_PW` construction is physically sensible (real spectrum) at every
level pair checked so far, not merely at one. This does not change the
ansatz's own unverified status (see C101's Counterfactual Frame) --
only its internal mathematical consistency, which is now better
supported.

## What this cannot show

- Does not prove the real-spectrum property for all `k` -- 2
  consistent points, not a proof.
- Does not identify the mechanism (candidate similarity transform `S`
  not constructed or tested).
- Does not establish `r`-untouched as physically correct.
- Does not change `N_gen=3`'s CONDITIONAL status.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## Verification

- `ruff check experiments/20260812-c102-k2k3-real-spectrum-replication/`
  — clean, 0 errors.
- Code reused verbatim from C101 (only `K_LOW`/`K_HIGH` changed),
  minimizing the risk that a fresh implementation bug produced this
  result rather than genuine replication.
- `np.linalg.eigvals` (general solver) used throughout, matching C85's
  and C101's own established convention -- `eigvalsh` never used.
