# TOM-CERT-01 Claim -- W = span{g_ab} in L^2(S^3): exact certificate of the SU(2)_L x SU(2)_R structure

**Date:** 2026-11-03
**FL tier:** [x] Micro (exact algebraic record; no project physics claim)
**Question type:** [x] descriptive (exact algebra; no population, no intervention)

## Estimand

We establish, with exact Gaussian-rational arithmetic, the action of SU(2)_L and SU(2)_R on the four matrix-element functions g_ab on S^3 = SU(2) (conventions in `verifier.py` docstring), the closure of W under both actions, its decomposition into two left doublets (fixed column) and two right doublets (fixed row), and its irreducibility with Casimirs (3/4, 3/4), i.e. type (1/2, 1/2).

## What this result does NOT mean

- does not say which SU(2) is spin, or that W is the correspondent's multiplet
- does not derive or select any field equation, and says nothing about D_0
- does not prove that physical fermions exist; no statement about statistics
- does not carry over anything from the POVM project (only the method of certificate + separate verifier + declared negative controls)
- does not cover functions of degree > 1 (W is the degree-1 block only)

## Kill criterion

Any check of `verifier.py` failing on the valid certificate; any negative control accepted or rejected for a reason other than the one declared in `negative_controls.py`; a fresh build in a clean copy differing from the stored certificate.

## Status of the evidence

Builder (sympy) and verifier (stdlib `fractions`) were written by the same author in one session; they share the conventions, not the code. No independent human review yet. A context-blind skeptic agent (same model family) reviewed the folder on 2026-11-03: the mathematics was confirmed by its own derivation; its verifier-weakness findings (vacuous empty fields, group checks blind to the stated convention) were fixed and covered by new controls. See `REPORT_RU.md` section 7a for limits.
