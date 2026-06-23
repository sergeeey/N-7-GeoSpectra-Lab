# G77 Claim вЂ” Algebraic Uplift Solver

**Date:** 2026-06-22
**Type:** deterministic algebraic/numerical reproduction audit

## Potential

`V(rho) = [F - A exp(-lambda/rho^2)] / (K rho^12) + D/rho^p`

with `F=15*C^3/(16*pi)`, `C=0.986`, `lambda=1/3`.

## Two branches

1. `target_rho`: fix `rho0=rho6_star=1.090`, choose `p`, solve `(A,D)` from
   `V(rho0)=0` and `V'(rho0)=0`.
2. `fixed_A`: fix `A=0.3787`, choose `p`, solve `(rho0,D)` from the same conditions.

## Gates

- G77-1: symbolic target-radius formulas satisfy both equations.
- G77-2: reproduce `A` and target-radius shifts for `p={2,4,6,8}`.
- G77-3: every solution has `D>0` and `V''(rho0)>0`.
- G77-4: report both `K=1` and repository `K=K_vol` uplift conventions.
- G77-5: negative control вЂ” using a `K=1` value of `D` in the repository convention
  must fail the Minkowski residual.
- G77-6: `p` remains a model choice; no microscopic uplift is claimed.

## Verdict

`PASS_ALGEBRAIC_TOY` only means the chosen uplift ansatz can produce a local
Minkowski minimum. It does not derive the uplift sector or prove metastability
against omitted fields.
