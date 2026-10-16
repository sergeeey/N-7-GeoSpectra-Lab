# C196 Claim — S² carries a genuine infinite tower of spin-weighted harmonics, not just χ_{±1/2} in isolation

**Date:** 2026-09-10
**FL tier:** [x] Standard
**Question type:** [x] descriptive [ ] predictive [ ] causal

---

## Prior Result Gate

1. **Exact claim:** applying `C184b`'s exact fibre-descent method at `k=3`
   (instead of `k=1`) produces a second, genuine, double-valued S²
   spin-weighted harmonic (spin-weight 3/2, a DIFFERENT associated bundle
   from the spin-1/2 one `χ_{±1/2}` lives in — see correction note below),
   not proportional to `χ_{-1/2}`.

**Correction (2026-09-10, round-2 skeptic pass on the letter drafted from
this round):** the object this experiment actually produces is spin-weight
**3/2**, not spin-1/2. Hand-refolded from the printed formula:
`(e^{iθ}+1)³·e^{-3i(φ+θ)/2}/8 = cos³(θ/2)·e^{-3iφ/2}` — a `3/2`-power of
`φ`, not `1/2`. The claim's original title and this line both said
"spin-1/2-type"/"S² spin-1/2-type harmonic," which is wrong and was caught
only when drafting external correspondence citing this result, not by this
round's own review. What the round DOES establish, correctly: the descent
method generalizes past `k=1` and produces a genuine tower of half-integer
spin-weighted harmonics (evidence the method is not a `k=1` fluke) — it
does NOT establish a second example specifically of the spin-1/2 (spinor)
content `χ_{±1/2}` carries. See `decision.md` for the full correction.
2. `decision.md` grep: [x] done — `C184b` demonstrates the method ONCE
   (`k=1`); its own negative control is `k=2` (integer weight, single-valued)
   — it never runs `k=3`. 0 hits for this specific extension.
3. Scripts grep: [x] done, 0 hits.
4. `null_results/`/`parked/`: [x] done, 0 hits.
5. `git log -S/-G`: [x] done, 0 hits.
6. Primary motivation: this turn's own synthesis answer to Tom's central
   question (§IV of the letter decomposition) currently rests on `[MEMORY]`
   — "spin-weighted spherical harmonics on S² are standard (Newman-Penrose)"
   — cited, not computed by this project. This round replaces that citation
   with a computed second data point from the project's own machinery.
7. **Status:** [x] NEW

---

## Claim

**H:** the `k=3` fibre-weight `=-3/2` sector, after Hopf substitution and
phase-stripping (C184b's exact method), gives a `(θ,φ)`-function that is (a)
double-valued under `φ→φ+2π` and (b) not a constant multiple of `χ_{-1/2}`.

## Kill criterion

| Kill condition | Threshold |
|---|---|
| Result is single-valued (φ→φ+2π gives back the same function) | would mean the tower does NOT generalize past k=1 |
| Result is proportional to `χ_{-1/2}` | would mean k=3 does not add new content, only rescales k=1 |
| `ψ` fails to strip to a pure phase | would mean the descent method itself does not generalize past k=1 |

## Checks planned

| # | Check | Negative control |
|---|---|---|
| A1 | dimension of k=3 harmonic level = 16 | — (structural sanity check) |
| B1 | k=3 carries only half-integer fibre weights | mirrors `C184b`'s own k=2-carries-only-integer-weights result, opposite parity |
| B2/B3 | each weight sector is 4-dimensional, split by the second generator into 4 distinct `m_R` labels | if the split failed to produce 4 distinct labels, the "degeneracy trap" (`C184b`'s own named risk) would be live here uncaught |
| C1/C2 | ψ strips to a pure phase; result depends on `(θ,φ)` only | — |
| D1 | double-valuedness under `φ→φ+2π` | N1: an ordinary single-valued function (`cos φ`) must FAIL this same test — checked explicitly |
| D2 | not proportional to `χ_{-1/2}` | — |

## What this does NOT mean

1. Does NOT derive the FULL spin-weighted spherical harmonic family
   `_{1/2}Y_{j,m}` for all `j` — one additional data point (`k=3`), not a
   general proof for all `k`.
2. Does NOT contradict `C179`'s no-go (spinor absent from bare `L²(S²)`
   scalar decomposition) — this is about SECTIONS, the route `C179` itself
   named as open.
3. Does NOT settle Tom's central question definitively — strengthens the
   synthesis answer's evidentiary basis, pending his forwarded Jantzen
   correspondence.

## Verdict

**CONFIRMED** — see `decision.md`. `[VERIFIED-sympy 9/9]` (after one
self-caught, corrected wrong prediction — see decision.md §2).
**Status:** CLOSED — PROMOTE.
