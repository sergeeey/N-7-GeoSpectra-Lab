# Anti-Hallucination Audit — Executive Status Verification

**Date:** 2026-06-11
**Trigger:** External audit raised 7 evidence questions + validation-theater risk estimate (35–45%)
**Method:** Every claim re-verified by tool THIS session (git, pytest, live python reproduction, grep, git-show). No memory claims.
**HEAD at audit:** `ea3d79c` (main = origin/main)

---

## Master Table: claim → evidence → independence → reproduction → blocker

| # | Claim | Evidence (tool, this session) | Independence level | Reproduction command | Remaining blocker |
|---|---|---|---|---|---|
| 1 | Executive status commit | `ea3d79c` 2026-06-11, main = origin/main [VERIFIED-git] | n/a | `git log -1; git status -sb` | none |
| 2 | 415 passed, 2 skipped | Re-run this session: **415 passed, 2 skipped, 14.76s** [VERIFIED-pytest] | self-test | `python -m pytest tests/ -q` | none |
| 3 | φ₀₀=cosα, g₀₀=sinα | C-H gr-qc/9505009 **eq 3.25** (φ_nl) + **eq 3.27** (ψ_nl), pp. 8–10; n=l=0, N=3, α=θ/2 ⇒ φ₀₀=cos(θ/2), ψ₀₀=sin(θ/2). Local PDF exists (410 KB) [VERIFIED-read + ls] | **external source** (published paper, PDF on disk) + numerical cross-check (eq 3.28 ≤2.3e-15, eqs 3.29/3.30 FD ≤5e-7) | see `source_register_av2.md` | none — page/eq references recorded |
| 4 | BG-H1 E1: k₀=1.4999999561, max_err=2.93e-08 | **Reproduced bit-exact this session**: k₀=1.4999999561, max_err=2.927e-08 [VERIFIED-python] | analytic formula is G0-source-traced (C-H); discretization self-built | `python -c "...s3_ground_eigenvalue(4000)..."` (see below) | none |
| 5 | BG-H1 E2: frag_ratio 0.9958/0.9984, mean_err 2.532e-04/2.538e-04, PASS | **Full gate re-run this session — all 4 metrics bit-exact** [VERIFIED-python] | self-test against own analytic gap; disorder model = KT-3 protocol | `python -c "...run_e2_gate()..."` | ⚠️ see Finding W1 |
| 6 | P5–P14 "VERIFIED after re-audit" | Evidence table EXISTS: `preserve:tom_s3_spinor_toy/reports/P5_P14_REAUDIT_REPORT.md` — file:line + marker per claim (F1–F6) [VERIFIED-git-show] | mixed — see Finding W2 | `git show preserve/tom-s3-p5-p14-scaffold:tom_s3_spinor_toy/reports/P5_P14_REAUDIT_REPORT.md` | W2 |
| 7 | P10 adds math? | **No — by its own text**: "Terminal review fence... No new V operator. No V-selection promotion"; `selection_rule_status=smoke_only` [VERIFIED-git-show] | n/a (fence, not result) | `git show preserve/...:.../P10_SELECTION_RULE_MATRIX_ELEMENT_REVIEW.md` | none — repo never claimed math content |
| 8 | SU(4)/Y_W derived? | **No — verdict is literally** `SU4_ALGEBRA_AUDIT_PASSED_WITH_NORMALIZATION_DEPENDENT_YW`; "[INFERRED] candidate Y_W remains normalization-dependent... does not promote" [VERIFIED-git-show] | n/a | `git show preserve/...:.../P7_SU4_HYPERCHARGE_GAUGE_BREAKING_AUDIT.md` | physical Y_W = requires_physical_input (Tom/S³×S⁶) |

### Reproduction commands (exact, run from repo root)

```bash
# E1 (reproduced 2026-06-11, matches bit-exact):
python -c "
import sys; sys.path.insert(0, '.')
from tom_s3_spinor_toy.bg_h1_e1_product_proxy import s3_ground_eigenvalue, gap_rel_error, E1_R_VALUES
k0 = s3_ground_eigenvalue(4000); print(k0)
print(max(gap_rel_error(k0, R, m1) for R in E1_R_VALUES for m1 in (1.0, 0.5)))"

# E2 (reproduced 2026-06-11, matches bit-exact):
python -c "
import sys; sys.path.insert(0, '.')
from tom_s3_spinor_toy.bg_h1_e2_disorder_proxy import run_e2_gate
print(run_e2_gate()['verdict'])"
```

