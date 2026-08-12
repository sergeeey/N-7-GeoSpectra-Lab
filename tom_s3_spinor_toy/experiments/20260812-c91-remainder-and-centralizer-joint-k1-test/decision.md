# decision -- both C83's remainder and C75's centralizer clean NULL on the joint k=1 space

## Verdict

`P1_REMAINDER_CLEAN_NULL_ALL_3_GROUPS__P2_CENTRALIZER_CLEAN_NULL_ADAPTED_CONSTRUCTION`
-> **P1 CONFIRMED (all 3 groups, zero crossings). P2 CONFIRMED (adapted
2-generator construction, zero crossings).**
**Date:** 2026-08-12 · L0: descriptive · script:
`c91_remainder_and_centralizer_joint_k1.py`, results: `results_c91.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **Setup** | D_S3 reproduces both physical n's at k=1 | **CONFIRMED** -- eigenvalues `-2.5` (mult 6, n=1 sigma=-1) and `1.5` (mult 2, n=0 sigma=+1), matching round67's own target exactly, `both_match=True`. | [VERIFIED-numpy] |
| **P1** remainder, 3 groups | clean NULL | **CONFIRMED**, all 3 groups: `compressed_n_crossings=0`, `nonartifact_full_crossings=0`, `base_is_hermitian=True` throughout (k=1, no Hermiticity correction needed). Closest approaches: `0.000313`, `0.000134`, `0.000026` -- all comfortably above the crossing tolerance (`1e-6`), none flagged. Reproduced C83's own `remaining_info` exactly (`rho=11`, `remaining_dim=9`, `gram_identity_residual=5.5e-16`), confirming this round used the SAME 9-dim remainder, not a re-derived different one. | [VERIFIED-numpy] |
| **P2** centralizer, adapted | clean NULL | **CONFIRMED** -- `compressed_n_crossings=0`, `nonartifact_full_crossings=0`, `base_is_hermitian=True`, closest approach `0.000950`. Centralizer sanity reproduced from C75 unmodified (`centralizer_dim=2`, `abelian=True`, machine-precision commutator). | [VERIFIED-numpy] |

## Same-day correction (documented in claim.md, restated here)

C89's own decision.md named this round's target as "C75's 10-dim
centralizer candidate." That phrasing conflates two different things
that both exist in this project's history: round124's **10-dim**
candidate symmetry (`su(3)+u(1)_a+u(1)_b`, already tested by the
ORIGINAL C75 and found to FAIL Gate 2 against round59's S6-only D --
unrelated to this round) and the **2-dim** abelian centralizer
(`u1_a`, `u1_b`) that this round actually tests, on a different
question (joint-level spectral crossing, not S6-only commutation).
`predictions_before_data.md`'s C89 entry corrected in place to say
"2-dim centralizer" (not "10-dim centralizer"); `C75's 10-dim candidate`
phrasing elsewhere in `CLAIM_LEDGER.yaml` (referring to the full
su(3)+u(1)+u(1) symmetry C75 already tested) was already correct and is
left untouched.

## Reproducibility note

Removing an unused local variable (`su3_flat`, a ruff `F841` fix, no
downstream use) between two runs of this script changed `group_3_4_5`'s
exact closest-approach value by one eps grid step (`0.000163`@`0.875` ->
`0.000134`@`0.950`) -- everything else (crossing counts, other groups,
P2) identical bit-for-bit. Traced to `remaining_info['shadow_singular_values']`
containing genuine near-degenerate values (three at `1.4142135623730954`,
several near `1.0`) -- SVD singular VALUES are unique, but singular
VECTORS within a degenerate subspace are not; run-to-run floating-point
jitter (e.g. multi-threaded BLAS reduction order) can select a different
orthonormal basis within that subspace, changing which specific linear
combinations land in `group_3_4_5` without changing the subspace itself.
Both runs agree on the actual claim (clean NULL, all groups) -- reported
here as a positive robustness check (Perelman-audit no-collapse
discipline: small legal changes, same conclusion), not a defect. Numbers
in the table above are from the second (post-cleanup) run, matching the
committed `results_c91.json`.

## What this adds

**Completes the joint-k=1-space test for every so(8) candidate this
project has ever built**, extending C86 (so(4)_1) and C89 (so(4)_2) to
the two remaining pieces: C83's 9-dim genuinely-untested remainder (now
tested at the richer n=0<->n=1 level, not just n=0's scalar
approximation) and C75's 2-dim centralizer (tested for the first time in
ANY spectral-crossing sense -- the original C75 only checked
commutation with the S6-only D). Combined with C86/C89: **every
dimension of C78's 20-dim so(8) complement, plus the 2-dim centralizer
outside it, has now been tested against the physical joint operator on
the richer k=1 level -- all clean nulls, no exceptions.**

The P2 adaptation (zero-padding a 2-generator abelian pair to fit the
3-generator construction) is explicitly weaker evidence than P1's
genuine 3-generator triples -- flagged in claim.md and repeated here,
not smoothed over. A clean NULL for an ad hoc 2-term sum says less than
a clean NULL for a well-motivated triple.

## Kill Analysis

**Killed:** C83's 9-dim remainder (all 3 groups) and C75's 2-dim
centralizer (adapted), as candidates for n=0<->n=1 mixing via this
project's `T=sum Z_i (x) Leibniz(g_i)` coupling construction, on the
joint k=1 space.

**Not killed:** k>=2 for either candidate; any construction outside the
translation-generator family (per C90's own structural finding, that
family is provably incapable of level-bridging regardless -- but within
one level, as tested here, remains a live, now-exhausted-for-so(8)
question).

## What this does NOT show

1. Does **not** test either candidate at k>=2.
2. Does **not** validate the P2 zero-padding adaptation as a generally
   meaningful construction -- explicitly ad hoc, flagged as weaker
   evidence than P1.
3. Does **not** change `N_gen=3`'s CONDITIONAL status.
4. Does **not** solicit or reference Tom Lawrence's unpublished Part 5.

## Reproduction

```
python experiments/20260812-c91-remainder-and-centralizer-joint-k1-test/c91_remainder_and_centralizer_joint_k1.py
```
Reuses C86's `build_full_level_d_s3`/`check_d_s3_full_matches_target`/
`build_coupling_on_full_level`/`run_full_level_test`, C83's
`build_complement_basis`/`build_remaining_complement_basis`, and C75's
`get_centralizer_generators_on_channel_v`, all unmodified.
