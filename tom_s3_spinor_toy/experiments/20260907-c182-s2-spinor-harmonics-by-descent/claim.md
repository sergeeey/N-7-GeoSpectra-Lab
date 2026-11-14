# C182 — Claim

**Experiment ID:** `20260907-c182-s2-spinor-harmonics-by-descent`
**Parent:** the remaining half of Tom Lawrence's §3.3 request — *"harmonics
of `S²` that form a basis for a two-component spinor"* — deliberately left
until last, because C179's Relaxation Map argued the order he proposed
(`S²` first, then `S³`) should be **inverted**: `S²` is not
parallelizable, and its spinor harmonics are standardly obtained by
descent from `S³ = SU(2)` at fixed `U(1)` weight (the Hopf fibration
`S³ → S²`).

This round tests whether that descent actually delivers, using C180's
already-built `S³` machinery.

## Step -5: Zero-Signal Gate

- **Entity:** the eigenspaces of the `U(1) ⊂ SU(2)_R` generator `X₃^R`
  acting on the harmonic polynomial spaces `H_k` of `S³`, i.e. the
  decomposition of `L²(S³)` by **spin weight**.
- **Falsifiable predicate:** does the spin-weight-`±½` sector of `H_k`
  (which exists only for `k` odd) have dimension exactly `k+1`, equal to
  `2(l+1)` with `l = (k−1)/2` — the standard `S²` Dirac multiplicity? And
  does the spin-weight-`0` sector of `H_k` (`k` even) have dimension
  `k+1 = 2l+1` with `l = k/2` — the standard scalar spherical-harmonic
  count on `S²`?
- **Measurable outcome:** explicit diagonalization of `X₃^R` on `H_k` for
  `k = 0..5`; report the weight spectrum, each weight's multiplicity, and
  the comparison against both standard counts.

## Step -2/-1 (EstimandOps L0)

**Question type: Descriptive.** Do explicitly-constructed eigenspaces have
stated dimensions — not causal.

## Honest scope, BEFORE computing

1. **Both target numbers are textbook.** `dim{scalar harmonics of degree
   l on S²} = 2l+1` and `{S² Dirac eigenvalue ±(l+1), multiplicity
   2(l+1)}` are standard results. This round does NOT derive them; it
   tests whether the **descent construction reproduces them**, which is a
   check on the construction, not a discovery about spheres. Stated up
   front per this project's own "forced not discovered" discipline.
2. **The scalar case is the positive control**, and it is the stronger of
   the two checks, because it is the one where an error in the weight
   normalisation would show up immediately against a number everyone
   knows (`2l+1`).
3. **This round does NOT build the `S²` Dirac operator** and therefore does
   NOT independently produce its eigenvalues `±(l+1)`. It establishes the
   harmonic *spaces* and their multiplicities. Deriving the eigenvalues
   requires the operator, which is a separate construction — named, not
   attempted.
4. C179's no-go must remain visibly respected: the spin-weight-`±½`
   sectors must be **non-invariant** under the `U(1)`, i.e. genuinely not
   functions on `S²`. This is checked, not assumed.

## Kill-criterion table (frozen before running)

| Verdict | Condition |
|---|---|
| `DESCENT-CONFIRMED` | Spin-weight-`0` sectors (`k` even) have dimension `2l+1`, AND spin-weight-`±½` sectors exist exactly for `k` odd with dimension `2(l+1)`, for every `k` tested. |
| `SCALAR-OK-SPINOR-FAILS` | The scalar control passes but the spin-`±½` count does not match `2(l+1)` — the descent does not deliver the spinor multiplicities and the route C179 recommended is wrong. |
| `WEIGHT-NORMALISATION-WRONG` | The weight spectrum is not the expected equally-spaced symmetric ladder (`k+1` distinct values, step 1 in standard normalisation, each of multiplicity `k+1`) — the `U(1)` generator or its normalisation is misidentified and no verdict may be read off. |
| `NOGO-VIOLATED` | A spin-weight-`±½` vector turns out to be `U(1)`-invariant — which would contradict C179 and must be resolved before anything else. |

**Pre-registered expectation:** `DESCENT-CONFIRMED`. Reasoning stated in
advance: `H_k` carries `(k/2, k/2)`, so under the `U(1)` in the right
factor the weights run `−k/2 … +k/2` in unit steps, each with multiplicity
`k+1` from the untouched left index. Half-integer weights therefore occur
exactly for `k` odd, and `weight = ½` needs `k` odd with multiplicity
`k+1 = 2l+2`. **If this fails, the descent route recommended in C179 is
wrong and that recommendation must be withdrawn** — which is the outcome
that would matter.

## AI-Hypothesis Pre-Gates

- **Source Trace:** `H_k` and the vector fields imported verbatim from
  C180 (`importlib`), which is itself skeptic-passed. Target numbers are
  textbook (`2l+1`; `2(l+1)`), used as reference values only.
- **Novelty Check:** the session's repo inventory found **no** explicit
  `S²` spinor harmonics anywhere in the repo, and no spin-weight
  decomposition of `S³` harmonics. New here.

## What this does NOT mean (pre-registered)

1. Does NOT produce the `S²` Dirac eigenvalues — spaces and multiplicities
   only (scope limit 3).
2. Does NOT contradict C179 — the spin-weight-`±½` objects are sections of
   a non-trivial bundle, not functions on `S²`; that is exactly why they
   carry non-zero weight, and it is checked.
3. Does NOT change `N_gen=3`, any open blocker, or any project claim.
4. Does NOT constitute a submission to Tom.
