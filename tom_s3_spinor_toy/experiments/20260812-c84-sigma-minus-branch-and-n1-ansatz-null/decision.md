# decision -- sigma=-1 branch clean NULL (n=0 now fully covered); naive n=1 ansatz explicitly KILLED, correct construction still open

## Verdict

`SIGMA_MINUS_BRANCH_CLEAN_NULL__N0_LEVEL_FULLY_COVERED__NAIVE_N1_ANSATZ_KILLED__CORRECT_N1_CONSTRUCTION_STILL_OPEN`
-> **P1 CONFIRMED (bracket relations exact). P2/P3 CONFIRMED (no crossing,
both candidates). P4 CONFIRMED (naive ansatz does not match, as predicted).**
**Date:** 2026-08-12 · L0: descriptive · script:
`c84_peter_weyl_tower_attempt.py`, results: `results_c84.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** Z_i brackets | `[Z_i,Z_j]=-2*eps_ijk*Z_k` exactly | **CONFIRMED**, all three cyclic triples exact (sympy symbolic). | [VERIFIED-sympy] |
| **P2** sigma=-1, self-dual | no crossing | **CONFIRMED** -- `compressed_n_crossings=0`, global min `7.9e-5` at `eps=-0.475` (avoided crossing, not a zero), 0 non-artifact full-spectrum crossings. | [VERIFIED-numpy] |
| **P3** sigma=-1, anti-self-dual | no crossing | **CONFIRMED** -- `compressed_n_crossings=0`, global min `7.9e-5` at `eps=+0.475` (mirror-symmetric to P2, as expected), 0 non-artifact crossings. | [VERIFIED-numpy] |
| **P4** naive n=1 ansatz | does NOT match round67's target | **CONFIRMED** -- eigenvalues `{-0.5: mult 3, +1.5: mult 1}`, target was `{+2.5: mult 6, -2.5: mult 6}`; dimension 4 vs required 12. | [VERIFIED-numpy] |

## What was genuinely achieved

**n=0's full level, both branches, is now covered** for round119's
`so(4)_1` self-dual and anti-self-dual triples -- the same candidates
tested at sigma=+1 throughout C79-C82. Both branches give a clean,
mirror-symmetric null (the global-minimum eps values are exact negatives
of each other, `-0.475` vs `+0.475`, an internal consistency check that
passed and supports the sigma-flip construction being sound). This closes
out C80's and C83's own named next step for these specific candidates,
though NOT for the full 20-dim `so(8)` complement C83 exhausted at
sigma=+1 only -- extending sigma=-1 coverage to the remaining complement
generators (C75's 10-dim candidate, C83's 9-dim remainder) is a further,
still-open, but now clearly cheap extension (same one-parameter
`d_s3_scalar` flip, reused mechanically) not attempted this round to keep
scope bounded.

## What was genuinely NOT achieved, and why

**The full Peter-Weyl tower (n>=1) remains unresolved.** The naive
`Delta_m (x) V_1` ansatz (the cheapest, most natural first guess) was built
explicitly and diagonalized -- it does NOT reproduce round67's own
closed-form target at n=1 (eigenvalues +-5/2, multiplicity 6 each). Its
own dimension (4) is smaller than the required total (12), which alone
rules it out; the actual eigenvalue pattern found (-0.5 with multiplicity
3, +1.5 with multiplicity 1) is exactly the standard "two spin-1/2's
combined" spin-orbit-coupling result (triplet/singlet split under
`Sigma sigma_i (x) sigma_i`), confirming the computation is correct for
what it computes -- it is simply the wrong representation-theoretic
object for round67's n=1 level.

**Root cause, as far as this round's scoping could establish:** round67's
own closed-form eigenvalue formula was never derived from an explicit
matrix construction anywhere in this codebase -- it was cited from an
external source (Sire & Xu, arXiv:2005.01448) and from the general abstract
Frobenius-decomposition machinery in Agricola's own paper (`L^2(S) =
sum_lambda M_lambda (x) V_lambda`, p.15), neither of which this round had
time to work through to an explicit n=1 matrix. Two hand-derivation
attempts (documented in claim.md) gave inconsistent dimension guesses (4
and 8) before this round settled on testing the cheapest one (4)
numerically rather than continuing to guess -- consistent with this
project's own OB10 discipline (verify, don't hand-derive).

## Kill Analysis (per Anti-Overfitting Gate discipline)

**Killed:** the specific naive `Delta_m (x) V_1`, `L_i=sigma_i/2` ansatz as
a representation of the n=1 Peter-Weyl level's orbital-derivative action.

**Not killed:** round67's own closed-form eigenvalue formula itself
(externally verified, independent of this round's construction attempt);
the possibility that a CORRECT n=1 construction exists (this round tested
one candidate, not the hypothesis that no construction exists at all); the
sigma=-1 branch machinery just built and verified (genuinely extends
coverage, unaffected by the n=1 finding).

**Relaxation Map for the surviving n>=1 question** (one assumption change
per future variant, per the Minimal Relaxation Rule):
- V1: build the full outer(x)inner Peter-Weyl block (`V_n (x) (V_n (x)
  Delta_m)`, dimension `2(n+1)^2`) and project onto the Clebsch-Gordan
  branches, rather than the naive `V_n (x) Delta_m` alone -- this was this
  round's OTHER hand-derivation guess (8-dim at n=1), also not yet verified
  numerically.
- V2: read Sire & Xu (arXiv:2005.01448) directly for an explicit n=1
  construction, rather than re-deriving one from Agricola's abstract
  Frobenius formula.
- V3: consult a classical reference for the Dirac spectrum on round S^3
  specifically (e.g. Bar's work on homogeneous-space Dirac operators),
  which may give the explicit eigenspaces directly rather than requiring
  a from-scratch representation-theoretic construction.

## What this does NOT show

1. Does **not** complete the full Peter-Weyl tower -- n=0 (both branches,
   for the `so(4)_1` candidates) is covered; n>=1 remains open.
2. Does **not** claim no correct n=1 construction exists -- only that this
   round's cheapest first guess fails, with the specific numerical evidence
   recorded (see Relaxation Map above for named next attempts).
3. Does **not** extend sigma=-1 coverage to C75's or C83's other complement
   candidates -- only round119's `so(4)_1` self-dual/anti-self-dual pair,
   for direct before/after comparison with sigma=+1.
4. Does **not** change `N_gen=3`'s CONDITIONAL status.
5. Does **not** solicit or reference Tom Lawrence's unpublished Part 5.

## Reproduction

```
python experiments/20260812-c84-sigma-minus-branch-and-n1-ansatz-null/c84_peter_weyl_tower_attempt.py
```
Reuses C81's `run_for_triple`/`build_t_generator`, C79's
`get_bridge_to_sigma`/`self_dual_anti_self_dual_triples`/`SO4MOD`, round67's
`clifford_generators`/`calibrate_h_H`, and C73's `build_numeric_dirac`, all
unmodified.
