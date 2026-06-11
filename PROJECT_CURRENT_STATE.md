# Project Current State

**Last authoritative commit:** `e2931e3` (HEAD = origin/main after push)
**Authoritative date:** 2026-06-11
**Branch:** `main` — clean, synced with origin/main
**Tests:** 415 passed, 2 skipped (main); 191 passed (preserve/tom-s3-p5-p14-scaffold)

---

## Sync Protocol — Run Before ANY Work

```bash
git fetch --all --prune
git pull --ff-only
python -m pytest tom_s3_spinor_toy/tests/ -q --tb=no
```

Expected output: `415 passed, 2 skipped`. If fewer → you are behind.

After work (before switching machines):

```bash
python -m pytest tom_s3_spinor_toy/tests/ -q --tb=no
git add <specific files>
git commit -m "type(scope): description"
git push
```

WIP checkpoint if leaving mid-task:

```bash
git add . && git commit -m "WIP: checkpoint before switching machine" && git push
```

**Rule:** session summaries older than the latest origin/main commit = historical,
NOT current roadmap.

---

## Completed Tracks (do not re-open without reading null_results/ first)

### AV-2: Full Angular/Spinor Sector ✅ COMPLETE

All gates passed. Item 40 is final.

| Gate | Result | Key finding |
|---|---|---|
| G0 — Source trace (C-H PDF) | ✅ PASS | g_nl_hopf IS C-H eq 3.27; eqs 3.29-3.30 absorb spin connection |
| G1 — 2-component first-order system | ✅ PASS | 24 tests; eq 3.28 ≤2.3e-15, eq 3.38 ≤6e-16 |
| G2 — Boundary exponent measurement | ✅ PASS | g_l0≈0 at boundary (nonzero); mixed_l0=0.928≈cos¹; 45 tests |
| E1 — Sparse mixed bilinear dict | ✅ STRONG_PASS | **1 term, 0% residual** — φ_{0,0}·g_{0,0} = cosα·sinα = sin(2α)/2 **analytically exact** |
| E2 — Angular singlet check | ✅ PASS | CG singlet=√2/2, C²=0.5>0; SU(2) singlet pairing confirmed |

**Item 40 final status:** `RADIAL + ANGULAR_BILINEAR_SUPPORTED`
The AV-1c′ obstruction was an artifact of projecting out the partner component.
Full spinor bilinears (φ·g cross-term) restore exact sparse representation.

### BG-H1: S³×S¹ KK Bridge Gate ✅ COMPLETE

| Gate | Result | Key finding |
|---|---|---|
| G0 — Source trace | ✅ PASS v1.1 | Joint mechanism: {Γʲ,Γ⁴}=0 ∧ [∇ⱼ,∂_y]=0; cross-terms vanish together, not independently |
| G1 — Product Dirac cross-check | ✅ PASS | D4²=-(k²+p²)·I₄, max_rel_error=0.0; 58 tests |
| E1 — Discrete S³×S¹ proxy | ✅ PASS | k₀(N=4000)=1.4999999561; max_rel_err=2.93e-08; 72 tests |
| E2 — Disorder robustness W=0.5 | ✅ PASS | max_frag_ratio=0.998; max_mean_err=2.54e-04; 67 tests |

**Conclusion:** `S3XS1_KK_BRIDGE_SUPPORTED_ROBUST` (descriptive only).
Spin structure fork unresolved (m∈ℤ vs m∈ℤ+1/2); no selection made.

### AV-1 / AV-1c′: Radial Dictionary ✅ COMPLETE

- AV-1a/b: φ₁₁ global argmax, 5-term residual 2.9%
- AV-1c′: sparse H-T1 killed — see `null_results/20260610-ht1-sparse-bilinear.md`
- P1/P2: boundary cos-exponent obstruction + f^(φ) necessity both VERIFIED

---

## Active Track: LAMBDA-B5

### LAMBDA-B5 G0 ✅ STRUCTURAL_SPLIT_REQUIRED

Invariant one-forms ξ̃/ξ̃′ are NOT in span(E_i/E′_i).
Dereli-style matching impossible by tuning c_i^I.
Required form: V = λ_geom·V_ω + Σc_i·V_modes.
λ total NOT fixed; λ_geom conditionally canonical (pending Tom Q3).

Full record: `experiments/20260611-lambda-b5-structural-split/`

### LAMBDA-B5 G2 — **NEXT GATE** (not started)

