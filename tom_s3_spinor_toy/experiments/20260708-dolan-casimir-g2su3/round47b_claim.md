---
experiment_id: 20260708-dolan-casimir-g2su3
round: 47b
date: 2026-07-13
tier: Full-Ladder
status: skeptic_reviewed_promoted
parent: round47a (mandatory Prior Result Gate, created after Round 46's
  duplicate rediscovery); this round is the FIRST to be run through the
  gate before writing anything, per the user's own P1 priority pick —
  the RHO/NU literal AHL2023 notation question (Round 13, long-standing,
  carried unresolved through Rounds 32-38)
---

# claim.md — Round 47B: AHL2023's literal `E_{a,b}` notation, verified —
Round 13's `RHO`/`NU` construction matches the paper exactly (notational
cleanup, not a new theorem)

## Prior Result Gate (run BEFORE writing this claim, per `PRIOR_RESULT_GATE.md`)

1. **Exact claim:** Does AHL2023's own literal `E_{a,b}` notation match
   the antisymmetric elementary matrix Round 13 ASSUMED (never
   verified against the primary source's own text), and does Round
   13's `RHO`/`NU` construction (`g2su3_appendix_a_construction.py`)
   match the paper's own verbatim Appendix A formulas, for all 14
   generators?
2. `decision.md`: literal string `"E_{a,b}"` appears from Round 34
   onward (`git log -S` confirms the code-file docstring origin at
   Round 13, commit `d60e838`); Rounds 32/33 discuss the SAME
   substantive gap in different wording ("`RHO`/`NU`'s own
   construction remains not independently re-derived from octonion
   multiplication rules or the primary-source PDF" — confirmed by
   reading those sections directly, not a literal grep match). Round
   34 explicitly left this SPECIFIC sub-question untouched ("does NOT
   prove AHL2023's own literal E_{a,b} notation... means Baez's
   specific Fano sign convention"). Confirmed still open.
3. `round*_claim.md` + scripts grep: no script previously attempted a
   direct literal-text verification (Round 13's own construction only
   ever calibrated INDIRECTLY, against Remark 5.2's trusted `ad(nu_i)
   (e_p)` action).
4. `null_results/`/`parked/` grep: zero hits — never rejected/parked.
5. `git log -S "E_{a,b}"`: shows this caveat carried, uncorrected,
   from Round 13 (commit `d60e838`) through Round 38 — confirms
   genuinely long-standing, never resolved.
6. Primary source re-read: performed THIS round (two targeted research
   agent PDF reads, independently cross-checked against the code below)
   — this IS the round's own task.
7. **Status: OPEN.** Proceeding.

## Background

Round 13's own code (`g2su3_appendix_a_construction.py`) carries this
unresolved caveat since 2026-07-09: `"E_{a,b}" convention: NOT verified
in the paper's text (OCR gives no explicit definition on this page) --
assumed to be the standard ANTISYMMETRIC elementary matrix... THIS
ASSUMPTION IS CALIBRATED BELOW before being trusted`. The downstream
calibration (against Remark 5.2's trusted `ad(nu_i)(e_p)` action)
passed for all 48 `(i,p)` pairs, giving indirect confidence — but the
paper's own literal definition of `E_{a,b}` was never directly read.
Round 34 (2026-07-12) built an explicit octonion↔`RHO` intertwiner but
explicitly left THIS specific sub-question untouched.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — a primary-source textual verification
(what does a specific notation mean in a specific paper) plus a direct
operator-identity check (does the code match the paper's own formulas
exactly), both falsifiable via re-reading and re-computation.

## Core argument

1. **[VERIFIED-tool, upgraded post-skeptic]** AHL2023 (Agricola-
   Hofmann-Lawn 2023) DOES explicitly define `E^(n)_{i,j}` — page 8,
   §2.2 "Spinors on Homogeneous Spaces" (heading appears p.7, section
   spans pp.7-9, no new heading interrupts p.8 — independently
   confirmed via rendered page images during skeptic review, resolving
   an initial skeptic disagreement about the subsection number) — the
   paper's own words: "Let us now fix notation related to matrix Lie
   algebras. We will use `E^(n)_{i,j}`... throughout to denote the
   elementary skew-symmetric n×n matrix" — general notation, NOT local
   to Appendix A, as the skew-symmetric elementary matrix with `-1` at
   `(i,j)`, `+1` at `(j,i)`. Round 13's own "OCR gives no explicit
   definition" claim was a FALSE NEGATIVE, caused by looking only
   within Appendix A itself rather than the paper's general-notation
   section.
2. **[VERIFIED]** Round 13's own `Emat(a,b)` (`+1` at `(a,b)`, `-1` at
   `(b,a)`) is the OPPOSITE overall sign from the paper's own
   `E^(n)_{i,j}`.
3. **[VERIFIED]** This sign difference flips every individual
   `ρ(ε_i)`, `i=1..7` (`code_ρ(i) = -paper_ρ(i)`, confirmed directly,
   not just argued) — but since every `ν_k` (`k=1..14`, Proposition
   A.3) is built ENTIRELY from PRODUCTS `ρ(ε_i)·ρ(ε_j)`, never a bare
   `ρ(ε_i)` alone, `(-A)(-B)=AB` makes this sign convention PROVABLY
   INVISIBLE to every `ν_k` — a structural consequence of `ν_k`'s own
   quadratic form, not a lucky coincidence.
4. **[VERIFIED, the actual test]** Building the paper's own `E^(n)_
   {i,j}`, `ρ(ε_i)` (Remark A.2, page 49), and `ν_k` (Proposition A.3,
   page 49) FRESH — independently, not imported from Round 13's own
   code — and comparing to Round 13's own `RHO`/`NU`: ALL 14 `ν_k`
   match EXACTLY, term-by-term.
5. **[VERIFIED, negative control]** A deliberately-corrupted `ν_5`
   (flipping one sign) is correctly flagged as different — confirms
   the comparison methodology actually discriminates.
6. **Conclusion:** this is a NOTATIONAL CLEANUP, not a new theorem.
   Round 13's construction was ALREADY mathematically correct (the
   indirect calibration was not masking an error); what was missing
   was the literal primary-source citation proving it directly,
   replacing an indirect (calibration-only) justification with a
   direct one, per the user's own acceptance criteria.

## Paper symbol → project object table

| Paper symbol (AHL2023) | Page | Project object | File |
|---|---|---|---|
| `E^(n)_{i,j}` (skew-symmetric elementary matrix, `-1` at `(i,j)`, `+1` at `(j,i)`) | p.8, §2.2 | `Emat(a,b)` — SAME structure, OPPOSITE overall sign (`+1`/`-1` swapped) | `g2su3_appendix_a_construction.py` |
| `ρ(ε_1)..ρ(ε_7)` | p.49, Remark A.2 | `RHO[1]..RHO[7]` — equal to `-paper_ρ(i)` (sign-flipped, harmless — see Core argument #3) | same |
| `ν_1..ν_14` (`ν_1..ν_8`=su(3), `ν_9..ν_14`=m) | p.49, Prop A.3 | `NU[1]..NU[14]` — EXACT match, no sign difference at all | same |

## Construction (code:
`g2su3_round47b_rho_nu_notation_audit.py`)

STEP 1+3: verify `code_ρ(i) = -paper_ρ(i)` for all `i=1..7` (built
fresh, `PAPER_RHO`, using the paper's own `E` convention). STEP 4:
compare all 14 `NU[k]` against a fresh `PAPER_NU[k]` (Proposition A.3,
independently built). STEP 5: negative control (deliberately-corrupted
`ν_5`).

## Falsifiable Claims

**C1:** AHL2023 p.8 defines `E^(n)_{i,j}` explicitly (skew-symmetric,
`-1`/`+1`). RESULT: `[VERIFIED]` (research agent direct PDF read,
independently cross-checked against the code's own downstream behavior
in C3).

**C2:** `code_ρ(i) = -paper_ρ(i)` for all `i=1..7`. RESULT:
`[VERIFIED-tool]` (STEP 1+3).

**C3 (the actual test):** all 14 `ν_k` (code vs. independently-rebuilt
paper formula) match exactly. RESULT: `[VERIFIED-tool]` (STEP 4).

**C4 (negative control):** a deliberately-wrong `ν_5` is correctly
flagged as different. RESULT: `[VERIFIED-tool]` (STEP 5).

## Kill Conditions

- C1 killed if: re-reading AHL2023 page 8 finds a different
  definition, or finds it's NOT actually general/used throughout —
  straightforward to re-check by reading the PDF directly.
- C2/C3 killed if: re-computation finds ANY of the 7 `ρ(ε_i)` or 14
  `ν_k` differing — this is the actual falsifiable content.
- C4 killed if: the corrupted `ν_5` is NOT flagged as different (would
  mean the comparison methodology is broken).
- **Overarching kill condition:** if this is read as claiming to
  resolve anything BEYOND the literal notation/citation question — no
  new physics, no new operator identity beyond what Round 13 already
  established (indirectly) 45 rounds ago.

## What this does NOT mean

- **Does NOT change any previously-established spectrum, index,
  eigenvalue, or curvature value from Rounds 13-46** — Round 13's own
  `RHO`/`NU`/`curvature_h` construction was ALREADY correct; this round
  replaces an indirect justification with a direct primary-source
  citation, it does not recompute anything downstream.
- **Does NOT resolve the L4A tension** (parked) or the Casimir_su3-
  vs-Jac_h question (already closed by Round 30, per Round 46's own
  correction) — both untouched.
- **Does NOT prove the paper's own choice of `E^(n)_{i,j}` sign
  convention is "the" universally correct one** — it's a citation of
  what AHL2023 itself uses; Round 13's own opposite-sign `Emat` is
  equally valid as an independent convention, shown here to be
  harmless for every downstream `ν_k`.
- **Does NOT touch `preprint.tex`.**
- **Concrete next step, NOT started:** update
  `g2su3_appendix_a_construction.py`'s own docstring to replace the
  stale "NOT verified... OCR gives no explicit definition" caveat with
  a direct citation (page 8 + page 49), per this round's own findings
  — this IS the deliverable, done immediately after skeptic review.

## Skeptic Verdict (FL Step 8a)

Two context-blind skeptics + a synthesis agent, all reading the
primary source PDF THEMSELVES (not trusting this round's own
transcriptions), independently re-verified every one of the 14 `ν_k`
formulas (not spot-checking) against rendered page images.

| Claim | Skeptic 1 | Skeptic 2 | Synthesis (independent 3rd read) |
|---|---|---|---|
| C1 | WEAKENED (disputed "§2.2" citation) | WEAKENED (same dispute, opposite conclusion — says §2.2 IS correct) | **CONFIRMED-REAL — resolved the disagreement via rendered page images: Skeptic 1's "no §2.2 heading on p.8" was itself wrong (heading appears p.7, section spans pp.7-9, not reprinted per-page); Skeptic 2 and the citation were correct** |
| C2 | CONFIRMED-REAL | CONFIRMED-REAL | CONFIRMED-REAL |
| C3 | CONFIRMED-REAL (all 14 checked against PDF image, not spot-checked) | CONFIRMED-REAL (same, independently) | CONFIRMED-REAL — additionally did a pixel-level re-check of `ν_8` specifically (Round 13's own docstring flags this term's history of misreadings), catching and resolving a false alarm in synthesis's own first-pass text extraction before confirming no discrepancy |
| C4 | CONFIRMED-REAL | CONFIRMED-REAL | CONFIRMED-REAL |

**No claim FALSIFIED.** Both skeptics independently found the SAME two
minor precision issues (one true — the Prior Result Gate's step 2
overstated grep precision on Rounds 32/33; one FALSE — the "§2.2"
citation, which skeptic 1 flagged as wrong and skeptic 2 flagged as
correct). The synthesis agent resolved this internal disagreement
directly, by rendering the actual PDF pages as images rather than
trusting either skeptic's text-extraction method — confirming §2.2
IS the correct citation (LaTeX section headings are not reprinted on
every page they span, which is what caused skeptic 1's false negative).

**Response: Fixed, not dismissed.** Applied both confirmed fixes: (1)
Core argument #1 now quotes the paper's own actual words rather than a
paraphrase presented as verbatim, and cites the independently-resolved
§2.2 citation with its own resolution history; (2) the Prior Result
Gate's step 2 now precisely distinguishes the literal `"E_{a,b}"`
string hit (Round 34 onward) from the substantively-real-but-
differently-worded gap discussed in Rounds 32/33.

**What survives, solid:** the round's actual mathematical deliverable
— all 14 `ν_k` (not a subset) independently rebuilt from the primary
source and matching Round 13's 45-round-old code exactly — is
unanimous, `[CONFIRMED-REAL]` across all three reviewers, with the
synthesis agent's own extra pixel-level check of the historically-
ambiguous `ν_8` term providing stronger-than-required confirmation.

**True kill? No** (unanimous). **Overall: PROMOTE**, all four claims
`[CONFIRMED-REAL]`, two citation-precision fixes applied, zero
mathematical content changed.
