# G77 Decision вЂ” PASS_ALGEBRAIC_TOY

**Date:** 2026-06-22
**Verdict:** `PASS_ALGEBRAIC_TOY` вЂ” the uplift ansatz admits local Minkowski minima

## Scheme A вЂ” enforce the Minkowski minimum at rho6_star

Choose `p`, fix `rho0=rho6_star=1.090`, and solve `V(rho0)=0` and
`V'(rho0)=0` for `(A_np,D)`.

| p | A_np | shift vs 0.3787 | D (K=1) | D (K=K_vol) |
|---:|---:|---:|---:|---:|
| 2 | 0.401215 | +5.95% | 0.0071833 | 1.1003e-5 |
| 4 | 0.407268 | +7.54% | 0.0108290 | 1.6587e-5 |
| 6 | 0.417772 | +10.32% | 0.0175970 | 2.6955e-5 |
| 8 | 0.440495 | +16.32% | 0.0330662 | 5.0650e-5 |

## Scheme B вЂ” uplift the AdS branch while retaining old A_np

Keep `A_np=0.3787`, then solve `V(rho0)=0` and `V'(rho0)=0` for the shifted
Minkowski minimum `rho0` and `D`.

| p | rho0 | shift vs rho_star | D (K=1) | D (K=K_vol) |
|---:|---:|---:|---:|---:|
| 2 | 1.196437 | +9.76% | 0.0023249 | 3.5611e-6 |
| 4 | 1.222196 | +12.13% | 0.0033946 | 5.1998e-6 |
| 6 | 1.264358 | +16.00% | 0.0052304 | 8.0117e-6 |
| 8 | 1.345853 | +23.47% | 0.0088356 | 1.3534e-5 |

Every row has `D>0`, `V=0`, `V'=0`, and `V''>0`.

## Normalization control

`K_vol=652.841994`. A value of `D` quoted in the `K=1` convention must be
divided by `K_vol` before it is inserted into the repository potential.
The deliberate wrong-convention control leaves a residual `V=0.00604` and fails.

## Scope

This proves algebraic viability of the toy uplift only. It does not derive `p`,
the microscopic source of `D`, multi-field stability, or a string embedding.
The uplift exponent `p` and microscopic uplift sector remain `FREE`/`OPEN`.

Run:

```bash
python tom_s3_spinor_toy/experiments/20260622-g77-uplift-solver/g77_uplift_solver.py
python -m pytest tom_s3_spinor_toy/tests/test_g77_uplift_solver.py -q
python -m pytest tom_s3_spinor_toy/tests/test_markdown_claim_audit.py -q
```

The generated `results_g77.json` is authoritative for full-precision values.
