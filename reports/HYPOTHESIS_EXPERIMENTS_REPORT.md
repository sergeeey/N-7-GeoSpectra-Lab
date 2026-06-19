# Hypothesis Experiments Report

**Status:** research_only | smoke_only | safe_for_runtime = no

Toy tests for HYP_01–HYP_03. Does not promote physical compactification or SM claims.

## HYP_01 — Flux / moduli stabilization

- Coupled branch: `hypothesis_supported` — Coupled flux sector yields 1 critical point(s); lambda_*=-0.302984 at N1=1, N2=2.
  - CP0: lambda*=-0.302984, R=1.155178, phi=1.000000, Hess proxy=1.9843
- Falsifier (decoupled): `hypothesis_killed` — Falsifier: d V_eff / d lambda == 0 identically when flux-lambda coupling removed.

## HYP_02 — Twisted Lichnerowicz eigenvalue

- Status: `hypothesis_supported` — Single admissible eigenvalue stable across conventions in toy truncation.
- Kernel dimension (toy constraint): 1
- Eigenvalues (UNIT / SQRT2): (-1.4109907439877516e-17,) / (2.3606623455016808e-17,)

## HYP_03 — Nonlinear realization

- Status: `hypothesis_supported` — R_B = sqrt(2) confirmed (1.414213562373); dR/dlambda = 0 — theory testable without fixing lambda. Full nonlinear-realization descent toy deferred (Tom Q1-Q2).
- R_B observable: 1.414213562373 (lambda derivative 0.0)
- Full descent toy: deferred=True

## Interpretation

- HYP_01: flux-lambda **coupling** can yield discrete lambda* in toy V_eff; removing coupling kills the route (falsifier confirmed).
- HYP_02: current P13B1 truncation — check status above; convention dependence aligns with P13E NO-GO if killed.
- HYP_03: lambda-free R_B=sqrt(2) confirmed; parent-action descent still deferred.
