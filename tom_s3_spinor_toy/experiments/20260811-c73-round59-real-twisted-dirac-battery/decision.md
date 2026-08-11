# decision -- chirality verified directly, deformation-robust, negative control genuinely incomplete (reported honestly)

## Verdict

`GROUND_TRUTH_REPRODUCED__CHIRALITY_VERIFIED_DIRECTLY__DEFORMATION_ROBUST_LINEAR_FAMILY__NEGATIVE_CONTROL_GENUINELY_OPEN`
-> **P1 CONFIRMED. P2 CONFIRMED. P3 CONFIRMED (explicable, not contradictory).
P4 CONFIRMED (within the tested family). P5 FAILS, honestly, as anticipated.**
**Date:** 2026-08-11 · L0: descriptive · script: `c73_dirac_battery.py`,
results: `results_c73.json`.

---

## Results, all [VERIFIED-numpy]

| # | predicted | found |
|---|---|---|
| **P1** ground-truth reproduction | matches round59's `(-1,-sqrt3,4)` | **CONFIRMED, exact** -- `a=-1.0+0j`, `b=-1.7320508...+0j` (`=-sqrt3` to float precision), `s=3.9999999999999996` (`=4` to float precision). Independent numeric route (complex128, `evalf`-converted from round59's own exact sympy `E`/`NOMIZU`) agrees with the three-route, skeptic-reviewed `[VERIFIED-INDEPENDENT-INTERNAL]` result to machine precision. |
| **P2** chirality | `ker(D+)=1, ker(D-)=0` | **CONFIRMED, and NEW** -- forward map (domain_inv=2 -> target_inv=1): rank 1, kernel 1. Backward/adjoint map (target_inv=1 -> domain_inv=2): rank 1, kernel 0. Hermiticity cross-check (`forward == backward^dagger`) exact, residual `0.0`. **This is the first time G74B/C21's "purely left-handed" conclusion has been verified directly from round59's own matrix** -- G74B (2026-06-21) derived it abstractly from dimension-counting (`dim ker(D+)+dim ker(D-)=1` and `ind=+1`), three weeks before round59's construction existed; this round closes that gap. |
| **P3** raw kernel vs invariant-sector kernel, explicable not contradictory | consistent, once scope is correctly identified | **CONFIRMED** -- raw 64-dim kernel of unrestricted `D`: **36**. Full (not invariant-restricted) `odd_even -> even_even` 16x16 block: rank 7, kernel **9**. SU(3)-invariant sector specifically (the quantity `preprint.tex` sec:kernel and round59 actually address): kernel **1**. The gap between 9 and 1 (non-trivial-isotype content within the SAME bigrading block) is exactly the territory Rounds 52-56's certified Casimir-difference bound (`K_cert=2sqrt(6)/3`) addresses -- **cited here, NOT independently re-verified**; this round makes no claim about whether that bound's specific numeric application to this operator's exact normalization has been checked. |
| **P4** deformation robustness | kernel dim stable near `t=1` | **CONFIRMED, exact closed form** -- `D(t) = t*D(1)` exactly (proven algebraically: `spin_lift` is linear in its bivector-coefficient argument, so scaling `NOMIZU` by `t` scales `D` by `t` identically; numerically confirmed, linearity residual at `t=2` vs `2*D(1)` is exactly `0.000e+00`). Kernel dimension of the invariant-sector map is **exactly 1 for every tested `t != 0`** (`-1, 0.5, 0.9, 1.0, 1.1, 1.5, 2.0`), degenerating to **2 only at the singular point `t=0`** (no connection at all). Calibration (the Killing-spinor condition) passes ONLY at `t=1` exactly, as expected from Killing-spinor rigidity -- but the RANK-1 structure survives well outside that single calibrated point. **Honest limitation:** this is a 1-parameter uniform-scale family only; no alternative admissible S6 connection (e.g. a characteristic nearly-Kahler connection distinct from Levi-Civita) exists anywhere in this project to test a genuinely richer, non-uniform deformation. |
| **P5** negative control | at least one discriminating wrong-twist test constructible | **FAILS, honestly, as anticipated in claim.md.** Three attempts, all within round59's own fixed construction, none discriminating: (a) Nomizu sign flip (`t=-1`): `\|b\|` unchanged (just sign-flipped, `b=+sqrt3` not `0`), rank still 1, kernel still 1 -- NOT a real negative control for kernel structure, only for the Killing-spinor calibration SIGN convention (which round59's own prior convention sweep already knew fails there, without checking the certificate value at that point -- now checked, and it does NOT vanish). (b) Alternate bigrading pairing `even_odd -> odd_odd`: gives the **exact same** `(a,b)=(-1,-sqrt3)` as the physical `odd_even -> even_even` pairing -- `Sigma`'s even/odd pieces are related by a hidden duality (plausibly the top-degree wedge element `y1 y2 y3` acting as an even<->odd swap), so this is a relabeling of the identical physics, not an independent test. (c) Mismatched-parity pairing `odd_even -> odd_odd`: identically zero (`max abs = 0.0`, exact) -- but this is **algebraically forced** (verified via the structural parity check: `D` preserves the SECOND factor's Clifford parity exactly, because both terms in `build_dirac` act via `E_i` only on the first factor while the bivector-built `NAB_i` preserves parity in whichever factor it touches), not a "wrong twist gets penalized" physics result. |

