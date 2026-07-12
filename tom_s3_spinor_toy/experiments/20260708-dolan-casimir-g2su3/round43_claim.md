---
experiment_id: 20260708-dolan-casimir-g2su3
round: 43
date: 2026-07-12
tier: Full-Ladder
status: skeptic_reviewed_promoted
parent: round42 (M_p-vs-Z_p aggregate-only shift, explicitly incomplete,
  named "read AHL2023's Example 4.18" as the concrete next step); this
  round pursued that next step, found a research dead end honestly, and
  turned that dead end into a general, connection-independent NO-GO
  theorem instead
---

# claim.md — Round 43: a general chirality/grading NO-GO theorem —
no bivector-type Z_p (of any connection) can satisfy Round 26's own
identity

## Background

Round 42 named a concrete next step: read AHL2023's own "Example 4.18"
to find an explicit per-index canonical-connection spin-lift formula for
`S^6`. A research agent dispatch found Example 4.18 (pp.27-28) is
actually about **S^7=Sp(2)/Sp(1)**, not S^6, describing an unrelated
spinor-kernel-intersection method — a genuine near-miss, honestly
reported. The agent kept searching and found **Proposition 5.4 (p.43)**:
the explicit Ambrose-Singer torsion 3-form for S^6=G2/SU(3) itself,
`T^AS = (1/√3)(-e_{1,3,6}-e_{1,4,5}-e_{2,3,5}+e_{2,4,6})`.

**Before acting on this** (per this project's own
`audit-verification-gate.md`: "agent's `[VERIFIED]` = your `[INFERRED]`"),
a hand-derivation was attempted: computing `e_i⌟T^AS` for i=1..6 gives
exactly `-2·Λ^g(e_i)` for all six generators (a clean, exact match, no
residual). Combined with the standard skew-torsion identity
`Λ^AS(e_i)=Λ^g(e_i)-(1/2)(e_i⌟T^AS)`, this gives either `Λ^AS=2Λ^g`
or `Λ^AS=0` depending on an unresolved sign convention — and testing
BOTH against Round 26's own `Delta_HCas` identity showed **neither can
possibly work**: any pure rescaling `Z_p := c·M_p` (for ANY constant c,
including c=0 or c=2) produces `Σ Z_p² = c²·Σ M_p²`, which — since
`Σ M_p² = -(1/2)Id+(1/4)Casimir_su3` in closed form (Round 39) — can
NEVER contain an H-dependent term for any c, because H is a genuinely
different (cubic Clifford) object.

This generalizes: the reason is not specific to rescaling, but to the
underlying grading structure of the spinor representation. This round
proves the general statement directly.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — an exact, general algebraic/representation-
theoretic argument, computationally verified on the actual 8-dim
Spin(6) spinor representation used throughout this project. NOT
empirical, NOT causal.

## Core argument

