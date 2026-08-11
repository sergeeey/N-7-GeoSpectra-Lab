# C79 -- a genuine non-product S3-S6 coupling term (exploratory, hypothesis-driven)

**Experiment id:** `20260811-c79-nonproduct-s3s6-coupling-attempt`
**Date:** 2026-08-11 · **Track:** B · **L0 (EstimandOps): descriptive
(exploratory -- this round tests the consequences of an EXPLICIT, clearly-
flagged postulate, not a derived physical claim; see "Honesty ledger"
below, matching round67's own convention for exactly this kind of
speculative construction)**
**Predecessors:** C78 (exhaustive so(8) commutant of `D_S6` equals
`su(3)`, closing every symmetry-preserving route within the current
product structure); `L3B_SPIN8_INTERFACE_SPEC.md` §1.5 (its own final kill
criterion: a surviving route needs a construction that is "non-product AND
`G2`-symmetry-breaking... mixing the `S3` frame index with the `S6`
triality index at the level of the Dirac operator itself"); round67
(S3's own Cl(0,3) Clifford generators `Z_i`, torsion-parameter methodology
this round directly extends); round119 (`SO(4)+SO(4)` candidate, `C78`'s
20-dim non-`su(3)` complement)

---

## Why this round is different from C70-C78, and what it honestly is not

Every prior round in this arc (C70-C78) tested whether some symmetry
commutes with round59's `D_S6` -- an operator that, by construction, has
**no dependence on `S3` whatsoever**. Testing symmetries against an
`S3`-blind operator can never satisfy `L3B_SPIN8_INTERFACE_SPEC.md`'s own
final requirement: a construction that genuinely **mixes** the two
factors. C78's exhaustive result (commutant of `D_S6` = `su(3)` exactly)
closes the entire class of "does some symmetry survive" questions for the
CURRENT product operator -- it says nothing about a genuinely different,
non-product operator, because it never builds one.

**This round builds one.** Not the full, rigorous joint operator this
project's own KT-8/round67 investigation never attempted even for the much
simpler torsion-parameter case (round67's own docstring: "This script does
NOT compute the full product operator" -- confirmed by inspection this
round, not assumed) -- that is a multi-round undertaking in its own right.
Instead, this round builds the **minimal, well-defined, honestly-scoped**
version: a coupling term of the standard Kaluza-Klein gauge-coupling shape
(`gamma-matrix (x) Lie-algebra generator`), restricted to `S3`'s `n=0`,
`+`-branch sector (round67's own "constant spinor" sector, where `D_S3`
acts as a known scalar), tested against `D_S6` directly.

## The explicit postulate, stated as a postulate (not a derivation)

**Which piece of `so(8)`'s 20-dim non-`su(3)` complement (C78) plays the
role of "`S3`'s frame/gauge index" is NOT derivable from anything already
established in this project** -- `L3B_SPIN8_INTERFACE_SPEC.md` says so
explicitly about its own, closely related `SO(4)` attempts ("a hypothesis
about how the two known ingredients would need to relate, not a
derivation"), and that remains true here. This round makes ONE specific,
minimal, structurally-motivated choice, stated plainly so a reader can
judge it on its own terms rather than mistake it for a forced conclusion:

> Take round119's own `so(4)_1` (6 of the 12 `SO(4)+SO(4)` generators,
> already tested in C77), split it via the STANDARD `so(4)=su(2)+su(2)`
> self-dual/anti-self-dual decomposition (`e01+-e23, e02-+e13, e03+-e12`
> on `Lambda^2(R^4)`), and use one resulting `su(2)` triple (verified by
> direct commutator computation to genuinely close as `su(2)`, not
> assumed) as the coupling generators, paired with round67's own `Z_i`
> (`Cl(0,3)`, already cross-verified `Clifford-sign-compatible` with
> round59's generators in C74).

This choice is motivated by using ALREADY-ESTABLISHED, ALREADY-TESTED
objects (round119's `so(4)_1`, round67's `Z_i`) rather than inventing new
ones, and by the standard, textbook `so(4)=su(2)+su(2)` structure (not a
project-specific invention) -- but it is still a choice among several that
could have been made, and is reported as such.

## The claim under test

> **C79 (working, exploratory).** The coupling term
> `T = eps * sum_i Z_i (x) Leibniz(g_i)` (`g_i` the chosen `su(2)` triple,
> transported to `Sigma` via `U_v`) is Hermitian by construction (`Z_i`,
> `Leibniz(g_i)` both anti-Hermitian, so their tensor product is
> Hermitian) and well-defined. `D_joint(eps) = (3/2)*I_128 + I_2 (x) D_S6
> + T(eps)`, restricted to `S3`'s `n=0` `+`-branch sector (2-dim) tensored
> with `Sigma (x) Sigma` (64-dim, 128-dim total), is diagonalized across a
> sweep of `eps`. **Prediction:** at `eps=0`, `ker(D_joint)` is empty
> (since `D_S6` is not independently known to have `-3/2` as an
> eigenvalue) -- turning on `eps` either (a) never produces a zero
> eigenvalue in the swept range, consistent with the pattern of every
> prior route in this project failing to produce a genuine escape, or (b)
> produces one or more crossings, which would be a genuinely new,
> significant finding requiring careful, skeptical follow-up before being
> trusted (per this project's own skeptic-triggers.md: an unexpectedly
> positive result after 8 rounds of consistent negative results is
> exactly the shape of finding that needs independent verification before
> being believed).

## Predictions, recorded before running

| # | Prediction | Outcome |
|---|---|---|
| **P1 (su(2) closure sanity)** | The self-dual (or anti-self-dual) triple from `so(4)_1` closes as a genuine `su(2)` algebra (commutators land back in the 3-dim span, structure constants matching `su(2)` up to normalization) | pending |
| **P2 (Hermiticity)** | `D_joint(eps)` is exactly Hermitian for every real `eps` tested | pending |
| **P3 (eps=0 sanity)** | `ker(D_joint, eps=0)` is empty (`D_S6` does not have `-3/2` as an exact eigenvalue) -- checked directly, not assumed | pending |
| **P4 (sweep for zero modes)** | Sweeping `eps` over a reasonable range (`[-2, 2]`, matching round67's own original torsion-parameter sweep range) finds ZERO crossings, consistent with every prior route in this project closing | pending |

## kill_criterion

P1 fails if the claimed `su(2)` triple does not actually close -- would
mean the self-dual/anti-self-dual construction was implemented
incorrectly, invalidating everything downstream; must stop and fix before
proceeding. P2 fails if `D_joint` is not Hermitian for any tested `eps` --
would indicate a sign/convention error in the anti-Hermiticity assumption
for `Z_i` or `Leibniz(g_i)`, also blocking. P3's outcome is recorded
either way (a nonempty kernel at `eps=0` would itself be a separate,
interesting fact about `D_S6`'s spectrum, orthogonal to this round's main
question). **P4 is the actual test**, and its outcome must be reported
exactly as found: a negative result (no crossings) is a genuine, informative
data point extending this project's already-long list of closed routes
under one MORE specific, honestly-labeled postulate -- not a failure of
this round. A positive result (a crossing found) must NOT be presented as
a resolved mechanism without the immediate skeptical follow-up named
above; per this project's own submission-gate discipline, an unexpectedly
positive result after this many consecutive negatives is the textbook
shape of a false positive and must be treated with extra scrutiny, not
excitement.

## What this cannot show, stated plainly

- Does **not** build the full, rigorous `S3xS6` joint Dirac operator (the
  complete Peter-Weyl tower on the `S3` side, both chirality branches) --
  restricted to the `n=0`, `+`-branch sector only, an explicitly narrower
  proxy question.
- Does **not** derive, from first principles, which piece of `so(8)`'s
  complement should carry "`S3`'s gauge index" -- an explicit, stated
  postulate, not a derivation, exactly as `L3B_SPIN8_INTERFACE_SPEC.md`
  itself required any candidate in this class to be honest about.
- Does **not**, even if P4 finds a crossing, establish that the resulting
  zero mode is consistent with this project's other already-established
  index-theorem results (chirality, `su(3)`-invariance of the physical
  sector) -- a genuinely new zero mode would need its OWN full battery of
  checks (chirality, negative controls) before being trusted, not
  attempted in this round.
- Does **not** solicit or reference any unpublished content from Tom
  Lawrence's Part 5 -- every object used is either already established in
  this project's own prior work or a standard, textbook Lie-theory
  construction (`so(4)=su(2)+su(2)`).
- Does **not** change `N_gen=3`'s CONDITIONAL status regardless of outcome
  within this round alone -- a genuinely new finding here would need
  independent verification and its own dedicated follow-up before feeding
  back into the headline claim.
