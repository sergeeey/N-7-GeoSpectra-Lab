# P4B Recovered Lawrence Frames

Date: 2026-06-07

Scope: update the Lawrence mapping status after recovery of direct frame text for
the S3 coordinate chart and Cartan generators.

## Executive Verdict

<fact> The recovered frame text provides an explicit Lawrence `S3` embedding and
an explicit Cartan-generator pair.

<inference> The prior P4 verdict `source_insufficient` is no longer the best
status for the S3 Cartan mapping layer.

<inference> Updated S3 status:

```text
source_sufficient_for_cartan_mapping
runtime verdict = research_only
```

<inference> Lawrence-specific runtime safety is still not reached because the
non-Cartan generators, `alpha`-dependence, `cot(2 alpha)`, `V` selection rules,
and full Dirac/spinor interpretation are not yet validated.

## Recovered S3 Evidence

<fact> Recovered frame formulas:

```text
x1 = rho sin(alpha) cos(theta)
x2 = rho sin(alpha) sin(theta)
x3 = rho cos(alpha) sin(theta_tilde)
x4 = rho cos(alpha) cos(theta_tilde)

i I_3L = 1/2 (partial_theta + partial_theta_tilde)
i I_3R = 1/2 (partial_theta - partial_theta_tilde)

chi(theta, theta_tilde)
  = exp(i[(i_L + i_R) theta + (i_L - i_R) theta_tilde])
```

<inference> Ben Achour displayed-phase conventions can be matched to the
Lawrence Cartan layer by the local identification:

```text
phi_BA <-> theta_L
theta_BA <-> theta_tilde_L
m_+ <-> i_L
m_- <-> i_R
```

## Remaining Blockers

- non-Cartan generators;
- `alpha`-dependence;
- `cot(2 alpha)` diagnostic;
- `V`-coupling selection rules;
- full Dirac / spinor interpretation.

## Next Gate

```text
P5_LAWRENCE_NONCARTAN_AND_SELECTION_RULE_VALIDATION
```

## Separate S6 Track

<fact> The recovered-frame package also opens a separate `S3 x S6` / `SU(4)`
track involving embedding, `SO(7)/SO(6)` local translations, hypercharge, and
right-handed neutrino background invariance.

<inference> This is a separate audit stream and should not be merged with the S3
Cartan-sign result.

```text
P6_S6_SU4_GAUGE_BREAKING_AUDIT
```
