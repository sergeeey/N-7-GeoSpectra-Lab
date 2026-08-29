# C107 decision -- naive Meier<->Kostant bridge falsified exactly; a sharp,
provable non-identity at n=k=0 redirects (not abandons) the OB1-bridge idea

**Verdict:** `NAIVE_BRIDGE_FALSIFIED__MEIER_AND_KOSTANT_NOT_IDENTIFIABLE_UNDER_N_EQ_K`
**Status:** RESOLVED -- clean, informative null result on the simplest bridge hypothesis

---

## Summary

Following `/boyko-project-radar` + `/tracy`'s converged recommendation (the
C90-C106 multiplication-operator machinery has never been pointed at OB1),
this round asked the necessary prerequisite question: is C85/Meier's own
certified `D-bar_k` -- the operator every C90-C106 round builds on -- the
SAME object as round67/Agricola's already-certified one-parameter torsion
family `D^t(n,sigma)`, under the simplest natural identification (Peter-Weyl
level `n` = C85's level `k`)?

**All 4 predictions confirmed, all pointing the same direction:**

| # | Prediction | Outcome |
|---|---|---|
| P1 | `D-bar_0` has an exact, doubly-degenerate zero eigenspace | **CONFIRMED** -- both eigenvalues exactly 0.0, [VERIFIED-tool]. |
| P2 | Under `n=k`, the two eigenvalue branches (`-k`, `k+2`) require DIFFERENT, k-independent `t` values in round67's formula | **CONFIRMED** -- `t=2/3` vs `t=1`, exact symbolic mismatch, same at every k. |
| P3 | Round67's own family cannot produce a doubly-degenerate zero at n=0 for ANY single t | **CONFIRMED** -- the two n=0 branches are `3t` and `3t-3`; zero at `t=0` and `t=1` respectively, never simultaneously. |
| P4 | Swapping which eigenvalue maps to which `sigma` branch does not fix the mismatch | **CONFIRMED** -- alt assignment gives k-DEPENDENT required t on both sides, worse, not better. |

## What this genuinely establishes

1. **A sharp, exact, non-approximate proof that C85/Meier's `D-bar_k` is
   NOT a member of round67/Agricola's Kostant-cubic torsion family under
   the natural `n=k` identification, in either branch assignment.** P3 is
   the strongest form of this: it is not merely that this round failed to
   find a matching `t` -- it is a proof, using round67's OWN certified
   formula, that no `t` exists that could reproduce `D-bar_0`'s exact
   double-zero at n=0. This is a `t`-independent structural fact about
   round67's family itself, not a search failure.
2. **This project has (at least) three independently-built S3
   Dirac-operator constructions that have never been fully
   cross-checked against each other**: G8/G4 (round67's own calibration
   source for `h_H=3`, itself external to both C85 and round67), Agricola/
   Kostant (round67, cross-checked against round99/111 in round113 --
   but NOT against C85), and Meier/Peter-Weyl (C85, used throughout
   C90-C106, never cross-checked against either of the other two before
   this round). Confirmed via grep: `docs/clifford_convention_registry.md`
   and `docs/load_bearing_formulas.md` mention Meier/Kostant/Agricola/
   Peter-Weyl only in unrelated contexts, never together, before this
   round.
3. **Answers the immediate question this round was scoped to ask**: the
   C90-C106 apparatus cannot be trivially "torsion-deformed" by importing
   round67's already-known crossing values -- there is no cheap shortcut.
   A genuine bridge, if one exists, requires either (a) an explicit,
   verified equivalence map between the Meier and Agricola constructions
   (not attempted this round -- a separate, larger literature/derivation
   task), or (b) building a torsion deformation NATIVELY within C85's own
   Peter-Weyl framework, using its own certified `L_i(k)`/`R_i(k)`
   apparatus from first principles rather than importing round67's
   abstract result.

## Kill Analysis (per this project's own Anti-Overfitting Gate discipline)

**Killed:** the hypothesis "C85/Meier's `D-bar_k`, under the natural
`n=k` identification (either branch assignment), is a member of round67/
Agricola's certified `D^t(n,sigma)` family for some single `t`." Killed
exactly, not approximately -- P3 in particular is a proof, not a search
result.

**NOT killed:** (a) round67's own D^t family and its zero-mode crossings
(`t* in {-2/3,-1/3,0,1,4/3,5/3}` for n=0,1,2) -- entirely unaffected,
this round only tested whether C85's operator is PART of that family;
(b) C85/Meier's own certification (Meier eq 6.4 spectrum) -- unaffected,
re-confirmed numerically this round; (c) the possibility that SOME other
identification map (nonlinear `n=f(k)`, different `h_H`, different
generator normalization) reconciles the two constructions -- genuinely
untested; (d) the possibility of building a torsion deformation natively
within C85's Peter-Weyl framework, independent of round67's abstract
Kostant-cubic route entirely.

**Relaxation map (one relaxation per candidate, none attempted further
this round):**

| Assumption in the killed hypothesis | Possible relaxation |
|---|---|
| `n = k` (direct, linear, 1-1 level identification) | Try a nonlinear or offset map `n = f(k)`, calibrated against more data points (this round only used the leading eigenvalue pair per k) |
| Single global `t` for all k | Allow `h_H` or the base calibration to itself be k-dependent (would require re-deriving round67's own scalar-shift argument, which assumed `H` acts as a k-independent scalar -- a nontrivial claim to relax) |
| Bridge via round67's abstract formula | Build `D-bar_k^t` natively inside C85's Peter-Weyl framework using its own certified `L_i(k)`, `R_i(k)` generators (C91-C99) and an explicit torsion-bracket term, rather than importing round67's result |

None of these is pursued in this round.

## What this cannot show

- Does not prove no identification exists between the two constructions at
  all -- only that the simplest one fails, exactly.
- Does not resolve OB1.
- Does not change N_gen=3's CONDITIONAL status.
- Does not touch KT-8's own established result.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## Verification

- `ruff check experiments/20260829-c107-meier-vs-kostant-bridge-attempt/`
  -- clean, 0 errors.
- P1's numeric eigenvalues are exact-arithmetic-derived (C85's certified
  construction), max|Im|=0.0 exactly at every k tested.
- P2-P4 computed via exact sympy symbolic solve, not numerical
  approximation -- the mismatch (`2/3` vs `1`) is an exact rational
  inequality, and P3's `t=0` vs `t=1` is likewise exact.
- This round's formal script independently re-derives every number found
  during the disclosed scratch exploration (claim.md's Counterfactual
  Frame) from a clean script.
