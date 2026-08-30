# C112 claim -- is the k=1 exceptional-point mechanism triggered by the
`j1=j2` coincidence specifically, or confounded with level-distance /
component-count / ignored-CG-channel-count? A small (j1,j2) grid, not a
single diagonal test.

## L0 gate (EstimandOps)

**Question type:** Descriptive.

## Background -- revised after DDD design-review (skeptic, full context,
BEFORE any code was written)

The original design (single diagonal test: `j2=k/2` at k=2,3, calling it
"does the resonance recur at higher k") was sent to the `skeptic` agent
in DDD full-context mode per this session's own recent self-correction
(see `OPEN_BLOCKERS.md` OB11's 2026-08-30 correction box). Verdict:
**the design does not test what it claims to test.** Full transcript
available on request; key findings, all independently checked against
the actual math before accepting:

1. **Four things change simultaneously with k under the original design,
   all locked together — not independent axes:** the `j1=j2` relation
   (intended variable), the level-distance jumped (`Delta = target_level
   - k`, forced from 1 at k=1 to 2k-k=k at general k), the number of
   summed `(a,b)` components (`(k+1)^2`, forced), and the number of
   ignored CG channels under the stretched-top-state convention
   (`2*min(j1,j2)`, forced). A "break" at k=2 could not be attributed to
   `j1=j2` specifically versus any of the other three.
2. **Algebraic fact, verified directly:** under this construction's
   stretched-top-state convention (`j_target = j1+j2`, always the top
   CG channel, never the full decomposition), ADJACENT-level coupling
   (`target_level = k+1`, what C108-C111 always tested) is algebraically
   EQUIVALENT to `j2=1/2` -- `j_target=(k+1)/2 = k/2+1/2` forces
   `j2=1/2` exactly. This means k=1 is the ONLY level where "matching
   `j2=k/2`" and "adjacent coupling" can coexist at all -- "does an
   adjacent-coupling resonance recur at higher k under matching j2" is
   not merely untested, it describes a construction that **cannot
   exist** for k>1. The original framing (inherited uncritically from
   C109's own pearl wording) was itself imprecise.
3. **The proposed P0 positive control (k=1 reproduces C108 exactly) is
   epistemically empty for validating the generalization** -- verified
   directly: at k=1, several distinct bugs (forgetting to generalize
   `j2`, forgetting to generalize the component count, an off-by-one in
   the target-level formula) all coincide with the correct answer,
   because every design choice collapses to the same k=1 numbers. P0 is
   kept below as a sanity check that the code runs, not as validation
   that the generalization is correct.
4. **Missing the control that actually isolates the variable.**

## Revised design: a small (j1, j2) grid, not a single point

Instead of one diagonal slice (`j1=j2=k/2` for increasing k, which the
review showed is not a fair single-variable test), scan a small grid and
let the PATTERN across cells distinguish the competing explanations --
this is the same "systematic sweep beats a hand-picked point" lesson
C111's own history already taught this project (C110 hand-picked cases
found nothing conclusive; C111's systematic `t`-sweep found the real
mechanism).

**Grid:** `j1 in {1/2, 1, 3/2}` (i.e. `k in {1,2,3}`) x `j2 in {1/2, 1,
3/2}` -- 9 cells. For each cell: `j_target = j1+j2` (stretched top,
unchanged convention), target level `= 2*j_target`, source level `=
2*j1 = k`, auxiliary `(a,b)` summed over all `(2*j2+1)^2` magnetic pairs.

| j1 \ j2 | 1/2 | 1 | 3/2 |
|---|---|---|---|
| **1/2** (k=1) | **anchor -- known C108 break** | control A | control B |
| **1** (k=2) | control C | **diagonal test (matched)** | off-diagonal |
| **3/2** (k=3) | control D | off-diagonal | **diagonal test (matched)** |

- The `(1/2, 1/2)` cell is C108's own already-certified result --
  reused as a live sanity check (P0), not re-derived as new information.
- The diagonal cells `(1,1)` and `(3/2,3/2)` are the ORIGINAL H_matching
  test (does matching `j1=j2` at higher spin break reality).
- The off-diagonal cells are the skeptic's requested negative controls
  AND give three-way discrimination: if breaking correlates with the
  diagonal specifically (not with row, column, or `j1+j2` total) --
  H_matching survives. If breaking correlates with e.g. `j2>=1`
  regardless of `j1` (a whole column breaks) -- component-count or
  ignored-channel-count is the real trigger, not `j1=j2`. If it
  correlates with `Delta=j_target*2-k` -- level-distance is the trigger.
  The grid can distinguish all three; a single diagonal point could not.

**Cheapest-first ordering (per skeptic's own suggestion):** compute cell
`(1/2, 1)` FIRST, before the rest of the grid. If it already breaks
reality, `j1=j2` is likely not the discriminating variable (a non-matched
cell breaking as readily as a matched one) and the remaining 7 cells can
be triaged/re-scoped before spending the full compute budget -- exactly
the Cheapest Differentiating Test Protocol this project already commits
to elsewhere.

## Independent structural self-checks (replaces the epistemically-empty
P0-only validation the review flagged)

Before trusting ANY cell's spectrum result:
1. Assert `source_dim == 2*j1+1`, `target_dim == 2*(j1+j2)+1`,
   `n_components == (2*j2+1)**2` for every cell -- catches shape bugs
   the numeric spectrum test alone would not surface.
2. Independently cross-check ONE CG coefficient per distinct `(j1,j2)`
   pair via `cg_via_wigner_3j` (C104's own independent code path,
   reused unmodified) against the builder's own direct CG call -- not
   just at the already-certified k=1 point.

## Predictions (stated before the script runs)

| # | Prediction |
|---|---|
| P0 | Cell (1/2,1/2) reproduces C108's own `max\|Im\|=0.10592470995283362` exactly -- sanity check the code runs, NOT validation of the generalization (per review finding 3). |
| P_shape | All 9 cells pass the structural shape assertions and the independent CG cross-check. |
| P_pattern | **No predicted sign per cell** (honest uncertainty, per this project's own Bridge-F' precedent for genuinely open questions) -- the round's actual output is the FULL 3x3 break/no-break pattern, read against three candidate explanations (diagonal / column / anti-diagonal-by-Delta) after the fact, not a single pre-committed pass/fail. |

## What this cannot show

- Does not test j1 or j2 beyond 3/2 (9-cell grid only; a positive
  diagonal-specific pattern would motivate extending the grid, not
  attempted here).
- Does not t-sweep any cell beyond t=1 (C111's own t-sweep was for the
  k=1 anchor specifically; repeating it for every grid cell is out of
  scope here).
- Does not derive a group-theoretic mechanism even if a clean
  diagonal pattern is found -- establishes correlation, not why.
- Does not change `N_gen=3`'s CONDITIONAL status; this entire C90-C111+
  lineage is outside the closed P1-P5 program and touches neither S6 nor
  triality (see `OPEN_BLOCKERS.md` OB11's correction box).
- Does not solicit Tom Lawrence's Part 5.

## kill_criterion

If P0 or P_shape fails for ANY cell -> STOP, do not interpret the
break/no-break pattern until the code is fixed (per skeptic finding 3,
a passing spectrum result with a shape bug is not trustworthy). If both
pass: report the full 9-cell pattern and which candidate explanation(s)
it is and is not consistent with -- do not force a clean H_matching /
H_specific binary verdict if the pattern is genuinely mixed (per this
round's own honest-uncertainty P_pattern framing).

## Skeptic design review record

Full DDD full-context review completed 2026-08-30 (`skeptic` agent,
before any code existed). Verdict: original single-diagonal design
rejected as confounded; this grid design is the direct response to all
5 objections raised. Agent session retained for continuation if needed
(agentId `a652fb9d14c95711c`).
