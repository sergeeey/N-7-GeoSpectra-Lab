# OB2/OB6 item 5 Claim — matrix-valued t order parameter with Z2 exchange

**Date:** 2026-08-03
**FL tier:** [x] Standard (self-contained algebraic construction on a finite toy model)
**Question type:** [x] descriptive (finite-geometry/NCG-style classification, not causal)

---

## Prior Result Gate

1. Exact claim: does promoting `t` from a discrete label to a finite
   matrix-valued order parameter `T` (2×2 Hermitian, eigenvalues 0,1)
   admit the internal `Z2` exchange symmetry `T↔1-T` that Codex's item 5
   proposed, and does it hold beyond the special diagonal case round110
   already tried?
2. `decision.md` grep: [x] done —
   `experiments/20260717-round110-codex-item4-block-spectral-triple/
   decision.md` is the only prior attempt; it tested a DIFFERENT
   question (literal self-invariance of `D_block` under a fixed swap)
   and found `False`. No prior round tests the statement this claim
   tests (unitary equivalence of `D(T)` and `D(1-T)`, for general `T`).
3. `round*_claim.md`/scripts grep: [x] done — Codex's own original
   wording located verbatim,
   `experiments/20260717-round105-codex-cross-model-audit/
   codex_review_2026-07-17.md:141-149`.
4. `null_results/`+`parked/` grep: [x] done, 0 hits for this exact
   question.
5. Primary source re-read: [x] done — read Codex's own item-5 text in
   full (not from memory/paraphrase), round110's `decision.md` and code
   in full, `PARENT_ACTION_GATE.md`'s OB2-specific 6-field checklist in
   full, and E9's own `H=(3c/2)·ω=3·I₂` calibration
   (`experiments/20260717-round73-e9-explicit-parallel-spinor/`).
6. **Status:** [x] NEW.

---

## Estimand

**Population:** the finite toy Hilbert space `H_int(2-dim)⊗H_spinor(2-dim,
E9's constant spinors)`, carrying a Dirac-type operator `D(T)=T⊗H`.
**Intervention:** promoting `t∈{0,1}` (a discrete external label) to
`T`, a general rank-1 Hermitian projector (a genuine finite matrix-valued
order parameter, per Codex's own proposal).
**Comparator:** round110's own diagonal-only, self-invariance test.
**Endpoint:** whether an internal unitary `S_T` exists with
`S_T·T·S_T⁻¹ = 1-T`, and consequently `(S_T⊗I₂)·D(T)·(S_T⊗I₂)⁻¹ = D(1-T)`.
**Summary measure:** categorical (holds / does not hold), checked exactly
for the diagonal case and via numeric spot-check across the general case.
**MCID:** not applicable — exact algebraic/numeric classification.

---

## Claim

Round110 asked the wrong question (literal self-invariance of `D_block`
under one fixed swap `S`) and correctly found it false. The Z2 exchange
Codex's proposal actually calls for — `D(T)` and `D(1-T)` are unitarily
equivalent via an internal `SU(2)` conjugation — **does hold**, both for
round110's own diagonal special case AND, more importantly, for a
GENERAL matrix-valued `T` (any point on the projector's Bloch sphere,
realizing Codex's "off-diagonal fluctuations possible" language), via
`S_T = m̂·σ` for any unit vector `m̂` orthogonal to `T`'s own axis `n̂`.

---

## Kill criterion

| Kill condition | Threshold |
|---|---|
| `S_T·T(θ,φ)·S_T⁻¹ ≠ 1-T(θ,φ)` at any tested Bloch-sphere point | residual ≥ 1e-10 at any of 8 random trials |
| `T(θ,φ)` fails to be a genuine rank-1 projector for general `(θ,φ)` | `T²≠T`, `T≠T†`, or `tr(T)≠1` symbolically |
| Round110's own diagonal result reproduced incorrectly | `S.D(T).S⁻¹ ≠ D(1-T)` for `T=diag(0,1)` |

If FAIL → kills: the claim that Codex's proposed Z2 exchange is realized
by this natural construction — would leave OB2/OB6 item 5 genuinely
unresolved even at the level of a toy model.
If PASS → survives: the internal Z2 exchange is realized, correcting
round110's mis-posed test and giving OB2 a genuine (if still toy-level)
positive construction toward Codex's proposal.

---

## Checks planned

- T1: `T(θ,φ)` is a genuine rank-1 Hermitian projector for all `(θ,φ)`
  symbolically (sanity gate).
- T2: reconfirm round110's own diagonal-case result (self-invariance
  under the fixed swap is False) — must NOT silently contradict the
  prior round.
- T3 (the actual new content): confirm `S·D(T)·S⁻¹ = D(1-T)` exactly
  for the diagonal case, THEN generalize via numeric spot-check (8
  random Bloch-sphere points, `m̂` built as the normalized cross product
  of `n̂` with a reference axis) — an adversarial widening beyond the one
  case round110 tried, analogous to OB10's 256-candidate widening.

---

## What this does NOT mean

1. Does NOT supply a physical action (F6 of `PARENT_ACTION_GATE.md`
   remains unaddressed — Codex's own text explicitly says "it still
   needs a physical action").
2. Does NOT supply a working grading `γ` or real structure `J` — the one
   naive grading candidate tried (`γ=(I-2T)⊗I₂`) explicitly FAILS
   `{γ,D}=0` and is reported as such, not rounded up to PROMOTE.
3. Does NOT extend beyond the finite constant-spinor toy model — the
   continuum/full spectral-triple question `PARENT_ACTION_GATE.md`
   describes is untouched.
4. Does NOT resolve OB1, OB4, or OB11's remaining conditions — a
   free-standing construction on the OB2/OB6-item-5 question only.
5. Does NOT affect `N_gen=3`, `λ=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`.

---

## Fence

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

**PARTIAL_PASS_Z2_EXCHANGE_VERIFIED_GRADING_AND_REAL_STRUCTURE_OPEN**

**Evidence:** [VERIFIED-sympy 2/3, VERIFIED-numpy 1/3] (T1-T3 all pass;
`PARENT_ACTION_GATE.md`'s 6-field checklist honestly reported as 3
supplied, 1 attempted-and-failed, 1 not attempted, 1 stated as
interpretation).

**Status:** CLOSED PARTIAL_PASS (OB2/OB6 item 5 makes real progress but
is NOT fully resolved — grading, real structure, and the physical action
remain open per `PARENT_ACTION_GATE.md`)
