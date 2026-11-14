# C215 Claim — Friedrich-Ivanov Ricci/torsion formula, component check on S6=G2/SU(3)

**Date:** 2026-10-02
**FL tier:** [ ] Micro  [ ] Standard  [x] Full
**Question type:** [x] descriptive  [ ] predictive  [ ] causal

---

## Prior Result Gate (MANDATORY)

1. Exact claim: Friedrich-Ivanov's general Ricci-torsion formula
   (arXiv:math/0102142, sec. 2), for ANY metric connection with totally
   skew torsion -- self-contained, single source, no T^c/mu bridge --
   applied component-wise to S6=G2/SU(3), checked via the independent
   Schur's-lemma isotropy requirement.
2. `decision.md`/`null_results` grep: C214 is the only directly related
   prior result (the REJECTED Russo/Agricola bridge) -- explicitly
   different formula, different author, different (successful) outcome.
3. **Status:** [x] NEW.

---

## Estimand

**Population:** S6=G2/SU(3), G96/C210's certified complement + su(3),
C213/C214's already-verified ambient-orthonormal basis (r=sqrt(3)).
**Intervention:** compute `corr(X,Y):=-(1/4)*sum_i g(T(e_i,X),T(Y,e_i))`
component-wise (6x6 tensor, not just its trace), from C214's own
torsion tensor; subtract from C213/C214's own Ricci (`Ric^g`) to get
`Ric^grad := Ric^g - corr`.
**Comparator:** the REQUIREMENT (not assumption) that `Ric^grad` be
isotropic (`c*delta_bd`), per Schur's lemma for an SU(3)-irreducible
6-dim real representation -- a structural fact independent of this
formula, used here as a check on whether the formula was applied
correctly, not fed into the computation.
**Endpoint:** `Ric^grad`'s off-diagonal max and diagonal spread (both
should be ~0 if correct); the resulting Einstein-like constant.
**Summary measure:** off-diagonal max, diag spread, Einstein-like const.
**MCID:** n/a -- exact match to machine precision expected if correct.

---

## Claim

Friedrich-Ivanov's formula, applied component-wise (not just traced) to
S6=G2/SU(3) using already-independently-verified `Ric^g` (C213/C214)
and `T` (C212/C214) in a single shared ambient-orthonormal basis, gives
`Ric^grad = 1.5 * delta_bd` exactly -- isotropic to machine precision
(off-diag `9.8e-16`, diag spread `6.7e-16`), confirming the formula was
applied correctly (Schur's lemma is a REQUIREMENT the computation was
never told to satisfy, not an assumption built into it).

---

## Kill criterion (MANDATORY)

| Kill condition | Threshold |
|---|---|
| `Ric^grad` not isotropic | off-diag or diag-spread `> 1e-8` -- would mean a sign/index/contraction error in applying the formula (the SAME risk class as C214's factor-of-2) |
| Recomputed `Ric^g`/`T` don't match C213/C214's own saved values | any mismatch `> 1e-6` -- would mean the reused basis/code diverged |
| Hand-derived trace prediction (`+\|T\|^2/4`) doesn't match the component-wise trace | mismatch `> 1e-8` -- would mean THIS round's own index algebra (not Russo's bridge this time) has an error |

If FAIL (isotropy) -> kills: this round's application of the formula
(a sign, index, or contraction error somewhere) -- NOT Friedrich-
Ivanov's theorem itself (cited, trusted, general).
If PASS (all three, as happened) -> survives: a new, self-contained,
single-author-formula relation between S6's Ricci and torsion, with a
non-trivial structural cross-check passed, not merely asserted.

---

## Checks planned

| # | Check | Negative control |
|---|---|---|
| T1 | Recomputed `Ric^g`=2.5, `\|T\|^2`=24 match C213/C214 exactly | any mismatch flags a reuse/basis error immediately, before the new formula is even applied |
| T2 | Hand-derived trace prediction (`+\|T\|^2/4=6.0`) matches the actual component-wise trace of `corr` | this is exactly the KIND of hand-algebra step that produced C214's undetected factor of 2 -- checking it explicitly, not trusting it, is the point |
| T3 [the real test] | `Ric^grad` isotropic (Schur) | PASSED -- off-diag 9.8e-16, diag spread 6.7e-16 |

---

## What this does NOT mean

1. Does NOT independently cross-check the value `1.5` itself against a
   SECOND, different computation of the characteristic connection's own
   Ricci (e.g. via the standard Kobayashi-Nomizu fact that a reductive
   space's canonical-connection curvature is determined purely by the
   isotropy representation's own structure, a Casimir-type computation)
   -- that remains a genuine, un-attempted next step, named not hidden.
2. Does NOT relate the number `1.5` to C213's Levi-Civita Einstein
   constant `2.5` by any NEW independent route beyond the formula
   itself -- `1.5 = 2.5 - 1.0`? No: `Ric^grad=Ric^g-corr`, and `corr`'s
   diagonal is `1.0` each (not `1.5`), so `1.5=2.5-1.0` -- this IS
   exactly the formula's own arithmetic, not a separate coincidence.
3. Does NOT close F6 -- this is an internal-consistency / structural
   result about S6's own intrinsic geometry (two different connections'
   Ricci tensors, now both known), not a new equation of motion for the
   full M4xS3xS6 background.
4. Does NOT revive or retroactively fix C214's rejected bridge -- that
   formula (Russo + Agricola's T^c<->mu) remains REJECTED; this is a
   genuinely different, independently-sourced formula (Friedrich-Ivanov)
   that happened to succeed where the other did not.

---

## Fence (do not change without postmortem)

- lambda = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

**PASS (formula confirmed, component-wise, with a non-trivial
structural cross-check)** — Ric^grad=1.5*delta_bd, isotropic to machine
precision.

**Evidence:** [VERIFIED-numpy, cross-checked via Schur's-lemma isotropy,
not merely a traced scalar match].

**Status:** CLOSED PASS — see `decision.md`.
