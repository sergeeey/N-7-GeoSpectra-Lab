# C112 decision -- j1=j2 alone does NOT reproduce the anomaly at the
tested points, but the grid does not fully disentangle this from a
narrower "target_level=2 specifically" explanation -- WEAKENED, not a
clean kill

**Verdict:** `WEAKENED__J1_EQ_J2_INSUFFICIENT_AT_TESTED_POINTS__TARGET_LEVEL_2_CONFOUND_NOT_FULLY_BROKEN`
**Status:** RESOLVED, with an honest caveat carried forward, not a clean binary result

---

## Summary

Follows up on C109's own pearl ("does an analogous resonance recur at
higher k under a matching auxiliary representation, j2=k/2"). Two rounds
of skeptic review were run -- DDD design review (full context, before
any code) and FL Step 8a artifact review (context-blind, after results)
-- per this session's own explicit commitment after a same-day self-
correction (see `OPEN_BLOCKERS.md` OB11). Both caught real, distinct
issues; neither was rubber-stamped.

## Design review (before code) -- rejected the original single-diagonal
test as confounded

Original plan: test `j2=k/2` at k=2,3 and call it "recurrence." Skeptic
found this changes FOUR things at once with k (the `j1=j2` relation,
level-distance jumped, component count, ignored-CG-channel count), and
that under this construction's own "stretched top state" convention,
adjacent-level coupling (what C108-C111 always tested) is algebraically
IDENTICAL to `j2=1/2` -- so "does an adjacent-coupling resonance recur"
describes something that cannot exist for k>1 at all. Redesigned as a
9-cell `(j1,j2) in {1/2,1,3/2}^2` grid instead of one diagonal slice, so
the PATTERN across cells (not one point) would discriminate hypotheses.

## Results (see `results_c112.json` for full grid)

| j1 \ j2 | 1/2 | 1 | 3/2 |
|---|---|---|---|
| **1/2** | **0.10592...** (anchor, breaks) | 0.0 | 8.9e-16 |
| **1** | 0.0 | 0.0 | 0.0 |
| **3/2** | 6.7e-16 | 2.3e-15 | 3.1e-15 |

- **P0 CONFIRMED exactly:** anchor cell (1/2,1/2) reproduces C108's own
  `max|Im|=0.10592470995283362` bit-for-bit.
- **P_shape CONFIRMED for all 9 cells:** component counts match
  `(2j2+1)^2` exactly, and an independent CG-via-Wigner-3j cross-check
  passes for all 9 (one coefficient per distinct `(j1,j2)` pair).
- **Every other cell is exactly real** (machine-epsilon residuals,
  `1e-16` to `3e-15`) -- including the two genuine "matched, higher-spin"
  cells `(1,1)` and `(3/2,3/2)`, which is what P_pattern was actually
  asking about.

## Artifact review (after code+results) -- found a real remaining confound

Context-blind Step 8a skeptic pass (given only claim.md + the script +
`results_c112.json`, no design history) found the code correct (no bug
producing false-real results in 8 cells -- checked block assembly,
dtype, Hermiticity-by-construction of the off-diagonal, cache-sharing
between cells) but flagged the CONCLUSION as over-scoped:

**Confound not broken:** `target_level = 2*(j1+j2)` equals 2 (i.e.
`j_target=1`) at EXACTLY ONE cell in this grid -- the anchor. Every
other cell has `target_level >= 3`. The grid therefore cannot
distinguish "the anomaly requires `j1=j2` generically" (falsified by
this data) from the narrower "the anomaly requires `target_level=2`
specifically, and `j1=j2` at the anchor was coincidental to that" (NOT
tested -- would require a cell with `j1 != j2` also giving
`target_level=2`, which needs a trivial/singlet representation,
`j2=0` or `j1=0`, excluded from this grid's `{1/2,1,3/2}` range).

