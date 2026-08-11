# C72 -- state-level triality obstruction, scoped as an equivariance-algebra sweep

**Experiment id:** `20260811-c72-state-level-triality-g2-equivariance-test`
**Date:** 2026-08-11 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C70/C71 (round59<->G102 su(3) bridge, all 3 channels, machine
precision); C71's own methodological lesson (chained-intertwiner "T^3=1" is a
pure algebraic tautology, proven not just observed); OB11(iii)'s literature
anchor (McRae 2025, state-level triality has "no intertwining action upon the
representation space" in the Euclidean case -- an open problem in the primary
source itself, not a proven theorem this project can simply cite as settled)
**User direction:** continue the original C70-C76 queue with C72, explicitly
leaving the S6-embedding gap (D/J/gamma provenance) open for now.

---

## Why this round is scoped the way it is

`predictions_before_data.md`'s P3 (ledger-C72) describes "the state-level
triality obstruction system (`T^3=1`, `T*rho(a)*T^-1=rho(tau(a))`,
compatibility with `D,J,gamma`)". Two of these three pieces are not usable as
literally stated, for reasons established THIS round (not assumed):

1. **`T^3=1` is vacuous by construction** whenever `T` is built by chaining
   three independently-found pairwise intertwiners through a common reference
   (`V_vs=U_s U_v^-1`, `V_sc=U_c U_s^-1`, `V_cv=U_v U_c^-1`) -- the product
   telescopes to `U_v U_v^-1 = Identity` for algebraic reasons alone, using no
   su(3)/g2/geometric structure whatsoever. C71 discovered this for su(3);
   this round re-derives it and confirms numerically that it holds for
   ARBITRARY random invertible blocks with no algebraic structure at all --
   fully general, not su(3)-specific. `T^3=1` therefore cannot discriminate
   "genuine triality" from "any three unrelated invertible intertwiners" via
   this construction, at ANY equivariance level.
2. **Compatibility with `D,J,gamma`** requires objects (a real `J`/`gamma` for
   round59's construction) that the prior "take stock" round found do not
   exist anywhere in this project -- explicitly deferred per user direction.

**What remains genuinely testable:** the middle condition,
`T*rho(a)*T^-1=rho(tau(a))`, asks whether an intertwiner between channels
survives as the algebra `a` ranges over is enlarged. C70/C71 already answered
this for `a in su(3)` (`Hom=6`, invertible elements exist). This round extends
the SAME question to `a in g2` (the full `S6=G2/SU(3)` isotropy+coset algebra,
14-dim) and `a in so(8)` (the full ambient algebra in which triality is
defined, 28-dim, expected to give `Hom=0` by Schur's lemma per the very
definition of triality-inequivalence -- and per G102's own module docstring,
which already asserts this without this project ever having re-verified it
directly in this specific construction).

## Predictions, recorded before running

| # | Prediction | Source |
|---|---|---|
| **P1** | `Hom_g2(channel_i,channel_j)` is nonzero and shrinks relative to `Hom_su3=6`, consistent with the already-published (pearl #33, 2026-07-15) `8_v=1+7` g2-branching -- NOT claimed as a new discovery if it matches Schur's prediction from that branching | pearl #33 cross-check |
| **P2** | the g2-level Hom-space contains an invertible (not merely nonzero) element -- a genuine cross-channel isomorphism, explicitly constructed for the first time (pearl #33 only established the branching symbolically for one channel, not a cross-channel map) | new construction |
| **P3 (negative control)** | `Hom_so8(channel_i,channel_j)=0` exactly, confirming Schur's lemma applied to triality-inequivalent so(8) representations, and independently re-verifying G102's own module-docstring assertion rather than trusting it | Gate 3 discipline |

## kill_criterion

P1/P2 fail if no invertible g2-equivariant intertwiner exists (would indicate
the bridge itself does not extend beyond su(3), a genuine narrowing of C70/71's
result). P3 fails if `Hom_so8 != 0` (would falsify a claim this project has
carried since G102, 2026-07-05, without this specific re-verification).

## What this cannot show

- Does **not** test `T^3=1` as a genuine, non-tautological constraint -- shown
  structurally impossible via the natural construction; a real test would need
  an INDEPENDENTLY-fixed definition of triality's automorphism tau (e.g. via
  Baez's explicit `S3 subset F4` construction, pearl #33's own follow-up),
  not derived circularly from the intertwiners being tested. Not attempted.
- Does **not** test compatibility with `D`, `J`, `gamma` -- explicitly
  deferred per user direction (S6-embedding gap left open).
- Does **not** resolve OB11(iii)'s state-level question (McRae's own open
  problem) -- this round operates entirely at the ALGEBRA-equivariance level,
  a necessary but not sufficient condition for a genuine state-level operator.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
