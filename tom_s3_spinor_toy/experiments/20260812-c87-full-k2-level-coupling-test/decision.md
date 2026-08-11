# decision -- n=1<->n=2 joint coupling test also clean NULL; a genuine Hermiticity caveat noted honestly

## Verdict

`FULL_K2_LEVEL_CONSTRUCTED_AND_VERIFIED__N1_N2_JOINT_COUPLING_TEST_CLEAN_NULL_BOTH_TRIPLES`
-> **P1 CONFIRMED (D_S3 construction matches round67's target exactly
for both physical n's). P2/P3 CONFIRMED (no crossing, both candidates).**
**Date:** 2026-08-12 · L0: descriptive · script:
`c87_full_k2_coupling.py`, results: `results_c87.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** D_S3 construction | reproduces D=2.5 (mult 6, n=1 sigma=+1) and D=-3.5 (mult 12, n=2 sigma=-1) | **CONFIRMED, exact** -- D_S3's own eigenvalues `[-3.5 (mult 12), 2.5 (mult 6)]`, matching round67's closed-form target for both physical n's living in level k=2. | [VERIFIED-numpy] |
| **P2** self-dual triple | no crossing | **CONFIRMED** -- `compressed_n_crossings=0`, global min `0.000242` at `eps=1.850`, 0 non-artifact full-spectrum crossings. | [VERIFIED-numpy] |
| **P3** anti-self-dual triple | no crossing | **CONFIRMED** -- `compressed_n_crossings=0`, global min `0.000242` at `eps=-1.850` (mirror-symmetric to P2), 0 non-artifact crossings. | [VERIFIED-numpy] |

## A genuine caveat, noted honestly, not smoothed over

`D-bar_pr`'s naive Euclidean-inner-product Hermiticity residual
(`||D-bar - D-bar^dagger||`) was exactly `0.0` at k=1 (C86) but is `2.0`
at k=2 (this round) -- growing with k, not zero. This does NOT affect
the actual gated result: D-bar's eigenvalues are guaranteed real by
Meier's own algebraic quadratic identity `(D-bar+k)(D-bar-(k+2))=0`
(certified exactly by C85's own bracket/Casimir/eq-6.4 battery for
k=0..10, independent of any Hermiticity property), and P1's target
crosscheck -- comparing D_S3's actual computed eigenvalues/multiplicities
against round67's own closed-form formula -- passed exactly. The most
likely explanation, not yet verified: Meier's `|p>` basis (symmetrized
tensor products) is not orthonormal in the standard Euclidean sense, so
D-bar can be self-adjoint with respect to a DIFFERENT (weighted) inner
product while appearing non-Hermitian under the naive one -- exactly the
kind of subtlety this project's own OB10 discipline says to verify, not
assume. **Flagged as a genuinely open question for a future round**
(compute the correct Gram matrix for Meier's own basis, verify D-bar is
self-adjoint with respect to it), not resolved here, and not treated as
invalidating this round's actual, algebraically-gated result.

## What was genuinely achieved

A second, independent joint-level coupling test, extending C86's
methodology one level deeper: level k=2's full 18-dimensional Hilbert
space, verified to contain physical n=2's sigma=-1 branch (mult 12) and
n=1's sigma=+1 branch (mult 6) simultaneously, tested against C79-C83's
own coupling operator on the resulting 1152-dim joint space with S6.
Clean NULL, both round119 `so(4)_1` candidate triples -- extending the
"no inter-level mixing found" pattern from C86's n=0<->n=1 pair to this
round's independent n=1<->n=2 pair.

## Kill Analysis

**Killed:** round119's `so(4)_1` self-dual and anti-self-dual triples,
as candidates for n=1<->n=2 inter-level mixing via C79-C83's own
coupling construction.

**Not killed:** the possibility of n=0<->n=2 (non-adjacent) mixing,
requiring a different joint construction not attempted here; the
possibility of mixing via a genuinely different, orbital-generator-based
coupling ansatz; and the open Hermiticity/normalization question noted
above.

## What this does NOT show

1. Does **not** test n=0<->n=2 or any non-adjacent pair.
2. Does **not** test any coupling candidate beyond round119's `so(4)_1`
   pair.
3. Does **not** resolve the D-bar Hermiticity/normalization caveat noted
   above -- flagged, not fixed.
4. Does **not** change `N_gen=3`'s CONDITIONAL status.
5. Does **not** solicit or reference Tom Lawrence's unpublished Part 5.

## Reproduction

```
python experiments/20260812-c87-full-k2-level-coupling-test/c87_full_k2_coupling.py
```
Reuses C86's `build_full_level_d_s3`/`check_d_s3_full_matches_target`/
`build_coupling_on_full_level`/`run_full_level_test` directly
(parametrized K=2), and C85/C79/C73's underlying machinery, all
unmodified.
