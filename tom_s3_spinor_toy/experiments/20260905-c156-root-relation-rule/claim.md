# C156 — the equivariant Dirac response of an invariant spinor is maximal

> ## WITHDRAWN (2026-09-05, same day, after the skeptic pass + a null model I ran)
> **HYPOTHESIS S below is VACUOUS.** Containment in the opposite-chirality part
> of `Sigma^T` is FORCED; surjectivity onto it is GENERIC — random integer maps
> of the same shapes (2x6, 4x30, 4x12) are surjective **200/200 = 100%** in all
> three cases. Forced + generic = no content. All four passing tests, including
> the pre-registered `A_2 x A_2` prediction, are consistent with that trivial
> explanation. A second defect: the framing `rank = (1/2) dim_R Sigma^T` assumes
> an even chirality split, which is forced only for `N` ODD (`A_2`); on both
> `N`-even cases (`G_2`, `A_2 x A_2`) it was a coincidence — verified by
> enumerating sign patterns. See `decision.md` for the full response matrix.
> The text below is kept unedited as the record of what was claimed.

**Question type (EstimandOps L0): DESCRIPTIVE.** Tier: FL Full.

## The claim

Let `G/T` be a full flag manifold, `m` its isotropy module (one 2-plane per
positive root), `Sigma` the spinor module, `Sigma^T` the `T`-invariant spinors,
and `V` the space of `T`-equivariant connections `Lambda : m -> so(m)`. For an
invariant spinor `psi` of definite chirality define

    M : V -> Sigma,     M(Lambda) = sum_k e_k . spin_lift(Lambda_k) psi

> **HYPOTHESIS S.** `image(M)` is exactly the OPPOSITE-chirality part of
> `Sigma^T`. The inclusion is forced; the **surjectivity** is the content.
> Consequently `rank(M) = (1/2) dim_R Sigma^T` and
> `dim ker(M) = dim V - (1/2) dim_R Sigma^T`.

## Status of each link (forced vs content)

| link | status |
|---|---|
| `omega` anticommutes with every `e_a`, so `D_Sigma(v)` is odd | **FORCED** (general Clifford fact; verified in code on 6 and 12 generators) |
| `psi` has definite chirality; `Sigma^T` splits evenly `+k/-k` | **OBSERVED** on every space tested |
| `image(M)` is CONTAINED in the opposite-chirality part of `Sigma^T` | **FORCED** by the two rows above plus equivariance; verified directly |
| `image(M)` EQUALS that part | **THE CONTENT — not forced, tested below** |

## Evidence

All exact (sympy, integer/rational arithmetic), no floating point.

| space | root system | `dim m` | `dim Sigma` | `dim V` | `dim_C Sigma^T` | split | `rank(M)` | surjective |
|---|---|---|---|---|---|---|---|---|
| `SU(3)/T^2` | `A_2` | 6 | 8 | 6 | 2 | 1+1 | 2 | yes, both spinors |
| `SU(3)/T^2`, other orientation | `A_2` | 6 | 8 | 6 | 2 | 1+1 | 2 | yes, both spinors |
| `G_2/T^2` | `G_2` (exceptional, non-simply-laced) | 12 | 64 | **30** | 4 | 2+2 | 4 | yes, all four spinors |
| `(SU(3)xSU(3))/T^4` | `A_2 x A_2` | 12 | 64 | **12** | 4 | 2+2 | 4 | yes, all four spinors |

**10 distinct invariant spinors, both chiralities, 3 distinct root systems,
families of dimension 6, 6, 30 and 12.** The rank tracks `Sigma^T`, not the
family: `G_2` and `A_2 x A_2` have families of very different size (30 vs 12)
and identical rank 4.

`A_2 x A_2` was a **pre-registered out-of-sample prediction** (`rank = 4`),
fixed in `PREREGISTRATION.md` AMENDMENT 2 before the space was built.

## This claim replaced a FALSIFIED one, in the same round

The round began with a different, also pre-registered rule:
`rank(M) = 2 * dim R`, where `R` is the space of linear relations among the
positive roots. On `A_2` it fit (`2 = 2*1`). **`G_2` falsified it: predicted 8,
measured 4.** The `A_2` fit was the 1-in-4 sign coincidence the pre-registration
had explicitly warned it might be. That rule is dead and is not rescued
anywhere in this round.

## Two corrections to earlier rounds, both mine

1. **C155 Step 5's falsification was UNSOUND.** It rejected a root-theoretic
   reading of `mu`'s sign pattern by comparing against the relation among the
   *oriented weights* `(1,1,1)` — an orientation-dependent object. Against the
   canonical *positive-root* relation the two agree exactly (`(1,-1,1)`). The
   correction does not save the rule (see above): `G_2` killed it anyway, on a
   different and stronger test.
2. **`Sp(2)/T^2` has no invariant spinors at all**, so it cannot host this
   construction. An invariant spinor exists iff `R` contains a vector with all
   entries `+-1`; for `C_2` no such vector exists (checked by solving, and by
   enumerating all 16 sign vectors). Same for `A_3` and `B_3`. This reproduces,
   from scratch, the kind of positive-root combinatorics that
   Artacho–Semmelmann (arXiv:2407.08493) use to characterise existence.

## What this does NOT establish

1. **Not a theorem.** Three root systems and ten spinors are evidence, not a
   proof. No derivation of surjectivity was obtained; a plausibility sketch
   (Clifford multiplication `Cl^odd(m) psi = Sigma_opposite` is surjective, and
   `m (x) Lambda^2 m` may cover enough of `Cl^odd` after taking invariants) is
   **not** a proof and is not claimed as one.
2. **Novelty not established.** This is a statement about equivariant Dirac
   operators on flag manifolds — a classical, heavily-studied area. It may well
   be known or be a corollary of something known. See `novelty_check.md`.
3. `A_2 x A_2` is a PRODUCT space, so its confirmation is weaker than a new
   simple group would be. The honest missing test is `C_3` (`dim Sigma = 512`),
   named and not attempted.
4. Nothing about `N_gen = 3`, `lambda` (still `FREE_COUPLING_PARAMETER`), or any
   physical claim.
5. The even chirality split of `Sigma^T` is an OBSERVATION on the tested spaces,
   not something derived; if it fails somewhere, the statement needs restating.

## Bug found and fixed during the round (kept, not hidden)

The first chirality test reported `image(M)` NOT contained in the opposite half —
which the chirality argument FORCES to be true, so the contradiction signalled a
bug in the test, not a finding. Cause: the real span of a complex subspace
spanned by `v` is `span_R{v, i v}`, two real dimensions, but the helper emitted
only one column per complex basis vector. Fixed; all four `H`-checks then passed.
