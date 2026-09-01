# C122 decision -- three rounds of self-correction (v1, v2, v3), each
found and fixed a real bug and each introduced a new one; PARKED, not
resolved, after the third round's own skeptic pass

**Verdict:** `PARKED__THREE_ROUNDS_EACH_FOUND_A_REAL_BUG__GENUINE_MATCHED_CONTROL_REQUIRES_DEGENERACY_STRUCTURE_MATCHING_NOT_ATTEMPTED__NO_QUANTITATIVE_CLAIM_FROM_THIS_EXPERIMENT_SURVIVES`
**Status:** PARKED (not REJECT, not SUPPORTED). A concrete, specific
reopen condition is named below, not attempted this session -- the
"cheap ~20 line" framing this whole negative-control idea started with
turned out to be wrong; a genuinely matched control requires
non-trivial RMT-level design work, per the third skeptic pass's own
"repair" list.

## What actually happened, honestly, across all three rounds

- **v1**: complex Hermitian perturbation on a real operator -- a
  category error. `s*` was a pure artifact of the search grid,
  containing zero information. Fixed in v2.
- **v2**: fixed the symmetry-class error, but compared the random
  family (fine search) against the real family's `s*` from C118's OWN
  coarser search -- an asymmetric-instrument bug. "No overlap" compared
  an interval the real family was never sampled in. Also: v2's own
  pre-registered kill criterion (matching `s*~1/dim` power-law
  exponents) was actually satisfied by the random family and not
  reported. Also: the headline "30-300x" figure was arithmetically
  wrong. Fixed (attempted) in v3.
- **v3**: rebuilt the real matrices via C118's own `build_cell` and ran
  an IDENTICAL log-spaced search on both families -- intended to fix
  the asymmetric-instrument bug. **FL Step 8a skeptic (context-blind,
  third pass on this one round) found v3 introduced TWO NEW, decisive
  problems, independently re-verified by this session before writing
  this correction (not merely accepted):**

## v3's own errors, self-verified

**1. The "fine" grid had a hole COARSER than C118's own grid, exactly
where the real j2=3/2 crossing sits -- confirmed directly:**

```
v3's logspace(-8,0,40) points above 0.05: [..., 0.3888, 0.6236, 1.0]
C118's own j2=3/2 coarse_scan (results_c118.json): supra-threshold
window is (0.45, 0.60) -- ENTIRELY inside v3's grid gap (0.389, 0.624).
```

