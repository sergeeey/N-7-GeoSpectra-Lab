# UV Completion Requirements and No-Go Map

## Executive summary

GeoSpectra currently supports a disciplined phenomenological toy model, not a fully closed first-principles UV completion. The internal geometry and spectral analysis have exhausted the lambda-origin route, the physical mass-ratio route, and the neutrino Majorana route.

The right boundary condition for external work is now explicit: a UV/string completion must provide a mechanism for exp(-lambda/rho6^2), a full reduced 4D action, a canonical radion, a same-frame KK scale, and (if desired) a B-L breaking sector.

## What the current repository supports

- A phenomenological spectral compactification toy model.
- A derived SM-like one-generation structure from S^3 × S^6.
- Exact N_gen = 3 from the G73/G74A/G74B chain.
- Exact Dirac-only status for the current right-handed neutrino branch.
- Lambda is tracked as FREE_COUPLING_PARAMETER, not as a derived quantity.

## What the current repository does not support

- A derived lambda origin from internal geometry or spectral data.
- A confirmed physical m_mod/m_KK ratio from a full reduced 4D action.
- A bare Majorana mass for nu_R in the current branch.

## No-go map

| Route | Checked by | Verdict | Why failed | What is needed to revive it |
|---|---|---|---|---|
| Standard gauge reduction | G84A | FAIL_FOR_INVERSE_SQUARE | Unwarped reduction yields positive powers (+12/+6), not 1/rho6^2. | A non-standard gauge kinetic function or additional dilaton/warp/duality prefactor. |
| Spectral / proper-time | G84B, G85A | FORMS_ONLY | The inverse-square form appears only at integrand level; no final A*exp(-lambda/rho6^2) term is derived. | A determinant or resummation step that produces a fixed effective exponential coefficient. |
| Poisson / theta resummation | G85A | BRIDGE_MISSING | A theta/Poisson identity exists, but it does not close the bridge to the inverse-square effective term. | A final identification of the resummed expression with a rho6-dependent effective potential term. |
| Saddle / worldline | G85B | NULL | The saddle gives exp(-3)=const, not exp(-lambda/rho6^2). | A rho6-dependent saddle that survives integration and produces the target functional form. |
| Dual modulus | G86A | STRUCTURAL_POWER_LAW_ONLY | Power-law T(rho6) always integrates to a power law, never to the desired inverse-square exponential. | A non-power-law modulus relation or a different UV mechanism. |
| Warp factor | G86B | TRIVIAL_OR_CIRCULAR | Uniform warp is trivial; localized warp becomes power-law plus free Q; the target form is circular. | A derived warp/dilaton equation with a genuine rho6-dependent exponential source. |
| Dimensional lambda gate | META-C1 / G83-G86B | PROMOTE_FREE_PARAMETER | Buckingham-Pi style reasoning shows geometric lambda collapses to rho6^2 along the trajectory. | A non-geometric source for lambda. |
| Physical mass ratio / canonical normalization | G88D, G88E, G88F | INSUFFICIENT_ACTION | No full reduced 4D action, no same-frame KK map, and only proxy-level masses are available. | A full 4D Einstein-frame reduced action with canonical radion and consistent KK/Planck/string normalization. |
| Majorana mass / neutrino seesaw | G89A, G89B | DIRAC_ONLY_CONFIRMED | Exact B-L forbids a bare Majorana mass and no B-L=+2 compensator exists. | An explicit B-L breaking sector or new operator with charge +2. |

## UV completion requirements

1. A mechanism for exp(-lambda/rho6^2).
2. A source for lambda.
3. A hidden gauge / brane / instanton sector or comparable UV origin.
4. A full 4D reduced action.
5. Canonical radion normalization.
6. Same-frame KK scale.
7. A B-L breaking sector if Majorana/seesaw neutrinos are desired.
8. Otherwise an explicit Dirac-only neutrino prediction.

## Status of the three bottlenecks

- Lambda origin: `FREE_COUPLING_PARAMETER` — Track B is exhausted; lambda is not derived in the current repository.
- Physical mass ratio: `INSUFFICIENT_ACTION` — 2.02% is a coordinate-curvature proxy; ~0.252% is a canonical proxy, but not a confirmed physical ratio.
- Right-handed neutrino Majorana mass: `DIRAC_ONLY_CONFIRMED` — Bare Majorana mass is forbidden by exact B-L in the current branch; Dirac-only is the current prediction.

## What would count as success

- Show a real non-perturbative mechanism for exp(-lambda/rho6^2).
- Derive lambda from that mechanism, not by convention.
- Reconstruct a reduced 4D action and canonically normalize the radion.
- Define the KK scale in the same frame and normalization as the mass.
- If Majorana neutrinos are desired, add explicit B-L breaking.
- If no B-L breaking is added, state Dirac-only neutrinos as the prediction.

## Commit anchors

- `9752c93` — `test(audit): close physical mass ratio as insufficient action`
- `7792811` — `test(audit): close neutrino Majorana channel as Dirac-only`

## Bottom line

The repository is strong as a phenomenological spectral toy model, but the stronger claims remain blocked until an external UV completion supplies the missing action, normalization, and non-perturbative input.
