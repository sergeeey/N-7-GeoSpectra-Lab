# C94 -- group-action certification of the q-side generator sign (no more hand-derivation)

**Experiment id:** `20260812-c94-group-action-certification-q-side-generator`
**Date:** 2026-08-12 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C92 (naive quaternion-mult q-side hypothesis falsified for
j,k), C93 (dual-representation `L_i=-l_{e_i}^T` satisfies su(2), Casimir
check found non-discriminating). Directed by an external reviewer's
proposal after reviewing C90-C93: stop hand-deriving the sign of `L_i`
(caught producing `+l_{e_i}^T` and `-l_{e_i}^T` from two re-derivations
of the same identity within minutes) and instead certify it directly
from the group action's own defining formula, computed by a tool, not
paper algebra.

**Pre-check (falsification-ladder discipline):** `null_results/INDEX.md`
flags `G38-S2` (spectral action functional `S_spec(c3)` minimization) as
a keyword collision on "spectral"/"action" -- confirmed false positive,
unrelated topic (a scalar parameter minimization from a different round,
not group-representation-theory generators).

---

## The claim under test

> **C94.** Fix the standard convention `(L_h f)(g) := f(h^{-1}g)`,
> `(R_h f)(g) := f(gh)` for the left/right regular representation acting
> on functions on `SU(2)`. Take `F_{m,n}(g) := D^{1/2}_{m,n}(g) = g_{m,n}`
> (the defining representation's own matrix entries, `j=1/2`, since
> `D^{1/2}(g)=g` literally). Differentiate `F_{m,n}(h(eps)^{-1}g)` and
> `F_{m,n}(g h(eps))` at `eps=0`, `h(eps)=exp(eps*e_i)` (quaternion
> units, same convention as C85/round67 throughout this project), via
> DIRECT symbolic 2x2 matrix multiplication and differentiation -- not
> abstract algebra. Compare the resulting generator matrices against the
> four candidates `+l_{e_i}(1)`, `-l_{e_i}(1)`, `+l_{e_i}(1)^T`,
> `-l_{e_i}(1)^T` (Meier's own certified generator, C85).

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1 (right-translation baseline)** | the `R_h` generator, acting on `F`'s column (`n`=`p`) index, matches EXACTLY ONE of the four candidates -- this MUST match `l_{e_i}(1)` itself (not a transpose or sign flip), since `l_{e_i}` was defined and certified (C85) to act on `p` directly | pending |
| **P2 (left-translation, the actual open question)** | the `L_h` generator, acting on `F`'s row (`m`=`q`) index, matches EXACTLY ONE of the four candidates. A hand derivation done while scoping this round (not trusted, recorded only as the pre-registered guess) suggested `-l_{e_i}(1)^T` -- i.e. that C93's own construction was right -- but this is exactly the kind of claim this round exists to verify independently, not assume | pending |
| **P3 (bracket consistency, EXPLORATORY -- added after seeing P1/P2's own result, not predicted in advance)** | `[Y1,Y2]` for the matched left-translation candidate should equal `2*Y3` (the same normalization `l_{e_i}` itself satisfies), since `L_{h1}L_{h2}=L_{h1h2}` is separately verified (a genuine group representation), and `dL` of a genuine representation must be a genuine, non-anti Lie algebra homomorphism | pending |

## kill_criterion

If P1 fails (the right-translation baseline doesn't recover `l_{e_i}`
itself), something is wrong with THIS round's own setup (the `(a,b)`
embedding, the quaternion-unit-to-matrix map, or the differentiation) --
stop, do not trust P2 either, diagnose the setup first. If P2 matches a
DIFFERENT candidate than C93's `-l_{e_i}^T`, C93's construction is
falsified and must be corrected before any further use.

## What this cannot show

- Does **not** test `j=1` (`k=2`) as an independent replication -- named
  by the reviewer as a follow-up, not attempted this round unless P1/P2
  resolve cleanly and cheaply enough to extend.
- Does **not** build or test the multiplication operator itself (C95 in
  the reviewer's proposed sequence).
- Does **not** run any spectral crossing scan (explicitly out of scope
  per the reviewer's own gate: no crossing scans until this passes).
- Does **not** change `N_gen=3`'s CONDITIONAL status.
- Does **not** solicit or reference Tom Lawrence's unpublished Part 5.
