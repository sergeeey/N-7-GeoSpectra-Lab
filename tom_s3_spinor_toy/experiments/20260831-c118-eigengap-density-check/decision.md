# C118 decision -- density hypothesis test: narrow numeric fact
survives, the hypothesis itself does not

**Verdict:** `S_STAR_DECREASES_WITH_DIM__NON_DIFFERENTIATING_VS_COUNTING_NULL__DOES_NOT_SUPPORT_DENSITY_MECHANISM`
(replaces the script's raw `DENSITY_HYPOTHESIS_SUPPORTED_S_STAR_TRENDS_DOWN`
-- retracted, per FL Step 8a skeptic pass; treat as effectively
FALSIFIED-as-worded, not merely weakened)
**Status:** RESOLVED as a cheap first-pass filter, per its own
pre-registered scope -- the filter result is negative, not positive

## Summary

Two attempts this round, both reviewed by FL Step 8a skeptic
(context-blind) before being trusted:

- **v1** (global minimum eigenvalue gap across the whole spectrum vs.
  component Frobenius norm): produced `min_gap = 0.0` EXACTLY at all
  5 cells. Diagnosed before any conclusion was drawn: `D1`/`D2` are
  built as `kron(I_dim_q, dbar)`, which creates exact `dim_q`-fold
  degeneracy by construction, dominating any global-minimum statistic
  and unrelated to the reality-breaking mechanism under study. Deleted
  before committing, per this project's own Substrate Gate (a test
  that cannot honestly measure the target quantity is never recorded
  as evidence against the hypothesis).
- **v2** (continuous removal-fraction sweep `s in [0,1]` for the
  corner `(j2,j2)` component, locating `s*` where `max|Im|` first
  crosses `1e-9`): produced a clean-looking result, `s* = 0.639,
  0.460, 0.134, 0.164, 0.073` for `j2 = 1, 3/2, 2, 5/2, 3`, one
  reversal, verdict `DENSITY_HYPOTHESIS_SUPPORTED`. Skeptic review
  found this verdict is NOT supported by the data -- full response
  matrix below.

## Skeptic response (2026-08-31, FL Step 8a, context-blind pass on
this round's v2 result)

Verdict: **WEAKENED, with an explicit instruction to treat the
verdict string as FALSIFIED if propagated unchanged.** Full response
per the project's own Response Matrix (`falsification-ladder.md`
Step 8a):

