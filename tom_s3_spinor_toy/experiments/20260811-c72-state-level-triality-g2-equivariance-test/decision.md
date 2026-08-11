# decision -- g2-level bridge exists and is invertible; T^3=1 confirmed vacuous at every equivariance level

## Verdict

`G2_BRIDGE_INVERTIBLE_VERIFIED__SO8_NEGATIVE_CONTROL_CONFIRMS_ZERO__T3_TAUTOLOGY_FULLY_GENERAL__STATE_LEVEL_QUESTION_STILL_OPEN`
-> **P1 CONFIRMED. P2 CONFIRMED. P3 CONFIRMED (negative control passes).**
**Date:** 2026-08-11 · L0: descriptive · script: `c72_g2_equivariance_test.py`,
results: `results_c72.json`.

---

## Results, all [VERIFIED-numpy]

| Algebra | dim | Hom(v,s) | Hom(s,c) | Hom(c,v) | invertible found |
|---|---|---|---|---|---|
| su(3) | 8 | 6 | 6 | 6 | yes (established C70/C71) |
| **g2** | **14** | **2** | **2** | **2** | **yes, all three -- det 0.013/0.0018/0.0047, explicit residual ~5-7e-16** |
| so(8) | 28 | **0** | **0** | **0** | n/a (negative control) |

**Monotone shrinkage** (6 -> 2 -> 0) as the equivariance algebra grows from
su(3) through g2 to the full ambient so(8), exactly consistent with Schur's
lemma applied at each step:

- **g2 = 2, not a surprise once checked, but not previously verified this
  way.** `channel_v`'s g2-Casimir-like eigenvalue spectrum
  (`sum_a X_a X_a^dagger`) gives exactly one eigenvalue `~0` and seven equal
  eigenvalues `=2.0` -- confirming pearl #33's `8_v=1+7` g2-branching
  numerically and independently (Casimir-eigenvalue method, not the symbolic
  Cayley-Dickson derivation-equation method pearl #33 used). For two
  DIFFERENT copies of the SAME `1+7` g2-module, Schur's lemma forces
  `Hom=Hom(1,1)+Hom(7,7)=1+1=2` exactly -- matching the computed value. The
  dimension itself is therefore EXPECTED given the already-published
  branching, not a new discovery by itself.
- **What IS new: an explicit, verified cross-channel g2-equivariant
  ISOMORPHISM.** Pearl #33 established the `1+7` branching for ONE channel,
  symbolically, via a from-scratch octonion-derivation construction -- it did
  NOT construct a map BETWEEN channels. This round explicitly builds one (for
  all three pairs) and verifies it intertwines all 14 g2 generators to
  machine precision (`4.996e-16` to `6.968e-16`), the first time this
  specific cross-channel object has existed in this project.
- **so(8) = 0, the structural negative control, independently re-verified.**
  G102's own module docstring (`g102_spin8_fiber.py:19`) already asserts
  `Hom_so(8)` off-diagonal `= 0` as part of its own S5/S6 analysis -- this
  round re-derives it directly rather than trusting the citation, confirming
  it holds for the SPECIFIC construction C70/C71's bridge uses (not just
  G102's original context). This is exactly the textbook statement of
  triality: `8_v`, `8_s`, `8_c` are INEQUIVALENT as `so(8)`-representations.

## The T^3=1 tautology, re-derived and shown fully general

C71 found `T^3=1` (built by chaining `V_vs=U_s U_v^-1` etc. through a common
reference) is a pure algebraic telescoping identity for the SPECIFIC su(3)
case tested there. This round re-runs the same check with THREE INDEPENDENT
RANDOM matrices (`u_v, u_s, u_c` -- no su(3), no g2, no algebraic structure at
all) and finds `monodromy - I` residual `= 1.156e-14` -- i.e. **exactly zero,
confirming the tautology holds unconditionally, for any three invertible
blocks whatsoever, built this way.** This is not new information (the
telescoping proof `V_cv V_sc V_vs = U_v U_c^-1 U_c U_s^-1 U_s U_v^-1 = U_v
U_v^-1 = I` already makes no reference to su(3)) -- included here as an
executable confirmation, not a new claim, closing the question of whether
C71's finding was somehow specific to that case (it is not).

## Kill Analysis

**Not killed:** the bridge itself -- C70/C71's su(3)-level result stands, and
this round shows it partially SURVIVES strengthening to the full g2 (shrinks
to 2-dim but remains invertible), only vanishing at the full so(8) level
exactly where triality's own definition says it must.

**Killed, cleanly and generally (extending C71):** any attempt to test
`T^3=1` via chaining independently-found pairwise intertwiners, AT ANY
EQUIVARIANCE LEVEL -- proven, not just observed, to be structurally incapable
of discriminating genuine triality from arbitrary invertible relabeling.

**What survives, as a genuinely scoped next step:** a non-tautological test
of `T^3=1` needs `tau` (triality's automorphism) fixed INDEPENDENTLY of the
intertwiners under test -- e.g. via Baez's explicit `S3 subset F4` permutation
construction (pearl #33's own follow-up direction), then checking whether
SOME choice within the now-established 2-dim g2-Hom-spaces matches that
independently-fixed `tau`. Not attempted here -- a distinct, nontrivial
construction task.

## What this does NOT show

1. Does **not** resolve OB11(iii)'s state-level question -- McRae's own
   literature no-go (Euclidean case) remains the primary reference; this
   round strengthens the ALGEBRA-level picture (g2-equivariant cross-channel
   isomorphisms now explicit) without touching the STATE-level question that
   requires D/J/gamma, deferred per user direction.
2. Does **not** establish `T^3=1` as achievable or unachievable in any
   non-tautological sense -- genuinely untested, the right next construction
   (independent `tau`) is named but not built.
3. Does **not** change `N_gen=3`'s CONDITIONAL status.
4. Does **not** newly discover the `1+7` g2-branching -- reconfirms pearl #33
   independently; what's new is the explicit cross-channel isomorphism.

## Reproduction

```
python experiments/20260811-c72-state-level-triality-g2-equivariance-test/c72_g2_equivariance_test.py
```
Reuses G102's `derivation_basis`/`stabilizer_basis`/`restrict_to_subalgebra`/
`so8_basis` and C68's `hom_basis`/`search_nonzero_intertwiner` unmodified.
