# C231 Claim -- The tangential Cauchy-Riemann kernel on S^3 and the doublet

**Date:** 2026-11-03
**FL tier:** [x] Micro (exact algebra; no project physics claim)
**Question type:** [x] descriptive

## Estimand

We compute exactly the kernel of Lbar = x1 d/dy2 - x2 d/dy1 on functions of (xi, conj xi) on S^3 with Hopf charge n, its SU(2) type, the weights of the holomorphic and anti-holomorphic doublets, and whether H2 of C228 equals {f(xi) J xi : f holomorphic of degree 1}.

## What this result does NOT mean

- does not say that Lbar f = 0 is the correspondent's field equation; it identifies a first-order equation whose degree-1 kernel is a doublet
- does not claim novelty: the dimension n+1 for charge n is the Borel-Weil / Riemann-Roch pattern, source not opened here
- the identification of H2 holds in the gauge xi^1 real used by C228

## Kill criterion

Any asserted claim failing, or a self-control not caught.

## Status of the evidence

Predictions P1-P4 are in the script docstring, written before the run. During development two of my own checks failed for reasons in my checks (a trig simplification that could not reduce a correct identity, and a badly designed self-control); a control with `and False` that could never fail was removed. No independent human review.
