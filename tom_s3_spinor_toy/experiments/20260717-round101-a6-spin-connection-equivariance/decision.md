# Round101 (A6) — Decision

**Date:** 2026-07-17
**Verdict:** `NAIVE_APPROACH_BLOCKED__X_DEPENDENT__INHOMOGENEOUS_TERM_NEEDED`
**Go/no-go:** the naive, cheapest way to check spin-connection-level
equivariance (direct analogue of round80 Section C's torsion-tensor
component substitution) does **not** work — for a mathematically
understood, correctly-identified reason. Round80's own Relaxation Map item
("full spin-connection-level check... `[INFERRED]`, not independently
verified") remains genuinely open; this round narrows WHY the cheap route
fails and what a full treatment would need to add.

## What was computed [VERIFIED-tool: sympy]

`Ω_i^R(t)(x) := Σ_j b_i^j(x)·Ω_j(t)`, using round80's own `b_i^j(x)`
coefficients (`Z_i^R = Σ_j b_i^j(x)·Z_j^L`) and E9/round73's own spin
connection formula, unchanged. Result: **`Ω_i^R(t)(x)` is genuinely
`x`-dependent** for all `i=1,2,3` (explicit matrix entries containing
`x0,x1,x2,x3`, printed in full in the script's output) — not a constant
matrix, unlike `Ω_i(t)` itself (constant in the L-frame).

## Why this is the mathematically correct outcome, not a bug

Round80 Section C's torsion-tensor pullback worked because `T^t` is a
genuine **tensor** — evaluating it on the R-frame and re-expressing via
`b(x)` reduces, via the rotation-coefficient identity (round80's own
27-case verified identity), to something that is EXACTLY
position-independent after the substitution, because a tensor's
components transform homogeneously (no derivative-of-`b(x)` term enters).
**A connection 1-form is NOT a tensor** — under a genuine (non-constant)
change of frame, a connection transforms with an ADDITIONAL inhomogeneous
term (the Maurer-Cartan-type/`g⁻¹dg` term in the standard gauge-
transformation formula `Ω'=g⁻¹Ωg+g⁻¹dg`), which this naive
component-substitution (`Σ_j b_i^j(x)Ω_j(t)`, no derivative term) omits
entirely. The `x`-dependence found here is exactly the signature of that
missing term, not a computational error — confirmed by cross-checking
that the SAME `b(x)` coefficients, used the SAME way, worked cleanly for
the (tensorial) torsion in round80 but not here (a genuinely different
mathematical object).

## Applying the pre-registered criteria (claim.md Section 3)

**NAIVE APPROACH BLOCKED** — exactly claim.md's pre-registered "honest
possibility," not a forced or unexpected outcome.

## Kill Analysis

- **What this kills:** the CHEAPEST possible route to closing round80's
  Relaxation Map item (direct reuse of the same `b(x)` substitution that
  worked for torsion) — it does not generalize to the spin connection.
- **What this does NOT kill:** the underlying question itself (does the
  Dirac operator `D^t` genuinely intertwine with `D^{1-t}` under the
  correct, full spin lift of `iota`) — remains open. Round80's affine-level
  result (the connection ITSELF pulls back correctly) is untouched.
- **What this narrows:** any future attempt at the full spin-level check
  now knows PRECISELY what is missing — the `g⁻¹dg`-type inhomogeneous
  term for the spin-frame change, i.e. the actual spinorial gauge
  transformation, not a bare component substitution. This is a
  well-defined (if substantially harder) follow-up, not a vague "try
  again."

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Full spin-level pullback, correct gauge-transformation formula | Compute the spin-frame's own "connection 1-form of the frame change" (the `dg·g⁻¹`-type term for the `b(x)` matrix viewed as an `SO(3)`→`Spin(3)` gauge transformation) and add it to the naive substitution — a substantially larger computation than this round |
| Sidestep the general-`x` question; check only AT THE TWO FIXED POINTS of `iota` (`g=±1`, round80 Section A) | At a fixed point, "change of frame" reduces to a single group element's adjoint action (no derivative term needed) — a cheaper, more tractable special case, NOT attempted here |

## Assumptions carried, unresolved

- `Ω_i(t)` formula (E9/round73) and `b_i^j(x)` (round80/E14) — both reused
  unchanged, not re-derived.
- Whether the fixed-point-only special case (Relaxation Map row 2) would
  suffice for this project's actual physical question (H1c/E12-E13's
  multiplicity gap) is not addressed here.

## What this does NOT mean

1. Does NOT overturn round80's own `PASS_GEOMETRIC_Z2_CONFIRMED` verdict
   at the affine/torsion level — untouched, independently reused here.
2. Does NOT resolve H1c, KT-8, or E12/E13's multiplicity gap.
3. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`. Does NOT modify `preprint.tex` or any prior
   experiment folder.

## Check (reproduces this decision)

```
cd experiments/20260717-round101-a6-spin-connection-equivariance
python e27_spin_connection_equivariance.py
```
Expect: `all_x_independent=False`,
`label='NAIVE_APPROACH_BLOCKED__X_DEPENDENT__INHOMOGENEOUS_TERM_NEEDED'`.
