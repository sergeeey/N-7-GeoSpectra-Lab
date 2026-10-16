# C156 — PRE-REGISTRATION (written BEFORE any C_2 computation)

**Date:** 2026-09-05. **Tier:** FL Full. **L0 (EstimandOps): DESCRIPTIVE.**

## Why this round exists

C155 Step 5 declared FALSIFIED the hypothesis that the `mu`-map's per-plane sign
pattern is root-theoretic. **C156 Step 1 shows that falsification was unsound**:
it compared `mu` against the relation among the *oriented weights*, which flips
when a plane is re-oriented, instead of against the relation among the
*positive roots*, which does not. Against the canonical object the two agree:

    mu functional (measured, A_2)                : (1, -1, 1)
    relation among the ORIENTED weights (C155)   : (1,  1, 1)   <- wrong object
    relation among the POSITIVE roots (C156 St1) : (1, -1, 1)   <- MATCHES

**This is not yet evidence of a rule.** `A_2` has exactly one relation, the
functional is fixed only up to overall sign, so a priori this is a 1-in-4
coincidence. n = 1.

## The rule, stated precisely (so it can fail)

For a full flag manifold `G/T` with positive roots `beta_1, ..., beta_N` and
rank `r`, each positive root spans one 2-plane of the isotropy module `m`. Let

    R := { x in R^N : sum_k x_k beta_k = 0 }        dim R = N - r

be the space of linear relations among the positive roots. Let `M` be the map
`v |-> D_Sigma(v) psi` on the `T`-equivariant connection family, for an
invariant spinor `psi`, and let `P` be its **per-plane coefficient matrix**
(rows = independent components of the image, columns = the `N` planes).

> **RULE:** `rank(P) = dim R = N - r`, and `rowspace(P) = R` exactly.

Equivalently: the kernel of the per-plane map is `R^perp`, and the number of
independent image components equals the number of independent root relations.

`A_2` check (already computed, in-sample): `N=3`, `r=2`, `dim R = 1`;
measured per-plane rank 1, rowspace `span{(1,-1,1)} = R`. **Consistent.**

## AMENDMENT (before any test-space object was built): `C_2` is DISQUALIFIED

While setting up `Sp(2)/T^2` I found it **has no invariant spinors at all**, so
`M` is not even defined there. The reason is worth recording because it connects
the rule to published work:

A spinor weight is `(1/2) sum_k eps_k beta_k` with `eps in {+-1}^N`, so an
invariant (weight-zero) spinor exists **iff `R` contains a vector all of whose
entries are `+-1`**. For `C_2`, a general element of `R` is
`a(1,1,-1,0) + b(0,1,1,-1) = (a, a+b, -a+b, -b)`; all entries `+-1` needs
`a = +-1`, `b = +-1` and `a+b = +-1`, impossible since `a+b in {2,0,-2}`.
Checked independently by enumerating all 16 sign vectors — none gives zero.

This `+-1`-in-`R` criterion is exactly the "combinatorial properties of the set
of positive roots" that Artacho–Semmelmann (arXiv:2407.08493) use to
characterise existence of invariant spinors on maximal flag manifolds. **The
rule under test and the published existence criterion are statements about the
same object `R`** — which is a reason to expect the rule is derivable (see
"will NOT establish", item 3), not a reason to expect it is deep.

`A_3 = SU(4)/T^3` is disqualified the same way: the `e_1` coefficient of
`sum eps_k beta_k` is `eps_12 + eps_13 + eps_14`, a sum of three `+-1`s, which
cannot vanish. Consistent with the published `A_n`-`n`-even condition.

## The out-of-sample test — `G_2/T^2` (replaces `C_2`)

`G_2` has `N = 6` positive roots and rank `r = 2`, so `dim R = 4`. In the
`(alpha_1, alpha_2)` coefficient basis the positive roots are
`(1,0), (0,1), (1,1), (2,1), (3,1), (3,2)`, and `eps = (+,-,+,-,-,+)` solves
`sum eps_k beta_k = 0` (verified by hand and re-verified in code), so invariant
spinors **do** exist. Costs: `dim m = 12`, `dim Sigma = 2^6 = 64`, family
ambient `12 * 66 = 792` unknowns — heavier than `A_2` but tractable.