v3's search therefore read sub-threshold at 0.389, sub-threshold AGAIN
at 0.624 (the real island had already closed by then), supra at 1.0,
and bisected between 0.624 and 1.0 -- landing on the SECOND crossing
(~0.679), not the true first crossing. **v3's "correction" of j2=3/2
(88.3) was itself wrong. C118's ORIGINAL value (0.4599, `s*.dim=59.8`)
was correct all along.** v3 additionally LOST the real island at
j2=3/2 (reported 0 islands there; C118's own data clearly shows one)
and presented this loss as if it were evidence the fine grid had
dissolved a spurious feature -- the opposite of what happened.

A genuinely finer grid can only move a detected first crossing DOWN,
never up -- v3's own reported increase (59.8 -> 88.3) should have been
a red flag on its face and was not caught before committing.

**2. The `kappa(V)` "non-monotonicity" claim used the wrong variable
and was statistically underpowered:**

- Bauer-Fike (`|Im lambda| &lt;= kappa(V)*s*||Delta||_2`) has NO
  dimension factor -- comparing `kappa(V)` against `s*.dim` (as v3's
  decision.md did) is the wrong pairing. Against the CORRECT variable
  (raw `s*`), the specific counterexample v3 named (`j2=5/2`, highest
  `kappa(V)`, "not the smallest s*") evaporates: in raw `s*`, j2=5/2 is
  the SECOND SMALLEST of five, consistent with a conditioning-driven
  story.
- With only 5 data points, a proper log-log regression of `s*` against
  `kappa(V)` gives a 95% confidence interval on the slope of
  approximately `[-1.13, +0.37]` -- this CONTAINS the pure-conditioning
  prediction (slope -1). **The data cannot distinguish "pure
  conditioning explains it" from "no relationship at all."** v3's
  confident "not monotone, structure beyond conditioning likely
  matters" was an overclaim on an underpowered dataset.

**3. The random-matrix control was never actually matched on the
quantity the density hypothesis is about: distinct eigenvalue count.**

The real `D1`, `D2` blocks are built as `kron(I_{L+1}, dbar(L))` --
this is EXACT, massive built-in degeneracy (already known since
C118's own v1 substrate failure). At most `2(L1+1)+2(L2+1)` distinct
eigenvalues exist in the real family -- **16 to 40** across the 5
cells, vs the random family's genuinely dense **68 to 436** distinct
eigenvalues (a Ginibre-conjugated matrix has no such structure). This
mismatch is 4x to 11x and **grows systematically with dimension** --
exactly the axis the whole comparison is about. A density-only
argument, applied HONESTLY, predicts the sparser (real) family should
need a LARGER perturbation to force a collision than the denser
(random) family -- for density reasons alone, no representation
theory required. A rough order-of-magnitude estimate (gap sizes from
each family's own known level spacing) suggests this density mismatch
alone plausibly accounts for the observed real/random ratio, possibly
over-accounting for it. **The "matched" comparison v3 claimed was
never matched on the one axis that mattered.**

**4. v3 repeated a mistake from v2 it had specifically set out to
fix:** the power-law exponent comparison (`real p=-1.92 vs random
p=-0.76`) is, with proper standard errors, statistically
indistinguishable (large overlapping confidence intervals given n=5) --
meaning the ORIGINAL pre-registered kill criterion (claim.md) is
STILL satisfied by the random family, and was STILL not reported as
such. Same defect skeptic caught in v2, present again in v3.

**5. `coarse_scan` was not persisted for either family in v3's own
output** -- a real provenance regression relative to C118's own
convention (which does save it), and the exact discipline gap that let
error #1 above go unnoticed until an independent skeptic pass caught
it by cross-referencing C118's own already-committed data.

## What this means for the round's own headline claims -- ALL RETRACTED

- ~~"Density hypothesis NOT supported, gap survives 15-253x"~~ --
  RETRACTED. The comparison was never validly matched (distinct-
  eigenvalue-count mismatch, growing with dimension, in exactly the
  direction that produces the observed gap).
- ~~"kappa(V) does not explain s*.dim, structure beyond conditioning
  matters"~~ -- RETRACTED. Wrong variable used; with the correct one,
  the data is statistically underpowered to distinguish pure
  conditioning from no relationship at all.
- ~~"C118's j2=3/2 value was grid-resolution-limited, true value
  88.3"~~ -- RETRACTED, REVERSED. C118's original value (59.8) was
  correct. v3's own grid had a worse hole in exactly that location.
- The j2=3 correction (32.0 -> ~5.27) remains PLAUSIBLE (C118's own
  grid genuinely never sampled below `s=0.05`, where this value sits)
  but is now flagged UNAUDITABLE, since v3 did not persist the coarse
  scan needed to independently confirm it is not itself another
  grid-hole artifact.
- ~~"Real-restoration islands are not exclusive to the real family,
  weakening a C118 pearl"~~ -- RETRACTED as stated. v3's own real-
  family island count was itself wrong (lost the genuine j2=3/2
  island due to the grid-hole bug); the comparison this claim rested
  on is not trustworthy as computed.

## Kill Analysis

**What was killed:** every specific quantitative claim this round's
v2 and v3 attempted to establish about the density hypothesis, the
`kappa(V)` relationship, and C118's own `s*.dim` values. None survive
independent, self-verified re-derivation.

**What was NOT killed:** the density hypothesis itself (still open --
this experiment failed to test it validly, three times, not that it
tested it and found against or for it). C118's own ORIGINAL `s*.dim`
values (all 5, including j2=3/2 -- CONFIRMED correct, not corrected,
by this round's own failed attempt to correct them).

**What survives as genuinely established, narrow:**
- `build_cell` reuse for the real family is sound: 3 of 5 rebuilt `s*`
  values reproduce C118's own stored values to 4-5 significant
  figures (the 2 that don't are v3's own grid-hole and grid-floor
  artifacts, now understood, not `build_cell` errors).
- The real family's threshold crossing is genuinely binary across ~8
  orders of magnitude at every tested cell (`&lt;1e-15` below, `&gt;1e-5`
  above, nothing in between) -- a clean, trustworthy signal on the
  real side specifically.
- The general METHODOLOGICAL lesson (see feedback memory saved this
  round): a "finer" log-spaced grid is not automatically finer
  EVERYWHERE than a coarser linear one -- log-spacing concentrates
  resolution near the low end and can leave WIDE gaps near the high
  end, wider than the linear grid it's meant to improve on. Any future
  attempt must use a union of grids or verify point-density
  everywhere in the search range, not just at the low end.

**Relaxation Map / reopen condition (named, NOT attempted this
session -- this is a real, larger round, not a quick patch):**

| Step | What it requires |
|---|---|
| Union grid for BOTH families | `np.union1d` of a fine linear grid and a fine log grid, verified no gap exceeds a fixed small ratio anywhere in `[0,1]` |
| Persist full `coarse_scan` for both families | One-line fix, restores C118's own standard, makes every future claim auditable |
| Build a GENUINELY degeneracy-matched random control | `[[I_{L1+1} kron A1, C^T],[C, I_{L2+1} kron A2]]` with `A_i` random non-symmetric real-spectrum matrices of size `2(L_i+1)` -- matches the real family's OWN degeneracy structure, not a generic dense-spectrum random matrix |
| Match `Delta`'s rank and block structure | Real `Delta_H` is block-anti-diagonal, rank `&lt;=` the corner component's own rank -- the random perturbation should be too, not a dense full-rank matrix |
| Per-eigenvalue conditioning near the actual collision, not global `kappa(V)` at `s=0` | `scipy.linalg.eig(left=True, right=True)`, compute `kappa(lambda)=1/|y^H x|` for the specific colliding pair, not a global condition number dominated by an unrelated degenerate cluster |
| Multiple seeds (>=20) per dimension | Report median + IQR, not a single draw -- needed given how much v2/v3's single-draw results moved between rounds |

## What this round does NOT show

- Does not establish or refute the density hypothesis.
- Does not correct C118's own `s*.dim` values (attempted, found
  wrong, reverted -- C118's original values stand, uncorrected, except
  possibly j2=3, itself unaudited).
- Does not change N_gen=3's CONDITIONAL status; does not touch S6/
  triality/OB1.
- Does not solicit Tom Lawrence's Part 5.

## Verification

- `ruff check experiments/20260901-c122-c118-negative-control/` --
  clean (v3 script, code itself has no bugs; the ERROR was in the
  search grid's resolution characteristics and the choice of
  comparison variable, not in code correctness per se).
- Full pytest suite run before commit (unchanged from v3's own run).
- The grid-hole claim independently re-verified by this session
  (computed the actual `logspace` grid points, confirmed the gap;
  read C118's own `results_c118.json` coarse_scan directly, confirmed
  the true crossing sits inside that gap) -- not merely accepted from
  the skeptic's own report.
- Three full FL Step 8a skeptic passes on this one round (v1, v2, v3),
  each catching a genuine, independently-verified defect -- itself
  informative about the actual difficulty of building a valid negative
  control for this operator family, matching this project's own
  Cheapest Differentiating Test discipline: this was NOT the cheap
  ~20-line test it was originally proposed as.
