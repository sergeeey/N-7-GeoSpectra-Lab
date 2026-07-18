# Claim — Round111 (Codex item 6): Actual Scalar Curvature `Scal(t)`,
Not a Toy Norm — Does the Leading Gravitational Term Really Prefer
`t=0,1`?

**Question type:** Descriptive (direct tensor computation — does the
STANDARD, leading-order term of any gravitational/spectral action
`∫Scal(t)` have the double-well shape round99 only sketched with a
non-standard higher-derivative toy quantity?).

## Section 1 — Background

Round99 built `V(t)∝‖R^t(Z_1,Z_2)Z_1‖²` (a curvature-NORM-SQUARED
quantity) and found a double-well shape — but skeptic review correctly
flagged this is NOT shown to be a term that actually appears in any real
gravitational/spectral action; it was offered only as a plausibility
sketch. Codex/round105's item 6 asks for the actual Seeley-DeWitt/
spectral-action computation. A full Seeley-DeWitt expansion is a large
undertaking; this round attempts the single most standard, always-
present LEADING term any such expansion contains: the scalar curvature
`Scal(t)` itself (the bare Einstein-Hilbert integrand, `a_2`-type
heat-kernel coefficient) — using the ACTUAL metric-compatible Ricci
tensor of `∇^t`, not a norm of one curvature component.

## Section 2 — Method

1. Define the metric on `su(2)` via `⟨X,Y⟩:=-½Tr(XY)` — verified to make
   `{Z_1,Z_2,Z_3}` orthonormal (`⟨Z_i,Z_j⟩=δ_ij`), matching how this
   project's own prior rounds (E2/E7/E9/round99) already implicitly treat
   `{Z_i}` as the orthonormal frame.
2. Compute `Ricci^t(Z_a,Z_b):=Σ_c⟨R^t(Z_c,Z_a)Z_b,Z_c⟩`, using round99's
   own established `R^t(X,Y)Z=t(t-1)[[X,Y],Z]`, for all 9 index pairs.
3. **Mandatory cross-check** before trusting the general-`t` formula: at
   `t=1/2` (Levi-Civita), independently compute `Ricci` via the STANDARD
   textbook formula for a bi-invariant metric's Levi-Civita Ricci tensor
   (`Ric(X,Y)=-¼Tr(ad_X·ad_Y)`, a different, independently-sourced
   route) and confirm the two methods agree.
4. Extract `Scal(t)=Σ_a Ricci^t(Z_a,Z_a)` and determine its exact
   functional form in `t` (linear in `t(t-1)`? quadratic? something
   else?) and its critical points.

## Section 3 — Pre-registered criteria

- **DOUBLE WELL CONFIRMED (would support round99's hope):**
  `Scal(t)` itself has minima at `t=0,1` and a local max at `t=1/2`.
- **SINGLE DIP / OPPOSITE SHAPE (would refute round99's hope at the
  standard-leading-term level):** `Scal(t)` is extremized (max or min)
  at `t=1/2`, not `t=0,1` — meaning the bare Einstein-Hilbert term, if
  it were the only `t`-dependent piece of a dynamical action, would push
  `t` TOWARD the Levi-Civita point (already known, KT-8, to be the
  zero-mode-free "wrong" point), not away from it.
- **BLOCKED:** the cross-check (two independent Ricci-computation
  routes) fails to agree — stop, do not trust the general formula.

## Section 4 — Escalation note

Given round99 already required a skeptic correction in this exact
territory (curvature-based toy potentials), and rounds 102/103/106/108/
109/110 all needed skeptic-driven corrections in adjacent Lie-theory/
differential-geometry territory, this round's conclusion goes through
mandatory context-asymmetric skeptic review before being reported as
more than a hypothesis — regardless of which pre-registered outcome is
reached.
