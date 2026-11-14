# C156 — Decision

**Date:** 2026-09-05. **Tier:** FL Full. **L0:** descriptive.
**Verdict: the pre-registered rule is REJECTED out-of-sample. Two corrections to
my own earlier work stand. The replacement hypothesis is reported as
near-vacuous unless the independent null-model test says otherwise.**

## What was pre-registered, and what happened

| # | pre-registered prediction | outcome |
|---|---|---|
| Q0 | `rank(M) = 2 * dim R` on a second root system | **FALSIFIED.** `G_2/T^2` gave `rank(M) = 4`; the rule required 8 |
| Q4 | the general code reproduces C155's `A_2` numbers | **PASSED** — family dim 6, `rank(M) = 2`, `dim_C Sigma^T = 2` |
| S1–S4 | (replacement HYPOTHESIS S, registered in AMENDMENT 2 before testing) | **all passed**: `A_2` rank 2, `A_2` other orientation rank 2, `G_2` rank 4 for all four spinors, `A_2 x A_2` rank 4 as predicted |

The `A_2` agreement that motivated Q0 was, exactly as the pre-registration
warned, a 1-in-4 sign coincidence. It is not rescued anywhere in this round.

## Why Q0 failed — a structural fact worth keeping

`A_2` and `A_2 x A_2` have `dim V = 2N` (every equivariant direction is
plane-local: 6 = 2*3, 12 = 2*6). **`G_2` has `dim V = 30` while `2N = 12`.**
`G_2`'s root system has many additive triples `beta_i + beta_j = beta_k`, and
each contributes equivariant directions that are NOT plane-local. Q0's
arithmetic silently assumed the `2N` structure, which `G_2` does not have. The
prediction was falsified by the data before this explanation was found, not
after — the explanation is a post-hoc diagnosis of a dead prediction, not a
rescue of it.

## The rule was a MIRAGE — full diagnosis, stronger than the empirical failure

The falsification above is empirical. The diagnosis is sharper: **the rule was
never about roots at all.**

| | `2 * dim R` (what the rule predicts) | `dim_C Sigma^T` (the FORCED target dimension) |
|---|---|---|
| `A_2` | `2*(3-2) = 2` | **2** — coincide |
| `A_2 x A_2` | `2*(6-4) = 4` | **4** — coincide again |
| `G_2` | `2*(6-2) = 8` | **4** — diverge |

On `A_2` (and, by accident, on `A_2 x A_2`) the root-theoretic number happens to
equal the dimension of the space the image is FORCED to live in. That is why the
rule looked predictive: it was the forced chirality/invariance dimension wearing
root-system clothing.

On `G_2` the two part company, and the rule predicts `rank = 8` **into a target
whose real dimension is 4**. So the rule does not merely fail against the data —
it contradicts the containment that is forced independently of any measurement.
**It is excluded by dimension counting alone, without running anything.**

Two consequences worth stating plainly:

1. Any dimensionally-consistent repair is also dead. Restricting to the
   plane-local part of the family (which the pre-registration explicitly
   licensed as the contingency if `dim V != 2N`) cannot help: the target is
   still 4-dimensional on `G_2`, so no restriction can produce a rank of 8.
2. The `A_2` match that started this whole line — `mu`'s functional `(1,-1,1)`
   equalling the positive-root relation — remains a true and orientation-
   canonical statement about `A_2`, but it now has no generalisation behind it.

## Two corrections to my own earlier rounds

1. **C155 Step 5's falsification was UNSOUND.** It compared `mu`'s per-plane
   functional `(1,-1,1)` against the relation among the *oriented weights*
   `(1,1,1)`. Oriented weights flip sign with an arbitrary choice of plane
   orientation; the canonical object is the relation among the *positive roots*,
   which is `(1,-1,1)` and agrees exactly. **C155's Step 5 verdict must be read
   as withdrawn.** It does not change C155's headline (that rested on the rank
   mismatch 6 vs 2, untouched here), and it did not save the rule either — `G_2`
   killed that independently and more decisively.
2. **`Sp(2)/T^2` cannot host this construction at all**: it has no invariant
   spinors. Re-derived from scratch (`+-1`-in-`R` criterion), cross-checked by
   enumerating all 16 sign vectors, and consistent with the published
   Artacho–Semmelmann combinatorial characterisation. Same for `A_3` and `B_3`.
   This is useful negative knowledge: it rules out three otherwise-obvious test
   spaces before anyone spends a build on them.

## HYPOTHESIS S — and the reason to distrust it

> `image(M)` is exactly the opposite-chirality part of `Sigma^T`.

Confirmed on 3 root systems, 10 invariant spinors, both chiralities, two
orientations of `A_2`, and families of dimension 6/6/30/12. But its content
decomposes as:

* **containment: FORCED.** `spin_lift(Lambda) in Cl^even` preserves chirality,
  `e_k` is odd, so `M(Lambda)` has chirality opposite to `psi`; equivariance puts
  it in `Sigma^T`. Nothing is being discovered here.
