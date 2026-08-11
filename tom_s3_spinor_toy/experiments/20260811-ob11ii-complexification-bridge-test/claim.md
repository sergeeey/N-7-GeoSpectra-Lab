# OB11(ii), hard half — the complexification bridge test

**Experiment id:** `20260811-ob11ii-complexification-bridge-test`
**Date:** 2026-08-11 · **Track:** B · **L0 (EstimandOps): descriptive**
**Predecessors:** C65 (module-type match, round59 Σ ≅ G102 channels as `su(3)`-modules),
`20260810-ob11ii-round59-g102-explicit-isomorphism` (BLOCKED-SUBSTRATE: round128's real-coefficient
Cartan-Weyl matching doesn't transfer across a real/complex reality-type boundary)

---

## Why this, why now

External review of the prior BLOCKED-SUBSTRATE finding correctly identified the sharpest next
move: drop the assumption that the intertwiner (or the Cartan-subalgebra coefficients used to
find it) must be **real**. C65 already proved round59's `Σ` and G102's `channel_v` are the same
abstract `su(3)`-module (identical Casimir, `-4/3`, both `1⊕1⊕3⊕3̄`) — module-type equality
guarantees a **complex** intertwiner exists; the earlier attempt failed only because it searched
for one under an unnecessary reality constraint inherited from round128's original (same-reality-
type) use case. This round drops that constraint entirely and asks the question in its native,
unconstrained form.

## The claim under test

> **C68 (working).** There exists `U ∈ GL(8,ℂ)` such that `U · ρ_r59(X_a) · U⁻¹ = ρ_g102(X_a)`
> for all 8 `su(3)` generators `X_a`, either (a) under the direct, given generator ordering (the
> cheapest possible test — no root-matching needed at all), or (b) failing that, under **some**
> reordering/recombination consistent with a genuine Lie-algebra automorphism of `su(3)` — found
> via a complex-coefficient version of the Cartan-Weyl matching technique, i.e. round128's
> `extract_csa_and_roots` with its real-coefficient assertion dropped rather than enforced.

**Falsifier, fixed in advance:** if no such `U` is found under **any** of the (up to 12)
`Aut(su(3))`-related generator correspondences, despite C65's module-type guarantee that an
abstract isomorphism exists, that indicates a genuine bug in the search procedure (the existence
of *some* isomorphism is not actually in doubt — only whether this specific numerical search finds
it).

## Predictions, recorded before running

| # | Prediction |
|---|---|
| **P1 (cheapest, direct ordering)** | testing `U·ρ_r59(X_a)·U⁻¹=ρ_g102(X_a)` under the literal given ordering (`a=1..8`, no permutation) most likely **fails** — round59's `ADNU` ordering and G102's `stabilizer_basis`-derived ordering were built by unrelated procedures with no reason to coincide index-for-index |
| **P2 (diagnosis of the earlier failure)** | dropping round128's real-coefficient assertion and allowing complex CSA coefficients resolves the earlier crash — a genuine complex 2-dim Cartan subalgebra is found for round59's generators, with `H1_r59`, `H2_r59` as complex linear combinations of the original 8 generators |
| **P3 (the deliverable)** | among the resulting candidate generator correspondences (matched via complex root-hexagon matching, analogous to round128's own 12-candidate search), at least one yields a nonzero, non-degenerate complex intertwiner `U` with small isomorphism residual |

## What a positive result would and would not unlock

If `U` is found: round59's real Nomizu-connection Clifford multiplication can be transported
through `U` into G102's triality-channel basis, making the actual mixing-term / Clifford-
compatibility test (the genuine OB11(ii) hard-half question) finally buildable — matching this
project's own next step, and the external review's own point B. It would **not** by itself
determine `X_ij=0` or `≠0` — that is a separate, subsequent test, not attempted here.

If no `U` is found despite exhausting the `Aut(su(3))`-related search: per the falsifier above,
this is evidence of a procedural gap in the search (C65's guarantee stands independently of
whether *this* numerical method finds the isomorphism), to be diagnosed rather than reported as
a mathematical surprise.

## What this cannot show

- Does **not** itself build the mixing-term operator or test Clifford-compatibility — that is
  the next round after this one succeeds.
- Does **not** resolve OB11(ii) even in the best case — localizes it one step further, per the
  external review's own correct framing ("bridge confirmed, explicit alignment open" →, if this
  succeeds, "alignment found, transported operator not yet tested").
- Nothing about `N_gen=3`'s CONDITIONAL status changes regardless of outcome.

## kill_criterion

Promotes to `EXPLICIT_ISOMORPHISM_FOUND` if P3 passes (any valid `U` found, any ordering).
Falls back to a diagnosed, re-scoped BLOCKED verdict only if the search is exhausted (all 12
candidate correspondences tried) with no valid `U` — recorded as a procedural gap, not treated
as evidence against C65's own module-type-equality guarantee.
