# Claim: closing four ledger gaps of the correspondence layer (R03, R15, R16, R17)

**Date:** 2026-11-23
**FL tier:** Micro-plus (no new mathematics; existing scripts re-run from a self-contained copy, results recorded as ledger rows)
**Question type:** [x] descriptive (what is established, with what evidence, and what is not)

## What is claimed

Four results of the private correspondence layer had no complete ledger entry (`ledger.gap`). This folder records them:

| ledger row | layer row | content |
|---|---|---|
| C244 | R16 | the extra term of the spin-weighted ladder is a derivative along the third Euler angle; closure rule agrees with the exploratory rule of C221 |
| C245 | R03 | the literal m = -1 reading gives the l = 1 lowest-weight state; the scalar ladder at m = +-1/2 does not close |
| C246 | R15 | the S^3 to S^2 reduction identity (numerical) and its relation to a published reduction (hand algebra, partly unread source) |
| C247 | R17 | open question: how a recorded statement about fermion waveforms reads against C222 and C224; no computation |

## What this does NOT mean

- It adds no new mathematics: the ten scripts were written earlier; they were copied here with style-only fixes (ruff; logs byte-identical before and after) and re-run (10 of 10 exit 0).
- C221 is not edited. C244 and C245 supplement it.
- It does not say which operator or which space the correspondent uses.
- It does not establish novelty of anything.

## Kill criterion

Any re-run script exiting non-zero, a negative control that stops failing, or a ledger statement that claims more than the logs in `logs/` show.

## Status of the evidence

Same author and same model family wrote and re-ran all of it; the only independent look is the context-blind verifier review of 2026-11-02 (verdict WEAKENED for R15 and R16). No human review.
