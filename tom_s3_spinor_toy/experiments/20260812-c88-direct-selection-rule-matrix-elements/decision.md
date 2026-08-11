# decision -- Z_i genuinely connects adjacent Peter-Weyl eigenspaces (a real coupling channel); corrects the reading of C86/C87's own "clean NULL"

## Verdict

`Z_I_HAS_NONZERO_MATRIX_ELEMENTS_BETWEEN_ADJACENT_N_EIGENSPACES__CORRECTS_C86_C87_READING__DOES_NOT_OVERTURN_THEIR_NO_CROSSING_RESULT`
-> **P1 CONFIRMED (D-bar exactly diagonalizable, real eigenvalues,
reconstruction exact to ~1e-15). P2 CONFIRMED (eigenspace dimensions
match round67's target exactly, k=1..4). P3: NONZERO -- a genuine
coupling channel exists.**
**Date:** 2026-08-12 · L0: descriptive · script:
`c88_direct_selection_rule.py`, results: `results_c88.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** diagonalizability | real eigenvalues, exact reconstruction | **CONFIRMED** -- max imaginary part of eigenvalues exactly `0.0` for all k=1..4, reconstruction residual `1.3e-15` to `2.7e-15` (machine precision). | [VERIFIED-numpy] |
| **P2** eigenspace dimensions | (k+2) and k per copy, matching round67's target | **CONFIRMED exactly**, k=1..4 (e.g. k=2: dims 4 and 2, matching (k+2)=4 and k=2). | [VERIFIED-numpy] |
| **P3** matrix elements | genuinely open | **NONZERO for all three generators Z_1, Z_2, Z_3, at every k=1,2,3,4 tested** -- Frobenius norms ranging 1.0 (k=1) to ~2.1 (k=4), growing with k, never even approximately zero (all values order-1, far above any numerical-precision threshold). | [VERIFIED-numpy] |

## What this genuinely establishes, precisely stated

`Z_i`, embedded in `D-bar`'s own `(p,r)` basis via `I_p (x) Z_i`
(the exact construction C79-C86-C87 use as the S3-side factor of their
coupling operator T), has REAL, NONZERO matrix elements connecting
D-bar's own "-k" eigenspace (physical n=k, sigma=-1) to its "+k+2"
eigenspace (physical n=k-1, sigma=+1) -- confirmed directly, without any
S6 factor, eps-sweep, or Hermiticity assumption, at every level tested.
**A genuine S3-side coupling channel between adjacent Peter-Weyl levels
exists**, contrary to the naive first guess (recorded honestly in C86's
own docstring) that T, by only touching the r-index, might trivially
fail to connect different orbital/level structure.

## Why this does NOT overturn C86/C87's own "clean NULL" findings

A nonzero matrix element of `Z_i` within the S3 factor alone is
NECESSARY but not SUFFICIENT for the FULL joint operator
`D_S3 (x) 1 + 1 (x) D_S6 + eps*T` to develop an actual zero eigenvalue as
eps varies -- that also depends on the S6-side `Leibniz(g_i)` structure,
the overall level gap (`D-bar`'s own eigenvalues are separated by
`2k+2`, a real, k-growing gap), and how these combine. C86 (k=1,
properly Hermitian, valid computation throughout) and C87 (k=2, corrected
this same session to use a general eigensolver after the Hermiticity bug
was found) BOTH independently confirm no crossing in the specific joint
operator, eps in [-2,2], for round119's `so(4)_1` triples specifically.
**Both findings are true simultaneously and are not in tension:** a real
coupling channel exists (this round), and it does not happen to produce
an eigenvalue crossing in the specific tested operator (C86/C87,
verified on a corrected computational footing).

## Correction applied to C86/C87's own language

C86's decision.md said "no evidence of n=0<->n=1 mixing for this
specific construction" -- imprecise, now corrected there with a pointer
to this round: the precise statement is "no eigenvalue crossing in the
tested joint operator", not "no coupling channel". This round's finding
is the reason that correction was needed, and is recorded in both C86's
and C87's own decision.md files (methodology-note additions), not
silently absorbed only here.

## Kill Analysis

**Not killed, genuinely established:** a real S3-side coupling channel
between adjacent Peter-Weyl levels, via `Z_i`, at every k tested.

**Not killed:** C86/C87's own "no eigenvalue crossing" findings, now
independently re-confirmed on a corrected computational footing.

**Killed:** the (never explicitly claimed, but implicitly risked)
reading that C86/C87's results meant "no S3-side coupling exists at
all" -- explicitly false, corrected here.

**What survives as a genuinely scoped next step:** understanding WHY
the S6-side structure keeps this real coupling channel from producing
an actual crossing (is it a generic gap-protection effect, or a
coincidence specific to round119's `so(4)_1` candidates?); testing
whether a LARGER eps range, or a different candidate with a stronger
S6-side Leibniz factor, could produce a genuine crossing; and properly
resolving the underlying Hermiticity/normalization question (finding
Meier's own basis's correct Gram matrix) rather than working around it
with a general eigensolver.

## What this does NOT show

1. Does **not** determine whether ANY joint operator, for ANY candidate
   or eps range, ever produces a crossing -- only that this specific
   S3-side channel is nonzero, a necessary but not sufficient condition.
2. Does **not** test k>=5.
3. Does **not** resolve the D-bar Hermiticity/normalization question at
   its source.
4. Does **not** change `N_gen=3`'s CONDITIONAL status.
5. Does **not** solicit or reference Tom Lawrence's unpublished Part 5.

## Reproduction

```
python experiments/20260812-c88-direct-selection-rule-matrix-elements/c88_direct_selection_rule.py
```
Reuses C85's `build_l_matrices`(repaired)/`right_mult_matrix_on_ab`/
`build_dbar`, C86's `ROUND67` reference, all unmodified.
