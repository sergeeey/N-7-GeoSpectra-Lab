# C216 Claim — Kobayashi-Nomizu canonical-connection route, second independent
# check of C215's `Ric^grad=1.5` for S6=G2/SU(3)

**Date:** 2026-10-02
**FL tier:** [ ] Micro  [ ] Standard  [x] Full
**Question type:** [x] descriptive  [ ] predictive  [ ] causal

---

## Prior Result Gate (MANDATORY)

1. Exact claim: the Kobayashi-Nomizu canonical-connection curvature formula
   (`R^c(X,Y)Z=-[[X,Y]_h,Z]`, `T^c(X,Y)=-[X,Y]_m`, Nomizu 1954 /
   Kobayashi-Nomizu Vol.II Ch.X) — using ONLY the Lie bracket and su(3)'s
   adjoint action on the complement, no octonions, no Castellani code, no
   Friedrich-Ivanov formula — reproduces C215's `Ric^grad=1.5` for
   S6=G2/SU(3), as an independent THIRD route to the same number.
2. `decision.md`/`claim.md` grep (project-wide, "Kobayashi"/"canonical
   connection"): [x] done. Found `experiments/20260906-c165-canonical-
   connection-curvature-check/` — computes the SAME `R^c(X,Y)=-[X,Y]_h`
   object via the SAME cited source (Nomizu 1954; Agricola-Hofmann-Lawn
   2023 Remark 5.2), but for a DIFFERENT question (does `R^c` restricted to
   the `3bar`-summand of `Lambda^2(m)` supply an independent su(3)-
   equivariant map for OB14?) and in a DIFFERENT, unrescaled basis (G96's
   raw QR-orthonormalized complement generators, `scale=1`, not C212-215's
   ambient-unit tangent rescaling `scale=sqrt(3)`). Not a duplicate — the
   formula/citation is independently confirmed consistent with C165's own
   use of it, but C165 never computed a Ricci tensor from it (only the raw
   curvature 2-form, for a Schur's-Lemma vanishing question). No prior round
   computes `Ric^c` or cross-checks it against Friedrich-Ivanov. `null_
   results/` + `parked/`: 0 hits for this specific cross-check.
3. **Status:** [x] NEW.

---

## Estimand

**Population:** S6=G2/SU(3), G96/C210's certified complement + su(3),
C212-215's ambient-unit tangent basis (`scale=sqrt(3)`).
**Intervention:** compute `R^c(X,Y)Z=-[[X,Y]_h,Z]` and `T^c(X,Y)=-[X,Y]_m`
directly from the Lie bracket (no octonion cross product, no Castellani
structure-constant formula), contract to `Ric^c`, and compare to C215's
`Ric^grad=1.5`.
**Comparator:** C215's own value (`1.5`), itself derived from C213's
Castellani-formula `Ric^g=2.5` plus a torsion-correction term via
Friedrich-Ivanov's formula.
**Endpoint:** `Ric^c`'s isotropic constant, off-diagonal max, diagonal
spread; `|T|^2` from the bracket alone, compared to C212/C214's octonion-
route value (`24`).
**Summary measure:** exact match (`<1e-8`) to `1.5`, or not.
**MCID:** n/a — exact match expected if correct.

---

## Claim

The KN canonical-connection route, calibrated on an independent positive
control (S6=SO(7)/SO(6), round sphere, expect `Ric=5`, `T=0` by the
textbook unit-n-sphere formula and symmetric-space torsion-freeness) BEFORE
being trusted on the unknown, reproduces C215's `Ric^grad=1.5` for
S6=G2/SU(3).

---

## Kill criterion (MANDATORY)

| Kill condition | Threshold |
|---|---|
| KN control fails (`Ric^c_KN != 5` or `T != 0` on SO(7)/SO(6)) | any deviation `> 1e-8` — convention/sign error in the KN implementation itself, STOP before testing the unknown |
| KN's G2/SU(3) `Ric^c` does not match C215's `1.5` | mismatch `> 1e-8` |
| KN's bracket-torsion does not match C212/C214's octonion-torsion (`24`) | mismatch `> 1e-6` — would mean the two constructions (bracket vs octonion cross product) disagree on the SAME geometric object |

If FAIL (mismatch with `1.5`) → kills: the specific claim that C215's value
is independently confirmed by a third, torsion-free-formula route — does
NOT by itself kill C215's own internal derivation (Friedrich-Ivanov applied
to C213/C214's own numbers), which stands on its own internal consistency
checks (Section "What this does NOT mean" below).
If PASS → survives: `Ric^grad=1.5` confirmed via THREE independent
constructions (Castellani+Friedrich-Ivanov, and now KN's pure-bracket
route), closing the loop C215 itself named as the next step.

---

## Checks planned

| # | Check | Negative control |
|---|---|---|
| T1 | KN control: SO(7)/SO(6) gives `Ric^c=5`, `T=0` | a non-reductive or mis-split K/H would fail the `leak` check (residual outside the K-span), or give a non-isotropic/wrong-magnitude result |
| T2 | KN's G2/SU(3) bracket-torsion matches C212/C214's octonion-torsion (`24`) | a basis/scale mismatch between the bracket route and the octonion route would show up as ANY deviation, not approximate agreement |
| T3 [the real test] | KN's G2/SU(3) `Ric^c` matches C215's `1.5` | — |

---

## What this does NOT mean

1. A PASS would NOT re-derive Friedrich-Ivanov's formula or C213's
   Castellani code — it would be a genuinely independent THIRD route,
   using only the Lie bracket.
2. A FAIL does NOT automatically mean the KN implementation is wrong — the
   positive control (T1) is checked FIRST and independently, precisely so a
   FAIL on T3 can be attributed to a real discrepancy rather than a KN
   convention bug, if T1 passes cleanly.
3. Does NOT, by itself, re-litigate C212's torsion value, C213's isotropy/
   Einstein-ness findings, or C214's REJECT of the Russo/Agricola bridge —
   those are addressed separately in the Kill Analysis if this round's
   result bears on them.

---

## Fence (do not change without postmortem)

- lambda = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

**MISMATCH** — see `decision.md` for full results and Kill Analysis,
including a significant unresolved finding this round's own diagnostic work
surfaced (a factor-of-2 anomaly in C213's Castellani-formula code, found on
an independent control, that is NOT a simple global bug but is NOT yet
root-caused either).

**Status:** CLOSED MISMATCH — see `decision.md`.
