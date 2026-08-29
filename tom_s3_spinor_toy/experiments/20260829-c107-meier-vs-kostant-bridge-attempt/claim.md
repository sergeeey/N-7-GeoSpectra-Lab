# C107 claim -- can C85/Meier's certified Peter-Weyl D-bar_k be identified
with round67/Agricola's Kostant-cubic torsion family D^t(n,sigma), as a
first step toward bridging the C90-C106 multiplication-operator apparatus
to OB1's own torsion-selection question?

## L0 gate (EstimandOps)

**Question type:** Descriptive (is object A the same mathematical object as
object B, under a stated identification map?). Not causal, not predictive.

## Background -- why this round exists

`/boyko-project-radar` (full-project scan, 2026-08-29) plus a `/tracy`
strategic pass converged on the same recommendation: the C90-C106
multiplication-operator machinery (the most active research thread of the
last several weeks) has never been pointed at OB1 (KT-8's own open
question: what selects a specific torsion value `t` for the S3 factor's
connection, if any). The user confirmed proceeding with this redirect.

Before building anything new, this round asks the necessary PREREQUISITE
question: is C85/Meier's own certified `D-bar_k` (the operator every
C90-C106 round is built from) actually PART of the same one-parameter
torsion family `D^t` that round67 already certified using an independent,
Agricola/Kostant-based construction -- or is it a structurally different
object that merely shares the name "S3 Dirac operator"? Per this project's
own Gate 1 (Artifact Identity) discipline: a shared subject/name does not
imply a shared object, and this specific cross-check has never been done
(confirmed by grep: `docs/clifford_convention_registry.md` and
`docs/load_bearing_formulas.md` mention Meier/Kostant/Agricola/Peter-Weyl
only in unrelated contexts, never together).

## Counterfactual Frame (exploratory round -- disclosed up front)

This round did NOT follow strict blind-prediction-before-data. Cheap
interactive scratch exploration (sympy/numpy) was run FIRST, following the
same discipline as C96/C99/C105/C106. It found:

1. C85's `D-bar_k` is a FIXED operator with no free torsion parameter at
   all (unlike round67's explicit one-parameter family `D^t`).
2. `D-bar_0` (k=0) has an EXACT, doubly-degenerate zero eigenspace
   (both eigenvalues exactly 0.0) -- [VERIFIED-tool].
3. Attempting the simplest natural identification (round67's Peter-Weyl
   level `n` = C85's level `k`, `D-bar_k`'s two eigenvalue branches
   `-k` and `k+2` matched to round67's own certified formula
   `D^t(n,sigma) = sigma*(n+3/2) + (t-1/2)*h_H`, `h_H=3`) gives a
   DIFFERENT required `t` for each branch (`t=2/3` for one, `t=1` for the
   other), a constant (k-independent) mismatch -- not a coincidental
   near-miss, an exact symbolic inconsistency for every k.
4. At `n=k=0` specifically: round67's own family can NEVER produce a
   doubly-degenerate zero, at ANY `t` -- its two `sigma`-branches at n=0
   are `3t` and `3t-3`, which cannot both vanish for the same `t`
   (0 != 1). This is a sharp, exact, `t`-independent proof, not merely a
   failed search.

The formal script below independently re-derives all of the above from
scratch, matching this project's own established discipline for
disclosed-scratch-then-formalize rounds.

## Entity / falsifiable predicate / measurable outcome (Zero-Signal Gate)

- **Entity:** C85/Meier's certified `D-bar_k` operator (k=0,1,2,3) vs.
  round67/Agricola's certified `D^t(n,sigma)` formula.
- **Falsifiable predicate:** there exists an identification `n=k` and a
  single torsion value `t` such that `D-bar_k`'s full eigenvalue spectrum
  (with correct multiplicities) equals `D^t(k,+1)` and `D^t(k,-1)`
  simultaneously, for the SAME t, at every tested k.
- **Measurable outcome:** exact symbolic equality (sympy), not a numeric
  tolerance -- both operators are built from exact rational/integer data.

## Predictions (stated before the formal script runs, though after the
disclosed scratch exploration above)

| # | Prediction |
|---|---|
| P0 | `D-bar_k` has no free parameter; is a single fixed operator per k (reuse-sanity, re-derives C85's own certification). |
| P1 | `D-bar_0` has an exact, doubly-degenerate zero eigenspace (both eigenvalues exactly 0). |
| P2 | Under `n=k`, solving round67's formula for `t` from the `sigma=+1` branch (`D^t(k,+1)=k+2`) and from the `sigma=-1` branch (`D^t(k,-1)=-k`) gives two DIFFERENT symbolic expressions for `t`, constant in k, that do not agree (an exact symbolic mismatch, not a numeric near-miss). |
| P3 | At n=k=0 specifically, round67's own family cannot produce a doubly-degenerate zero at ANY single t (the two branches `3t` and `3t-3` never vanish simultaneously) -- an exact, t-independent proof that `D-bar_0` (P1) is not reproducible inside round67's own family under `n=k`. |
| P4 | The alternate branch assignment (swap which eigenvalue maps to `sigma=+1` vs `sigma=-1`) also fails to give a k-independent common t (rules out a trivial labeling swap as the fix). |

## What this cannot show

- Does not prove NO identification exists between C85/Meier and
  round67/Agricola's constructions -- only that the simplest one (`n=k`,
  single global t, either branch assignment) fails exactly. A nonlinear
  map `n=f(k)`, a different h_H calibration, or a genuinely different
  normalization of the Clifford generators could still reconcile them;
  none of these are tested this round.
- Does not resolve OB1 (the torsion-selection question) either way.
- Does not change N_gen=3's CONDITIONAL status.
- Does not touch KT-8's own established result (Levi-Civita S3 spectrum
  never zero) -- this round is about whether C85's operator IS
  Levi-Civita-family in the first place, not a challenge to KT-8 itself.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## kill_criterion

If P2-P3 both hold as predicted (exact symbolic mismatch, provable
non-reproducibility at n=k=0), this round's verdict is: the naive bridge
between C90-C106's apparatus and round67's already-certified torsion
crossings is FALSIFIED in its simplest form. This is a genuine, informative
null result (per this project's own Anti-Overfitting Gate) that redirects
-- rather than abandons -- the OB1-bridge idea: a real bridge would need
either an explicit Meier<->Agricola equivalence proof (not attempted here)
or a torsion deformation built natively within C85's own Peter-Weyl
framework (a larger, separate undertaking). If P2-P3 instead reveal a
consistent identification, this round would instead report a genuine
PROMOTE-tier bridge and immediately proceed to building `D-bar_k^t` using
C85's own certified L_i(k)/R_i(k) machinery.
