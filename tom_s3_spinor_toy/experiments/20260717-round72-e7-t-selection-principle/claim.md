# E7 — Claim: freezing rival hypotheses for "why t=0/t=1" BEFORE testing

**Date:** 2026-07-17
**FL tier:** [x] Full (research claim; methodology per project CLAUDE.md)
**Question type:** [x] descriptive [ ] predictive [ ] causal

Descriptive: does Agricola's own classification of the one-parameter connection
family ∇^t on S³=SU(2)/{e} (arXiv:math/0202094) single out t=0 and t=1 — the exact
n=0 zero-mode crossing values found by E2 — for a reason that is structurally
independent of the Dirac operator / zero-mode condition itself?

## Stakes
Internal-only (methodology discipline note on the open E2/E3 candidate mechanism,
feeding the still-open KT-8 gap). Not promoted to `preprint.tex` here.

## Background (established, not re-derived here)
- E2 (`experiments/20260717-round67-e2-s3-torsion-deformation/`): the torsion-deformed
  S³ Dirac operator family D^t = D^{1/2} + (t−1/2)·h_H (h_H=3) has zero modes at
  t ∈ {−2/3,−1/3,0,1,4/3,5/3} for n=0,1,2. The n=0 crossings are **exactly t=0 and
  t=1** (`results_e2.json`, `step4_closed_form_crossings_sorted_by_t`, rows n=0).
- E3 (`experiments/20260717-round68-e3-full-operator-torsion-deformed/`): confirmed
  the product-decoupling identity survives this deformation.
- Both E2's `decision.md` and E3's `decision.md` explicitly flag: **no physical
  principle is known for selecting any specific crossing t over t=1/2
  (Levi-Civita)** — picking t=0 specifically because it produces the wanted zero
  mode would be exactly the FITTED-vs-DERIVED trap this project's own methodology
  warns against (`~/.claude/CLAUDE.md` "Research parameter estimation" lesson, the
  G56/λ=0.30 case: finding a parameter value that produces a wanted result is a
  different, weaker claim than deriving that value from an independent condition).
  E2's `decision.md` "Recommended next action" already speculated that t=0/t=1
  "being the canonical/anticanonical — i.e. the two *flat* connections in
  Agricola's classification" might be "a more principled anchor than an arbitrary
  crossing," but did not check this. This experiment checks it.

## Rival hypotheses (frozen verbatim, BEFORE running any code below — Adaptive
Iteration Branch Rule / hypothesis-arbiter discipline: do not test one hypothesis
in a way that could tacitly confirm it while ignoring the others)

**H1 (Killing spinor):** `t` is fixed by requiring the existence of a Killing
spinor on S³ under the deformed connection `∇^t` (i.e., the deformed connection's
own defining geometric property, independent of the Dirac-operator zero-mode
computation).

**H2 (equations of motion):** `t` is fixed by background/gravitational equations
of motion for a torsion-carrying connection (i.e., torsion sourced by a physical
field satisfying its own EOM, not chosen post hoc).

**H3 (anomaly cancellation):** `t` is fixed by requiring anomaly cancellation in
the resulting 4D effective theory (a constraint from consistency of the full
construction, unrelated to the zero-mode condition itself).

**H4 (free parameter / fine-tuning):** `t` is a free parameter with no independent
physical principle selecting it; the zero-mode value is fine-tuning, chosen only
because it produces the wanted result.

## Claim (falsifiable) — scope: H1's cheapest sub-question ONLY

This experiment does **not** adjudicate H1 vs H2 vs H3 vs H4 in general. It runs
only the cheapest test available: **does Agricola's own classification of ∇^t
(established in her Section 2, via curvature/Ricci-tensor computations, BEFORE the
Dirac operator is even introduced in her Section 3) single out t=0 and/or t=1 for
a reason with zero reference to spinors or zero modes?**

