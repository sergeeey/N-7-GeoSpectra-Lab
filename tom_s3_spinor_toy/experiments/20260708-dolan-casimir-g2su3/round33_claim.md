---
experiment_id: 20260708-dolan-casimir-g2su3
round: 33
date: 2026-07-11
tier: Full-Ladder
status: skeptic_reviewed_promoted
parent: round31 (found jach_coeff/degree4_coeff nonzero on exactly 3 of
  15 possible index-quadruples, verified computationally but explicitly
  flagged as "not explained from a deeper principle — plausibly connects
  to Round 28's proven 3-dim SU(3)-equivariant space")
---

# claim.md — Round 33: WHY only 3 of 15 quadruples are ever nonzero —
a structural corollary of Round 28's own 3-dim-space theorem

## Background

User chose this scope explicitly (of 4 offered candidates for Round 33):
"Объяснить почему только 3 из 15 quadruples ненулевые" — explain why
only 3 of 15 quadruples are nonzero, the recommended option connecting
to Round 28's proven 3-dimensional space, matching the same "verify
numerically → explain structurally" pattern as Round 29→30.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — structural/representation-theoretic
argument, verified computationally at every step. NOT empirical, NOT
causal.

## Core argument (a corollary of Round 28's theorem, not a new proof
from scratch)

1. **Round 28's theorem (already proven, reused unchanged):** any
   SU(3)-equivariant + Swap-symmetric Hermitian operator on `Σ` lies
   EXACTLY in the 3-dim space spanned by `{Id, Casimir_su3, H}`.
2. **[VERIFIED, STEP A]** `Ch_4` (Round 26's degree-4 piece of `C̃h`)
   and `degree4_term` (Round 26's degree-4 piece of `Ωg`'s cubic-term
   expansion) are BOTH SU(3)-equivariant, Swap-symmetric, AND Hermitian
   — so Round 28's theorem applies to them DIRECTLY.
3. **Structural fact (automatic from construction, not assumed):**
   `Ch_4`/`degree4_term` are built ENTIRELY as sums over 4 DISTINCT
   frame-vector indices `Z_i·Z_j·Z_k·Z_l` — ALWAYS a genuine degree-4
   Clifford element, hence ZERO degree-0 and ZERO degree-3 component,
   by construction.
4. **Degree-counting in the `{Id,Casimir_su3,H}` basis:** `H` is PURELY
   degree-3 (Kostant's cubic torsion element, by construction) — the
   ONLY source of degree-3 content in the span. `Casimir_su3 = Id+X/3`
   (Round 29/30) has ONLY degree-0 (coeff 1) and degree-4 (coeff 1/3 on
   `X:=Z1234+Z1256+Z3456`) parts. So in `M=a·H+b·Id+c·Casimir_su3`:
   zero degree-3 forces `a=0`; zero degree-0 (with `a=0`) forces `b=-c`.
   Hence `M = c·(Casimir_su3-Id) = (c/3)·X` for a unique `c` — FORCED,
   not assumed.
5. **[VERIFIED, STEP B]** Solving Round 28's own 3×3 system for
   `Ch_4`/`degree4_term` gives EXACTLY `a=0` for BOTH — confirming the
   prediction directly, not merely consistent with it.
6. **Conclusion:** `Ch_4`/`degree4_term` are FORCED proportional to
   `Casimir_su3-Id = X/3` — and since `X`'s own support (Round 29) is
   EXACTLY the 3 pair-partition quadruples with EQUAL coefficient across
   all three, `Ch_4`/`degree4_term` are FORCED to share this SAME
   support and "equal across the 3" property. This is WHY only 3 of 15
   quadruples are ever nonzero — a NECESSARY CONSEQUENCE, not a
   coincidence of Jacobiator index gymnastics.

**Bonus (STEP D):** re-derives Round 30's `Ch_tilde=Casimir_su3` via a
cleaner route: `Ch_tilde=Ch_0·Id+Ch_4`, `Ch_0=1` (established) +
`Ch_4=Casimir_su3-Id` (this round) gives `Ch_tilde=Casimir_su3` directly
— Round 30's finding is a SPECIAL CASE of this round's more general
theorem.

## Construction (code: `g2su3_round33_why_three_quadruples.py`)

**STEP A:** verify `Ch_4`/`degree4_term` are SU(3)-equivariant,
Swap-symmetric, and Hermitian — Round 28's theorem premise, checked
directly.

**STEP B:** solve Round 28's own 3×3 basis system for `Ch_4`/
`degree4_term`'s own `(a,b,c)` coordinates — PREDICT `a=0, b=-c` from
the degree-counting argument BEFORE solving, then check the prediction
against the actual solve (not merely observing it after the fact).

**STEP C:** confirm `Ch_4`/`degree4_term` equal `c·(Casimir_su3-Id)`
exactly (full 64-entry match), for the specific `c` each solves to.

**STEP D:** re-derive Round 30's `Ch_tilde=Casimir_su3` as a bonus
special case.

## Falsifiable Claims

**C1:** `Ch_4` and `degree4_term` are each SU(3)-equivariant,
Swap-symmetric, and Hermitian.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP A).

**C2 (the headline result):** solving Round 28's 3×3 system for
`Ch_4`/`degree4_term` gives `a=0` (zero H-component) for BOTH,
confirming the degree-counting prediction directly.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP B):
`Ch_4→(a,b,c)=(0,-1,1)`, `degree4_term→(a,b,c)=(0,5/4,-5/4)` — both
satisfy `a=0, b=-c` exactly.

