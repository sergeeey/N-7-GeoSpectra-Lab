# G88D Claim: Full 4D reduced action and canonical mass extraction audit

## Hypothesis

The project's reported `m_mod / m_KK` can be promoted to a physical mass ratio only if the local repository data already reconstructs a normalized 4D Einstein-frame action, fixes the radion canonical field, and defines the KK scale in the same normalization.

## What must be shown for success

`PHYSICAL_CONFIRMED` is allowed only if all of the following are explicit:

1. a reduced 4D action is reconstructed or imported from local repo data;
2. the Einstein-frame normalization is explicit;
3. the radion kinetic term is canonicalized explicitly;
4. the mass is extracted as the second derivative in the canonical field;
5. the KK scale is defined in the same frame and normalization as the mass;
6. the resulting ratio is stable under coordinate reparametrization of `rho6`.

## What falsifies the physical claim

- only a coordinate-space curvature proxy is available;
- canonical normalization exists but the reduced action is incomplete;
- the KK scale is defined only in a different convention/frame;
- the ratio changes under `rho6` reparametrization;
- the reduced-action / frame map is missing.

## Allowed verdicts

- `PHYSICAL_CONFIRMED`
- `CANONICAL_PROXY_ONLY`
- `COORDINATE_ARTIFACT`
- `INVALID_ACTION`
- `INSUFFICIENT_ACTION`
- `MIXED`

## Reproduction command

```powershell
python tom_s3_spinor_toy/experiments/20260623-g88d-full-4d-reduced-action-mass-extraction/g88d_full_4d_reduced_action_mass_extraction.py
```

