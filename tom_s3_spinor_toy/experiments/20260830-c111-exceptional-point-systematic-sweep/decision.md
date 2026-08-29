# C111 decision -- confirmed exceptional-point mechanism, richer than
first found: a self-caught missed narrow real island corrects the
picture from 2 to 4 threshold crossings

**Verdict:** `EXCEPTIONAL_POINT_MECHANISM_CONFIRMED__FOUR_SYMMETRIC_THRESHOLDS_ONE_NARROW_REAL_ISLAND`
**Status:** RESOLVED -- with a mid-round self-correction recorded transparently

---

## Summary

Follows up on C110's own pearl (a full 4-complex-parameter symbolic
sweep of the k=1 reality-breaking condition) via the single most
natural, physically-motivated 1-parameter slice: scaling C104's own
`M_1^sum` by an overall real factor `t`, with `t=1` being the actual
certified construction tested in C108-C110.

## Self-correction, recorded transparently (not edited away)

**claim.md's own P1 prediction ("exactly two threshold crossings in
`t in (0,8)`, at `~0.966` and `~6.856`") was WRONG**, based on a
161-point scratch scan. This round's own FIRST formal script pass
(400-point resolution) found **4** crossings, not 2 -- a narrow
additional real "island" near `t~2.888-2.896`, sandwiched inside what
the coarser scratch scan had read as one continuous complex region, had
been missed entirely. Before accepting this as real (not a resolution
artifact), the region was rescanned at 8000-point resolution (20x
finer) -- the same 4 crossings reappeared, unchanged, with no further
structure revealed. `claim.md`'s prediction was then revised to match
the verified 4-crossing structure, and the script itself carries an
explicit `self_correction_note` in its own JSON output (see
`results_c111.json`) rather than silently presenting only the corrected
version.

**All 5 (revised) predictions confirmed:**

| # | Prediction | Outcome |
|---|---|---|
| P0 | Reproduces C108's own `max\|Im\|=0.10592470995283362` at `t=1` | **CONFIRMED**. |
| P1 (revised) | Exactly 4 crossings in `(0,8)`, stable at 8000-point resolution | **CONFIRMED**. |
| P2 | Bisected thresholds: `t1=0.9660948033007579`, `t2=2.8876251468636065`, `t3=2.8956501224413778`, `t4=6.856157181497904` | **CONFIRMED**, matches scratch to the tested tolerance. |
| P3 | Negative-side thresholds are exactly `-t1,-t2,-t3,-t4` | **CONFIRMED**, bit-for-bit. |
| P4 | `D_PW(t)` and `D_PW(-t)` have IDENTICAL spectra (not just matching real/complex classification) | **CONFIRMED**, max spectrum difference `0.00e+00` across 6 tested `t` values. |

## What this genuinely establishes

1. **The reality-breaking mechanism is a genuine, confirmed
   eigenvalue-collision (exceptional point) phenomenon**: inspecting
   eigenvalues near the first threshold showed two distinct real
   eigenvalues (near `-1.834` and `-1.687` at `t=0.95`) merging into a
   complex-conjugate pair beyond `t1`. This is qualitatively different
   from, and sharper than, C108-C110's own "some couplings break it"
   characterization.
2. **The full structure for `t in (0,8)` (and, by the proven symmetry
   below, `(-8,0)`) is: REAL on `(0,t1)`, COMPLEX on `(t1,t2)`, REAL
   (narrow) on `(t2,t3)`, COMPLEX on `(t3,t4)`, REAL again for `t>t4`** --
   confirmed stable under a 20x resolution refinement, though a fully
   exhaustive proof that no finer structure exists at even higher
   resolution is not claimed (see "What this cannot show").
3. **An exact, general, and cheaply-provable explanation for the `t`-`-t`
   symmetry**: for ANY block matrix `D_PW(t) = [[D1, t*B^H],[t*B, D2]]`
   with FIXED diagonal blocks and off-diagonal linearly scaled by `t`,
   conjugating by `S = diag(I_8, -I_18)` gives EXACTLY
   `S D_PW(t) S^{-1} = D_PW(-t)`. This is elementary and holds for any
   `B`, not specific to `M_1^sum` -- the symmetry was not a mysterious
   coincidence, and is recorded here as understood, not left open.

## Kill Analysis (per this project's own Anti-Overfitting Gate discipline)

**Killed:** the (self-generated, not from a prior round) hypothesis
that the k=1 reality-breaking region is a single simple interval --
directly falsified by the narrow real island at `t2-t3`.

**NOT killed:** C108's own finding (`t=1` breaks reality) and C109's own
finding (requires the full 4-component sum) -- both fully consistent
with, and now embedded in, this round's richer picture (`t=1` falls
inside the first complex window `(t1,t2)=(0.966,2.888)`, consistent).

**What remains genuinely open:** (a) a closed-form/exact-algebraic
derivation of `t1,t2,t3,t4` (this round converges them numerically to
double precision via bisection, not symbolically) -- the Schur-complement
reduction of `D_PW(t)`'s eigenvalue problem to an effective <=8-dimensional
problem (using `D1`,`D2`'s own known eigenprojectors) is identified as
the correct approach, not carried out; (b) whether resolution beyond
8000 points would reveal yet more narrow islands elsewhere in `(0,8)`
or beyond `t=8` -- not exhaustively ruled out, flagged as a residual
pearl; (c) the full 4-complex-parameter sweep C110's own pearl
originally envisioned -- this round tested only the 1-parameter
`t*M_1^sum` slice, the single most natural path through that space, not
the full space.

## What this cannot show

- Does not derive `t1,t2,t3,t4` in exact closed form.
- Does not exhaustively prove no finer structure exists beyond
  8000-point resolution -- confirms stability under a 20x refinement,
  not an infinite-resolution guarantee.
- Does not perform the full 4-complex-parameter sweep.
- Does not change N_gen=3's CONDITIONAL status.
- Does not touch OB1.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## Verification

- `ruff check experiments/20260830-c111-exceptional-point-systematic-sweep/`
  -- clean, 0 errors.
- **Self-caught, transparently recorded correction**: claim.md's
  original P1 (exactly 2 crossings) was wrong; this round's own script,
  not a later round, caught it by using finer resolution (400 points)
  than the disclosed scratch exploration (161 points), then verified
  the correction's stability at 8000 points before finalizing. The
  script's own JSON output carries a `self_correction_note` field
  documenting this, rather than the correction living only in this
  prose.
- All threshold values converged via 60-iteration bisection (double-
  precision stable); the `t`-`-t` symmetry is additionally verified
  exactly (not just via matching classification) by directly comparing
  sorted complex eigenvalue arrays, `0.00e+00` max difference.