**C3:** `Ch_4`/`degree4_term` equal `c·(Casimir_su3-Id)` exactly (full
matrix match), explaining their confinement to `X`'s own 3-quadruple
support.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP C).

**C4 (bonus):** `Ch_tilde=Casimir_su3` (Round 30) re-derived via
`Ch_0=1` + `Ch_4=Casimir_su3-Id`.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP D).

## Kill Conditions

- C1 killed if: skeptic finds `Ch_4`/`degree4_term` do NOT actually
  commute with all 8 `su3_action` generators or the `Swap` matrix, or
  are not genuinely symmetric — would invalidate applying Round 28's
  theorem to them at all.
- C2 killed if: skeptic finds the "predict `a=0,b=-c` BEFORE solving"
  framing is misleading (e.g. the prediction was written AFTER seeing
  the solve's result) — verify the docstring's degree-counting argument
  (STEP 4) is derivable purely from `H` being degree-3 and
  `Casimir_su3=Id+X/3`'s own established decomposition (Round 29/30),
  WITHOUT reference to `Ch_4`/`degree4_term`'s own solved values.
- C2 killed if: skeptic finds `H` is NOT actually purely degree-3 as an
  8×8 matrix (i.e. has a hidden degree-0/2/4 component) — this is the
  load-bearing structural fact behind "only H contributes degree-3" —
  verify by checking `Tr(H)=0` (no degree-0 component) directly, and
  more generally that `H`'s own construction (`build_H_matrix`, a sum
  over `i<j<k` DISTINCT triples of `Z_i·Z_j·Z_k`) cannot produce
  anything but a genuine degree-3 Clifford element.
- C3 killed if: skeptic finds the "full 64-entry match" check is not
  actually exhaustive, or `X`'s own 3-quadruple support (cited from
  Round 29) has since changed/regressed.
- C4 killed if: skeptic finds `Ch_0≠1` under some re-verification, or
  the bonus re-derivation secretly depends on numbers not independently
  established elsewhere.

## What this does NOT mean

- Does NOT explain the SPECIFIC numeric value of the proportionality
  constant `c` (e.g. why `Ch_4`'s own `c=1` specifically, not some other
  number) — that still requires the direct combinatorial computation
  from Rounds 26/29/31/32, unchanged by this round. This round explains
  the SUPPORT (which quadruples, why equal across them), not the VALUE.
- Does NOT independently re-prove Round 28's own 3-dim-space theorem —
  reused as an already-established, skeptic-reviewed fact.
- Does NOT change any previously-established spectrum, index, eigenvalue,
  or numeric value from Rounds 4-32 — purely an EXPLANATORY round, using
  already-verified objects (`Ch_4`, `degree4_term`, `Casimir_su3`, `H`,
  `Swap`) without modification.
