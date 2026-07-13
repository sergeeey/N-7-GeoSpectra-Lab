# Round51-Universality-Scoping Claim — cost re-estimate for the L4 universality question

**Date:** 2026-07-13
**FL tier:** [x] Standard (scoping/feasibility, not a mathematical derivation)
**Question type:** [x] descriptive

---

## Prior Result Gate (MANDATORY — fill BEFORE writing anything below)

1. Exact claim: does Charbonneau-Harland (2016) let the "Universality (L4 →
   CP³/SU(3)/T²)" open problem be closed cheaply (as its Round 48 priority
   score of 1.5 assumed), or does it require an independent derivation?
2. `decision.md` grep: done. `experiments/20260708-dolan-casimir-g2su3/
   decision.md:6444,6478` — Round 48 scored this "clean, reusable
   machinery... direct extension of Charbonneau-Harland 2016" without
   having read the paper.
3. `round*_claim.md` + scripts grep: done, 0 hits — no prior round ever
   attempted this.
4. `null_results/` + `parked/` grep: done, 0 hits.
5. `git log -S`/`-G` pickaxe: done — `CP^3`/`SU(3)/T^2` strings only
   ever appear in the single preprint.tex-introduction commit; no
   generalization work anywhere in history.
6. Primary source re-read: done — full read of
   `Charbonneau_Harland_2016_NK_instantons.pdf` (29 pages, via agent,
   independently spot-checked citations below).
7. **Status:** [x] OPEN → this round.

---

## Estimand

**Population:** the "Universality" open-problem item in preprint.tex
(§7, Mathematical list).
**Intervention:** read the one directly-relevant, already-available
primary source (Charbonneau-Harland 2016) that Round 48 assumed would
let this be closed cheaply.
**Comparator:** Round 48's own cost/value scoring (priority 1.5, "clean,
reusable machinery... doesn't touch the paper's core claims").
**Endpoint:** whether the paper's results are directly reusable for the
L4 generalization question, or whether an independent derivation is
still required.
**Summary measure:** qualitative (transferable / not transferable /
partially transferable), plus a corrected cost estimate.
**MCID:** N/A — descriptive scoping question, not a numeric claim.

---

## Claim

Charbonneau-Harland 2016 studies a structurally DIFFERENT operator
(instanton-deformation complex on the full spinor bundle twisted by the
gauge group's own adjoint bundle) from this project's L4 mechanism
(chirally-projected twisted Dirac operator D_{S^6}⊗S^- twisted by
T^{1,0}S^6⊕1), and its results are therefore NOT directly reusable as
kernel/index data for the universality question — Round 48's cost
estimate for this item was too low.

---

## Kill criterion (MANDATORY — fill BEFORE running)

| Kill condition | Threshold |
|---|---|
| Charbonneau-Harland's operator turns out to be literally the same object as D_{S^6}⊗S^-, just described differently | if confirmed, their S⁶ result (deformation space = 0) or CP³/flag results become directly reusable, reversing this claim |
| Their Casimir-difference formula (Lemma 4) applies to my exact representations without adaptation | if confirmed, "reusable machinery" framing survives; if it requires deriving a NEW branching rule for my specific spinor bundle on the new spaces, it does not |

If FAIL (operator turns out to be the same) → kills this scoping
conclusion, re-open the original priority-1.5 framing as accurate.
If PASS (operator is confirmed different) → the corrected, higher cost
estimate stands; re-score the shortlist.

---

## Checks planned

- T1: extract Charbonneau-Harland's exact operator definition (Eq. 13-14
  in their numbering) and compare term-by-term against this project's
  own D_{S^6}⊗S^- / Weitzenböck definition (preprint.tex §L4A/L4B).
- T2: check whether their S⁶ result (deformation space=0, a DIFFERENT
  quantity) is consistent with (not contradicting) this project's own
  dim ker=1 claim, since both concern the same base manifold — a
  cross-consistency spot check, not a reuse of the number itself.
- T3 (adversarial): specifically look for any place the two operators
  might secretly coincide (e.g. if T^{1,0}S^6⊕1 happens to equal the
  adjoint bundle 𝔰𝔲(3) as an SU(3)-representation) that would undercut
  the "different operator" conclusion.

T3 result: NOT coincident — `T^{1,0}S^6` under SU(3) is the standard
rep `(1,0)` (dim 3, per this project's own preprint.tex branching data),
while `𝔰𝔲(3)` (the adjoint, what Charbonneau-Harland twist by) is the
`(1,1)` rep (dim 8) — different SU(3)-representations, confirming the
two operators are not secretly the same object.

---

## What this does NOT mean

1. Does NOT mean the universality question is unanswerable — only that
   it costs more than a literature lookup.
2. Does NOT mean Charbonneau-Harland 2016 is useless — its Casimir
   formulas for 𝔤₂, 𝔰𝔲(3), 𝔰𝔭(2), 𝔲(1)⊕𝔲(1) and its tracelessness-audit
   methodology (which caught a real 2009 error, Xu's incorrect S⁶
   rigidity proof) are directly reusable INGREDIENTS for a future
   independent derivation, just not a shortcut to the answer itself.
3. Does NOT re-derive or challenge this project's own L4A/L4B result on
   S⁶ — untouched.

---

## Fence (do not change without postmortem)

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

See `decision.md`.
