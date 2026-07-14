# Round59-TrivialRankCertification Claim — independent verification of rank(D⁺|₁)=1

**Date:** 2026-07-14
**FL tier:** [x] Full (closes the last internally-resolvable conditionality of the
headline N_gen=3 chain; external-facing consequence: preprint L4B upgrade)
**Question type:** [x] descriptive

---

## Prior Result Gate (run 2026-07-13, logged in activeContext.md)

The computation ALREADY EXISTS: `experiments/20260708-dolan-casimir-g2su3/
g2su3_compute_crossterm.py` (commit `2b638c6`, 2026-07-09) gives
`D(v_a) = D(v_b) = -sqrt(3)·w` exactly (sympy), zero leftover components,
implying rank(D⁺|₁)=1. Calibrated against AHL2023 Thm 5.1; passed 2
skeptic-requested stress tests. Status per that experiment's decision.md
(~lines 377-384): **[HYPOTHESIS-STRONG]** — "strong computational evidence,
pending independent sign-off (not yet [CONFIRMED-REAL])".

**This round is therefore a CERTIFICATION round, not a discovery round.**
Per the Verification Strength Ladder, re-running the same scripts (done
2026-07-13, reproduced exactly) is only "same model, isolated context" —
weak. What is missing is **independently-written code + an analytic anchor**,
which this round provides.

null_results check: the only adjacent killed branch is R45-Leibniz
(a structurally tautological blind test in the L4A fork — a test that could
not fail by construction). Lesson imported: every check below must be able
to FAIL (each has an explicit failure signature); no kron-structure
tautologies of the R45 type are used.

---

## Frozen claim

**rank(D⁺|₁ : ℂ² → ℂ¹) = 1** for the physical Levi-Civita twisted Dirac
operator on S⁶ = G₂/SU(3), where the domain is the SU(3)-invariant subspace
of the fibre Σ_odd ⊗ Σ_even (S⁺⊗S⁻) and the target is the SU(3)-invariant
subspace of Σ_even ⊗ Σ_even (S⁻⊗S⁻), Σ = Λ•(ℂ³) per AHL2023 §5.1.

Equivalently: with orthonormal bases u₁,u₂ (domain) and ŵ (target),
D⁺u₁ = a·ŵ, D⁺u₂ = b·ŵ, the exact certificate

    s := |a|² + |b|²  >  0

holds in exact (symbolic) arithmetic, and its POSITIVITY (not its numeric
value) is invariant under every residual convention ambiguity consistent
with the AHL2023 Thm 5.1 calibration anchor.

Consequence if true (combined with the already-certified non-trivial-sector
vanishing, Rounds 52-56): dim ker(D⁺_{S⁻}) = 1, dim ker(D⁻_{S⁻}) = 0 per
channel — the L4B rank hypothesis is discharged.

---

## Method — three routes + adversarial verify (Workflow)

- **Route A (from-scratch reimplementation, PRIMARY):** a new script that is
  FORBIDDEN to read any file in `experiments/20260708-dolan-casimir-g2su3/`.
  Re-transcribes the Clifford action (AHL2023 eq. (5)), the Levi-Civita
  Nomizu map, and the su(3) generators DIRECTLY from the PDF primary source
  (`Agricola_Hofmann_Lawn_2023_invariant_spinors.pdf`, repo root). Gate:
  must reproduce Thm 5.1's Killing-spinor identity exactly (all 6 directions)
  before anything else. Then: find ALL SU(3)-invariants in both fibre blocks
  by nullspace over the FULL 64-dim fibre (not a pre-selected 9-dim block),
  build the twisted D, compute (a,b,s) exactly, and sweep every residual
  sign/phase convention the calibration does not pin. Builder blindness:
  Route A's prompt does NOT contain the known values (−√3, −√3) or the
  expected invariant dimensions.
- **Route B (consistency + completeness on the ORIGINAL implementation):**
  full-64-dim-fibre invariant enumeration (the original searched only a
  9-dim subblock — a completeness gap this closes), Hermiticity/adjoint
  check ⟨D⁺uᵢ, ŵ⟩ = ⟨uᵢ, D⁻ŵ⟩, target-complement residual
  (1−P_tar)D⁺uᵢ = 0 over all 64 coordinates, orthonormal-basis s, and
  basis-rotation invariance of rank.
- **Route C (analytic anchor):** derive from AHL2023 Thm 5.1 alone that the
  untwisted Dirac eigenvalue on the Killing spinors ψ± = 1 ± y₁₂₃ is ∓√3
  (n=6, Killing number 1/(2√3)), then decompose the trivial-block twisted
  map in the Killing basis and derive the certificate in closed form —
  a literature-anchored prediction neither code route can contaminate.
- **Verify:** ≥2 adversarial skeptics with asymmetric context (claim +
  route outputs only, no reasoning chains), tasked to find a common-mode
  convention error that could produce a false s>0 in ALL routes
  simultaneously, and to audit Route A's script for hidden dependence on
  the original code (imports, copied constants beyond the primary source).

## Kill criteria (fixed before running)

| Kill condition | Verdict |
|---|---|
| Route A: a=b=0 in exact arithmetic (calibration passing) | **REFUTED** — rank=0, preprint chain must be re-derived for 2-dim kernel |
| Any calibration-consistent convention variant flips s>0 → s=0 | **UNRESOLVED SIGN BLOCKER** — no promotion |
| Full-fibre invariant search finds domain dim ≠ 2 or target dim ≠ 1 | **FRAMING COLLAPSE** — the ℂ²→ℂ¹ block structure itself is wrong; stop, re-derive |
| Route A calibration cannot reproduce Thm 5.1 after independent transcription | **FAIL-CALIBRATION** — no result either way; transcription discrepancy must be resolved first |
| Hermiticity check fails | implementation error somewhere — no promotion until located |
| Routes disagree on sign/rank | **CONFLICT** — investigate before any status change |

## PASS (all required)

1. Route A calibration exact (6/6 directions).
2. Full-fibre dims = (2, 1) — from both A (fresh) and B (original machinery).
3. Route A's exact s > 0; agrees with Route B's orthonormal s.
4. Convention sweep: s > 0 in every calibration-consistent variant.
5. Route C closed form consistent with the computed (a,b) structure.
6. No skeptic finds a viable common-mode failure or hidden dependence.

## What this does NOT mean

1. Does NOT change L3b (channel independence) — that remains open/external.
2. Does NOT constitute external peer review — this is still internal, though
   at the "independently-written code" rung of the strength ladder (Strong),
   up from "same code re-run" (Weak).
3. Does NOT make N_gen=3 unconditional — it discharges ONE of the two
   conditionality layers (L4B rank), not the other (L3b).
4. Does NOT recompute the non-trivial sectors — those are already certified
   (Rounds 52-56) and are out of scope here.

## Fence

- λ = FREE_COUPLING_PARAMETER (untouched)
- safe_for_runtime = False
- Tom Lawrence: no contact initiated
