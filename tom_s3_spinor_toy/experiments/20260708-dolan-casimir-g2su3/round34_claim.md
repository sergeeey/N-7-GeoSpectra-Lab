---
experiment_id: 20260708-dolan-casimir-g2su3
round: 34
date: 2026-07-11
tier: Full-Ladder
status: skeptic_reviewed_promoted
parent: round32 (flagged: "RHO/NU's own construction is NOT independently
  re-derived from octonion multiplication rules or the primary-source PDF
  ... NU_BIVEC_SOURCE is a direct transcription of Round 13's
  already-established data" — restated identically in Round 33's decision.md
  as a "still open" item, unaffected by Rounds 29-33)
---

# claim.md — Round 34: RHO/NU derived from octonion multiplication via
an explicit Hadamard intertwiner

## Background

User chose this scope explicitly (of 4 offered candidates for Round 34,
recommended-but-not-chosen was "derive the specific value c=1"):
"Довывести RHO/NU из октонионных правил умножения" — derive RHO/NU from
octonion multiplication rules, closing a gap flagged since Round 32 and
carried unchanged through Round 33's own "still open" list.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — representation-theoretic equivalence,
verified computationally (exact sympy arithmetic) at every step. NOT
empirical, NOT causal.

## Core argument

1. **Cl(7,0)** (7 anticommuting generators squaring to −1), as an
   ungraded real algebra, is isomorphic to `M_8(ℝ)⊕M_8(ℝ)` — exactly
   TWO inequivalent real 8-dim irreducible Clifford modules, distinguished
   by the sign of the pseudoscalar `Ω_7` (product of all 7 generators;
   `Ω_7²=+Id` for this signature, so `Ω_7=±Id` on each summand).
2. **[VERIFIED, STEP A]** Octonion LEFT multiplication `L_1..L_7` by the
   7 Fano-plane imaginary basis units (Baez 2002's canonical
   multiplication table — identical data already used and tested in
   Round 68, `tests/test_g68_octonion_channels.py`) satisfies the exact
   `Cl(7,0)` relations and has `Ω_L = −Id` exactly.
3. **[VERIFIED, STEP B]** Round 13's `RHO[1..7]` (AHL2023 Appendix A,
   ALREADY calibrated against the paper's own trusted Remark 5.2
   `su(3)`-action, independently of this round) ALSO has `Ω_RHO = −Id`
   exactly — the SAME chirality as `L`, not `R` (octonion RIGHT
   multiplication, `Ω_R=+Id`, Round 68). Since conjugation by any
   invertible matrix fixes a central scalar matrix `±Id` exactly, this
   is a RIGOROUS proof that `RHO` can only possibly be equivalent to
   `L`, never to `R` — not a numerical coincidence, a structural fact
   about central elements.
4. **[VERIFIED, STEP C]** Solving the linear intertwiner system
   `P·L_i = RHO_i·P` for `i=1..7` SIMULTANEOUSLY (448 equations = 7
   generators × 64 entries, 64 unknown entries of `P`) gives a UNIQUE
   solution up to overall scale (1-dimensional nullspace — matching
   Schur's lemma for this irreducible 7-generator system). The
   resulting `P` has every entry in `{+1,−1}` and `P^T P = 8·Id`
   exactly — a genuine order-8 Hadamard matrix. `P·L_i = RHO_i·P` holds
   EXACTLY for ALL 7 generators — since all 7 were used simultaneously
   to solve for `P`, this exact re-check is a genuine self-consistency
   verification of `linsolve`'s own output (catches a `linsolve`
   misapplication or a masked residual), not an independent held-out
   test on generators not used in the solve.
5. **[VERIFIED, STEP D]** Since all 14 `NU_k` (the full `g2` Lie algebra
   basis, AHL2023 Remark A.2) are explicit linear combinations of
   products `RHO(a)·RHO(b)`, and conjugation by `P` is an algebra
   homomorphism, the SAME formula applied to `L(a)·L(b)` instead is
   automatically `P`-conjugate to `NU_k`. Verified DIRECTLY (not merely
   asserted from the homomorphism argument) for all 14 generators
   exactly.
6. **Conclusion:** Round 13's entire `g2` construction (`RHO` + all 14
   `NU_k`, hence the whole Phase 2 derivation chain built on it since
   Rounds 13-33) is, after the single explicit Hadamard intertwiner `P`,
   literally the canonical octonion-triality construction of
   `g2 = Der(O)` via left-multiplication bivectors on Baez's standard
   Fano-plane table — not an unrelated ad hoc Clifford-generator recipe.

## Construction (code: `g2su3_round34_octonion_derivation.py`)

**STEP A:** build `L_1..L_7` from Baez's Fano-plane octonion
multiplication table (7 triples, reimplemented locally in exact sympy —
same data as Round 68, not cross-imported, matching this experiment's
own self-contained-script convention); verify exact `Cl(7,0)` relations
and `Ω_L=−Id`.

