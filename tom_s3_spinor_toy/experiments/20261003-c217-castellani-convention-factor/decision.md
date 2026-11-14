# C217 Decision — C213's Castellani curvature is exactly 1/2 x the standard
# curvature (a CONVENTION factor, eq. 3.34); C216's anomaly resolved,
# C214's REJECT retracted, C215's 1.5 corrected to 4.0

**Date:** 2026-10-03
**Verdict:** PASS — `UNIFORM_FACTOR_2_CONFIRMED`. Pre-registered prediction (claim.md, written before running) held on every check.

## Results [VERIFIED-numpy, component-wise, 6^4 = 1296 entries per space]

```
CONTROL SO(7)/SO(6) (only term2 active, max|C_KKK| = 0):
  as_is x1       : max|R_code - R_round| = 5.0e-01   Ric = 2.5
  uniform x2     : max|R_code - R_round| = 4.4e-16   Ric = 5.0
  term2_only x2  : 4.4e-16   (expected: only term2 is active here -> cannot discriminate)
  KN + Friedrich-Ivanov (no Castellani): Ric^g = 5.0, |Ric - 5 I| = 1.8e-15

G2/SU(3), ambient-unit frame (max|C_KKK| = 0.458; terms 1,2,4 active):
  ambient-Gram error 1.2e-15, generators antisymmetric to 1.5e-15
  as_is x1       : 5.0e-01      Ric = 2.5      <- negative control FAILS (as it must)
  uniform x2     : 2.0e-15      Ric = 5.0      <- matches the unit round S6 tensor
  term2_only x2  : 2.5e-01      Ric = 4.5      <- negative control FAILS (as it must)
  KN + Friedrich-Ivanov (no Castellani): Ric^g = 5.0, |Ric - 5 I| = 5.3e-15
```

`results_c217.json`, script `c217_castellani_factor.py`.

## Root cause, from the primary source [VERIFIED, arXiv hep-th/9912277 v1 text]

Castellani eq. (3.34): `R^a_b = dB^a_b + B^a_c ^ B^c_b = R^a_{b de} V^d ^ V^e`.
The standard definition is `R^a_b = 1/2 R^a_{b de} V^d ^ V^e`. The paper's
components (3.35) are therefore exactly 1/2 of the standard Riemann
components, and the code's Ricci (a trace over them) is exactly 1/2 of the
standard Ricci. Nothing is wrong with the transcription of (3.35)-(3.36); the
paper's definition (3.34) has no 1/2. (The paper also uses a negative flat
metric `eta_ab = -delta_ab`; the sign is already absorbed by the C213
calibration and is not part of this question.)

## What this resolves

| Item | Before | After |
|---|---|---|
| C213 Ricci of S6=G2/SU(3), G96 native `r=1` | `5/6` | `5/3` (standard convention); Einstein-ness/isotropy unchanged |
| C213/C214 Ricci at the ambient-unit frame | `2.5` | `5.0` = round unit S6 (`n-1`) |
| C216 "unresolved Castellani anomaly" | 2 hypotheses refuted, cause unknown | cause = eq. 3.34 convention; both listed hypotheses were wrong |
| C215 `Ric^grad` (characteristic connection) | `1.5` | `4.0` = `5.0 - 1.0`; isotropy check still valid; KN gives 4.0 independently |
| C214 REJECT of `Ric = (5/24)|T^c|^2` | rejected (50% mismatch) | **RETRACTED**: the bridge predicted 5.0 = the true standard Ricci; the "mismatch" was against a half-convention number. `5/24 * 24 = 5` |
| C212 torsion `|T|^2 = 24` (ambient-unit) | PASS | unchanged |

Why this was missed for a day (record, not blame): the N^010 calibration
reproduced the paper's published `R = 12` with the code, which validates the
code against the paper's own convention, not against the standard definition.
It was a real calibration of the wrong target. The independent positive control
that exposed it (SO(7)/SO(6), textbook `Ric = n-1`) was the first one with a
convention-independent answer.

## Kill analysis

**Killed:** C214's REJECT (retracted), C215's value `1.5`, and C216's two
"refuted" explanations as explanations (each was a correct negative on a
non-uniform change, but the uniform all-term factor was never tested there).
**Not killed:** C212 (torsion), C213's structural findings (Einstein, isotropic,
code reproduces the paper's own N^010 numbers), the KN implementation, the
Friedrich-Ivanov formula, Russo's theorem, `Ric = 5 mu^2` with `mu^2 = |T|^2/24`.

## What this does NOT establish

1. N^010 in the standard convention: if the factor is uniform there too the
   standard `R` is 24 for the published points; not checked against any
   independent N^010 value.
2. It does not use or check the paper's Einstein equation of motion (which is
   written in the paper's own convention).
3. Gate/F6 status unchanged: this is an internal consistency correction of S6's
   intrinsic curvature numbers, not a new equation-of-motion input.

## Process note (for the record)

C216's skeptic fallback (the `reviewer` cap was closed) found this: the verdict
was NEEDS_WORK and its single most useful finding was that the pending
"anomaly" was already settled by data in hand. Corrections to C213/C214/C215/
C216 were made as dated addenda, not by rewriting verdict lines silently.
