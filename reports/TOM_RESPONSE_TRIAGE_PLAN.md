# Tom S³ — Response Triage Plan

**Status:** Phase 3 clarification SENT — waiting for Tom's response  
**Created:** 2026-06-07  
**Do NOT start Phase 4 work before Tom answers**

---

## What was asked (pre-registered questions)

**Q1 — Inner product / measure:**
Is the Riemannian volume measure implicit in your S³ orthonormality integral?
i.e., is the norm weighted by sinα cosα dα (= sin(2α)/2 dα)?

**Q2 — Coordinate convention:**
In your notation, should α be understood as the Hopf-type angle (two-plane angle,
α ∈ [0, π/2]) from the angular coordinates r = ρ sinα, r̃ = ρ cosα — or is it
related to the geodesic-polar angle θ ∈ [0, π] from Camporesi-Higuchi?

---

## What is already confirmed (independent of Tom's answer)

| Finding | Evidence | Status |
|---------|----------|--------|
| √sin(2α) = √2 · √(sinα cosα) | test_alpha_ansatz.py, max err 2.22e-16 | [VERIFIED] |
| √sin(2α) is NOT a Dirac eigenspinor | Δf/f std/mean = 4×, overlaps 4+ modes | [VERIFIED] |
| Dirac eigenspinors = weighted Jacobi polynomials | Camporesi-Higuchi eq 3.25 | [VERIFIED_FROM_PDF] |
| √sin(2α) = √(Hopf volume density) · √2 | sinα cosα = √g radial factor | [VERIFIED] |
| S³ volume = 2π² | numerical + analytical | [VERIFIED] |
| Ben Achour scope = vector harmonics, not spinor | Paper title + content | [VERIFIED_FROM_PDF] |

---

## Triage scenarios

### Scenario A — Hopf α + weighted measure (most likely)

Tom confirms:
- α is the Hopf/two-plane angle (α ∈ [0, π/2])
- inner product includes Riemannian measure sinα cosα

**Interpretation:**
√sin(2α) is the square root of the volume density — consistent with the √g expansion.
Measure-vs-mode hypothesis fully supported.

**Next safe step:**
Write `NOTE_FOR_TOM_v1.md` — short technical note with:
- √sin(2α) = √2 · √(sinα cosα) numerical proof (2.22e-16)
- Weighted vs unweighted L² diagram (ALPHA_COMPARISON_PHASE2.png, if Tom requests)
- Caveat: "this is measure-density behaviour in Hopf coordinates, not a full diagnosis"
- Offer: "does this match your expansion framework?"

**Do NOT claim:** "we found your error" / "spin connection was omitted"

---

### Scenario B — Hopf α + unweighted measure

Tom confirms:
- α is Hopf angle
- but inner product does NOT include sinα cosα measure

**Interpretation:**
Measure-vs-mode hypothesis strengthened. The √sin(2α) factor appears as normalization
artifact from working in unweighted L²(S³, dα dθ dφ) instead of weighted L².

**Next safe step:**
Write `NOTE_FOR_TOM_v1.md` with:
- Sturm-Liouville substitution explanation (u = v/√w removes measure from operator)
- √sin(2α) appears as the "trivial vacuum" in unweighted L²
- Suggest: check if weighted inner product removes the factor

**Do NOT claim:** "this is the source of your α-problem" — say "this may explain..."

---

### Scenario C — Geodesic-polar θ (not Hopf α)

Tom confirms:
- he is using geodesic-polar θ ∈ [0, π], not Hopf α

**Interpretation:**
Direct comparison requires coordinate transform. Hypothesized relation: θ_geod = 2α_Hopf.
Our Phase 2 results are in Hopf α coordinates — not directly comparable.

**Next safe step:**
1. Verify coordinate relation θ = 2α (check Camporesi-Higuchi eq 3.1 and Ben Achour eq 1)
2. Re-express Phase 2 results in geodesic-polar coordinates
3. Then ask Tom: "In θ coordinates, does √sin θ appear?" (= √sin(2α) in Hopf)

**Do NOT claim:** results are wrong — they are in a different coordinate system.

---

### Scenario D — Different convention / no clear answer

Tom uses a different parameterization not covered by A/B/C.

**Next safe step:**
Ask one focused follow-up: "Could you write the measure in your orthonormality integral
explicitly? E.g., ∫ f* g · [measure] dα dθ dφ = δ_{fg}?"

Do NOT send code, plots, or long explanations until convention is established.

---

## Forbidden actions until Tom responds

```
❌ Do NOT send a second message to Tom
❌ Do NOT send plots, code, or reports without Tom requesting them
❌ Do NOT start S³ × S⁶ / instanton / chirality analysis
❌ Do NOT run heavy compute
❌ Do NOT build Wigner/Haar analytic backend
❌ Do NOT touch Gate 4B / Negative Controls pipeline
❌ Do NOT claim authorship or priority
❌ Do NOT interpret Tom's framework beyond what he explicitly confirms
```

---

## Untracked files in working tree (do NOT touch for Tom work)

```
reports/GATE4B_REANALYSIS_STATS_2026-06-07.json   ← GeoSpectra main, separate decision
reports/GATE4B_REANALYSIS_STATS_2026-06-07.md     ← GeoSpectra main, separate decision
scripts/reanalyze_gate4b_stats.py                 ← GeoSpectra main, separate decision
```

These belong to the GeoSpectra main / Gate4B track — handle in a separate session.

---

**Last updated:** 2026-06-07  
**Trigger for next update:** Tom's response received