**STEP B:** compute `Ω_RHO` (Round 13's data) and `Ω_R` (negative
control); verify `Ω_RHO=−Id=Ω_L≠Ω_R=+Id`.

**STEP C:** solve the 7-generator simultaneous linear intertwiner
system for `P`; verify 1-dim solution space, Hadamard property
(`P^T P=8·Id`, entries `±1`), and exact intertwining for all 7
generators.

**STEP D:** verify the same `P` intertwines all 14 `NU_k` against the
octonion-bivector version of the same formulas.

## Falsifiable Claims

**C1:** octonion left-multiplication `L_1..L_7` (Baez's Fano-plane
table) satisfies exact `Cl(7,0)` relations with pseudoscalar `Ω_L=−Id`.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP A);
reproduces Round 68's independently-established numeric finding, now
confirmed EXACTLY (sympy Integer arithmetic, not `np.allclose`).

**C2:** `RHO[1..7]`'s pseudoscalar is `Ω_RHO=−Id` (matches `L`, not `R`).

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP B).

**C3 (the headline result):** there exists an explicit orthogonal
(Hadamard-type) matrix `P` with `P·L_i = RHO_i·P` exactly for all
`i=1..7`.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP C):
1-dim solution space (all 7 generators used simultaneously in the
solve, 448 equations), `P` entries all `±1`, `P^T P=8·Id`, exact
intertwining re-verified for all 7 generators.

**C4:** the same `P` intertwines all 14 `NU_k` (full `g2` basis) against
the octonion-bivector version of the identical linear-combination
formulas.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP D), for
all 14 generators exactly.

## Kill Conditions

- C1 killed if: skeptic finds the Fano-plane table reimplementation here
  diverges from Round 68's own already-tested `OCT_TABLE`/`left_matrix`
  (e.g. a transcription error in `FANO_TRIPLES` or the multiplication
  table construction) — verify by direct comparison against
  `experiments/20260621-g68-octonion-channels/g68_channels.py`.
- C2 killed if: skeptic finds `RHO` (Round 13, imported unchanged) has
  been silently modified since Round 13, or the pseudoscalar computation
  itself is wrong (e.g. wrong generator ordering changing the sign).
- C3 killed if: skeptic finds the linear intertwiner system was solved
  incorrectly (e.g. `linsolve` misapplied, or the "1-dim solution space"
  claim is wrong — verify by checking `free_syms` count directly), OR
  the Hadamard/exact-intertwining verification is not actually exact
  (re-run and check for any `simplify` masking a nonzero residual).
- C4 killed if: skeptic finds the `NU_OCT_FORMULA` dict does not
  actually match Round 13's own `NU` dict formulas term-by-term (a
  transcription mismatch between the two dicts would silently produce
  a false "match" only by coincidence, not by the claimed
  homomorphism argument) — verify by diffing `NU_OCT_FORMULA`'s
  `Lprod(a,b)` argument pairs/signs against `g2su3_appendix_a_construction.py`'s
  `NU` dict's `prod(a,b)` argument pairs/signs directly, entry by entry.

## What this does NOT mean

- Does NOT prove that AHL2023's own literal "E_{a,b}" notation
  (Appendix A, still UNVERIFIED against the source PDF's actual
  definition — Round 13's own long-standing caveat) means Baez's
  SPECIFIC Fano-plane sign convention. That notational question is
  untouched, unaffected, and irrelevant to this round's claim: this
  round shows Round 13's ALREADY-CALIBRATED `RHO` (validated
  independently via Remark 5.2, not via the `E_{a,b}` guess) is
  octonion-multiplication-equivalent to the standard construction
  REGARDLESS of how that separate notational question resolves.
- Does NOT change any previously-established numeric value from Rounds
  4-33 — `P` is an orthogonal (Hadamard/√8) change of basis; every
  downstream trace, inner product, and eigenvalue used throughout this
  experiment is `P`-invariant. Purely an EXPLANATORY/GROUNDING round.
- Does NOT explain WHY the intertwiner `P` happens to be Hadamard-type
  (all entries `±1`) rather than, say, a signed permutation — that
  deeper "why" is not pursued here, matching this round's own scope
  (find and verify the concrete matrix, not explain its further
  structure).
- Does NOT resolve the preprint's `8/45 vs ~1.03` norm-ratio tension,
  the `M_p`/`Z_p` L4A convention question, or the SPECIFIC numeric value
  of Round 33's proportionality constant `c` — all remain open,
  untouched by this round.

## Skeptic Verdict (FL Step 8a — context-blind, claim.md + code only)

Two independent context-blind skeptics + a tool-verified synthesis
agent (Workflow tool, task `w7br1lam4`) reviewed this round. **Zero
FALSIFIED claims** — all four survive; one confirmed non-cosmetic
documentation defect was fixed.

