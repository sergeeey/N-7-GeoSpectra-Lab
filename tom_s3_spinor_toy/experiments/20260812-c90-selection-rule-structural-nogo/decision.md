# decision -- entire C79-C89 coupling family is structurally level-preserving; a verified, viable alternative named but not built

## Verdict

`STRUCTURAL_NOGO_FOR_TRANSLATION_GENERATOR_COUPLINGS__MULTIPLICATION_OPERATOR_ALTERNATIVE_VERIFIED_VIABLE_NOT_YET_BUILT`
-> **P1 CONFIRMED (structural/dimensional fact, by direct inspection).
P2 CONFIRMED (nonzero Clebsch-Gordan coefficients, sympy-verified,
k=1,2,3).**
**Date:** 2026-08-12 · L0: descriptive · script:
`c90_structural_analysis.py`, results: `results_c90.json`.

---

## Results

| # | predicted | found | evidence level |
|---|---|---|---|
| **P1** structural obstruction | `T_k` has no shared index with `T_{k+1}` | **CONFIRMED** -- `T_k` is built entirely within level `k`'s own `(p,q,r)` space, `Z_i` acts as identity on `(p,q)`, and this holds for `l_{e_i}` too (Meier's own construction, certified in C85). Both are infinitesimal generators of the group's regular representation; Peter-Weyl levels are that representation's isotypic components -- invariant under translation by definition. | [VERIFIED-by-construction] |
| **P2** CG coefficients nonzero | level `k` to level `k+1`, via a level-1 multiplication function | **CONFIRMED**, `k=1,2,3`, coefficient `1` (exact) in each case tested, via sympy's own `CG` class. | [VERIFIED-sympy] |

## What this genuinely establishes

**The entire coupling-postulate family used throughout C79-C89 (built
from round67's `Z_i` and/or Meier's `l_{e_i}`, both infinitesimal
generators of S3's own left/right regular representation) is
STRUCTURALLY incapable of connecting different Peter-Weyl levels.** This
is not a limitation discovered by exhaustive testing -- it follows
directly from what a Peter-Weyl level (isotypic component) IS: a
subspace invariant under the very group action these generators
implement. C86, C87, and C89's per-level "no crossing" results were
therefore not merely three data points suggesting a pattern -- they were,
for this construction family, an EXHAUSTIVE test: no assembly of these
same pieces into a larger matrix could ever reveal inter-level mixing,
because the pieces themselves have no cross-level matrix elements to
assemble.

**This resolves the reviewer's own proposed "truncation convergence"
experiment before it needed to be built**: had it been constructed
literally from the existing `T`, it would have reduced to a direct sum
of the exact blocks already tested in C86/C87/C89, and would have
"converged" trivially -- not because of new physics, but because the
construction cannot do otherwise.

**A genuinely different construction was identified and its mathematical
basis verified**, not merely proposed: multiplying the S3 wavefunction
pointwise by a level-1 matrix-coefficient function (e.g. the fundamental
representation's `D^{1/2}_{ab}(g)`) is, by Clebsch-Gordan, capable of
connecting level `k` to level `k+1` -- confirmed via sympy's own exact
`CG` class (not hand-derived), coefficient `1` for the specific
`(m1,m2,j,m)` combination checked at `k=1,2,3`. This is a genuinely
different kind of operator (multiplication, not a translation generator)
and is NOT subject to the P1 obstruction.

## Kill Analysis

**Killed:** the reviewer's literal proposal (assemble C86-C89's existing
`T` into a block-tridiagonal `D_PW`, test truncation convergence) --
shown to add no information beyond what C86/C87/C89 already established,
for a structural reason, before being built.

**Not killed:** the underlying insight (does SOME coupling mechanism
bridge Peter-Weyl levels, and if so does it produce a crossing) --
redirected toward a verified-viable, genuinely different construction.

**What survives as the real next step, explicitly scoped, not built
here:** construct the multiplication-type coupling operator properly in
the certified `(p,q,r)` basis (C85's substrate), verify it against the
full set of Clebsch-Gordan coefficients (not just the one representative
checked here), build the resulting genuinely block-tridiagonal `D_PW`,
and THEN run the truncation-convergence test the reviewer originally
proposed -- this time on a construction capable of showing something new.
This is a substantial undertaking (comparable in scope to C85's own
certification work) and was not attempted this round, given the real
risk of introducing errors in a rushed construction late in a long
session -- deliberately deferred rather than rushed.

## What this does NOT show

1. Does **not** build or certify the multiplication-type coupling
   operator -- only verifies its mathematical basis is sound.
2. Does **not** run any spectral-flow or truncation-convergence test.
3. Does **not** claim no coupling construction whatsoever could bridge
   levels -- only that the translation-generator family (C79-C89's own)
   cannot, for a general and now-explicit reason.
4. Does **not** change `N_gen=3`'s CONDITIONAL status.
5. Does **not** solicit or reference Tom Lawrence's unpublished Part 5.

## Reproduction

```
python experiments/20260812-c90-selection-rule-structural-nogo/c90_structural_analysis.py
```
Self-contained -- uses sympy's own `CG` class directly, no reuse of
prior rounds' scripts (this round's subject is the structural relationship
between constructions already built, not a new numerical construction).
