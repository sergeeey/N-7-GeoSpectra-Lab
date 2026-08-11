# C82 -- so(4)_2's two halves, using the corrected (raw-kernel-excluded) test from C81

**Experiment id:** `20260811-c82-so4-2-raw-kernel-excluded-test`
**Date:** 2026-08-11 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C77 (Gate 2 test of the FULL `so(4)+so(4)`, all 12
generators including `so(4)_2`, failed -- but via the OLD, un-diagnosed
test methodology, i.e. simple commutator-with-`D_S6` test, not the
non-product coupling test); C79/C80 (built and diagnosed the non-product
coupling test on `so(4)_1`'s two halves, found the raw-kernel artifact);
C81 (fixed the test design, reconfirmed `so(4)_1`'s two halves are a
clean NULL under the corrected test)

---

## Why this round, and what "so(4)_2" means here precisely

C81 fixed the test design (compress `D_joint` onto `Delta_m (x) D_S6`'s
gapped non-kernel eigenspace before sweeping `eps`) and re-confirmed
`so(4)_1`'s two halves (`BLOCK1=[0,1,2,3]`'s self-dual/anti-self-dual
`su(2)` triples) are a clean NULL. `so(4)_1` was one specific, arbitrary
half of round119's full 12-dim `SO(4)xSO(4)` candidate -- `so(4)_2`
(`BLOCK2=[4,5,6,7]`'s own self-dual/anti-self-dual split, generators
`so4_all[6:12]`) is the OTHER half, structurally symmetric to `so(4)_1`
but built from a different 4-dim octonion block and never tested with
the corrected, non-product coupling methodology (C77's own Gate-2 test
of `so(4)_2` used the OLD, simple-commutator test, which answers a
different question -- "does `so(4)_2` commute with `D_S6` as a symmetry"
-- not "does coupling `S3`'s `Z_i` to `so(4)_2` produce a genuine
non-product zero mode," which is what this round tests).

**Sanity confirmed before running the full pipeline:** `so4_all[6:12]`
splits into genuine `su(2)` triples via the SAME self-dual/anti-self-dual
construction used for `so(4)_1` -- structure constants `-2.0`/`+2.0`,
residual `0.0`, identical to `so(4)_1`'s own result.

## The claim under test

> **C82 (working).** Using C81's own corrected test (raw kernel excluded
> by construction, not filtered post-hoc), do either of `so(4)_2`'s two
> `su(2)` halves produce a genuine non-product zero mode when coupled to
> `S3`'s `Z_i` on the `n=0` sector? **Prediction:** no -- `so(4)_2` is
> structurally symmetric to `so(4)_1` (same self-dual/anti-self-dual
> construction, same octonion-block origin), and C81 found nothing for
> `so(4)_1` under the corrected test; no specific reason distinguishes
> the two blocks in a way that would predict a different outcome. This
> prediction must not be protected if the result differs.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1 (su(2) closure)** | both `so(4)_2` halves close as genuine `su(2)` (already confirmed above, re-verified in-script) | pending |
| **P2 (compressed test, self-dual)** | zero crossings in the raw-kernel-excluded 56-dim space | pending |
| **P3 (compressed test, anti-self-dual)** | zero crossings | pending |
| **P4 (full-spectrum cross-check)** | any near-zero eigenvalues found across the sweep are raw-kernel artifacts (`frac_in_raw_kernel>=0.5`), none are genuine signal | pending |

## kill_criterion

P1 fails if `so(4)_2`'s split does not close as `su(2)` -- would indicate
an indexing error in extracting `BLOCK2`'s generators, must stop and fix.
**P2/P3/P4 are the actual test.** A "no crossing" result matching the
prediction is a genuine, informative negative, completing the picture for
both known octonion blocks under the corrected methodology -- not a
failure of effort. A crossing found here would be a genuinely new,
significant finding (the FIRST candidate to survive the corrected test)
and must receive the same extra scrutiny every unexpectedly positive
result in this arc has received (fine-scan verification that it is a true
crossing and not an avoided one, kernel-overlap check on the eigenvector)
before being trusted.

## What this cannot show

- Does **not** test any candidate beyond `so(4)_2`'s two halves -- other
  elements of C78's 20-dim complement (outside `so(4)_1`/`so(4)_2`
  entirely) and the full Peter-Weyl tower remain untested.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