| Claim | Verdict | Note |
|---|---|---|
| C1 (octonion `L` satisfies `Cl(7,0)`, `Ω_L=−Id`) | `[CONFIRMED-REAL]` | Synthesis ran a direct numeric diff of the full 8×8×8 multiplication tensor against Round 68's `g68_channels.py`: zero mismatches. Both skeptics independently hand-verified `Ω_L=−Id` (skeptic 2 traced `Ω_L(e_0)` by hand through all 7 left-multiplications and got `−e_0`). Cosmetic labeling nit: the relations used here (`L_i²=−Id`) are "Cl(0,7)" in the Lawson-Michelsohn textbook convention rather than "Cl(7,0)" — **dismissed, not fixed**: Round 68 (the source this round reuses) already established "Cl(7,0)" as this project's own internal convention throughout, so keeping it matches project-internal consistency over one external textbook's labeling; the structural claim (`M₈(ℝ)⊕M₈(ℝ)`) is identical either way. |
| C2 (`Ω_RHO=−Id`, matches `L` not `R`) | `[CONFIRMED-REAL]`, unconditional | Both skeptics initially noted they could only confirm this "contingent on the assert firing cleanly" (their sandboxes had no Bash tool). Synthesis ran the script to completion (`exit 0`, zero `AssertionError`s across all 8 in-script checks), converting this to an unconditional verified fact. |
| C3 (explicit Hadamard intertwiner `P`, `P·L_i=RHO_i·P` for all 7) | `[CONFIRMED-REAL]` (math), **one real documentation defect found and fixed** | Both skeptics + synthesis independently caught the same defect: claim.md and the script both stated "128 equations" and "not just the 2 used to solve for P" — but the code actually builds all 7 generators' constraints simultaneously (448 equations = 7×64), never a 2-then-5 split. **Fixed**: claim.md's Core-argument point 4, its C3 RESULT text, the script's docstring, and its print statement all corrected to state 448 equations and clarify the 7-generator re-check is a `linsolve`-output self-consistency verification, not an independent held-out test. The underlying MATH (1-dim solution space, Hadamard property, exact intertwining) was never in question — only the process-description was wrong. |
| C4 (same `P` intertwines all 14 `NU_k`) | `[CONFIRMED-REAL]` | Both skeptics independently hand-diffed all 14 `NU_OCT_FORMULA` entries against Round 13's `NU` dict, term-by-term and sign-by-sign — exact match, no transcription bug. Both skeptics and the synthesis agent correctly note C4 is an automatic algebraic consequence of C3 + exact-transcription (not independent evidence) — already self-acknowledged in the script's own docstring, not an overclaim. |

**Beyond both skeptics — synthesis's independent Cayley-Dickson cross-check:** the synthesis agent built octonion multiplication from scratch via Cayley-Dickson doubling of Hamilton quaternions (a genuinely different construction from Baez's Fano-plane table, not a relabeling). The resulting left-multiplication matrices `L2_i` ALSO satisfy `Cl(7,0)` exactly with `Ω_L2=−Id` matching `Ω_RHO` (not automatic — a different quaternion-doubling sign choice could have flipped the chirality) — confirming that *existence* of an orthogonal intertwiner between octonion left-multiplication and `RHO` is convention-independent, essentially forced by chirality-matching plus Schur's lemma. However, the intertwiner `P2` found this way is **NOT Hadamard** (only 32 of 64 entries nonzero, values in `{0,+1,−1}`, `P2^T P2=4·Id`) — meaning THIS round's specific dense, all-`±1` Hadamard property of `P` is a coincidence of how Baez's specific Fano labeling happens to align with Round 13's `Emat` convention, not a universal structural fact. This independently substantiates claim.md's own pre-existing caveat ("Does NOT explain WHY the intertwiner `P` happens to be Hadamard-type") as correctly scoped, not just cautious hand-waving.

**Pearl candidate** (falsifiable, worth a `pearl_registry/INDEX.md` entry): *observation* — the mere existence of an orthogonal Cl(7,0) intertwiner between any two octonion-multiplication-derived Clifford representations of matching chirality appears to be convention-independent (forced by Schur), but the intertwiner's SPARSITY/Hadamard-ness is convention-dependent; *falsifiable prediction* — trying a third, different octonion multiplication convention (e.g. a different Fano-triple ordering/labeling) against `RHO` will produce yet another valid intertwiner, generically NOT Hadamard, confirming the Hadamard property found in THIS round is non-generic; *trigger* — if a future round needs a third independent octonion-based construction for any reason; *next_check* — no specific date, opportunistic.

**Decision: PROMOTE.** All 4 falsifiable claims (C1-C4) survive; the one
real finding (C3's process-description) was fixed, not a retraction.

**Out-of-scope item flagged, not fixed here:** both skeptics and the
synthesis agent independently noticed `g68_channels.py`'s own docstring
header (lines 6-7) states `Ω_L=+I₈, Ω_R=−I₈`, contradicting its own
inline verification comment and actual computed values (`Ω_L=−I₈,
Ω_R=+I₈`) — a pre-existing bug in a DIFFERENT experiment's file, not
introduced by this round. Left untouched per scope discipline; flagged
separately as a spawn-task candidate.
