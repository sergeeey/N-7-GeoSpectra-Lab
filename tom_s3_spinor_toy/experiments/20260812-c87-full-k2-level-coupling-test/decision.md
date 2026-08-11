# decision -- n=1<->n=2 joint coupling test: original computation was INVALID (caught and fixed), corrected re-run confirms the same clean NULL

## Verdict

`FULL_K2_LEVEL_CONSTRUCTED_AND_VERIFIED__N1_N2_JOINT_COUPLING_TEST_ORIGINAL_COMPUTATION_INVALID__CORRECTED_REDO_CONFIRMS_CLEAN_NULL`
-> **P1 CONFIRMED (D_S3 construction matches round67's target exactly
for both physical n's -- unaffected by the bug below). P2/P3: original
computation INVALID, corrected re-run CONFIRMS no crossing, both
candidates.**
**Date:** 2026-08-12 · L0: descriptive · script:
`c87_full_k2_coupling.py`, results: `results_c87.json`.

---

## An integrity correction, made the same session, not smoothed over

While scoping the round after this one, a direct check found
`d_s3_full`'s Hermiticity residual is `2.0` at k=2 (nonzero, genuinely
non-Hermitian in the naive Euclidean sense) -- meaning the ORIGINAL
version of this round's own script called `np.linalg.eigvalsh` on a
matrix that was not actually Hermitian. `eigvalsh` silently reads only
the Hermitian part of its input and does not error on a non-Hermitian
matrix, so the original "clean NULL" conclusion, while POSSIBLY still
correct, was reached via a computation that could have produced
ARBITRARY wrong eigenvalues, not merely imprecise ones -- this needed to
be caught before being trusted, not accepted because the printed numbers
looked reasonable.

**Root cause:** Meier's `|p>` basis (symmetrized tensor products) is not
orthonormal. The certified `l_{e3}` (repaired) generator is individually
anti-Hermitian at k=1 (where the repaired and literal forms coincide)
but genuinely NOT anti-Hermitian at k=2 and above -- a real, structural
feature of the construction (confirmed by direct calculation, not a bug
in the C85 repair itself), not yet resolved by finding the correct Gram
matrix for this basis.

**Fix:** `run_full_level_test` (in `c86_full_k1_coupling.py`, reused
unmodified here) was patched to detect non-Hermiticity and fall back to
a general (non-Hermitian) eigensolver, reporting the resulting maximum
imaginary part as an explicit diagnostic. D-bar's own eigenvalues remain
guaranteed real regardless of Hermiticity, via the algebraic quadratic
identity certified in C85 (`(D-bar+k)(D-bar-(k+2))=0`, independent of
any inner-product structure) -- and since `D_S6` genuinely IS Hermitian
and commutes trivially with `D_S3` (different tensor factors), the
UNPERTURBED joint operator's eigenvalues are also guaranteed real. What
was NOT guaranteed, and had to be checked, is whether adding `eps*T`
keeps the perturbed operator's eigenvalues real throughout the sweep.

## Results (corrected re-run)

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** D_S3 construction | reproduces D=2.5 (mult 6, n=1 sigma=+1) and D=-3.5 (mult 12, n=2 sigma=-1) | **CONFIRMED, exact** -- unaffected by the bug (this check never used `eigvalsh`). | [VERIFIED-numpy] |
| **P2** self-dual triple | no crossing | **CONFIRMED by corrected computation** -- `compressed_n_crossings=0`, general eigensolver used (`base_is_hermitian=False`), max imaginary part seen across the entire sweep: `1.53e-14` (machine precision -- the perturbed operator's eigenvalues stayed effectively real throughout, a genuine finding, not assumed), global min `0.000656` at `eps=-1.825`. | [VERIFIED-numpy] |
| **P3** anti-self-dual triple | no crossing | **CONFIRMED by corrected computation** -- same pattern, max imaginary part `1.35e-14`, global min `0.000656` at `eps=1.825` (mirror-symmetric). | [VERIFIED-numpy] |

**The corrected result matches the original (invalid) computation's own
numbers exactly** -- reassuring, but this was NOT knowable in advance;
the original conclusion could just as easily have been wrong. The
methodological fix, not the coincidence of matching numbers, is what
makes this result trustworthy now.

## What C88 adds, and why "clean NULL" needs precise wording

C88 (run the same session) computed the DIRECT matrix elements of `Z_i`
(the S3-side coupling generator) between D-bar's own adjacent-n
eigenspaces, with no S6 factor and no eps-sweep at all. Finding:
**these matrix elements are genuinely NONZERO at k=1 and k=2 alike** (as
well as k=3, k=4, tested for a broader pattern). This means a real S3-
side coupling channel between adjacent Peter-Weyl levels exists -- this
round's own "no crossing" result should be read precisely as "this
specific joint operator's spectrum does not cross zero for eps in
[-2,2]", not as "no coupling exists at all". Both statements are
consistent: a nonzero coupling matrix element is necessary but not
sufficient to produce an eigenvalue crossing in the full joint operator,
which depends on the interplay with `D_S6`'s own structure and the
overall level gap. See C88 for the full analysis.

## Kill Analysis

**Killed:** round119's `so(4)_1` self-dual and anti-self-dual triples,
as candidates for a genuine eigenvalue crossing (n=1<->n=2, joint
S3xS6 operator) via C79-C83's coupling construction -- now on a properly
verified computational footing.

**Not killed:** the S3-side coupling channel itself (C88 shows it is
genuinely nonzero); the possibility that a different candidate, or a
wider eps range, or the still-unresolved Hermiticity/normalization issue
properly fixed (rather than worked around), could reveal a crossing
this test did not find.

## What this does NOT show

1. Does **not** claim no S3-side coupling exists -- C88 shows it does.
2. Does **not** test n=0<->n=2 or any non-adjacent pair.
3. Does **not** resolve the underlying D-bar Hermiticity/normalization
   question -- worked around (general eigensolver) for a trustworthy
   result, not fixed at the source.
4. Does **not** change `N_gen=3`'s CONDITIONAL status.
5. Does **not** solicit or reference Tom Lawrence's unpublished Part 5.

## Reproduction

```
python experiments/20260812-c87-full-k2-level-coupling-test/c87_full_k2_coupling.py
```
Reuses C86's `build_full_level_d_s3`/`check_d_s3_full_matches_target`/
`build_coupling_on_full_level`/`run_full_level_test` directly
(parametrized K=2, including the post-fix general-eigensolver fallback),
and C85/C79/C73's underlying machinery, all unmodified.
