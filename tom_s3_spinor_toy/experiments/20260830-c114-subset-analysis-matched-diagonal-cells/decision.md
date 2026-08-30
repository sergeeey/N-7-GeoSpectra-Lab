# C114 decision -- confirmed: partial sums at k=2,3 DO break reality, even
though the full sum (C112) doesn't -- reopens the H_matching/H_specific
picture, mechanism still unexplained

**Verdict:** `SUBSET_BREAKS_REALITY__CONFIRMED_NOT_TRIVIAL__MECHANISM_OPEN`
**Status:** RESOLVED as a confirmed observation; mechanism explicitly NOT
resolved, named as the next open item

---

## Summary

Surfaced by `narrow-discovery-engines` Engine 2 (Constraint Relaxation
Search), run against the C90-C113 construction family's own unquestioned
assumptions (full 15-category mining + 4-axis criticality ranking).
Highest-scoring, cheapest testable candidate: this project has always
tested only the FULL component sum at every `(j1,j2)` cell except the
k=1 anchor, where the opposite pattern (any proper subset restores
reality) is already established (C109). Tests whether an analogous
subset-sensitivity exists at C112's own genuine "matched, higher-spin"
cells `(1,1)` and `(3/2,3/2)`, both certified real at the full sum.

## Results

**Finding, confirmed:** at BOTH matched cells, specific proper subsets
DO break reality, even though the full sum does not.

- **Cell (1,1)**, 9 components: removing any ONE of the 4 "corner"
  components `{(1,1),(1,-1),(-1,1),(-1,-1)}` breaks reality
  (`max|Im|~0.00136` in each case); removing any of the other 5 (the
  `a=0` or `b=0` components) stays exactly real. Two structured
  intermediate subsets (sizes 5 and 7, both respecting the
  `(a,b)<->(-a,-b)` pairing symmetry) also break reality
  (`~0.0029`, `~0.0043`).
- **Cell (3/2,3/2)**, 16 components: removing any ONE of 12 out of 16
  components breaks reality, clustering into 3 magnitude groups
  (`~1.06e-5` for the 4 extreme-corner removals, `~2.7e-4` and
  `~3.0e-4` for two other groups of 4); removing any of the 4
  `(±3/2,±1/2)`-type components stays exactly real.

