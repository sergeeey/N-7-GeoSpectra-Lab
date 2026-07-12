---
experiment_id: 20260708-dolan-casimir-g2su3
round: 36
date: 2026-07-12
tier: Full-Ladder
status: skeptic_reviewed_promoted
parent: round35 (explicitly flagged, "What this does NOT mean": "Does
  NOT derive Jm4's own d=2 from a deeper principle... same 3×3-solve-
  and-read-off method", and "degree4_term's c'=-5/4 is RELOCATED, not
  reduced in solve-count -- the SAME combinatorial 3×3 solve is still
  performed... only relocated")
---

# claim.md — Round 36: the Jacobi identity fully closes Jm4/degree4_term
(no solve needed at all)

## Background

User chose this scope explicitly (of 4 offered candidates for Round 36,
the recommended option): "Вывести Jm4's d=2 структурно" — derive `Jm4`'s
own coefficient `d=2` from a deeper principle, the exact gap Round 35
explicitly left open.

**Attribution correction (post-skeptic, IMPORTANT — read before
trusting any "fresh discovery" framing below):** the identity this
round centers on (`jac_h=-jac_m`) is Agricola 2002's OWN theorem
(Section 2, pages 5-6, in the proof leading to Lemma 2.3), NOT a fresh
discovery of this round. It was ALREADY found, quoted from the primary
source, and USED in this exact project on 2026-07-09 —
`g2su3_delta_correction.py` (predating Round 26 by two days) builds a
general `quartic_term(t)` formula directly via `H²` using this
identity, and `decision.md` (~line 525-560, "Round 6") documents the
citation plus a non-trivial cross-check (`Delta(1/3)=0` exactly,
64/64 entries). The synthesis agent (FL Step 8a review, task
`wji4ntu3g`) caught that Rounds 26/33/35 each independently rebuilt
`Ch_4`/`degree4_term`/`Jm4` via harder combinatorial routes without
ever connecting back to this already-on-record shortcut — a genuine
methodology lag, not a math error. What THIS round genuinely
contributes: (a) an independent re-derivation of the identical
identity via a cleaner, more explicit direct-sum argument (matching
Agricola's own terser mechanism); (b) the FIRST application of it
specifically to `Ch_4`/`Jm4`/`degree4_term` as named, separate matrix
objects (Round 26's own introduction, which `g2su3_delta_correction.py`
predates and never named).

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — an elementary Lie-algebra identity, verified
computationally at every step. NOT empirical, NOT causal.

## Core argument

1. **[VERIFIED, STEP A]** `jac_h(j,k,l) + jac_m(j,k,l) = 0` EXACTLY, for
   ALL `C(6,3)=20` ordered triples in `1..6` (and all 120 permutations,
   as a sanity check on the fully-antisymmetric Jacobiator structure).
2. **Abstract argument (re-derivation, matching Agricola's own
   mechanism):** for `X,Y,Z ∈ m`, the AMBIENT Lie algebra `g = h⊕m`'s
   own Jacobi identity (an axiom) gives
   `0 = Σ_cyc [X,[Y,Z]] = Σ_cyc [X,[Y,Z]_h] + Σ_cyc [X,[Y,Z]_m]`.
   `[X,[Y,Z]_h]` lies ENTIRELY in `m` (reductivity `[h,m]⊆m`, already
   established since Round 12/13), so `Σ_cyc [X,[Y,Z]_h] = jac_h(X,Y,Z)`
   exactly. `[X,[Y,Z]_m]` can have BOTH an `m`-part and an `h`-part in
   general (this coset is reductive but NOT symmetric — precisely the
   nonzero-torsion/nearly-Kähler feature of `S⁶=G₂/SU(3)`); write the
   `m`-part as `β(X,Y,Z)` and the `h`-part as `γ(X,Y,Z)`. Since
   `g=h⊕m` is a DIRECT SUM, the total zero vector `jac_h+β+γ=0` splits
   into TWO SEPARATE zero-equations: `γ`-sum`=0` (a bonus fact, unused
   further) AND `jac_h+β=0`. Since `β(X,Y,Z)` IS Round 26's own
   `jac_m(X,Y,Z)` (`m_bracket` used twice, exactly the `m`-part of
   `[X,[Y,Z]_m]` by construction) — this gives `jac_h+jac_m=0` DIRECTLY.
   No canonical-connection Bianchi identity or "torsion is parallel"
   theorem is invoked — this is strictly more elementary (a pure
   vector-space decomposition of ONE Lie-algebra axiom).
3. **[VERIFIED, STEP B]** By LINEARITY of `build_quartic_matrix`
   (already established/used since Round 26): `Jm4 = 2·Ch_4` EXACTLY —
   a direct matrix identity, no 3×3 solve.
4. **[VERIFIED, STEP C]** Similarly: `degree4_term = −5/4·Ch_4` EXACTLY
   — a direct matrix identity, no 3×3 solve.
5. **[VERIFIED, STEP D]** Combined with Round 35's OWN
   `Ch_4=Casimir_su3−Id` (`c=1`, cited unchanged, itself a logical
   consequence of Round 30's structural chain, NOT re-derived here):
   `Jm4=2·(Casimir_su3−Id)` (`d=2`, matches Round 35 exactly) and
   `degree4_term=−5/4·(Casimir_su3−Id)` (matches Rounds 26/31/33/35
   exactly).
6. **Conclusion:** Round 35's "RELOCATED, not reduced" framing for
   `degree4_term` is SUPERSEDED — there is no longer ANY separate 3×3
   combinatorial solve needed for `Jm4` or `degree4_term` at all. Round
   33's original 3×3-solve route to `degree4_term`'s `c'=-5/4` remains
   VALID (an independent cross-check, both giving the identical value)
   but is no longer NECESSARY.

## Construction (code: `g2su3_round36_jacobi_identity_closure.py`)

**STEP A:** verify `jac_h+jac_m=0` exactly for all 20 ordered triples
and all 120 permutations.

**STEP B:** verify `Jm4=2·Ch_4` exactly (direct linearity consequence).

**STEP C:** verify `degree4_term=−5/4·Ch_4` exactly (direct linearity
consequence).

**STEP D:** combine with Round 35's `Ch_4=Casimir_su3−Id` to get the
fully closed forms for `Jm4` and `degree4_term`.

**STEP E (sanity cross-check, not load-bearing):** re-verify `Jm4`
still satisfies Round 28's theorem premises (equivariance, Swap-
symmetry, Hermiticity) — consistent with, but no longer NEEDED to
derive, its value.

## Falsifiable Claims

**C1 (the headline result):** `jac_h(j,k,l)+jac_m(j,k,l)=0` exactly,
for all triples and orderings.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP A).

**C2:** `Jm4 = 2·Ch_4` exactly (direct matrix identity, no solve).

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP B).

