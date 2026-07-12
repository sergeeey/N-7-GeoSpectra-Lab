---
experiment_id: 20260708-dolan-casimir-g2su3
round: 44
date: 2026-07-12
tier: Full-Ladder
status: skeptic_reviewed_promoted
parent: round43 (general chirality no-go theorem — no bivector-type
  Z_p, of any connection, can satisfy Round 26's own identity); this
  round pursued round43's own named "concrete next step" (verify what
  Agricola's own "Z_i" notation denotes) via direct primary-source
  reading, not speculation
---

# claim.md — Round 44: primary-source confirmation — Agricola's `Z_i`
is a vector + bare-derivative compound, NEVER a per-index connection
operator, throughout her ENTIRE paper (not just one formula)

## Background

Round 43's own "What this does NOT mean" flagged as speculative and
untested: "the natural reading... is that `Z_i·Z_i(ψ)` is shorthand
for a compound first-order object (`e_i · ∇^t_{e_i}ψ`)... rather than
a per-index bivector square" — and named "independently verify what
`Z_i` denotes in Agricola 2002's own primary-source Dirac-operator
formula" as the concrete next step. This round pursued exactly that,
via two targeted research-agent dispatches reading
`Agricola_2002_Dirac_naturally_reductive.pdf` directly (pages 1-8, then
9-14), each independently verified rather than trusted on first report
(per `audit-verification-gate.md`).

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — a primary-source textual verification
question (what does a specific symbol denote in a specific paper),
not empirical or causal. Falsifiable via direct re-reading of the cited
pages.

## Core argument

1. **[WEAKENED, page citation corrected post-skeptic]** `Z_i` is
   defined — informally on p.2 (Introduction: "For an orthonormal
   basis Z_1,...,Z_n of m, it induces the third degree element H
   :=...") and formally on p.4 (Lemma 2.2) — as "an orthonormal basis
   of `m`", i.e. Clifford VECTORS, the same TYPE of object as this
   project's own `e_i` (NOT the same type as `M_p`, this project's own
   bivector spin-connection operator). **Content confirmed correct by
   two independent skeptics + synthesis; the ORIGINAL citation ("p.3,
   p.4") was wrong — page 3 contains zero occurrences of `Z_i`
   (Wang correspondence, `Λ_m`, Lemma 2.1 only); the symbol first
   appears p.2, formalized p.4. Fixed here.**
2. **[VERIFIED, agent 1, pages 7-8, eq 3-5]** The Dirac operator's own
   defining formula: `∇_Z ψ = Z(ψ) + Λ̃_m(Z)ψ` (eq 3, p.7); `Dψ = Σ_i
   Z_i·Z_i(ψ) + Z_i·Λ̃_m(Z_i)ψ` (eq 4, p.7); `D^t ψ = Σ_i Z_i·Z_i(ψ) +
   t·H·ψ` (eq 5, p.8). `Z_i(ψ)` here is the BARE/flat directional
   derivative of ψ along the vector field `Z_i` — the connection
   correction is a SEPARATE additive term, later resummed into the
   single object `t·H`.
3. **[CONFIRMED-REAL substance; WEAKENED equation-number, post-
   skeptic]** The SAME bare-derivative reading of `Z_i(ψ)`/`Z_i²(ψ)`
   holds throughout `Ω_g`'s own definition (p.13: "Ω_gψ = −Σ_i
   Z_i²(ψ) + C̃_h·ψ") and Theorem 3.2 (p.14) — the paper's own gloss
   (bottom of p.12, glossing Proposition 3.4's identical `−ΣZi²(ψ)`
   term, which `Ω_g` reuses verbatim on p.13) is explicit: "one has to
   take the derivative of ψ along all vector fields `Z_i` **twice**"
   — i.e. `Z_i²(ψ) = Z_i(Z_i(ψ))`. No second, distinct meaning of
   `Z_i` is introduced anywhere in pages 3-14 (Lemma 3.4's `X(ψ) =
   −ãd(X)·ψ` is explicitly restricted to `X∈h`, a different space,
   not a counterexample). **Equation-number correction:** `Ω_g`'s own
   formula on p.13 is itself UNNUMBERED — the actual "eq (9)" is the
   following line, `(D^0)²ψ = Ω_g + C̃_h + (1/2)Σ...` (this project's
   own `g2su3_round26_jach_derivation.py` docstring's "eq (8)/(9),
   pages 12-13" citation is actually fine as-is; it was THIS round's
   own original C3 text that mislabeled `Ω_g`'s bare definition itself
   as "eq 9" — corrected here).
4. **[FALSIFIED — full correction, post-skeptic]** This round's
   ORIGINAL text characterized this project's own `g2su3_round26_jach_
   derivation.py` docstring ("`Zi(psi)` inside Omega_g ALWAYS means
   the CANONICAL (t=0) covariant derivative -- NOT the full
   Levi-Civita derivative directly") as "a mild misreading of the
   mechanism". **This was WRONG — two independent skeptics plus the
   synthesis agent, working from the primary source directly (not
   from each other), confirmed the docstring's claim is mathematically
   TRUE, not a misreading:** `Λ_m^t(X)Y := t·[X,Y]_m` (p.4) is
   identically zero at `t=0`; substituting into eq(3) (p.7, `∇_Zψ =
   Z(ψ) + Λ̃_m(Z)ψ`, general for any connection) gives `∇^0_Z ψ =
   Z(ψ) + 0 = Z(ψ)` **exactly**. So `Z_i(ψ)` (the bare derivative) IS
   identically `∇^0_{Z_i}ψ` (the canonical connection's own covariant
   derivative) — the docstring's factual claim holds. The synthesis
   agent additionally found decisive independent confirmation neither
   skeptic had cited: Agricola's own **Proposition 3.4 (p.12) is
   explicitly TITLED** "The square of `D^0`, **the Dirac operator
   corresponding to the canonical connection**" — naming the EXACT
   term (`−Σ Zᵢ²(ψ)`) later reused verbatim inside `Ω_g` (p.13) with
   her OWN terminology, not merely a coincidence this round derived.
   **What survives from this round's original point:** `Z_i(ψ)` IS
   also, simultaneously and correctly, a single uniform symbol used
   unchanged across `D^t`'s own formula and `Ω_g` (Core argument #2-3
   above) — but this is a COMPLEMENTARY description of the SAME fixed
   object, not a competing one, and does NOT make the docstring's
   framing a misreading. The two descriptions ("bare, t-independent
   directional derivative" and "the canonical t=0 covariant
   derivative") are mathematically identical here BECAUSE `Λ_m^0=0` —
   this round's original text simply never performed that
   derivation before asserting a factual error in the docstring.
5. **Conclusion (ties directly to Round 43):** `Z_i` (Agricola's own
   notation, throughout the ENTIRE relevant portion of her paper) is
   NEVER a per-index bivector connection operator (like `M_p`) — it is
   consistently a vector-times-bare-derivative compound, i.e. exactly
   the "chirality-ODD, first-order Dirac-building-block" type object
   Round 43 flagged as the speculative alternative. **Round 26's own
   implicit labeling of the leftover algebraic term (isolated by
   subtraction from `Dslash_mat²`) as "`Z_p`" — by loose analogy with
   Agricola's notation — was therefore comparing against the WRONG
   KIND of mathematical object from the very start of this
   investigation (Rounds 26/41/42).** Round 43's general,
   representation-theoretic chirality no-go theorem is not merely
   *consistent* with this reading — it independently *predicted*,
   from pure structure, exactly what this primary-source check now
   *confirms* textually: two completely independent routes (abstract
   representation theory; direct primary-source reading) converge on
   the same answer.

## Construction

No new code. This round is a primary-source verification finding (two
independent, targeted research-agent PDF reads, each reporting exact
page/equation numbers and verbatim quotes), following the Structure-
Bias Guard's own principle that a reasoning/verification step need not
be forced into an executable-code format. Falsifiability is via direct
re-reading of the cited pages, not computation.

## Falsifiable Claims

**C1:** `Z_i` is defined as an orthonormal basis of `m` (p.2 informal,
p.4 Lemma 2.2 formal). RESULT: `[WEAKENED]` — content confirmed by two
independent skeptics + synthesis, all reading the PDF themselves;
ORIGINAL citation ("p.3-4") was wrong (p.3 has zero occurrences of
`Z_i`), fixed above.

**C2:** `D^t ψ = Σ_i Z_i·Z_i(ψ) + t·H·ψ` (eq 5, p.8), with `Z_i(ψ)`
the bare directional derivative. RESULT: `[CONFIRMED-REAL]` — all
quotes and page/equation numbers verbatim-correct, independently
confirmed by two skeptics + synthesis, each reading pp.7-8 themselves.

**C3:** `Ω_g` uses the IDENTICAL bare-derivative reading of `Z_i(ψ)` —
no second, distinct meaning is introduced anywhere in pages 3-14.
RESULT: `[CONFIRMED-REAL]` (substance) / `[WEAKENED]` (this round's
own original text mislabeled `Ω_g`'s own formula as "eq 9" — it is
unnumbered; eq 9 is the following line) — both independently confirmed
by two skeptics + synthesis, all reading pp.9-14 themselves.

**C4:** Round 26's own docstring's stated mechanism (`Z_i(ψ)` inside
`Ω_g` equals the canonical t=0 covariant derivative) is a misreading.
RESULT: `[FALSIFIED]` — **this round's ORIGINAL characterization was
wrong.** Two independent skeptics plus the synthesis agent, all
re-deriving from the primary source directly, confirmed the docstring
is mathematically CORRECT (`Λ_m^0=0` at p.4 + eq(3) at p.7 ⟹ `Z_i(ψ) =
∇^0_{Z_i}ψ` exactly), with the synthesis agent additionally citing
Agricola's own Proposition 3.4 title (p.12, "the Dirac operator
corresponding to the canonical connection") as decisive independent
confirmation. Fixed in Core argument #4 above — see full correction
there. Response per Step 8a matrix: **Fix** (this correction), not
Dismiss or Accept — the concern was a genuine factual error in this
round's own original text, not a defensible alternative framing.

**C5 (the tie-in to Round 43):** `Z_i` (as genuinely used by Agricola,
throughout her paper) was never intended to be a per-index bivector
connection operator — Round 26's comparison target was mislabeled by
analogy, not by the primary source's own usage. RESULT: `[VERIFIED]`
as a direct logical consequence of C1-C3 combined with Round 43's own
established chirality argument (not a new computation, a synthesis of
two independently-established facts).

## Kill Conditions

- C1-C3 killed if: re-reading pages 3-14 finds a DIFFERENT definition
  of `Z_i`, or finds a second distinct meaning of `Z_i(ψ)` the agents
  missed — straightforward to check by re-reading the same pages.
- C4 killed if: Round 26's own docstring is re-read and found to NOT
  actually claim what this round says it claims — a direct text
  comparison. **[POST-SKEPTIC NOTE] This kill condition, as originally
  worded, only tests quote-fidelity, not substantive mathematical
  truth — it would have PASSED even though C4 turned out FALSE (the
  docstring's mechanism is mathematically correct, not merely
  "claimed"). Both skeptics tested the substantive math instead of
  just the quote-fidelity, which is what actually caught the error.
  Flagged here as a phrasing lesson for future rounds of this type,
  not re-litigated further since C4 is already fixed above.**
- **Overarching kill condition:** if this round is read as claiming to
  have RESOLVED what "individual Z_p matrices" would look like, or as
  resolving the L4A tension, or as invalidating Round 43's own
  theorem in any way — none of these are claimed, and any such reading
  would be a genuine overclaim requiring a fix.

## What this does NOT mean

- **Does NOT resolve the L4A `8/45 vs ~1.03` norm-bound tension** —
  remains completely open.
- **Does NOT mean building an actual "Z_i(ψ)" bare-derivative operator
  for THIS project's own realization is trivial or has been done.**
  Understanding HOW ψ (a Δ_m-valued function satisfying an
  equivariance condition on `G=G2`, per Agricola's own setup) is
  differentiated along left-invariant vector fields `Z_i` is a
  separate, nontrivial representation-theoretic computation this
  round does NOT attempt.
- **Does NOT establish that Round 26's own numerical identity
  (`Delta_HCas = H-(1/2)Id-(7/4)Casimir_su3`) has any deeper physical
  meaning now that "Z_p" is known to have been mislabeled.** It may
  remain a bookkeeping curiosity — the difference between two
  DIFFERENT KINDS of Dirac-operator-squared constructions
  (`Dslash_mat²`, built from this project's own `M_p`; vs whatever
  "the leftover algebraic term Theorem 3.2 implies" actually
  represents) — not a physically meaningful M_p-vs-Z_p comparison at
  all. This is a genuinely open question this round does not resolve.
- **Does NOT modify or invalidate Round 43's own claim, proof, or
  code** — Round 43's theorem is representation-theoretic and stands
  on its own regardless of what "Z_p" was intended to denote. This
  round provides independent textual confirmation of WHY that theorem
  was inevitable, not a correction to it.
- **Does NOT touch `preprint.tex`, any `.py` file, or the test suite**
  — a documentary/primary-source finding only. No pytest re-run
  required (no source code changed).
- Does NOT resolve the Casimir_su3-vs-Jac_h identity question (Round
  39), `RHO`/`NU`'s literal AHL2023 notation question, or WHY Round
  34's intertwiner `P` is Hadamard-type — all remain untouched.
- **Concrete next step, NOT started:** either (a) attempt to build
  the genuine bare-derivative operator `Z_i(ψ)` for this project's own
  Δ_6-valued spinor realization on `G=G2` (a nontrivial representation-
  theoretic construction), to directly test `D^0=Σ Z_i·Z_i(ψ)` against
  this project's own established `D^0=-H` (Round 27) fact — or (b) set
  aside the M_p-vs-Z_p thread entirely (four rounds — 26, 41, 42, 43,
  44 — have now converged on "this specific avenue is closed") and
  pursue the L4A `8/45 vs ~1.03` tension via a genuinely different
  angle not yet identified.

## Skeptic Verdict (FL Step 8a)

Two context-blind skeptics + a synthesis agent, ALL THREE independently
reading the SAME primary-source pages (1-14 of
`Agricola_2002_Dirac_naturally_reductive.pdf`) themselves — not
trusting this round's own research-agent-sourced quotes, per this
project's explicit rule that "agent's `[VERIFIED]` = your `[INFERRED]`"
until independently re-checked. This is a stricter review than most
prior rounds, since the claims here are textual/quote-based rather
than computational — the failure mode being guarded against is
hallucinated or misattributed quotes, not arithmetic errors.

| Claim | Skeptic 1 | Skeptic 2 | Synthesis (independent 3rd read) |
|---|---|---|---|
| C1 | WEAKENED (p.3 citation wrong, content right) | WEAKENED (same finding) | WEAKENED (confirmed independently) |
| C2 | CONFIRMED-REAL | CONFIRMED-REAL | CONFIRMED-REAL |
| C3 | CONFIRMED-REAL substance / WEAKENED eq-number | CONFIRMED-REAL substance / WEAKENED eq-number | CONFIRMED-REAL substance / WEAKENED eq-number |
| C4 | **FALSIFIED** | WEAKENED ("overstates a terminology dispute") | **FALSIFIED** (sides with skeptic 1, adds new evidence) |
| C5 | CONFIRMED-REAL, unaffected by C4 | CONFIRMED-REAL, no overreach | CONFIRMED-REAL, unaffected by C4 |

**C4 was the one genuine finding requiring a response.** The two
skeptics disagreed on SEVERITY (FALSIFIED vs WEAKENED) but agreed on
the SUBSTANCE: this round's original claim that Round 26's docstring
"misread" the mechanism was itself incorrect. Both independently
re-derived, from the primary source, that `Λ_m^t(X)Y := t[X,Y]_m`
(p.4) vanishes at `t=0`, so substituting into eq(3) (p.7) gives
`∇^0_{Z_i}ψ = Z_i(ψ)` exactly — meaning the docstring's factual claim
(`Z_i(ψ)` = canonical t=0 covariant derivative) is mathematically
TRUE, not a misreading. **The synthesis agent resolved the severity
disagreement with evidence NEITHER skeptic had cited:** Agricola's own
Proposition 3.4 (p.12) is explicitly TITLED "The square of `D^0`, the
Dirac operator corresponding to the canonical connection" — naming the
exact term later reused in `Ω_g` with her OWN terminology, not a
coincidence this round derived. This is textually decisive, not just
an algebraic re-derivation both skeptics already agreed on, and
tips the verdict to FALSIFIED (agreeing with skeptic 1) rather than
skeptic 2's softer "overstated framing" characterization. The
synthesis agent also caught a genuinely new gap neither skeptic named:
this round's ORIGINAL C4 text mischaracterized the docstring itself as
asserting "a second meaning" of `Z_i` — the docstring never claimed
that; it asserted one fixed meaning, correctly contrasted against a
different, inapplicable object (`∇^{1/2}`). This confirms **Fix** (not
Dismiss/Accept) was the correct response — the error was in this
round's own characterization, not a defensible alternative reading.

**Response: Fixed, not dismissed.** Core argument #4 fully rewritten
(the "mild misreading" framing removed entirely, replaced with the
correct derivation and the Prop. 3.4 citation); C1's page citation
corrected (p.2+p.4, not p.3+p.4); C3's equation-number note added
(`Ω_g`'s own formula is unnumbered, distinct from the following eq 9).
All three fixes applied to Core argument and Falsifiable Claims
sections above, not just noted here.

**What survives, solid, unaffected by the C4 correction:** the round's
core, independently load-bearing thesis (C1 content + C3 substance +
C5) — `Z_i` is consistently a Clifford-degree-1 vector throughout
pp.3-14, NEVER a bivector connection operator, so Round 26's implicit
"Z_p" comparison target was mislabeled by analogy from the outset. All
three reviewers confirm C5 (the tie-in to Round 43) is a valid
synthesis, grounded in C1+C3, not in the now-corrected C4 — Round 43's
own theorem is untouched by any of this.

**True kill? No** (all three reviewers agree). The FALSIFIED finding
(C4) was about this round's OWN characterization of a prior round's
docstring — a correctable error in exposition, not a defect in the
round's core thesis, which survives fully.

**Overall: PROMOTE** (post-fix). C2/C5 clean `[CONFIRMED-REAL]`; C1
`[WEAKENED]` (citation, now fixed); C3 `[CONFIRMED-REAL]`
substance/`[WEAKENED]` eq-number (now fixed); C4 `[FALSIFIED]` (now
corrected in place — this round's own text was wrong, not the prior
round's docstring).
