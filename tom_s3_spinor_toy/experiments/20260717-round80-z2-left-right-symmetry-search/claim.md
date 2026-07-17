# E14 (round80) Claim — Z2 left-right symmetry search

**Date:** 2026-07-17
**FL tier:** [x] Full (research/hypothesis, per project CLAUDE.md — every experiment
in this repo runs Full tier)
**Question type:** [x] descriptive (geometric facts, Sections A-C) + [ ] speculative
physical interpretation (Section D, explicitly labeled non-descriptive/exploratory)

---

## Prior Result Gate

1. Exact claim: does group inversion `g -> g^{-1}` on `S^3=SU(2)` realize the
   `t<->1-t` symmetry of the Cartan-Schouten connection family as an actual
   geometric isometry (not just an algebraic symmetry of the curvature/eigenvalue
   formula), and does this supply a physical mechanism forcing BOTH `t=0` and `t=1`
   to be simultaneously present in the physical spectrum?
2. `decision.md` grep for "inversion", "g^{-1}", "involution", "antipodal": 0 hits
   in any existing `experiments/*/decision.md` — done.
3. `round*_claim.md` + scripts grep for same terms: 0 hits — done.
4. `null_results/` + `parked/` grep: no such directories exist yet in
   `tom_s3_spinor_toy/experiments/` at top level (checked `ls`) — N/A, done.
5. `git log -S"g^{-1}"` / `-S"inversion"` pickaxe: not run (no existing hits found
   by grep above to require disambiguating a prior deletion) — skipped, low risk
   given (2)-(4) all clean.
6. Primary source: Agricola arXiv:math/0202094 (already used by E7/E9/E10 for the
   Cartan-Schouten family) — reused, not re-fetched; the isometry/inversion claim
   itself is standard Lie-group differential geometry (Cartan & Schouten 1926;
   any textbook treatment of bi-invariant metrics), verified here by direct
   computation rather than by re-reading a new source.
7. **Status:** [x] NEW

---

## Estimand

**Population:** the concrete quaternion-model realization of `S^3=SU(2)` used
throughout this project's torsion-family experiments (`g(x)=x0 I+x1 Z1+x2 Z2+x3 Z3`,
`Z_i=i sigma_i`, E9/round76's own conventions), together with the Cartan-Schouten
one-parameter connection family `Nabla^t` built from the left-invariant frame.
**Intervention:** the map `iota: g -> g^{-1}` (equivalently, on coordinates,
`Phi(x0,x1,x2,x3) = (x0,-x1,-x2,-x3)`).
**Comparator:** the identity map / no map (i.e., is `iota` a *nontrivial* isometry
with the claimed properties, vs. having no special structure).
**Endpoint:** (a) whether `Phi` preserves the round metric; (b) whether `Phi`
exchanges left- and right-invariant vector fields up to sign; (c) whether `Phi`
pulls back the torsion tensor `T^t` (hence the connection `Nabla^t`, given the
Levi-Civita part is isometry-invariant) to `T^{1-t}` (`Nabla^{1-t}`) exactly, for
ALL `t`, not merely `t=0,1`.
**Summary measure:** binary PASS/FAIL per sub-claim, verified by exact symbolic
(sympy) identities — no statistical/approximate measure involved (pure algebra).
**MCID:** N/A — these are exact symbolic identities; either they hold identically
or they do not.

**ICE:** none (no missing data / dropout in a symbolic-computation experiment).

---

## Claim

**Falsifiable statement (Sections A-C, descriptive/geometric):** the map
`iota: g |-> g^{-1}` on `S^3=SU(2)`, realized concretely as `Phi(x)=(x0,-x1,-x2,-x3)`,
(A) is an isometry of the round metric, (B) sends the left-invariant frame `{Z_i^L}`
to `{-Z_i^R}` (and vice versa) as an exact vector-field pushforward identity, and
(C) pulls back the torsion of the Cartan-Schouten connection family, `T^t`, to
`T^{1-t}` exactly for all symbolic `t` — hence, combined with isometry-invariance
of the shared Levi-Civita part, `iota^*(Nabla^t) = Nabla^{1-t}` as connections, for
the WHOLE family, not merely as a restatement of the `t<->1-t` symmetry already
known (E7) at the level of the curvature/eigenvalue formula.

**Separate, NOT pre-registered as a PASS/FAIL claim (Section D):** whether this
geometric fact supplies a physical mechanism forcing BOTH `t=0` and `t=1` sectors
to be simultaneously present in the physical spectrum (needed by E12/E13's
multiplicity gap). This is explicitly exploratory per the task; Section D reports
what was checked and reasoned through, honestly, without forcing a PASS/FAIL label
on an inherently interpretive question.

Supporting sub-claims:
1. `Phi` is an isometry of the round `S^3` metric (checked via `J^T J = I` for the
   constant Jacobian `J` of the linear map `Phi`).
2. `Phi(x)` gives exactly the coordinates of `g(x)^{-1}` on the unit sphere (i.e.
   `iota` is concretely realized by `Phi`, not merely analogous to it).
