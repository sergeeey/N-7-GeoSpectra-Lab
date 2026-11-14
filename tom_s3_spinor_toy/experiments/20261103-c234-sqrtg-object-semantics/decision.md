# C234 Decision -- The object behind "sqrt|g| in harmonics"

**Date:** 2026-11-03

## Result

Exact sympy at three regular points, 24 asserted checks and 3 self-controls, exit 0 (`run_output_sqrtg_object_semantics.txt`).

- sqrt(det g) of the round S^3 is sin(eta)cos(eta) in Hopf coordinates and (2/(1+r^2))^3 in stereographic coordinates. At the same point the values differ: 1/2 versus 1/8 at (1/2,1/2,1/2,1/2); 1/2 versus 27/8 at (1/2,1/2,1/2,-1/2); 2 sqrt(5)/9 versus 1 at (1/3,2/3,2/3,0). So sqrt(det g) as a function on S^3 is a scalar density (weight 1): its value depends on the coordinates, and for the round metric it is a property of the chart, not of the geometry.
- The ratio rho = sqrt(det g_deformed)/sqrt(det g_round) in the same coordinates has the same value at the same point in both charts: it is a scalar. For g = exp(2 e x4) g_round: rho = exp(3 e x4); for g = g_round + e dx4 (x) dx4: rho = sqrt(1 + e (1 - x4^2)).
- To first order rho = 1 + (1/2) tr h; for h = 2 e x4 g_round it is 1 + 3 e x4: a degree-1 harmonic, a member of the (1/2,1/2) multiplet of TOM-CERT-01.

## Which readings of his plan are well defined

(a) the coordinate density in Hopf coordinates: well defined as a function of three angles, but a chart artefact for the round metric; (b) the invariant volume form: a form, not a function; (c) the scalar ratio of the deformed to a reference density: well defined and the natural object for "deformation of the de Sitter slice"; (d) other scalars built from the metric (curvature invariants). Which one he means is [UNKNOWN] and must be asked neutrally.

## What this does NOT imply

- that (c) is his meaning
- that the first-order degree-1 content has anything to do with the right-handed neutrino: that is a hypothesis in the call note

## Caveat

Closed forms are checked at three points (exactly), and for two deformations; this is not a symbolic proof for all points.

Ledger: C234_SQRT_DET_G_IS_A_SCALAR_DENSITY_THE_RATIO_TO_A_REFERENCE_DENSITY_IS_A_SCALAR_FIRST_ORDER_IS_DEGREE_ONE_HARMONIC
Follow-ups: none
