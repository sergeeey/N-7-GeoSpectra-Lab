# C157 — Decision

**Date:** 2026-09-05. **Tier:** FL Full. **L0:** descriptive.

**Verdict under the user's own five-gate mandate: TRUE, PROVEN, VERIFIED —
NOT A DISCOVERY. The novelty gate fails explicitly. Reported as the correct
completion of the protocol, not as a partial success.**

## The five gates, scored honestly

| gate | result |
|---|---|
| **1. Theorem** | **PASS.** Proved before any census ran: chirality balance is the vanishing `e^0`-coefficient of the Weyl denominator, since `rho != 0` and `W` acts by isometries. One imprecision in the original wording (cited `rho`'s regularity instead of the simpler isometry argument) — caught by the skeptic, corrected, re-verified. |
| **2. Out-of-sample verification** | **PASS**, with the right caveat: this is a proven theorem, not an empirical pattern, so "out-of-sample" means computational verification across systems never used to derive it — done on 18 root systems, all balanced exactly, including `E_6` at `|Z| = 13,697,920` split evenly. Not the same epistemic status as C155/C156's genuinely predictive out-of-sample tests. |
| **3. Null model** | **PASS with an admitted limitation.** Random sets of the same shape balance far less often than 100% at small/moderate `N` (1–35%), unlike C156 where the null model was 100% and killed the hypothesis outright. Limitation, stated up front and confirmed by the skeptic: the random rate rises toward the true value as `N` grows (85% at `N=16`), so the null model has real discriminating power at small `N` and weak power at the scale (`E_6`, `N=36`) where it matters most. The theorem's proof, not the null model, is what actually rules out coincidence at that scale. |
| **4. Novelty audit** | **FAIL.** The theorem is the `lambda=0`, `r=T` special case of the Gross–Kostant–Ramond–Sternberg formula (1998, arXiv:hep-th/9910119 Eq.2), built on Kostant's own cubic Dirac operator — the same operator this project's C144 already identified as the origin of `D_Sigma`. Classical, not new. This was the pre-registered expectation, written down before the proof was attempted. |
| **5. Independent skeptic pass** | **RUN, response matrix below.** |

**Gate 4 failing is decisive under the mandate: this is not a discovery,
regardless of how cleanly gates 1–3 and 5 passed.**

## Skeptic (FL Step 8a) — Response Matrix

Context-blind, no session history. Reported honestly it had **no shell/python
execution** in that session and did everything by hand (full `2^N` enumeration
for `A_2`, `G_2`; hand-verified Cartan integers and reflection closure for a
sample of `E_6` root pairs). Per `audit-verification-gate.md` its
`[CONFIRMED-REAL]` is `[HYPOTHESIS]` here until I re-verify with a tool.

| # | skeptic point | my tool verification | response |
|---|---|---|---|
| 1 | re-derived the proof independently; hand-enumerated `A_2` (1+1) and `G_2` (2+2) via full `2^N`, matching exactly | consistent with the DP census already run | **Accepted** |
| 2 | flagged an imprecision: the proof cited `rho`'s *regularity* where the simpler *isometry, `rho != 0`* argument suffices | re-derived and confirmed the simpler argument is correct and sufficient | **Accepted, claim.md corrected** |
| 3 | hand-checked a sample of `E_6` pairwise inner products and a few reflections, concluded the construction is a genuine `E_6` | **RAN A FULL (not sampled) computational check**: all `36` roots have squared length `2`; all `C(36,2)=630` pairwise inner products lie in `{-1,0,1}` (valid Cartan integers for simply-laced); **zero** reflection-closure violations across all `36x35` ordered pairs | **CONFIRMED independently and exhaustively** — this closes the one gap the round had not verified beyond the root count |
| 4 | null model has decaying power at large `N`, `E_6` untested and likely poorly discriminated | already stated in `claim.md` before the skeptic ran; skeptic's own attempted extrapolation (interpolating the `N/dim` ratio) guessed `50-80%` for the `E_6` shape, explicitly caveated as a guess | **Accepted**, consistent with what was already disclosed |
| 5 | could not fetch `arXiv:hep-th/9910119` directly (no network tool) but independently re-derived that the `lambda=0, r=T` collapse of the standard Dirac-cohomology character identity gives exactly this result, calling it "elementary and classical" on mathematical grounds alone | I DID fetch the paper directly (`mcp__arxiv__download_paper`) and quoted Eq.(2) verbatim in `novelty_check.md` — the skeptic's independent mathematical argument and my direct citation agree | **Confirmed by two independent routes** (direct citation + independent re-derivation) |

**No concern dismissed. One correction made (regularity → isometry). One gap
closed with a stronger check than the skeptic could run (exhaustive, not
sampled, `E_6` root-system validity).**

## What survives, stated plainly

1. A genuine, correctly-proved theorem: invariant spinors on any full flag
   manifold split evenly by chirality, independent of root-count parity —
   resolving the question C156 left open (`G_2`, `A_2 x A_2` both `N`-even).
2. Independent, tool-verified confirmation that the round's `E_6` construction
   is a real `E_6` root system (exhaustive Cartan-integer and
   reflection-closure check), not merely a count match.
3. A correction to the proof's own wording, caught by adversarial review.
4. Honest closure: **not a discovery**, by the explicit mandate. The result is
   real mathematics, independently re-derived, but it already exists in the
   literature this project's own C144 already cited.

## What this does NOT establish

1. Not a discovery — gate 4 fails explicitly.
2. Nothing about `N_gen = 3`, `lambda`, triality, or any physical claim.
3. No canonical parity-reversing involution was exhibited (the theorem proves
   equal counts via a character identity, not a bijection). Genuinely open,
   separate, and likely harder.
4. The null model's finding is solid for small/moderate `N` only; it says
   nothing decisive about `F_4`/`E_6`-scale genericity on its own — the proof
   does that work instead.

## Reproduce

```
python c157_step1_root_systems.py   # root system data, self-checked counts
python c157_step2_census.py         # P1 exhaustive census + P4 regression
python -u c157_step3_null_model.py  # P3 null model (state-guarded)
```
