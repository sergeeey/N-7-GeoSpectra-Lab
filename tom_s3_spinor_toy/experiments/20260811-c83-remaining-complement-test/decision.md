# decision -- exact 1-dim su(3) overlap found in so(4)_1+so(4)_2; genuine 9-dim remainder computed and tested clean; full 20-dim complement now exhausted

## Verdict

`SU3_OVERLAP_FOUND_EXACT__GENUINE_9DIM_REMAINDER_COMPUTED_RANK_AWARE__ALL_3_GROUPS_CLEAN_NULL__FULL_20DIM_COMPLEMENT_NOW_EXHAUSTED`
-> **P1 CONFIRMED (overlap exact, machine precision). P2 CONFIRMED
(9-dim remainder, rank-aware, verified three independent ways during
scoping). P3/P4/P5 CONFIRMED (no crossing, all three groups).**
**Date:** 2026-08-11 · L0: descriptive · script:
`c83_remaining_complement.py`, results: `results_c83.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** overlap direction | a specific combination of `so(4)_1+so(4)_2`'s 12 generators commutes with `D` exactly | **CONFIRMED, exact** -- found via joint SVD (coefficients `-1/sqrt(6)` on `so(4)_1`'s `e23` and `so(4)_2`'s `e03`), `[D, Leibniz(overlap_dir)] = 2.787e-16` (machine precision). | [VERIFIED-numpy] |
| **P2** remaining-dim | exactly 9-dimensional, rank-aware | **CONFIRMED, exact** -- `so(4)_1+so(4)_2`'s shadow within the 20-dim complement has rank `11` (SVD singular values: six at `1.414`, four at `1.0`, one at `0.816`, one at `0` -- the zero one confirms exactly 1 direction has NO complement-shadow, consistent with P1's finding); remaining dim `20-11=9`, extracted basis verified orthonormal (`gram_identity_residual=5.5e-16`) and zero-overlap with `so(4)_1+so(4)_2`'s shadow (`4.6e-16`). | [VERIFIED-numpy] |
| **P3** group `[0,1,2]` | no crossing | **CONFIRMED** -- `compressed_n_crossings=0`, closest approach `0.002027` at `eps~=-0.495`, fine-scan confirms a clean avoided crossing (smooth V, no sign change). | [VERIFIED-numpy] |
| **P4** group `[3,4,5]` | no crossing | **CONFIRMED** -- `compressed_n_crossings=0`, closest approach `0.000266` at `eps~=1.105`, fine-scan confirms avoided crossing. | [VERIFIED-numpy] |
| **P5** group `[6,7,8]` | no crossing | **CONFIRMED** -- `compressed_n_crossings=0`, closest approach `0.000590` at `eps~=-1.830`, fine-scan confirms avoided crossing. | [VERIFIED-numpy] |

**Full-spectrum cross-check for all three groups: ZERO near-zero
eigenvalues found across the entire sweep** (not even raw-kernel
artifacts, unlike `so(4)_1`/`so(4)_2` which each showed several) --
these generic, non-block-structured generators apparently do not align
with the raw kernel strongly enough to produce even the artifact pattern
within the swept range. Reported as observed, not investigated further.

## The new finding, and why it does not contradict C77

**`so(4)_1+so(4)_2` (round119's full `SO(4)xSO(4)` candidate, 12
generators) has an EXACT 1-dimensional intersection with `su(3)` itself**
-- a specific linear combination that commutes with the physical `D`,
found and verified to machine precision. C77's own claim ("all 12
generators fail Gate 2") is about the 12 BASIS elements individually,
tested one at a time -- that claim remains fully correct; not one of the
12 basis generators, alone, commutes with `D`. This round's finding is
about a SPECIFIC LINEAR COMBINATION of them, invisible to a basis-by-
basis test, and does not contradict C77 -- it reveals additional
structure C77's methodology could not see.

**Physical/structural interpretation, offered tentatively, not
over-claimed:** this 1-dim commuting direction is a genuine `u(1)`
subalgebra of `so(4)_1+so(4)_2` respected by `D` -- a small but real
piece of extended symmetry beyond bare `su(3)`. No physical
identification (gauge charge, etc.) is offered or investigated here.

## What this means for the complement's coverage

C78 established the commutant of `D` within `so(8)` is exactly `su(3)`
(8-dim), complement 20-dim. `so(4)_1+so(4)_2`'s EFFECTIVE testing power
within the complement is only 11-dim (not 12, because of the su(3)
overlap just found) -- leaving a genuine, previously entirely untested
9-dim remainder, computed rank-aware (not via a naive projection, which
this round's own scoping caught giving an inconsistent answer -- see
"Method note" below) and tested here in full, three groups of three,
under C81's corrected methodology.

**Combining C75 (round124's 10-dim candidate), C77+C79-C82 (round119's
12-dim candidate, 11 effective dims within the complement), and C83
(the remaining 9 dims): every dimension of C78's 20-dim `so(8)`
complement has now been tested against the physical `D`, either via
direct commutator (Gate 2, C75/C77) or via the corrected non-product
coupling test (C79-C83).** No candidate has produced a genuine,
verified crossing anywhere in the entire complement, for this specific
`Z_i`-coupling construction restricted to `S3`'s `n=0` sector.

## Method note (a genuine correction made during this round's own scoping, not smoothed over)

Computing "the 9-dim remainder" correctly required real care, worth
recording plainly. Three flawed attempts preceded the correct one:
1. A first attempt truncated SVD coefficients to `.real`, silently
   discarding genuine complex structure -- corrected to match C78's own
   established convention (keep full complex coefficients).
2. A second attempt (projecting complement vectors onto `so(4)_1+
   so(4)_2`'s span in the AMBIENT 64-dim space and taking the residual)
   gave a dimension count consistent across methods (`14`) but a
   residual-outside-complement check FAILED (`0.333`, not `~0`) --
   revealing the construction did not actually stay within the
   complement, an important self-check that caught the error before it
   propagated into the actual test.
3. The final, correct method works entirely in the complement's OWN
   orthonormal coordinate system (not the ambient space), and uses
   SVD (not plain unpivoted QR, which was found to silently mishandle
   the rank-11 deficiency of a nominally-12-column matrix) to correctly
   identify the true rank and its orthogonal complement. This gave `9`,
   matching the original hand-derived expectation, and passed every
   downstream verification (zero overlap, clean Gram identity, nonzero
   `D`-commutators for all 9 new generators).

## Kill Analysis

**Not killed:** C77's own claim (all 12 basis generators individually
fail Gate 2) -- unaffected, still true. C75/C78/C79-C82's own results --
all reused/confirmed, none contradicted.

**Killed:** the three tested groups of the 9-dim remainder, as
candidates for a genuine non-product zero mode via this specific
`Z_i`-coupling construction.

**New, positive structural finding, not a kill:** the 1-dim `su(3)`
overlap within `so(4)_1+so(4)_2` -- a genuine piece of extended symmetry
respected by `D`, previously unknown, logged in the claim ledger and
flagged for possible future physical interpretation.

**What survives, as genuinely scoped next steps:** the full Peter-Weyl
tower (still `S3`'s `n=0` sector only, across every round in this arc);
physical interpretation of the newly-found `u(1)` overlap direction (not
attempted); a completely different coupling construction not based on
`Z_i(x)g_i` at all (not attempted, no specific candidate named).

## What this does NOT show

1. Does **not** test the full Peter-Weyl tower.
2. Does **not** offer a physical interpretation of the newly-found `u(1)`
   overlap direction beyond noting its existence.
3. Does **not** claim the 3-groups-of-3 partition is uniquely privileged
   -- a reproducible, systematic choice, not asserted as the only one.
4. Does **not** change `N_gen=3`'s CONDITIONAL status.
5. Does **not** solicit or reference Tom Lawrence's unpublished Part 5.

## Reproduction

```
python experiments/20260811-c83-remaining-complement-test/c83_remaining_complement.py
```
Reuses C81's `run_for_triple`, C79's `get_bridge_to_sigma`/
`leibniz_matrix`, C78's `G102.so8_basis`, C70's `su3_g102_on_channel_v`,
round59's `build_clifford`/`NOMIZU`, and C73's `build_numeric_dirac`, all
unmodified.
