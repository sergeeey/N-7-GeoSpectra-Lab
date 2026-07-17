# E7 — Decision

**Date:** 2026-07-17
**Verdict:** PASS_H1_SUBQUESTION_INDEPENDENT_CRITERION_FOUND (H1's cheapest sub-question only)
**Go/no-go:** OPEN — a real, independent geometric criterion was found for t=0/t=1,
but H1 (Killing spinor) is not thereby proven, and H2/H3 remain entirely untested.
H4 (free parameter) is NOT the default for t=0/t=1 specifically, but IS still the
honest default for the n=1,2 crossings.

## Result

**Yes — Agricola's own classification of the ∇^t family independently singles out
exactly t=0 and t=1, with zero reference to spinors, Dirac operators, or zero
modes anywhere in the derivation.**

Two facts read directly from Agricola (arXiv:math/0202094), both established in
her **Section 2** (curvature and Ricci-tensor computations) — entirely before her
Section 3 introduces the Dirac operator at all:

1. **t=0 is the "canonical connection" ∇⁰** — by the Ambrose-Singer theorem, it is
   the *unique* metric connection on M=G/H such that its torsion and curvature are
   both parallel, ∇⁰T⁰ = ∇⁰R⁰ = 0 (PDF p.3, right after eq.(1)). This is a pure
   fact about parallelism of geometric tensors, with no mention of spinors.
2. **t=1 is what Agricola names the "anticanonical connection"** — she introduces
   this name specifically because, as she computes, "it has the same Ricci tensor
   than the canonical connection" (PDF p.5, immediately after her general
   curvature/Ricci formula, Lemma 2.2). Again purely a curvature-tensor fact.
3. **Remark 4.2** (from her general Ricci formula, Theorem 4.4): Ric^t(X,Y) =
   (t−t²)β(X,Y) + (2t²−2t+1)A(X,Y), and "the coefficient of β vanishes for t=0 and
   t=1, and is positive between these parameter values" (PDF p.19-20). An explicit
   algebraic (t−t²) factor derived from curvature alone.

This experiment went one step further than simply quoting these three facts: it
**independently re-derived, by direct symbolic computation** ([VERIFIED-tool],
`round72_t_selection_check.py`, `results_e7.json`), that for the specific
presentation used by this project (S³=SU(2)/{e}, H={e} trivial, m=g=su(2) — the
same presentation E2 used, chosen because the symmetric-space presentation gives
zero deformation freedom), the situation is even sharper than Agricola's Ricci-only
remark: the **full curvature tensor** R^t (not merely its trace, the Ricci tensor)
vanishes **identically as an operator** if and only if t(t−1)=0, i.e. **t ∈ {0,1}
exactly**, for any nonzero structure constant. Concretely:

```
R^t(X,Y)Z = t(t-1) · S(X,Y,Z)     for ALL basis triples (X,Y,Z), exactly
```

where S(X,Y,Z) := [X,[Y,Z]] + [Y,[Z,X]] is a fixed (t-independent) bracket
expression, derived using the Jacobi identity to eliminate the term linear in t
from Agricola's general curvature formula (her Lemma 2.2, specialized to h=0,
which holds identically for this presentation, not approximately). This is
exhaustively verified over all 27 ordered basis triples
(`step1_exhaustive_flatness_check.factorization_holds_for_all_27_triples = true`,
`curvature_vanishes_at_t0_and_t1_for_all_27_triples = true`), and a nonzero
example of S (triple (1,2,1), S = c²·Z2) confirms the vanishing at t=0,1 is a
genuine, non-vacuous constraint — R^t is nonzero for generic t (confirmed
concretely at t=1/2, the Levi-Civita/round-sphere connection, where curvature must
be nonzero — sanity check passed, `R_at_t=1/2_LeviCivita_nonzero_as_expected = true`).

