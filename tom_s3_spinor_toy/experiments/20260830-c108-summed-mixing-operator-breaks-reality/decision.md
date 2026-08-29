# C108 decision -- first coupling in the entire series to break the
real-spectrum property, and only at the smallest level

**Verdict:** `SUMMED_MIXING_BREAKS_REALITY_AT_K1_ONLY__HOLDS_AT_K_GEQ_2`
**Status:** RESOLVED -- clean, sharp, level-dependent finding

---

## Summary

Returning to the pure C90-C106 numerical-exploration track (per user
request, after the C107 OB1-bridge detour and its documentation-only
follow-up both concluded), this round finally ran the test C104's own
decision.md flagged as a natural follow-up: does the 2-level D_PW
construction (C101's own minimal setup) still have an exactly real
coupled spectrum when the off-diagonal block is C104's `M_k^sum`
(summed over all 4 `(a,b)` CG components -- genuine 4-fold mixing,
`4*dim_k^2` nonzero entries) instead of C100-C103/C105/C106's
single-component `M_k` (`dim_k^2` nonzero entries)?

**All 6 predictions confirmed exactly:**

| # | Prediction | Outcome |
|---|---|---|
| P0 | `M_1^sum` entrywise real | **CONFIRMED**. |
| P1 | `M_1^sum` genuinely differs from single-component `M_1` | **CONFIRMED**. |
| P2 | k=1->2: clearly non-real | **CONFIRMED** -- `max\|Im\|=0.106`. |
| P3 | k=2->3: exactly real | **CONFIRMED** -- `max\|Im\|=0.0` exactly. |
| P4 | k=3->4: exactly real | **CONFIRMED** -- `max\|Im\|=6.7e-16` (machine epsilon). |
| P5 | k=4->5: exactly real | **CONFIRMED** -- `max\|Im\|=4.1e-15` (machine epsilon). |

## What this genuinely establishes

1. **The first coupling in the entire C101-C108 series to break the
   real-spectrum property.** Every previous candidate tested (r-untouched
   single-component `M_k` in C101-C103/C105; r-coupled Clifford-type
   `sum_i M_1^{(i)} (x) rmult_i` in C106) gave an exactly real coupled
   spectrum, at every level tested. `M_k^sum` is the first to break it --
   and only at k=1.
2. **The break is level-specific, not uniform.** This is not "mixing
   breaks reality" as a general statement -- P3, P4, P5 directly falsify
   that reading. It is specifically: the smallest level pair (k=1->2) is
   anomalous, and the property is robustly restored from k=2 onward
   (confirmed at three separate higher-level pairs, to machine epsilon
   each time -- not a fluke or a near-miss).
3. **Narrows the still-open real-spectrum mechanism question.** Whatever
   protects reality for k>=2 clearly does NOT depend on using a
   single-component (as opposed to summed) coupling -- both work fine at
   k>=2. Something specific to k=1 (the smallest, most constrained level,
   dim_1=2) makes it uniquely fragile under this particular coupling.

## Kill Analysis (per this project's own Anti-Overfitting Gate discipline)

**Killed:** the hypothesis "any CG-derived off-diagonal coupling
preserves the real-spectrum property" -- `M_1^sum` at k=1->2 is a direct,
exact counterexample.

**NOT killed:** (a) the real-spectrum property's robustness at k>=2 --
if anything strengthened, now confirmed under a coupling structure
(4-fold summed mixing) qualitatively different from every prior test,
at three independent higher-level pairs; (b) any of C101-C107's own
findings, all built on different constructions or different levels,
unaffected.

**New open question (not resolved this round):** why is k=1 specifically
anomalous under `M_k^sum`? Candidate directions, none tested: (a) k=1 is
the smallest nontrivial level (`dim_1=2`), where the 4 summed CG
components may have less "room" to avoid destructive interference than
at higher, larger-dimensional levels; (b) some structural coincidence
specific to the k=1->2 transition's own CG coefficients. Flagged as a
pearl for a future round, not chased further here (per the Cheapest
Differentiating Test Protocol -- this round's own scope was "does M^sum
preserve reality," now answered with the necessary nuance; "why k=1" is
a separate, only loosely motivated follow-up question).

## What this cannot show

- Does not explain the k=1 anomaly mechanistically.
- Does not test the r-coupled (Clifford-type) variant combined with
  summed mixing.
- Does not test the 3-level block-tridiagonal construction with `M^sum`.
- Does not change N_gen=3's CONDITIONAL status.
- Does not touch OB1 or the C107 bridge-attempt line.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## Verification

- `ruff check experiments/20260830-c108-summed-mixing-operator-breaks-reality/`
  -- clean, 0 errors.
- All D-bar and M_k^sum construction is exact sympy symbolic arithmetic
  before floating-point conversion; the k=1 break (`0.106`) is far above
  any floating-point tolerance, and the k>=2 machine-epsilon values
  (`6.7e-16`, `4.1e-15`) are consistent with exact-zero results seen
  throughout C101-C107.
- This round's formal script independently re-derives every number found
  during the disclosed scratch exploration (claim.md's Counterfactual
  Frame), including the extended k=3,4 replication not run during the
  initial scratch pass.
