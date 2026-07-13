# Round56-ExceptionalSet Claim — formal registration/closure

**Date:** 2026-07-13
**FL tier:** [x] Standard (symbolic/mechanical registration, no new computation beyond Round 52-55a.1's already-certified pieces)
**Question type:** [x] descriptive

---

## Prior Result Gate

Direct, mechanical closure of the Round 52→53→54→55→55a→55a.1 chain,
per the reviewer's own explicit 6-step scope (a registration round,
not a search round — all certification work was already done). Status:
OPEN → this round.

---

## Claim

`E_nontrivial = {(1,0)} = {ρ=7}` — the unique nontrivial G₂
representation not certified positive by the general bound
`λ²_min(ρ) ≥ C₂_Bourbaki(ρ) - 3 - (2√6/3)√C₂_Bourbaki(ρ)`. Every other
nontrivial G₂ representation, starting from ρ=14 (adjoint), is
certified positive by this single, general, already-proven bound — no
case-by-case computation needed beyond what Round 52-55a.1 already
established.

**This does not mean ρ=7 has a bad zero mode.** Its Levi-Civita
invertibility is already independently, explicitly ESTABLISHED
(Round 22, preprint.tex §sec:schur) — the general bound simply doesn't
certify it (a known, small-margin case, matching why it was flagged
"the single most exposed block" back at the very start of this
investigation, colloquially "Round 6").

---

## Kill criterion

| Kill condition | Threshold |
|---|---|
| `K_N√C_N ≠ K_B√C_B` identity fails | any symbolic mismatch |
| `C_*` doesn't match `(13+2√22)/3` | any mismatch |
| Enumerated exceptional set ≠ `{(1,0)}` | any extra or missing label |
| `f(4)≥0` or `f(8)≤0` | regression failure |

All 4 checked: PASS (script exits 0, all assertions hold).

---

## What this does NOT mean

1. Does NOT claim ρ=7 has an undesired zero mode — its status is
   UNCHANGED from Round 22's own independent, explicit computation
   (established, Levi-Civita invertible).
2. Does NOT compute any new representation's spectrum.
3. Does NOT change `preprint.tex` in this round (a citation-only update
   reflecting this closure is a natural follow-on, not done here
   without separate confirmation).
4. Does NOT claim the bound is tight — `ρ=14`'s margin (`f(8)≈0.381`)
   is small but strictly positive and exact (closed-form radicals, not
   a numerical approximation).

---

## Fence

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

**PASS.** `E_nontrivial = {7}`, registered. See `decision.md` for the
full closure summary of the Round 52→56 arc.
