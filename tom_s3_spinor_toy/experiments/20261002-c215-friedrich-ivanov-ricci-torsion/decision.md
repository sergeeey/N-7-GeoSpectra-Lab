# C215 Decision — Friedrich-Ivanov Ricci/torsion formula, component check on S6=G2/SU(3)

**Date:** 2026-10-02
**Verdict:** PASS — self-contained, single-author formula confirmed component-wise; `Ric^grad = 1.5*delta_bd`.

## Results [VERIFIED-numpy, isotropy check NOT assumed anywhere in the code]

```
Ric^g (Levi-Civita, C213/C214 re-confirmed)   = 2.5 * delta_bd
|T|^2 (torsion, C212/C214 re-confirmed)        = 24.0
corr(X,Y) = -(1/4)*sum_i g(T(e_i,X),T(Y,e_i))  = 1.0 * delta_bd  (off-diag 6.8e-16)
  trace(corr) = 6.0, matching the hand-derived prediction +|T|^2/4=6.0 exactly
Ric^grad := Ric^g - corr                       = 1.5 * delta_bd
  off-diagonal max = 9.8e-16, diag spread = 6.7e-16  -- ISOTROPIC, as Schur's lemma requires
```

`experiments/20261002-c215-friedrich-ivanov-ricci-torsion/results_c215.json`.

## What this is, and why it succeeds where C214 did not

C214 attempted to bridge C212's torsion and C213's Ricci via a formula
this project derived itself by COMBINING two papers that never cite
each other on this specific point (Russo's mu-based Einstein theorem +
Agricola-Borowka-Friedrich's T^c definition). That bridge failed by an
exact, unexplained factor of 2.

This round instead uses ONE single, self-contained, general-purpose
formula from ONE paper (Friedrich-Ivanov, arXiv:math/0102142, section
2), which directly relates the LEVI-CIVITA Ricci tensor to the
CHARACTERISTIC CONNECTION's own Ricci tensor plus an explicit torsion-
squared correction term -- valid for ANY metric connection with totally
skew torsion, not derived from or dependent on nearly-Kahler-specific
mu-type constructs:

```
Ric^g(X,Y) = Ric^grad(X,Y) + (1/2)*delta^g(T)(X,Y) - (1/4)*sum_i g(T(e_i,X),T(Y,e_i))
```

For nearly-Kahler, T is parallel w.r.t. the characteristic connection
(Kirichenko's theorem -- a standard, single structural fact about
naturally reductive spaces, not a bridge between two papers' own
bespoke definitions), so `delta^g(T)=delta^grad(T)=0` (the paper's own
section 2 states the two codifferentials always coincide on a 3-form
torsion). This leaves the two-term relation used here.

**Critically, this round checked the formula COMPONENT-WISE (a full 6x6
tensor), not just its scalar trace.** The resulting `Ric^grad` coming
out ISOTROPIC to machine precision (9.8e-16 off-diagonal) is a genuine,
non-trivial consistency check: Schur's lemma REQUIRES this for an
SU(3)-irreducible real 6-dim representation, but nothing in this
script's arithmetic assumes or enforces it -- a sign error, a wrong
index contraction, or a misapplied formula would generically produce a
non-isotropic (or simply wrong-magnitude) result, not a suspiciously
clean one. This is the SAME kind of structural cross-check that made
C213's Einstein-ness result trustworthy, now applied a second time to
a different pair of quantities.

## Relationship to prior results (explicitly scoped)

- Re-confirms C213's Ric^g=2.5 and C212/C214's |T|^2=24 in the process
  (both matched to the digit before the new formula was applied) --
  not a new, independent measurement of either, just a reuse check.
- Does NOT revive C214's rejected bridge -- that formula (Russo+
  Agricola's T^c<->mu) is unrelated to this one and remains REJECTED.
- Gives a genuinely NEW number: `Ric^grad=1.5` (the characteristic/
  canonical connection's own Ricci tensor for S6=G2/SU(3), in this
  project's established ambient-unit normalization) -- not previously
  computed anywhere in this project.

## Kill Analysis

**What was killed:** nothing -- all three checks (reuse consistency,
hand-derivation trace match, isotropy) passed.
**What this does NOT establish:** see claim.md's 4-item "What this does
NOT mean" -- most importantly, `Ric^grad=1.5` has not been independently
cross-checked via a SECOND route (e.g. the standard Kobayashi-Nomizu
fact that a reductive space's canonical-connection curvature is pure
isotropy-representation data, a Casimir-type computation) -- named as
the next step, not attempted here.

## Next step this motivates (not started here)

Independently compute `Ric^grad` via the Kobayashi-Nomizu canonical-
connection-curvature formula (`R^grad(X,Y)Z=-[[X,Y]_h,Z]` for a
reductive space, a pure isotropy/Casimir computation using ONLY su(3)'s
own action on the complement, no torsion tensor involved at all) and
check it ALSO gives `1.5` -- this would be a genuinely independent
THIRD route to the same number, closing the loop completely without
relying on this round's own (already internally cross-checked, but
still single-route) application of Friedrich-Ivanov's formula.

## Status

Not added to `PARENT_ACTION_GATE.md` -- an internal structural result
about S6's own intrinsic geometry (two connections' Ricci tensors now
both known, consistently related), not a new F6 equation-of-motion
input on its own; `activeContext.md` updated with the full chain
(C212-C215) for continuity.
