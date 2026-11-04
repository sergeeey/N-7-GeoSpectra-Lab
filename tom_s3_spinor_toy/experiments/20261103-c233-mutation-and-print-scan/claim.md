# C233 Claim -- Mutation testing and a print-only scan of the Tom-line scripts

**Date:** 2026-11-03
**FL tier:** [x] Micro (instrument run; no project physics claim)
**Question type:** [x] descriptive

## Estimand

We measure how many seeded AST mutations of C225, C226, C229, C231, C232 are noticed by the scripts' own checks, and list prints of results that no check tests (C222-C233 scripts).

## What this result does NOT mean

- not a mutation score of the whole project: 8 sites per file, three operators (binary +/-, unary minus removal, integer constant +1)
- a SURVIVED mutant is not a bug: it may be equivalent; each survivor was triaged by reading
- a CRASHED mutant is a loud failure, not a check that noticed

## Kill criterion

None (instrument); the result is a list.

## Status of the evidence

Seed 20261103, k = 8, timeout 240 s. No independent human review.
