---
experiment_id: 20260708-dolan-casimir-g2su3
round: 41
date: 2026-07-12
tier: Full-Ladder
status: skeptic_reviewed_promoted
parent: round40 (T12+T21 partial closure); this round closes the
  FINAL two pieces (TORSION_E, cross-Casimir) of Round 25's 5-piece
  decomposition of Delta, completing the algebraic accounting begun
  by Round 39
---

# claim.md — Round 41: complete algebraic accounting of `Delta`'s
5-piece decomposition — a narrower claim than "L4A tension resolved"

## Background

User: "го, round 41" — chose "Закрыть оба куска (рекомендую)" via
`AskUserQuestion`, after a scouting computation found BOTH remaining
pieces of Round 25's decomposition (`TORSION_E`, `cross-Casimir`) are
clean, rational matrices when compressed on `span(w_a,w_b)`, and their
sum reconstructs Round 40's own `still_owed=[[8/3,1/3],[1,0]]` exactly
— a strong signal this round is tractable.

**Scope discipline (applying Round 40's own lesson):** following Round
40, this round does NOT attempt to express `TORSION_E`/`cross-Casimir`
in terms of `Casimir_su3` or any other named object — both are built
via DIRECT construction (matching Round 25's own exact code), not a
derived closed form.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — an exact algebraic construction, verified
computationally. NOT empirical, NOT causal.

## Core argument

1. **[VERIFIED, STEP A]** `TORSION_E` (built via direct construction
   from the `T`-table/`curv_h`-table, exactly Round 25's own code)
   compresses on `span(w_a,w_b)` to `[[8/3,2/3],[2,0]]` EXACTLY.
2. **[VERIFIED, STEP B]** `cross_casimir` (`2·Σ_p kron(M_p,M_p)`,
   exactly Round 25's own algebraic re-expression of Round 24's
   `∇*∇`) compresses to `[[0,-1/3],[-1,0]]` EXACTLY.
3. **[VERIFIED, STEP C]** `TORSION_E+cross_casimir` reproduces Round
   40's own `still_owed=[[8/3,1/3],[1,0]]` EXACTLY (self-contained
   re-derivation, not just cited).
4. **[VERIFIED, STEP D, the headline result]** Assembling ALL FIVE
   pieces of Round 25's decomposition — `piece_H+piece_step2_rem`
   (Round 39), `T12+T21` (Round 40), `TORSION_E`, `cross_casimir`
   (this round) — reconstructs `Delta_2x2=[[5/2,4/3],[4,5/2]]`
   (Round 24/25's own known value) EXACTLY.
5. **[VERIFIED, STEP E, mandatory honesty check]** `Delta_2x2` is
   directly asserted NOT proportional to `Id` (i.e. genuinely
   non-scalar) — this is a positive, in-artifact check, not merely
   left unstated.
6. **Conclusion — narrow, deliberately modest [POST-SKEPTIC REWORD]:**
   individual per-piece values Round 25 previously only PRINTED are now
   ASSERTED against fixed target matrices — every piece Round 25 set up
   (some flagged "not-yet-built" or "least-examined") is now a
   known, verified, exact quantity. **This is NOT the same claim as
   "the L4A norm-bound tension is resolved."**
   `Delta` remains genuinely non-scalar; Round 24's own concern
   (whether `R/4` can be cleanly, separately isolated from `Delta` AT
   ALL, given the twisted Weitzenböck identity does not close to a
   scalar `Scal/4+nabla*nabla`) is completely UNTOUCHED by this round
   — knowing WHERE each piece of `Delta`'s value comes from does not
   answer WHETHER the norm-bound argument's premise (`R/4` being a
   clean, isolable scalar) is valid.

## Construction (code:
`g2su3_round41_torsion_crosscasimir_full_closure.py`)

**STEP A:** build `TORSION_E` via direct construction, compress.

**STEP B:** build `cross_casimir` via direct construction, compress.

**STEP C:** re-derive Round 40's `still_owed` in-script.

**STEP D:** assemble the grand total of all 5 pieces, compare to
`Delta_2x2`.

**STEP E:** assert `Delta_2x2` is NOT scalar (honest-scoping check).

## Falsifiable Claims

**C1:** `TORSION_E` compressed = `[[8/3,2/3],[2,0]]` exactly.
RESULT: `[VERIFIED-tool]` (STEP A).

**C2:** `cross_casimir` compressed = `[[0,-1/3],[-1,0]]` exactly.
RESULT: `[VERIFIED-tool]` (STEP B).

**C3:** `TORSION_E+cross_casimir` reproduces Round 40's own
`still_owed=[[8/3,1/3],[1,0]]` exactly. RESULT: `[VERIFIED-tool]`
(STEP C).

**C4:** all 5 pieces sum to `Delta_2x2=[[5/2,4/3],[4,5/2]]` exactly.
RESULT: `[VERIFIED-tool]` (STEP D) — **`[WEAKENED]` per FL Step 8a:**
this is mathematically FORCED once C1/C2 hold, given Round 25's own
already-verified 64×64 five-piece identity plus linearity of
`compress_2x2` plus Round 24/25's cited `Delta_2x2` value — a
re-verification, not independent new evidence beyond C1/C2. See
Skeptic Verdict.

**C5:** `Delta_2x2` is NOT proportional to `Id` (i.e. `Delta` is
genuinely non-scalar). RESULT: `[VERIFIED-tool]` (STEP E) —
**`[WEAKENED — TRIVIAL]` per FL Step 8a:** `Delta_2x2` is a hardcoded
rational matrix (`5/2≠4/3`); this reduces to a `sympy.Rational`
arithmetic check, not a probe of physics. Both skeptics independently
flagged listing it as a numbered claim alongside C1-C4 as mild
taxonomy inflation — retained here (relabeled) because claim.md
already, transparently, called it a "mandatory honesty check" rather
than substantive evidence.

## Kill Conditions

- C1/C2 killed if: skeptic finds an error in the direct construction
  of `TORSION_E`/`cross_casimir` (e.g. a copy error from Round 25's
  own code, a sign flip in `nabla_bracket`, or a wrong `p<q` range).
- C3 killed if: the sum does not match Round 40's own value — would
  indicate C1 or C2 (or Round 40's own value) is wrong.
- C4 killed if: the grand total does not match `Delta_2x2` — since
  `Delta_2x2`'s known value is itself Round 24/25's OWN established
  fact (not re-derived from D64 here, but cited), this would mean an
  error in one of the FIVE piece constructions, or that `Delta_2x2`
  itself needs re-verification against the raw D64 construction (not
  attempted this round — a genuine limit, see below).
- C5 killed if: `Delta_2x2` turns out scalar — this WOULD be
  interesting (contradicts Round 24's own established finding) but is
  considered highly unlikely given `Delta_2x2` is a cited, previously
  multiply-verified fact (Round 24, re-verified Round 25).

## What this does NOT mean

- **Does NOT make `Delta` scalar.** `Delta_2x2=[[5/2,4/3],[4,5/2]]`
  remains genuinely non-scalar (C5, directly asserted). This round
  explains WHERE each piece of that value comes from — it does not
  change the value itself or make it scalar.
- **Does NOT resolve the `8/45 vs ~1` L4A norm-bound tension.** That
  tension is about whether `R/4=Scal/4` can be cleanly, INDEPENDENTLY
  isolated from `Delta` as a scalar piece at all — Round 24's own
  concern, explicitly UNTOUCHED here. Knowing the exact algebraic
  origin of each of `Delta`'s 5 pieces does not answer whether the
  underlying three-term Weitzenböck split (`D²=∇*∇+Scal/4+F`) is even
  the right decomposition to use for a norm-bound argument.
- **"Complete algebraic accounting" is a narrower, more modest claim
  than "L4A tension resolved" or "L4A investigation closed."** Do not
  conflate the two — this round explicitly does NOT attempt the
  latter.
- Does NOT re-verify `Delta_2x2` from the raw `D64` construction
  in-script — it is CITED from Round 24/25's own established,
  previously-verified value, not re-derived from scratch here.
- Does NOT touch `preprint.tex`.
- Does NOT resolve the Casimir_su3-vs-Jac_h identity question from
  Round 39, the `M_p`/`Z_p` L4A convention question (Rounds 23-26),
  `RHO`/`NU`'s literal AHL2023 notation question, or WHY Round 34's
  intertwiner `P` is Hadamard-type — all remain untouched.

## Skeptic Verdict (FL Step 8a)

Two context-blind skeptics (Read/Bash, no session history) + a
tool-using synthesis agent independently reviewed this round — with an
EXPLICIT instruction to scrutinize the "milestone"/"complete
accounting" framing hard, given this round's inherent overclaim risk.

| Claim | Skeptic 1 | Skeptic 2 | Synthesis (tool-verified) |
|---|---|---|---|
| C1, C2 | CONFIRMED-REAL | CONFIRMED-REAL | CONFIRMED-REAL (ran script, exit 0) |
| C3 | CONFIRMED-REAL | CONFIRMED-REAL (tautological given C1+C2) | CONFIRMED-REAL |
| C4 | CONFIRMED-REAL, weakened novelty | WEAKENED (mathematically forced) | WEAKENED |
| C5 | CONFIRMED-REAL, trivial | WEAKENED (trivial) | WEAKENED |

**No FALSIFIED claims. No killing overclaim found — but real,
substantive findings, applied here as fixes, not dismissed:**

1. **Construction fidelity — CONFIRMED, no action needed.** Both
   skeptics independently did a line-by-line comparison of
   `TORSION_E`/`cross_casimir`'s construction against Round 25's own
   code: bit-identical (same `nabla_bracket`, same `p<q` range, same
   sign conventions, same `T`-table source). No reimplementation drift.
   The synthesis agent additionally confirmed the constructions are
   NOT reverse-fitted to the expected values (the `expected_torsion`/
   `expected_cc` targets appear only in `assert` lines, never feeding
   into construction).
2. **Rhetoric overweighted the content — MITIGATED.** Both skeptics
   independently flagged the same issue: "genuine milestone for the
   L4A investigation running since Round 16" (script) and repeated
   "COMPLETE ALGEBRAIC ACCOUNTING" phrasing overstate what is
   substantively "Round 25's own per-piece printouts are now `assert`-
   pinned." Neither skeptic found this a KILLING overclaim (each strong
   phrase was already co-located with an honest caveat, including in
   the claim.md TITLE itself) — but both recommended tightening.
   **Response: Fixed** — reworded both the script's CONCLUSION and this
   claim.md's Core argument #6 to drop the unverified "Round 16"
   attribution and the "L4A investigation" scope-broadening, replacing
   with the narrower, accurate framing: individual per-piece values
   are now asserted (previously only printed), specifically closing
   Round 25's OWN decomposition bookkeeping.
3. **C4 mathematically forced, not independent evidence — ACCEPTED,
   labeled.** Given Round 25's own already-verified 64×64 five-piece
   identity plus linearity of `compress_2x2` plus Round 24/25's cited
   `Delta_2x2`, C4's match is forced once C1/C2 hold. claim.md already
   flagged the citation dependency (Kill Conditions, "What this does
   NOT mean") — now also explicitly labeled `[WEAKENED]` in the
   Falsifiable Claims section itself, not just in prose elsewhere.
4. **C5 trivial — ACCEPTED, labeled.** `Delta_2x2` not being scalar
   reduces to `5/2≠4/3` on hardcoded rationals — a `sympy.Rational`
   sanity check, not physics content. Retained as a numbered claim
   (both skeptics agreed this is defensible given claim.md's own
   transparent framing) but now explicitly marked `[WEAKENED — TRIVIAL]`.
5. **Citation chain for `Delta_2x2` — independently traced by the
   synthesis agent (neither skeptic went this far without Bash):** the
   synthesis agent traced `Delta_2x2=[[5/2,4/3],[4,5/2]]` back to
   `g2su3_Sminus_weitzenbock.py` (Round 24), confirmed it builds `D64`
   from scratch via `build_D_matrix64()` and computes `Delta` directly
   — NOT a copy-pasted, ungrounded number. Also independently ran Round
   25's own script fresh (exit 0) to confirm the underlying 64×64
   five-piece identity that mathematically forces C4 is itself a real,
   currently-passing computational fact.

**True kill? No** (both skeptics + synthesis agree). The core
predicate — all 5 pieces of Round 25's decomposition are now
individually, exactly known and verified — genuinely holds. What
needed fixing was rhetorical calibration, not substance.

**Overall: PROMOTE**, with C1-C3 clean `[VERIFIED-tool]`, C4/C5
explicitly labeled `[WEAKENED]` per their actual epistemic weight, and
the "milestone" framing tightened to its accurate, bounded scope.