| Concern | Response |
|---|---|
| The `Delta_H` linear-algebra construction itself, and the corner-component identification | **CONFIRMED-REAL, independently.** Skeptic bit-for-bit cross-checked the `s=1` (full removal) endpoint against C114's own already-committed `results_c114.json` for j2=1 (`0.0013604607813099468`, exact match) and j2=3/2 (`1.064498730197737e-05`, exact match) -- the strongest positive finding in the review. No fix needed. |
| **`max_im(s)` is NOT monotone in `s` -- two cells (j2=3/2, j2=2) show reality RESTORED after the first crossing** (real-restoration "islands": j2=3/2 drops back below threshold at `s=0.60,0.65` after crossing at `s=0.50`; j2=2's `s=0.15` crossing is a single isolated grid point surrounded by sub-threshold neighbors on both sides). Bisection on a non-monotone predicate converges to *an* exceedance, not necessarily the first one -- and the reported `s*` values are NOT the same kind of object across cells (persistent onset for j2=1,5/2,3; leading edge of a transient island for j2=3/2,2) | **Accepted, fatal to the "one comparable number per cell" framing.** The 5 `s*` values are not commensurable as originally presented. Documented below; the raw per-cell sweep data (already in `results_c118.json`'s own `coarse_scan` field) is the only trustworthy artifact, not the single reduced number. |
| **The one reversal that the pre-registered kill criterion "tolerated" (j2=2 -> j2=5/2, `0.134 -> 0.164`) is caused by exactly ONE grid point** (`s=0.15` at j2=2, an isolated spike ~9 orders above its immediate 1e-15-scale neighbors). Removing that single point flips the bracket entirely -- `s*(j2=2)` becomes `~0.36-0.40`, and the reversal disappears, but at a DIFFERENT location than either reading | **Accepted.** The pre-registered "<=1 reversal" criterion was satisfied by a coarse-grid artifact, not a robust signal. A 21-point grid (step 0.05) cannot resolve a genuine feature narrower than 0.05, and multiple such features are visible in the raw scan data. |
| Skeptic independently proved `\|\|Delta_H\|\|_2 = 1` EXACTLY at every one of the 5 cells (from the exact Kronecker-factorization of `M_ab` and the stretched-state CG coefficient `<j j; j j\|2j,2j> = 1`) -- this closes claim.md's own named component-norm confound (Frobenius norm grows mildly, `5/3` to `13/7`, but the OPERATOR norm that actually governs eigenvalue perturbation is exactly constant) | **Accepted as a genuine positive result, not previously established.** Worth keeping: `s*` is a comparable ABSOLUTE perturbation-size measurement across cells, not confounded by a growing perturbation norm. |
| **A worse, unaddressed confound: non-normality/ill-conditioning grows with `j2`** (`d1_hermitian_err`, `d2_hermitian_err` scale with level, already known since C114-C117) -- for a non-normal operator, Bauer-Fike gives `\|delta-lambda\| <= kappa(V) * \|\|E\|\|_2`; a growing eigenvector condition number predicts `s* -> 0` exactly as well as a denser spectrum does, and this design does not separate the two | **Accepted, not adjudicated.** A real gap; the cheapest fix (record `kappa(V)` per cell) is named below as unattempted future work, not done this round. |
| **The framing "density explains it, no representation theory required" is internally incoherent**: the eigenvalue multiplicities that set the spectral density are themselves given by Meier's own representation-theoretic multiplicity formula, and the perturbation itself is built from Clebsch-Gordan coefficients. "Density" here is not an alternative to representation theory; it IS representation theory under a different name | **Accepted.** This reframes what this whole line of inquiry (C117's pearl, this round) was actually asking -- corrected in the pearl_registry entry below. |
| **FATAL: C114's own already-committed data refutes density as THE mechanism.** At j2=3/2, dimension and spectral density are FIXED (one matrix, 130-dim), and all 16 remove-one components have IDENTICAL Frobenius norm (1.75, confirmed) -- yet outcomes range from exactly real (`3.06e-15`) to `3.04e-4`, an 11-order-of-magnitude spread, with the corner itself only a middling `1.06e-5`, 28x weaker than the strongest breaker in its own cell. Same dimension, same density, same perturbation norm, wildly different outcomes -- only the `(a,b)` label distinguishes them | **Accepted as fatal to the density hypothesis's explanatory scope.** claim.md's own pre-existing limitation ("does not explain within-cell variation") is not a minor scoping choice -- it is exactly the part of the phenomenon a representation-theoretic account (the label-dependent asymmetric rule) explains and density cannot. Density and the rep-theoretic rule are not competing explanations of the SAME question; density (even if real) leaves the actual asymmetric-rule pattern completely unexplained. |
| **No negative control was run.** A random non-normal matrix family with matched dimensions and matched `\|\|E\|\|_2=1` would very plausibly show the SAME `s*` downward trend from pure extreme-value statistics (more eigenvalues -> earlier first exceedance by counting alone) -- `s* * dim = 43.5, 59.8, 28.5, 51.4, 32.0`, roughly consistent with a trivial `s* ~ 1/dim` null with no group theory content at all | **Accepted, the test as designed cannot discriminate the density hypothesis from a content-free counting null.** The cheapest actually-discriminating test (named by skeptic, NOT run this round): build a random matched-dimension non-normal matrix family, run the identical sweep. If it shows the same trend, `s*` measures nothing about THIS operator family specifically. |
| An anomaly the reduction discarded: `max_im` AT s=1 (full corner removal, identical relative perturbation at every cell) is itself non-monotone and ANTI-correlated with dimension (`1.36e-3, 1.06e-5, 3.04e-4, 1.07e-4, 3.80e-5`) -- the largest cell breaks reality 36x more WEAKLY than the smallest, opposite to what "denser spectrum -> easier collision" would predict for the collision's eventual magnitude | **Accepted, recorded as an open anomaly, not explained by density either.** |
| A genuinely interesting free finding the single-number reduction discarded: the real-restoration islands occur at EXACTLY `j2 in {3/2,2}` and nowhere else -- precisely the two cells this whole investigation (C114-C117) already identified as the narrow window where single-component removal sometimes preserves reality | **Accepted, recorded as a new pearl below** -- a density/counting mechanism has no way to "know" which two specific cells this happens at; this is exactly the kind of signal that favors a label-dependent (representation-theoretic) explanation over a density-only one. |
| Reproducibility: no environment/LAPACK provenance in `results_c118.json`; false precision (16 significant digits reported for a quantity resolved to a 0.05 grid then bisected); no in-script self-check that `s=1` matches C114's independently-committed value (skeptic had to do this by hand) | **Accepted as hygiene gaps for any future round in this family, not fixed retroactively in the already-written JSON** (per this project's convention, raw computed output is not mutated after the fact -- corrections live in this decision.md). |

## What survives (narrow, stripped of interpretation)

