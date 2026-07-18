# Round125 — SO(4)×SO(4) vs su(3)+centralizer: same structure or different?

## Question (round124's own flagged Relaxation Map item, row 3)

> "Cross-check against SO(4)×SO(4): are these two candidates the SAME
> underlying structure in different language, or genuinely different?"

Both candidates (round119's `SO(4)×SO(4)`, round124's `su(3)⊕u(1)⊕u(1)`)
independently achieve Gate 1 (algebraic distinguishability of `8_v,8_s,8_c`)
by escaping the rank-3 `SO(7)` ceiling. Neither round checked whether they
are secretly the same subalgebra of `so(8)`.

## Claim

`A = so(4)⊕so(4)` (12-dim, round119) and `B = su(3)⊕u(1)⊕u(1)` (10-dim,
round124), both realized as subspaces of `so(8)` in the 8-dim vector
representation (8×8 antisymmetric matrices on `8_v`), satisfy:

```
dim(A) = 12,  dim(B) = 10,  dim(A ∪ B) = 19,  dim(A ∩ B) = 3
```

Verdict: **PARTIAL_OVERLAP** — neither identical, nor one containing the
other, nor fully independent.

## Method (Cheapest Differentiating Test)

Reused already-verified machinery directly (no re-derivation):
- `A`: `triality_so4xso4_invariance.py:build_so4xso4_basis()` (round119).
- `B`: `g102_spin8_fiber.py`'s `derivation_basis → stabilizer_basis →
  centralizer_dim` chain (already used by round124).

Two independent numerical routes on the same generator sets, both via SVD:
1. `dim(A∩B) = dim(A) + dim(B) − dim(A∪B)`, rank of stacked flattened
   generators.
2. Principal angles: `SVD(Q_A^T Q_B)` where `Q_A, Q_B` are orthonormal
   bases of span(A), span(B). Count of `cos θ = 1` = intersection dim.

Both agree exactly: 3 singular values at `1.000000`, 4 at `0.707107`
(45°), remainder at `0`.

## No-Collapse Test (tolerance sweep, run before the skeptic pass)

Swept the SVD rank-cutoff tolerance over `{1e-4, 1e-6, 1e-8, 1e-10, 1e-12}`
× both near-1 thresholds `{1e-3, 1e-6}` — **identical result every time**:
`rA=12, rB=10, n_common=3`, same cosine spectrum to displayed precision.
Not a tolerance artifact.

## Skeptic Review (Step 8a, context-asymmetric: claim + code only)

**Verdict: CONFIRMED, with 2 corrections applied below.**

1. **Method validity confirmed** — both `A` and `B` are genuine linear
   subspaces of the same 28-dim ambient (`so(8)`, antisymmetric 8×8
   matrices); the rank-identity and principal-angle methods both apply
   exactly as used.
2. **Correction accepted — genericity was misjudged in the original
   framing.** Generic intersection of a 12-dim and a 10-dim subspace of a
   28-dim ambient is `max(0, 12+10−28) = 0` (the two subspaces "generically
   miss" — a negative expected overlap floors at 0). An **observed 3 is
   non-generic** — a real algebraic coincidence, not "as unremarkable as 0
   would have been" (my own initial framing, corrected here rather than
   smoothed over).
3. **Correction applied — structural identification, not just a dimension
   count.** Per the skeptic's explicit ask ("identify WHICH 3-dim
   subalgebra"): computed all 3 pairwise commutators of the intersection
   generators directly — **all exactly zero** (residuals `5e-15, 1e-15,
   5e-16` — machine precision, not "small"). The 3-dim intersection is
   **abelian**, a genuine `u(1)³` Cartan-type subalgebra, not `su(2)`.
4. **Caveat on method independence, accepted as stated, not disputed:**
   both SVD routes consume the SAME upstream generator constructions
   (`derivation_basis()`, `build_so4xso4_basis()`) — a bug in either
   would propagate to both numerical checks equally. The two methods are
   independent *computations* on shared inputs, not independent
   *re-derivations* of the input algebras from different first
   principles. Reported as such, not oversold as full independence.

Skeptic could not execute code in its own sandbox (Bash unavailable there)
— its review is analytical/code-inspection-based, cross-checked here by my
own actual tool execution (the tolerance sweep + commutator check above),
per this project's audit-verification-gate discipline (agent's [VERIFIED]
= my [INFERRED] until independently re-run, which was done here).

## What this establishes

`SO(4)×SO(4)` and `su(3)⊕u(1)⊕u(1)` are **genuinely different**
subalgebras of `so(8)` — not the same structure in different language —
but they are not unrelated either: they share an exact, non-generic,
3-dimensional abelian (`u(1)³`) common subalgebra. Both candidates being
rank-4 overall, sharing a rank-3 abelian core is itself worth flagging as
a possible hint of shared Cartan structure between the two routes to Gate
1 — not yet interpreted physically.

## What this does NOT establish (kill analysis / caveats)

- Does **not** identify the shared `u(1)³` with any known physical charge
  (hypercharge, `B-L`, etc.) — same caveat pattern as round119/round124.
- Does **not** resolve Gate 2 (physical/global realization) — this remains
  exactly as open as before for both parent candidates.
- Does **not** by itself explain WHY the two constructions (one from the
  octonion `H⊕Hℓ` block split, one from `su(3)`'s own centralizer) share a
  Cartan-type subalgebra — that would require identifying the shared
  `u(1)³` inside both parent objects explicitly (not attempted here).

## Pearl

`pearl_registry/INDEX.md` entry: "generic-intersection-dimension check
(`dim(A)+dim(B)−dim(ambient)`, floored at 0) is a cheap, first-pass test
for whether an observed subspace overlap is coincidental or structural —
apply it before interpreting any future dimension-counting result in this
project as 'just a number.'" Falsifiable prediction: any future overlap
check between two named candidate subalgebras should report this floor
alongside the observed intersection dimension.

## Next step (not attempted here)

Identify which 3 generators of `A` (or `B`) span the shared `u(1)³` in
terms of the octonion block structure (`H`, `Hℓ`) vs the `su(3)`
Cartan/centralizer basis — cheap, well-scoped, deferred (not required to
close this round's own question).

## Check (reproduces the verification)

```
cd experiments/20260718-round125-so4xso4-vs-su3-centralizer-comparison
python e42_so4xso4_vs_su3_centralizer.py
```
Expect: `dim_A_so4xso4=12`, `dim_B_su3_plus_centralizer=10`,
`dim_A_union_B=19`, `dim_A_intersect_B=3`, `verdict=PARTIAL_OVERLAP`.
