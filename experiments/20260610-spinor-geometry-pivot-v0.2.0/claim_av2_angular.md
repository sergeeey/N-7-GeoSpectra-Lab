# AV-2 — Pre-registered Claim: Full Angular/Spinor Sector and the Boundary Obstruction

**Experiment:** AV2_FULL_ANGULAR_SPINOR_SECTOR
**Date pre-registered:** 2026-06-10 (design only — implementation NOT started)
**Question type:** [x] descriptive  [ ] predictive  [ ] causal
**Status:** research_only — no physical promotion

---

## Central Estimand

*Does the full angular/spinor structure of S³ Dirac eigenmodes
(half-integer Hopf weights, spin connection, 2-component structure)
change the effective boundary exponents at α → π/2 enough to explain
Tom's eq. 49 expansion of √||g|| without requiring a dense radial fit?*

Population: S³ Dirac eigenspinors, levels n ≤ 6, all sectors.
Comparator: the radial-proxy picture of AV-1/AV-1c′ (boundary obstruction:
cos¹ target vs cos² bilinears; dense series; f^(φ) required).
Endpoint: measured boundary exponent of angular-singlet bilinear densities;
sparse-reconstruction residual of √||g|| in the full treatment.
MCID: a change of boundary exponent by ≥ 1 (cos² → cos¹) OR sparse residual
dropping below 5% counts as "obstruction lifted".

## Motivation (from null_results/20260610-ht1-sparse-bilinear.md)

The radial-proxy obstruction is structural: every radial bilinear vanishes
≥ cos²α at α → π/2 while sin(2α) vanishes as cos¹α. BUT the radial proxy
treats φ_{nl}(α) alone. The full eigenspinor carries:
1. half-integer angular weights e^{i(mθ + m'φ)}, m, m' ∈ ℤ + ½,
2. a 2-component spinor structure with PARTNER radial function g_{nl}
   (mirror under α → π/2 − α: g_nl ∝ sin^{l+1}·cos^l — vanishes as cos^l,
   i.e. cos⁰ for l=0 at the π/2 boundary!),
3. spinor bilinears ψ̄ψ that mix φ- and g-components.

**Pre-registered hypothesis H-AV2:** bilinears of the form g̅·g (partner ×
partner) have boundary exponent cos^{2l} — for l=0 that is cos⁰ — so MIXED
bilinear densities (φ̄φ + ḡg combinations) can produce the cos¹ behavior
that pure φ̄φ cannot. If true, eq. 49 admits a sparse expansion in FULL
spinor bilinears, and the AV-1c′ obstruction was an artifact of projecting
out the partner component.

This is falsifiable and decisive either way:
- obstruction lifts → Tom's eq. 49 sparse structure restored at full level;
- obstruction persists → dense-series conclusion is final, fundamental.

## Gates and Endpoints (in order; each gates the next)

| Gate | Check | Kill condition |
|---|---|---|
| AV2-G0 | Source trace (Step -4): verify from C-H PDF the full eigenspinor form incl. partner component normalization and angular weights; verify spin connection in Hopf coords from a primary source | formula not verifiable from PDF → STOP, no implementation from memory |
| AV2-G1 | 2-component radial system (φ, g) reproduces λ = ±(n+3/2) AND both components match C-H analytic forms (rel. error < 1e-4) | spectrum wrong → implementation invalid, fix before any claim |
| AV2-G2 | Boundary exponent measurement: numerical log-log fit of mode densities near α = π/2; confirm φ-bilinears → cos², measure g-bilinears (prediction: cos^{2l}) | exponents contradict analytic forms → numerics broken |
| AV2-E1 (PRIMARY) | Sparse reconstruction of sin(2α) over MIXED bilinear dictionary {φ̄φ, ḡg, φ̄g} + const, greedy ≤5 terms | residual > 10% → obstruction persists at full level → dense conclusion FINAL |
| AV2-E2 | If E1 passes: angular singlet check — verify the chosen bilinears can pair to total-angular-momentum singlets (required for a scalar √||g||) | no singlet pairing → reconstruction is formal, not eq.-49-meaningful |

Verdict rules (pre-registered):
- E1 residual < 5% AND E2 singlet check passes →
  item 40 upgrades to RADIAL+ANGULAR_BILINEAR_SUPPORTED (still NOT
  "Tom's ansatz solved"; still no physical promotion).
- E1 < 5% but E2 fails → FORMAL_FIT_ONLY — no upgrade.
- E1 > 10% → obstruction persists; record in null_results/ as final;
  eq. 49 radial layer is dense, period.

## Known Risks (declared)

1. Spin connection in Hopf coordinates is the highest hallucination-risk
   step — hence AV2-G0 source-trace gate is BLOCKING.
2. The g-component boundary behavior claim (cos^{2l}) is [INFERRED] from
   the mirror structure g_nl ∝ sin^{l+1}cos^l — must be re-derived from
   the PDF at G0, not trusted from this document.
3. 2D angular operator may be unnecessary if G1+G2 suffice — prefer the
   2-component radial system over a full 2D lattice (cheaper, fewer
   discretization artifacts). Full 2D lattice only if E2 demands it.

## Sensitivity (≥2)

1. Two measures (weighted / unweighted), as in AV-1.
2. Grid refinement 4000 → 8000.
3. Boundary-fit window variation (log-log fit range ×2, ÷2).

## What This Will NOT Mean (pre-declared, regardless of outcome)

1. No statement about S⁶, f^{αχ} cross-couplings, SU(4)/SU(3) sector.
2. No physical promotion; λ = FREE_COUPLING_PARAMETER.
3. PASS ≠ "Tom's ansatz solved" — it would mean: the radial+angular
   bilinear layer of eq. 49 on the S³ factor is sparse-representable.
4. Nothing about S³×S¹ / GEOMETRY_AGNOSTIC (that is BG-1/2/3, separate track).