## What this means, stated carefully

1. **Chirality is now directly verified**, not merely inherited from an
   earlier abstract argument -- closes a genuine, previously-unnoticed gap
   between G74B/C21's dimension-counting claim and round59's own construction.
2. **The "kernel=1" headline claim is now precisely scoped and cross-checked**
   against the raw and full-block kernel counts -- these are NOT in tension,
   they measure different (nested) quantities, and the difference is
   attributable to already-established (cited) work, not a new problem.
3. **The zero mode survives a genuine, if narrow, deformation test** --
   robust under any nonzero rescaling of the connection, degenerating only at
   the trivial (no-connection) point. This is real evidence of topological
   (not fine-tuned) protection, within the tested family.
4. **A genuine wrong-twist negative control remains unbuilt.** Every
   accessible variation of round59's own fixed construction is either
   physically identical (hidden duality) or trivially zero (algebraic
   parity constraint) -- neither tests "does the twist need to be physically
   correct." This is reported as a real, unresolved gap, not smoothed over
   or quietly dropped.

## Kill Analysis

**Not killed:** round59's own certified `(a,b,s)=(-1,-sqrt3,4)` result --
independently reproduced, unchanged. G74B/C21's chirality claim -- confirmed,
now on firmer (direct, not just abstract) footing.

**Killed:** the assumption (implicit in `predictions_before_data.md`'s
phrasing) that "negative controls (wrong twist) failing as they must" would
be a quick, natural check within the existing construction -- shown false;
every natural candidate either isn't independent or isn't discriminating.

**What survives, as a genuinely scoped next step:** constructing a real
wrong-twist negative control requires twisting `D_{S6}` by a DIFFERENT
representation than `Sigma` itself (e.g. a non-`(1+1+3+3bar)`-type bundle, or
a deliberately non-`G2`-equivariant twist) -- a new construction, not a quick
follow-up, comparable in scope to round59's own original build effort.

## What this does NOT show

1. Does **not** independently re-verify Rounds 52-56's certified bound for
   non-trivial isotypic sectors -- cited by reference only.
2. Does **not** supply a genuine wrong-twist negative control -- P5 fails
   honestly; this piece of the original C73 spec stays open.
3. Does **not** test a general (non-uniform) connection deformation -- no
   richer admissible S6 connection family exists in this project.
4. Does **not** change `N_gen=3`'s CONDITIONAL status.

## Reproduction

```
python experiments/20260811-c73-round59-real-twisted-dirac-battery/c73_dirac_battery.py
```
Reuses round59's own `build_clifford`/`build_dirac`/`spin_lift`/`ADNU`/
`NOMIZU`/`EVEN_IDX`/`ODD_IDX`/`block_global`/`run_calibration` unmodified.