**PREDICTION for `G_2/T^2`, fixed now: `rank(M) = 2 * dim R = 2 * (6 - 2) = 8`.**
Wrong values available a priori: anything in `0..dim V`. Secondary: the
per-plane relation structure should be governed by `R` (4-dimensional), not by
any smaller or larger space.

## The out-of-sample test as originally written — `Sp(2)/T^2`, the `C_2` flag manifold (DISQUALIFIED, kept for the record)

Chosen because its root system is structurally different from `A_2`:
**non-simply-laced**, `N = 4` positive roots, rank `r = 2`, so `dim R = 2`.
Positive roots `beta_1 = a1`, `beta_2 = a2`, `beta_3 = a1+a2`, `beta_4 = a1+2a2`,
whose pairings with the two simple coroots are

    beta_1 = (2,-2),  beta_2 = (-1,2),  beta_3 = (1,0),  beta_4 = (0,2)

and whose relation space is spanned by `(1,1,-1,0)` and `(0,1,1,-1)`.

### Amendment, made before any `C_2` object was built

Q2/Q3 as worded compare *per-plane coefficient vectors*, which needs the family
directions of different planes to be matched up — and no canonical matching is
guaranteed to exist. So the **primary** test is restated in a matching-free form
that is equivalent on `A_2`:

> **Q0 (primary, matching-free):** `rank(M) = 2 * dim R = 2 (N - r)`.

`A_2` in-sample: `2*(3-2) = 2`, and `rank(M) = 2` was measured in C155 — ✓.
`C_2` prediction: `2*(4-2) = **4**`.

This also makes the test sharper, because `rank(M)` is a single integer with
several a-priori-plausible wrong values (`M` maps an 8-dimensional family into a
16-dimensional spinor space, so `rank` could be anything from 0 to 8; the rule
picks 4). Q1/Q2/Q3 stay as secondary structure checks, reported honestly if the
per-plane matching turns out ill-defined.

**Risk acknowledged in advance:** the prediction `rank(M) = 2(N-r)` implicitly
assumes each plane contributes 2 family directions (true on `A_2`: `dim V = 6 =
2N`). If `dim V != 2N` on `C_2`, that is an unforeseen structural difference; it
will be reported as such and the prediction re-derived in the open, not quietly
adjusted after seeing the rank.

**PREDICTIONS, fixed now:**

| # | prediction | falsified by |
|---|---|---|
| **Q1** | the per-plane rank of `M` on `Sp(2)/T^2` is **exactly 2** | any other rank (1, 3 or 4) |
| **Q2** | its rowspace equals `R = span{(1,1,-1,0), (0,1,1,-1)}` **exactly** | a rowspace of dim 2 that is not `R` |
| **Q3** | equivalently the per-plane kernel is `R^perp = span{(1,-1,1,1)... }` as computed from `R` | any other kernel |
| **Q4** | *(regression / positive control)* the SAME general code, fed `A_2` weights, reproduces C155's measured `(1,-1,1)` and per-plane rank 1 | failure ⟹ `BLOCKED-INFRASTRUCTURE`, the `C_2` numbers mean nothing |

**A priori strength.** `rowspace(P)` is a 2-dimensional subspace of `R^4`. The
set of 2-planes in `R^4` is a 4-dimensional Grassmannian; hitting `R` exactly is
a measure-zero coincidence, not a 1-in-4 sign flip. Q1+Q2 together are a genuine
out-of-sample test, unlike the `A_2` observation that motivated them.

## What makes this test honest

* The prediction is written here **before** any `C_2` object is constructed.
* The `C_2` build needs **only the torus weights** — no Levi-Civita connection,
  no structure constants — so there is no free convention to tune. (Verified on
  `A_2`: C155's own machinery uses the torus generators for the family and for
  the invariant spinors; the LC connection entered only to *name* `psi_+`, and
  C155 Step 6 showed the rank result does not depend on which invariant spinor
  is used — `rank(v -> (D psi_+, D psi_-)) = 2`, same as either alone.)