**C3:** `degree4_term = −5/4·Ch_4` exactly (direct matrix identity, no
solve).

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP C).

**C4:** combined with Round 35's `Ch_4=Casimir_su3−Id`, both `Jm4` and
`degree4_term` reproduce their previously-established values exactly.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP D).

## Kill Conditions

- C1 killed if: skeptic finds the abstract argument (Step 2 above) is
  actually flawed — e.g. that `[X,[Y,Z]_h]` does NOT lie entirely in
  `m` (would mean reductivity `[h,m]⊆m` fails for this project's own
  setup — a much larger, foundational problem, not specific to this
  round), or that `jac_m` as coded does NOT actually equal the `m`-part
  of `[X,[Y,Z]_m]` (a transcription mismatch between the abstract
  argument and Round 26's own code).
- C2/C3 killed if: skeptic finds `build_quartic_matrix` is NOT actually
  linear in its coefficient function (would invalidate the whole
  "direct consequence via linearity" argument) — verify by direct
  inspection of the function's loop structure (unchanged since Round
  26, already verified in Round 35's own skeptic review).
- C4 killed if: skeptic finds Round 35's own `Ch_4=Casimir_su3−Id`
  citation is stale/wrong, or the arithmetic combining `c=1` with the
  scalars `2` and `−5/4` from STEPs B-C is incorrect.

## What this does NOT mean

- Does NOT re-derive `Ch_4`'s own `c=1` from scratch — that still
  rests ENTIRELY on Round 30's structural chain (`Ch_tilde=Casimir_su3`
  + 2 cited textbook Lie-theory facts + one back-solved case, `k=8`),
  per Round 35's own honest scope, untouched by this round. This round
  isolates that as the SOLE remaining dependency for the entire
  degree-4 story (`Ch_4`, `Jm4`, `degree4_term`), but does not close it.
- Does NOT change any previously-established numeric value from Rounds
  4-35 — `Jm4=2·(Casimir_su3−Id)` and `degree4_term=−5/4·(Casimir_su3−Id)`
  already matched these exact numbers via Round 35's combinatorial
  3×3-solve route; this round provides a SECOND, more direct, solve-
  free derivation route to the SAME numbers, not new numbers.