**In standard differential-geometry language: t=0 and t=1 are exactly the two
Cartan–Schouten "flat" (torsion-full but zero-curvature) connections that exist on
any Lie group carrying a bi-invariant metric** (Cartan & Schouten 1926) — the
"(−)-connection" and "(+)-connection" that parallelize the Lie group via
left-invariant and right-invariant framings respectively. This is one of the
oldest, most standard facts in the differential geometry of Lie groups, completely
unrelated to spinors or the Dirac operator.

## Cross-reference against E2's own (independently computed, already-verified)
result

E2's `results_e2.json` (`step4_closed_form_crossings_sorted_by_t`) was read
**read-only** (not modified, not recomputed) for this cross-check:

```
n=0 crossings (E2, from the ZERO-MODE condition alone): { 0, 1 }
n=1,2 crossings (E2, same condition):                    { -1/3, 4/3, -2/3, 5/3 }
```

`step4_cross_reference_against_E2_results_e2_json.n0_crossings_equal_flat_connection_set_{0,1} = true`.

The n=0 zero-mode crossing set found by E2 **exactly equals** the independent,
purely-geometric flat-connection set {0,1} found here — via two totally separate
computations (E2: spinor Dirac-operator eigenvalue crossing at the lowest KK
level; E7: full curvature tensor of the affine connection, zero spinors involved).
This is not a coincidence of loose language — the sets are literally identical,
{0,1} = {0,1}, verified by exact symbolic/rational arithmetic on both sides.

`step4_cross_reference_against_E2_results_e2_json.higher_n_crossings_NOT_in_flat_connection_set = true`:
the n=1,2 crossings are confirmed **NOT** in {0,1} — i.e. this independent
criterion explains the n=0 values only, honestly, without overreach.

## Verdict on the 4 frozen hypotheses

| Hypothesis | Status after this experiment |
|---|---|
| **H1 (Killing spinor)** | **Sub-question tested: PASS.** An independent, purely-geometric criterion (full-curvature flatness — the Cartan–Schouten canonical/anticanonical connections) singles out exactly t=0 and t=1, with zero reference to spinors or zero modes. This is consistent with, and could motivate, a Killing-spinor-based selection argument for H1 (a flat connection is a natural candidate for admitting a parallel/Killing spinor structure), but **this experiment did NOT check whether a Killing spinor actually exists** at t=0 or t=1 under ∇^t on the deformed S³ — that would require a further, spinorial computation this experiment deliberately avoided (to keep the H1 sub-question independent of the zero-mode machinery). H1 remains a live, now-somewhat-more-plausible hypothesis, not a proven one. |
| **H2 (equations of motion)** | **Not tested. Explicitly out of scope.** Would require a full background-field-theory / torsion-sourced-EOM computation this project does not have — comparable in scope to a new multi-round investigation. Remains open. |
| **H3 (anomaly cancellation)** | **Not tested. Explicitly out of scope.** Would require a 4D effective-theory anomaly computation this project does not have. Remains open. |
| **H4 (free parameter / fine-tuning)** | **Downgraded for t=0/t=1 specifically** (a real independent criterion was found, so "no independent principle exists" is no longer accurate for these two values) — **but remains the honest default for the n=1,2 crossings** ({−1/3,4/3},{−2/3,5/3}), for which no independent geometric distinction was found anywhere in Agricola's paper. H4 also remains the default until H1's full Killing-spinor claim (not just this sub-question) or H2/H3 are actually tested. |

## Why this is NOT a resolution of the t-selection question (the reason for OPEN,
not GO)

1. **Sub-question, not the hypothesis.** H1 as stated requires an actual Killing
   spinor to exist at the selected t. This experiment tested only whether t=0/t=1
   are geometrically distinguished by *some* independent criterion — a necessary
   but not sufficient condition for H1. A follow-up would need to build the
   explicit Killing-spinor equation for ∇^t on S³ and check it directly at t=0,1
   (this reuses Agricola's own Theorem 4.2 apparatus for constant/parallel
   spinors under the canonical connection — already partially present in E2's own
   citation of Theorem 4.2 — but was not re-derived or re-checked here as an
   independent Killing-spinor condition; E2 used it only as a calibration input).