3. `Phi` pushes `Z_i^L` to `-Z_i^R` and `Z_i^R` to `-Z_i^L` (exact vector-field
   pushforward identity, both directions, all `i=1,2,3`).
4. The rotation-coefficient identity `sum_{k,l} b_i^k(x) b_j^l(x) eps(k,l,m) =
   sum_p eps(i,j,p) b_p^m(x)` holds for all `i,j,m in {1,2,3}` and all `x` (the
   "cross product of SO(3)-rotated vectors" identity, specialized to this
   project's own concrete `b(x)` functions from the adjoint-action conjugation
   `gbar(x) Z_i g(x)`, generalized here from round76's single representative case
   `k=0` to all three).
5. Combining 1-4 (algebraic derivation, documented in `decision.md`, each input
   step tool-verified): `iota^*(Nabla^t) = Nabla^{1-t}` for all `t`.

---

## Kill criterion

| Kill condition | Threshold |
|---|---|
| `Phi` does NOT preserve the metric (`J^T J != I`) | Any nonzero entry in `J^T J - I` |
| `Phi(x)` does not equal `g(x)^{-1}`'s coordinates on the unit sphere | `g(x)*g(Phi(x)) != NORM2*I` as a symbolic identity |
| Pushforward does not send `Z_i^L` to `-Z_i^R}` (or vice versa) exactly | Any nonzero symbolic residual in `J*XL[i] - (-XR[i] composed with Phi)` for any `i` |
| Rotation-coefficient identity fails for any `(i,j,m)` | Any nonzero symbolic residual |

If FAIL on any of the first three → kills the entire candidate mechanism outright
(the isometry/frame-exchange claim itself is false; there is no further point
asking about torsion/connection pullback). If FAIL only on the 4th (rotation
identity) → kills the CLEAN general-`t` connection-pullback claim specifically,
but does not necessarily kill the `t=0,1` ENDPOINT-only version (which can be
checked independently, more cheaply, via round76's already-established fact that
`Nabla^0` parallelizes the L-frame and `Nabla^1` parallelizes the R-frame,
combined with sub-claim 3 alone).

If PASS on all four → strengthens (does NOT prove) the physical hypothesis in the
background context; Section D still must be assessed on its own, separate,
interpretive terms — a PASS on the geometry does not automatically supply a PASS
on "both sectors are physically required" (see "What this does NOT mean").

---

## Checks planned

- T1: isometry check (`J^T J = I`, `Phi` maps unit sphere to itself, `Phi(x)`
  equals `g(x)^{-1}`'s coordinates, `det(J)` for orientation).
- T2: pushforward/frame-exchange check (`J*X_i^L(x) = -X_i^R(Phi(x))` and the
  reverse, for `i=1,2,3`, exact symbolic identity, reusing round76's
  `build_invariant_frames`).
- T3 (adversarial/edge case): the rotation-coefficient identity generalized to
  ALL `i,j,m in {1,2,3}` (27 combinations, including the diagonal `i=j` cases
  which must come out trivially `0=0` — checking these too, not just the
  non-trivial `i!=j` cases, catches any sign error that might otherwise cancel
  only in the cases actually checked).
- T4: `t=1-t` has a unique solution `t=1/2` (trivial algebra, but load-bearing
  for Section D's orbifold-descent argument) + fixed-point count of `Phi` on
  `S^3` (`x1=x2=x3=0`, `x0=+-1` — exactly 2 points) + `det(J)=-1`
  (orientation-reversing).

---

## What this does NOT mean

1. Does NOT prove H1c (which of `t=0`/`t=1`, if either, is physically selected) —
   the geometric symmetry relates the two values; it does not by itself select
   either one, nor does it resolve whether either is realized at all (KT-8's
   blocking gap, that `ker(D_full)=0` on the untwisted round ansatz, is
   completely untouched here).
2. Does NOT establish that the physical construction requires BOTH `t=0` and
   `t=1` simultaneously — Section D explicitly explores this and, on the two
   most natural concrete readings tried, finds the opposite (under-counting or
   a collapse back to `t=1/2`), not the hoped-for doubling. This is reported
   honestly as the main, expected-to-be-hard, unresolved part of the task.
3. Does NOT resolve E12/E13's multiplicity gap (6 total internal zero modes vs.
   3 needed) — nothing here changes the zero-mode-COUNT at fixed `t`; it only
   describes how the `t`-family transforms under one specific discrete isometry.
4. Does NOT claim this isometry, or its role, is already used anywhere in
   `preprint.tex` — Section 4 of `decision.md` reports a clean grep-verified
   absence.
5. Does NOT extend to the S^6 factor, the full `S^3 x S^6` operator, or any
   claim about `D_full`'s kernel — scope is the S^3 factor and its connection
   family only, exactly as E7/E9/E10/E11 restricted themselves.

---

## Fence (do not change without postmortem)

- lambda = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

See `decision.md`.