- Does NOT invalidate Round 33's original 3×3-solve route to
  `degree4_term`'s `c'=-5/4`, or Round 35's `Jm4` 3×3-solve route —
  both remain valid, independent cross-checks; they are simply no
  longer NECESSARY, since this round's Jacobi-identity route is more
  direct and requires strictly fewer assumptions (no Round 28 theorem,
  no degree-counting argument, no 3×3 linear system at all).
- Does NOT resolve the preprint's `8/45 vs ~1.03` norm-ratio tension,
  the `M_p`/`Z_p` L4A convention question, `RHO`/`NU`'s literal
  AHL2023 "E_{a,b}" notation question (Round 34), or WHY Round 34's
  intertwiner `P` is Hadamard-type — all remain open, untouched by
  this round.
- Does NOT mean the `jac_h=-jac_m` identity is a discovery of this
  round — it is Agricola 2002's own theorem, already cited and used in
  this project's `g2su3_delta_correction.py` (2026-07-09, predating
  Round 26). See the "Attribution correction" note in Background.

## Skeptic Verdict (FL Step 8a — context-blind, claim.md + code only)

Two independent context-blind skeptics + a tool-verified synthesis
agent (Workflow tool, task `wji4ntu3g`) reviewed this round. **Zero
FALSIFIED claims** — all four survive, confirmed independently multiple
times over. One significant, non-mathematical finding: the synthesis
agent caught that this round's original framing presented `jac_h=-jac_m`
as a fresh discovery, when it is actually Agricola 2002's own theorem,
already cited and used in this project 2 days before Round 26.

| Claim | Verdict | Note |
|---|---|---|
| C1 (`jac_h+jac_m=0`, abstract argument + code) | `[CONFIRMED-REAL]` | Both skeptics independently traced Round 26's exact code (`h_bracket_action_on`, `m_bracket`, sign conventions) and confirmed the abstract argument matches it term-for-term. The synthesis agent went further: ran `g2su3_appendix_a_construction.py`'s own calibration to NUMERICALLY re-verify the reductivity premise `[h,m]⊆m` (48/48 pairs match, not just assumed by type-signature), and independently re-derived the argument from scratch, confirming it's logically sound with no gap. |
| C2 (`Jm4=2·Ch_4`) | `[CONFIRMED-REAL]` | Both skeptics + synthesis hand-verified the linearity of `build_quartic_matrix` by direct loop inspection; synthesis additionally ran an empirical linearity test with two unrelated coefficient functions and a random rational combination — confirmed. |
| C3 (`degree4_term=-5/4·Ch_4`) | `[CONFIRMED-REAL]` | Arithmetic chain (`-1/2·(1-9/4)=5/8`, `5/8/(-1/2)=-5/4`) independently re-derived and hand-checked by both skeptics and the synthesis agent — all three arrive at the identical result. |
| C4 (combined closed forms match Round 35) | `[CONFIRMED-REAL]` | Confirmed as a genuine same-run recomputation (STEP D independently rebuilds `Casimir_su3` and re-asserts `Ch_4=Casimir_su3-Id`), not a stale citation; cross-checked against Round 35's own file directly. |

**The significant finding — attribution, not falsification:** the
synthesis agent searched `decision.md` and sibling scripts (correct use
of tool access neither skeptic had reason to exercise, since context-
asymmetry gives skeptics only the 4 cited files) and found this exact
identity, with the exact same primary-source citation (Agricola 2002
§2, pp.5-6), already on record since 2026-07-09 in
`g2su3_delta_correction.py` — TWO DAYS before Round 26 even introduced
`Ch_4`/`degree4_term` as named objects. Neither Round 26, 33, nor 35
connected back to this already-cited shortcut, each instead rebuilding
the relevant quantities via harder combinatorial 3×3-solve routes. This
round's original framing ("elementary, no citation needed... not
previously stated explicitly") was an unintentional but real novelty
overclaim relative to this project's OWN history. **Fixed**: docstring,
all relevant print statements, and this claim.md reworded throughout to
credit Agricola 2002 directly, cross-reference `decision.md`'s prior
"Round 6" discussion and `g2su3_delta_correction.py`, and reframe the
round's genuine contribution as "re-derivation + first application to
these specific objects," not "fresh discovery."

**Decision: PROMOTE.** All 4 claims (C1-C4) survive; the correction was
to attribution/framing, not to any mathematical content — every
identity, arithmetic step, and non-vacuous check held exactly across
three independent reviewers. This finding is itself worth noting as a
project-methodology lesson: `decision.md` and sibling round scripts
should be searched for related prior identities BEFORE a fresh
combinatorial re-derivation, not only after (see `activeContext.md`
for this round's memory entry).
