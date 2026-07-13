# Round51-Universality-Scoping Decision

**Date:** 2026-07-13
**Verdict: PASS** (scoping conclusion confirmed) — **re-scores Round 48's
priority table, does not close the universality open problem**

## Summary

Read Charbonneau-Harland 2016 ("Deformations of nearly Kähler
instantons") in full, the one directly-relevant primary source Round 48
assumed would make "Universality → CP³, SU(3)/T²" a cheap, ~1.5-priority
follow-on. It is not.

**The paper studies a structurally different operator:**

| | Charbonneau-Harland 2016 | This project's L4 (S⁶) |
|---|---|---|
| Spinor bundle | Full `S` (rank 8, Λ⁰⊕Λ¹⊕Λ⁶), no chirality projection | `S⁻` (negative-chirality half) |
| Twisting bundle | `Ad_P` = the instanton's OWN gauge-group adjoint (`𝔥` or `𝔰𝔲(3)`) | `T^{1,0}S⁶⊕1` (the tangent bundle, a genuinely different SU(3)-rep) |
| Quantity computed | Deformation space of the canonical connection as an instanton | Kernel dimension of a twisted Dirac operator |
| Method | Frobenius reciprocity + Casimir-difference (Lemma 4) | Weitzenböck curvature-norm bound (L4A) + Kostant-Parthasarathy Casimir gap (L4B) |

Confirmed NOT secretly the same object (T3 in claim.md): `T^{1,0}S⁶`
under SU(3) is the standard representation `(1,0)` (complex dim 3,
verified against `preprint.tex:405-457`'s own branching data); the
adjoint `𝔰𝔲(3)` Charbonneau-Harland twist by is `(1,1)` (dim 8) — these
are different SU(3)-representations by construction, so their
deformation-space computation cannot be read as a kernel-dimension
result for this project's own operator, in either direction (no support,
no contradiction).

## What IS usable from the paper (real value, correctly scoped)

1. **Reusable Casimir eigenvalue formulas** for 𝔤₂, 𝔰𝔲(3) (isotropy
   normalization), 𝔰𝔲(2), 𝔰𝔭(2), 𝔲(1)⊕𝔲(1) — exact closed forms, would
   save real derivation time in a future attempt.
2. **A methodological lesson with immediate, checkable value**: their
   §4 discussion of Xu 2009's incorrect S⁶ rigidity proof — Xu's
   Casimir-difference computation silently produced a non-traceless
   result for an operator that is structurally forced to be traceless
   (contraction of a 2-form on a 1-form, and 𝔰𝔲(3) adjoint action, are
   both individually traceless), and this inconsistency alone proved
   the computation wrong, independent of re-deriving it. **Actionable
   for this project**: any future Casimir-difference / curvature-norm
   computation here should get the same cheap trace-consistency audit
   before being trusted — a pattern worth keeping in mind for any
   future L4B-style extension, not just this one.
3. **Confirms the torsion 3-form machinery itself is not G₂-specific**
   — it is derived generically for any nearly-Kähler 6-manifold and the
   paper applies it uniformly to all 4 Butruille spaces. This weakly
   supports the plausibility of SOME generalization existing, without
   telling us whether THIS project's specific L4B mechanism (built on
   the tangent bundle, not the adjoint bundle) is one of them.

## Corrected cost estimate

The actual generalization would require an independent derivation of
this project's own tangent-bundle SU(3)-structure decomposition under
the NEW isotropy groups (Sp(1)×U(1) for CP³, U(1)² for the flag
manifold) — i.e. redoing the equivalent of preprint.tex's own §L4A/L4B
construction (Weitzenböck bound + curvature endomorphism spectrum +
Kostant-Parthasarathy Casimir gap) for a genuinely new space, not a
formula substitution. This is comparable in scope to the original L4A/
L4B derivation itself (a multi-round effort in this project's own
history, per `experiments/20260621-g74a-lichnerowicz-gap/` and the
21-round L4A sub-investigation in `20260708-dolan-casimir-g2su3/`), not
a 30-minute follow-on.

**Re-applying the priority formula** (impact+kill_power+reusability+
publication_value)/(cost+assumption_debt+continuity_risk) with the
corrected cost (now comparable to the original multi-round L4
derivation, not "clean, reusable machinery"): this item's priority
drops from 1.5 to roughly **0.3-0.5** (cost term dominates) — now the
LOWEST-priority item on the Round 48 shortlist, not the second-highest.

## Recommended shortlist re-ranking

| # | Candidate | Old priority | Corrected priority | Note |
|---|---|---|---|---|
| — | RGE-matching | 2.11 | — | DONE (Round 49-50) |
| 1 | L4B remaining reps (ρ=27,64,77...) | 1.31 | ~1.31 (unchanged — cost was already correctly scoped as "reuses calibrated machinery") | still the best-scoped next candidate |
| 2 | Strong CP / θ_QCD | 0.80 | ~0.80 (unchanged) | untouched, but "full resolution" flagged as physically heavy at write-time already |
| 3 | L4A full 16-dim spectrum | 1.29 | ~1.29 (unchanged) | still flagged high continuity risk (adjacent to parked 21-round branch) |
| 4 | Universality (CP³/SU(3)/T²) | 1.5 | ~0.3-0.5 | **demoted** — this round's finding |

## What this does NOT mean

Does not mean Universality is permanently closed or uninteresting — the
Casimir formulas and trace-audit method extracted here remain reusable
if a future session wants to invest multi-round effort in it. This
round only corrects the cost estimate that made it look artificially
cheap.

## Files

- `claim.md` — this round's FL Standard-tier artifact
- No script needed — pure literature-reading + cost re-estimation, no
  numeric computation of this project's own to verify beyond the T3
  representation-theory cross-check (done inline, standard Lie theory,
  cross-checked against preprint.tex's own branching data).
