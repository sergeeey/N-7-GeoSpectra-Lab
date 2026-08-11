# C73b -- genuine 2-parameter torsion family found and swept; S+ twist tested honestly

**Experiment id:** `20260811-c73b-torsion-family-genuine-deformation-and-twist-control`
**Date:** 2026-08-11 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C73 (round59 Dirac battery -- reproduced kernel=1, verified
chirality directly, proved `D(t)=t·D(1)` exact linearity along NOMIZU's own
ray, but failed to find a genuine wrong-twist negative control, and only
tested a 1-parameter uniform-scale deformation, honestly flagged as narrow)
**User direction:** after reviewing C73 (rated 9.4/10), directed: (1) do not
proceed to C74 until S6-twist specificity is addressed; (2) build a genuine
negative control via a different twisting representation or a different
admissible connection not related to the physical case by the hidden
symmetry C73 found; (3) check whether kernel=1/index=1 survives a more
general family of connections, not just `D->tD`.

---

## What this round actually tested

**Part 1 (representation theory, the load-bearing new result):** is round59's
`NOMIZU` unique up to scale among `su(3)`-equivariant torsion tensors on the
isotropy representation `m=g2/su3` (6-dim), or does a genuinely richer
admissible family exist? Computed `dim Hom_su(3)(m, Lambda^2 m)` directly
(a Sylvester-type linear system, 720 equations x 90 unknowns, `su(3)`
generators built independently from `ADNU`'s own bivector data, not reused
from the 8-dim spinor construction).

**Part 2:** genuine different-twist test -- twist `D_S6` by `S+`
(`ODD_IDX` on the second factor) instead of `S-` (`EVEN_IDX`), the physically
cited bundle. Checks whether this differs from, or secretly coincides with,
the physical case.

**Part 3:** using Part 1's genuine 2-parameter family, sweep the FULL angular
range (not just NOMIZU's own ray) at fixed magnitude, tracking kernel
dimension, the certificate value `b`, and calibration at each point.

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1** | `dim Hom_su(3)(m, Lambda^2 m)` is either 1 (NOMIZU unique up to scale, matching a naive Schur's-lemma guess treating `m` as irreducible) or larger (a genuinely richer family exists) | pending -- explicitly NOT assumed either way beforehand |
| **P2** | the `S+` twist either reproduces the physical result (a hidden symmetry, like C73's earlier failed attempts) or gives a genuinely different, discriminating result | pending |
| **P3** | kernel dimension across the full angular sweep (fixed magnitude, varying phase) either stays constant (topological protection across the whole family) or varies (fine-tuning specific to NOMIZU's own direction) | pending |

## kill_criterion

P1 fails (in the sense of "nothing new found") if the space is exactly
1-dimensional, confirming C73's deformation test already covered the entire
admissible family. P2 fails to supply a negative control if the `S+` result
turns out non-independent (as C73's prior attempts all did). P3 fails if
kernel dimension changes anywhere on the tested circle away from a narrow
neighborhood of NOMIZU's own angle (would indicate fine-tuning, not
topological protection).

## What this cannot show

- Does **not** supply a genuine wrong-twist negative control even if P2 finds
  a "different" result -- see decision.md for why the `S+` finding, though
  new, still does not discriminate.
- Does **not** test deformations outside the identified 2-parameter family
  (e.g. non-`su(3)`-equivariant, symmetry-breaking torsion) -- by
  construction, such deformations exit the domain where the invariant-sector
  machinery (`domain_inv`/`target_inv`) is even meaningful.
- Does **not** change `N_gen=3`'s CONDITIONAL status.
