# C230 Claim -- Which J-equivariant first-order operators on C^2-valued functions on S^2 preserve H2

**Date:** 2026-11-03
**FL tier:** [x] Micro (exact algebra; no project physics claim)
**Question type:** [x] descriptive

## Estimand

For the family O = a + b (sigma.L) + c Gamma + d Gamma (sigma.L) (Gamma = sigma.n, L = -i x cross grad, J = L + sigma/2), we decide exactly for which (a, b, c, d) the two-dimensional space H2 = span{Psi, Phi} of C228 is mapped into itself, and whether a constant matrix M added to A = 2(1 + sigma.L) can make H2 invariant.

## What this result does NOT mean

- does not say the correspondent's operator is in this family, or that H2 is his multiplet
- does not cover operators of second order or non-equivariant ones
- does not contradict C228: for D0 itself (b + d = 2) the leak is confirmed

## Kill criterion

Any asserted claim failing, or a self-control (the equivariance test, or the solver saying yes for O*) not behaving as declared.

## Status of the evidence

Predictions are in the script docstring, written before the run. During development the first run FAILED two checks because my symbolic simplification could not reduce correct expressions; a later control caught a faulty check of mine (an exact-zero test on unsimplified roots of -1) before it produced a wrong "no M exists" conclusion. No independent human review.
