# decision -- so(4)_2's two halves also clean NULL under C81's corrected test; both octonion blocks of SO(4)xSO(4) now exhausted

## Verdict

`SO4_2_ALSO_CLEAN_NULL_BOTH_HALVES__BOTH_OCTONION_BLOCKS_OF_SO4XSO4_NOW_EXHAUSTED_UNDER_CORRECTED_TEST`
-> **P1 CONFIRMED. P2 CONFIRMED (no crossing). P3 CONFIRMED (no
crossing). P4 CONFIRMED (all near-zero eigenvalues are raw-kernel
artifacts).**
**Date:** 2026-08-11 · L0: descriptive · script: `c82_so4_2_coupling.py`,
results: `results_c82.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** su(2) closure | `so(4)_2` splits into genuine `su(2)` triples, matching `so(4)_1`'s own construction | **CONFIRMED, exact** -- self-dual structure constant `-2.0`, anti-self-dual `+2.0`, both residual `0.0`, identical to `so(4)_1`. | [VERIFIED-numpy] |
| **P2** self-dual, compressed | no crossing | **CONFIRMED** -- `compressed_n_crossings=0`. Closest approach: `min|eigval|=0.000742` at `eps=-0.325` -- larger than `so(4)_1`'s own `0.0000789`, but a fine 31-point scan confirms this is ALSO a genuine avoided crossing (clean V-shaped minimum), not a near-miss. | [VERIFIED-numpy] |
| **P3** anti-self-dual, compressed | no crossing | **CONFIRMED** -- `compressed_n_crossings=0`, closest approach `min|eigval|=0.000742` at `eps=+0.325` (exact sign-mirror of P2, matching the opposite structure constant, same pattern as `so(4)_1`'s own C81 result). | [VERIFIED-numpy] |
| **P4** full-spectrum cross-check | no non-artifact signal | **CONFIRMED** -- 8 total near-zero eigenvalues found across the sweep for EACH triple (double `so(4)_1`'s count of 4 -- noted, not investigated further), all classified as raw-kernel artifacts (`frac_in_raw_kernel>=0.5`), zero non-artifact. | [VERIFIED-numpy] |

## What this means

**Both octonion blocks of round119's `SO(4)xSO(4)` candidate -- all 4
`su(2)` halves across `so(4)_1` and `so(4)_2` -- are now clean,
rigorously-confirmed NULLs under C81's corrected (raw-kernel-excluded)
test.** This completes the picture C81 started: not only was the ONE
candidate tested there (`so(4)_1`) a genuine null once the artifact was
properly excluded, but the STRUCTURALLY SYMMETRIC other half of the same
parent candidate (`so(4)_2`) behaves identically. No asymmetry between
the two octonion blocks was found -- consistent with `H` and `H-perp`
playing structurally equivalent roles in the underlying octonion
construction (as they must, by the very symmetry of the Cayley-Dickson
doubling that defines them).

**One noted, unexplained difference:** the closest-approach magnitude is
`~0.000742` for `so(4)_2` vs `~0.0000789` for `so(4)_1` -- roughly 9x
larger -- and the full-spectrum sweep finds 8 near-zero eigenvalues for
`so(4)_2` vs 4 for `so(4)_1`. Both are comfortably far from a genuine
crossing either way, so this does not change the qualitative conclusion,
but the difference itself is not explained and is logged as a pearl
rather than investigated further this round.

## Kill Analysis

**Not killed:** C77's, C79's, C80's, C81's own results -- all consistent,
none contradicted. `so(4)_2` was previously only tested via the OLD
Gate-2 (simple commutator) methodology in C77 (found: does not commute
with `D_S6`, a different question) -- this round is the first to test it
with the actual non-product coupling methodology, and it agrees with
`so(4)_1`'s own corrected result.

**Killed:** both `su(2)` halves of `so(4)_2`, coupled via round67's `Z_i`
on `S3`'s `n=0` sector, as candidates for a genuine non-product zero mode
-- same specific, narrow claim `so(4)_1`'s halves were already killed for
in C81.

**What survives, as genuinely scoped next steps:** other elements of
C78's 20-dim `so(8)` complement OUTSIDE `so(4)_1 (+) so(4)_2` entirely
(the full `so(4)+so(4)` is only 12 of the 20 non-`su(3)` dimensions), and
the full Peter-Weyl tower rather than `S3`'s `n=0` sector alone -- both
already named in C80, neither attempted here or before.

## What this does NOT show

1. Does **not** test any candidate outside `so(4)_1 (+) so(4)_2` -- the
   remaining 8 dimensions of C78's 20-dim complement are untested.
2. Does **not** test the full Peter-Weyl tower.
3. Does **not** change `N_gen=3`'s CONDITIONAL status.
4. Does **not** solicit or reference Tom Lawrence's unpublished Part 5.

## Pearl

The closest-approach magnitude and near-zero-eigenvalue count both scale
up (~9x, ~2x respectively) from `so(4)_1` to `so(4)_2`, with no offered
explanation. Falsifiable prediction: if this reflects a genuine structural
asymmetry rather than numerical happenstance, a third, independent
generator from C78's complement (outside both `so(4)` factors) should show
a THIRD, generically different closest-approach scale -- logged in
`pearl_registry/INDEX.md`.

## Reproduction

```
python experiments/20260811-c82-so4-2-raw-kernel-excluded-test/c82_so4_2_coupling.py
```
Reuses C81's `run_for_triple` unmodified (which itself reuses C79's
`get_bridge_to_sigma`/`leibniz_matrix`/`check_su2_closure` and all of
C79's own module-level reuses).
