---
experiment_id: 20260708-dolan-casimir-g2su3
round: 39
date: 2026-07-12
tier: Full-Ladder
status: skeptic_reviewed_promoted
parent: round38 (established Dslash_mat^2 and sum M_p^2 closed forms via
  Casimir_su3); this round applies those closed forms to DERIVE a closed
  form for Round 25's own `step2_remainder`, part of the L4A norm-bound
  tension investigation (preprint.tex L560-607)
---

# claim.md — Round 39: Round 25's `step2_remainder` gets a full closed
form via Round 38 — REFRAMED after FL Step 8a (see Skeptic Verdict)

## Background

User: "го, round 39" — chose the recommended option from 4 candidates:
"Frame-term correction (рекомендую)" — continuing Round 24's own
flagged next step for the L4A investigation.

**Stale-summary correction (self-caught, before any computation):**
Round 38's own "Background" section characterized Round 23 as having
left `∇*∇` "NOT YET independently isolated/verified" on the twisted
bundle. Reading the actual files (not a compacted summary) shows this
was WRONG — Round 24 already isolated `∇*∇` directly from the
connection (`-Σ N_p²`, non-circular, PSD by construction), and **Round
25** (already closed, merged `main@811cb2b`, simply absent from the
stale summary I was working from) went further: it decomposed
`Dslash_mat²` itself via `cubic_and_curvature_L := Dslash_mat² -
CASIMIR_L_plain` (`CASIMIR_L_plain := -Σ_p M_p²`), tested
`cubic_and_curvature_L - (-H)` (`H` = Kostant's cubic torsion element,
`g2su3_H_element.py`) against scalarity, found it NON-scalar
(`step2_remainder`, diagonal `[-1/6, 5/2]` on the 2-dim SU(3)-invariant
subspace `span(w_a,w_b)`), and PROMOTED this as "empirical evidence the
Jac_h/curvature-Jacobi piece is a real, nonzero presence" — flagging
"derive the Jac_h term explicitly" as the concrete next step, NOT
started there. A research agent (this round, read-only) traced this
full history from the primary files before any new computation began.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — an exact algebraic identity and its
consequence, verified computationally. NOT empirical, NOT causal.

## Core argument

1. **[VERIFIED, STEP A]** Re-confirmed Round 38's own two closed forms
   unchanged: `Dslash_mat²=3·Id−(9/4)·Casimir_su3`,
   `Σ_p M_p²=−(1/2)·Id+(1/4)·Casimir_su3`.
2. **[VERIFIED, STEP B]** `cubic_and_curvature_L := Dslash_mat² −
   CASIMIR_L_plain = Dslash_mat² + Σ_p M_p² = (5/2)·Id − 2·Casimir_su3`
   EXACTLY — a direct algebraic sum of Round 38's two identities, on
   the full 8-dim Σigma (not just the 2-dim restriction Round 25 used).