* The same code path computes `A_2` and `C_2`; `A_2` is the regression gate.

## What this will NOT establish, whatever the outcome

1. Nothing about `N_gen = 3`, `lambda`, or any physical claim.
2. Two root systems are not a theorem. Confirmation would make the rule a
   well-supported empirical regularity with a stated domain (full flag manifolds),
   not a proved statement about all of them.
3. If the rule holds, it is likely **derivable** from weight bookkeeping
   (the image must have weight 0, and `sum x_k beta_k = 0` is exactly a
   weight-zero condition). Deriving it would make it *forced*, which by this
   project's own repeatedly-applied standard means **explained, not discovered**.
   That derivation is attempted in Step 3 and its outcome is reported either way.

---

# AMENDMENT 2 (2026-09-05) — the pre-registered rule is DEAD; a replacement is registered here BEFORE its test

## Outcome of the registered test

`G_2/T^2` gave **`rank(M) = 4`**. The rule predicted `2 * dim R = 8`.
**FALSIFIED out of sample.** The `A_2` agreement was the 1-in-4 sign
coincidence this document warned it might be. Recorded, not rescued.

## What the data show instead (POST-HOC — stated as such)

|        | `dim_C Sigma^T` | chirality split | `rank(M)` | opposite half, real dim |
|--------|---|---|---|---|
| `A_2`  | 2 | 1 + 1 | 2 | 2 |
| `G_2`  | 4 | 2 + 2 | 4 | 4 |

Decomposed into a forced part and a content part, each tested separately:

* `omega` anticommutes with every `E_a`, so `D_Sigma(v)` is **odd** — a general
  Clifford fact, verified in code on 6 and 12 generators. **FORCED.**
* `psi` has definite chirality and `Sigma^T` splits evenly. **OBSERVED.**
* Therefore `image(M)` lies in the OPPOSITE-chirality part of `Sigma^T`.
  **FORCED** by the two lines above — verified directly (`H4 = True`).
* `image(M)` **equals** that part. **NOT forced — this is the content.**

> **HYPOTHESIS S (replacement, post-hoc, registered now):** for a full flag
> manifold `G/T` and an invariant spinor `psi` of definite chirality, the map
> `M : v |-> D_Sigma(v) psi` on the `T`-equivariant connection family is
> **surjective onto the opposite-chirality part of `Sigma^T`**.

## Tests of HYPOTHESIS S, fixed before running

| # | test | prediction |
|---|---|---|
| **S1** | every definite-chirality invariant spinor on `G_2` (4 complex, 2 per chirality), not just `inv[0]` | surjectivity holds for each; `rank(M) = 4` every time |
| **S2** | same on `A_2` for both invariant spinors | `rank(M) = 2` every time |
| **S3** | THIRD SPACE `A_2 x A_2 = (SU(3)xSU(3))/T^4`: `N=6`, `r=4`, `dim m=12`, `dim Sigma=64`; invariant spinors expected `dim_C = 2*2 = 4` with a `2+2` chirality split | **`rank(M) = 4`** |
| **S4** | `A_2` recomputed with the POSITIVE-root orientation `(2,-1),(1,1),(-1,2)` instead of C155's `(-2,1),(1,1),(1,-2)` | same `rank(M) = 2` (orientation must not matter) |

**Weakness stated in advance:** `A_2 x A_2` is a PRODUCT, so its answer may
factorise trivially and is a weaker test than a new simple group would be. The
non-product rank-3 candidates were checked and mostly disqualified: `B_3` has no
invariant spinor (the `e_1` coefficient of `sum eps_k beta_k` is a sum of five
`+-1`s, never zero); `A_3` likewise (three `+-1`s). `C_3` may qualify but needs
`dim Sigma = 512` and a 2754-unknown family — not attempted here, and named as
the honest next test rather than quietly skipped.

**If S3 fails, HYPOTHESIS S dies the same way the root rule did, and this round
ends with two falsified hypotheses and no positive claim.** That outcome is
acceptable and will be reported as such.
