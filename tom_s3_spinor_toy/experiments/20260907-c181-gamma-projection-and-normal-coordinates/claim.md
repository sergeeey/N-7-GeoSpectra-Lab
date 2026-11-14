# C181 — Claim

**Experiment ID:** `20260907-c181-gamma-projection-and-normal-coordinates`
**Parent:** items 4 and 5 of the 5-item plan responding to Tom Lawrence's
2026-09-07 §3.3 request, following C179 (the no-go) and C180 (the explicit
`S³` spinor harmonics).

His item 4, verbatim: *"a good double check is that you should be able to
take the outer product of the spinor multiplet and its adjoint, and then
use gamma matrices to project out the vector multiplet."*
His item 5: *"use the techniques described in my Part 5 video to find the
eigenfunctions of differential operators with respect to Riemann normal
coordinates ... These would then constitute a local section of a true
local spinor field."*

## Step -5: Zero-Signal Gate

- **Entity:** (a) the bilinear map from spinor data to the four vector
  harmonics `x_μ` on `S³`; (b) an alternative, equally-equivariant spinor
  basis built from the OPPOSITE chirality (`X^L` instead of `X^R`); (c)
  Riemann normal coordinates on `S³` at the identity via the quaternion
  exponential map, and the induced metric in them.
- **Falsifiable predicates:**
  1. Does the gamma-matrix projection actually recover the vector
     multiplet — i.e. is `x_μ = ½·Tr(σ_μ† g)` exact?
  2. **Does his proposed check DISCRIMINATE?** If an alternative spinor
     basis built from the wrong chirality passes the identical test, the
     check is necessary but not sufficient — a blind spot he should know
     about before relying on it.
  3. Does the outer product of ONE Weyl spinor with its own adjoint give
     the 4-dimensional `SO(4)` vector, or something smaller?
  4. Do the exponential-map coordinates satisfy the defining property of
     Riemann normal coordinates, `g_ab(0) = δ_ab` and `∂_c g_ab(0) = 0`?
- **Measurable outcome:** exact/symbolic verification of each, with the
  discrimination question (2) answered by actually building the
  alternative and running the same test on it, not by assertion.

## Step -2/-1 (EstimandOps L0)

**Question type: Descriptive.** Do explicitly-constructed objects have
stated algebraic properties, and does a proposed test distinguish between
two specified alternatives — not causal.

## Honest scope, BEFORE computing

1. Predicate 2 is the scientifically interesting one. This round expects
   the check to FAIL to discriminate, based on the general principle that
   a representation-content test cannot see which operator's eigenbasis
   was used. **Stating the expected answer in advance so that finding it
   is not mistaken for a discovery** — and so that the opposite outcome
   (the check DOES discriminate) would be the surprising, valuable result.
2. Predicate 3 is a dimension count that may correct the wording of his
   item 4: `2 ⊗ 2* = 1 ⊕ 3` is 4-dimensional but decomposes as singlet
   plus triplet under a single `SU(2)`; the `SO(4)` vector is `(½,0)⊗(0,½)`,
   which needs one index from EACH chirality. If confirmed, his recipe
   needs both chiralities, not one spinor and its own adjoint.
3. Item 5 here establishes the coordinate system and its RNC property.
   Transporting the full spinor-harmonic machinery into those coordinates
   is a larger task and is NOT attempted; the round reports what it does
   and does not cover.

## Kill-criterion table (frozen before running)

| Verdict | Condition |
|---|---|
| `PROJECTION-WORKS-BUT-DOES-NOT-DISCRIMINATE` | (1) the projection recovers `x_μ` exactly, AND (2) the wrong-chirality alternative passes the identical test — his check is necessary, not sufficient. |
| `PROJECTION-DISCRIMINATES` | (1) holds AND (2) fails, i.e. the alternative is rejected by the test — his check is stronger than expected, a genuinely useful finding in his favour. |
| `PROJECTION-FAILS` | (1) fails — the bilinear does not recover the vector multiplet, meaning either his item 4 is wrong or our construction is. Must be resolved before anything is sent. |
| `RNC-FAILS` | (4) fails — the exponential-map coordinates are not normal coordinates, meaning the item-5 groundwork is wrong. |

**Pre-registered expectation:** `PROJECTION-WORKS-BUT-DOES-NOT-DISCRIMINATE`,
plus predicate 3 confirming that one Weyl spinor's own outer product does
NOT give the `SO(4)` vector, plus (4) passing.

## AI-Hypothesis Pre-Gates

- **Source Trace:** Tom's PDF §2.2 and §3.3 (read directly). Spinor
  harmonics and vector fields reused verbatim from C180 via `importlib`.
  Existing frame work for cross-reference:
  `experiments/20260623-s3-spin-connection-to-tom-operators/decision.md`
  (Hopf-frame spin connection `ω₁₂=tan(α)e²`, `ω₁₃=−cot(α)e³`, `ω₂₃=0`,
  verdict `PASS_LOCAL_GEOMETRIC_MATCH`).
- **Novelty Check:** the session's repo inventory found **no** existing
  spinor⊗spinor*→gamma→vector projection anywhere in the repo, and **no**
  use of Riemann normal coordinates by name (the existing work uses the
  Hopf frame). Both are new here.

## What this does NOT mean (pre-registered)

1. A non-discriminating result does NOT mean his check is useless — a
   necessary condition that a wrong construction would fail is still worth
   running; it means it cannot be the ONLY check.
2. Does NOT deliver "a local section of a true local spinor field" in
   full — only the coordinate groundwork for it.
3. Does NOT change `N_gen=3`, any open blocker, or any project claim.
4. Does NOT constitute a submission to Tom (Submission Gate separate).