2. **Only explains 2 of 6 crossings.** The n=1,2 crossings remain unexplained.
   If this candidate mechanism is meant to select a *specific* zero mode (not
   just "some" zero mode), the fact that only the n=0 pair has independent
   geometric meaning is itself informative — it is some evidence that IF a
   selection principle exists, it plausibly points to the n=0 (lowest KK level)
   zero mode specifically, which is at least a structurally sensible outcome
   (lowest level = simplest/most likely physically relevant sector) rather than
   an arbitrary pick — but this is a plausibility remark, not a new proven fact.
3. **H2/H3 completely untested.** Nothing here rules out that anomaly
   cancellation or EOM constraints would select a *different* t (possibly not
   even in {−2/3,...,5/3} at all, in which case the whole candidate mechanism
   would need re-examination against those constraints too).
4. **Does not promote E2/E3.** The scope gaps already flagged in E2/E3's own
   `decision.md` files (generalized product-decoupling formula not literature-
   verified; consistency with the rest of the project's construction not
   examined) are completely unaffected by this experiment and remain exactly as
   open as before.

## Kill Analysis (per this project's Anti-Overfitting Gate — recorded even though
this is a PASS, not a REJECT, since the sub-question could have failed)

- **What this result rules out:** the possibility that Agricola's classification
  of ∇^t has *no* independent geometric content for t=0/t=1 (i.e. it rules out
  the strongest form of "these are just arbitrary crossing values with no other
  meaning" — that specific claim is now false for t=0/t=1, though it remains true
  for the other four crossings).
- **What remains unresolved:** whether H1's full claim (Killing spinor existence)
  holds; H2 and H3 entirely; why n=0 rather than another level would be physically
  selected; whether the flat-connection property is *causally* relevant to
  whatever physical selection mechanism (if any) actually operates in this
  project's compactification, or merely a suggestive correlation.

## Scientific significance

Independent of the t-selection question, this experiment reproduces (via direct
symbolic re-derivation, not just citation) a clean classical fact — S³=SU(2)'s
bi-invariant-metric Lie group structure has exactly two flat (Cartan–Schouten)
connections, and these coincide exactly with the n=0 zero-mode crossings of the
torsion-deformed Dirac operator family found independently in E2. Worth recording
as a genuinely non-obvious structural coincidence-with-a-reason, even though it
does not (yet) amount to a full physical selection principle.

## Recommended next action

If this line is pursued further, in order of cheapness: (a) build the explicit
Killing-spinor equation for ∇^t on S³ directly (reusing Agricola's Theorem 4.2
machinery for parallel/constant spinors under the canonical connection) and check
whether it is satisfied at t=0 and/or t=1 specifically — this is the natural next
cheap test for H1's actual claim, not yet done here; (b) if that also passes,
document the full chain (flatness → parallel-spinor existence → Killing spinor)
as a candidate — but still NOT sufficient — physical selection argument; (c) H2
and H3 each require substantially more work (a full background-field EOM setup or
a 4D anomaly computation) and should not be attempted casually. Until (a) is done,
do not cite "t=0/t=1 are physically selected" in `preprint.tex` or any report —
only "t=0/t=1 are independently geometrically distinguished (Cartan-Schouten flat
connections), which is a necessary but not sufficient condition for a
Killing-spinor-based physical selection argument (H1)."

## Summary table (per task requirement)

| Hypothesis | Tested here? | Verdict |
|---|---|---|
| H1 (Killing spinor) | Sub-question only (independent geometric distinction of t=0/1) | PASS on sub-question; full H1 claim (Killing spinor existence) NOT tested |
| H2 (equations of motion) | No | OPEN — not attempted, out of scope |
| H3 (anomaly cancellation) | No | OPEN — not attempted, out of scope |
| H4 (free parameter) | By elimination | Downgraded for t=0/t=1 (real criterion found); still the honest default for n=1,2 crossings and until H1's full claim / H2 / H3 are tested |