---

## Independence Map (Q5)

| Result | External oracle | Self-test only |
|---|---|---|
| AV-2 E2 CG singlet = √2/2 | ✅ `sympy.physics.quantum.cg.CG` (independent library) | — |
| Jacobi radial modes φ_nl, ψ_nl | ✅ `scipy.special.eval_jacobi` + C-H PDF eqs 3.25/3.27 | — |
| E0 eigenvalue recovery 6.7e-7 | ✅ closed-form C-H eq 3.26 as oracle | discretization self-built |
| BG-H1 G0 cross-term cancellation | ✅ C-H PDF eqs 2.1/2.10/3.46-3.48 + **adversarial re-audit (4 verifiers, v1.1 after corrections)** | — |
| BG-H1 G1 D₄²=−(k²+p²)I₄ | symbolic identity, machine precision | partially self-referential (own Γ-matrices), but convention-pin tests wrong alternatives |
| BG-H1 E1/E2 δ(R) | analytic formula traced to C-H via G0 | numerics self-built |
| P13H coefficient 16π²ρ³/15 | ✅ sympy symbolic integration | — |
| KT-3/NC-2/E2 disorder | — | self-test (protocol pre-registered) |

---

## Findings — where the auditor is RIGHT (and what was done)

### W1: E2 kill condition is analytically unreachable [CONFIRMED]

**Gate classification (explicit):** E2 is a **consistency / robustness gate**, NOT a strong falsification gate for the product structure. This distinction must be used verbatim in any re-telling of BG-H1 results.

`fragility_ratio > 10` cannot fire: δ=f(k₀) is a deterministic function with |dδ/dk₀|<1, so ratio ≤ 1 by construction. **This was already documented in `e2_disorder_report.md` §Fragility Ratio Analysis** ("Kill condition (ratio > 10) cannot be triggered by this mechanism") — but it means E2's falsification power lives ONLY in:
- (b) mean_rel_error > 5% — real check (could fire if discretization broke under disorder), and
- (c) monotonicity — real check, and
- S³-sector robustness at W=0.5 itself.

**Status:** disclosed pre-existing limitation, now elevated to top-level audit finding. Cite E2 only as "consistency + S³ robustness gate"; never as strong product-structure falsification.

### W2: P13A–P13G upgrades are [VERIFIED-read] of status fields [CONFIRMED]
The re-audit table upgrades P13A–G from E:only → VERIFIED based on reading the modules' own status fields. This verifies **fence self-consistency**, not independent re-derivation of the math. Only P13H (pytest 3/3 + live sympy) and P14 (pytest 2/2 + lambda_fixed=False) have stronger evidence.

**Status:** acknowledged. Correct reading of the 34-map: P13A–G = "fence verified", P13H/P14 = "result reproduced".

### W3: No dedicated negative control in E2 [CONFIRMED, minor]
E1 has `run_negative_control_periodic_ground` (m=0 → δ₀=0 exactly). E2 has monotonicity checks but no injected-failure control (e.g., wrong-formula branch should FAIL the gate). G1 partially covers this via convention-pin (wrong conventions ±i(p±k) rejected).

---

## Risk Re-Assessment (post tool-verification)

| Risk (auditor estimate) | Post-audit estimate | Basis |
|---|---|---|
| Full hallucination: 20–30% | **<5%** | all key numbers reproduce bit-exact; sources on disk with page/eq refs; 415 tests re-run |
| Overclaim in re-telling: 60–70% | **unchanged — real risk** | mitigations: this table + fence language; P13A–G must be quoted as "fence verified" |
| Self-referential validation: 40–50% | **~20%** | external oracles at key nodes (sympy CG, scipy Jacobi, C-H PDF, 4-verifier G0 re-audit); residual: E1/E2 numerics self-built (W1, W3) |

## What still depends on Tom (Q7)

1. Replacement basis U(α,θ,θ̃) correctness → tom_ansatz≈φ₁₁ **interpretation in his convention**
2. cot(2α) vanishing in correct SO(4) basis
3. λ fixing path (S³×S⁶ / action / gauge) → until then λ = FREE_COUPLING_PARAMETER
4. α convention + measure sin(α)cos(α)dα → affects all inner-product statements
5. Spin structure on S¹ (periodic vs antiperiodic) → BG-H2 candidate gate (feasibility only, no physics selection)