**Hypothesis:** cot(2α) term in frame is a frame artifact, not physics.
Mechanism: tan α − cot α = −2cot(2α); Hopf ω₁₂=tanα·e², ω₁₃=−cotα·e³
vs invariant form ω_ij=ε_ijk σ_k/ρ.
Candidate answer to Tom Q2.
Pre-registration: not yet written — write claim first, then implement.

Note: G1/G3 only if G0/G2 are clean.

---

## Pending Items

### Tom Lawrence — awaiting reply

4 questions sent 2026-06-09 (LinkedIn). Status: no reply yet.

Questions:
1. Is replacement basis U(α,θ,θ̃) the correct spinor frame for S³?
2. cot(2α) — expected to vanish with correct SO(4) spinor basis?
3. λ — expected free at S³ stage, or fixed by S³×S⁶/action/gauge?
4. α convention and S³ measure sin(α)cos(α)dα correct?

**Constraint:** do NOT write to Tom until he responds.

### BG-GATE §4 — Phase 3 entry

Geometry discrimination. Awaiting Tom Lawrence reply.

### P14B — S³ normalization robustness

After Tom confirms replacement basis.

### preserve/tom-s3-p5-p14-scaffold

P5–P14 scaffold on preserve branch (191 tests). Re-audit complete
(`reports/P5_P14_REAUDIT_REPORT.md`). Do NOT merge preserve→main without
explicit audit/cherry-pick decision.

---

## Null Results

| ID | Date | Verdict | Slug |
|---|---|---|---|
| 20260610-ht1-sparse-bilinear | 2026-06-10 | **REJECT** | Boundary cos-exponent mismatch blocks sparse bilinear reconstruction |

Retry condition: do NOT retry with bigger dicts. AV-2 showed the correct path
(cross-term φ·g, not diagonal φ·φ).

---

## Hard Constraints (non-negotiable)

```
λ = FREE_COUPLING_PARAMETER           — never fixed, never claimed
research_only = yes                   — no physical promotion
S³×S¹_solved = no                     — KT-3 PASS ≠ old problem resolved
tom_ansatz → "solved"                 — FORBIDDEN PHRASING
preserve → main merge                 — only via explicit audit/cherry-pick
write to Tom Lawrence                 — only after his reply to 4 questions
```

---

## Branch Map

| Branch | Status | Contains |
|---|---|---|
| `main` | **current, HEAD** | v0.2.0 + AV-2 + BG-H1 + lambda-B5-G0 — 415 tests |
| `preserve/tom-s3-p5-p14-scaffold` | stable | P5–P14, V-operator, lambda no-go — 191 tests |
| `research/av2-*` | merged to main | AV-2 G2/E1/E2 research branches |
| `research/bg-h1-*` | merged to main | BG-H1 research branches |
| `research/bg-h1-preregistration` | merged to main | BG-H1 pre-reg |

---

## Key File Index

| File | Role |
|---|---|
| `.claude/memory/activeContext.md` | Authoritative current focus + next steps |
| `tom_s3_spinor_toy/reference_spinor_harmonics.py` | `phi_nl_hopf` — upper component (C-H eq 3.25) |
| `tom_s3_spinor_toy/discrete_radial_dirac_proxy.py` | `g_nl_hopf` (eq 3.27), E0 gate |
| `tom_s3_spinor_toy/av1c_prime_cross_bilinear.py` | AV-1c′ kill result; P1/P2 |
| `tom_s3_spinor_toy/tests/test_ch_first_order_system.py` | C-H eqs regression (24 tests, G1) |
| `experiments/20260610-spinor-geometry-pivot-v0.2.0/` | AV-1, AV-2 claims, reports, source registers |
| `experiments/20260610-bg-h1-s3xs1-bridge/` | BG-H1 claims, reports, decision |
| `experiments/20260611-lambda-b5-structural-split/` | Lambda-B5 G0 results |
| `null_results/` | REJECT entries + INDEX |
| `reports/ITEM40_ALPHA_RADIAL_DICTIONARY_STATUS.md` | Item 40 ladder |
| `references/camporesi_higuchi_grqc9505009.pdf` | Primary source — C-H 1996 |

---

## Historical Checkpoints (useful for reconstruction, not for planning)

| Date | Summary covers | Status |
|---|---|---|
| 2026-06-10 (session 1) | E0, KT-3, NC-2, HA-4, v0.2.0 pivot | Historical |
| 2026-06-10 (session 2) | AV-1, AV-1c′, AV-2 G0 | Historical |
| 2026-06-10 (session 3) | AV-2 G1–E2 COMPLETE, BG-H1 complete, lambda-B5-G0 | **Most recent before this sync** |