Falsifiable sub-claim: the full curvature tensor R^t of ∇^t on S³=SU(2)/{e}
(H={e} trivial, m=g=su(2) — the same presentation E2 used) vanishes identically
as an operator if and only if t(t−1)=0, i.e. t ∈ {0,1} exactly — for **any**
nonzero structure constant (i.e. this is a structural fact about the S³=Lie-group
presentation itself, not an artifact of one calibration).

## Kill criterion (MANDATORY — filled BEFORE running)

| Kill condition | Threshold |
|---|---|
| R^t(X,Y)Z does NOT factor as t(t−1)·S(X,Y,Z) for some basis triple | `factorization_holds_for_all_27_triples == False` |
| R^t fails to vanish at t=0 or t=1 for some basis triple | `curvature_vanishes_at_t0_and_t1_for_all_27_triples == False` |
| R^t vanishes identically for ALL t (not just t=0,1) — i.e. S≡0 everywhere | `nonzero_S_example is None` — would mean the flatness condition is vacuous, not a genuine selection |
| t(t−1)=0 has roots other than exactly {0,1} | `matches_{0,1}_exactly == False` (this is pure algebra and cannot fail, included as a completeness check, not a real risk) |
| E2's own n=0 crossings do NOT equal {0,1} | `n0_crossings_equal_flat_connection_set_{0,1} == False` — would mean this test doesn't even connect to E2's result |

If FAIL on any of the first four → H1's specific sub-question comes back
**negative**: Agricola's classification does not single out t=0/t=1 for a reason
independent of the zero-mode condition, and this experiment should report H4
(free parameter / fine-tuning) as the honest current default. Do NOT force a
positive result by relaxing the check.

If PASS on all → H1's sub-question is **supported** (not proven): an independent,
purely-geometric criterion (full-curvature flatness, unrelated to spinors) exists
and happens to pick out exactly the same two values E2 found via the completely
separate zero-mode computation at n=0. H2, H3, H4 remain untouched either way —
see "What this does NOT mean" below.

If no hypothesis distinction is possible from FAIL vs PASS here → this gate would
not be scientifically motivated. It is: FAIL supports H4 by elimination of the
cheapest H1 test; PASS raises H1's plausibility for the n=0 crossing specifically,
without resolving H1 vs H2 vs H3 for the general case.

## Method

1. Read Agricola's paper (`Agricola_2002_Dirac_naturally_reductive.pdf`) for her
   own stated classification of the ∇^t family, independent of spinors:
   - t=0 = the "canonical connection" ∇^0 — by the Ambrose-Singer theorem, the
     *unique* metric connection on M with ∇^0 T^0 = ∇^0 R^0 = 0 (torsion AND
     curvature parallel). [PDF p.3]
   - t=1 = what Agricola names the "anticanonical connection" — introduced
     specifically because "it has the same Ricci tensor than the canonical
     connection." [PDF p.5]
   - Remark 4.2 (Theorem 4.4): Ric^t(X,Y) = (t−t²)β(X,Y) + (2t²−2t+1)A(X,Y); "the
     coefficient of β vanishes for t=0 and t=1." [PDF p.19-20] A purely algebraic
     (t−t²) factor from curvature alone, zero reference to Dirac operators.
2. Independently re-derive, by direct symbolic computation (not quoting the paper's
   prose alone), that for the trivial-isotropy presentation used here (H={e}, so
   Agricola's general curvature formula Lemma 2.2 collapses — the `[Z,[X,Y]_h]`
   term drops identically, not approximately, since h=0), the FULL curvature
   operator R^t(X,Y)Z factors exactly as `t(t−1)·S(X,Y,Z)` (using the Jacobi
   identity to eliminate the linear-in-t term — this is the sharper, stronger fact
   behind Agricola's Ricci-only Remark 4.2: R^t itself, not just its trace,
   vanishes at t=0,1 — these are the two Cartan–Schouten "flat" connections that
   exist on any Lie group with a bi-invariant metric).
3. Check exhaustively (all 27 ordered basis triples) that (a) the factorization
   holds exactly, (b) R^t vanishes at t=0 and t=1 for every triple, (c) R^t is
   genuinely nonzero for generic t (i.e. some triple has S≠0) — so the vanishing
   at t=0,1 is a real, non-vacuous constraint, not a trivial always-zero tensor.
