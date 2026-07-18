# Round113 — Claim

**Follows up:** `PARENT_ACTION_GATE.md` field F3, flagged as "the single
highest-priority item to resolve before either OB1 or OB2 proceeds" — this
project appears to have TWO different `t`-parameter conventions in play:
- **Convention A** (preprint.tex / round67-68, KT-8 escape route): Kostant
  Dirac operator `D^t = D^{1/2} + (t-1/2)·h_H`, connection stated as
  `∇^t_X Y = t[X,Y]`, torsion `T^t=(2t-1)[X,Y]`, vanishing (Levi-Civita) at
  `t=1/2`. Zero modes of `D^t` (S³ factor alone) at `t=0,1,...` (discrete
  ladder).
- **Convention B** (round99/round111): connection family with curvature
  `R^t(X,Y)Z=t(t-1)[[X,Y],Z]`, torsion `T^t=(2t-1)c·vol`. `Scal(t)=
  Scal_LC-6(2t-1)²`, single hump at `t=1/2`, zero at `t=0,1`.

Both use the **identical Cl(3) generator convention** (`Z_i=i·σ_i`,
`{Z_i,Z_j}=-2δ_ij`, round67's `e2_s3_torsion_deformation.py` and round99/
111's scripts) — a strong hint these may be the SAME connection family
under the SAME `t`, not two conflicting conventions, but this has never
been directly verified.

## L0 gate (EstimandOps)

**Question type: Descriptive.** Whether two already-established formulas in
this project's own scripts are mathematically consistent under direct
symbolic substitution is arithmetic/algebra on established definitions, not
a causal or predictive claim.

## Falsifiable claim

For the connection `∇^t_X Y := t·[X,Y]` (round67's own stated formula,
`e2_s3_torsion_deformation.py` line 22, using this project's own
`Z_i=i·σ_i` basis), the standard curvature tensor
`R^t(X,Y)Z := ∇^t_X∇^t_Y Z - ∇^t_Y∇^t_X Z - ∇^t_{[X,Y]} Z`
(the textbook definition, not re-derived here, applied directly to
round67's own stated `∇^t`) equals round99/round111's own formula
`R^t(X,Y)Z = t(t-1)[[X,Y],Z]`, verified by direct symbolic computation on
all independent basis triples `(Z_i,Z_j,Z_k)`, not asserted from a
Jacobi-identity hand-derivation alone.

## Kill criterion (pre-registered)

- If the two formulas **agree exactly** (same sign, same coefficient, for
  all basis triples) → F3's flagged risk is **resolved as a false alarm**:
  conventions A and B use the SAME `t`, the SAME connection family, and
  compute two different derived quantities from it (Dirac-operator
  spectrum vs. curvature/torsion) — genuinely unifying, not conflicting.
  `PARENT_ACTION_GATE.md` F3 downgrades from "highest-priority risk" to
  "resolved, cite this round."
- If the two formulas **disagree** (different sign, different coefficient,
  or agree only after an unstated reparameterization) → F3's risk is
  **CONFIRMED as a real Type-1 symbol-overload error** (per
  `research-methodology.md`'s classifier) — any future OB1/OB2 round citing
  "`t=0,1`" from either source without specifying which convention would be
  citing potentially different physical configurations under a shared
  label. Requires an explicit reparameterization map before either
  convention can be reused together.

## What this does NOT mean (pre-registered)

1. Does NOT re-derive round67's `h_H` calibration or round99/111's
   `Scal(t)` computation — both reused as established inputs.
2. Does NOT itself supply a parent action or resolve OB1/OB2 — purely a
   convention-reconciliation check, one field of `PARENT_ACTION_GATE.md`.
3. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.
4. Even if the connections match exactly, this does NOT establish that
   `D^t`'s zero modes (Dirac-operator level, convention A) and `Scal(t)`'s
   extremum (curvature level, convention B) being at compatible `t`-values
   is itself evidence for a parent action — it only confirms they are
   talking about the SAME geometric family, a prerequisite for combining
   them, not a combination itself.
