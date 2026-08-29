# C110 claim -- does "covariance" (single real-coordinate combinations
vs arbitrary complex mixes) explain which couplings preserve reality at
k=1? Tests the falsifiable prediction from C109's own new pearl.

## L0 gate (EstimandOps)

**Question type:** Descriptive (does property X of a coupling matrix --
correspondence to a genuine real coordinate function -- predict property
Y -- whether the coupled spectrum stays real?). Not causal in the
EstimandOps population sense -- a structural/algebraic classification
question about a fixed family of matrices.

## Background -- why this round exists

C109 found that C108's k=1 anomaly requires the FULL 4-component sum
`M_1^sum` specifically, and flagged a new, sharper pearl: `M_1^sum`
corresponds to the non-covariant quantity `sum_{a,b} D^1_{ab}(g)
= 2*aw + 2i*bx` (mixing the real quaternion coordinates `aw` and `bx`
with a factor of `i`), unlike C106's own genuinely covariant Cartesian
combinations (`ax`, `bw`, `bx` individually). The pearl's own falsifiable
prediction: build a genuinely covariant (single-real-coordinate or
real-weighted) combination and check whether it stays real, as a
contrast to the non-covariant `M_sum`. User asked to test this directly
("проверь ковариантность").

## Counterfactual Frame (exploratory round -- disclosed up front, INCLUDING
a hypothesis that was refuted mid-exploration, not smoothed over)

Cheap interactive scratch exploration (sympy/numpy) was run FIRST,
matching this project's established discipline. It proceeded in stages,
and the intermediate refutation is recorded here honestly rather than
hidden:

1. **Stage 1 (initial, appealing hypothesis)**: tested the four
   individually-covariant quaternion coordinates (`aw`,`ax`,`bw`,`bx`,
   each as a standalone coupling) plus `M_sum` as the non-covariant
   baseline. ALL FOUR single coordinates gave exactly real spectra;
   `M_sum` broke it (`0.106`). This looked like a clean confirmation:
   "covariant preserves, non-covariant breaks."
2. **Stage 2 (first crack)**: tested `aw+bw` (real sum of two DIFFERENT
   coordinates, no `i`) -- stayed real, consistent with the hypothesis.
   But `aw+i*bw` (mixing with an explicit `i`, structurally similar to
   `M_sum`'s own `aw+i*bx` pattern) ALSO stayed exactly real -- the
   first genuine counter-example to a naive "any i-mixing breaks it"
   reading.
3. **Stage 3 (clean refutation)**: using exact sympy symbolic
   decomposition (not error-prone hand algebra -- an earlier hand
   computation of one test case was independently caught and corrected
   mid-round when it contradicted the exact symbolic result) of several
   more combinations (`(c1,c2,c3,c4)=(1,2,3,4)`, `(1,-1,1,-1)`,
   `(2,1,1,2)`) against their exact `real_part`/`imag_part`
   decomposition in `(aw,ax,bw,bx)`: some combinations with a NONZERO
   symbolic imaginary part (hence "non-covariant" by the pearl's own
   definition) preserve reality (`i*aw` alone, `i*ax` alone, `i*bw`
   alone, `aw+i*bw`), while others with nonzero imaginary part break it
   (`M_sum`, `(1,2,3,4)`, `(1,-1,1,-1)`, `(2,1,1,2)`). Matrix-entrywise
   realness of the coupling itself also does not cleanly separate the
   two groups (`M_trace` and `M_sum` are both entrywise-real matrices,
   yet only one breaks reality; `M1_x`, `M1_z` are entrywise-imaginary
   matrices, both preserve reality).

**The simple covariance hypothesis, as originally stated by the pearl,
is REFUTED by stage 3.** No single criterion tried this round (real
symbolic imaginary part being zero; matrix entrywise realness) cleanly
separates the "breaks" group from the "preserves" group.

The formal script below independently re-derives every data point from
scratch, preserving the full, precise (c1,c2,c3,c4) -> (real_part,
imag_part) -> reality-status table as a resource for future
characterization attempts, rather than forcing an unsupported narrative.

## Entity / falsifiable predicate / measurable outcome (Zero-Signal Gate)

- **Entity:** a set of specific linear combinations
  `c1*M_pp+c2*M_pm+c3*M_mp+c4*M_mm` at k=1, each used as the off-diagonal
  coupling in C101's own 2-level D_PW.
- **Falsifiable predicate:** whether "the combination's exact symbolic
  imaginary part (in terms of `aw,ax,bw,bx`) is identically zero"
  correctly predicts "the coupled spectrum is exactly real," for a
  representative set of combinations spanning both simple coordinates
  and more complex mixes.
- **Measurable outcome:** `max|Im(eig(D_PW))|` per combination
  (`np.linalg.eigvals`, `1e-6` threshold), cross-tabulated against the
  symbolic `imag_part` (identically zero or not, via sympy exact
  arithmetic).

## Predictions (stated before the formal script runs, though after the
disclosed, honestly-reported-including-refutation scratch exploration
above)

| # | Prediction |
|---|---|
| P0 | All 4 single coordinates (`aw`,`ax`,`bw`,`bx`) and `M_sum` reproduce Stage 1's numbers exactly (`aw,ax,bw,bx`: real; `M_sum`: `max\|Im\|=0.106`). |
| P1 | `aw+bw` (zero symbolic imag_part) is exactly real; `aw+i*bw` (nonzero symbolic imag_part = `bw`) is ALSO exactly real -- reproducing Stage 2's counter-example. |
| P2 | The "zero imaginary part correctly predicts real spectrum" direction of the hypothesis holds for every zero-imag_part case tested (no false negatives). |
| P3 | The "nonzero imaginary part correctly predicts non-real spectrum" direction FAILS for at least `aw+i*bw`, `i*aw` alone, `i*ax` alone, `i*bw` alone (false positives for the hypothesis -- these have nonzero imag_part but real spectrum). |
| P4 | At least one nonzero-imag_part case (`M_sum`, `(1,2,3,4)`, `(1,-1,1,-1)`, or `(2,1,1,2)`) genuinely breaks reality, confirming the hypothesis is not simply wrong in the OTHER direction either -- SOME nonzero-imag_part cases do break it. |

## What this cannot show

- Does not identify the TRUE, complete characterization of which
  combinations break reality -- only that the simple covariance
  hypothesis fails, with the full data table preserved for a future,
  more systematic (e.g. fully parametrized complex 4-space) attempt.
- Does not test k>=2 combinations (already established real in C108).
- Does not change N_gen=3's CONDITIONAL status.
- Does not touch OB1.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## kill_criterion

If P0-P4 all hold as predicted, this formally confirms (not just via
scratch) that the simple covariance hypothesis from C109's pearl is
refuted -- a genuine, informative null result on a specific, well-posed
question, per this project's own Anti-Overfitting Gate discipline (a
refuted specific hypothesis is real progress, narrowing the space of
remaining candidate explanations). If instead some prediction fails
(e.g. P3's claimed counter-examples turn out to actually be real
numerically-but-not-symbolically, or vice versa), this round reports
that discrepancy directly rather than the refutation.
