# PX Known Limitations and Next Evidence Requirements

Date: 2026-06-08

## Purpose

This document is not a gate. It records what the current P11/P12 evidence
does and does not establish, and what kind of new evidence would be required
for any future promotion review.

## Verified Claims

```yaml
verified_claims:
  - gate: P11_EXTERNAL_ORACLE_MATRIX_ELEMENT_DERIVATION
    checked: external Wigner/CG oracle matches the frozen P9/P10 scaffold pattern for k_max = 1, 2
    evidence: pytest bundle passed
    status: passed
  - gate: P12_MATRIX_ELEMENT_DERIVATION_ROBUSTNESS_AUDIT
    checked: the P11 pattern is robust on tested axes
    evidence: pytest bundle passed
    status: passed
```

## Not Verified

```yaml
not_verified:
  - physical V-operator formula
  - exact physical coefficient normalization
  - physical V-selection rules
  - Standard Model reproduction
  - fermion generation claim
  - runtime safety
  - universality beyond tested conventions and k_max values
```

## Scope Fence

This document records only the current scaffold-level and oracle-level state.

```text
runtime = research_only
safe_for_runtime = no
selection_rules = smoke_only
promotion = forbidden_without_separate_gate
```

This document does not verify:

```text
- physical interpretation
- runtime safety
- Standard Model reproduction
- full selection-rule promotion
- claims outside current scaffold
```

## Current Status

```text
P11 = external oracle matched frozen scaffold
P12 = robustness audit passed on tested axes
V-selection rules = smoke_only
physical V-operator = not established
```

## Next Evidence Requirements

A promotion review would require a new explicit physical operator formula and
its own dedicated gate. Minimum requirements:

```text
- explicit V operator formula candidate
- failure condition
- negative controls
- basis-ordering check
- normalization check
- phase-convention check
- Hermiticity check
- regression bundle
```

Without that new operator formula, the correct next step is to stop at the
current limitation boundary.

