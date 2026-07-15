---
# Round65-SU3T2-Killing-Spinor-Test Claim — falsify Round 59's own generalization pearl

**Date:** 2026-07-15
**FL tier:** [x] Standard
**Question type:** [x] descriptive

---

## Prior Result Gate (MANDATORY — filled BEFORE computing anything)

1. Exact claim: does Round 59's Killing-spinor closed-form argument for the
   trivial-`G₂`-isotypic block's rank (`b=⟨w,D⁺v_b⟩=−√3≠0 ⟹ rank=1`, via
   (i) the Killing eigenvalue `Dψ=∓nμψ` at the Friedrich-bound-saturating
   value, and (ii) `Term2≡0` because `Λ²⊗Λ²=3⊗3` has no `SU(3)` singlet)
   generalize to the analogous trivial-`T²`-isotypic block on
   `SU(3)/T²` (Butruille's other homogeneous nearly-Kähler 6-manifold with
   `T²=U(1)×U(1)` isotropy, NOT a sphere)?
2. `decision.md` grep: [x] done — `pearl_registry/INDEX.md` 2026-07-14 entry
   (Round 59) states the generalization as an untested prediction, impact
   6/10, explicit trigger "at Universality round kickoff." This round
   executes that trigger. 0 hits for any prior actual computation.
3. `round*_claim.md` + scripts grep: [x] done, 0 hits for `SU(3)/T2`,
   `T^2`, or `U(1)xU(1)` isotropy anywhere in this repo's scripts.
4. `null_results/` + `parked/` grep: [x] done, 0 hits.
5. `git log -S`/`-G` pickaxe: [x] done, 0 hits outside the pearl entry.
6. Primary source re-read: [x] to be done by the executing agent — see
   explicit warning below, this is the crux of the probe.
7. **Status:** [x] NEW.

---

## Explicit risk flagged BEFORE starting (learned from Round 64, same session)

Round 64 (`experiments/20260715-round64-universality-cp3-probe/decision.md`)
found that a superficially reusable formula (Charbonneau-Harland 2016's
Weitzenböck construction) was actually a CATEGORY mismatch when moved from
`S⁶` to `CP³`, because a coincidence specific to `S⁶` (`H=SU(3)` exactly)
made the original machinery look portable. The SAME risk applies here,
symmetrically:

- Round 59's source, Agricola-Hofmann-Lawn 2023 ("Invariant spinors on
  **homogeneous spheres**"), classifies Killing spinors on **multiple
  homogeneous presentations of the sphere `S⁶` itself** (`G₂/SU(3)` is one
  of nine). `SU(3)/T²` is the flag manifold — **topologically NOT a
  sphere** — and is very likely simply outside AHL2023's stated scope.
- The general fact that DOES transfer without a new source (classical
  nearly-Kähler theory, Grunewald 1990 / Friedrich-Grunewald): every
  homogeneous nearly-Kähler 6-manifold, sphere or not, admits a real
  Killing spinor with `Dψ=∓nμψ`, `μ` fixed by the Friedrich bound from the
  scalar curvature. This part should transfer.
- What must NOT be assumed to transfer without re-derivation: the
  `Term2≡0` step, which used `SU(3)`'s OWN representation theory
  (`Λ²⊗Λ²=3⊗3` has no `SU(3)` singlet). On `SU(3)/T²` the analogous
  isotropy group is the ABELIAN `T²`, a structurally different
  representation-theory question (abelian isotropy has only 1-dimensional
  irreps; "no singlet" means something different and must be checked
  fresh, not copy-pasted).

**This probe explicitly tests whether the SAME failure mode as Round 64
recurs — do not let that possibility bias the execution toward forcing a
positive result.**

---

## Estimand

**Population:** The trivial-`T²`-isotypic component of the twisted Dirac
operator `D⁺` on `SU(3)/T²`, analogous to `S⁶`'s trivial-`G₂`-isotypic
component.

**Intervention:** Apply Round 59's Route C argument structure (Killing
eigenvalue + Term2 vanishing check) to `SU(3)/T²`, using ONLY primary
sources that actually cover this specific coset (Charbonneau-Harland 2016
§1 gives its isotropy/structure data; a Killing-spinor source that
actually covers non-sphere nearly-Kähler manifolds must be identified —
do not assume AHL2023 covers it without checking).

**Comparator:** `S⁶`'s own result: `b=−√3≠0`, rank forced to 1.

**Endpoint:** Whether the analogous `Term2`-type quantity vanishes on
`SU(3)/T²`'s trivial block (by an honest rep-theory check of `T²`, not
copied from `SU(3)`), and whether a nonzero Killing-eigenvalue term
similarly forces rank ≥ 1 there.

**Summary measure:** A boolean (does the two-line argument go through) plus
the explicit rep-theory computation that decides it.

**MCID:** Not applicable — procedural probe, binary outcome.

---

## Claim

**Falsifiable statement:** Round 59's two-line rank-forcing argument,
re-derived (not copy-pasted) for `SU(3)/T²`'s own Killing-spinor data and
own `T²` isotropy representation theory, either goes through unchanged, or
fails at an identifiable specific step.

---

## Kill criterion (MANDATORY — filled BEFORE running)

| Outcome | Verdict |
|---|---|
| Killing eigenvalue nonzero AND `Term2`-analog vanishes by an honestly-rechecked `T²` rep-theory argument | PROMOTE (pearl confirmed on a second coset — genuine support for the Universality open problem, still not a full L4A/L4B derivation) |
| Killing eigenvalue nonzero BUT `Term2`-analog does NOT vanish for `T²` isotropy (abelian reps behave differently from `SU(3)`'s) | STRUCTURAL-NULL (genuine negative result: the pearl's mechanism is `SU(3)`-isotropy-specific, does not generalize — falsifies the pearl's own stated prediction, a real and citable finding either way) |
| No primary source in this repo (or reachable in one session) actually states `SU(3)/T²`'s Killing-spinor eigenvalue or `T²`-isotropy decomposition of the relevant bundle, without a fresh derivation from scratch | INCOMPLETE-MACHINERY — stop, do not improvise the missing representation theory from first principles (that would be a new multi-round project, exactly what this probe must not silently become) |
| `SU(3)/T²`'s trivial-isotypic block itself is not well-defined analogously to `S⁶`'s (e.g. isotropy has no nontrivial-enough structure to define an analogous split) | ILL-POSED |

**Explicit escape route:** one session only. Default to INCOMPLETE-MACHINERY
if the needed primary-source data isn't directly at hand — do not extend
into a second session "just to finish it."

## What this does NOT mean

- A PROMOTE verdict does NOT close the Universality open problem — it is
  one more data point (2 of 4 Butruille spaces checked), not a full
  generalization proof, and does not touch L4A's own still-open norm-bound
  tension.
- A STRUCTURAL-NULL verdict does NOT mean Universality is closed either —
  it means THIS specific mechanism (Killing-spinor trivial-block rank
  forcing) is `S⁶`-isotropy-specific, not that no mechanism could work on
  `SU(3)/T²`.
- Does NOT commit to checking the remaining two Butruille spaces (`CP³`
  already ILL-POSED via a different route in Round 64; `S³×S³` untested)
  regardless of this round's outcome.