## Negative Control Backlog — not yet implemented

The following negative controls would strengthen E2 and related gates. None are required for
current BG-H1 PASS status (all gates passed their pre-registered conditions), but are flagged
here as explicit gaps for Phase 3 review.

| # | Control | What it tests | Gate it strengthens |
|---|---|---|---|
| NC-E2-1 | **Wrong spin structure** — inject m∈ℤ+½ into periodic gate, m∈ℤ into antiperiodic gate | E2 must distinguish structures, not collapse them | E2 |
| NC-E2-2 | **Wrong k₀** — replace S³ ground eigenvalue with k₀=1.0 or k₀=2.0 | δ(R) formula must fail if S³ ground state is wrong | E1 + E2 |
| NC-E2-3 | **Wrong α mapping** — use θ instead of α=θ/2 as argument to C-H formulas | Catches coordinate convention errors in radial modes | G0/E1 |
| NC-E2-4 | **Convention flip** — negate the KK quadrature (λ²(S³×S¹) = (n+3/2)² − (m/R)²) | E1 gap should spike for this wrong formula | G1/E1 |
| NC-E2-5 | **Corrupted operator** — zero out off-diagonal Γ blocks in product Dirac before squaring | D₄² should fail the k²+p² identity | G1 |

**Priority:** NC-E2-5 > NC-E2-4 > NC-E2-1. These are backlogged, not blocking current Phase 3 design.

---

## Gate Failure Scope Table

Answers: "Could each result have come out differently if the physics were wrong?"

| Result | Can it fail? | Failure mechanism | Current status |
|---|---|---|---|
| G0: cross-terms vanish | ✅ yes — if product structure wrong | Non-zero off-diagonal in Γ-commutator; falsified individually (|X|≈13.9) | PASS v1.1 (both conditions required jointly) |
| G1: D₄²=−(k²+p²)·I₄ | ✅ yes — if eigenvalue formula wrong | max_err spikes above machine precision; convention-pin rejects ±i(p±k) forms | PASS (max_err=0.0, machine precision) |
| E1: δ(R) max_err=2.93e-08 | ✅ yes — if FD discretization inconsistent with analytic gap | max_err > 1e-2 kill fires | PASS (margin 340 000×) |
| E2: mean_err < 5% | ✅ yes — if disorder breaks gap more than S³-sector predicts | mean_err > 0.05 kill fires | PASS (max 2.54e-04, margin 200×) |
| E2: frag_ratio < 10 | ⚠️ analytically unreachable — ratio ≤ 1 always | δ=f(k₀) deterministic; kill condition by construction unreachable | PASS (W1 — cited as consistency gate only) |
| E2: monotonicity | ✅ yes — stochastic disorder could break monotone ordering | `_monotone_decreasing` assertion fails | PASS (30 seeds, both structures) |
| P13A–G status fields | ✅ fence-consistency only | A different status field value would be caught | READ-VERIFIED (fence); NOT independent re-derivation |
| P13H coefficient 16π²ρ³/15 | ✅ yes — if sympy integration wrong | Coefficient mismatch vs pre-registered | PASS (pytest 3/3 + live sympy) |
| P14 lambda=FREE | ✅ yes — if S³-only does fix λ | lambda_fixed=True would fire promotion | PASS (lambda_fixed=False, pytest 2/2) |
| P10 selection rule | n/a — terminal fence only | Not a math result; no fail mode applies | FENCE (smoke_only, no new V operator) |

---

## Verdict

```
ENGINEERING SCAFFOLD:      confirmed reproducible (bit-exact reproduction, 415 tests)
SOURCE TRACEABILITY:       confirmed (C-H PDF on disk, eq-level register)
PHYSICAL PROOF OF THEORY:  not claimed anywhere in repo — fence machine-enforced
VALIDATION THEATER:        not detected; 3 real weaknesses (W1-W3) disclosed above
E2 GATE SCOPE:             consistency/robustness gate — NOT strong falsification gate (explicit)
NEGATIVE CONTROLS:         5 backlogged (NC-E2-1 to NC-E2-5), none blocking BG-H1 PASS
```
