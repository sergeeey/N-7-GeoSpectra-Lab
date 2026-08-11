# decision -- raw kernel excluded properly, NO genuine crossing survives for either so(4)_1 half; clean, honest NULL

## Verdict

`RAW_KERNEL_PROPERLY_EXCLUDED__NO_GENUINE_CROSSING_EITHER_HALF__CLOSEST_APPROACH_CONFIRMED_AVOIDED_CROSSING_NOT_ZERO__CLEAN_NULL`
-> **P1 CONFIRMED. P2 CONFIRMED. P3 CONFIRMED (no crossing). P4 CONFIRMED
(no crossing). P5 CONFIRMED (cross-check finds zero non-artifact
crossings, and reproduces the known artifact crossings for a sanity
match).**
**Date:** 2026-08-11 · L0: descriptive · script:
`c81_raw_kernel_excluded_retest.py`, results: `results_c81.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** spectral gap | 36 exact zeros, clean gap to `>=0.8` | **CONFIRMED, exact** -- `D_S6`'s full spectrum: `{-2.0, -1.8257, -0.8165, 0 (x36), 0.8165, 1.8257, 2.0}`. Clean, well-separated gap. | [VERIFIED-numpy] |
| **P2** eps=0 sanity, restricted | compressed `eps=0` min\|eigval\| matches the already-established full-space value | **CONFIRMED, exact** -- `0.3257` in the compressed 56-dim space, matching C79's own full-space `eps=0` result exactly (expected: the raw kernel contributed nothing to that number even in the original, unrestricted test). | [VERIFIED-numpy] |
| **P3** self-dual, restricted | no crossing | **CONFIRMED** -- `compressed_n_crossings=0`. Closest approach: `min|eigval|=0.0000789` at `eps=0.475`, confirmed by a fine 31-point scan around this value to be a genuine **avoided crossing** (level repulsion, V-shaped minimum, turns back up symmetrically) -- not a near-miss that a finer grid would resolve into a real zero. | [VERIFIED-numpy] |
| **P4** anti-self-dual, restricted | no crossing | **CONFIRMED** -- `compressed_n_crossings=0`, closest approach `min|eigval|=0.0000789` at `eps=-0.475` (exact sign-mirror of P3, consistent with the anti-self-dual triple's opposite structure constant). | [VERIFIED-numpy] |
| **P5** full-spectrum cross-check | known artifact crossings reproduced (sanity), zero non-artifact crossings | **CONFIRMED** -- for each triple, the full 128-dim sweep finds exactly 4 near-zero eigenvalues total across the range (a wider net than the single crossing C79/C80 reported, since this round scanned all near-zero eigenvalues at every `eps`, not just the single closest one) -- **all 4, for both triples, have `frac_in_raw_kernel >= 0.5`** (in fact all `>0.99`, matching C79/C80's own reported crossing plus its near-neighbors on the grid), and **zero** have `frac_in_raw_kernel < 0.5`. No hidden non-artifact signal was missed by the compression. | [VERIFIED-numpy] |

## What this means, stated carefully

1. **With the raw-kernel artifact mechanism properly excluded by
   construction (not just filtered after the fact), NEITHER half of
   round119's `so(4)_1` produces a genuine crossing.** This confirms, with
   the correct test design, exactly what C80's own diagnosis predicted:
   the raw kernel was the ENTIRE signal in C79/C80's results, not merely
   a confound sitting alongside a real, smaller effect. Removing it
   leaves nothing.
2. **The closest approach (`eps~=+-0.475`, `min|eigval|~=0.0000789`) is
   confirmed, not just assumed, to be a genuine avoided crossing** --
   the textbook signature of the no-crossing rule for a Hermitian family
   depending on one real parameter (two independent conditions are
   needed to force an exact degeneracy; a single real parameter generically
   only ever gets close). This is itself a clean, physically unremarkable
   fact about the compressed operator's spectrum, not a hidden near-signal.
3. **This is now a genuinely clean, honest NULL** for this specific
   postulate -- not "explained away after the fact" (C79/C80's framing,
   accurate but leaving a lingering "what if we missed something"
   question) but "shown not to exist under a test design built specifically
   so that the known artifact cannot produce a false positive." This is
   the stronger, more defensible form of the same conclusion.

## Kill Analysis

**Not killed:** any of C79/C80's own results -- fully consistent with
and now more rigorously confirmed by this round's properly-designed test.

**Killed, more rigorously than before:** the specific hypothesis that
round119's `so(4)_1` (either half), coupled via round67's `Z_i` on `S3`'s
`n=0` sector, produces a genuine non-product zero mode. C79/C80 already
showed the ONE crossing found was an artifact; this round shows there is
NOTHING ELSE to find once that artifact is properly excluded by
construction, not merely filtered post-hoc.

**What survives, as genuinely scoped next steps (not attempted here,
matching C80's own list):** (a) test `so(4)_2` or other elements of C78's
20-dim complement, now with the CORRECT (raw-kernel-excluded) test design
from the start; (b) escalate to the full Peter-Weyl tower rather than
`S3`'s `n=0` sector alone.

## What this does NOT show

1. Does **not** test any candidate beyond `so(4)_1`'s two halves.
2. Does **not** test the full Peter-Weyl tower -- `n=0` sector only.
3. Does **not** change `N_gen=3`'s CONDITIONAL status.
4. Does **not** solicit or reference Tom Lawrence's unpublished Part 5.

## Reproduction

```
python experiments/20260811-c81-raw-kernel-excluded-retest/c81_raw_kernel_excluded_retest.py
```
Reuses C79's `get_bridge_to_sigma`/`leibniz_matrix`/`check_su2_closure`/
`self_dual_anti_self_dual_triples` and all of C79's own module-level
reuses, unmodified.
