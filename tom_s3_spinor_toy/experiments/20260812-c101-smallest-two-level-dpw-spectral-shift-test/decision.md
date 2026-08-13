# C101 decision — genuine spectral shift found; coupled spectrum stays exactly real (unexplained, flagged as open); one self-caught eigensolver bug

**Verdict:** `SPECTRAL_SHIFT_FOUND__CONSTRUCTION_NOT_INERT_R_UNTOUCHED_ANSATZ_UNVERIFIED`
**Status:** RESOLVED — first genuine multi-level spectral result for task #59, one real bug self-caught mid-round

---

## Same-day correction: eigensolver bug found via P0's own reuse check

First run used `np.linalg.eigvalsh` (which assumes Hermitian input and
silently reads only one triangle of the matrix) to compute
eigenvalues of `D-bar`. **`D-bar` is real-SPECTRUM (per Meier eq 6.4,
certified in C85) but is NOT itself a symmetric/Hermitian matrix** --
verified directly (e.g. for `k=2`, entry `(1,2)=-2` but entry
`(2,1)=-4`, not symmetric). Using `eigvalsh` on this non-symmetric
matrix silently produced WRONG eigenvalues for `k=2` specifically
(`{-3:3,-2:6,-1:3,3:3,5:3}` instead of the certified `{-2:12,4:6}`) --
caught immediately by this round's own P0 reuse-sanity check (which
exists exactly to catch this class of error), not discovered later.
`k=1` happened to still produce approximately-correct-looking output
under the wrong solver, which could easily have masked the bug had P0
only spot-checked one level. **Fixed** by switching to
`np.linalg.eigvals` (the general, non-Hermitian-assuming solver),
matching C85's own established convention exactly (C85 never used
`eigvalsh`, always `eigvals` + `real()`). Re-verified: `D1_full`,
`D2_full` now reproduce C85's own certified eigenvalues exactly, with
zero imaginary-part residual.

**This also invalidated an earlier claim.md-adjacent assumption**
(not in the final claim.md, caught before writing it) that
`[[A,B†],[B,C]]` is "Hermitian by construction" -- that reasoning
requires `A`, `C` to be Hermitian to begin with, which `D-bar` is not.
P1 was reframed accordingly (see below) as a genuine, non-guaranteed
question, not a trivial implementation check.

## Results

| # | Prediction | Outcome |
|---|---|---|
| P0 (reuse sanity) | `D1_full`, `D2_full` individually reproduce C85's certified eigenvalues | **PASSES** (after the eigensolver fix) -- `{-1:6,3:2}` and `{-2:12,4:6}` exactly, zero imaginary residual. |
| P1 (real spectrum, reframed as a genuine open question, not "guaranteed by construction") | does `D_PW = [[D1_full, B†],[B, D2_full]]` have a real spectrum? | **YES -- exactly real** (`max|Im| = 0.0` exactly, not merely small). This is a striking, NOT fully explained result -- see "Open question" below. |
| P2 (the actual test) | coupling shifts eigenvalues relative to the uncoupled union | **YES** -- max shift `≈5.08` (comparing paired-by-rank against the uncoupled union `{-2:12,-1:6,3:2,4:6}`), a substantial, genuine spectral effect. |

## The actual spectral-shift finding, in detail

Uncoupled union (`B=0`): `{-2: mult 12, -1: mult 6, 3: mult 2, 4: mult 6}`.

Coupled `D_PW`: `-2` mult drops from 12 to **exactly 6** (6 states stay
pinned at exactly `-2`, 6 shift away into a spread from `-2.49` to
`-2.05`); `-1` (mult 6) is entirely shifted away (no states remain at
exactly `-1`, spread from `-1.15` to `-0.55`); `3` (mult 2) shifts
entirely away (spread `3.03`-`3.05`); `4` mult drops from 6 to
**exactly 2** (2 states stay pinned exactly at `4`, 4 shift into a
spread from `4.05` to `4.16`).

**Every level-1 eigenvalue (`-1`, `3`) shifts completely** -- consistent
with C100's own finding that `M_1` is an injective embedding of ALL
of level 1's `(q,p)` states into level 2 (nothing in level 1 is left
untouched by the coupling). **Only a SUBSET of level-2's eigenvalues
shift** (6 of 12 at `-2`, 4 of 6 at `4`) -- consistent with `B` having
rank at most 8 (its shape is `18x8`), leaving part of level 2's own
space outside the coupling's reach, protected at its original
eigenvalue. The exact split (6/12 and 4/6, not the naive `18-8=10`
one might guess from a crude rank count) was not independently
re-derived by hand here -- reported as computed, not extrapolated from
an unverified rank formula.

## Open question this round surfaces (not resolved here)

**Why is the coupled spectrum EXACTLY real**, given `D-bar` itself is
not Hermitian and there was no a priori guarantee `[[A,B†],[B,C]]`
would produce real eigenvalues for non-Hermitian `A`,`C`? Two
possibilities, neither checked here: (a) `D-bar` may be similar to a
Hermitian matrix via some fixed similarity transform `S` (`D-bar =
S·H·S⁻¹`), and `B`'s own construction may happen to respect the same
`S` consistently across levels, which would make real-spectrum a
structural (provable) fact rather than a coincidence of this one
`k=1,2` case; (b) it could be specific to this particular pair of
levels and not generalize. This is exactly the kind of "unexpected but
testable" observation this project's own Pearl Registry discipline
exists for -- flagged here, not chased further in this already-large
round. A cheap next check: repeat at `k=2,3` and see if the coupled
spectrum stays exactly real there too.

## Practical consequence for task #59

This is the first genuine multi-level spectral result in the entire
C90-C101 arc: a concretely-built, verified 2-level `D_PW`, under the
explicitly-flagged "r-untouched" ansatz, produces a real, substantial
spectral shift when the multiplication-operator coupling is turned on
-- proof that this general construction approach is NOT spectrally
inert, addressing the actual question C90's own decision.md scoped as
the endpoint of this work. **This does not yet establish that
`r`-untouched is the physically correct hypothesis** (see claim.md's
Counterfactual Frame) -- it establishes that IF it is (or is close to
it), the resulting operator has genuine, non-trivial spectral
behavior worth taking seriously, rather than being a degenerate/inert
construction.

## What this cannot show

- Does not establish `r`-untouched as the physically correct
  hypothesis -- one candidate, explicitly flagged (see claim.md).
- Does not run a genuine multi-level (3+) truncation-convergence test
  -- only the smallest possible 2-level instance.
- Does not explain WHY the spectrum stays exactly real -- flagged as
  an open question, not resolved.
- Does not sum over the other three `D^1_{a,b}` components.
- Does not change `N_gen=3`'s CONDITIONAL status.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## Verification

- `ruff check experiments/20260812-c101-smallest-two-level-dpw-spectral-shift-test/`
  — clean, 0 errors.
- P0's own reuse-sanity check caught a real eigensolver bug before any
  conclusion was drawn from it -- exactly the mechanism it was
  designed for.
- All eigenvalue computations use the general (non-Hermitian-assuming)
  `np.linalg.eigvals`, matching C85's own established convention, not
  a new/different solver choice.
