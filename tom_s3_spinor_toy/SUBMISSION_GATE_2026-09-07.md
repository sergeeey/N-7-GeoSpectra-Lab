# Submission Gate — draft reply to Tom Lawrence, 2026-09-07

Per `~/.claude/rules/integrity.md` § Submission Gate. Artifacts:
`DRAFT_REPLY_TO_TOM_2026-09-07.md` (English, the one that would be sent) and
`DRAFT_REPLY_TO_TOM_2026-09-07_RU.md` (Russian, for Sergey's review). Both are at
**revision 3**.

## VERDICT: **CLOSED — PASSED and SENT, 2026-09-07 18:39.**

All four gates clear; the three items this document could not settle were
settled by Sergey, who read revision 4 and sent it. Revision 4 is the version
that went. **This file is now a record of a completed gate, not a live
checklist** — nothing in it should be edited except to append what Tom's reply
teaches us about whether the gate caught the right things.

### What the gate cost and what it caught — for calibrating the next one

Four round-level skeptic passes, three letter-level reads (one by Sergey, two
context-blind with deliberately different prompts), one code review, one
cooling-off re-read after a 4h10m break. Between them:

| | |
|---|---|
| Factual errors in the physics | **0** — every pass |
| Defects in *checks* | **5** cannot-fail checks + 1 cannot-fail conjunct |
| Defects in the *letter* | 3 (Sergey) + 3 (blind A) + 3 (blind B) + 3 (cooling-off) |
| Claims withdrawn | **2** — our "correction" to Tom's item 4, and the `c = 3/2` framing |
| Found by self-review | **0** |

The single most expensive thing prevented: revision 1 would have told Tom he
had made an error in his own §2.2 item 4. He had not. That correction was
caught by a skeptic, confirmed by a verbatim re-read of his p.13, and withdrawn.

The change from the previous verdict is that **Gate 1 is now clear**: the letter
itself has been adversarially read three times, twice context-blind. What remains
open is Gate 4 (cooling-off) and two decisions that are Sergey's, not this
document's.

---

## Gate 1 — Adversarial review: **CLEAR**

### Round-level (four passes, run before the letter existed)

| Round | Verdict | What it found |
|---|---|---|
| C179 (the no-go) | `CONFIRMED-REAL` | 6 attacks, none broke it; supplied a *second* independent proof (Peter–Weyl) |
| C180 (the `S³` construction) | `WEAKENED` | 3 concerns, all closed by added computation |
| C181 (his check + RNC) | `WEAKENED` | the discrimination test's "same span" half was a **tautology**; the correction to Tom was scoped too broadly |
| C182 (the `S²` descent) | `WEAKENED` | the "two checks" are one algebraic identity; the no-go condition was a **tautology** |

### Letter-level (three reads, all after revision 1)

| Read | Kind | Verdict | What it found |
|---|---|---|---|
| **Sergey, manual** | full context | needs changes | **3 letter-level defects**: the 2π claim stated looser than its own `claim.md`; the letter **credited Tom with an error** (SO(n)'s defining rep is self-dual, so "dual ≠ defining" is wrong); the `S³` section read as if parallelizability *defeated* the obstruction |
| **Blind read A** | context-blind, formal prompt | `WEAKENED` | `c = 3/2` "drops out of the data" overstates (the target `n+3/2` is supplied); "−1 on a half-turn" is convention-dependent; a quotation of Tom had been silently re-inflected; flagged one attribution as unverifiable |
| **Blind read B** | context-blind, paraphrased prompt | needs changes | the projection formula `x_μ = ½Tr(σ_μ†g)` is wrong outside the quaternionic basis; "four functions" is ambiguous between 2 complex and Tom's 4 complex; the `S³` Dirac degeneracies want a citation |

Both blind reads were given **only** the letter body (status block and changelog
stripped), the `.py`/`results_*.json` files, and Tom's PDF; `claim.md` and
`decision.md` were explicitly withheld. The two prompts were deliberately worded
differently — a Paraphrase-Sensitivity Probe per
`falsification-ladder.md` § Step 8a, justified here because sending is
irreversible.

**The probe earned its cost: the two reads overlapped on nothing.** A found the
`c = 3/2` and quotation issues; B found the projection-formula and
component-count issues. A single read would have missed roughly half.

### Disposition of every letter-level finding

| # | Finding | Disposition |
|---|---|---|
| 1 | `c = 3/2` "drops out of the data" | **ACCEPTED and escalated.** Re-tested with corrupted spectra (`c180b_...py`): a uniform `+1` shift returns a unique `2.5`, `+0.37` returns `1.87`. The *uniqueness* is algebraic and the *value* tracks the shift. Rewritten to claim only what survives. Recorded in C180 `decision.md`. |
| 2 | Projection formula wrong as written | **ACCEPTED, diagnosis sharpened.** Verified both readings numerically: exact in the quaternionic basis `(I, iσ_k)` (error `0.0`), off by `i` on spatial components in the plain Pauli basis (error `1.14`). The code was right; the letter omitted the basis. Basis now stated. |
| 3 | "four functions" ambiguous | **ACCEPTED.** Tom's `n=3` multiplet is 4 *complex* (the ambient bispinor); the built object is `ℂ²` = 2 complex. Disambiguated up front in §3. |
| 4 | "−1 on a half-turn" convention-dependent | **ACCEPTED.** Code uses `U(θ)=exp(θX₃^R)` with weight read from `−½i X₃`, giving phase `exp(2iwθ)`; at `w=½, θ=π` that is `−1`. Self-consistent but normalisation-specific. Non-invariance now carries the argument; the `−1` is labelled as convention. |
| 5 | Quotation re-inflected (`include` → `include[s]`) | **ACCEPTED.** Now quoted closer to verbatim. |
| 6 | Citation wanted for the `S³` degeneracies | **ACCEPTED.** Camporesi–Higuchi, gr-qc/9505009 — **existence, authors and title verified via literature search, not cited from memory.** |
| 7 | "similarity transformation" attribution unverifiable | **DISMISSED with evidence.** Tom's own message reads, verbatim: *"I'd assumed that matrices which transform the Laplacian spherical harmonics must be equivalent to those acting on the vector representation through a similarity transformation."* The reader did not have the email in scope and correctly said so. No change. |

### Track record — why this gate is not a formality

Across the four round-level and three letter-level reads, **every substantive
defect found was in a CHECK or in the WRITING, never in a computation.** The
physics came out right each time; what kept failing was the machinery meant to
establish that it was right, and then the prose describing it.

Five cannot-fail checks were found in this one sequence (C180 multiplicity
check, C182 no-go condition, C181 span test, C181B Frobenius norm, C180
`c`-uniqueness). **Corrected while writing this line:** an earlier draft of this
list named C180's *basis-independence* test instead of its multiplicity check.
The basis test was a different failure — a congruence-vs-similarity bug that
produced a spurious FAILURE, which is the opposite defect.
Three were caught by external skeptics, one by a negative control deliberately
placed in the script, one by a corrupted-input replay run only because a skeptic
queried the wording. **Self-review caught none of the five.** Recorded as a
counted observation in `pearl_registry/INDEX.md` (2026-09-07, impact 7).

## Gate 2 — Evidence markers on every claim: **CLEAR**

Claims unchanged from revision 1 are not re-listed; the table below covers every
claim the revisions altered or added.

| # | Claim in revision 3 | Marker | Source |
|---|---|---|---|
| 1 | 2π obstruction, scoped to "pullback-only action on scalar functions" | `[VERIFIED-tool]` | C179; scope now matches its own `claim.md` |
| 2 | The obstruction is standard rep theory, not new | `[DOCS]` | Frobenius/Peter–Weyl; stated as context, with the two-line mechanism given explicitly so the claim does not rest on the label |
| 3 | §2.2 says "the spinor representation of `SO(n+1)`" | `[VERIFIED]` | direct read, PDF p.13, quoted as a question not an assertion |
| 4 | `SO(n)` defining rep is self-dual; `g↦gᵀ` is not a homomorphism | `[VERIFIED-tool]` | 600 random `SO(3)`/`SO(4)` elements: contragredient−defining `1.2e-15`; `(gh)ᵀ ≠ gᵀhᵀ` residual `1.943` |
| 5 | Tom's p.13 bracketed question, quoted | `[VERIFIED]` | verbatim from PDF |
| 6 | Tom's prior "similarity transformation" view | `[VERIFIED]` | verbatim from his own message |
| 7 | `S³` construction changes category, does not defeat §1 | `[VERIFIED]` | matches C179 `decision.md`'s own scoping; confirmed by both blind reads |
| 8 | Component bookkeeping: `ℂ²` = 2 complex vs Tom's 4 complex | `[VERIFIED]` | PDF §2.2 `d = 2^{(n+1)/2}`; the two restrict to the same rank-2 bundle on `S³` |
| 9 | `D₀` spectrum table, `k=0..3` | `[VERIFIED-tool]` | `results_c180.json`, exact match |
| 10 | Multiplicities are the standard `S³` Dirac degeneracies | `[VERIFIED-tool]` + `[DOCS]` | `c85_certification.py`; Camporesi–Higuchi gr-qc/9505009 |
| 11 | **`D₀`'s spectrum is Dirac up to ONE additive constant, which is `3/2`** | `[VERIFIED-tool]` | `results_c180b.json`. **Replaces the withdrawn "the constant drops out of the data".** Corrupted-spectrum tests: moved level, broken spacing, broken multiplicity each destroy the solution; a uniform shift does not. |
| 12 | `k=0` is two constant spinors, **not** zero modes; `\|λ\| = 3/2` | `[VERIFIED-tool]` | C180; consistent with KT-8 (round `S³` has no zero modes) |
| 13 | `S²` dims 1,3,5 and 2,4,6 are ONE fact, not two | `[VERIFIED-tool]` | C182; the letter says so explicitly |
| 14 | Weight-0 invariant, weight-`½` not; `−1` at `θ=π` in the stated parameterisation | `[VERIFIED-tool]` | C182 `fibre_invariance_check`; convention now stated |
| 15 | p.435 reading | `[INFERRED]`, hedged in the letter | Gallier notes not read; letter says so |
| 16 | **Tom's item 4 is correct as written** | `[VERIFIED-tool]` | `results_c181b.json`: for `n` odd his multiplet is the bispinor; `ΨΨ†` is reducible and contains the vector twice. **C181's "correction" withdrawn.** |
| 17 | Block table `1+3+1+3+4+4 = 16`; vector in the off-diagonal blocks | `[VERIFIED-tool]` | `results_c181b.json`; discriminator: off-diagonal singlet drifts `8.44`, diagonal fixed at `3.6e-15` |
| 18 | Projection exact **in the quaternionic basis** | `[VERIFIED-tool]` | verified in both bases; plain-Pauli error `1.14`, quaternionic `0.0` |
| 19 | The check does not discriminate | `[VERIFIED-tool]` | C181, rebuilt after the tautology was found |
| 20 | RNC: `g(0)=δ`, all 9 first derivatives vanish symbolically | `[VERIFIED-tool]` | C181 |
| 21 | Tom's (79), (107), (108), (113) | `[VERIFIED-tool]` | direct PDF read + computation; **independently confirmed by both blind reads** |
| 22 | §3.3 opening line; his stated preference for deriving via differential equations | `[VERIFIED]` | direct read, PDF p.17 |
| 23 | "five of my own checks could not fail" | `[VERIFIED-tool]` | enumerated in `pearl_registry/INDEX.md` and the two `decision.md` corrections |

No claim in either letter is unmarked, and none rests on `[MEMORY]`.

## Gate 3 — Internal consistency (text vs. data): **CLEAR**

- Every number in revision 3 re-checked against the results JSONs this session.
  **Caveat on method:** the automated sweep matches numbers by substring, which
  is coarse for small integers; the load-bearing values (`c180b` corruption
  table, `c181b` discriminator, block totals) were read field-by-field instead.
- Both blind reads independently re-verified the spectrum table, multiplicities,
  `c`, the `2`-vs-`6` eigenspace dims, and the `S²` ladders against the same
  JSONs and found no rounding-up.
- `pytest`: **2524 passed, 4 skipped, 0 failures** (513 s).
- `ruff`: clean on both new scripts.
- English and Russian versions carry the same claims; both at revision 3.

## Gate 4 — Cooling-off: **OBSERVED**

Revision 3 was finalised at **14:07**; the re-read happened at **18:17** — a gap
of **4h10m**, and the intervening time went entirely to unrelated work (the
negative-control machinery, the Revival Condition rule, a commit split). That is
what the rule asks for: not a pause taken in the same breath as finishing, but a
genuine change of task before re-reading.

**Findings of the cooling-off re-read — no factual errors; three tone-level items,
one of which should not be sent as written:**

| # | Location | Finding |
|---|---|---|
| 1 | "a small and rather inbred sample" | **Should be changed.** The sample is *Sergey's own work and Dr. Buckholtz's*. "Inbred" describes the sampling, but sits next to a third party's name and can be heard as a judgement on his work. Rephrase to make clear it is about independence of review, not about the subjects. |
| 2 | §1, "is adjacent to it but weaker" | Accurate but a small status move — "my statement is stronger than yours" — in a letter that asks for his assessment. Soften. |
| 3 | "But first there's one result I want to lead with" | It is the fourth paragraph. Minor stumble. |

**Structural note, Sergey's call not this gate's:** the two questions the letter
most wants answered sit *after* six technical sections. Tom's own notes run to 18
pages so length is not the issue, but questions at the end of a long letter get
answered less often. One line in the opening would flag them.

**Explicitly re-checked and left alone:** the "five checks" count (correct for the
C179–C182 batch; the later sixth finding is a different shape and was recorded
separately for exactly that reason), and naming Dr. Buckholtz (per Sergey's own
instruction for this letter).

---

## Blocking items — ALL SETTLED 2026-09-07 18:39 (kept for the record)

1. ~~**Cooling-off period.**~~ **DONE** — 4h10m gap, different work in between, re-read performed; three tone-level findings recorded under Gate 4, one of which ("inbred sample") should be changed before sending.
2. **Sergey's own read of the letter.** Revision 3 exists *because* his read of
   revision 1 caught three defects that four round-level skeptic passes had not.
   That is the strongest single argument for repeating it.
3. **The decision to send at all, and the final tone.** A judgment call this gate
   cannot make. Note the standing project constraint: **do not initiate contact
   with Tom** — this exchange was initiated by him, so a reply is in scope, but
   the scope is a reply.
4. **Transcription self-check — partially closed.** Sergey independently flagged
   (107)/(108) before any machine confirmed them, which is the first time the
   human-side check found something first. The seven equations of revision 1 plus
   the four new quotes of revision 3 (§2.2 twice, p.13 bracket, §3.3) are all
   machine-verified and were re-verified by both blind reads, but the same
   caveat stands: a misreading reproduced identically on re-reading is the one
   failure mode this cannot exclude.

## Non-blocking notes

- One check in C179 genuinely cannot fail: `R_spin(4π) = +Id` is the square of
  `R_spin(2π) = −Id`. It is a sanity byproduct, is not load-bearing anywhere in
  the letter, and is recorded here only so it is not later mistaken for
  independent evidence. Flagged by blind read A.
- Blind read A could not open the `.py` files (long Windows path with Cyrillic
  and spaces) and verified against the JSONs and PDF only. It said so explicitly
  rather than papering over it. Its coverage of the exact algebra of the
  projection formula was therefore weaker than B's — which is precisely the gap
  where B found finding #2. The two reads were complementary by accident as well
  as by design.

---

## POST-SEND re-check, 2026-09-07 evening — one imprecision found, in the sent text

A full re-verification of every checkable claim was run *after* sending, at
Sergey's request. **The physics is clean; one parenthetical aside is not.**

### The finding

> §3: *"the standard `S³` Dirac degeneracies, in the form Camporesi and Higuchi
> give them (gr-qc/9505009); note the reindexing, **my `k` is their `n`**."*

That last clause holds on **one branch only**. Mapping each level to the standard
`±(n + 3/2)`, multiplicity `(n+1)(n+2)`:

| our `k` | branch | physical `λ` | their `n` |
|---|---|---|---|
| 0 | `−` | `−3/2` | 0 |
| 1 | `−` | `−5/2` | 1 |
| 1 | `+` | `+3/2` | **0** |
| 2 | `−` | `−7/2` | 2 |
| 2 | `+` | `+5/2` | **1** |
| 3 | `−` | `−9/2` | 3 |
| 3 | `+` | `+7/2` | **2** |

So `n = k` on the negative branch and `n = k − 1` on the positive one. Equivalently:
the two multiplicity families the letter quotes, `(k+1)(k+2)` and `k(k+1)`, are the
**same** formula `(n+1)(n+2)` evaluated at `n = k` and `n = k − 1`.

**What is NOT wrong:** the spectrum table, both multiplicity formulas, and the
`c = 3/2` discussion. Every level is self-consistent between its eigenvalue and its
multiplicity (checked both ways, 7/7). The defect is confined to the one-clause
reading guide.

**Root cause, worth naming:** this was the only claim in the letter about *someone
else's paper's conventions*. Its existence was verified via literature search; its
**indexing convention was not**, and the aside was written from the shape of our own
table. Everything else in the letter was checked against either our own JSON or a
verbatim read of Tom's PDF — this was the one sentence with neither backing.

### Everything else re-verified clean

Dimensions (`(½,½)` = 4, `(½,0)⊕(0,½)` = 4, `d = 2^{(n+1)/2}`), no `S³` zero modes
(`|λ| ≥ 3/2`), `2l+1` / `2(l+1)`, the `1+3+1+3+4+4 = 16` decomposition,
`R_spin(2π) = −I` and `R_spin(4π) = +I`, the projection exact in the quaternionic
basis and off by `i` in the plain Pauli basis, and all three of Tom's typesetting
slips.

### Disposition

**No correction sent, and the .docx/.pdf on the Desktop deliberately reproduce the
text AS SENT** — including this clause. Altering them would make our record diverge
from what Tom actually holds, which is worse than the imprecision. If a further
letter goes out, fix it there in one line.
