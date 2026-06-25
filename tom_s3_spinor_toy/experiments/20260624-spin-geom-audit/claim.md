# Spin Geometry Audit — Lemmas L1–L5

**Date:** 2026-06-24
**Auditor:** Claude Sonnet 4.6 (context-asymmetric, no session history)
**Subject:** preprint.tex §3–§4 (N_gen=3 proof)
**Method:** Adversarial review — falsification-first, claim.md + code only, no reasoning chain

## Estimand (L0)
- **Question type:** Descriptive (is the mathematical argument valid as written?)
- **Claim being audited:** N_gen=3 follows exactly from Atiyah-Singer index theorem on S⁶=G₂/SU(3) via lemmas L1-L5
- **Population:** The specific mathematical argument in preprint.tex §3.1–4.3

## Lemmas audited

| Lemma | Description | Verdict | Confidence |
|-------|-------------|---------|------------|
| L1 | S⁻ ≅ T^{1,0}S⁶⊕1 | VALID (with standard ref needed) | HIGH |
| L2 | c₃(S⁻)=χ(S⁶)=2, Â=1, ind=1 | VALID (KN1969 ref covers non-integrable case) | HIGH |
| L3 | Z₃ triality channels independent | **FLAWED** | HIGH |
| L4A | Lichnerowicz gap → dim ker = \|ind\| | **FLAWED (self-contradictory)** | HIGH |
| L4B | G₂-Schur caps kernel at 1 | **FLAWED (Schur ≠ L²-sections)** | MEDIUM |
| L5 | sign(ind)=+1 → left-handed | VALID (one discrete input: orientation) | HIGH |

## Detailed findings

### L3 — Triality channels (CRITICAL)
**Gap:** The argument conflates two different Z₃ groups:
- Z₃ ⊂ G₂ — isometry of S⁶, acts on sections of spinor bundle
- Z₃ ⊂ Aut(SO(8)) — outer automorphism of abstract Lie group, does NOT act on S⁶ sections

If only Z₃ ⊂ G₂ is used: the kernel of D has total dim=1. Z₃ partitions it into eigenspaces summing to 1, not three independent modes.

**What's needed:** Either (a) construct three EXPLICIT G₂-equivariant bundles E₀, E₁, E₂ and compute ind(D⊗Eₐ)=1 for each separately, or (b) invoke a specific theorem about the G₂-representation content of the kernel.

### L4A — Lichnerowicz self-contradiction (HIGH)
**Gap:** The argument states R/4 > |F| → spectral gap → ker = index-required modes only.
BUT: if (R/4 + F) > 0 as an operator everywhere, then ker(D) = 0. This contradicts ind ≠ 0.

The correct argument requires: the curvature endomorphism (R/4 + F_{S⁻}) has negative modes precisely on the index-required subspace of the kernel, and positive definite on the rest. This is a much more specific statement that needs to be derived, not just from the ratio 8/45.

**Reference needed:** Cahen-Gutt 1988 or Bär's work on Dirac operators on homogeneous spaces — explicit spectral calculation.

### L4B — Schur's lemma on L²-sections (MEDIUM)
**Gap:** Schur's lemma bounds multiplicity of a representation in a FINITE-DIMENSIONAL G-module (a fibre). The kernel of an elliptic operator is infinite-dimensional before taking the relevant eigenspace.

The correct argument requires G₂-equivariant Atiyah-Singer theorem with explicit character computation showing that the zero modes of D⊗S⁻ transform trivially under G₂.

The fibre multiplicity argument (mult(trivial G₂, T^{1,0}S⁶)=0, mult(trivial G₂, 1)=1) is suggestive but not a proof — it needs to be backed by the full representation-theoretic computation.

## What is NOT in dispute
- The index formula computation: ind = Â·c₃/2 = 1·1 = 1 ✓
- c₃(T^{1,0}S⁶) = χ(S⁶) = 2 on almost-Hermitian manifolds ✓
- Â(S⁶) = 1 (from H²=H⁴=0) ✓
- sign(ind) = +1 → left-handed (one Z₂ input) ✓
- The uniqueness argument (only S⁶ among NK6 has G₂ and χ=2) ✓
