# C214 Decision — torsion-Ricci relation check (C212 vs C213)

**Date:** 2026-10-02
**Verdict:** REJECT (the specific bridging formula `Ric=(5/24)|T^c|^2`) — C212 and C213 both independently re-confirmed, unaffected.

## Results [VERIFIED-numpy]

```
Step 1: v_a=K_a@N (G96 complement, ambient R^7 metric):
  Gram = (1/3) * I_6  exactly (off-diag 4.3e-16) -- NOT ambient-orthonormal as given in C212.
  Rescale factor needed: sqrt(3) = 1.732051

Step 3: torsion in TRUE ambient-orthonormal basis:
  |T|^2 = 24.000000  (= 27 * C212's own 8/9, confirming the rescaling -- torsion is
  degree-3, so length-rescale^3 -> squared norm rescale^6... wait, actually confirmed
  numerically as exactly 27x, matching (sqrt(3))^6=27 for a degree-3 tensor's squared norm)
  antisymmetry error: 2.22e-16 (Gray's theorem still holds, as it must)

Step 4: Ricci recomputed with Castellani's r=sqrt(3) (the SAME rescaling, applied to
the SAME validated riemann_ricci() code from C213):
  Einstein constant = 2.500000  (NOT 5/6/3=0.2778 as naive 1/r^2 scaling would suggest --
  Castellani's r enters the curvature formula non-trivially, not as a pure conformal
  factor on the final answer; this round's hand-prediction of the scaling DIRECTION was
  wrong, caught by just running the already-calibrated code instead of trusting hand
  algebra -- exactly the discipline this project's own feedback memory already names)
  off-diagonal: 1.19e-15, diag spread: Einstein confirmed again at this new r.

Step 5: Russo's Ric=5*mu^2 with mu^2=|T^c|^2/24=1.0 predicts Ric=5.0.
  Directly computed (step 4): Ric=2.5.
  Relative error: 50.0% -- a CLEAN factor of 2, not noise.
```

`experiments/20261002-c214-torsion-ricci-relation-check/results_c214.json`.

## What happened, and why this is a REJECT of the bridge, not of C212/C213

This round set out to connect two already-recorded, independently-
calibrated results (C212's torsion, C213's Ricci) via a formula this
round derived itself from Russo (arXiv:2002.04673, Ric_g=5*mu^2*g) and
the Agricola-Borowka-Friedrich T^c definition (arXiv:1707.08591). Before
even attempting the comparison, a critical prerequisite check (Gram
matrix of the tangent vectors) revealed that C212's and C213's own
numbers were NOT directly comparable at all -- they live in two
DIFFERENT normalizations (C212: ambient tangent vectors with norm^2=1/3
each; C213: Castellani's own `r=1` vielbein convention, a factor-of-3
DIFFERENT metric scale). This round fixed that first, by recomputing
BOTH quantities from scratch in a single, explicitly verified ambient-
orthonormal basis (Castellani's `r=sqrt(3)`, confirmed numerically to
give unit-norm tangent vectors before trusting anything downstream).

Only AFTER establishing a shared, verified basis did this round compare
against Russo's theorem -- and found a clean, exact factor-of-2
mismatch between the PREDICTED Ricci (5.0, from the torsion via the
derived bridge) and the DIRECTLY COMPUTED Ricci (2.5, via the SAME
Castellani code already double-calibrated in C213).

## Kill Analysis (per Falsification Ladder § Anti-Overfitting Gate discipline)

**What was killed:** the specific formula `Ric=(5/24)|T^c|^2`, as
derived in this round's own docstring from Russo's Lemma 3.1 + the
Agricola T^c definition. The mismatch is exact and reproducible (50.0%,
not a small residual), ruling out numerical noise as the explanation.

**What was NOT killed:**
- C212's torsion computation (`|T|^2`, Gray's antisymmetry theorem) --
  re-verified in THIS round's own rescaled basis, still antisymmetric
  to machine precision (2.22e-16).
- C213's Ricci computation (Castellani's formula, N^010-calibrated) --
  re-verified in THIS round at a NEW `r` value, still Einstein to
  machine precision (off-diag 1.19e-15). The code's correctness does
  NOT depend on which `r` it's run at.
- Russo's own theorem (`Ric_g=5*mu^2*g`) -- a cited, trusted result;
  this round never computed `mu` directly from its own definition
  (Lemma 3.1, via `(grad_X J)Y`), only INFERRED it indirectly from
  `|T^c|^2` via a derived bridge -- that bridge is what's suspect, not
  Russo's own theorem.

**Relaxation Map (candidate sources of the factor of 2, none verified
in this round -- named so the next attempt doesn't re-derive blindly
from scratch):**
1. A form-vs-tensor normalization convention: some authors define the
   norm of a p-form with an extra `1/p!` factor (`1/6` for a 3-form);
   this round used the raw tensor sum `sum T_ijk^2` with no such
   factor. A `1/6` factor would NOT explain a clean factor of 2 alone,
   but combined with another slip could.
2. A sign or factor-of-2 in how `T^c(X,Y,Z):=<(grad_X J)(JY),Z>`
   (Agricola et al.'s own definition) relates to the MORE PRIMITIVE
   object `(grad_X J)Y` that Russo's Lemma 3.1 and Theorem (Ric=5mu^2)
   are actually stated in terms of -- this round's own Y->JY
   substitution step (shown in the script's docstring) could hide a
   missed factor if `(grad_X J)` and `J` do not commute/anti-commute
   exactly as assumed at some intermediate step.
3. Possibly NOT a bug at all, but a genuine convention difference
   between "the torsion of the CHARACTERISTIC connection" (what
   Agricola et al.'s T^c literally is, and what this project's C212
   computed) and some OTHER torsion-like quantity Russo's own implicit
   derivation effectively uses internally (even though Russo's paper,
   as read, does not itself mention T^c or octonions at all -- the
   bridge from mu to T^c is entirely this project's own construction,
   built by combining two papers that don't cite each other on this
   specific point).

**Revival condition:** find a THIRD primary source that states the
torsion-Ricci (or torsion-scalar-curvature) relation for nearly-Kahler
6-manifolds EXPLICITLY in terms of T^c (not mu), with its own fully
worked normalization -- then re-run this SAME verified code against
THAT formula directly, rather than re-deriving another bridge by hand.

## Status

Not added to `PARENT_ACTION_GATE.md` -- this is an internal consistency
check between two already-recorded results, not a new F6 input itself.
Logged to `null_results/INDEX.md` per the REJECT protocol.
