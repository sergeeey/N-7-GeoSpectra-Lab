# Submission Gate — draft reply to Tom Lawrence, 2026-09-07

Per `~/.claude/rules/integrity.md` § Submission Gate. Artifact:
`DRAFT_REPLY_TO_TOM_2026-09-07.md`.

## VERDICT: **NOT PASSED — DO NOT SEND YET.** 2 of 4 gates clear, 2 open.

---

## Gate 1 — Adversarial review: **PARTIAL**

| Round | Context-blind skeptic | Verdict |
|---|---|---|
| C179 (the no-go) | run | `CONFIRMED-REAL` — 6 attacks, none broke it; supplied a *second* independent proof for `S³` |
| C180 (the `S³` construction) | run | `WEAKENED` → all 3 concerns closed by added computation |
| C181 (his check + RNC) | **not run** | — |
| C182 (the `S²` descent) | run | `WEAKENED` — found the scalar/spinor 'two checks' are one algebraic identity, and the no-go check was a tautology. **Both accepted and fixed**; the draft's wording was corrected as a result. |
| **The draft letter itself** | **not run** | — |

**Open:** the C181 skeptic pass, and no adversarial read of the letter
*as a letter* (tone, overclaim, anything that reads stronger than what was
proved).

**Track record so far — the reason this gate is not a formality:** of the
three skeptic passes completed, two returned `WEAKENED` and between them
found four real defects (a missing negative control, an imprecise citation,
a pair of "checks" that were one algebraic identity, and a check whose
condition was logically impossible so it could never fail). All four were
accepted and fixed, and one of them forced a correction to this very
draft. A fourth pass is outstanding.

## Gate 2 — Evidence markers on every claim: **CLEAR**

| # | Claim in the draft | Marker | Source |
|---|---|---|---|
| 1 | The July transpose finding; `L_x` opposite sign, `L_y`/`L_z` fine | `[VERIFIED]` | `20260728-tom-so3-harmonics-sign-check/TRANSPOSE_LEMMA.md` |
| 2 | 2π rotation = identity on functions | `[VERIFIED-tool]` | C179: point shift `3.3e-16`, function-value change `1.8e-15` |
| 3 | 2π rotation = `−1` in Spin(n+1) | `[VERIFIED-tool]` | C179, exact, both `d=2` and `d=4`; `4π → +Id` control passes |
| 4 | Therefore no spinor multiplet of functions on `S²` or `S³` | `[VERIFIED-tool]` | C179 |
| 5 | This resolves his `[*check*]` on §2.2 | `[INFERRED]` | interpretive reading of his own marker — correct as far as it goes, but it is our reading of his intent |
| 6 | His footnotes 1 (p.3) and 2 (p.11) already flag the area | `[VERIFIED]` | direct read of the PDF |
| 7 | Dimension trap: `dim(½,½) = dim[(½,0)⊕(0,½)] = 4`; kernel phase `+1` vs `−1` | `[VERIFIED-tool]` | C179 |
| 8 | `S³ = SU(2)` is parallelizable | `[DOCS]` | standard |
| 9 | `D₀` spectrum table (`k=0..3`) | `[VERIFIED-tool]` | C180 |
| 10 | Multiplicities `(k+1)(k+2)`, `k(k+1)` are the standard `S³` Dirac degeneracies | `[VERIFIED-tool]` | `c85_certification.py`. **Note:** round67's own statement of this is marked `[INFERRED]` in its `claim.md:73` — cite c85, not round67 |
| 11 | `c = 3/2` emerges uniquely | `[VERIFIED-tool]` | C180, intersection over 7 independent pairs |
| 12 | Lowest harmonics are the two constant spinors | `[VERIFIED-tool]` | C180 |
| 13 | `S²` is not parallelizable | `[DOCS]` | hairy-ball theorem |
| 14 | `S²` descent dimensions 1,3,5 and 2,4,6 | `[VERIFIED-tool]` | C182. **Note:** these are ONE fact (both equal `k+1`), not two independent confirmations — the draft now says so explicitly |
| 14b | Weight-0 fixed by the fibre; weight-`½` picks up `−1` on a half-turn | `[VERIFIED-tool]` | C182 `fibre_invariance_check`: drift `1.2e-15` vs `0.686`, phase `+1` vs `−1`. This is the genuinely independent check |
| 15 | `2l+1` and `2(l+1)` are the standard counts | `[DOCS]` | textbook |
| 16 | Half-integer weights only at odd `k`, and non-zero | `[VERIFIED-tool]` | C182 |
| 17 | `x_μ = ½Tr(σ_μ†g)` recovers the vector exactly | `[VERIFIED-tool]` | C181, error `0.0` |
| 18 | `ψψ†` (one chirality) has invariant trace → `1 ⊕ 3` | `[VERIFIED-tool]` | C181, `3.6e-15` |
| 19 | Opposite-chirality alternative passes the same check | `[VERIFIED-tool]` | C181 |
| 20 | Constant is `+3/2` vs `−3/2` by chirality | `[VERIFIED-tool]` | C180 skeptic follow-up |
| 21 | RNC: `g(0)=δ` on 5 exact directions, all 9 first derivatives vanish | `[VERIFIED-tool]` | C181 |
| 22 | Scope statements ("haven't built the `S²` Dirac operator", "groundwork only") | `[VERIFIED]` | accurate — matches what the rounds actually did |

No claim in the draft is unmarked, and no claim rests on `[MEMORY]`.

## Gate 3 — Internal consistency (text vs. data): **CLEAR**

Every number in the draft was re-checked against the results JSON this
session:

- `D₀` table `(0,2) / (−1,6),(3,2) / (−2,12),(4,6) / (−3,20),(5,12)` —
  matches `results_c180.json` exactly.
- `c = 3/2`, unique over 7 pairs — matches `results_c180.json`.
- `S²` dimensions `1,3,5` and `2,4,6` — match `results_c182.json`.
- `0.0`, `3.6e-15`, `3.3e-16`, `1.8e-15` — match their respective JSONs.
- All three scripts re-run from scratch this session; verdicts reproduce.
- `pytest`: 2524 passed, 4 skipped, 0 failures.

## Gate 4 — Cooling-off: **NOT OBSERVED**

The draft was written in the same session as the results. Per the rule,
the moment right after declaring something ready is the least reliable
moment to judge readiness. **Re-read after a break before sending.**

---

## Blocking items before this may be sent

1. **Human re-read of the equation transcription.** The draft quotes and
   relies on Tom's eqs (4), (40), (61), (72), (77), (89), (99). These were
   read off the PDF by machine and re-checked once by the same process.
   The C179 skeptic explicitly named this as the one risk a self-check is
   weakest against and could not verify it independently. **Sergey should
   re-read those equations against the source.**
2. **C181 skeptic pass** — running at time of writing. (C182's is complete; its two findings were accepted and the draft corrected accordingly.)
3. **Adversarial read of the letter itself**, separately from the rounds:
   does anything in it read stronger than what was proved?
4. **Cooling-off period.**
5. **Attribution and tone conventions** for this correspondence — a
   judgment call for Sergey, not something this gate can settle.

## Non-blocking notes

- Claim 5 is `[INFERRED]`, not `[VERIFIED]` — it is our reading of what
  his `[*check*]` marker was asking. Consider softening the wording, or
  simply asking him whether that is what he meant.
- Claim 10 should cite `c85_certification.py`, not round67, if a citation
  is ever added — round67's own version of that statement is `[INFERRED]`
  and self-flagged as un-cross-checked.
