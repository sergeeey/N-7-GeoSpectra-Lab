---
# C185 — build the S^2 Dirac operator and close the standing caveat

**Date:** 2026-09-08
**FL tier:** [x] Full
**Question type:** [x] descriptive

---

## Why this round exists

`C182`'s own `decision.md` line 116 states the gap in its own words:

> **The `S²` Dirac eigenvalues `±(l+1)` are NOT derived.** Only multiplicities.
> The `S²` Dirac operator was not built.

That sentence has since travelled: it is the first item in the "what I have NOT
established" section of the letter drafted for Tom Lawrence
(`DRAFT_REPLY_TO_TOM_2026-09-08_PART2.md` §7), where it reads as an asymmetry
against `S^3` — there an operator was built and its whole spectrum computed
(`C180`, `C184`), here only multiplicities were obtained by descent.

This round closes it or reports honestly that it could not.

---

## Prior Result Gate

1. `C182` (2026-09-07): Hopf descent, sector dimensions `1,3,5` and `2,4,6`.
   Multiplicities only; operator not built; states so itself.
2. `C184b` (2026-09-08): derived the lowest `S²` spinor doublet
   `chi = (e^{-i phi/2} cos(th/2), e^{+i phi/2} sin(th/2))` by descent, and
   verified its double-valuedness and its bilinears. **Did not apply any
   operator to it.**
3. `C180`/`C184`: the `S^3` operator `D_0 = -i sum_a sigma_a X_a^R` and its
   spectrum — the thing `S^2` currently lacks.
4. `null_results/INDEX.md`, `parked/INDEX.md`: 0 hits for an `S^2` Dirac
   attempt. Nothing was killed here; it was simply never done.
5. **Status:** [x] NEW.

---

## Substrate note, stated up front (Step 2a)

The **conventions** — orientation, frame choice, the sign of the spin
connection, which Pauli matrix plays which role — are substrate, not
hypothesis. They will be fixed by construction and printed, not guessed. The
claim below is deliberately stated in a form that does not depend on any of
them: eigenvalues and multiplicities are convention-independent, an overall
sign of `D` is not (it flips with orientation), so the claim is about `|lambda|`
and about the multiplicity pattern.

**A frame subtlety that must not be waved through:** the doublet `chi` derived
in `C184b` is written in the frame the Hopf descent produces, which is NOT the
coordinate frame `(partial_theta, partial_phi/sin theta)` a coordinate-built
Dirac operator uses. A hand-check performed while designing this round found
`D chi` is *not* proportional to `chi` in the naive pairing — which is a frame
mismatch, not a contradiction, and this round must resolve it explicitly rather
than quietly re-pair things until something matches.

---

## Mechanism Claim Gate (Step 0a)

**The sentence doing justificatory work:** "the spin connection can be obtained
from Cartan's first structure equation `de^a + omega^a_b ^ e^b = 0`, so it is
derived rather than quoted."

**Check before use:** compute `de^a`, solve for `omega`, and verify the equation
holds identically for the solution found — not merely that a standard-looking
expression was written down. If the solution does not satisfy the equation
identically, the sentence FAILS and the operator is quoted, not derived, and must
be labelled that way.

---

## Estimand

**Population:** the Dirac operator on the round unit `S^2` and its spectrum.

**Intervention:** construct `D` from metric → frame → spin connection, then find
its eigenvalues symbolically.

**Comparator:** the standard result `±(n+1)`, `n = 0, 1, 2, …`, with
multiplicity `2(n+1)`; and, independently, `C182`'s own sector dimensions
`2, 4, 6`.

**Endpoint:** the lowest eigenvalues of `D` and their multiplicities.

**MCID:** not applicable — exact identities.

---

## Pre-registered predictions (written BEFORE computing)

| # | prediction | falsified if |
|---|---|---|
| P1 | the frame reproduces the metric: `sum_a e^a (x) e^a = g` | any component differs |
| P2 | the spin connection solving Cartan's equation satisfies it **identically**, and is unique | no solution, or the found one leaves a residual |
| P3 | `D` is formally self-adjoint w.r.t. the round measure `sin(theta) d theta d phi` | the adjoint differs by more than a total derivative |
| P4 | `D^2 = -Laplacian + 1/4 · R` with `R = 2` for the unit sphere (Lichnerowicz) | the constant is not `1/2`, or the second-order part is not the scalar Laplacian |
| P5 | the lowest eigenvalue has `\|lambda\| = 1` with multiplicity 2 | any other magnitude or multiplicity |
| P6 | the next two levels give `\|lambda\| = 2` multiplicity 4, and `\|lambda\| = 3` multiplicity 6 — i.e. `\|lambda\| = n+1`, multiplicity `2(n+1)` | the pattern breaks at either level |
| P7 | those multiplicities `2, 4, 6` equal `C182`'s independently obtained weight-sector dimensions | they differ |

P7 is the one that makes this more than a textbook re-derivation: two routes
that share no machinery — a coordinate-built operator here, a Hopf weight count
there — must land on the same three numbers.

---

## Floor and ceiling (Step 4a)

**FLOOR.** "Some operator has some spectrum" is free — any first-order operator
on a 2-sphere has *a* spectrum. The floor is therefore not zero information but
it is low: a WRONG spin connection also produces a discrete spectrum with
multiplicities. So the criterion is not "we obtained eigenvalues" but "we
obtained `n+1` with multiplicity `2(n+1)`", which a mis-derived connection does
not. **This is tested directly** — the injected-error control below perturbs the
connection coefficient and the spectrum must move off the pattern.

**CEILING.** Exact symbolic eigenvalues; attainable, and `S^2` is small enough
that there is no headroom question.

---

## Kill criteria

| outcome | verdict |
|---|---|
| P1–P7 all hold, injected-error control breaks the pattern | **PROMOTE** — caveat closed, letter §7 first bullet removed |
| P2 fails | the operator is quoted, not derived — say so, keep the caveat, downgrade the letter's wording |
| P5/P6 hold but P7 fails | the two routes disagree; STOP and reconcile before touching the letter — a disagreement between our own two computations is more important than the caveat |
| P5 or P6 fails | either the construction is wrong or the standard result does not apply in this convention; do NOT adjust conventions until it matches — report the mismatch |
| injected-error control does NOT break the pattern | `CRITERION_INVALID` — the check cannot fail, so it certifies nothing |

---

## What this will NOT establish

- Does **NOT** make the `S^2` spinors functions. The obstruction is untouched;
  this is an operator on the same double-valued objects.
- Does **NOT** claim novelty. `±(n+1)` on the round `S^2` is textbook; the point
  is that this project can now produce it from its own construction instead of
  citing it.
- Does **NOT** transport anything into normal coordinates.
- Does **NOT** settle the frame question for `S^3`, which is separate.
