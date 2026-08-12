# decision -- so(4)_2 also clean NULL on the joint n=0<->n=1 test

## Verdict

`SO4_2_FULL_K1_JOINT_TEST_CLEAN_NULL_BOTH_TRIPLES`
-> **P1 CONFIRMED (su(2) closure exact, matching C82's own result).
P2 CONFIRMED (D_S3 construction matches round67's target exactly).
P3/P4 CONFIRMED (no crossing, both triples).**
**Date:** 2026-08-12 · L0: descriptive · script:
`c89_so4_2_full_k1_coupling.py`, results: `results_c89.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** su(2) closure | exact | **CONFIRMED** -- `[g1,g2]=-2*g3` (self-dual) / `+2*g3` (anti-self-dual), residual `0.0` both, matching C82's own result exactly. | [VERIFIED-numpy] |
| **P2** D_S3 construction | matches target | **CONFIRMED** -- D=1.5 (mult 2), D=-2.5 (mult 6), identical to C86's own (candidate-independent, as expected -- this is the S3 side, unaffected by which S6 candidate is tested). | [VERIFIED-numpy] |
| **P3** self-dual | no crossing | **CONFIRMED** -- `compressed_n_crossings=0`, `base_is_hermitian=True` (k=1, no Hermiticity concern here), global min `0.000233` at `eps=0.575`. | [VERIFIED-numpy] |
| **P4** anti-self-dual | no crossing | **CONFIRMED** -- mirror-symmetric, global min `0.000233` at `eps=-0.575`. | [VERIFIED-numpy] |

## What this adds

**Both octonion blocks of round119's `SO(4)xSO(4)` candidate (so(4)_1,
C86; so(4)_2, this round) are now clean NULLs on the genuinely richer
n=0<->n=1 joint test**, extending C82's own n=0-only result the same way
C86 extended C79-C81's. Per C88's own finding, this is not surprising in
one specific sense (the S3-side coupling channel is candidate-
independent and was already known nonzero) but is NOT redundant: whether
THIS candidate's own S6-side Leibniz factor combines with that channel
to produce a crossing is a genuinely candidate-specific question, now
answered (negatively) for so(4)_2 specifically, on a properly verified
computational footing (k=1 is exactly Hermitian, no correction needed).

## Kill Analysis

**Killed:** so(4)_2's self-dual and anti-self-dual triples, as
candidates for n=0<->n=1 mixing via C79-C89's coupling construction.

**Not killed:** C75's 10-dim centralizer candidate and C83's 9-dim
remainder groups, not yet tested on any joint-level space.

## What this does NOT show

1. Does **not** test k>=2 for so(4)_2.
2. Does **not** test the remaining `so(8)` complement candidates
   (C75's 10-dim, C83's 9-dim remainder) on this joint space.
3. Does **not** change `N_gen=3`'s CONDITIONAL status.
4. Does **not** solicit or reference Tom Lawrence's unpublished Part 5.

## Reproduction

```
python experiments/20260812-c89-so4-2-full-k1-level-coupling-test/c89_so4_2_full_k1_coupling.py
```
Reuses C86's `build_full_level_d_s3`/`check_d_s3_full_matches_target`/
`build_coupling_on_full_level`/`run_full_level_test` directly
(K=1, `so4_all[6:12]`), and C79/C73's underlying machinery, all
unmodified.
