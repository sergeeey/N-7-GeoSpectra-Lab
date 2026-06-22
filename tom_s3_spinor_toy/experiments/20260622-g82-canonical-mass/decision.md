# G82 Decision вЂ” CONDITIONAL

**Date:** 2026-06-22
**Verdict:** `CONDITIONAL` вЂ” G62's 2.02% is a coordinate-curvature proxy, not yet a physical mass ratio

## Result

For the standard 4D Einstein-frame product-space kinetic metric,

`G_ij = n_i delta_ij + n_i n_j/2`,

and the imposed path `rho3=C*rho6^2`, the logarithmic tangent is `(2,1)` and

`G_path = 90`.

At `rho_min=1.179058`:

- old coordinate proxy: `m_mod/m_KK = 0.020248` (2.02%)
- metric-only canonical proxy with `M4=Ms=1`: `0.0025165` (0.252%)
- correction factor: `0.12428`
- analytic Hessian transform and independent finite difference agree to `1.1e-5` relative

## Interpretation

The 2.02% headline is not canonically normalized and is not a confirmed
physical mass ratio. The 0.252% value is only a metric-level conditional proxy:
the physical ratio still requires the explicitly normalized reduced 4D action,
the Planck/string scale map `M4/Ms`, and proof that the imposed
one-dimensional constraint is the physical mass eigen-direction.

All algebraic gates pass, but physical identifiability does not.

```bash
python tom_s3_spinor_toy/experiments/20260622-g82-canonical-mass/g82_canonical_mass.py
python -m pytest tom_s3_spinor_toy/tests/test_g82_canonical_mass.py -q
python -m pytest tom_s3_spinor_toy/tests/test_markdown_claim_audit.py -q
```
