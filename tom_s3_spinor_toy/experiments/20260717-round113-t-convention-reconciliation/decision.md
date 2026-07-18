# Round113 — Decision

**Date:** 2026-07-17
**Verdict:** `RESOLVED__CONVENTIONS_A_AND_B_ARE_THE_SAME_CONNECTION__F3_DOWNGRADED_TO_NON_ISSUE`
(skeptic pass 1: `WEAKENED`, load-bearing gap identified and closed by a
direct follow-up check — not smoothed over)
**Go/no-go:** `PARENT_ACTION_GATE.md` field F3's flagged risk (two possibly
different `t`-conventions) is resolved. Round67/preprint.tex's Kostant
Dirac-operator shift and round99/round111's curvature computation are built
from the **literal same connection**, `∇^t_X Y = t[X,Y]`, not two
independently-asserted formulas that happen to numerically coincide.

## What was computed [VERIFIED-tool: sympy, this round]

Built `∇^t_X Y := t·[X,Y]` (round67's own stated connection,
`e2_s3_torsion_deformation.py` line 22) using this project's own `Z_i=i·σ_i`
Cl(3) basis (identical convention to round67/99/111), then computed the
standard curvature tensor `R^t(X,Y)Z := ∇^t_X∇^t_Y Z - ∇^t_Y∇^t_X Z -
∇^t_{[X,Y]} Z` **directly from this connection**, checked against round99/
111's stated `R^t(X,Y)Z = t(t-1)[[X,Y],Z]` on all 27 ordered basis triples.
**All 27 match exactly.** The torsion definition applied to the same
connection also matches round67's stated `T^t=(2t-1)[X,Y]` on all 9 pairs.
An independent Jacobi-identity hand-derivation (`R^t=t²([X,[Y,Z]]-[Y,[X,Z]])
-t[[X,Y],Z] = t(t-1)[[X,Y],Z]` via `[X,[Y,Z]]-[Y,[X,Z]]=[[X,Y],Z]`) was also
verified symbolically, all 27 triples.

## Skeptic review [context-asymmetric: claim.md + code only]

**Arithmetic: fully confirmed**, all four checks (curvature match, torsion
match, Jacobi identity, "same `t`" ruled out reparameterization since the
match holds as symbolic polynomials in `t`, not just at isolated points).

**Load-bearing gap identified, correctly, before this label was earned:**
the round113 script only verified ONE direction — "does round67's stated
`∇^t=t[X,Y]` produce round99/111's stated `R^t` formula?" It did **not**,
by itself, verify the reverse — "did round99/111's own script actually
*derive* its `R^t` formula from that SAME `∇^t=t[X,Y]`, or did it *assert*
the curvature formula via a different, independently-constructed route that
only coincidentally matches?" Since the map connection→curvature is not
injective in general, agreement of `R^t` alone does not prove agreement of
`∇^t` without this check. Skeptic recommended a "10-minute follow-up":
directly read round99's own script to settle which case holds.

## Follow-up check that closes the gap [VERIFIED-tool: direct read, this round]

Read `experiments/20260717-round99-toy-Vt-curvature-double-well/
e26_toy_Vt_curvature_double_well.py` directly (not round111's later reuse of
round99's formula, which only cites it). **Round99's own script explicitly
defines** (lines 63-65):

```python
def nabla_t(X, Y, tt):
    """nabla^t_X Y = tt*[X,Y] for left-invariant X,Y (Cartan-Schouten family)."""
    return tt * bracket(X, Y)
```

and derives its `R^t` formula **directly from this same connection**
(lines 74-89: `term1 = t*[X,t*[Y,Z]]`, `term2 = t*[Y,t*[X,Z]]`,
`term3 = t*[[X,Y],Z]`, `R_direct = term1-term2-term3`, checked against
`t(t-1)[[X,Y],Z]` for all 27 triples) — **the identical construction this
round independently re-derived**, not a coincidentally-matching,
separately-asserted formula. This closes the skeptic's load-bearing gap
directly, not by assumption: round67 and round99/111 build from the
literal same `∇^t_X Y = t[X,Y]`, confirmed by reading round99's own source,
not inferred.

## Residual honest caveat [per skeptic's patch request, accepted]

The identification still silently assumes **bi-invariant-metric
compatibility** — i.e., that `∇^t` is being compared as an affine
connection on `S³=SU(2)` with its standard bi-invariant metric in both
uses, not merely as an abstract algebraic operation. Both round67 and
round99/111 state this context explicitly (round67: "S³ realized as G/H...
bi-invariant metric"; round99: "for left-invariant X,Y"), so this is not an
unstated assumption in the underlying sources — but it is not re-verified
independently by this round's own computation, and is recorded here per the
skeptic's own request rather than left implicit.

## Applying the pre-registered kill criterion (claim.md)

"Agree exactly" branch is met, closing F3 as resolved — **with the
skeptic's identified gap (one-directional verification) explicitly closed
by the follow-up read**, not left as an open assumption. `PARENT_ACTION_GATE.md`
F3 downgrades from "single highest-priority risk" to "resolved, cite this
round" as pre-registered.

## Kill Analysis

- **What this kills:** the possibility that round67/preprint.tex's `t=0,1`
  (Dirac-operator zero modes) and round99/111's `t=0,1` (flat-connection/
  curvature-zero points) refer to different physical configurations under a
  shared label — they are now confirmed the SAME configurations.
- **What this does NOT kill:** OB1's own central question (what selects a
  specific `t`) remains exactly as open as before — this round only
  confirms both prior results are talking about the same object, not that
  either supplies a parent action.
- **What survives, sharper than before:** a single, unified statement of
  the `S³` torsion family usable by BOTH the Dirac-operator/zero-mode
  program (round67/68, KT-8 escape route) and the curvature/action program
  (round99/111) without translation — genuinely useful going forward,
  closes a real (if ultimately benign) risk rather than leaving it
  unverified.

## What this does NOT mean

1. Does NOT supply a parent action or resolve OB1/OB2.
2. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.
3. Does NOT establish that `D^t`'s zero modes (`t=0,1,4/3,...`, the full
   discrete ladder, round67) and `Scal(t)`'s extremum (`t=1/2`) being
   properties of the same connection is itself evidence for a parent
   action — only that they can now be combined/compared without a
   translation step, which is a prerequisite, not a result.

## Check (reproduces this decision)

```
cd experiments/20260717-round113-t-convention-reconciliation
python e35_t_convention_reconciliation.py
```
Expect: `clifford_relations_confirmed=True`,
`curvature_conventions_A_and_B_agree_exactly=True`,
`torsion_definition_matches_stated_formula=True`,
`jacobi_identity_independent_check=True`, `triples_checked=27`,
`label='RESOLVED__CONVENTIONS_A_AND_B_ARE_THE_SAME_CONNECTION_FAMILY_SAME_T__F3_FALSE_ALARM'`.
Cross-check: `experiments/20260717-round99-toy-Vt-curvature-double-well/
e26_toy_Vt_curvature_double_well.py` lines 63-89 (round99's own
`nabla_t`→`R^t` derivation, confirming the same connection).
