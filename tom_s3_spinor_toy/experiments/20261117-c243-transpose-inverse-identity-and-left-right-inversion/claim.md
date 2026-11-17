# C243 Claim -- The transposed SU(2) matrix is the inverse element conjugated by sigma2; inversion on S^3 reverses orientation and swaps left and right

**Date:** 2026-11-17
**FL tier:** [x] Micro (record of an exact calculation; no project physics claim)
**Question type:** [x] descriptive (exact calculation; no population, no intervention)

## Estimand

We establish, exactly, for every u in SU(2): u^T = sigma2 u^{-1} sigma2 and u^T e1 = i sigma2 u^{-1} e2. We record the standard facts that inversion on S^3 reverses its orientation and turns left translations into right translations, and three negative controls that bound what is claimed.

## What this result does NOT mean

- does not say that the sign question of C242 is a question of left versus right SU(2), or of which SU(2) is the spin: that link is a HYPOTHESIS and needs the correspondent's explicit definitions
- does not say anything about the earlier contragredient-representation issue: no comparison was made (UNVERIFIED)
- does not say that SU(2) cannot map one doublet to another: for one pair it can (transitivity); only a FIXED element realising the reflection at all points is excluded
- does not identify inversion on S^3 with the reflection of the 2-sphere in C242; the S^3 statement is a standard fact stated alongside the algebraic identity

## Kill criterion

Any check in the script failing on re-run, or a numeric worst residual reaching 1e-12.

## Status of the evidence

Written and run in this folder on 2026-11-17, after an external note (a language-model "radar") raised the antiunitary and left/right questions and a review of its claims. The exact part uses a, b and their conjugates as independent symbols; the numeric part uses random unit quaternions. The S^3 orientation and left/right facts are standard. Same-model-family review only; no independent human review.