**Full data:** `results_c114.json` (46 subsets tested at (1,1), 32 at
(3/2,3/2); structured-intermediate sampling only run for the smaller
cell per claim.md's Cheapest Differentiating Test scoping).

## FL Step 8a artifact review (skeptic, context-blind) -- two real
objections raised, one resolved cleanly, one left honestly open

Ran BEFORE writing this decision, given the finding's significance
(directly complicates C112's own conclusion). Verdict on the first
version of this script: **WEAKENED**, two concrete objections:

1. **"Is 'safe removal' just removing a near-zero component (trivial)?"**
   -- **RESOLVED, cleanly ruled out.** Added `component_norms` diagnostic:
   ALL 9 components at cell (1,1) have IDENTICAL norm (`5/3` exactly,
   to floating-point precision); all 16 at cell (3/2,3/2) have identical
   norm (`7/4` exactly). The "safe" and "breaking" components are
   numerically indistinguishable by size -- this is not an artifact of
   some components being negligible. The pattern is genuinely about
   WHICH component is removed, not how large it is.
2. **"Are D1/D2 secretly Hermitian, making the whole framing suspect?"**
   -- **Checked directly, confirms the already-certified project fact**:
   `D1_hermitian_err` = 2 and 4 (cells (1,1), (3/2,3/2) respectively),
   `D2_hermitian_err` = 6 and 10 -- both clearly nonzero, confirming
   `dbar_full` is NOT Hermitian as a raw matrix (consistent with every
   prior round in this series, C101 onward, which is exactly why
   `np.linalg.eigvals` and never `eigvalsh` is used throughout).
3. **"Do 'safe' components vanish on D2's own anti-Hermitian part
   (meaning the pattern is an already-implied, non-novel consequence of
   `dbar`'s structure)?"** -- **NOT resolved, honestly left open.** A
   first attempt at this diagnostic hit a genuine dimension mismatch
   (`M_ab` is the rectangular `dim_target^2 x dim_source^2` coupling
   map, not a member of `D2`'s own square `dim(dbar) x dim(dbar)` space;
   `kron(M_ab, I_2)` does not correctly embed it there). Removed rather
   than force-fit incorrectly under time pressure -- recorded as the
   genuinely open mechanism question, not silently dropped.

## What this genuinely establishes

1. **C112's own "the full sum stays real at (1,1) and (3/2,3/2)" is
   correct and unaffected** -- but its implicit framing ("therefore no
   coupling at k=2,3 in this family can break reality") was too broad.
   Reality-breaking DOES occur at k=2,3, via specific partial
   combinations of components -- just not the particular full-symmetric-
   sum construction C104's convention has used since it was introduced.
2. **The k=1 anchor's own pattern (full sum required, any removal
   restores reality) does NOT generalize to k=2,3** -- if anything, the
   opposite shape appears: at k=2,3, the FULL sum is the SPECIAL
   (reality-preserving) point, and SPECIFIC partial sums are what break
   it. This is a genuinely different relationship between "completeness
   of the sum" and "reality," not a simple analog.
3. **Not numerically trivial** -- confirmed via the component-norm check,
   the strongest of the skeptic's alternative explanations is ruled out.
4. **Mechanism remains unexplained.** Which specific components are
   "safe" vs "breaking" shows a partial pattern (corners vs. edges/
   center at (1,1); a 3-way magnitude clustering at (3/2,3/2)) but no
   closed-form characterization is offered here -- establishing
   recurrence/existence of the phenomenon, not its cause, consistent
   with this project's own standing distinction between those two
   questions throughout the C108-C113 series.

## Kill Analysis

**Not killed:** C112's own full-sum result at both matched cells --
reused, unmodified, confirmed to full precision (`0.0` and `3.12e-15`
respectively) as this round's own P0.

**Killed:** the implicit broader reading of C112 ("no coupling breaks
reality at k>=2 in this construction family") -- directly falsified;
specific subsets do break it.

**NOT killed, now the live open question:** what characterizes the
"safe" vs "breaking" subsets. The corner/edge distinction at (1,1) is a
plausible candidate pattern but not verified as general (only 2 cells
tested, at different `j2`, with different apparent groupings -- (1,1)'s
pattern is a clean 4-vs-5 split, (3/2,3/2)'s is a 3-magnitude-cluster
12-vs-4 split, not obviously the same rule restated at different scale).

## What survives as a scoped next step (two candidates already checked
and refuted, same session, against the data already in results_c114.json
-- not left as untested suggestions)

1. **Checked: does `|a|=j2 AND |b|=j2` ("both-extreme") explain both
   cells?** Fits `(1,1)` PERFECTLY (9/9 exact match). Fits `(3/2,3/2)`
   only PARTIALLY (8/16 exact -- correct on every `a=+-3/2` row, WRONG
   on all 8 `a=+-1/2` rows, which break regardless of `b`, contradicting
   the rule's own prediction of no-break there). Refuted as the full
   mechanism, though the perfect low-`j2` fit is itself informative (not
   pure coincidence-shaped).
2. **Checked: the natural a-vs-b-asymmetric refinement the `(3/2,3/2)`
   data itself suggests** ("breaks unless `|a|=j2` AND `|b|<j2`", i.e.
   `a` privileged as the source/extreme-sensitive index) -- fits
   `(3/2,3/2)` by construction but FAILS on `(1,1)`'s own `(a,b)=(0,1)`
   case (predicts breaks=True, actual is False). Also refuted.
3. **Genuinely still open, not attempted:** a graded (non-binary)
   condition on `|a|,|b|` relative to `j2`, or the skeptic's own
   anti-Hermitian-projection diagnostic (correctly formalized this time
   -- would test whether the pattern is a known consequence of `dbar`'s
   spectral structure rather than requiring an ad hoc combinatorial
   rule), or a third matched cell (e.g. `(2,2)`) for a third data point
   before guessing a fourth rule. Recorded as a pearl below; two
   candidate rules already eliminated there so a future round does not
   repeat either.

## What this does NOT show

- Does not derive WHY specific subsets break reality -- establishes the
  phenomenon, not its mechanism.
- Does not exhaustively search all `2^9`/`2^16` subsets -- a structured
  sample per claim.md's own scoping.
- Does not resolve C112's own `target_level=2` vs `j1=j2` confound --
  orthogonal to that question; this round is about a DIFFERENT axis
  (component subset, not level/spin choice).
- Does not change `N_gen=3`'s CONDITIONAL status; this lineage stays
  entirely internal to S3, touches neither S6 nor triality.
- Does not solicit Tom Lawrence's Part 5.

## Verification

- `ruff check experiments/20260830-c114-subset-analysis-matched-diagonal-cells/`
  -- clean.
- FL Step 8a skeptic pass run and incorporated (see above) -- one
  objection cleanly resolved (component norms), one honestly left open
  (anti-Hermitian projection, a first attempt had a real dimension bug,
  removed rather than force-fixed).
- Reused C112's own `build_M_ab_general` unmodified.
