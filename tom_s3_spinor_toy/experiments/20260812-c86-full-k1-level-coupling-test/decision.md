# decision -- first n=0<->n=1 joint test built and run; clean NULL for C79-C83's existing coupling postulate

## Verdict

`FULL_K1_LEVEL_CONSTRUCTED_AND_VERIFIED__N0_N1_JOINT_COUPLING_TEST_CLEAN_NULL_BOTH_TRIPLES`
-> **P1 CONFIRMED (D_S3 construction matches round67's target exactly
for both physical n's). P2/P3 CONFIRMED (no crossing, both candidates).**
**Date:** 2026-08-12 · L0: descriptive · script:
`c86_full_k1_coupling.py`, results: `results_c86.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** D_S3 construction | reproduces D=1.5 (mult 2, n=0 sigma=+1) and D=-2.5 (mult 6, n=1 sigma=-1) | **CONFIRMED, exact** -- `dbar_pr_hermiticity_residual=0.0`, D_S3's own eigenvalues `[-2.5 (mult 6), 1.5 (mult 2)]`, matching round67's closed-form target for both physical n's living in level k=1. | [VERIFIED-numpy] |
| **P2** self-dual triple | no crossing | **CONFIRMED** -- `compressed_n_crossings=0`, global min `0.000137` at `eps=0.275` (a genuine avoided crossing, not a zero), 0 non-artifact full-spectrum crossings. | [VERIFIED-numpy] |
| **P3** anti-self-dual triple | no crossing | **CONFIRMED** -- `compressed_n_crossings=0`, global min `0.000137` at `eps=-0.275` (mirror-symmetric to P2, as expected), 0 non-artifact crossings. | [VERIFIED-numpy] |

## What was genuinely achieved

**The first-ever test of whether C79-C83's existing coupling postulate
mixes different physical Peter-Weyl levels.** Level k=1's own full
8-dimensional S3 Hilbert space was built from C85's certified substrate
and independently verified to reproduce BOTH physical n=0's sigma=+1
branch (D=1.5, total multiplicity 2) AND physical n=1's sigma=-1 branch
(D=-2.5, total multiplicity 6) simultaneously -- something the entire
C79-C85 arc could never test before, since every prior round's n=0
construction used a bare scalar approximation with no orbital structure
at all. The coupling operator T = sum Z_i (x) Leibniz(g_i), tested on
this genuinely richer joint space (512-dim with S6, via C81's exact
raw-kernel-excluded methodology, generalized from a scalar D_S3 block to
a real 8x8 matrix block), produces a clean null for both round119
`so(4)_1` candidate triples -- no evidence of n=0<->n=1 mixing for this
specific, already-extensively-tested coupling construction.

## Why this was not a foregone conclusion

T's construction (Z_i acting on the r/Delta_m index, identity on the
orbital p,q indices) does NOT trivially imply "no coupling to orbital
structure" -- D-bar's own eigenspaces are genuine (r,p)-MIXED
combinations (Meier's basis pairs), so T preserving p as a separate
tensor factor does not automatically mean T preserves D-bar's own
eigenbasis. This had to be checked numerically, and was -- following
this session's own repeated lesson (Meier's eq 6.3 transcription error,
C85) that structural claims about representation-theoretic constructions
must never be trusted by hand-argument alone.

## Kill Analysis

**Killed:** round119's `so(4)_1` self-dual and anti-self-dual triples,
as candidates for genuine n=0<->n=1 inter-level mixing via C79-C83's own
coupling construction -- extends, not merely repeats, their already-
established n=0-only null result to a genuinely richer test.

**Not killed:** the possibility that a DIFFERENT coupling ansatz --
specifically, one built from the orbital generators `l_{e_i}` themselves
(certified in C85, genuinely level-dependent) rather than round67's
level-independent `Z_i` -- could produce inter-level mixing. This
remains a distinct, untested postulate, named explicitly as a possible
future direction, not attempted here.

**What survives as a genuinely scoped next step:** extending this same
joint-level test to k=2 (testing n=1<->n=2, and simultaneously
re-confirming n=0-independent behavior at a third level); testing the
remaining `so(8)` complement candidates (C75's 10-dim, C83's 9-dim
remainder) against this same k=1 joint space, for direct comparison with
their own n=0-only results; or building the genuinely different
orbital-generator-based coupling ansatz named above.

## What this does NOT show

1. Does **not** test k>=2, or n=1<->n=2 (or higher) mixing.
2. Does **not** test any coupling candidate beyond round119's `so(4)_1`
   pair.
3. Does **not** rule out inter-level mixing for a genuinely different
   coupling construction (e.g. orbital-generator-based).
4. Does **not** change `N_gen=3`'s CONDITIONAL status.
5. Does **not** solicit or reference Tom Lawrence's unpublished Part 5.

## Reproduction

```
python experiments/20260812-c86-full-k1-level-coupling-test/c86_full_k1_coupling.py
```
Reuses C85's `build_l_matrices`/`right_mult_matrix_on_ab`/`build_dbar`
(certified, repaired variant), C79's `get_bridge_to_sigma`/
`self_dual_anti_self_dual_triples`/`SO4MOD`/`leibniz_matrix`, round67's
`clifford_generators`, and C73's `build_numeric_dirac`, all unmodified.
C81's raw-kernel-excluded methodology is generalized (not copy-pasted)
from a scalar `d_s3_scalar` to a genuine matrix `D_S3` block.