> For the corner `(j2,j2)` component, the removal fraction at which
> `max|Im(eigenvalue)|` first exceeds `1e-9` on a 21-point grid
> decreases from `0.639` to `0.073` as cell dimension grows `68 ->
> 436`, roughly consistent with `s* ~ 1/dim` (`s*.dim = 43.5, 59.8,
> 28.5, 51.4, 32.0`). `max_im(s)` is NOT monotone in `s`: real-
> restoration islands (reality returning after an initial crossing)
> occur ONLY at `j2 in {3/2, 2}` -- exactly the two cells previously
> identified as the narrow reality-preservation window -- and nowhere
> else. `\|\|Delta_H\|\|_2 = 1` exactly at every cell (proven, not
> merely observed), ruling out a growing-perturbation-norm confound
> specifically.

## What does NOT survive (retracted)

- **"The density hypothesis is supported."** The test cannot
  distinguish this operator family from a content-free extreme-value
  counting null (no negative control run); "density" here is itself
  representation-theoretic (multiplicities + CG coefficients), so the
  framing "no group theory required" is incoherent; and C114's own
  fixed-density, fixed-norm, 11-order-of-magnitude within-cell spread
  is direct evidence AGAINST density as the (or even a) primary
  mechanism for the pattern this whole line of inquiry set out to
  explain.
- **The specific `s*` numbers as one comparable trend.** Non-monotone
  `max_im(s)` means the 5 values are not the same kind of quantity;
  the one "tolerated" reversal is a single-grid-point artifact, not a
  measured signal.

## Kill Analysis (per Anti-Overfitting Gate discipline)

**What was killed:** the specific claim "spectral density [alone]
explains the asymmetric-rule pattern, no representation theory
required," at the level of rigor this crude two-attempt test could
provide.

**What was NOT killed:** that SOME density/conditioning effect
contributes to the overall collapse trend at large `j2` -- genuinely
still open, requires the negative control and the `kappa(V)`
measurement named below, neither attempted.

**What survives as a new pearl, not this round's finding but
generated by it:** the real-restoration islands appearing at exactly
`j2 in {3/2,2}` and nowhere else in the corner-component sweep is a
free, falsifiable, undiscussed-until-now data point that favors a
label-dependent mechanism over a density-only one -- recorded in
`pearl_registry/INDEX.md`.

## What this does NOT show

- Does not establish OR refute the density hypothesis at a rigorous
  level -- the two cheap attempts made (global-min-gap; single
  removal-fraction sweep with no negative control) were both
  insufficient, for different reasons (a genuine substrate failure,
  then a genuine inferential gap).
- Does not explain the asymmetric-rule pattern (which components break
  vs. stay real, at a GIVEN cell) -- explicitly out of scope from the
  start, and now additionally shown to be the exact part density
  cannot reach even in principle (per C114's fixed-density spread).
- Does not change N_gen=3's CONDITIONAL status; stays entirely
  internal to S3, touches neither S6 nor triality.
- Does not solicit Tom Lawrence's Part 5.

## Named, unattempted next steps (per skeptic, in cost order)

1. **Negative control** (cheapest, ~20 lines, NO symbolic CG
   construction needed -- random non-normal matrices, matched
   dimension and `\|\|E\|\|_2=1`): if it shows the same `s* ~ 1/dim`
   trend, the whole `s*`-vs-dimension approach is retired for this
   family, cheaply and definitively.
2. Record `kappa(V)` (eigenvector condition number) per cell alongside
   `s*`, to separate the density confound from the non-normality
   confound.
3. Fine rescan of `[0, s*]` at >=1000 points per cell, to find the
   TRUE first crossing rather than a 0.05-grid-limited one.
4. Resolve the j2=2, `s=0.15` point specifically (higher precision,
   orthogonal-similarity invariance check, conjugate-pair sanity
   check) -- decides whether the reversal is real or artifact.
5. In-script self-check asserting `\|\|Delta_H\|\|_2 == 1` and cross-
   checking the `s=1` endpoint against the relevant prior round's own
   committed JSON, rather than relying on manual cross-checks.

**None of these attempted this round** -- explicitly deferred to a
user decision, given the original "cheap ~30 min check" framing has
already been exceeded twice (v1's substrate failure, v2's inferential
gap) and further investment should be a deliberate choice, not
another silent continuation.

## Verification

- `ruff check experiments/20260831-c118-eigengap-density-check/` --
  clean (v2 script).
- v1 script deleted before commit, per Substrate Gate -- not part of
  the committed artifact set.
- Independently re-verified by FL Step 8a skeptic (context-blind):
  bit-for-bit cross-check of 2 endpoints against C114's own committed
  data; hand-derivation of `\|\|Delta_H\|\|_2=1`; full non-monotonicity
  audit of all 5 `coarse_scan` arrays.
- Full pytest suite run before commit.
