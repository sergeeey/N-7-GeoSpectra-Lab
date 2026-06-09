# Protocol: Scope Fence / Non-Promotion Discipline + HD-MAVP

Date: 2026-06-08

## Purpose

This protocol is an always-on guardrail for the S3/S6/SU4 research pipeline.
It prevents smoke-test or scaffold-level evidence from being promoted into
physical claims, runtime-safety claims, or selection-rule promotion.

This is not a research gate. It does not change any frozen gate status.

## Verified Claims

```yaml
verified_claims:
  - gate: P11_EXTERNAL_ORACLE_MATRIX_ELEMENT_DERIVATION
    checked: external Wigner/CG oracle matches the frozen P9/P10 scaffold pattern
    evidence: pytest passed for k_max = 1, 2
    status: passed
  - gate: P12_MATRIX_ELEMENT_DERIVATION_ROBUSTNESS_AUDIT
    checked: the P11 pattern is stable under tested basis-ordering, phase, normalization, and k_max extension stress tests
    evidence: pytest passed for k_max = 1, 2, 3
    status: passed
```

## Not Verified

```yaml
not_verified:
  - physical V-operator formula
  - physical V-selection-rule promotion
  - Standard Model reproduction
  - fermion generation claim
  - runtime safety
  - exact coefficient universality across all conventions
```

## Scope Fence

This protocol verifies only:

```text
- smoke-tested scaffold compatibility
- external-oracle pattern matching
- robustness classification under tested conventions
- explicit non-promotion discipline
```

This protocol does not verify:

```text
- physical interpretation
- runtime safety
- Standard Model reproduction
- full selection-rule promotion
- claims outside current scaffold
```

Current status:

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

## Classification Levels

```text
LEVEL 0: code exists
LEVEL 1: smoke test passed
LEVEL 2: scaffold invariant passed
LEVEL 3: external oracle matched
LEVEL 4: robustness audit passed
LEVEL 4.5: external oracle + robustness audit passed, but no explicit physical operator
LEVEL 5: physical interpretation supported by explicit derivation
LEVEL 6: runtime-safe promotion after separate promotion gate
```

## Forbidden Promotion Language

Replace any of the following with scoped language unless a separate promotion
gate has passed:

```text
proved
доказано
полностью подтверждено
physical rule established
Standard Model reproduced
safe for runtime
production ready
V-selection promoted
```

Preferred scoped language:

```text
smoke-tested
scaffold-compatible
matches frozen pattern
research-only
requires robustness audit
normalization-dependent
phase-dependent
basis-ordering-dependent
```

## Promotion Rule

If promotion is desired, create a separate promotion gate with:

```text
- explicit claim under test
- failure condition
- independent evidence
- robustness audit
- negative controls
- regression bundle
```

## Application to Current Project

P11 and P12 are strong evidence for a matrix-element scaffold and an external
oracle match, but they do not justify V-selection promotion. The current
project fence remains:

```text
runtime = research_only
safe_for_runtime = no
V-selection rules = smoke_only
```

