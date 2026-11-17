# C242 Claim -- Second component of the doublet representative derived two ways, and the relation between two sign versions

**Date:** 2026-11-16
**FL tier:** [x] Micro (record of an exact calculation; no project physics claim)
**Question type:** [x] descriptive (exact calculation; no population, no intervention)

## Estimand

We establish, exactly, (1) the second component of the doublet representative for a point on the 2-sphere, from V^i = (1/2) xi^dagger sigma^i xi alone; (2) the same component from u = cos(theta/2) I + i sin(theta/2) n.sigma acting on (r, 0)^T, under two stated input assumptions; (3) the exact relation between the two sign versions of that component, including the matrix entry of u that each corresponds to.

## What this result does NOT mean

- does not establish the two input assumptions: th n = (t1, t2, 0) for the unit vector n in u, and sin(phi) = t1/th, cos(phi) = -t2/th for the standard coordinates; both are inputs
- does not say which of the two sign versions the correspondent intends
- does not give a physical meaning to the orientation reversal V -> (-V^1, V^2, V^3); it shows only that the map has determinant -1
- does not establish that this is the same issue as the anti-representation or transposed readings of C229; the algebraic fact shown is that the second version is built from u^T, which is a hypothesis-generating link, not a result

## Kill criterion

Any check in the script failing on re-run, or the numeric worst residual reaching 1e-12.

## Status of the evidence

Written and run in this folder on 2026-11-16. The three precursor scripts were run earlier the same day in the private correspondence folder (all PASS) and merged here, with the correspondent's name removed from comments. The numeric part uses a matrix exponential (no closed form for u) and is an independent code path. Same-model-family review only (four fresh-context reviews of the letter that uses these results). No independent human review.