1. **[VERIFIED]** In the 8-dim spinor rep (subsets of `{1,2,3}` encoding
   Spin(6)=SU(4)'s `Δ_6`, even-occupation = `S^+`, odd-occupation =
   `S^-`), `H` (Kostant's cubic element) has its ONLY nonzero entries at
   `(0,7)` and `(7,0)` — strictly chirality-OFF-diagonal (`S^+ ↔ S^-`).
2. **[VERIFIED]** Each individual `M_p` (p=1..6, this project's own
   Levi-Civita spin connection) is chirality-BLOCK-diagonal (`S^+→S^+`,
   `S^-→S^-`), and so are `Casimir_su3` and `Id8`.
3. **[VERIFIED, general lemma]** This is NOT special to Levi-Civita's
   own coefficients: 5 independent RANDOM bivector combinations (not
   metric-compatible, not claimed to be any meaningful connection) are
   ALL chirality-block-diagonal, and so are their squares. This
   confirms block-diagonality is a structural fact about "built from an
   even number of Clifford vector actions" — true of ANY so(6)-valued
   spin connection (Levi-Civita, Agricola's canonical `t=0`, any other
   `t`, or literally any other bivector-valued 1-form).
4. **[VERIFIED]** `Delta_HCas := H-(1/2)·Id-(7/4)·Casimir_su3` (Round
   26's own target) is chirality-off-diagonal with support EXACTLY
   `{(0,7),(7,0)}` — identical to H's own support, confirming Id and
   Casimir_su3 contribute nothing off-diagonal.
5. **Conclusion (general, not ansatz-specific):** chirality-block-
   diagonal matrices are closed under sums and products. So for ANY
   bivector-type `Z_p` (any connection whatsoever), `Σ_p Z_p²` is
   block-diagonal, and can never equal anything with H's unavoidable
   off-diagonal content. **Round 26's own implicitly-defined `-Σ Z_p²`
   (defined purely by subtraction from `Dslash_mat²`, never built as an
   actual per-index operator — confirmed by re-reading
   `g2su3_round26_jach_derivation.py` this round) cannot be the
   spin-lift of ANY connection's Nomizu map.** This rules out the
   entire "find the right connection" program (Rounds 26/41/42) at
   once, for a general structural reason — not one more falsified
   ansatz.

## Construction (code: `g2su3_round43_chirality_no_go.py`)

**STEP 1:** confirm `H`'s support is exactly `{(0,7),(7,0)}`.
**STEP 2:** confirm `Casimir_su3`, `Id8` are block-diagonal.
**STEP 3:** confirm each `M_p` (p=1..6) is block-diagonal.
**STEP 4:** confirm 5 random bivector combinations (and their squares)
are block-diagonal — the general lemma, not Levi-Civita-specific.
**STEP 5:** confirm `Delta_HCas`'s off-diagonal support matches H's own
exactly.

## Falsifiable Claims

**C1:** H's only nonzero entries are at `(0,7)`/`(7,0)`. RESULT:
`[VERIFIED-tool]` (STEP 1).

**C2:** `Casimir_su3`, `Id8`, and each `M_p` (p=1..6) are chirality-
block-diagonal. RESULT: `[VERIFIED-tool]` (STEP 2, 3).

**C3:** 5 independent random bivector combinations (non-Levi-Civita,
non-metric) are ALL block-diagonal, and their squares too. RESULT:
`[VERIFIED-tool]` (STEP 4) — confirms the property is general, not an
artifact of Levi-Civita's specific coefficients. **[POST-SKEPTIC
STRENGTHENING]** both skeptics + synthesis independently proved this is
actually a stronger, unconditional fact than "5 samples happened to
pass": `e_action(i,·)` is a strict occupation-number ladder operator —
every single basis state maps to exactly one output state at level
shift ±1 (never a superposition of both), confirmed exhaustively
(48/48 cases, one skeptic; 120/120, the other). The synthesis agent
went further and ran a **fully symbolic** check — 15 independent
symbolic (complex-valued) bivector coefficients spanning the entire
coefficient space at once, not samples — confirming 0 off-block
entries unconditionally. This means block-diagonality cannot fail for
ANY coefficient choice; the "5 random probes" framing in Step 4
understates what is actually a deterministic combinatorial certainty,
not a property that merely survived sampling.

**C4:** `Delta_HCas`'s off-diagonal support equals exactly `{(0,7),
(7,0)}` (H's own support, no cancellation from Id/Casimir_su3). RESULT:
`[VERIFIED-tool]` (STEP 5).

**C5 (the theorem):** no bivector-type `Z_p` (any connection) can
satisfy `(-Σ Z_p²)-(-Σ M_p²) = Delta_HCas`. RESULT: `[VERIFIED]` as a
direct logical consequence of C1-C4 (closure of block-diagonal matrices
under sum/product is a standard linear-algebra fact, not separately
computationally checked beyond C3's direct instances).

## Kill Conditions

- C1/C2/C4 killed if: re-computation finds different nonzero-entry
  patterns — straightforward direct check.
- C3 killed if: any of the 5 random bivector probes (or their squares)
  turns out NOT block-diagonal — would falsify the general lemma and
  reduce this to "true for Levi-Civita specifically, not proven general".
- C5 killed if: the closure argument itself is wrong (e.g. if
  chirality-block-diagonal matrices were NOT closed under sum/product —
  this is standard and not in genuine doubt, but flagged for skeptic
  review since C5 is not itself a separate computational check).
- **Overarching kill condition:** if this is found to overclaim beyond
  "bivector-type Z_p is impossible" — e.g. if it is read as resolving
  what Agricola's own `Z_i` notation means, or as resolving the L4A
  `8/45 vs ~1.03` tension — this would be a genuine overclaim requiring
  a fix.

## What this does NOT mean

- **Does NOT identify what Agricola's own `Z_i` in `D^t = Σ_i
  Z_i·Z_i(ψ) + t·H·ψ` actually denotes.** The natural reading — not
  verified here, flagged as the next avenue — is that `Z_i·Z_i(ψ)` is
  shorthand for a compound first-order object (`e_i · ∇^t_{e_i}ψ`, a
  genuine per-direction Dirac-operator building block), which IS
  chirality-odd (like a single Clifford vector) and so COULD carry
  H-type content — consistent with this project's own `D^0=-H` (Round
  27). This reinterpretation is speculative and UNTESTED here.
- **Does NOT resolve the L4A `8/45 vs ~1.03` norm-bound tension** — that
  remains completely open regardless of this result.
- **Does NOT mean AHL2023's Proposition 5.4 was wasted effort** — it
  directly motivated the hand-derivation that led to testing (and
  ruling out) the `Z_p = c·M_p` rescaling family, which in turn
  motivated asking the GENERAL question this round answers. The
  specific `e_i⌟T^AS = -2Λ^g(e_i)` relationship is NOT used in the
  final proof (which is connection-independent) and its own sign
  convention was NEVER independently resolved — left open, now moot for
  this round's purposes since ANY sign choice is covered by the general
  theorem.
- **Does NOT touch `preprint.tex`.**
- **Does NOT resolve** the Casimir_su3-vs-Jac_h identity question
  (Round 39), `RHO`/`NU`'s literal AHL2023 notation question, or WHY
  Round 34's intertwiner `P` is Hadamard-type — all remain untouched.
- **[POST-SKEPTIC ADDITION] Does NOT make any claim about Standard
  Model fermion chirality (SU(2)_L/R gauge sectors, per this project's
  own G23/G74B).** "Chirality" in this round is the standard Clifford-
  module `S^+`/`S^-` grading of `Δ_6` (occupation-number parity of the
  8-dim spinor representation) — an internal mathematical grading of
  this specific representation, unrelated to physical fermion
  handedness. Flagged by the synthesis agent as cheap insurance against
  a future reader conflating this round's title with the SM chirality
  question this project's own memory (`g23-chirality-2026-06-19.md`)
  already settled as a separate matter.
- **Concrete next step, NOT started:** independently verify (via
  direct re-reading of Agricola 2002's own primary-source definition)
  what `Z_i` denotes in her own Dirac-operator formula — testing the
  "compound Dirac-building-block" hypothesis above directly, rather
  than continuing to search for a per-index bivector connection
  operator that this round shows cannot exist.

## Skeptic Verdict (FL Step 8a)

Two context-blind skeptics (Read/Bash, no session history) + a
tool-using synthesis agent independently reviewed this round via direct
file reads AND direct execution of `g2su3_round43_chirality_no_go.py`
and `g2su3_round26_jach_derivation.py`, plus independent adversarial
code neither the claim nor the script supplied.

| Claim | Skeptic 1 | Skeptic 2 | Synthesis (independent re-derivation) |
|---|---|---|---|
| C1 | CONFIRMED-REAL | CONFIRMED-REAL | CONFIRMED-REAL |
| C2 | CONFIRMED-REAL | CONFIRMED-REAL (+ exhaustive 120/120 ladder-operator proof) | CONFIRMED-REAL (+ independent 48/48 exhaustive proof) |
| C3 | CONFIRMED-REAL (+ complex/irrational coefficient probes) | CONFIRMED-REAL, methodological caveat: "5 random probes" undersells a deterministic certainty | CONFIRMED-REAL, strengthened via fully symbolic (15 free complex symbols) proof spanning the entire coefficient space |
| C4 | CONFIRMED-REAL | CONFIRMED-REAL | CONFIRMED-REAL |
| C5 (theorem) | CONFIRMED-REAL (verified closure concretely, e.g. `M_1*B`, `H*M_1` correctly flagged) | CONFIRMED-REAL (generic symbolic closure proof on the actual 4+4 partition; explicitly checked and ruled out complex Z_p, larger/different spaces, non-metric connections, full Agricola t-family) | CONFIRMED-REAL (re-derived the full logical chain from Round 26's own run output, symbolic closure proof) |

**No FALSIFIED claims. No counterexample or logical gap found by either
skeptic or the synthesis agent**, despite specifically hunting for one
(individual generators, complex/irrational coefficients, extreme
magnitudes, negative controls verifying the detector itself is
sensitive, and an explicit search for escape routes — complex-valued
Z_p, Z_p on a different space, non-metric connections, the full
Agricola t-family — all checked and ruled out).

**Overclaim check: none found.** All three reviewers independently
confirmed the "What this does NOT mean" section is honestly scoped and
the prose never oversteps it — in particular, none of the L4A tension,
Agricola's `Z_i` meaning, or `preprint.tex` are touched, matching the
claim's own disclaimers.

**Two required, non-mathematical fixes identified (both applied
above, not dismissed):**
1. **Frontmatter/body inconsistency**, independently caught by both
   skeptics and confirmed by the synthesis agent via `git status`
   (script/claim were untracked — no review had occurred yet): this
   document's frontmatter declared `status: skeptic_reviewed_promoted`
   while this very section was still an unfilled placeholder. Fixed by
   this edit (the status is now actually earned).
2. **C3's "5 random probes" framing understated the actual strength of
   the result** (both skeptics independently flagged this as a
   "presentation nitpick" / "methodological caveat", the synthesis
   agent supplied the fully symbolic proof that justifies stronger
   wording). Fixed — see C3's updated text above.

**One additional finding, applied (not part of either skeptic's core
mandate, raised by the synthesis agent):** this round's "chirality"
(Clifford-module `S^+`/`S^-` occupation-parity grading) is unrelated to
physical SM fermion chirality (`SU(2)_L/R`), which this project's own
G23/G74B already established via a separate mechanism. Added a
disambiguating line to "What this does NOT mean" as cheap insurance
against future symbol/term reuse confusion (an explicitly named risk
class in this project's own `research-methodology.md` §
Классификатор, Тип 1).

**True kill? No** (all three reviewers agree). Core predicate — the
general, connection-independent chirality no-go theorem — holds
exactly as stated, and was independently re-derived (not merely
re-checked) by two separate reviewers using different methods
(exhaustive numeric sweep; fully symbolic proof).

**Overall: PROMOTE**, all five claims `[CONFIRMED-REAL]`, no `[WEAK]`
or `[HYPOTHESIS]` markers needed — this round's argument is
representation-theoretic and general, not an empirical/ansatz-specific
finding like Rounds 41-42.