4. Cross-check the Ricci-tensor trace directly reproduces Agricola's own stated
   Remark 4.2 factor (t−t²).
5. Cross-check with the project's own established structure constant c=2 (from
   E2's h_H=3=(3/2)·c, not re-fit here) that R^t is nonzero at t=1/2 (Levi-Civita,
   the round sphere — sanity check that the family is non-degenerate) and zero at
   t=0,1.
6. Read E2's own already-computed, already-verified `results_e2.json` (read-only,
   not modified, not recomputed) and confirm its n=0 crossings are exactly {0,1}
   — the same set singled out by this independent geometric criterion — while its
   n=1,2 crossings ({−1/3,4/3},{−2/3,5/3}) are explicitly NOT in that set.

## What this does NOT mean

1. Does **not** resolve H1 vs H2 vs H3 vs H4 in general. It tests only H1's
   cheapest sub-question (independent geometric distinction of t=0/t=1 via
   Agricola's own classification) and reports that result honestly.
2. Does **not** establish that a Killing spinor actually exists on the deformed
   S³ at t=0 or t=1 — H1 as literally stated ("t fixed by requiring the existence
   of a Killing spinor") is a spinorial condition that this script, by design,
   never touches (it works purely with Lie brackets, no Clifford algebra). A
   PASS here is evidence that t=0/t=1 are geometrically distinguished in a way
   that COULD support a Killing-spinor selection argument, not a demonstration
   that such a Killing spinor exists or that it is the actual selection mechanism.
3. Does **not** touch H2 (equations of motion) or H3 (anomaly cancellation) at
   all — both require a full background field theory / anomaly computation this
   project does not have, comparable in scope to a new multi-round investigation.
   They remain open, unexamined, regardless of this experiment's outcome.
4. Does **not** explain why n=0 (rather than n=1 or n=2) would be the physically
   relevant KK level for whatever compactification role this candidate mechanism
   might play — that is a separate, unaddressed physics question.
5. Does **not** explain the n=1,2 crossings ({−1/3,4/3,−2/3,5/3}) — no independent
   geometric distinction for these values was found anywhere in Agricola's paper
   (the only other named special values are t=1/2 Levi-Civita and t=1/3 Kostant's
   cubic Dirac operator — itself defined via the Dirac operator, hence not fully
   independent of the spinor picture — and neither matches any of these four).
6. Even if H1's sub-question is confirmed for t=0/t=1, this does **not** by
   itself promote the E2/E3 candidate mechanism to the preprint — the E2/E3 scope
   gaps (product-decoupling generalization, consistency with the rest of the
   construction) remain exactly as open as before this experiment.

## Assumptions (status)

| Assumption | Status |
|---|---|
| Agricola's ∇^t curvature formula (Lemma 2.2), canonical/anticanonical naming, Remark 4.2 | [VERIFIED-external-source] — read directly from the PDF this session |
| S³=SU(2)/{e}, H={e} trivial (m=g=su(2)) | [VERIFIED-external-source] — same presentation E2 used, justified there (symmetric-space presentation gives zero deformation freedom) |
| Jacobi identity holds for the coded bracket (sanity control) | [VERIFIED-tool] — checked exhaustively, all 27 triples, this script |
| R^t(X,Y)Z = t(t−1)·S(X,Y,Z) exactly (not merely at t=0,1) | [VERIFIED-tool] — exhaustive symbolic check, this script |
| E2's own established structure constant c=2 (h_H=3=(3/2)c) | [VERIFIED-tool, inherited from E2] — not re-fit here, used only for one concrete cross-check; main result is c-independent |

## Check
`python round72_t_selection_check.py` →
`verdict.label == "PASS_H1_SUBQUESTION_INDEPENDENT_CRITERION_FOUND"`,
`verdict.h1_subquestion_independent_geometric_criterion_found == true`,
`verdict.e2_n0_zero_mode_crossings_match_the_independent_flat_connection_set == true`.
