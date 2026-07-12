---
experiment_id: 20260708-dolan-casimir-g2su3
round: 40
date: 2026-07-12
tier: Full-Ladder
status: skeptic_reviewed_promoted
parent: round39 (established step2_remainder's closed form); this round
  continues the SAME technique on `T12+T21`, the piece both FL Step 8a
  Round-39 skeptics flagged as "the least-examined piece" of Round 25's
  5-piece decomposition of Delta
---

# claim.md — Round 40: `T12+T21`'s exact but PARTIAL contribution to
Delta, via two construction routes

## Background

User: "го, round 40" — chose "T12+T21 через {Dslash,E_p} (рекомендую)"
via `AskUserQuestion`, after a quick scouting computation (not part of
this round's committed script) found `{Dslash_mat,E_p}` (the
anticommutator) is SPARSE — only 4/64 nonzero entries per `p`,
connecting the two SU(3) singlets (basis indices `0,7`) to a
`p`-dependent pair of "3+3̄" indices.

**Scope narrowed honestly before writing this claim:** a follow-up
attempt to identify `{Dslash_mat,E_p}` as a single NAMED Clifford
bivector operator (e.g. `E_2·E_3`) did NOT match cleanly — so this
round does NOT claim an elegant closed form for the anticommutator
itself. Instead, `T12+T21` is built via direct matrix construction
(exactly Round 23's own original method) and its compressed
contribution to `Delta` is computed directly.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — an exact algebraic construction, verified
computationally. NOT empirical, NOT causal.

## Core argument

1. **[VERIFIED, STEP A]** `T12+T21` built via Round 23's ORIGINAL
   method: `TERM1_mat·TERM2_mat + TERM2_mat·TERM1_mat` (direct 64×64
   matrix multiplication, no algebraic manipulation).
2. **[VERIFIED, STEP B — NOTE ON EPISTEMIC WEIGHT, stated upfront]**
   `T12+T21` ALSO equals `Σ_p kron({Dslash_mat,E_p}, M_p)`. **This
   agreement is algebraically FORCED, not independent evidence:**
   `TERM1_mat=kron(Dslash_mat,Id)`, `TERM2_mat=Σ_p kron(E_p,M_p)`, and
   the GENERAL Kronecker mixed-product rule `(A⊗B)(C⊗D)=(AC)⊗(BD)`
   (specialized with `B=Id`) forces `TERM1·TERM2+TERM2·TERM1` to reduce
   to the anticommutator sum, with no additional assumption. STEP B is
   a CONSTRUCTION SANITY CHECK (confirms no arithmetic slip in either
   route), not a second, independent confirmation — stated honestly
   here from the outset, applying the lesson from Round 39's own FL
   Step 8a review (where an analogous linearity-forced "cross-check"
   was originally overclaimed and had to be corrected after skeptic
   review). **[POST-SKEPTIC CORRECTION]** The original version of this
   claim cited the special-case identity `kron(A,Id)·kron(B,Id)=
   kron(AB,Id)` (both right-factors `Id`) — imprecise, since `TERM2`'s
   right factor is `M_p`, not `Id`. Both skeptics independently caught
   this; the conclusion was unaffected (substance correct, citation
   imprecise) — fixed to cite the correct general identity above.
3. **[VERIFIED, STEP C, the headline result]** `T12+T21` compressed on
   Round 23/24/25's own `span(w_a,w_b)` = `[[0,1],[3,0]]` EXACTLY —
   trace `0`, det `-3`, eigenvalues `±√3` (added post-skeptic, STEP
   C.1 — both skeptics independently flagged this as a mild underclaim
   in the original version; noted as a hook for a future round, not
   interpreted further here).
4. **[VERIFIED, STEP D]** Re-deriving Round 39's own
   `piece_H+piece_step2_rem` compressed value in-script (self-contained
   re-verification): `[[-1/6,0],[0,5/2]]`, matching Round 39 exactly.
   Given `Delta_2x2` (Round 24/25's own known, cited value)
   `=[[5/2,4/3],[4,5/2]]`, the REMAINING three pieces (`T12+T21`,
   `TORSION_E`, `cross-Casimir`) must together supply
   `[[8/3,4/3],[4,0]]`. `T12+T21` alone supplies `[[0,1],[3,0]]` —
   `still_owed := [[8/3,1/3],[1,0]]` for `TORSION_E+cross-Casimir`,
   NOT computed this round.
5. **Conclusion:** `T12+T21` is now EXACTLY known — a genuine, real
   contribution to `Delta`'s non-scalarity, confirmed via two
   (algebraically-linked, not independent) construction routes — but
   this is explicitly a PARTIAL result. Round 25's own 5-piece
   decomposition of `Delta` now has THREE pieces closed/known exactly
   (`H`, `step2_remainder`, `T12+T21`) and TWO still fully open
   (`TORSION_E`, `cross-Casimir`).

## Construction (code: `g2su3_round40_t12t21_partial_closure.py`)

**STEP A:** build `T12+T21` via direct matrix multiplication
(Round 23's own method).

**STEP B:** cross-check via the anticommutator identity (construction
sanity check, algebraically forced — see Core argument #2).

**STEP C:** compress `T12+T21` onto `span(w_a,w_b)`.

**STEP D:** re-derive Round 39's own `piece_H+piece_step2_rem`
compressed value in-script, compute `target_remaining` and
`still_owed`.

## Falsifiable Claims

**C1:** `T12+T21` (direct multiplication) matches the anticommutator-
sum route exactly. RESULT: `[VERIFIED-tool]` (STEP B) — construction
sanity check, algebraically forced (see Core argument #2), NOT
independent evidence.

**C2 (headline):** `T12+T21` compressed on `span(w_a,w_b)` =
`[[0,1],[3,0]]` exactly. RESULT: `[VERIFIED-tool]` (STEP C).

**C2.5 (added post-skeptic):** `T12T21_2x2` has trace `0`, det `-3`,
eigenvalues `±√3` exactly. RESULT: `[VERIFIED-tool]` (STEP C.1).

**C3:** Round 38/39's `cubic_and_curvature_L=(5/2)·Id−2·Casimir_su3`
re-verifies in this script (self-contained). RESULT: `[VERIFIED-tool]`
(STEP D).

**C4:** Round 39's own `piece_H+piece_step2_rem=[[-1/6,0],[0,5/2]]`
re-derives in this script exactly. RESULT: `[VERIFIED-tool]` (STEP D).

**C5:** `T12+T21` does NOT fully account for `Delta`'s remaining
non-scalarity; `still_owed=[[8/3,1/3],[1,0]]` for `TORSION_E+
cross-Casimir`. RESULT: `[VERIFIED-tool]` (STEP D) — an explicit,
honest NEGATIVE result (this round does NOT claim full closure).

## Kill Conditions

- C1 killed if: the two construction routes disagree — would mean an
  arithmetic error in either `kron` implementation or the anticommutator
  computation (NOT evidence about `T12+T21`'s own value, since the two
  routes are algebraically forced to agree given correct code).
- C2 killed if: skeptic finds `T12+T21`'s compressed value differs from
  `[[0,1],[3,0]]` — would mean an error in `w_a`/`w_b`/`compress_2x2`
  (all copied EXACTLY from Round 25's own definitions) or in `T12+T21`'s
  own construction.
- C3/C4 killed if: Round 38/39's own closed forms fail to re-derive —
  would mean drift in shared upstream primitives (`nabla_g`,
  `e_action`, `su3_action`) since those rounds, which would ALSO break
  Rounds 38/39's own assertions.
- C5 killed if: `still_owed` computes to zero (i.e. `T12+T21` DOES fully
  close Delta's non-scalarity) — this would actually be a STRONGER,
  MORE INTERESTING result than what this round claims; the script's own
  STEP D computes and reports `still_owed` honestly rather than
  asserting a particular sign or magnitude.

## What this does NOT mean

- Does NOT close `Delta`'s non-scalarity. `TORSION_E` and
  `cross-Casimir` (2 of Round 25's 5 pieces) remain completely
  UNTOUCHED — `still_owed=[[8/3,1/3],[1,0]]` is real, nonzero, and
  unexplained by this round.
- Does NOT resolve the `8/45 vs ~1` L4A norm-bound tension.
- Does NOT touch `preprint.tex`.
- Does NOT claim an elegant, named closed form for `{Dslash_mat,E_p}`
  itself — the scouting attempt to identify it as a Clifford bivector
  product did not succeed; `T12+T21`'s value here comes from DIRECT
  construction, not a derived formula in terms of `Casimir_su3` or any
  other already-named object.
- Does NOT claim STEP B's route-agreement is independent evidence — it
  is a construction sanity check, algebraically forced by the general
  Kronecker mixed-product identity `(A⊗B)(C⊗D)=(AC)⊗(BD)` (specialized
  with `B=Id`). Stated upfront here (see Core argument #2), not as a
  post-skeptic correction — though the SPECIFIC identity cited was
  itself corrected post-skeptic (see Skeptic Verdict).
- Does NOT interpret the `±√3` eigenvalue structure of `T12T21_2x2`
  (C2.5) — noted as a hook for a future round, not analyzed here.
- Does NOT resolve the Casimir_su3-vs-Jac_h identity question left open
  by Round 39, the `M_p`/`Z_p` L4A convention question (Rounds 23-26),
  `RHO`/`NU`'s literal AHL2023 notation question, or WHY Round 34's
  intertwiner `P` is Hadamard-type — all remain untouched.

## Skeptic Verdict (FL Step 8a)

Two context-blind skeptics (Read/Bash, no session history) + a
tool-using synthesis agent independently reviewed this round via direct
file reads of `round40_claim.md`, the script, and the two cited prior
scripts (`g2su3_round25_K_derivation.py`, `g2su3_round39_...py`).

| Claim | Skeptic 1 | Skeptic 2 | Synthesis (tool-verified) |
|---|---|---|---|
| C1-C5 | CONFIRMED-REAL (all) | CONFIRMED-REAL (all) | CONFIRMED-REAL (ran script, exit 0, all asserts pass) |

**No FALSIFIED claims — the cleanest review of this session so far.**
Both skeptics independently converged on the SAME two minor findings:

1. **Cited Kronecker identity was imprecise.** Core argument #2 cited
   `kron(A,Id)·kron(B,Id)=kron(AB,Id)` (both right-factors `Id`), but
   `TERM2`'s right factor is `M_p`, not `Id` — the actually-invoked
   identity is the GENERAL mixed-product `(A⊗B)(C⊗D)=(AC)⊗(BD)`
   specialized with `B=Id`. The CONCLUSION (route agreement is
   algebraically forced) was correct throughout — only the specific
   identity cited to justify it was a strict subset of what's needed.
   **Response: Fixed** — reworded in both the script's docstring and
   this claim.md.
2. **Mild underclaim on `T12T21_2x2`'s structure.** `[[0,1],[3,0]]` has
   trace `0`, det `-3`, eigenvalues `±√3` — not surfaced in the
   original version. Both skeptics independently noted the `√3` also
   appeared in the `{Dslash_mat,E_p}` scouting entries this round
   started from, flagging it as a hook worth carrying forward.
   **Response: Fixed** — added a genuine new in-script STEP C.1
   computing and asserting this eigenvalue structure directly (not
   merely stated in prose), `EXIT=0`, confirmed. C2.5 added to
   Falsifiable Claims.

**Bonus finding (synthesis agent, tool-verified, neither skeptic could
check without Bash):** re-running Round 25's OWN script fresh
independently reproduces `piece_T12T21` compressed = `[[0,1],[3,0]]`
exactly — a genuine cross-script corroboration from a DIFFERENT,
chronologically-earlier script (committed 2026-07-11) that never
hardcoded this specific value as an assert (Round 25 only asserted the
full 5-piece SUM). This confirms both Round 40's own value AND that no
primitive has drifted since Round 25.

**Notably good practice, confirmed by both skeptics independently:**
the proactive, upfront disclosure of STEP B's limited epistemic weight
(stated three times — Core argument, Kill Conditions, "What this does
NOT mean" — BEFORE any skeptic review, applying the lesson from Round
39's own FL Step 8a review where an analogous overclaim had to be
caught and fixed) was found to be genuine, not cosmetic. This is the
FIRST round this session where a self-applied lesson from a prior
round's skeptic review measurably reduced the skeptics' own findings to
two minor, easily-fixed items rather than a substantive overclaim.

**True kill? No.** All five claims (C1-C5, plus C2.5) are
`[VERIFIED-tool]`, honestly scoped as a genuine but PARTIAL result.

**Overall: PROMOTE**, clean.