3. **[VERIFIED, STEP C]** Round 25's own `step2_remainder :=
   cubic_and_curvature_L − (−H)` therefore has the FULL closed form
   `step2_remainder = (5/2)·Id − 2·Casimir_su3 + H`.
4. **[VERIFIED, STEP D]** Compressing this closed form onto Round
   23/24/25's own `span(w_a,w_b)` (via their EXACT definitions and
   compression method) reproduces Round 25's own asserted value
   `[[-1/6,0],[0,5/2]]` EXACTLY.
5. **[VERIFIED, STEP E]** Splitting the compressed value into its three
   closed-form pieces — `(5/2)·Id → [5/2,5/2]` (scalar),
   `−2·Casimir_su3 → [-8/3,0]`, `H → [0,0]` — shows `H`'s own
   contribution is exactly zero and `(5/2)·Id` is a genuine scalar, so
   the compressed non-scalarity traces to `−2·Casimir_su3`.
   **[POST-SKEPTIC CORRECTION, STEP F]** Two context-blind skeptics +
   a tool-using synthesis agent found this framing overclaimed: since
   `compress_2x2` is R-linear, `H`'s zero contribution here is a
   sign-flipped ALGEBRAIC CONSEQUENCE of Round 25's own STEP 5 result,
   not independent evidence; and the off-diagonal-zero half of the
   split is ALSO structurally forced for ANY `kron(X,Id8)` (confirmed
   by a new random-matrix control, STEP F) — carrying NO Casimir_su3-
   specific content. **Only the DIAGONAL split (`-8/3` vs `0`) is
   genuinely informative** — a direct, verified consequence of
   `Casimir_su3`'s own known eigenvalues (`4/3` on the sextet spanning
   `w_a`'s LEFT-factor content, `0` on the singlet spanning `w_b`'s).
6. **Conclusion (REFRAMED, not "corrects"):** this round DERIVES a
   closed form for `step2_remainder`, showing its diagonal
   non-scalarity traces to `Casimir_su3`'s eigenvalue split. Whether
   `Casimir_su3` (built from the su(3)-generator family) IS or merely
   resembles Agricola's own "Jac_h/curvature-Jacobi" term
   (`g2su3_H_element.py`'s own docstring ties that term to "su(3)-valued
   curvature") is an OPEN question this round does NOT resolve. If
   `Casimir_su3` IS that term, this round has DERIVED Jac_h in closed
   form, not shown it unnecessary — Round 25's original finding would
   then be VALIDATED, not corrected. What IS refuted is narrower:
   Round 25's own "not-yet-built" framing — `step2_remainder`'s closed
   form uses only PRE-EXISTING ingredients (`Casimir_su3`, `H`, a
   scalar), nothing new needed to construct it.

## Construction (code:
`g2su3_round39_step2_remainder_closed_form.py`)

**STEP A:** re-verify Round 38's two closed forms.

**STEP B:** verify `cubic_and_curvature_L = (5/2)·Id − 2·Casimir_su3`
exactly (sum of Round 38's two identities).

**STEP C:** verify `step2_remainder = (5/2)·Id − 2·Casimir_su3 + H`
exactly.

**STEP D:** reproduce Round 25's own compressed value on
`span(w_a,w_b)` via this round's closed form.

**STEP E:** split the compressed value into its three closed-form
pieces and confirm `H`'s contribution is exactly zero, and the
non-scalarity traces entirely to `Casimir_su3`.

## Falsifiable Claims

**C1:** Round 38's `Dslash_mat²`/`Σ M_p²` closed forms re-verify.
RESULT: `[VERIFIED-tool]` (STEP A).

**C2:** `cubic_and_curvature_L = (5/2)·Id − 2·Casimir_su3` exactly.
RESULT: `[VERIFIED-tool]` (STEP B).

**C3:** `step2_remainder = (5/2)·Id − 2·Casimir_su3 + H` exactly.
RESULT: `[VERIFIED-tool]` (STEP C).

**C4:** this closed form reproduces Round 25's own compressed value
`[[-1/6,0],[0,5/2]]` on `span(w_a,w_b)` exactly.
RESULT: `[VERIFIED-tool]` (STEP D).

**C5:** `H`'s own compressed contribution is exactly zero, and the
three closed-form pieces sum to reproduce `step2_remainder|_{2dim}`.
RESULT: `[VERIFIED-tool]` (STEP E) — **caveat added post-skeptic:**
this equality is guaranteed by R-linearity of `compress_2x2` given
Round 25's own STEP 5 result (sign-flipped), NOT independent evidence.
See Skeptic Verdict.

**C6 (added post-skeptic):** the off-diagonal-zero pattern in STEP
E/C5 is structural — it holds for `kron(X,Id8)` with an UNRELATED
random matrix `X` too, carrying no `Casimir_su3`-specific content.
RESULT: `[VERIFIED-tool]` (STEP F).

## Kill Conditions

- C2/C3 killed if: skeptic finds the closed-form arithmetic
  (`Dslash²+ΣM_p² = [3Id−9/4Cas]+[−1/2Id+1/4Cas] = 5/2Id−2Cas`) is
  wrong, or if `step2_remainder`'s definition doesn't actually match
  Round 25's own (`cubic_and_curvature_L − (−H)`).
- C4 killed if: the recomputed compressed value does NOT match Round
  25's own asserted `[[-1/6,0],[0,5/2]]` — the script's own STEP D
  directly asserts this equality using Round 25's EXACT `w_a`/`w_b`
  definitions and compression method, not a re-derived approximation.
- C5 killed if: `H`'s compressed contribution is NOT exactly zero (this
  is guaranteed by R-linearity of `compress_2x2` plus Round 25's own
  STEP 5 result, sign-flipped — a determinism/consistency check, NOT
  independent verification; see Skeptic Verdict), or if the three
  pieces do not sum to `step2_remainder|_{2dim}`.
- C6 killed if: the off-diagonal is NOT zero for a random `X` — would
  mean the "structural, not Casimir-specific" claim is wrong and the
  off-diagonal vanishing in C5 actually DOES carry Casimir-specific
  information.

## What this does NOT mean

- Does NOT resolve Delta's FULL non-scalarity. Round 25's own 5-piece
  decomposition of `Delta := D64²−∇*∇−F_{S^-}` also includes `T12+T21`
  (the TERM1·TERM2+TERM2·TERM1 cross pieces), `TORSION_E`, and
  `cross-Casimir` (`2·Σ kron(M_p,M_p)`) — NONE of these are touched by
  this round. `Delta`'s known value `[[5/2,4/3],[4,5/2]]` still has an
  unexplained non-scalar structure once `step2_remainder`'s own
  contribution is subtracted out.
- Does NOT reconcile the preprint's `8/45` norm-bound estimate against
  the exact `~1` ratio Round 23 found. That tension remains open.
- Does NOT touch `preprint.tex`.
- Does NOT prove no "Jac_h/curvature-Jacobi" term exists anywhere in
  this construction — nor does it prove `step2_remainder` is NOT
  evidence for one. Per FL Step 8a's finding: `g2su3_H_element.py`'s
  own docstring ties Agricola's Jac_h term to "su(3)-valued curvature,"
  the SAME family `Casimir_su3` is built from — so `Casimir_su3` may
  literally BE that term. This round does NOT determine whether it is
  "the same object, now in closed form" or "a genuinely separate,
  coincidentally-matching quantity." Either reading is currently open.
- Does NOT change `H`'s own status — Round 25's STEP 5 caveat (the
  `kron(-H,Id8)=0` finding being an inconclusive probe about H
  specifically, per two skeptics + author follow-up controls) is
  UNCHANGED by this round; this round's STEP E reproduces the SAME
  zero, but — per FL Step 8a — this is an algebraic consequence of
  linearity (a sign flip of Round 25's own computation), not a fresh,
  independent cross-check, despite the original framing claiming
  otherwise.
- Does NOT establish that the off-diagonal-zero pattern found in STEP
  E carries any `Casimir_su3`-specific information — STEP F's
  random-matrix control shows it is structural, holding for ANY
  `kron(X,Id8)`, a consequence of `w_a`/`w_b`'s disjoint RIGHT-index
  support alone (the same mechanism behind Round 25's own H/e_1/M_1
  null controls).
- Does NOT resolve the `M_p`/`Z_p` L4A convention question, `RHO`/`NU`'s
  literal AHL2023 notation question, or WHY Round 34's intertwiner `P`
  is Hadamard-type — all remain open, untouched.

## Skeptic Verdict (FL Step 8a)

Two context-blind skeptics (Read/Bash, no session history) + a
tool-using synthesis agent independently reviewed this round via direct
file reads of `round39_claim.md`, the script, and the two cited prior
scripts (`g2su3_round25_K_derivation.py`, `g2su3_round38_...py`).

| Claim | Skeptic 1 | Skeptic 2 | Synthesis (tool-verified) |
|---|---|---|---|
| C1-C3 | CONFIRMED-REAL | CONFIRMED-REAL | CONFIRMED-REAL (ran script, exit 0) |
| C4 | WEAKENED (tautological — regression check, not fresh evidence, though honestly worded) | CONFIRMED-REAL but tautological (same finding) | Agreed: consistency check, not independent verification |
| C5 | WEAKENED (H=0 "different route" claim FALSIFIED as characterization; off-diag zero partly structural per Round 25's own controls) | WEAKENED (identical two sub-findings) | Both confirmed by DIRECT tool re-test: verified `compress_2x2`'s R-linearity explicitly, verified `compress(kron(H,Id8)) = -compress(kron(-H,Id8))` exactly, verified off-diagonal zero for an unrelated random matrix too |

**Both skeptics independently reached materially identical
conclusions** (no disagreement to arbitrate). **Two concrete
overclaims found, both FIXED (not dismissed):**

1. **"H's zero contribution via a completely different route, genuine
   cross-check not a tautology"** — FALSIFIED as a characterization.
   `compress_2x2` is R-linear (`Pmat`, `G`, matrix multiplication — all
   linear operations), so `compress(kron(H,Id8)) = -compress(kron(-H,
   Id8))` is an algebraic identity; Round 25's own STEP 5 already
   established the right-hand side is zero, so the left-hand side is
   FORCED to be zero too, not independently discovered. **Response:
   Fixed** — removed the "genuine cross-check" language from both
   claim.md and the script's own printed CONCLUSION; STEP E's own print
   statement already said "sign-flipped," which was honest — only the
   claim.md prose and Core-argument framing overclaimed.

2. **Off-diagonal-zero carries no `Casimir_su3`-specific content** —
   the synthesis agent independently tool-tested this with a random
   8×8 matrix and confirmed off-diagonals vanish for ANY `kron(X,Id8)`,
   matching the exact mechanism (disjoint RIGHT-tensor-index support)
   Round 25's own post-skeptic controls already established for H/e_1/
   M_1. **Response: Fixed** — added a new in-script STEP F performing
   this exact random-matrix control directly (not merely citing Round
   25's analogous result), `EXIT=0`, confirmed. C6 added to Falsifiable
   Claims.

3. **"CORRECTS Round 25's own promoted headline finding"** — WEAKENED,
   with NEW supporting textual evidence found by the synthesis agent:
   `g2su3_H_element.py`'s own docstring explicitly ties Agricola's
   Jac_h/curvature-Jacobi term to "su(3)-valued curvature" — the SAME
   algebraic family `Casimir_su3` (built from `su3_action`) belongs to.
   This means `Casimir_su3` may literally BE Agricola's Jac_h term, in
   which case this round has DERIVED Jac_h in closed form rather than
   shown it unnecessary, and Round 25's original finding would be
   VALIDATED, not corrected. **Response: Fixed, not dismissed** —
   reframed throughout (script docstring, script CONCLUSION, claim.md
   Core argument #6, "What this does NOT mean") from "CORRECTS" to a
   narrower, defensible claim: `step2_remainder`'s closed form uses
   only pre-existing ingredients (refuting Round 25's "not-yet-built"
   framing specifically), while leaving the Casimir_su3-vs-Jac_h
   identity question explicitly open.

**True kill? No** (both skeptics + synthesis agree). C1-C3 are solid,
tool-verified algebra with no core-predicate falsification. What was
wrong was rhetorical/interpretive overclaiming in C5's framing and the
overall "CORRECTS" narrative — both fixed via genuine artifact-level
additions (STEP F) and honest reframing, not narrative dismissal.

**Overall: PROMOTE**, with C1-C4 and C6 `[VERIFIED-tool]` clean, C5
`[VERIFIED-tool]` with an explicit linearity caveat, and the headline
framing corrected from "CORRECTS Round 25" to "derives a closed form,
leaves the Casimir_su3-vs-Jac_h identity question open."
