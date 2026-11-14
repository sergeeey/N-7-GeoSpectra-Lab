# C212 Decision — explicit nearly-Kahler torsion 3-form on S6=G2/SU(3)

**Date:** 2026-10-02
**Verdict:** PASS_CALIBRATED — new, calibrated number for F6's S6-side gap; does NOT give Ricci/Einstein constant.

## Results [VERIFIED-numpy, positive control passed]

```
dim(complement) = 6, tangent rank = 6                [matches G96 exactly]
cross product antisymmetry err  = 5.55e-17            (PASS)
cross product orthogonality err = 2.30e-17            (PASS)
TOTAL ANTISYMMETRY of T_abc (Gray's theorem, positive control) = 1.53e-16  (PASS)

|T|^2 = sum_abc T_abc^2 = 0.888889  (= 8/9 exactly)
max|T_abc| = 0.152773
```

`experiments/20261002-c212-s6-nearlykahler-torsion-3form/results_c212.json`.

## What this is

Agricola-Borowka-Friedrich (arXiv:1707.08591), Proposition 4.2, gives the
torsion 3-form of S6=G2/SU(3)'s characteristic connection explicitly:

```
T^c(X,Y,Z) = -<N,(XxY)xZ>
```

where N is the base point on S6 subset R^7=Im(O), X,Y,Z are tangent
vectors, and x is the octonion cross product -- the SAME cross product
G96's own `build_phi()` already encodes as the Fano-plane structure
tensor (phi_ijk = structure constant of e_i x e_j = phi_ijk e_k).

Computed directly on G96/C210's own certified complement basis (6
generators, already shown to form the SU(3) rep 3+3bar): identify the
tangent space T_N(S6) with the complement via the orbit map K|->K@N
(standard reductive-space construction, not a new one), then evaluate
the formula literally.

## Mandatory positive control, and why it matters here specifically

Per this project's own "instrument calibration before discovery"
discipline (C201) and the direct lesson from the PRECEDING turn in this
session (where a general Castellani curvature formula was judged too
risky to hand-transcribe without calibration): Gray's theorem states the
torsion of ANY 6-dim nearly-Kahler manifold's characteristic connection
is TOTALLY ANTISYMMETRIC. This is not something the formula is built to
satisfy automatically in my code -- `octonion_cross` and the base-point
contraction were implemented from the paper's formula directly, and
total antisymmetry in (a,b,c) is a NONTRIVIAL, independently-checkable
consequence that only holds if the transcription is correct. It passed
to machine precision (1.53e-16), which is strong evidence (not proof)
the implementation matches the cited formula and the underlying
octonion/complement data is self-consistent.

## Clean-number note (research-methodology.md Principle 6)

|T|^2=8/9 is an exact rational, same pattern as C211's Term1=8/Term2=-16.
Same caveat applies: this number is tied to G96's specific Frobenius-
orthonormal complement basis and the unit-radius choice N (|N|=1) --
rescaling the ambient radius or the complement generators rescales |T|^2
accordingly. Not re-derived against an independent source in this round
(no second computation of this exact quantity exists yet to compare
against) -- the calibration here is methodological (Gray's antisymmetry
theorem), not a numeric cross-check against a second number.

## Relationship to existing project results (explicitly NOT claimed)

- Does NOT relate to C134/C207's ECSK torsion (`T^{ABC}=(kappa_13/2)*i
  <psibar Gamma^{ABC} psi>`) -- that is a MATTER-SOURCED torsion on the
  full 13D background's equation of motion; this is the INTRINSIC,
  matter-independent geometric torsion of the S6 factor's own nearly-
  Kahler structure. Same word, different objects, per the Mechanism
  Transfer Gate (FORMULA/OBJECT/GENERATOR/SECTOR/OBSERVABLE all differ).
  No comparison attempted.
- Does NOT give S6's Ricci tensor/scalar curvature or Einstein constant
  -- the general Castellani curvature-formula route explored earlier
  this session was set aside as too risky to hand-transcribe without a
  calibration case; this round computed the TORSION instead via a
  lower-risk, directly-sourced formula with its own built-in positive
  control. The Ricci/Einstein-constant question for S6 remains open.
- Does NOT relate to round111's S3 Ricci scalar -- different coset
  factor entirely.

## Kill Analysis

**What was killed:** nothing -- all three checks (cross-product sanity,
tangent rank, total antisymmetry) passed.
**What this does NOT establish:** see claim.md's 4-item "What this does
NOT mean" -- most importantly, this is torsion, not curvature, and the
absolute magnitude is normalization-dependent.

## Next step this motivates (not started here)

Two independent follow-ups, neither attempted in this round:
1. S6's Ricci/Einstein constant via the Castellani general formula
   (arXiv:hep-th/9912277), NOW with a natural calibration path: since
   this round already built a verified, antisymmetric torsion for the
   SAME complement basis, a from-scratch Ricci derivation via the
   standard naturally-reductive-space torsion-to-curvature relation
   could reuse this round's already-validated `octonion_cross`/tangent
   machinery as a second, independent check -- cheaper than the N^010
   hand-transcription route considered and set aside earlier.
2. A real, careful embedding/normalization bridge between this round's
   intrinsic S6 torsion and C134/C207's matter-sourced ECSK torsion, IF
   a physically motivated reason to compare them is found -- not done
   here, flagged as a genuine open question, not a silent gap.

## Status

`PARENT_ACTION_GATE.md` F6 section to be updated with this result as a
new, calibrated input (separate from C211's moduli-potential terms and
C134/C207's ECSK torsion).