- Does NOT resolve the preprint's `8/45 vs ~1.03` norm-ratio tension, the
  `M_p`/`Z_p` L4A convention question, or independently re-derive `RHO`/
  `NU`'s own octonion-multiplication origin — all remain open, untouched
  by this round.
- Does NOT make STEP D (bonus) a purely structural re-derivation of
  `Ch_tilde=Casimir_su3` — STEP D plugs in `Ch_4`'s own SOLVED `c=1`
  from STEP B (a directly-computed fact), not a value forced by
  degree-counting alone. Only the SUPPORT (`c*(Casimir_su3-Id)` form) is
  structural; the specific `c=1` is not.

## Skeptic Verdict (FL Step 8a — context-blind, claim.md + code only)

Two independent context-blind skeptics + a synthesis agent (Workflow
tool, task `w21faxvs4`) reviewed this round. This was the CLEANEST
round of the entire session to date: **zero FALSIFIED claims** from
either skeptic or the synthesis agent.

| Claim | Verdict | Note |
|---|---|---|
| C1 (SU(3)-equivariance/Swap-symmetry/Hermiticity of `Ch_4`/`degree4_term`) | `[CONFIRMED-REAL]` | Both skeptics + synthesis independently re-checked; synthesis additionally decomposed both objects into the full 64-element Clifford basis, confirming zero degree-0/3 content directly, not just via the commutator checks. |
| C2 (degree-counting forces `a=0, b=-c`) | `[CONFIRMED-REAL]` | Synthesis agent additionally tested the mechanism's GENERALITY on hand-built random/generic tensors unrelated to this project's physics data, confirming it is a general Clifford-algebra fact, not an accident of the specific curvature data. |
| C3 (`Ch_4`/`degree4_term` proportional to `Casimir_su3-Id`, full 64-entry match) | `[CONFIRMED-REAL]` | Independently re-verified via the synthesis agent's from-scratch full-basis decomposition — a third, fully independent route beyond the script's own `Basis_mat.solve`. |
| C4 (bonus re-derivation of `Ch_tilde=Casimir_su3`) | `[CONFIRMED-REAL], scope-corrected` | Both skeptics + synthesis flagged that the "clean route" framing understated its dependence on `Ch_4`'s own SOLVED `c=1` (a computed fact, not a structural derivation of that specific constant). Fixed: docstring BONUS section and STEP D print statements now explicitly state this is a PARTIALLY structural re-derivation (general proportionality form is structural; the `c=1` plug-in is not). Added to "What this does NOT mean". |
| C5 ("Honest Scope" precision) | `[CONFIRMED-REAL]` | Already accurately distinguished support-vs-value before this round's fixes; the C4 fix brings STEP D's in-script prose into alignment with what this section already said. |

**Minor non-blocking findings, both resolved via Fix (not Accept-limitation, since fixes were cheap):**
1. `.T` vs `.H` in STEP A's Hermiticity check — mathematically equivalent for these specific real matrices, but `.T` is inconsistent with Round 26's own convention. **Fixed**: changed to `.H` with an explanatory comment.
2. Docstring/STEP B "prediction BEFORE solving" language understated that the result is STRUCTURALLY FORCED, not a falsifiable experimental prediction in the ordinary sense. **Fixed**: STEP B's banner/prints/assert-message reworded to "structurally forced" framing throughout.
3. Recommended defense-in-depth: re-verify `Casimir_su3=Id+X/3` directly in this round's own script rather than only citing Round 29/30. **Fixed**: added STEP A', an independent in-script re-verification (builds `X:=Z1234+Z1256+Z3456` via `e_action`, checks `Casimir_su3`'s trace/8 degree-0 coefficient equals 1 and the remainder equals `X/3` exactly).

**Decision: PROMOTE.** All 5 falsifiable claims (C1-C5) survive; the one
scope-precision finding (C4) was a wording fix, not a retraction —
consistent with this project's FL response matrix (`FALSIFIED` ≠
`KILLED`; here nothing was even `FALSIFIED`, only a framing
imprecision caught pre-emptively).
