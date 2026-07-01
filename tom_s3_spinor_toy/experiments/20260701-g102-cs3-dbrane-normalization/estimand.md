# Estimand — G102: does c_S3 (G94) reduce to a prediction for g_s?

**Date:** 2026-07-01
**FL tier:** Full
**Question type:** [x] descriptive  [ ] predictive  [ ] causal

## Background

G94 introduces a D2-brane instanton NP term A_S3*exp(-c_S3*rho3^3) to
stabilize rho3. c_S3 is currently a SCANNED parameter (valid range
0.248-0.372, found by requiring EFT-validity + path-constraint recovery),
not derived from a brane-action formula. This mirrors the lambda_np
situation (S6 side): "candidates not first-principles derivations" per
the parameter registry.

Source trace (FL Step -4, required for this AI-assisted claim):
Standard Dp-brane tension formula, cross-confirmed via 2 independent web
searches (WebSearch, 2026-07-01) citing Polchinski's convention:
  T_p = 1 / ((2*pi)^p * alpha'^((p+1)/2) * g_s)
For a Euclidean D2-brane (E2, p=2) wrapping a 3-cycle of volume V:
  S_inst = T_2 * V = V / ((2*pi)^2 * alpha'^(3/2) * g_s)
Direct primary-source PDF fetch (arXiv:2310.20559) FAILED to parse cleanly
(garbled/corrupted extraction, produced a self-inconsistent formula) --
this source is NOT used as a citation; only the cross-confirmed WebSearch
summary is used, at [WEAK-MEDIUM] confidence (textbook-standard formula,
multiple independent aggregator agreement, but no clean primary-source
read achieved this session).

## Critical risk found during source trace (drives the kill criterion)

GA2 (this repo, 2026-06-26) explicitly states its own M_Pl^2 = M_s^(D-2)*V_9
convention "using geometric volume WITHOUT momentum-space (2*pi) factors;
consistent with G91 potential normalisation" -- i.e. THIS REPO's convention
already deviates from the standard textbook KK-reduction formula by
dropping (2*pi)^d factors. Applying the STANDARD Dp-brane tension formula
(which DOES carry explicit (2*pi)^p factors) directly to this repo's
rho3/g_s definitions, without reconciling the two conventions, risks
introducing spurious powers of 2*pi into any g_s prediction -- the exact
same class of convention-mismatch trap as G98 (diagonal-vs-offdiagonal
artifact) and G101 (Lie-algebra-generator-count mismatch).

## Estimand

**Population:** the D2-brane instanton term introduced in G94, in the
specific normalization convention already fixed by G91/GA2 (rho3 in string
units M_s=1, VOL_S3_UNIT=2*pi^2, no momentum-space 2*pi factors in the
Planck-mass relation).

**Intervention:** substitute the standard Dp-brane tension formula
(T_2 = 1/((2*pi)^2 * alpha'^(3/2) * g_s)) into G94's ansatz
S_inst = c_S3 * Vol(S3) = c_S3 * VOL_S3_UNIT * rho3^3, using THIS repo's
own rho3-to-l_s convention (rho3 dimensionless, physical radius = rho3*l_s,
per GA2), and solve for c_S3 in terms of g_s ALONE (not as a free scan).

**Comparator:** G94's current treatment (c_S3 as a free scanned parameter,
valid range found empirically by path+EFT constraints) vs a version where
c_S3 = f(g_s) is fixed by the brane-tension formula, and the EMPIRICALLY
valid range (0.248, 0.372) is reinterpreted as a PREDICTED range for g_s.

**Endpoint:** does substituting the standard tension formula give
c_S3 = 1/(2*g_s) EXACTLY (my preliminary hand-derivation, NOT yet verified
against the repo's exact 2*pi conventions), or does reconciling GA2's
missing-2*pi convention change this coefficient?

**Summary measure:** the exact numeric/symbolic relationship c_S3 = f(g_s),
and the implied g_s range from G94's valid c_S3 window.

**MCID:** any relationship that is NOT simply "c_S3 is unconstrained /
g_s cancels out entirely" is sufficient to show this is a real constraint,
not vacuous.

## Intercurrent events (ICE)

None -- symbolic derivation, no missing data. The convention-reconciliation
step (GA2's dropped 2*pi factors) is the primary source of ambiguity, to be
resolved by explicit unit tracking, not treated as noise.

## What this result does NOT mean

1. Does NOT mean g_s is measured or independently verified -- at most this
   would show G94's valid c_S3 window CORRESPONDS to a specific g_s range,
   which is a NEW testable constraint, not a measurement.
2. Does NOT resolve whether that g_s range is physically sensible (e.g. if
   it implies g_s > 1, that is a real tension with perturbative string
   theory requiring separate discussion, not silently accepted).
3. Does NOT change lambda_np's status (S6-side NP exponent) -- this is
   about c_S3 (S3-side) specifically; the two are structurally analogous
   but were established independently (G60/G61 for lambda_np vs G94 for
   c_S3) and are not assumed to share a resolution mechanism.
4. If the convention mismatch (GA2's missing 2*pi) cannot be cleanly
   reconciled: does NOT mean the brane-instanton picture is wrong -- it
   means this repo's simplified normalization is not yet precise enough
   to extract a g_s prediction, a documentable limitation, not a refutation.
