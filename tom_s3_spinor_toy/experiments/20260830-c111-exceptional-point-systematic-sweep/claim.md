# C111 claim -- systematic sweep of C108-C110's k=1 reality-breaking
mechanism: is it a generic algebraic condition, or a specific
eigenvalue-collision (exceptional point) phenomenon?

## L0 gate (EstimandOps)

**Question type:** Descriptive (what is the exact mathematical mechanism
producing the observed effect, as a function of a continuous parameter?).

## Background -- why this round exists, and an honest scope correction

C110's own pearl recommended "a full parametrized symbolic sweep
(treating c1..c4 as free complex symbols, computing the discriminant...
of the characteristic polynomial)" over all 4 CG-component weights.
User asked to carry this out ("сделай систематический перебор").

**Scope correction, made explicit rather than silently substituted:** a
literal 4-complex-parameter symbolic characteristic polynomial for the
full 26x26 `D_PW` matrix is not a computation this round attempted to
force through -- a degree-26 polynomial in `lambda` with coefficients
that are degree-26 polynomials in 4 free complex parameters is far
beyond tractable symbolic manipulation by direct methods. Instead, this
round swept the single MOST NATURAL and physically relevant slice
through that 4-parameter space: the overall real scale `t` of `M_1^sum`
itself (`D_PW(t)` built with off-diagonal block `t*M_1^sum (x) I_r`),
since `t=1` is the actual certified construction (C104/C108) and `t=0`
is the trivial (uncoupled, certainly real) limit -- the most physically
meaningful one-parameter path through the space C110's pearl asked to
explore, chosen over a computationally infeasible full sweep.

## Counterfactual Frame (exploratory round -- disclosed up front)

Cheap interactive scratch exploration (sympy/numpy) was run FIRST. It
found, in order:

1. Scanning `t` from 0 to 1.5 (`D_PW(t)` with off-diagonal
   `t*M_1^sum (x) I_r`): reality holds for `t` roughly in `[0, 0.965)`,
   breaks sharply starting near `t=0.966`, and grows continuously for
   `t>1` -- NOT a sharp jump exactly at the certified `t=1` value, but a
   genuine, continuous bifurcation at a nearby critical `t*`.
2. Bisection pinned this threshold to `t* = 0.9660948033007579`
   (double-precision converged). Inspecting the eigenvalues just below
   and at this threshold showed TWO DISTINCT real eigenvalues
   (near `-1.834` and `-1.687` at `t=0.95`) approaching each other and
   merging into a complex-conjugate pair beyond `t*` -- a textbook
   non-Hermitian "exceptional point" (eigenvalue collision), not a
   generic/diffuse breakdown.
3. A wider scan (`t` in `[-8,8]`) found a SECOND pair of thresholds at
   `t ~ +-6.856`, with reality RESTORED (reentrant) beyond `|t|>6.856`.
   Bisection gave `t** = 6.856157181497904`.
4. The two threshold pairs are EXACTLY `+-`-symmetric
   (`t*` and `-t*` agree to full double precision; likewise `t**`).
   This symmetry has an elementary, general explanation, not specific to
   `M_1^sum`: for ANY block matrix `D_PW(t) = [[D1, t*B^H],[t*B, D2]]`
   (fixed diagonal blocks, off-diagonal linearly scaled by `t`),
   conjugating by `S = diag(I_8, -I_18)` gives exactly
   `S D_PW(t) S^{-1} = D_PW(-t)` -- so `D_PW(t)` and `D_PW(-t)` are
   ALWAYS similar (same spectrum) for any such construction, regardless
   of what `B` is.

The formal script below independently re-derives all of the above from
scratch.

## Entity / falsifiable predicate / measurable outcome (Zero-Signal Gate)

- **Entity:** `D_PW(t)` (C101's own 2-level k=1->2 construction), with
  off-diagonal block `t*M_1^sum (x) I_r`, `t` a real scale parameter.
- **Falsifiable predicate:** the exact locations of the reality-breaking
  threshold(s) as `t` varies over `[-8,8]`, and whether `D_PW(t)` and
  `D_PW(-t)` always have identical spectra.
- **Measurable outcome:** `max|Im(eig(D_PW(t)))|` as a function of `t`
  (`np.linalg.eigvals`, `1e-6` threshold for "real"), converged via
  bisection to double-precision for each threshold crossing.

## Predictions (stated before the formal script runs, though after the
disclosed scratch exploration above)

| # | Prediction |
|---|---|
| P0 | `D_PW(1)` reproduces C108's own `max\|Im\|=0.10592470995283362` exactly. |
| P1 | There exist exactly two threshold crossings in `t in (0,8)`: one near `0.966`, one near `6.856`; reality holds for `t in (0, t*)` and `t > t**`, breaks for `t in (t*, t**)`. |
| P2 | `t*` converges (bisection, 50 iterations) to `0.9660948033007579` and `t**` to `6.856157181497904`, both to double-precision stability. |
| P3 | The negative-side thresholds are EXACTLY `-t*` and `-t**` (bit-for-bit, not merely close). |
| P4 | `D_PW(t)` and `D_PW(-t)` have identical spectra for every tested `t` (general block-similarity fact, not specific to `M_1^sum`), verified by directly checking eigenvalue sets agree, not merely both being classified "real" or "complex". |

## What this cannot show

- Does not derive `t*`, `t**` in exact closed form (e.g. as roots of a
  low-degree polynomial or algebraic numbers) -- only converges them
  numerically to double precision. A closed-form derivation would
  require the Schur-complement reduction of `D_PW(t)`'s eigenvalue
  problem to a smaller (<=8-dimensional) effective problem using `D1`,
  `D2`'s own known eigenprojectors -- identified as the correct next
  step, not carried out this round.
- Does not perform a full 4-complex-parameter sweep (`c1,c2,c3,c4`
  independently) -- restricted to the single physically-motivated
  1-parameter slice (`t` scaling the certified `M_1^sum` construction).
- Does not change N_gen=3's CONDITIONAL status.
- Does not touch OB1.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## kill_criterion

If P0-P4 all hold as predicted, this establishes that C108's k=1 anomaly
is a genuine, isolated, two-eigenvalue exceptional-point bifurcation
(with a second, reentrant pair at larger coupling), not a generic
algebraic breakdown -- a substantially sharper characterization than
C108-C110's own "some combinations break it" findings, while honestly
falling short of the fully closed-form derivation C110's pearl
originally envisioned. If instead more than 2 threshold pairs are found,
or the +-symmetry fails for some tested t, this round reports that
directly instead.