**Second, lower-priority caveat:** the auxiliary coupling's action on
the untouched `r`-index is hardcoded as `kron(M_sum, eye(2))` for every
`j2`, inherited unmodified from the `j2=1/2` construction. C106's own
already-established `R_UNTOUCHED_NOT_LOAD_BEARING` result provides some
prior support this is safe, but C106 tested it only for the original
`j2=1/2` construction -- not independently re-verified here for `j2>1/2`.

## What this genuinely establishes

1. **`j1=j2` alone, without controlling for `target_level`, does NOT
   reproduce the C108 anomaly at any of the 8 tested non-anchor points**
   -- a real, structurally-checked, skeptic-surviving negative result.
2. **The narrower alternative ("target_level=2 specifically is the
   trigger, and `j1=j2` at the anchor is coincidental to that, not
   causal") remains untested** -- this grid could not reach it within
   the chosen spin range.
3. Combined with C109's own finding (the anomaly requires the FULL
   4-component sum at the anchor), the anomaly's true necessary-and-
   sufficient condition is narrower than "any `j1=j2` pairing" and at
   least as narrow as "the specific `(j1,j2,target_level)=(1/2,1/2,2)`
   point" -- possibly narrower still (not yet determined whether
   `target_level=2` alone, without `j1=j2`, would also trigger it).

## Kill Analysis

**Killed:** H_matching as originally, broadly stated ("matching `j1=j2`
at higher spin reproduces the anomaly") -- cleanly falsified by 2 direct
tests (`(1,1)`, `(3/2,3/2)`) plus 6 supporting non-diagonal nulls, all
structurally checked.

**NOT killed:** the possibility that `target_level=2` (not `j1=j2`) is
the real trigger -- genuinely open, not addressed by this round.

**What survives as a scoped next step (not attempted here, per Cheapest
Differentiating Test discipline -- this round already ran two full
skeptic passes, further extension deferred rather than compounding
scope):** a cell reaching `target_level=2` via `j1 != j2` (e.g.
`j1=1, j2=0`, a trivial/singlet auxiliary -- note this is itself a
degenerate case, `D1=D2` since `j_target=j1` when `j2=0`, so it tests a
qualitatively different "self-coupling" construction, not a like-for-
like control; a cleaner route was not identified this round). Recorded
as a new pearl below rather than attempted under time/scope pressure.

## What this does NOT show

- Does not disentangle `j1=j2` from `target_level=2` as the true trigger
  (see Artifact review above) -- the round's own headline claim is
  narrower than "H_matching vs H_specific, resolved" as a result.
- Does not independently re-verify the `r`-index treatment for `j2>1/2`.
- Does not derive a group-theoretic mechanism for either candidate
  explanation.
- Does not change `N_gen=3`'s CONDITIONAL status; this lineage remains
  entirely outside the closed P1-P5 program and touches neither S6 nor
  triality (see `OPEN_BLOCKERS.md` OB11's 2026-08-30 correction box).
- Does not solicit Tom Lawrence's Part 5.

## Verification

- `ruff check experiments/20260830-c112-matching-auxiliary-representation-resonance-test/`
  -- clean.
- DDD design review (skeptic, full context, before code): rejected
  original design as confounded, this grid design is the direct
  response.
- FL Step 8a artifact review (skeptic, context-blind, after results):
  verdict WEAKENED -- code correct, conclusion over-scoped, caveat named
  and carried forward here rather than dropped.
- Own verdict-classification code (`c112_matching_auxiliary_grid.py`'s
  own `verdict` string) auto-labeled this `MIXED_PATTERN` -- imprecise,
  documented transparently: the classification heuristic conflated the
  anchor cell (which trivially "breaks" by construction, reusing C108's
  own certified point) with the genuine higher-spin diagonal test cells
  in the same `diag` list, so "not all(diag)" fired even though the
  actual pattern (only the anchor breaks, both genuine matched-diagonal
  cells and all off-diagonal cells stay real) is much cleaner than
  "mixed" suggests. This decision.md's own verdict string is the
  accurate one; the JSON's `verdict` field is left as-is (not silently
  edited) with this note explaining the discrepancy.
