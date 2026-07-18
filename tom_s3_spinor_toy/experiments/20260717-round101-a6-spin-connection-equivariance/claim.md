# Claim — Round101 (A6 from goal-expansion-100): Spin-Connection-Level
Equivariance of `iota∘(t↔1-t)`

**Question type:** Descriptive (fills the ONE explicitly-flagged remaining
gap in round80/E14's own Relaxation Map: "Explicit spin-lift check... a
full spin-connection-level check... was NOT separately computed").

## Section 1 — Background

Round80 (E14) proved, at the AFFINE/torsion level, `iota^*(∇^t)=∇^{1-t}`
exactly for all `t` — a genuine isometry (`iota(g)=g⁻¹`, realized as
`Φ(x)=(x0,-x1,-x2,-x3)`) implements the `t↔1-t` symmetry as an actual
diffeomorphism, not merely an algebraic curvature-formula coincidence.
Round80's own Relaxation Map flags the ONE thing NOT checked: whether this
lifts to the SPIN CONNECTION `Ω_i(t)` (E9/round73's own formula,
`Ω_i(t)=(1/4)Σ_{j,k}Γ^k_{ij}(t)·Z_jZ_k`, `Γ^k_{ij}(t)=t·c·ε(i,j,k)`) and
hence to the Dirac operator `D^t` itself — flagged there as `[INFERRED]`
("standard consequence... via the canonical spin lift"), not independently
verified.

## Section 2 — What this experiment computes (new this round)

Reusing round80's own `b_i^j(x)` coefficients (`Z_i^R = Σ_j b_i^j(x)·Z_j^L`,
`e14_z2_left_right_symmetry.py`'s `express_fk_in_Z_basis`), form the
"R-frame spin connection component" `Ω_i^R(t)(x) := Σ_j b_i^j(x)·Ω_j(t)`
— the NAIVE component-substitution analogue of what worked at the affine/
torsion level (round80 Section C) — and check directly whether it is
`x`-independent (a NECESSARY condition for any clean "constant spin-lift
matrix `S`" story, since `Ω_i(t)` itself is a CONSTANT matrix in the
L-frame).

## Section 3 — Pre-registered criteria

- **SPIN-LEVEL EQUIVARIANCE HOLDS:** `Ω_i^R(t)(x)` is `x`-independent, and
  (after accounting for signs from the frame-exchange, round80 Section B)
  equals `±Ω_i(1-t)` exactly.
- **NAIVE APPROACH BLOCKED (expected/honest possibility):** `Ω_i^R(t)(x)`
  is genuinely `x`-dependent — meaning the affine-level trick (simple
  component substitution via `b(x)`) does NOT directly generalize to the
  spin connection, because a connection 1-form is not a tensor and
  transforms with an inhomogeneous (Maurer-Cartan-type) term under a
  non-constant frame change, which this naive substitution omits. This
  would be a genuine, informative negative finding (not a failure of the
  experiment), correctly identifying why the spin-level check is harder
  than the affine-level one, and precisely what a full treatment would
  need to add.

## Section 4 — What this does NOT claim

Does NOT attempt the full, correct spin-level pullback (which would need
the inhomogeneous gauge-transformation term) if the naive check is
blocked — that remains open, flagged in the Relaxation Map. Does NOT
affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, `safe_for_runtime=False`.
