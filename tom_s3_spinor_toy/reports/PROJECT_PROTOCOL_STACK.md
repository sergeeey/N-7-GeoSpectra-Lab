# Project Protocol Stack

Date: 2026-06-08

## Purpose

This document defines the always-on research operating stack for the project.
It is not a research gate and does not change any frozen gate status.

The goal is to prevent scope inflation, fake-pass behavior, silent repair, and
premature promotion of scaffold-level evidence into physical claims.

## Always-On Stack

### 1. Scope Fence / Non-Promotion Discipline

Use before any interpretation of a passed gate.

- Verified smoke/scaffold evidence does not imply physical promotion.
- `runtime = research_only`
- `safe_for_runtime = no`
- `selection_rules = smoke_only`
- `promotion = forbidden_without_separate_gate`

### 2. HD-MAVP

Use to decompose any claim into hypotheses, claims, assumptions,
dependencies, unknowns, risks, and falsification conditions.

- Required for any claim that could be promoted.
- Produces the weakest-link analysis for the next gate.
- Forces explicit blocks on promotion when unknowns remain.

### 3. LLM-MCM Gate Selection

Use whenever a next gate must be chosen.

- Selects the next gate by value, cost, risk, and testability.
- Prefers small, falsifiable, fence-compatible steps.
- Rejects gates that are “interesting” but not information-dense.

### 4. Algebra Scaffold Verification

Use for coordinate, matrix, tensor, Pauli/Clifford, parity, and basis-order
conventions.

- Coordinates first.
- Matrix convention second.
- Basis ordering and factor order explicit.
- Smoke actions stay smoke actions.

### 5. Selection-Rule Audit

Use for matrix-element scaffolds and any V-like selection pattern.

- Distinguish tensor-product-derived structure from physical selection rules.
- Keep exact coefficients normalization-dependent unless separately proven.
- Do not promote selection rules without a dedicated promotion gate.

### 6. Mathematical Source Verification

Use for every nontrivial formula, normalization, spectrum relation, or
Wigner/CG statement.

- Formula must have a source or a local derivation.
- Convention must be stated explicitly.
- Domain of applicability must be bounded.

### 7. Red Team / No Fake-Pass

Use before any gate is declared closed.

- Attack basis ordering.
- Attack normalization.
- Attack phase conventions.
- Require negative controls.
- Reject silent repair and ad hoc expectation changes.

### 8. CI / Regression Bundle

Use whenever code, convention, scaffold, or source basis changes.

- Targeted test for the current gate.
- Smoke bundle for the nearest dependencies.
- Regression bundle for the frozen chain.
- Record exact command and result.

### 9. ReportOps / ActiveContext Discipline

Use after every gate, passed or failed.

- If it is not in the report and activeContext, it is not project state.
- Keep old gates intact.
- Record implemented vs verified separately.
- Include exact pytest command and next gate.

### 10. Gate-Based TDD

Use as the implementation discipline for the current gate.

- RED -> GREEN -> REFACTOR.
- One gate, one claim family, one smallest sufficient verification bundle.
- Do not widen scope while the gate is still open.

### 11. Convention / Normalization Registry

Use whenever a gate depends on basis ordering, factor order, generator
normalization, phase convention, radius convention, multiplicity convention,
or external oracle conventions.

- Freeze conventions before interpreting results.
- Record drift explicitly.
- Block promotion on any convention mismatch until a repair gate resolves it.
- Treat the registry as a fence layer, not a research gate.

## Current Project Fence

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

## Current Verified Position

```yaml
verified_claims:
  - gate: P11_EXTERNAL_ORACLE_MATRIX_ELEMENT_DERIVATION
    status: passed
    checked: external Wigner/CG oracle matches frozen P9/P10 scaffold pattern for k_max = 1, 2
  - gate: P12_MATRIX_ELEMENT_DERIVATION_ROBUSTNESS_AUDIT
    status: passed
    checked: P11 pattern is stable under tested basis-ordering, phase, normalization, and k_max extension stress tests
```

## Operating Order

Recommended order for future gates:

1. Scope Fence / Non-Promotion Discipline
2. HD-MAVP
3. Gate Selection
4. Algebra Scaffold Verification
5. Mathematical Source Verification
6. Red Team / No Fake-Pass
7. CI / Regression Bundle
8. ReportOps / ActiveContext Discipline
9. Convention / Normalization Registry
10. Gate-Based TDD

## Notes

- This stack is always-on.
- It does not replace domain-specific gates.
- It only controls how results are interpreted, documented, and promoted.
