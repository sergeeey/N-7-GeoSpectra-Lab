# C70 -- independent bridge round: direct solve finds the round59<->G102 su(3) intertwiner

**Experiment id:** `20260811-c70-independent-bridge-fingerprint-and-direct-solve`
**Date:** 2026-08-11 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C65 (module-type match, Casimir), C68 (complexification bridge, gap
localized), C69 (ground-truth control refutes C68's own hypothesis, obstruction sharply
characterized: cross-Hom is exactly the singlet block, E-to-Cartan-augmented mu-fit
systematically inconsistent ~2e-3 across 48 candidates x 20 restarts each)
**Program:** `experiments/20260811-ngen3-decisive-program/predictions_before_data.md`,
P1 (ledger-C70 = user's "C69")

---

## Why this round exists

C69 localized the round59<->G102 obstruction precisely (singlet-block-only Hom, genuinely
inconsistent mu-fit even with the missing Cartan relations added) and identified one
untested suspect: non-normal `ad(H)` on round59's side breaking Rayleigh-quotient root
extraction. Rather than patch the Cartan-Weyl root-matching pipeline further, this round
follows the user's directive (predictions_before_data.md P1): bypass root-matching
entirely and solve directly for the isomorphism.

## The claim under test

> **C70 (working).** A direct, pipeline-free global nonlinear solve for an isomorphism
> `Phi: su(3)_r59 -> su(3)_g102` (at the level of abstract Lie-algebra structure
> constants, not via CSA/root extraction) finds a solution to machine precision on every
> random restart. Given this `Phi`, the corresponding representation-space intertwiner
> `U` (the object C65/C68/C69 were actually after) exists and is found explicitly, with
> `hom_dim=6` -- matching C69's own ground-truth benchmark (G102-vs-G102 self-match) exactly,
> not the previously-stuck value of 4. **The round59<->G102 su(3) bridge (OB11(ii) hard
> half) is closed.**

## Predictions, recorded before running

| # | Prediction | Source |
|---|---|---|
| **P1 (non-normality)** | round59's `ad(H)` is either normal (refuting C69's identified suspect) or non-normal (confirming it) | C69 decision.md's stated next test |
| **P2 (bracket invariant)** | a fully basis-independent structure-constant invariant matches between the two constructions, ruling out scale/normalization mismatch | natural complement to C69's checks |
| **P3 (direct solve)** | a global nonlinear solve for `Phi` (bypassing CSA/root-matching) either finds a nondegenerate isomorphism or fails cleanly | predictions_before_data.md P1 |
| **P4 (representation intertwiner)** | given a valid `Phi`, the pushed-forward round59 representation is equivalent to G102's (i.e. `U` exists), matching the `hom_dim=6` ground-truth benchmark | natural follow-up once P3 succeeds |

## kill_criterion

C70 fails (P1 of the decisive program fails) if no nondegenerate `Phi`/`U` can be found by
any method tried, or if a found `Phi` does not survive positive/negative-control
discrimination (Gate 3). Per predictions_before_data.md: failure here would be "the first
serious anomaly in the Clifford<->triality bridge... C65 must be downgraded; headline
weakens materially."

## What this cannot show

- Does **not** transport `D`, `J`, `gamma`, `B-L` through `U` -- that is C71 (ledger
  numbering), the next round.
- Does **not** establish uniqueness of `U` -- `Inn(su(3))` acts transitively on the
  solution family (a continuous ~8-real-dim orbit), so many valid `U`'s exist, all related
  by inner automorphisms. C71 must fix one specific `U` (this round's, or any orbit
  representative) and use it consistently; physics conclusions should not depend on the
  choice, but this has not been separately verified.
- Does **not** fully explain, only plausibly diagnoses, why the discrete Cartan-Weyl
  root-matching approach (C68/C69) missed this: the likely mechanism is that fixed-weight
  root extraction (`combo_weight=0.37123`, one fixed linear combination of the CSA) only
  explores a single point in the CSA's own continuous re-parametrization freedom, while
  the genuine isomorphism needed an inner-automorphism component (a continuous CSA
  rotation) the discrete Weyl x Out x real-mu search never varied. This diagnosis is
  **[INFERRED]**, not independently confirmed by a side-by-side reconciliation test.
- Does **not** change `N_gen=3`'s CONDITIONAL status -- this closes one specific open
  blocker (OB11(ii) hard half) within the larger, still-open research program.
