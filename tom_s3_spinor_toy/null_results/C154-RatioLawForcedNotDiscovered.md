# C154 — |c(∇)|=(2/3)·μ(∇) "family-wide law" — REJECT (forced, not discovered)

**Date:** 2026-09-04. **Verdict:** REJECT (the family-wide-law framing).
**Underlying single-point coincidence:** still true, still open, unaffected.

## The claim that died

That the numeric coincidence `|c(∇_LC)|/μ(∇_LC)=2/3` (true on both `S⁶`
and `SU(3)/T²` at their respective Levi-Civita connections) is evidence of
a genuine family-wide structural law, `|c(∇)|=(2/3)·μ(∇)` for ALL `∇` in
the admissible connection family — strengthened by testing 3 independent
points on `S⁶` (Levi-Civita, its `J`-rotation, and their sum) and finding
exact agreement at all three.

## Why it died

Two independently-defined quadratic forms, `|c(∇)|²` and `μ(∇)²`, are each
**forced to be conformal** (proportional to `a²+b²` in the family's own
`(a,b)` coordinates) by facts already on record before this round ran:

- `⟨ψ₊,ψ₋⟩ = 0` — visible by direct inspection of their definitions in
  `round59_route_a_independent.py` (two fixed unit-entry vectors), forces
  the cross-term in `μ(∇)²`'s quadratic form to vanish.
- `c_B = i·c_A` — C147b's own already-committed exact result, forces the
  cross-term in `c(∇)²`'s quadratic form to vanish.

Given both forms are conformal, a closed form follows in two lines:
`μ(a,b)=√3·√(a²+b²)`, `|c(a,b)|=(2/√3)·√(a²+b²)`, ratio `=2/3` **at every
point of the family**, verified directly at a random untested point
`(a,b)=(3/7,-2/5)`, not just the 3 originally chosen. Agreement at the
"third, independent" point `∇_LC+∇_LC∘J` therefore carries **zero**
additional information — it was never possible to disagree, once the two
cross-terms were (independently, already) known to vanish.

## Kill Analysis

**Killed:** the "3-point-confirmed, non-tautological family-wide law"
framing. Not the arithmetic (every number is exact and correct) — the
claim that it constitutes NEW evidence beyond the single Levi-Civita-point
ratio.

**NOT killed:**
- `|c(∇_LC)|/μ(∇_LC)=2/3` on `S⁶` itself — true, still unexplained.
- The analogous `SU(3)/T²` value — true, still unexplained, and now known
  to sit on an unnormalised basis (see the separate C153 correction).
- `S⁶`'s exact closed-form `c`/`μ` machinery — correct, reusable.

**Relaxation Map:** none for "the family-wide law" specifically — it was
never a real target once the two forcing facts are accounted for. The only
remaining open question is the ORIGINAL one: why `2/3` at the Levi-Civita
point, on either coset. No relaxation of the family-wide claim is
meaningful; it should not be revived.

## SU(3)/T² — genuinely inconclusive, not a second REJECT

The Frobenius-norm-based test there gave 3 different, mutually
inconsistent ratios (`2√2` on the basis, `2√6` at the sum, `2√6/3` at the
actual Levi-Civita vector) — none matching `2/3`. Recorded as
INCONCLUSIVE: the correct scalarisation for a 3-dimensional (vs `S⁶`'s
1-dimensional) target sector was not identified, and a real,
previously-unflagged gap (C153's `dom_sym`/`tgt_sym` were never
Gram-Schmidt-orthonormalised) means even the numbers tried are on an
unaccounted scale. See
`experiments/20260904-c153-nk-linearity-structural-derivation/decision.md`'s
own appended correction.

## The pattern (third occurrence today, second one this specific round)

Same day, same mechanism, twice: C153's "per-plane multiplicative law"
(forced by Schur's lemma + a classical theorem) and this round's
"family-wide ratio law" (forced by two already-registered orthogonality/
ratio facts) both looked like discoveries and both collapsed to already-
known structure under a context-blind skeptic pass. See pearl_registry for
the tracked meta-pattern.