* **surjectivity: probably GENERIC.** `dim V` is 6, 30, 12 against a target of
  real dimension 2, 4, 4. A random linear map with those dimensions is
  surjective with probability 1. On every flag manifold `dim V` will exceed the
  target for the same combinatorial reason, so this is not a lucky feature of
  the tested cases.

**Honest reading: forced part + generic part, with little or nothing left over.**
Stated here rather than left for a reader to notice.

## Skeptic (FL Step 8a) — Response Matrix. HYPOTHESIS S is VACUOUS.

The reviewer was context-blind and, as in the previous round, reported honestly
that it had **no code execution**. Under `audit-verification-gate.md` its
verdicts are `[HYPOTHESIS]` here until re-run, so both decisive points were
re-tested with a tool (`c156_step5_skeptic_response.py`).

| # | skeptic point | my tool verification | response |
|---|---|---|---|
| A1 | the weight-only construction really is the full `T`-equivariant family; traced the `A_2` torus generators by hand against C153's independently-built `T2_M` and got an exact match | consistent with the `A_2` regression gate already in the code | **Accepted** |
| **A2** | **"the killer":** `dim V` (6, 30, 12) exceeds the target (2, 4, 4) by ≥3x, so surjectivity is what ANY map of these shapes does; no null model was ever run | **RAN THE NULL MODEL: random integer maps of the same shapes are surjective 200/200, 200/200, 200/200 — 100%** | **CONFIRMED. HYPOTHESIS S is VACUOUS** and is withdrawn as a claim |
| **A4** | a structural fact this round did NOT have: the even chirality split of `Sigma^T` is FORCED only when `N` is ODD, because `eps -> -eps` preserves the relation and flips the `+`-count `k -> N-k`, changing parity iff `N` is odd | **VERIFIED by enumeration**: `A_2` (`N=3`) — `eps` and `-eps` have different parity, split forced; `G_2` and `A_2 x A_2` (`N=6`) — same parity, so the observed `2+2` is NOT explained by the pairing | **Accepted; a real gap in my reasoning, now recorded** |
| A3 | `A_4` (`SU(5)/T^4`) DOES admit invariant spinors (the `e_1` coefficient is a sum of four `+-1`s, which can vanish), so it is a genuine untested candidate — but every flag manifold will have `dim V >> dim Sigma^T`, so more confirmations of this shape would not tighten anything | argument accepted; not run (`dim Sigma = 1024`) | **Accepted** — and moot, since A2 already empties the claim |
| A5 | no hidden convention dependence at the level of rank | matches the S4 orientation test already run (rank 2 in both orientations) | Accepted |
| A6 | the `2 * dim R` rule is genuinely dead — the round's cleanest finding | independently re-derived here as a *dimensional impossibility*, not just an empirical failure | Accepted, strengthened |

**No concern dismissed. The round's central replacement hypothesis is withdrawn
as vacuous on the strength of a test the skeptic demanded and I ran.**

### Final status of HYPOTHESIS S

**WITHDRAWN.** Decomposed honestly: containment in the opposite-chirality part
of `Sigma^T` is **forced**; surjectivity onto it is **generic** (100% in the null
model). Forced + generic = no content. The four passing tests (S1–S4), including
the pre-registered `A_2 x A_2` prediction, are all consistent with a completely
trivial explanation, which is exactly what the pre-registration said would make
them worthless.

### What the skeptic contributed that I did not have

The `N`-parity argument for the chirality split (A4). My framing
`rank(M) = (1/2) dim_R Sigma^T` silently assumed an even split; that assumption
is only forced for `N` odd, and both `N`-even test cases were coincidences.
Third consecutive round in which a context-blind reviewer *without* code
execution located the load-bearing defect.

## What this round produced that is worth keeping regardless

1. **Reusable machinery** (`c156_general.py`): builds the isotropy module,
   Clifford algebra, invariant spinors, equivariant connection family and the
   Dirac response for **any** full flag manifold from the positive-root weights
   alone — no structure constants needed. Validated by an `A_2` regression
   against C153/C155's independently-built machinery (family dim 6, rank 2).
   Solves the family nullspace by connected components so it scales to `G_2`
   (792 unknowns) and would reach `C_3` (2754).
2. Three flag manifolds shown to have no invariant spinors, with the criterion.
3. Two corrections to my own prior rounds.
4. One pre-registered hypothesis honestly killed out-of-sample.

## What this does NOT establish

1. No discovery is claimed. The pre-registered rule died; the replacement is
   probably vacuous.
2. Nothing about `N_gen = 3`, `lambda` (still `FREE_COUPLING_PARAMETER`), or any
   physical claim.
3. Novelty of HYPOTHESIS S is NOT established — see `novelty_check.md`; the area
   is classical and the search was shallow.
4. `A_2 x A_2` is a product space and therefore a weak third data point. `C_3`
   (`dim Sigma = 512`) is the honest untried test.

## Reproduce

```
python c156_step1_recheck_step5.py    # C155 Step 5 was unsound
python c156_general.py                # A_2 regression gate
python c156_step2_g2_test.py          # the pre-registered rule DIES on G_2
python c156_step3_chirality.py        # forced vs content decomposition
python c156_step4_hypothesis_S.py     # S1-S4
```
