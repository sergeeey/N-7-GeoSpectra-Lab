# decision -- genuine 2-parameter family found; kernel=1 topologically protected across the whole family; S+ still not independent

## Verdict

`GENUINE_2PARAM_FAMILY_FOUND__KERNEL_PROTECTED_ACROSS_FULL_ANGULAR_SWEEP__CALIBRATION_ISOLATED_TO_NOMIZU__SPLUS_STILL_NOT_INDEPENDENT`
-> **P1 CONFIRMED (space is 2-dim, not 1). P2 gives new information but does
NOT supply a discriminating negative control. P3 CONFIRMED, strongly.**
**Date:** 2026-08-11 · L0: descriptive · script: `c73b_torsion_family.py`,
results: `results_c73b.json`.

---

## Results, all [VERIFIED-numpy]

| # | predicted | found |
|---|---|---|
| **P1** dimension of admissible torsion family | 1 or larger | **2, not 1** -- `dim Hom_su(3)(m, Lambda^2 m) = 2` (direct linear-algebra computation, 720 equations x 90 unknowns, nullspace via SVD, smallest nonzero singular value `1.155` cleanly separated from two exact-zero singular values). round59's `NOMIZU` reconstructs in this 2-dim basis with residual `5.6e-16` (exact), at coefficients `(-0.9987, 0.0512)` -- magnitude `~1.0000` (sits on the unit circle of this basis), angle `177.064 deg`. **C73's own 1-parameter deformation test (`D(t)=t*D(1)`) covered only the RADIAL direction through NOMIZU's own point -- an entire ANGULAR direction was untested until this round.** |
| **P2** `S+` twist | matches or differs from `S-` | **Differs in shape, matches in substance.** Domain/target dimensions are exactly SWAPPED relative to `S-` (`(1,2)` vs `(2,1)`) -- consistent with the expected index sign flip `ind(D(x)S+) = -ind(D(x)S-)`. The map is injective (rank 1, kernel 0, out of a 1-dim domain) with the SAME magnitude structure `(1, sqrt3)` as the physical `S-` case. This is consistent with `S+`/`S-` being related by the same conjugation symmetry as round59's own `psi_+`/`psi_-` Killing-spinor branches (already known, from round59's own convention sweep, to give identical `s`) -- **not independent evidence**, but a genuinely new, correctly-computed, non-tautological cross-check (unlike C73's earlier attempts, which were either exactly identical results via a hidden duality, or algebraically-forced zeros). |
| **P3** kernel dimension across the angular sweep | constant or varying | **Constant, exactly, everywhere tested.** 13 angles swept (`0` to `270` degrees in `22.5`-degree steps, unit magnitude in the `(T1,T2)` basis): **rank 1, kernel 1 at EVERY single point**, no exceptions. `\|b\|` is `1.7320508076 = sqrt(3)` to 10 decimal places at ALL 13 angles -- only `arg(b)` varies, and it varies EXACTLY LINEARLY with the sweep angle (slope `-1` exactly, a clean U(1) phase-rotation structure: the genuinely 2-real-dimensional admissible family is, physically, a single COMPLEX parameter, and the kernel-rank result is a statement about that parameter's MAGNITUDE, which is protected, not its phase, which is free). |

## What this means, stated carefully

1. **The admissible torsion family is genuinely 2-(real-)dimensional, i.e. one
   complex parameter -- round59's `NOMIZU` is a specific point on the unit
   circle of this family, not a uniquely-forced choice.** This corrects an
   implicit assumption (never stated as a claim, but never checked either)
   that a naive Schur's-lemma intuition (`m` irreducible => `Hom(m,m)` scalar)
   might have suggested -- the correct computation is `Hom(m, Lambda^2 m)`,
   not `Hom(m,m)`, and `Lambda^2 m` contains `m`'s own irreducible pieces with
   multiplicity 1 each, giving `1+1=2`.
2. **Kernel=1 is topologically protected across the ENTIRE admissible family,
   not merely a narrow 1-parameter slice of it.** Combined with C73's own
   radial (`t`) sweep, this now covers the FULL `(r,theta)` plane's
   qualitative behavior: kernel=1 for every `r != 0` at every angle tested,
   degenerating only at the single point `r=0`. This is substantially
   stronger evidence for topological (not fine-tuned) protection than C73
   alone supplied.
3. **Calibration (genuine Killing-spinor existence) is a much sharper
   condition than mere kernel-rank protection** -- it fails at all 13 swept
   angles (none coincide exactly with NOMIZU's own `177.064` degree point,
   which sits between the `157.5` and `180` degree samples, both of which
   fail calibration) -- consistent with Killing spinors being essentially
   rigid/isolated, not a continuous family, exactly as expected from the
   general theory. The kernel-rank result and the calibration result are
   genuinely DIFFERENT conditions with different (and now separately
   characterized) domains of validity.
4. **The `S+` twist still does not supply a discriminating negative
   control**, despite being a legitimately new and independently-computed
   test. Four attempts total across C73 and C73b (sign flip, alternate
   bigrading pairing, mismatched-parity pairing, `S+` instead of `S-`) all
   either reproduce the identical physical result via a hidden symmetry, or
   vanish for purely algebraic reasons -- a consistent, now well-documented
   pattern suggesting round59's specific construction may not admit an
   internally-accessible discriminating negative control at all.

## Kill Analysis

**Not killed:** kernel=1's status as topologically protected -- STRENGTHENED
substantially, now confirmed across a genuinely 2-dimensional family, not
just a 1-dimensional slice.

**Killed:** the (implicit, never-stated) possibility that C73's narrow
1-parameter deformation test was missing a large, untested admissible
direction that could have broken the result -- checked directly, does not
break it.

**Not killed, sharpened:** the "no discriminating negative control" gap from
C73 -- confirmed to persist even after trying a genuinely different,
representation-theoretically motivated twist (`S+`). The pattern across FOUR
independent attempts (not one) makes it substantially more likely that this
specific construction (round59's homogeneous, Killing-spinor-based S6
Dirac operator) simply does not have an internally-accessible wrong-twist
control -- would require twisting by a bundle from OUTSIDE this
construction's own natural symmetry class.

## What survives, as a genuinely scoped next step

A discriminating negative control, if one is still wanted, needs a twist
bundle that is NOT related to `S-` by any symmetry of `Sigma`'s own
construction (not `S+`, not a sign flip, not a bigrading relabeling) -- e.g.
a twist by a representation with a DIFFERENT `su(3)`-module type entirely
(not `1+1+3+3bar`), or an explicitly non-`G2`-equivariant perturbation. This
is a substantial new construction, comparable in scope to round59's own
original build, not attempted here.

## What this does NOT show

1. Does **not** supply a genuine wrong-twist negative control -- this gap,
   identified in C73, persists after a fourth, well-motivated attempt.
2. Does **not** test deformations outside the identified `su(3)`-equivariant
   2-parameter family (by construction, non-equivariant deformations exit
   the domain where the invariant-sector machinery applies at all).
3. Does **not** change `N_gen=3`'s CONDITIONAL status.

## Reproduction

```
python experiments/20260811-c73b-torsion-family-genuine-deformation-and-twist-control/c73b_torsion_family.py
```
Reuses round59's own `build_clifford`/`ADNU`/`NOMIZU`/`run_calibration` and
C73's own `invariant_basis`/`build_numeric_dirac`/`su3_gens64` unmodified.
