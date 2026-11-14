# C234 Claim -- What "sqrt|g| expanded in S^3 harmonics" can mean: density versus scalar

**Date:** 2026-11-03
**FL tier:** [x] Micro (exact calculation; no project physics claim)
**Question type:** [x] descriptive

## Estimand

We compute, at regular points and exactly, sqrt(det g) of the unit S^3 from the pull-back metric in Hopf and in stereographic coordinates; we compare the values at the same point; and we test whether the ratio of the deformed to the round sqrt(det g), both in the same coordinates, is the same in both systems and has the stated closed forms.

## What this result does NOT mean

- does not say what the correspondent intends to expand; it lists which readings are well defined
- does not say his idea is wrong: a density is a legitimate object once a reference density is fixed
- the closed forms are for two example deformations, not for every deformation

## Kill criterion

Any asserted claim failing, or a self-control not caught.

## Status of the evidence

Predictions O1-O3 are in the script docstring, before the run. Development was bumpy: the first version relied on a simplifier that could not reduce correct expressions and put a ratio check at a coordinate singularity of the Hopf chart; a later version had a point-equality check that was silently comparing a matrix with 0 (fixed). No independent human review.
