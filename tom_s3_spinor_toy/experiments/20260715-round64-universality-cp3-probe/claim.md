---
# Round64-Universality-CP3-Probe Claim — cheapest differentiating test, NOT a full generalization

**Date:** 2026-07-15
**FL tier:** [x] Standard
**Question type:** [x] descriptive

---

## Prior Result Gate (MANDATORY — filled BEFORE computing anything)

1. Exact claim: does the SAME method used for L4A's norm-bound ratio
   `‖F_{S^-}‖_F/(R/4) = 8/45` on `S⁶=G₂/SU(3)` give a quick (same-session)
   answer — of EITHER sign — when applied to `CP³=Sp(2)/(Sp(1)×U(1))`,
   the other nearly-Kähler 6-manifold flagged in Round 51 as having
   directly reusable Casimir formulas (Charbonneau-Harland 2016)?
2. `decision.md` grep (formula + synonyms "CP3", "Sp(2)", "universality"):
   [x] done — Round 51's own `decision.md`/`claim.md` scope the COST of a
   full L4A/L4B-equivalent derivation for CP³ (found: expensive, ~30-min
   follow-on claim was wrong), but do not themselves compute any bound,
   ratio, or spectrum for CP³. 0 hits for an actual computed number.
3. `round*_claim.md` + scripts grep: [x] done, 0 hits — no script in this
   repo currently touches `Sp(2)` or `Sp(1)` representation theory.
4. `null_results/` + `parked/` grep: [x] done, 0 hits for CP3/Sp(2)/Sp(1)
   /universality beyond Round 51's own scoping (already read in full).
5. `git log -S`/`-G` pickaxe: [x] done (`git log --all -S"Sp(2)"` and
   `-S"CP3"` on this dir), 0 hits outside Round 51's text.
6. Primary source re-read: [x] Charbonneau-Harland 2016 PDF present in
   repo root (`Charbonneau_Harland_2016_NK_instantons.pdf`, downloaded
   this session) — re-read directly by the executing agent, not from
   memory or from Round 51's summary of it.
7. **Status:** [x] NEW — no prior round computed this number.

---

## Estimand

**Population:** The nearly-Kähler homogeneous 6-manifold
`CP³ = Sp(2)/(Sp(1)×U(1))` (Butruille's classification), analogous role
to `S⁶=G₂/SU(3)` in this paper's L4A argument.

**Intervention:** Apply the SAME Weitzenböck norm-bound construction used
in `preprint.tex` §sec:lichnerowicz (`R = 30/ρ⁶²` scalar curvature form
for a round nearly-Kähler space; `‖F_{S^-}‖_F` via a Casimir formula for
the relevant twisting representation of the isotropy group) to CP³'s own
isotropy group `Sp(1)×U(1)` and its analogous twisting bundle, using
Charbonneau-Harland 2016's own Casimir formulas (reused verbatim, not
re-derived) wherever the representation-theoretic setup transfers without
modification.

**Comparator:** `S⁶`'s own ratio `8/45 ≈ 0.178` (this paper's existing L4A
result) and its sign (curvature endomorphism has at least one negative
mode of magnitude ≥ R/4, required for a nonzero kernel — this is a
NECESSARY condition for the Atiyah-Singer index to be realized by an
honest kernel, not an artifact of positivity).

**Endpoint:** The analogous ratio `‖F_{S^-}‖_F/(R/4)` for CP³ (or the
closest well-defined analog reachable without inventing new
representation-theoretic machinery), and whether it is ≥ 1 (same
qualitative regime as S⁶'s exact spectral value 1, not the estimated
8/45) or provably < 1 everywhere (which would forbid a zero mode by the
same Bochner argument S⁶'s open problem describes — i.e. NO kernel, a
genuine structural NULL for fermion generations on CP³ specifically).

**Summary measure:** A single computed ratio (or a provably-signed
inequality if the exact value needs machinery beyond this probe's scope).

**MCID:** Not applicable in the usual sense — this is a scoping probe,
not a hypothesis test with a practical-significance threshold. The
practical threshold is procedural: computable in ONE session using
ONLY formulas Charbonneau-Harland 2016 already provides, or STOP.

---

## Claim

**Falsifiable statement:** Using ONLY the Casimir/branching data already
extracted and cited by Round 51 from Charbonneau-Harland 2016 (no new
representation-theoretic derivation), the CP³ analog of the L4A
norm-bound ratio is computable within this single-session probe.

Supporting sub-claims:
1. CP³'s isotropy representation decomposition for the analog of `S^+⊗S^-`
   (or the closest analogous twisted bundle CH2016's own instanton
   deformation-space setup provides) is stated explicitly in
   Charbonneau-Harland 2016 without requiring a fresh derivation.
2. The scalar curvature `R` and a Casimir-based norm bound for the
   twisting curvature are both obtainable from CH2016's stated formulas
   with only substitution of CP³'s own structure constants (isotropy
   dimension, Casimir normalization), analogous to how S⁶'s `8/45` was
   obtained in this paper.

---

## Kill criterion (MANDATORY — filled BEFORE running)

> What exact result STOPS this probe and reclassifies it (not a failure —
> a valid, cheap answer either way)?

| Outcome | Verdict |
|---|---|
| Ratio computable this session from CH2016 formulas alone, value ≥ 1 (same regime as S⁶) | PROMOTE (weak positive signal for universality — NOT a full generalization, just "not obviously ruled out") |
| Ratio computable this session, value found to be < 1 everywhere on the relevant fibre (provably no negative mode reaching R/4) | STRUCTURAL-NULL (genuine negative result: CP³ cannot host the analogous zero mode by this mechanism — a real, cheap, citable finding) |
| CH2016's formulas do NOT directly cover the needed representation (a genuine NEW branching-rule derivation is required, as Round 51 warned) | INCOMPLETE-MACHINERY — matches Round 51's cost re-estimate exactly; STOP here, do not improvise a derivation, report back and re-confirm Round 51's ~0.3-0.5 priority stands unchanged |
| The "S^+⊗S^-"-analog bundle on CP³ is not even the right object (CH2016 studies instanton deformations of the CANONICAL CONNECTION on the ADJOINT bundle, not a spinor kernel problem, per Round 51's own T3 finding) | ILL-POSED — this probe itself was mis-scoped; report why and stop, no computation to force |

**Explicit escape route:** if after ONE session (no multi-day continuation)
none of PROMOTE/STRUCTURAL-NULL is reached, default verdict is
INCOMPLETE-MACHINERY or ILL-POSED — both are valid, cheap, honest
outcomes. Do NOT extend into a second session "just to finish it" — that
would silently convert this from a probe into the expensive multi-round
project Round 51 already correctly declined.

## What this does NOT mean

- Does NOT mean a PROMOTE verdict here proves the L4 mechanism
  generalizes to CP³ — it would only mean the CHEAPEST available test
  did not rule it out, i.e. still worth a future multi-round investment
  if anyone chooses to make it.
- Does NOT mean a STRUCTURAL-NULL verdict here closes Universality for
  ALL nearly-Kähler spaces — only for CP³ specifically, via this specific
  mechanism.
- Does NOT commit to redoing the full L4A/L4B derivation for CP³
  regardless of outcome — that remains explicitly out of scope per
  Round 51's cost re-estimate, which this probe does not attempt to
  overturn.
