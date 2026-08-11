# OB11(ii) — ground-truth control refutes C68's own "directionality error" hypothesis

**Experiment id:** `20260811-ob11ii-ground-truth-refutes-directionality-hypothesis`
**Date:** 2026-08-11 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C68 (complexification bridge, gap localized to correspondence pipeline,
"most likely a directionality error in the Cartan-transport formula" — that hypothesis is
what this round tests and refutes)

---

## Why this round exists

C68 localized the failure to find the round59↔G102 intertwiner to the cross-construction
correspondence pipeline and hypothesized a directionality error in the `Phi_H1`/`Phi_H2`
Cartan-transport formula (reused from round128). The obvious next test, run here: **ground-truth
the entire pipeline on a case where the answer is known** — match G102's `su(3)` against
*itself*, via two independent random-seed CSA extractions. If the pipeline (including the
transport formula) is broken, the self-match should fail the same way; if the self-match
succeeds, the pipeline is correct and C68's hypothesis is wrong.

## The claim under test

> **C69 (working).** C68's "likely directionality error" hypothesis is refuted: the identical
> pipeline, applied to G102-vs-G102 (two independent extractions of the same representation),
> reaches the predicted `Hom` dimension 6 — so the pipeline is correct, and the round59↔G102
> obstruction is a genuine property of that specific pair, not an implementation bug. Additional
> structure of the obstruction is characterized (see predictions).

## Predictions, recorded before running (P1 was run first; P2-P4 sequenced on its outcome)

| # | Prediction |
|---|---|
| **P1 (ground truth)** | G102-vs-G102 self-match through the full pipeline (independent seeds, root matching, mu-fit, Hom computation) reaches `hom_dim=6` for at least one candidate — validating the pipeline including the Cartan transport |
| **P2 (structure of the 4)** | the 4-dim cross-construction Hom space is **exactly the singlet↔singlet block** (both sides have 2 singlets; `2×2=4`), i.e. every Hom element annihilates the non-singlet (`3⊕3̄`) sector — the obstruction lives entirely in the 3-dim irreps |
| **P3 (chirality swap ruled out)** | conjugating either side's representation wholesale (`ρ→ρ̄`, swapping `3↔3̄`) does **not** raise the direct Hom dimension above 4 — the obstruction is not a simple chirality mismatch |
| **P4 (missing-relations hypothesis, the last cheap candidate)** | augmenting the mu-fit with the `[E_α,E_{−α}]→Cartan` relations (absent from round128's original fit, automatically consistent in any self-match but not guaranteed across constructions) either (a) resolves the obstruction (some candidate becomes fully consistent, `hom_dim=6`), or (b) reveals genuine inconsistency (nonzero fit residual across all candidates and many restarts) — distinguishing "under-constrained fit" from "genuinely obstructed correspondence" |

## kill_criterion

C69's core (P1) fails if the self-match cannot reach `hom_dim=6` — which would instead confirm
C68's original hypothesis. P2-P4 characterize the obstruction; their outcomes are recorded
whichever way they fall.

## What this cannot show

- Does **not** find the intertwiner — if P4(b) holds, the obstruction survives all cheap tests
  run so far and needs its own dedicated round with a new hypothesis.
- Does **not** contradict C65 (module-type equality; an abstract isomorphism exists) — a failure
  of every *numerically constructed candidate correspondence* to extend is a statement about the
  construction procedure's remaining blind spot, not about abstract existence.
- Nothing about `N_gen=3`'s CONDITIONAL status changes.
