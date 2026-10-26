# G94 UV gap: Does a wrapped Euclidean D2 determine the instanton amplitude?

**Research status:** CONDITIONAL / AMPLITUDE NONIDENTIFIABLE (2026-10-27). **Evidence-only supplement** to PR #9. No changes to G94 code or tracker status. Base source: `main` at `40ae3f402bbc829c1bb4a53b5d71d122d7123bbc`.

## Independent physical input and its limits

For a conventional 10D Type IIA Euclidean D2 wrapping a round string-frame S3 of radius `R3=rho3*sqrt(alpha')`, and under constant dilaton, zero world-volume flux and no warping:

```
T_D2 = 1 / [(2*pi)^2 * g_s * alpha'^(3/2)]
Vol(S3) = 2*pi^2*R3^3
S_cl = rho3^3/(2*g_s)
c = 1/(2*g_s)        (conditional identification with G94 exp(-c*rho3^3)).
```

Thus G94's preferred `c=.235` would imply `g_s≈2.13`, not weak coupling. However the toy background `M4×S3×S6` is **13-dimensional**, unlike conventional Type IIA's ten dimensions. This is an **imported conditional analogy**, not an established string embedding or a physical derivation for G94.

The classical brane tension gives the exponential slope, **not** the `+A3` scalar-potential prefactor. One-loop determinants, fermionic zero modes, collective-coordinate measures, RR/axion phases, frame factors and flux/orientifold content are not specified. A wrapped Euclidean brane need not produce a positive standalone potential term; familiar BPS instantons may instead correct a superpotential.

## Bounded test of corrected G94 calibration

`A3_correct = -Nref*exp(c*r3ref^3)/(1+c*r3ref^3)`, where `Nref<0`, at the G91 constrained reference. This corrects the published derivative-sign defect but is still **fitted to a reference state**, not derived from an instanton determinant.

The complete stationary-locus equations are

```
u=lambda/r6^2; ustar=lambda/rstar^2; E=exp(ustar-u); z=c*r3^3
z=u*E / [3*(E-1)-u*E]
A_required=B*(E-1)*exp(z)/(1+z)
B=15*(.986)^3/(16*pi); lambda=1/3
```

At the original anchor `rstar=1.09`:

| g_s | c | corrected A3 | strict local 2D minimum | deviation from r3=r6^2 |
|---:|---:|---:|---|---:|
| 2.13 | .235 | .01372 | none | — |
| 1.0 | .5 | .01947 | none | — |
| .5 | 1 | .04742 | (.980, 1.433) | 52.3% |
| .2 | 2.5 | 1.2747 | (1.331, 1.292) | 20.3% |
| .1 | 5 | 562.98 | (1.366, 1.277) | 16.3% |
| .0625 | 8 | 1.143e6 | (1.376, 1.272) | 15.0% |
| .05 | 10 | 1.990e8 | (1.379, 1.271) | 14.6% |

The alternate radius `rstar=1.1541` is a **user-reported, not independently established C219 input**. Its `g_s=.1` (`c=5`) row gives `A3≈8.657e4`, minimum `(1.540,1.348)` and 15.22% deviation.

All 10 numerical minima across both anchors were checked by a separate finite-difference implementation of the **raw** potential: max absolute logarithmic gradient `9.11e-11`, all Hessian eigenvalues positive. These are toy-model results, not physical predictions. Even at small `g_s` the radii remain ~1–1.5 string lengths, so alpha-prime control is unproven.

## Post-hoc exact-path inverse (exploratory, not prediction)

Solving both 2D stationarity equations and **imposing** `r3=r6^2` to invert for the needed `A3` at `g_s=.1` (`c=5`):
- original radius: `A3≈1.60435e6`, `(r3,r6)≈(1.61848,1.27219)`, `S≈21.20`;
- conditional C219 radius: `A3≈3.99014e9`, `(r3,r6)≈(1.80625,1.34397)`, `S≈29.46`.

Because `A3_correct` grows as `exp(c*r3ref^3)/(1+c*r3ref^3)`, it compensates semiclassical exponential suppression by construction. Such growth cannot be attributed to an ordinary one-loop determinant without independent microscopic calculation. These are not universal no-go results for other potentials.

## Decision

**Do not promote “D2-instanton dynamically selects G94 path” to physical mechanism.** Conventional D2 tension, even conditionally applied, cannot fix the G94 4D prefactor/sign and therefore cannot independently predict a stable minimum. Next evidence needed: consistent UV dimensional embedding, string/Einst. frame map, dilaton/flux/brane zero-mode content, microscopic determinant and full normalized 4D effective action. Until supplied, record `A3 = FREE / UV-BLOCKED`.

Sources:
- Polchinski, *Dirichlet Branes and Ramond-Ramond Charges* (1995), https://doi.org/10.1103/PhysRevLett.75.4724
- Alexandrov et al., *D-instanton induced superpotential* (2022), https://doi.org/10.1007/JHEP07(2022)090
- Alexandrov, Sen, Stefański, *D-instantons in Type IIA string theory on Calabi-Yau threefolds*, https://arxiv.org/abs/2108.04265
- Lawrence, *Covariant Compactification*, public v3, https://www.preprints.org/manuscript/202303.0314

Execution: numerical calculations in a separate Python environment; no full project CI and no derived Tom Lawrence field equation. A reproducibility package was generated in the conversation, containing `research_contract.yaml`, `verify_d2_amplitude.py`, `finite_difference_validation.py`, `exact_path_exploratory.py`, and machine-readable outputs.
