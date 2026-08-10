# C36 fix — `J_F² = +1` restored across 11 documents, manuscript included

**Date:** 2026-08-10
**Verdict:** `PROPAGATION_FIXED__AND_A_SECOND_OVERCLAIM_FOUND_IN_THE_SAME_SENTENCES`
**Fixes:** C36 (found while grounding C35)

## What was wrong

`J_F² = −1` appeared in 11 documents including `preprint.tex`. The correct
value is **`+1`**, and the project's own code has always said so.

## The evidence is entirely one-sided [VERIFIED-sympy]

| location | what it says |
|---|---|
| `g18_ncg.py:156` | `assert J_F**2 == sp.eye(32)` |
| `g18_ncg.py:17` (docstring) | `J_F² = I` |
| `tests/test_g18_ncg.py:60` | test named **`test_J_F_squares_to_identity`** |
| `round61_route_a_commutant.py:120` | asserts it, and **depends** on it: `J_F⁻¹ = J_F` |
| `round61_route_b_blocks.py:401` | asserts it |
| direct load of G18's `J_F` | 32×32, all entries real, `J_F conj(J_F) = +I₃₂` |

`J_F` is 16 real transpositions, so for antilinear `J = J_F∘conj` the antilinear
square equals the linear one. **Nothing anywhere computes or depends on `−1`.**

**The typo never touched a computation.** This was a reporting error that
propagated for ~7 weeks through prose only.

**Downstream semantic audit [VERIFIED-grep + VERIFIED-read, added 2026-08-10
after external review].** The first version of this document said "every derived
result stands unchanged" on the strength of a grep for the *sign*. An external
review correctly objected that this is weaker than the claim: a file could
depend on `J_F`'s reality *semantically* without containing the string `−1`. So
the audit was actually run — every code site touching `J_F`, classified by what
it uses:

| site | what it uses | sensitive to the square? |
|---|---|---|
| `g20_yukawa_intertwiner.py` | `[D_F,J_F]=0` | no |
| `g22_first_order.py` | **`J_F²=I`** (gate F5) + `R_k = J_F G_k J_F` | **requires +1** |
| `g23_chirality.py` | `{J_F,γ_F}=0` | no |
| `g25_yukawa_texture.py` | `[D_F,J_F]=0` | no |
| `round61_route_a/_b` | `J_F⁻¹ = J_F` | **requires +1** |
| `tests/` (4 files) | assertions | **requires +1** |

Plus: **no code anywhere branches on a KO-dimension assumption** (grep for
conditional/assert on `KO` → empty), which was the review's specific
hypothetical.

**The audit strengthens the conclusion rather than weakening it.** `g22` — the
first-order-condition experiment — does not merely tolerate `+1`, it *depends*
on it: `R_k = J_F G_k J_F` is only the right-action formula when `J_F⁻¹ = J_F`.
Had `−1` been true, a load-bearing downstream experiment would have been
silently wrong. **Zero sites require `−1`.**

Stated at the strength the evidence supports: *no computational downstream
dependence on `−1` exists, and two independent downstream constructions require
`+1`.*

## The second overclaim, in the same sentences

Fixing the sign exposed a distinct problem the sign was sitting next to.
`preprint.tex` read:

> `J_F²=−1, {J_F,γ_F}=0, [D_F,J_F]=0` (KO-dim 6 relations verified).

That parenthetical is ambiguous between *"the relations are verified"* (true)
and *"KO-dimension 6 is verified"* (**not established here**). This repo has no
KO-dimension table, no CCM source file, and no internal derivation mapping a
sign triple to a KO-dimension number — and `G26`'s own comparison table already
marks CCM's KO-6 as `[DOCS] postulated`. What G18 verifies is three relations.
The *number* is inherited.

Corrected in `preprint.tex`, `preprint_draft.md`, and `g26/claim.md`, whose
"Same KO-dim independently" note was the strongest form of the overclaim. This
follows `docs/clifford_convention_registry.md` rule 4 (store the tuple, never a
bare "KO-dim N") — written six days ago by the convention audit, for this exact
failure mode.

## Files changed (11)

**Live documents — value corrected in place with an inline marker:**
`preprint.tex:354` · `preprint_draft.md:172` · `docs/gates_tracker.md:38` ·
`RESEARCH_STATUS_REPORT.md:118` · `SPIN13_TO_SPIN4_DECOMPOSITION.md:73` ·
`OPEN_BLOCKERS.md` (×2)

**Historical experiment records — corrected with a visible provenance note,
per this repo's retract-in-place convention:**
`g18/decision.md:9` · `g26/claim.md` (×2) · `ob10/claim.md` (×3) ·
`ob10/decision.md:60`

**Two OB10 sentences marked VOID rather than corrected.** OB10 justified its
pseudo-real verdict as "matching the finite algebra's own pseudo-real
`J_F²=−1`". That fails twice over: `J_F²` is `+1`, **and** C32 already showed
OB10's own verdict was a Clifford-convention artifact. A void corroboration is
not repaired by fixing one of its two broken halves, so both sentences keep
their original text with an explicit VOID marker.

## Verification

- No unmarked `J_F² = −1` remains: every surviving occurrence is inside a
  correction annotation quoting the old value as wrong.
- `pdflatex -halt-on-error preprint.tex` → **exit 0**, `grep -cE "^!" preprint.log` → **0**.
- `preprint.pdf` **rebuilt 2026-08-10** (3 × `pdflatex`, exit 0, 0 errors,
  0 unresolved citations, 30 pages — same count as before). Build intermediates
  removed. Previous build preserved as `preprint_PREV_20260718.pdf.bak`.
  **Correction to this document's first draft:** it said the July-18 PDF was
  "already stale by 3 weeks". Only its *timestamp* was old — a `pdftotext` diff
  of old vs new shows the sole content differences are this fix and the page
  reflow it causes (§2.5 moves 7→8, TOC updated). The old build was
  content-current with the `.tex`; it simply predated this change.
- Suite: 2512 passed, 4 skipped, 0 failed.

## What this does NOT do

1. **Does not rebuild `preprint.pdf`.** It was already stale by three weeks;
   regenerating a distributable artifact is a separate, deliberate act.
2. **Does not establish which KO-dimension the tuple `(+1, [D,J]=0, {J,γ}=0)`
   corresponds to.** It removes the claim that this project derived it. Settling
   the number needs a cited external table — deliberately not done from memory.
3. **Does not revisit whether KO-dim 6 is the right target** for this
   construction. Unchanged question, unchanged basis (CCM).
4. **Changes no result.** The sign was never used in a computation.

## Check

```
grep -rn "J_F²=−1\|J_F²=-1" --include="*.md" --include="*.tex" .
```
Every hit should be inside a correction/VOID annotation, never a bare assertion.
